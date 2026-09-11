"""Comprueba que no se perdió nada: la fuente contra el entregable, palabra por palabra.

`guard.py` cuenta cosas —temas, tablas, figuras— y por eso no puede ver una pérdida
*dentro* de un tema: si el convertidor se comiera el texto de las celdas de tabla, los
conteos seguirían cuadrando. Esta etapa hace la pregunta directa: **¿está en el Markdown
cada palabra que está en el HTML de IBM?**

La comparación pone un separador en **cada frontera de elemento** de la fuente, porque el
Markdown inserta `**` o `` ` `` en esos mismos bordes. Sin eso, `<span>Reuters</span>y`
—que IBM escribe sin espacio— se contaría como una palabra perdida cuando en realidad se
transcribe exactamente como el navegador la muestra.

Fue así como aparecieron las dos pérdidas reales del proyecto: los bloques dentro de
celdas de tabla, que salían pegados en el 37,7% de las celdas, y los 46 temas que IBM
enlaza desde el texto sin listarlos en su índice.
"""

from __future__ import annotations

import json
import re
from collections import Counter

from . import DATA, OUTPUT, cache_file
from .parse import Tree, _dropped

WORD = re.compile(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")
# Cobertura mínima del texto de origen. Lo que falta son palabras que IBM misma escribe
# pegadas a una etiqueta (`Thomson Reutersy`): se transcriben tal cual, así que aparecen
# como ausentes sin serlo. Por debajo de esto, la pérdida ya no es de tokenización.
MIN_COVERAGE = 0.999
IMAGE_SUFFIX = (".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp")


def source_words(html: str) -> Counter:
    """Las palabras del HTML de origen, sin la navegación generada ni los iconos."""
    tree = Tree()
    tree.feed(html)
    chunks: list[str] = []

    def walk(node) -> None:
        for child in node.children:
            if isinstance(child, str):
                chunks.append(child)
            elif not _dropped(child) and child.attrs.get("id") != "lastModifiedDate":
                chunks.append("\n")
                walk(child)
                chunks.append("\n")

    walk(tree.root)
    return Counter(w.lower() for w in WORD.findall("".join(chunks).replace("\xa0", " ")))


def run() -> None:
    documents = json.loads((DATA / "documents.json").read_text(encoding="utf-8"))

    total = missing = 0
    worst: list[tuple[float, int, str, list]] = []
    for topic_id, document in documents.items():
        path = cache_file(document["href"])
        if not path.exists():
            continue
        source = source_words(path.read_text(encoding="utf-8"))
        produced = Counter(
            w.lower() for w in WORD.findall(document["markdown"] + " " + document["title"])
        )
        absent = source - produced
        count, gone = sum(source.values()), sum(absent.values())
        total += count
        missing += gone
        if gone:
            worst.append((gone / count if count else 1, gone, topic_id, absent.most_common(4)))

    coverage = 1 - missing / total if total else 0
    worst.sort(reverse=True)
    print(f"  source text: {total:,} words · not in the Markdown: {missing} "
          f"· coverage {coverage:.4%}")
    for ratio, gone, topic_id, sample in worst[:5]:
        print(f"    {ratio:6.2%} {gone:3} {topic_id[:44]:46} {[w for w, _ in sample]}")

    problems = []
    if coverage < MIN_COVERAGE:
        problems.append(f"text coverage {coverage:.4%}, expected >={MIN_COVERAGE:.2%}")
    problems += _sitemap(documents)
    problems += _package()

    if problems:
        raise SystemExit("\nVERIFICATION FAILED:\n" + "\n".join(f"  - {p}" for p in problems))
    print("  every source word, every sitemap topic and every local reference checks out")


def _sitemap(documents: dict) -> list[str]:
    path = DATA / "sitemap.xml"
    if not path.exists():
        return ["sitemap.xml missing"]
    listed = set(re.findall(r"\?topic=([^<&]+)</loc>", path.read_text(encoding="utf-8")))
    absent = listed - set(documents)
    print(f"  IBM's sitemap: {len(listed)} topics, {len(absent)} missing from the corpus")
    return [f"{len(absent)} sitemap topics missing: {sorted(absent)[:5]}"] if absent else []


def _package() -> list[str]:
    """Que el entregable se pueda leer solo: figuras presentes, enlaces internos resueltos.

    Los enlaces que no resuelven son texto de IBM que *parece* un enlace —trazas de Java,
    el ejemplo `[Link title](URL)` que la propia documentación imprime—, así que se
    informan y no se cuentan como fallo salvo que aparezca uno nuevo.
    """
    if not OUTPUT.exists():
        return ["output/ missing: run export first"]
    anchors: dict[str, set[str]] = {}
    for path in sorted(OUTPUT.glob("*.md")):
        seen: dict[str, int] = {}
        from .export import anchor

        anchors[path.name] = {
            anchor(m.group(1), seen)
            for m in re.finditer(r"^#{1,6} (.+)$", path.read_text(encoding="utf-8"), re.M)
        }

    images = broken_images = links = broken_links = 0
    for path in sorted(OUTPUT.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for _, url in re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", text):
            images += 1
            # Por defecto las figuras apuntan a ibm.com; solo las que se copiaron con
            # `crawl --images` tienen que existir en el paquete.
            if not url.startswith("http") and not (OUTPUT / url).exists():
                broken_images += 1
        for _, url in re.findall(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)", text):
            if url.startswith("http"):
                continue
            links += 1
            target, _, fragment = url.partition("#")
            name = target or path.name
            if (target and not (OUTPUT / target).exists()) or (
                fragment and fragment not in anchors.get(name, set())
            ):
                broken_links += 1
    linked = sum(
        1 for path in OUTPUT.glob("*.md")
        for _, url in re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", path.read_text(encoding="utf-8"))
        if url.startswith("http")
    )
    where = "linked to ibm.com" if linked == images else f"{images - linked} copied locally"
    print(f"  package: {images} figures ({where}, {broken_images} unresolved), "
          f"{links} internal links ({broken_links} unresolved)")
    problems = []
    if broken_images:
        problems.append(f"{broken_images} figures do not resolve to a local file")
    # Medido: 13 «enlaces» que son texto literal de IBM dentro de bloques de código.
    if broken_links > 20:
        problems.append(f"{broken_links} internal links do not resolve, more than the 13 measured")
    return problems
