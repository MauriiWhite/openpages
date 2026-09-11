"""Del HTML de IBM Documentation a Markdown. Determinista, sin modelo.

El HTML que sirve el API es DITA compilado y envuelto en clases de Carbon Design System.
Eso es una suerte: la semántica original sigue ahí, en los nombres de clase
(`uicontrol`, `codeph`, `filepath`, `cmd`, `step`, `notetitle`, `tablecap`), y se puede
traducir a Markdown sin adivinar nada. Lo que se pierde si uno toma solo el texto visible
es justo eso: qué era un control de la interfaz y qué era una ruta de archivo.

Decisiones medidas sobre el corpus completo (2.466 temas, 19 MB de HTML, 2026-09-11):

  - **`<aside>` se descarta entero.** Son 2.428 bloques de "Tema principal / Subtemas":
    navegación generada, no contenido. La jerarquía ya está en el índice, y repetirla en
    cada archivo la duplicaría 2.466 veces.
  - **`rowspan` no existe.** Cero ocurrencias en las 523 tablas del corpus, así que no hay
    una malla que rellenar. `colspan` sí, 18 veces, y se rellena con celdas vacías.
  - **Las tablas traen `<th>` de verdad.** 1.300 celdas de encabezado en 523 tablas: acá
    sí se promueve la primera fila, al revés que en un corpus sin `<thead>`.
  - **Los `<h1>` no van al cuerpo.** Hay exactamente uno por tema y es su título; queda
    como metadato para que `export` lo coloque al nivel que le toque dentro del archivo
    agrupado. Los `<h2>`…`<h4>` internos se normalizan a niveles relativos (1, 2, 3) por
    lo mismo.
  - **Las imágenes apuntan a ibm.com.** Lo que el corpus garantiza de una figura es su
    procedencia; copiarla localmente no la hace más verificable y el destinatario de este
    Markdown no lee imágenes. El `alt` en español sí se conserva, que es lo que un modelo
    puede leer.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser

from . import HOST, Node

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "param", "source", "track", "wbr"}

# Subárboles que no son contenido. `aside`/`nav` son la navegación generada;
# `svg` son los iconos de Carbon; el botón de copiar no tiene texto pero sí un hueco.
DROP_TAGS = {"aside", "nav", "svg", "button", "script", "style", "noscript"}
DROP_CLASSES = {"docs--copy-btn", "familylinks", "cds--inline-notification__icon"}

BLOCK = {"p", "div", "section", "article", "ul", "ol", "dl", "li", "dt", "dd", "table",
         "thead", "tbody", "tr", "td", "th", "caption", "colgroup", "pre", "figure",
         "figcaption", "blockquote", "iframe", "h1", "h2", "h3", "h4", "h5", "h6"}

# Clases DITA que marcan texto monoespaciado. Van a `` `código` `` porque eso es lo que
# eran en el original: un nombre de archivo, una variable, una orden, un valor literal.
CODE_CLASSES = {"codeph", "filepath", "varname", "cmdname", "parmname", "apiname",
                "systemoutput", "userinput", "msgnum", "msgph", "option", "synph", "sep"}
# Clases DITA que marcan la interfaz. En la convención de IBM van en negrita.
# `menucascade` NO va acá: envuelve `uicontrol`s que ya van en negrita, y anidarlos
# produce `****Aplicaciones** > …`, que GFM no renderiza como negrita sino como literal.
BOLD_CLASSES = {"uicontrol", "wintitle", "notetitle", "ibm-bold", "tablecap", "sectiontitle"}

NOTE_LABEL = {"warning": "Aviso", "error": "Atención", "info": "Nota"}

# El HTML de IBM no declara el lenguaje de sus 1.813 bloques de código: todos son
# `<pre class="codeblock">` a secas. La etiqueta se deduce, y solo cuando la señal es
# inequívoca —una etiqueta equivocada colorea mal, pero una ausente deja al modelo sin
# saber si está mirando SQL o una línea de consola—. Sin señal clara, no se etiqueta.
LANGUAGES = (
    ("xml", re.compile(r"^\s*(<\?xml|<!DOCTYPE|</?[a-zA-Z][\w:.-]*(\s+[\w:.-]+=|\s*/?>))")),
    ("json", re.compile(r"^\s*[{\[][\s\S]*\"\s*:")),
    ("sql", re.compile(r"^\s*(SELECT|INSERT\s+INTO|UPDATE\s+\w+\s+SET|DELETE\s+FROM|CREATE\s+"
                       r"(TABLE|INDEX|OR\s+REPLACE)|ALTER\s+(TABLE|SESSION|SYSTEM)|GRANT\s|DROP\s+"
                       r"(TABLE|INDEX)|COMMIT\b)", re.IGNORECASE | re.MULTILINE)),
    ("java", re.compile(r"^\s*(package\s+[\w.]+;|import\s+[\w.]+;|public\s+(class|interface|static))",
                        re.MULTILINE)),
    ("bat", re.compile(r"^\s*(@echo|set\s+\w+=|[A-Za-z]:\\|\w+\.(cmd|bat)\b)", re.MULTILINE)),
    ("bash", re.compile(r"^\s*(#!/|sudo\s|export\s+\w+=|\./|\w+\.sh\b|chmod\s|su\s+-\s)",
                        re.MULTILINE)),
    ("properties", re.compile(r"\A(?:[\w.$-]+\s*=[^\n]*\n?){2,}\Z")),
)


def language(code: str) -> str:
    """La etiqueta de lenguaje de un bloque, o cadena vacía si no hay señal clara."""
    for name, pattern in LANGUAGES:
        if pattern.search(code):
            return name
    return ""

LAST_MODIFIED = re.compile(r"(\d{4}-\d{2}-\d{2})")
# El tipo DITA del tema, que IBM deja en la clase del cuerpo. Distingue lo que se explica
# de lo que se ejecuta: un `task` es una secuencia de pasos que hay que devolver entera.
BODY_KIND = re.compile(r'<div class="body (\w+)"')
KIND = {"conbody": "concepto", "taskbody": "tarea", "refbody": "referencia"}
# Cuenta tablas. Va anclado con `^\s*` y no a `\n|`: una tabla dentro de un `<li>` sale
# indentada, y sin la holgura no se contarían 141 de las 523 del corpus.
TABLE_SEPARATOR = re.compile(r"^[ \t]*\|( --- \|)+[ \t]*$", re.M)


@dataclass
class Element:
    tag: str
    attrs: dict[str, str]
    children: list = field(default_factory=list)

    @property
    def classes(self) -> set[str]:
        return set((self.attrs.get("class") or "").split())

    def text(self) -> str:
        return "".join(c if isinstance(c, str) else c.text() for c in self.children)

    def find(self, tag: str):
        for child in self.children:
            if isinstance(child, Element):
                if child.tag == tag:
                    return child
                found = child.find(tag)
                if found is not None:
                    return found
        return None


class Tree(HTMLParser):
    """HTML a árbol. `html.parser` no cierra las etiquetas vacías por su cuenta y este
    HTML las escribe sin barra (`<img src=…>`), así que se cierran acá."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Element("#root", {})
        self._stack = [self.root]

    def handle_starttag(self, tag: str, attrs) -> None:
        element = Element(tag, {k: (v or "") for k, v in attrs})
        self._stack[-1].children.append(element)
        if tag not in VOID:
            self._stack.append(element)

    def handle_startendtag(self, tag: str, attrs) -> None:
        self._stack[-1].children.append(Element(tag, {k: (v or "") for k, v in attrs}))

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self._stack) - 1, 0, -1):
            if self._stack[index].tag == tag:
                del self._stack[index:]
                return
        # Un cierre sin apertura: HTML mal formado. Se ignora en vez de desarmar la pila.

    def handle_data(self, data: str) -> None:
        self._stack[-1].children.append(data)


def _dropped(node: Element) -> bool:
    return node.tag in DROP_TAGS or bool(node.classes & DROP_CLASSES)


def _absolute(url: str) -> str:
    """Los enlaces del API son relativos a ibm.com. Se absolutizan porque este Markdown se
    lee fuera del sitio: un `/docs/es/…` suelto no lleva a ninguna parte."""
    if url.startswith("//"):
        return f"https:{url}"
    if url.startswith("/"):
        return f"https://{HOST}{url}"
    return url


def _squash(text: str) -> str:
    return re.sub(r"[ \t\n\r]+", " ", text.replace("\xa0", " "))


# -- en línea ---------------------------------------------------------------


# Texto que parece una etiqueta y no lo es. Son 139 en el corpus —`<OP_HOME>`,
# `<server_name>`, `<ruleSet>`— escritas así por IBM en prosa corriente. Sin escapar, un
# renderizador de Markdown se las traga como HTML y el marcador desaparece de la página.
TAGLIKE = re.compile(r"<(?=[a-zA-Z/])")
PILL = re.compile(r"/pill_[a-z_]+\.svg$")


def inline(nodes: list, cell: bool = False, marks: frozenset = frozenset()) -> str:
    """Contenido en línea a Markdown.

    Con `cell`, los saltos van como `<br>`: una tabla Markdown vive en una línea y un
    salto dentro de una celda la parte en dos.

    `marks` lleva el énfasis ya abierto más arriba. Sin él, un `<strong>` que contiene un
    `uicontrol` —el original los anida— sale como `**Tipo nuevo: **Amenaza****`, que GFM
    imprime con los asteriscos a la vista en vez de en negrita.
    """
    out = []
    for node in nodes:
        if isinstance(node, str):
            out.append(TAGLIKE.sub(r"\\<", _squash(node)))
            continue
        if _dropped(node):
            continue
        out.append(_inline_element(node, cell, marks))
    return "".join(out)


def _wrap(node: Element, mark: str, cell: bool, marks: frozenset) -> str:
    if mark in marks:
        return inline(node.children, cell, marks)
    inner = inline(node.children, cell, marks | {mark}).strip()
    return f"{mark}{inner}{mark}" if inner else ""


def _inline_element(node: Element, cell: bool, marks: frozenset) -> str:
    tag, classes = node.tag, node.classes

    if tag == "br":
        return "<br>" if cell else "  \n"
    if tag == "img":
        alt = _squash(node.attrs.get("alt", "")).strip()
        source = node.attrs.get("src", "")
        # Las 922 «píldoras» de aplicabilidad (`pill_on_prem.svg`, `pill_on_cloud.svg`)
        # no son figuras: son el rótulo que dice a qué despliegue aplica el tema, y el
        # dato está en su texto alternativo. Como imagen, 773 temas del corpus abren con
        # un enlace a un SVG en vez de con la palabra que responde «¿esto aplica a la
        # nube?». Se emite el rótulo.
        if PILL.search(source):
            return alt
        return f"![{alt}]({_absolute(source)})"
    if tag == "a":
        text = inline(node.children, cell, marks).strip()
        href = node.attrs.get("href", "")
        # Un `#ancla` apunta a un `id` del HTML de IBM que este Markdown no conserva:
        # queda el texto, que es lo que dice algo, y no un enlace que no lleva a ninguna
        # parte.
        if href.startswith("#"):
            return text
        return f"[{text}]({_absolute(href)})" if href and text else text
    if tag in ("code", "kbd", "samp", "tt", "var") or classes & CODE_CLASSES:
        inner = _squash(node.text()).strip()
        return f"`{inner}`" if inner else ""
    if tag in ("strong", "b") or classes & BOLD_CLASSES:
        return _wrap(node, "**", cell, marks)
    if tag in ("em", "i", "cite", "dfn"):
        return _wrap(node, "*", cell, marks)
    if tag == "sub":
        return f"_{{{inline(node.children, cell, marks).strip()}}}"
    if tag == "sup":
        return f"^{{{inline(node.children, cell, marks).strip()}}}"
    if tag == "q":
        return f"«{inline(node.children, cell, marks).strip()}»"
    # `abbr`, `span`, `abbr title=…` y el resto son transparentes: su texto ya dice lo que
    # hay que decir (`<abbr title="y, a continuación,"> &gt; </abbr>` es el `>` de un menú).
    return inline(node.children, cell, marks)


# -- bloques ----------------------------------------------------------------


def blocks(nodes: list, level: int = 0) -> list[str]:
    """Contenido de bloque a una lista de bloques Markdown, ya separados."""
    out: list[str] = []
    buffer: list = []

    def flush() -> None:
        if buffer:
            text = inline(buffer).strip()
            if text:
                out.append(_escape_block(text))
            buffer.clear()

    for node in nodes:
        if isinstance(node, str):
            buffer.append(node)
            continue
        if _dropped(node):
            continue
        if node.tag in BLOCK:
            flush()
            out.extend(_block_element(node, level))
        else:
            buffer.append(node)
    flush()
    return [b for b in out if b.strip()]


LEADING = re.compile(r"^([>#|]|\d+[.)]\s|[-+*]\s)")


def _escape_block(text: str) -> str:
    """Un párrafo que empieza por `>` o `#` se leería como cita o encabezado. Es lo único
    que hace falta escapar: GFM no interpreta `_` dentro de palabra ni `*` suelto."""
    return "\\" + text if LEADING.match(text) else text


def _indent(text: str, prefix: str = "  ") -> str:
    return "\n".join(prefix + line if line.strip() else line for line in text.split("\n"))


def _block_element(node: Element, level: int) -> list[str]:
    tag, classes = node.tag, node.classes

    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        text = inline(node.children).strip()
        if tag == "h1":
            return []  # El título del tema es metadato; lo coloca `export`.
        depth = min(int(tag[1]) - 1, 6)
        return [f"{'#' * depth} {text}"] if text else []

    if tag == "table":
        return _table(node)
    if tag in ("thead", "tbody", "colgroup", "caption", "tr", "td", "th"):
        return blocks(node.children, level)  # sueltos fuera de una tabla: transparentes

    if tag == "pre":
        code = node.text().replace("\xa0", " ").strip("\n")
        fence = "`" * max(3, *(len(m) + 1 for m in re.findall(r"`+", code)), 3)
        return [f"{fence}{language(code)}\n{code}\n{fence}"]

    if tag in ("ul", "ol"):
        return [_list(node, level)]
    if tag == "dl":
        return [_definitions(node, level)]

    if tag == "figure":
        return blocks(node.children, level)
    if tag == "figcaption":
        text = inline(node.children).strip()
        return [f"*{text}*"] if text else []

    if tag == "iframe":
        title = _squash(node.attrs.get("title", "")).strip() or "Vídeo"
        return [f"[{title}]({_absolute(node.attrs.get('src', ''))})"]

    if tag == "blockquote" or "note" in classes:
        inner = "\n\n".join(blocks(node.children, level))
        if not inner.strip():
            return []
        if "note" in classes:
            kind = next(
                (NOTE_LABEL[k] for k in NOTE_LABEL
                 if f"cds--inline-notification--{k}" in classes), None)
            if kind and not inner.lstrip().startswith("**"):
                inner = f"**{kind}:** {inner}"
        return [_indent(inner, "> ")]

    if node.attrs.get("id") == "lastModifiedDate":
        return []

    # `div`, `section`, `article`, `li`, `dt`, `dd` sueltos: transparentes. Toda la
    # maquetación de Carbon son `div` anidados y tratarlos como bloque propio metería
    # líneas en blanco donde el original no las tiene.
    return blocks(node.children, level)


def _list(node: Element, level: int) -> str:
    ordered = node.tag == "ol"
    items = [c for c in node.children if isinstance(c, Element) and c.tag == "li"]
    lines = []
    for index, item in enumerate(items, 1):
        marker = f"{index}. " if ordered else "- "
        body = "\n\n".join(blocks(item.children, level + 1)).strip()
        if not body:
            continue
        indented = _indent(body, " " * len(marker))
        lines.append(marker + indented[len(marker):])
    return "\n".join(lines)


def _definitions(node: Element, level: int) -> str:
    """Markdown no tiene listas de definición. Un ítem con el término en negrita y la
    definición anidada conserva el par y admite bloques dentro, que es lo que `<dd>`
    trae: tablas, listas y ejemplos, no solo una frase."""
    lines = []
    term: str | None = None
    bodies: list[str] = []

    def close() -> None:
        if term is None and not bodies:
            return
        # El término va en negrita salvo que ya venga marcado: 1.452 `<dt>` del corpus son
        # rutas de menú (`**Aplicaciones** > **Frecuentes** > …`) y envolverlas otra vez
        # da `****Aplicaciones**`, que GFM imprime con los asteriscos a la vista.
        head = "-" if term is None else f"- {term}" if term.startswith("**") else f"- **{term}**"
        joined = "\n\n".join(bodies).strip()
        lines.append(f"{head}\n\n{_indent(joined)}" if joined else head)

    for child in node.children:
        if not isinstance(child, Element):
            continue
        if child.tag == "dt":
            close()
            term, bodies = inline(child.children).strip(), []
        elif child.tag == "dd":
            # Un `<dt>` puede traer varios `<dd>` —"Valor predeterminado:", "Valores:"—
            # y son del mismo término. Cerrar en cada `<dd>` los partía en ítems sueltos,
            # el segundo sin término.
            body = "\n\n".join(blocks(child.children, level + 1)).strip()
            if body:
                bodies.append(body)
    close()
    return "\n\n".join(lines)


# Etiquetas de bloque que aparecen DENTRO de una celda. Medido sobre las 10.291 celdas del
# corpus: 2.775 `<p>`, 1.553 `<div>`, 216 `<ul>`, 25 `<dl>`, 1 `<ol>`. No hay ni un `<pre>`
# ni una tabla anidada, pero `pre` va igual para que un cambio de IBM no pierda el formato
# del código en silencio.
CELL_BLOCKS = {"p", "div", "section", "figure", "blockquote", "pre",
               "h1", "h2", "h3", "h4", "h5", "h6"}


def _cell(node: Element) -> str:
    """El contenido de una celda, con sus bloques separados.

    Una tabla Markdown vive en una línea, así que el único salto admitido dentro de una
    celda es `<br>`. Sin él, los 3.878 casos de bloque dentro de celda salían pegados:
    `<td>Tabla principal<p>Por ejemplo: …</p></td>` daba `Tabla principalPor ejemplo:` —
    una palabra que no existe, en el 37,7% de las celdas del corpus.
    """
    segments: list[str] = []
    buffer: list = []

    def flush() -> None:
        if buffer:
            text = inline(buffer, cell=True).strip()
            if text:
                segments.append(text)
            buffer.clear()

    for child in node.children:
        if isinstance(child, str):
            buffer.append(child)
            continue
        if _dropped(child):
            continue
        if child.tag in ("ul", "ol"):
            flush()
            # Una lista dentro de una celda no puede ser una lista Markdown: se marca con
            # viñetas y se separa con `<br>`, que es lo que un renderizador sí respeta.
            segments += [
                f"• {text}"
                for text in (
                    _cell(item) for item in child.children
                    if isinstance(item, Element) and item.tag == "li"
                )
                if text
            ]
        elif child.tag == "dl":
            flush()
            segments.append(_definitions(child, 0).replace("\n\n", "<br>").replace("\n", "<br>"))
        elif child.tag == "pre":
            flush()
            segments.append("`" + _squash(child.text()).strip() + "`")
        elif child.tag in CELL_BLOCKS:
            flush()
            text = _cell(child)
            if text:
                segments.append(text)
        else:
            buffer.append(child)
    flush()
    return "<br>".join(s for s in segments if s)


def _cells(row: Element) -> tuple[list[str], bool]:
    out: list[str] = []
    header = False
    for child in row.children:
        if not isinstance(child, Element) or child.tag not in ("td", "th"):
            continue
        header = header or child.tag == "th"
        text = _cell(child).strip().replace("|", "\\|")
        out.append(text)
        # `rowspan` no aparece ni una vez en las 523 tablas del corpus, así que no hay
        # malla que rellenar. `colspan` sí, 18 veces: se rellena con celdas vacías para
        # que la fila conserve su ancho y la tabla no se desalinee.
        out += [""] * (int(child.attrs.get("colspan", 1) or 1) - 1)
    return out, header


def _table(node: Element) -> list[str]:
    caption = node.find("caption")
    rows: list[tuple[list[str], bool]] = []
    for row in _descendants(node, "tr"):
        cells, header = _cells(row)
        if cells:
            rows.append((cells, header))
    if not rows:
        return []

    width = max(len(cells) for cells, _ in rows)
    rows = [(cells + [""] * (width - len(cells)), header) for cells, header in rows]

    # Las 523 tablas del corpus traen `<thead>` y 1.300 celdas `<th>`: acá el encabezado
    # es un encabezado de verdad y se promueve. Si alguna no lo trajera, se emite un
    # encabezado vacío antes que convertir un dato en un rótulo.
    head, body = (rows[0][0], [c for c, _ in rows[1:]]) if rows[0][1] else ([""] * width, [c for c, _ in rows])
    lines = ["| " + " | ".join(head) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines += ["| " + " | ".join(cells) + " |" for cells in body]

    out = []
    if caption is not None:
        text = inline(caption.children).strip().strip("*")
        if text:
            out.append(f"**{text}**")
    out.append("\n".join(lines))
    return out


def _descendants(node: Element, tag: str):
    for child in node.children:
        if isinstance(child, Element):
            if child.tag == tag:
                yield child
            else:
                yield from _descendants(child, tag)


# -- documento --------------------------------------------------------------


def parse_topic(html: str) -> dict:
    """Un tema a Markdown más sus metadatos.

    El `<h1>` y la fecha de última modificación salen del cuerpo y quedan como metadatos:
    el título porque `export` tiene que colocarlo al nivel que le toque dentro del archivo
    agrupado, y la fecha porque es de la página, no de su texto.
    """
    tree = Tree()
    tree.feed(html)
    root = tree.root

    heading = root.find("h1")
    title = inline(heading.children).strip() if heading is not None else ""

    modified = ""
    stamp = _find_by_id(root, "lastModifiedDate")
    if stamp is not None:
        found = LAST_MODIFIED.search(stamp.text())
        modified = found.group(1) if found else ""

    markdown = "\n\n".join(blocks(root.children)).strip()
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)

    kind = BODY_KIND.search(html)
    return {
        "title": title,
        "kind": KIND.get(kind.group(1) if kind else "", "contenedor"),
        "last_modified": modified,
        "markdown": markdown,
        "chars": len(markdown),
        "sha256": hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
        "figures": re.findall(r"!\[[^\]]*\]\((https://[^)]+)\)", markdown),
        "tables": len(TABLE_SEPARATOR.findall(markdown)),
    }


def _find_by_id(node: Element, wanted: str):
    for child in node.children:
        if isinstance(child, Element):
            if child.attrs.get("id") == wanted:
                return child
            found = _find_by_id(child, wanted)
            if found is not None:
                return found
    return None


def run() -> None:
    """Etapa: el caché a `documents.json`, con las invariantes antes de escribir.

    Dos fuentes de temas, no una: los que IBM lista en su índice y los que solo enlaza
    desde el texto. De los 86 enlazados, la mayoría resulta ser un tema que ya está bajo
    otro nombre de archivo —IBM renombró archivos al traducir— y se anota como **alias**,
    para que `export` reapunte esos 1.306 enlaces al tema de verdad en vez de dejarlos
    saliendo del paquete. Los que no calzan con ningún hash son contenido que el índice
    de IBM no lista y que no está en ninguna otra parte.
    """
    import json

    from . import DATA, cache_file, guide_of
    from .guard import enforce

    manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
    nodes = {k: Node(**v) for k, v in manifest["nodes"].items()}

    documents: dict[str, dict] = {}
    for topic_id, node in nodes.items():
        # La raíz es el producto, no un tema: su `href` devuelve un cuerpo vacío y su
        # título es el nombre del producto.
        path = cache_file(node.href)
        if node.depth == 0 or not path.exists():
            continue
        documents[topic_id] = {
            "topic_id": topic_id,
            "href": node.href,
            "label": node.label,
            "guide": node.guide,
            "depth": node.depth,
            "listed": True,
            **parse_topic(path.read_text(encoding="utf-8")),
        }

    by_sha = {d["sha256"]: tid for tid, d in documents.items()}
    aliases: dict[str, str] = {}
    extra = 0
    for href in manifest.get("extra", []):
        path = cache_file(href)
        if not path.exists():
            continue
        document = parse_topic(path.read_text(encoding="utf-8"))
        canonical = by_sha.get(document["sha256"])
        if canonical:
            aliases[href] = canonical
            continue
        topic_id = _extra_id(href, documents)
        documents[topic_id] = {
            "topic_id": topic_id,
            "href": href,
            "label": document["title"],
            "guide": guide_of(href),
            "depth": 2,
            "listed": False,
            **document,
        }
        by_sha[document["sha256"]] = topic_id
        extra += 1

    enforce(nodes, documents)
    (DATA / "documents.json").write_text(
        json.dumps(documents, ensure_ascii=False), encoding="utf-8"
    )
    (DATA / "aliases.json").write_text(
        json.dumps(aliases, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    chars = sum(d["chars"] for d in documents.values())
    print(f"  {len(documents)} topics ({extra} outside IBM's toc, {len(aliases)} aliases resolved)"
          f" -> {chars / 1e6:.2f} MB of Markdown, "
          f"{sum(d['tables'] for d in documents.values())} tables, "
          f"{sum(len(d['figures']) for d in documents.values())} figures")


def _extra_id(href: str, taken: dict) -> str:
    """El identificador de un tema que el índice no lista. IBM solo asigna `topicId` a lo
    que publica en su árbol, así que acá se deriva del nombre del archivo, que es lo único
    estable que tiene."""
    base = href.rsplit("/", 1)[-1].removesuffix(".html").replace("_", "-")
    topic_id = base
    suffix = 2
    while topic_id in taken:
        topic_id = f"{base}-{suffix}"
        suffix += 1
    return topic_id
