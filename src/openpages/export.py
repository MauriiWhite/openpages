"""Arma el entregable: una guía por archivo, con cada tema capaz de ubicarse solo.

`data/` es el área de trabajo —caché, manifiesto, documentos— y `output/` es lo único que
se le pasa a alguien. Esta etapa no transforma texto: coloca los temas ya convertidos en la
jerarquía del índice de IBM, resuelve los enlaces entre ellos y trae las figuras.

Cuatro decisiones, todas tomadas pensando en que el destinatario es un modelo:

  - **Una guía por archivo, no un capítulo.** Por capítulo eran 158 archivos. Ninguna
    ganancia: todo canal de ingesta trocea el documento igual, así que el número de
    archivos es un problema de administración, no de recuperación. Solo se parte cuando
    la guía pasa de `export.max_bytes`, y nunca por la mitad de un capítulo.
  - **Cada tema dice dónde está.** Bajo cada encabezado va su ubicación en el árbol y el
    enlace al original. Es lo que de verdad decide el rendimiento: cuando el canal corta
    un archivo de 700 KB, el trozo del medio tiene que seguir sabiendo de qué guía y de
    qué capítulo es. Sin eso, «Pulse Aceptar» no significa nada.
  - **Las figuras se copian al paquete.** MEDIDO: las URL de imagen de IBM responden 403
    a cualquier cliente que no venga de su sitio, así que un Markdown que las enlace las
    muestra rotas en todas partes. La copia local se ve; el enlace, no.
  - **Los enlaces internos apuntan al paquete.** Incluidos los 1.306 que IBM escribe
    contra el nombre inglés del archivo: se reapuntan al tema de verdad por su hash.
"""

from __future__ import annotations

import json
import math
import re
import shutil
import unicodedata
from collections import Counter
from datetime import date

from . import (CONFIG, DATA, IMAGES, LANG, OUTPUT, PRODUCT, SITE_URL, VERSION, Node,
               image_file, topic_url)

MAX_BYTES = CONFIG["export"]["max_bytes"]
PRODUCT_NAME = f"IBM OpenPages {VERSION}"
IMAGE_DIR = "imagenes"
IMAGE_SUFFIX = (".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp")

# Un destino del propio producto dentro del Markdown ya generado.
INTERNAL = re.compile(
    r"\]\(https://www\.ibm\.com/docs/[a-z]{2}/(" + re.escape(PRODUCT) + r"/[^)#]+)(#[^)]*)?\)"
)
# Coste en bytes de la cabecera de cada tema: encabezado, línea de ubicación y separaciones.
TOPIC_OVERHEAD = 260
# Palabras del cuerpo, para los términos propios de cada archivo. Sin dígitos: un año o un
# número de versión es frecuente y no dice de qué trata el archivo.
WORD = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{4,}")
# Lo que no cuenta como prosa: los bloques de código, el código en línea y los destinos de
# enlaces e imágenes. Sin recortarlos, la lista la encabezan `op_grc_admin` y los nombres
# de archivo de las capturas de pantalla, que no son términos del producto.
NOT_PROSE = re.compile(r"```.*?```|`[^`\n]*`|\]\([^)]*\)", re.DOTALL)
# Términos que se listan en la cabecera y veces que uno tiene que aparecer para contar. El
# mínimo evita que una errata que sale una vez encabece la lista del archivo.
TOP_TERMS = 14
MIN_TERM_HITS = 5
# Y en cuántos archivos, como mucho, puede aparecer para seguir siendo «propio». Sin este
# tope sobreviven `seleccione`, `pulse` y `clic`: están en dieciséis de los diecisiete, así
# que su peso inverso no llega a cero, pero no distinguen nada.
MAX_TERM_SPREAD = 0.6


def slug(text: str, limit: int = 60) -> str:
    """Un nombre de archivo a partir de un título en español. Sin tildes ni eñes: el
    entregable se copia a Windows, a SharePoint y a un índice de búsqueda, y cada uno
    normaliza el Unicode a su manera."""
    plain = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    plain = re.sub(r"[^a-zA-Z0-9]+", "-", plain).strip("-").lower()
    return plain[:limit].rstrip("-") or "sin-titulo"


def anchor(title: str, seen: dict[str, int]) -> str:
    """El ancla que GFM le da a un encabezado, con el mismo desempate: los títulos se
    repiten («Introducción» aparece decenas de veces) y el segundo lleva `-1`."""
    base = re.sub(r"[^\w\- ]", "", unicodedata.normalize("NFC", title.lower())).strip()
    base = base.replace(" ", "-")
    seen[base] = seen.get(base, -1) + 1
    return base if not seen[base] else f"{base}-{seen[base]}"


def _shift(markdown: str, levels: int) -> str:
    """Baja los encabezados del cuerpo tantos niveles. El cuerpo trae `#`…`###` relativos
    al tema; dentro del archivo agrupado tienen que quedar por debajo de su título. Se
    topan en 6 porque Markdown no tiene un séptimo nivel."""
    return re.sub(
        r"^(#{1,6}) ", lambda m: "#" * min(len(m.group(1)) + levels, 6) + " ", markdown, flags=re.M
    )


def run() -> None:
    manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
    documents = json.loads((DATA / "documents.json").read_text(encoding="utf-8"))
    aliases = json.loads((DATA / "aliases.json").read_text(encoding="utf-8"))
    nodes = {k: Node(**v) for k, v in manifest["nodes"].items()}
    root = next(k for k, n in nodes.items() if n.parent is None)

    # El nombre de cada guía, por su `topicId` y por su slug: `_pack` tiene el primero y
    # `_render` el segundo, y los dos escriben el mismo rótulo.
    for guide_id in nodes[root].children:
        _LABELS[guide_id] = nodes[guide_id].label
        _LABELS[nodes[guide_id].guide] = nodes[guide_id].label

    order = _reading_order(nodes, documents, root)
    files = _pack(order, documents)

    # Dónde queda cada tema. Se resuelve antes de escribir porque un tema puede enlazar a
    # otro que se escribe después.
    location: dict[str, tuple[str, str]] = {}
    for name, topics in files:
        seen: dict[str, int] = {}
        for topic in topics:
            location[topic] = (name, anchor(_title(documents, nodes, topic), seen))

    targets = {documents[t]["href"]: t for t in documents}
    targets.update({href: topic for href, topic in aliases.items()})

    terms = _terms(files, documents)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name, topics in files:
        (OUTPUT / name).write_text(
            _render(nodes, documents, name, topics, files, location, targets, terms[name]),
            encoding="utf-8",
        )

    _copy_images()
    _readme(nodes, documents, manifest, files, location, root, terms)
    _prompt(documents, files)

    total = sum((OUTPUT / name).stat().st_size for name, _ in files)
    copied = [f for f in (OUTPUT / IMAGE_DIR).rglob("*") if f.is_file()] \
        if (OUTPUT / IMAGE_DIR).exists() else []
    figures = (f"{len(copied)} figures copied ({sum(f.stat().st_size for f in copied) / 1e6:.0f} MB)"
               if copied else "figures linked to ibm.com")
    print(f"  {len(files)} files, {sum(len(t) for _, t in files)} topics, {total / 1e6:.2f} MB,"
          f" {figures} in {OUTPUT}")


def _stats(documents: dict, topics: list[str]) -> dict:
    """Lo que un modelo necesita para decidir si la respuesta está en este archivo."""
    kinds = Counter(documents[t].get("kind", "") for t in topics)
    applies = Counter()
    for topic in topics:
        applies.update(set(APPLIES.findall(documents[topic]["markdown"])))
    return {
        "topics": len(topics),
        "words": sum(len(documents[t]["markdown"].split()) for t in topics),
        "tasks": kinds["tarea"],
        "concepts": kinds["concepto"],
        "references": kinds["referencia"],
        "tables": sum(documents[t]["tables"] for t in topics),
        "code_blocks": sum(documents[t]["markdown"].count("```") // 2 for t in topics),
        "figures": sum(len(documents[t]["figures"]) for t in topics),
        "applies_to": [label for label, _ in applies.most_common()],
        # La fecha en que IBM tocó por última vez alguno de los temas de este archivo. Es
        # la señal de caducidad: dice si lo que hay acá sigue siendo lo vigente.
        "updated": max((documents[t].get("last_modified", "") for t in topics), default=""),
    }


APPLIES = re.compile(r"\*\*Se aplica a:\*\*\s*\[([^\]]+)\]")


def _terms(files: list[tuple[str, list[str]]], documents: dict) -> dict[str, list[str]]:
    """Los términos propios de cada archivo, por frecuencia relativa contra los demás.

    No hace falta una lista de palabras vacías: «para» y «que» están en los diecisiete
    archivos, así que su peso inverso es cero y se caen solas. Lo que queda es la jerga del
    producto —`fastmap`, `objectmanager`, `desencadenante`—, que es justo lo que un
    buscador léxico necesita para elegir archivo y lo que no aparece en los títulos.
    """
    counts: dict[str, Counter] = {}
    spread: Counter = Counter()
    for name, topics in files:
        words = Counter(
            word
            for topic in topics
            for word in WORD.findall(NOT_PROSE.sub(" ", documents[topic]["markdown"]).lower())
        )
        counts[name] = words
        spread.update(words)
        spread.subtract({w: c - 1 for w, c in words.items()})  # cuenta archivos, no usos

    total_files = len(files)
    out: dict[str, list[str]] = {}
    for name, words in counts.items():
        size = sum(words.values()) or 1
        ranked = sorted(
            ((w, c) for w, c in words.items()
             if c >= MIN_TERM_HITS and spread[w] <= total_files * MAX_TERM_SPREAD),
            key=lambda pair: -(pair[1] / size) * math.log(total_files / spread[pair[0]]),
        )
        chosen: list[str] = []
        for word, _ in ranked:
            # `campo` y `campos` son el mismo término y ocupan dos de los catorce lugares.
            if any(word.rstrip("es") == kept.rstrip("es") for kept in chosen):
                continue
            chosen.append(word)
            if len(chosen) == TOP_TERMS:
                break
        out[name] = chosen
    return out


def _title(documents: dict, nodes: dict[str, Node], topic: str) -> str:
    document = documents.get(topic, {})
    return document.get("title") or document.get("label") or nodes[topic].label


def _reading_order(
    nodes: dict[str, Node], documents: dict, root: str
) -> list[tuple[str, list[tuple[str, int]]]]:
    """Los temas por guía, en orden de lectura, con el nivel de encabezado de cada uno.

    Los temas que el índice de IBM no lista van al final de su guía, juntos: no tienen
    lugar en el árbol —por eso no están— y repartirlos por parecido sería inventarles uno.
    """
    out = []
    for guide_id in nodes[root].children:
        guide = nodes[guide_id].guide
        topics: list[tuple[str, int]] = []

        def visit(topic: str) -> None:
            if topic in documents:
                topics.append((topic, min(nodes[topic].depth, 6)))
            for child in nodes[topic].children:
                visit(child)

        visit(guide_id)
        unlisted = [
            (tid, 2) for tid, d in documents.items()
            if not d["listed"] and d["guide"] == guide
        ]
        unlisted.sort(key=lambda pair: documents[pair[0]]["title"])
        if topics or unlisted:
            out.append((guide_id, topics + unlisted))
    return out


def _pack(
    order: list[tuple[str, list[tuple[str, int]]]], documents: dict
) -> list[tuple[str, list[str]]]:
    """Empaqueta cada guía en uno o varios archivos, sin partir un capítulo.

    Se agrupa primero por capítulo y recién después se reparten los capítulos entre
    archivos: partir dentro de un capítulo dejaría media configuración de seguridad en un
    archivo y media en otro. Un capítulo que solo ya pasa del presupuesto se lleva su
    archivo entero — la alternativa sería cortarlo, que es justo lo que no se hace.
    """
    files: list[tuple[str, list[str]]] = []
    for index, (guide_id, topics) in enumerate(order, 1):
        chapters: list[list[tuple[str, int]]] = []
        for topic, level in topics:
            if level <= 2 or not chapters:
                chapters.append([])
            chapters[-1].append((topic, level))

        parts: list[list[tuple[str, int]]] = [[]]
        size = 0
        for chapter in chapters:
            weight = sum(documents[t]["chars"] + TOPIC_OVERHEAD for t, _ in chapter)
            if parts[-1] and size + weight > MAX_BYTES:
                parts.append([])
                size = 0
            parts[-1] += chapter
            size += weight

        # `3.2-guia-del-administrador.md`: el número de guía y el de parte, como se citan
        # («la 3.2»). Una guía que cabe en un archivo lleva solo su número —`4`—: un `.1`
        # que nunca tiene un `.2` al lado no dice nada.
        #
        # Sin relleno a cero, el explorador de archivos lista la 10 y la 11 entre la 1 y la
        # 2. Se acepta: el índice maestro y la cabecera de cada archivo llevan el orden de
        # lectura, y el nombre se lee y se dicta como lo dice la gente.
        name = slug(_guide_label(guide_id))
        for part, contents in enumerate(parts, 1):
            number = f"{index}" if len(parts) == 1 else f"{index}.{part}"
            files.append((f"{number}-{name}.md", [t for t, _ in contents]))
    return files


_LABELS: dict[str, str] = {}


def _guide_label(guide_id: str) -> str:
    return _LABELS.get(guide_id, guide_id)


def _render(
    nodes: dict[str, Node],
    documents: dict,
    name: str,
    topics: list[str],
    files: list[tuple[str, list[str]]],
    location: dict[str, tuple[str, str]],
    targets: dict[str, str],
    terms: list[str],
) -> str:
    """Un archivo del entregable: la cabecera que lo describe y después sus temas.

    La cabecera existe para una pregunta concreta: **¿está acá lo que busco, o en otro
    archivo?** Por eso dice qué capítulos cubre, cuántos procedimientos trae, a qué
    despliegue aplican sus temas, con qué jerga se habla dentro, y —lo que más ahorra—
    dónde está el resto si no es acá. Sin eso, un modelo tiene que abrir los diecisiete.
    """
    guide = documents[topics[0]]["guide"] if topics else ""
    guide_label = _LABELS.get(guide, guide)
    # `03.2-guia-del-administrador.md` -> guía 03, parte 2. `04-…` -> guía 04, sin partes.
    number = name.split("-", 1)[0]
    parts = [f for f, _ in files if f.split("-", 1)[0].split(".")[0] == number.split(".")[0]]
    part_of = f"{parts.index(name) + 1} de {len(parts)}" if len(parts) > 1 else ""
    levels = {t: _level(nodes, documents, t) for t in topics}
    chapters = [t for t in topics if levels[t] <= 2] or topics[:1]
    stats = _stats(documents, topics)
    heading = f"{number} · {guide_label}" + (f" — parte {part_of}" if part_of else "")

    out = [
        "---",
        f"product: {PRODUCT_NAME}",
        f"product_key: {PRODUCT}",
        f"file: {_yaml(number)}",
        f"guide: {_yaml(guide_label)}",
        *([f"part: {_yaml(part_of)}"] if part_of else []),
        f"covers: {_yaml(_covers(documents, nodes, chapters))}",
        f"chapters: {len(chapters)}",
        f"topics: {stats['topics']}",
        f"words: {stats['words']}",
        f"tasks: {stats['tasks']}",
        f"concepts: {stats['concepts']}",
        f"references: {stats['references']}",
        f"tables: {stats['tables']}",
        f"code_blocks: {stats['code_blocks']}",
        f"figures: {stats['figures']}",
        f"applies_to: {_yaml(', '.join(stats['applies_to']) or 'sin declarar')}",
        f"updated: {stats['updated']}",
        f"lang: {LANG}",
        f"source: {topic_url(_root_topic(nodes, documents, topics))}",
        f"extracted: {date.today().isoformat()}",
        "---",
        "",
        f"# {heading}",
        "",
        *_about(documents, nodes, name, number, guide_label, part_of, parts, chapters, stats),
        "",
        f"**Términos propios de este archivo:** {', '.join(terms)}." if terms else "",
        "",
        "## Índice de este archivo",
        "",
    ]
    for topic in topics:
        level = levels[topic]
        out.append(f"{'  ' * max(level - 2, 0)}- [{_title(documents, nodes, topic)}]"
                   f"(#{location[topic][1]})")
    out.append("")

    for topic in topics:
        document = documents[topic]
        level = levels[topic]
        out += ["", f"{'#' * level} {_title(documents, nodes, topic)}", ""]
        out.append(_where(nodes, documents, topic, guide_label))
        body = document.get("markdown", "")
        if body:
            out += ["", _rewrite(_shift(body, level), name, location, targets)]
    return "\n".join(line for line in out if line is not None).rstrip() + "\n"


def _miles(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def _covers(documents: dict, nodes: dict[str, Node], chapters: list[str]) -> str:
    """Del primer capítulo al último, que es cómo se cita un tramo de un manual."""
    first = _title(documents, nodes, chapters[0])
    last = _title(documents, nodes, chapters[-1])
    return first if first == last else f"{first} — {last}"


def _n(count: int, singular: str, plural: str) -> str:
    return f"{_miles(count)} {singular if count == 1 else plural}"


def _about(
    documents: dict,
    nodes: dict[str, Node],
    name: str,
    number: str,
    guide_label: str,
    part_of: str,
    parts: list[str],
    chapters: list[str],
    stats: dict,
) -> list[str]:
    """El párrafo de orientación. Va como cita para que se lea aparte del contenido.

    Se escribe sin artículo delante del nombre de la guía —«Notas del release» es femenino
    plural y «Guía del administrador» femenino singular— porque el rótulo lo pone IBM y no
    hay forma determinista de concordar con él.
    """
    titles = [_title(documents, nodes, c) for c in chapters]
    shown = titles if len(titles) <= 12 else titles[:12] + [f"y {len(titles) - 12} más"]
    scope = (
        f"parte {part_of}: capítulos «{titles[0]}» a «{titles[-1]}»" if part_of
        else f"completa: {_n(len(titles), 'capítulo', 'capítulos')}"
    )
    pieces = [_n(stats["topics"], "tema", "temas")]
    if stats["tasks"]:
        pieces.append(f"{_miles(stats['tasks'])} de ellos "
                      + ("un procedimiento paso a paso" if stats["tasks"] == 1
                         else "procedimientos paso a paso"))
    for count, singular, plural in (
        (stats["tables"], "tabla", "tablas"),
        (stats["code_blocks"], "bloque de código", "bloques de código"),
        (stats["figures"], "figura", "figuras"),
    ):
        if count:
            pieces.append(_n(count, singular, plural))

    lines = [
        f"> **Qué hay en este archivo.** «{guide_label}» de {PRODUCT_NAME}, {scope}. "
        f"{', '.join(pieces)} y {_n(stats['words'], 'palabra', 'palabras')}.",
        ">",
        f"> **Capítulos:** {' · '.join(shown)}.",
    ]
    if stats["applies_to"]:
        lines += [">", f"> **Se aplica a:** {', '.join(stats['applies_to'])}."]
    siblings = [f.split("-", 1)[0] for f in parts if f != name]
    where_else = f"El resto de esta guía está en {', '.join(siblings)}. " if siblings else ""
    lines += [
        ">",
        f"> **Si lo que buscas no está acá.** {where_else}"
        f"El índice de los {_miles(len(documents))} temas del producto, con su archivo y su ancla, está en "
        "`index.md`.",
    ]
    return lines


def _level(nodes: dict[str, Node], documents: dict, topic: str) -> int:
    return min(nodes[topic].depth, 6) if topic in nodes else 2


def _root_topic(nodes: dict[str, Node], documents: dict, topics: list[str]) -> str:
    for topic in topics:
        if topic in nodes:
            parent = nodes[topic]
            while parent.parent and nodes[parent.parent].depth >= 1:
                parent = nodes[parent.parent]
            return parent.topic_id
    return topics[0]


def _where(nodes: dict[str, Node], documents: dict, topic: str, guide_label: str) -> str:
    """La línea de ubicación: dónde vive este tema y dónde se verifica.

    Es la pieza que hace que un trozo suelto siga sirviendo. Un canal de ingesta corta el
    archivo por donde le conviene; si el trozo que le toca a Copilot empieza en «Pulse
    Aceptar», esta línea es lo único que dice de qué procedimiento se trata.
    """
    document = documents[topic]
    if document["listed"] and topic in nodes:
        # `path` trae [producto, guía, …ancestros]. Los dos primeros sobran: el producto
        # está en el front matter y la guía se antepone acá.
        trail = [label for label in nodes[topic].path[2:] if label]
        path = " › ".join([guide_label, *trail]) or guide_label
        origin = topic_url(topic)
    else:
        path = f"{guide_label} › temas fuera del índice de IBM"
        origin = f"https://www.ibm.com/docs/{LANG}/{document['href']}"
    return f"`{path}` · [origen]({origin})"


def _rewrite(
    markdown: str, name: str, location: dict[str, tuple[str, str]], targets: dict[str, str]
) -> str:
    """Reapunta los enlaces al paquete.

    Un enlace dentro del mismo archivo queda como `#ancla`; a otro archivo, como
    `archivo.md#ancla`. Lo que no resuelve —otra versión del producto, otro producto de
    IBM, la web— se queda apuntando a ibm.com.

    Las **figuras se dejan apuntando a ibm.com**, que es donde se verifican: lo que el
    corpus garantiza de una figura es su procedencia, y su texto alternativo en español
    —que sí va en el Markdown— es lo que un modelo puede leer de ella. Solo se reapuntan
    a una copia local si alguien la pidió con `crawl --images`.
    """
    def rewrite(match: re.Match) -> str:
        href = match.group(1)
        if href.lower().endswith(IMAGE_SUFFIX):
            local = IMAGES / "/".join(href.split("/")[1:])
            if local.exists():
                return "](" + IMAGE_DIR + "/" + "/".join(href.split("/")[1:]) + ")"
            return match.group(0)
        topic = targets.get(href)
        if topic is None or topic not in location:
            return match.group(0)
        target, slug_anchor = location[topic]
        return f"](#{slug_anchor})" if target == name else f"]({target}#{slug_anchor})"

    return INTERNAL.sub(rewrite, markdown)


def _copy_images() -> None:
    """Solo si existe la copia local. Por defecto no existe y las figuras quedan enlazadas
    a ibm.com."""
    destination = OUTPUT / IMAGE_DIR
    if destination.exists():
        shutil.rmtree(destination)
    if IMAGES.exists():
        shutil.copytree(IMAGES, destination)


def _yaml(text: str) -> str:
    return '"' + text.replace('"', "'") + '"' if any(c in text for c in ':#"') else text


def _readme(
    nodes: dict[str, Node],
    documents: dict,
    manifest: dict,
    files: list[tuple[str, list[str]]],
    location: dict[str, tuple[str, str]],
    root: str,
    terms: dict[str, list[str]],
) -> None:
    """El índice maestro. No es decorativo: sin él, encontrar «el capítulo de perfiles de
    seguridad» obliga a abrir los 17 archivos; con él es una búsqueda y un archivo."""
    stamp = date.today().isoformat()
    words = sum(len(d["markdown"].split()) for d in documents.values())
    unlisted = [d for d in documents.values() if not d["listed"]]

    lines = [
        f"# {PRODUCT_NAME} — documentación en español",
        "",
        f"Extracción completa de <{SITE_URL}> al {stamp}.",
        f"{len(documents)} temas · {words:,} palabras · {len(files)} archivos".replace(",", "."),
        "",
        "| Nº | Archivo | Guía | Temas | Palabras |",
        "| --- | --- | --- | ---: | ---: |",
    ]
    for name, topics in files:
        guide = _LABELS.get(documents[topics[0]]["guide"], "")
        number = name.split("-", 1)[0]
        count = sum(len(documents[t]["markdown"].split()) for t in topics)
        lines.append(f"| `{number}` | [{name}]({name}) | {guide} "
                     f"| {len(topics)} | {_miles(count)} |")
    lines += [
        "",
        "## Cómo leer este paquete",
        "",
        _HOW.strip(),
        "",
        f"## Temas que IBM no lista en su índice ({len(unlisted)})",
        "",
        "IBM los enlaza desde el texto de otros temas pero no los pone en su árbol de "
        "contenidos. Se encontraron siguiendo los enlaces internos; son "
        f"{sum(d['chars'] for d in unlisted):,} caracteres".replace(",", ".")
        + " y están al final de la guía a la que pertenecen.",
        "",
        "| Tema | Archivo |",
        "| --- | --- |",
    ]
    for document in sorted(unlisted, key=lambda d: d["title"]):
        name, slug_anchor = location[document["topic_id"]]
        lines.append(f"| {document['title']} | [{name}]({name}#{slug_anchor}) |")

    assets = manifest.get("assets", [])
    if assets:
        lines += [
            "",
            f"## Material que no es prosa ({len(assets)})",
            "",
            "IBM lo publica como archivo suelto, no como tema. No entra al corpus y se "
            "enlaza a su origen.",
            "",
        ]
        lines += [f"- [{a.rsplit('/', 1)[-1]}](https://www.ibm.com/docs/{LANG}/{a})"
                  for a in assets]

    lines += [
        "",
        "## Cómo elegir archivo",
        "",
        "Una fila por archivo con lo que trae y con qué jerga se habla dentro. Es lo que "
        "permite decidir dónde buscar sin abrir los diecisiete.",
        "",
    ]
    for name, topics in files:
        stats = _stats(documents, topics)
        chapters = [t for t in topics if _level(nodes, documents, t) <= 2] or topics[:1]
        titles = [_title(documents, nodes, c) for c in chapters]
        lines += [
            f"### `{name.split('-', 1)[0]}` · {_LABELS.get(documents[topics[0]]['guide'], '')}",
            "",
            f"[{name}]({name}) · {_n(stats['topics'], 'tema', 'temas')} "
            f"({_n(stats['tasks'], 'procedimiento', 'procedimientos')}, "
            f"{_n(stats['tables'], 'tabla', 'tablas')}) · "
            f"{_n(stats['words'], 'palabra', 'palabras')}"
            + (f" · se aplica a {', '.join(stats['applies_to'])}" if stats["applies_to"] else "")
            + (f" · actualizado {stats['updated']}" if stats["updated"] else ""),
            "",
            f"**Capítulos:** {' · '.join(titles)}.",
            "",
        ]
        if terms.get(name):
            lines += [f"**Términos:** {', '.join(terms[name])}.", ""]

    lines += ["", "## Índice de temas", ""]
    for name, topics in files:
        lines.append(f"### {name}")
        lines.append("")
        for topic in topics:
            level = _level(nodes, documents, topic)
            indent = "  " * max(level - 2, 0)
            lines.append(f"{indent}- [{_title(documents, nodes, topic)}]"
                         f"({name}#{location[topic][1]})")
        lines.append("")
    (OUTPUT / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _prompt(documents: dict, files: list[tuple[str, list[str]]]) -> None:
    """El prompt del agente, con las cifras del corpus interpoladas.

    Se genera en vez de escribirse a mano por la misma razón que el índice: un prompt que
    diga «2.511 temas» cuando el corpus tiene otros tantos le está mintiendo al agente
    sobre su propia fuente. Cada reextracción lo rehace con lo que de verdad hay.
    """
    kinds = Counter(d.get("kind", "") for d in documents.values())
    on_prem = sum(
        1 for d in documents.values()
        if {label for a, b in APPLIES_ANY.findall(d["markdown"]) for label in [(a or b).strip()]}
        == {"De forma local"}
    )
    numbers = {
        "files": len(files),
        "topics": _miles(len(documents)),
        "words": _miles(sum(len(d["markdown"].split()) for d in documents.values())),
        "tasks": _miles(kinds["tarea"]),
        "references": _miles(kinds["referencia"]),
        "tables": _miles(sum(d["tables"] for d in documents.values())),
        "code": _miles(sum(d["markdown"].count("```") // 2 for d in documents.values())),
        "figures": _miles(sum(len(d["figures"]) for d in documents.values())),
        "on_prem": _miles(on_prem),
        "stamp": date.today().isoformat(),
        "product": PRODUCT_NAME,
        "version": VERSION,
        "videos": sum(1 for d in documents.values() if VIDEO.search(d["markdown"])),
    }
    (OUTPUT / "prompt.md").write_text(_PROMPT.format(**numbers).lstrip(), encoding="utf-8")


# Un vídeo enlazado desde el texto: IBM los aloja en estos dos dominios.
VIDEO = re.compile(r"\]\(https?://(?:video|mediacenter)\.ibm\.com/")
APPLIES_ANY = re.compile(r"\*\*Se aplica a:\*\*\s*(?:\[([^\]]+)\]|([^\n*\[]+))")


_HOW = """
- **Una guía por archivo.** Los temas van anidados como encabezados, en el orden en que
  IBM los lista. Una guía se parte en partes solo si pasa del presupuesto de tamaño, y el
  corte cae siempre entre capítulos.
- **Cada tema dice dónde está.** Bajo cada encabezado, la línea `` `Guía › Capítulo › …` ``
  ubica el tema en el árbol y `[origen]` enlaza al tema en ibm.com, que es donde se
  verifica. Sirve sobre todo cuando un buscador devuelve un trozo suelto del archivo.
- **`Se aplica a:`** al inicio de un tema dice a qué despliegue aplica —local, en cloud,
  Cloud Pak for Data—. Cerca de un tercio de los temas lo declara.
- **Las figuras se enlazan a ibm.com**, que es donde se verifican, y conservan su texto
  alternativo en español, que es lo que un modelo puede leer de ellas. Ojo: IBM responde
  403 a las peticiones de figuras que no vienen de su sitio, así que el enlace vale como
  referencia y no como vista previa. Para verlas: `uv run openpages crawl --images` y
  volver a exportar, que las copia a `imagenes/` y reapunta cada figura ahí.
- **Las tablas son tablas** Markdown, con su encabezado y su título (`Tabla 1. …`). Dentro
  de una celda, `<br>` separa los párrafos: es el único salto que admite una tabla.
- **Los bloques de código llevan su lenguaje** cuando la señal es inequívoca (`sql`,
  `xml`, `bash`, `bat`, `properties`, `json`, `java`). IBM no lo declara; el resto queda
  sin etiquetar antes que con una etiqueta equivocada.
- **Nada se interpreta.** La conversión es un parser determinista sobre el HTML del API de
  IBM Documentation, sin modelo de lenguaje de por medio. Las erratas del original se
  conservan.
"""


_PROMPT = """
# Prompt para el agente de Copilot Studio

Generado el {stamp} a partir de este mismo paquete. Las cifras son **medidas sobre el
corpus**, no estimadas: cada reextracción rehace este archivo con las que correspondan.

## Cómo usarlo

1. En Copilot Studio, crea el agente y abre **Instrucciones**.
2. Pega el bloque de abajo, entre las dos líneas de guiones.
3. Sube los {files} archivos `.md` de esta carpeta como **origen de conocimiento**.
4. Antes de publicar, edita la línea marcada `>>> AJUSTA ESTO <<<` con el tipo de
   despliegue de tu instalación. Es el único dato que el paquete no puede saber solo.

---

Eres un asistente especializado en **{product}**. Respondes preguntas sobre cómo
configurar, administrar y usar el producto apoyándote **únicamente** en la documentación
oficial de IBM que tienes como conocimiento. No inventas, no completas con lo que sabes de
otras versiones y no supones comportamientos que la documentación no describa.

## Qué tienes como fuente

La documentación completa de {product} en español: {topics} temas, {words} palabras,
repartidos en {files} archivos Markdown. Incluye {tasks} procedimientos paso a paso,
{references} temas de referencia, {tables} tablas, {code} bloques de código y {figures}
figuras enlazadas a ibm.com.

`index.md` es el índice maestro. Tiene, por archivo, sus capítulos, sus términos propios y
sus cifras; y después la lista completa de los {topics} temas con el archivo y el ancla de
cada uno.

## Cómo encontrar la respuesta

1. **Empieza por `index.md`.** La sección «Cómo elegir archivo» dice qué trae cada uno y
   con qué vocabulario se habla dentro. Elige archivo ahí antes de leer nada más.
2. **Lee la cabecera del archivo.** Cada uno abre con un bloque «Qué hay en este archivo»
   que dice qué capítulos cubre y —si no es el correcto— en cuál está el resto.
3. **Ubícate con la línea de cada tema.** Bajo cada encabezado hay una línea como
   `` `Guía del administrador › Seguridad › Reglas de seguridad` `` seguida de
   el enlace de origen. Te dice de qué guía y de qué capítulo es ese fragmento aunque lo hayas
   recuperado suelto.

## Cómo responder

- **Los procedimientos van completos y en orden.** {tasks} de los {topics} temas son
  secuencias numeradas. Nunca resumas un procedimiento, nunca saltes un paso y nunca
  reordenes. Si el usuario solo necesita una parte, entrega la secuencia entera y señala
  dónde está lo que preguntó.
- **Las notas y avisos nunca se omiten.** Van como cita: `> **Nota:**`, `> **Aviso:**`,
  `> **Atención:**`. Suelen ser exactamente lo que evita perder datos o dejar el sistema
  inconsistente. Repítelos textualmente junto al paso al que pertenecen.
- **Las tablas se reproducen como tablas**, con su encabezado y su título (`Tabla 1. …`).
  No las conviertas en prosa ni en viñetas: son especificaciones de campos, parámetros y
  códigos de error.
- **El código va en bloque y literal.** No reescribas rutas, nombres de archivo, variables
  ni mayúsculas. Los marcadores entre ángulos —`<OP_HOME>`, `<server_name>`— son
  marcadores: explícalos, no los rellenes con un valor inventado.
- **Cita siempre el origen.** Cierra cada respuesta con el enlace de origen del tema del
  que la sacaste, para que quien pregunte pueda verificarla en ibm.com.

## Tipo de despliegue

`>>> AJUSTA ESTO <<<` Esta instalación de OpenPages es: **local (on-premises)**.
*(Reemplaza por «SaaS / OpenPages on Cloud» o «Cloud Pak for Data» según corresponda.)*

Muchos temas abren declarando a qué despliegue aplican, con una línea `**Se aplica a:**`
seguida de «De forma local», «En cloud», «Cloud Pak for Data» o «Todos los tipos de
despliegue». **Respétala siempre**: {on_prem} temas del corpus son exclusivos de la
instalación local —rutas de servidor, comandos de base de datos, mantenimiento de la
aplicación— y no existen en los otros despliegues.

Si el tema que contesta la pregunta declara un despliegue distinto al de esta instalación,
dilo antes de responder y aclara que el procedimiento puede no aplicar.

## Idioma

IBM traduce su documentación con terminología de España. Tú **respondes en español de
Chile**, aunque la fuente diga otra cosa:

| La fuente dice | Tú dices |
| --- | --- |
| pulse / pulsa | haga clic |
| vía de acceso | ruta |
| serie de caracteres | cadena de texto |
| renovar | actualizar |
| cuadro (refiriéndose a una tabla) | tabla |
| fichero | archivo |

Trata esos pares como sinónimos también **al buscar**: si el usuario pregunta por «la ruta
de instalación», el texto que lo responde dice «vía de acceso de instalación».

Los nombres de menús, botones y campos de la interfaz **no se traducen ni se corrigen**: si
la documentación dice **Perfiles permitidos predeterminados**, eso es lo que el usuario va
a ver en pantalla.

## Cuándo decir que no sabes

Di que no está en la documentación —y no lo completes— cuando:

- La pregunta sea de una versión distinta. Este corpus es **solo {version}**; IBM publica
  además 8.3.0, 9.0.0 y 9.2.0, y los procedimientos cambian entre versiones.
- La respuesta esté en un vídeo. Hay {videos} temas que enlazan un vídeo de ibm.com; puedes dar
  el enlace, pero no describir su contenido.
- La respuesta esté en un PDF o un ZIP suelto —la guía de referencia de la API REST, la de
  desencadenantes, el SDK, el `swagger2.json`—. Están inventariados en `index.md` con su
  enlace: entrégalo en vez de improvisar.
- Sea una decisión de negocio, una configuración específica de AFP Capital o algo que
  dependa de datos que no tienes. Deriva a quien corresponda.

Ante la duda entre responder de memoria y decir «eso no está en la documentación que
tengo», elige lo segundo. Una respuesta inventada sobre una configuración de GRC cuesta más
que una pregunta sin responder.

---

## Notas de configuración (esto NO va en el prompt)

- **Origen de conocimiento:** sube los {files} archivos `.md`. `index.md` es el que enruta;
  si el canal permite priorizar uno, que sea ése.
- **Tamaño:** el archivo más grande ronda los 700 KB. Si tu canal tiene un tope menor, baja
  `export.max_bytes` en `config.toml` y vuelve a exportar.
- **Figuras:** son enlaces a ibm.com y responden 403 fuera del sitio, así que no se van a
  ver incrustadas. Su descripción en español sí está en el texto, que es lo que el agente
  lee. Para incluirlas: `uv run openpages crawl --images && uv run openpages export`.
- **Actualización:** cuando IBM publique cambios, `uv run openpages` rehace el paquete y
  este prompt con las cifras nuevas.
"""
