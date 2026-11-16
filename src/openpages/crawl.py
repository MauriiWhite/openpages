"""El índice, los temas, los temas escondidos y las imágenes, a disco.

A diferencia de un portal corriente, IBM publica el árbol entero en **una** petición
(`/docs/api/v1/toc/<producto>?lang=es`). No hay que recorrer nada en anchura: el índice
*es* el manifiesto, y viene ya en orden de lectura.

Pero el índice **no lo lista todo**. Medido sobre este producto: 53 destinos `.html` del
propio producto aparecen enlazados desde el cuerpo de otros temas y no están en el árbol.
Cuarenta son el mismo tema bajo otro nombre de archivo —IBM renombró archivos al traducir y
los enlaces del texto quedaron apuntando al nombre inglés—, pero **trece son contenido que
no está en ninguna otra parte**: 65.225 caracteres, entre ellos la integración de la API
REST con certificados de cliente y los procedimientos de creación de vistas.

Por eso el recorrido no termina con el índice: sigue los enlaces internos hasta que no
aparecen destinos nuevos. Es la diferencia entre «bajé lo que IBM lista» y «bajé lo que
IBM publica».

Lo que sí hay que traer uno por uno es el cuerpo de cada tema, porque la página que ve el
navegador es una SPA: su HTML trae 17 caracteres de texto visible y el contenido llega
después por el API. Descargar la página pública daría 2.467 archivos vacíos.

El sitemap que IBM publica aparte se baja también, y no es decorativo: es el único
testimonio independiente de qué temas existen. Si el índice se encoge, el sitemap lo dice.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict

from . import CACHE, DATA, HOST, IMAGES, LANG, PRODUCT, cache_file, content_url, image_file, walk
from .net import fetch

TOC_URL = f"https://{HOST}/docs/api/v1/toc/{PRODUCT}?lang={LANG}"
SITEMAP_URL = f"https://{HOST}/docs/{LANG}/{PRODUCT}/0/sitemap.xml"

# Un destino del propio producto dentro del HTML: `/docs/es/SSFUEU_9.1/op_grc_admin/x.html`
LOCAL = re.compile(
    rf'(?:href|src)="/docs/[a-z]{{2}}/({re.escape(PRODUCT)}/[^"#?]+)', re.IGNORECASE
)
PAGE = (".html", ".htm")
IMAGE = (".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp")
# La navegación generada al pie de cada tema. Se recorta antes de buscar enlaces: sus
# destinos salen del propio índice, así que no descubren nada, y arrastran los alias en
# inglés de cada tema hasta que el cierre deja de converger.
ASIDE = re.compile(r"<aside\b.*?</aside>", re.DOTALL | re.IGNORECASE)
# Rondas de seguimiento de enlaces. El tope existe para que un ciclo no se vuelva infinito;
# en este corpus el cierre converge mucho antes.
MAX_ROUNDS = 8


def _linked(hrefs: set[str]) -> tuple[set[str], set[str], set[str]]:
    """Los destinos del producto que citan las páginas ya en caché.

    Tres cubos, porque se tratan distinto: las **páginas** se siguen, las **figuras** se
    copian, y el resto —los PDF oficiales, el `swagger2.json` de la API REST— se anota en
    el manifiesto y se deja enlazado a ibm.com. No son prosa y no entran al corpus, pero
    tampoco pueden desaparecer del inventario.
    """
    pages: set[str] = set()
    figures: set[str] = set()
    assets: set[str] = set()
    for href in hrefs:
        path = cache_file(href)
        if not path.exists():
            continue
        body = ASIDE.sub("", path.read_text(encoding="utf-8"))
        for target in LOCAL.findall(body):
            low = target.lower()
            bucket = pages if low.endswith(PAGE) else figures if low.endswith(IMAGE) else assets
            bucket.add(target)
    return pages, figures, assets


def run(refresh: bool = False, images: bool = False) -> None:
    DATA.mkdir(parents=True, exist_ok=True)

    print(f"toc: {TOC_URL}")
    fetch([(TOC_URL, DATA / "toc.json"), (SITEMAP_URL, DATA / "sitemap.xml")], "index")
    toc = json.loads((DATA / "toc.json").read_text(encoding="utf-8"))["toc"]

    nodes = walk(toc)
    print(f"  {len(nodes)} topics in the tree, {max(n.depth for n in nodes.values())} levels deep")

    listed = {node.href for node in nodes.values()}
    _download(listed, refresh, "topics")

    # Cierre por enlaces: lo que el índice no lista pero el texto sí cita.
    seen = set(listed)
    extra: set[str] = set()
    figures: set[str] = set()
    assets: set[str] = set()
    frontier = set(listed)
    for _ in range(MAX_ROUNDS):
        pages, found, other = _linked(frontier)
        figures |= found
        assets |= other
        frontier = {p for p in pages if p not in seen}
        if not frontier:
            break
        seen |= frontier
        extra |= frontier
        print(f"  {len(frontier)} topics linked from the text but absent from the toc")
        _download(frontier, refresh, "linked topics")

    if images:
        _download_images(figures, refresh)

    missing = sorted(h for h in seen if not cache_file(h).exists())
    if missing:
        print(f"  {len(missing)} listed but not served: {', '.join(m.rsplit('/', 1)[-1] for m in missing)}")

    manifest = {
        "product": PRODUCT,
        "lang": LANG,
        "topics": len(nodes),
        "extra": sorted(extra),
        "images": sorted(figures),
        "assets": sorted(assets),
        "missing": missing,
        "nodes": {topic_id: asdict(node) for topic_id, node in nodes.items()},
    }
    (DATA / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    size = sum(f.stat().st_size for f in CACHE.glob("*"))
    local = [f for f in IMAGES.rglob("*") if f.is_file()] if IMAGES.exists() else []
    figures = f"{len(figures)} linked" + (f", {len(local)} copied locally" if local else "")
    print(f"  cache: {len(list(CACHE.glob('*')))} pages, {size / 1e6:.1f} MB · figures: {figures}")


def _download(hrefs: set[str], refresh: bool, label: str) -> None:
    jobs = [
        (content_url(href), cache_file(href))
        for href in sorted(hrefs)
        if refresh or not cache_file(href).exists()
    ]
    cached = len(hrefs) - len(jobs)
    if cached:
        print(f"  {cached} {label} already in cache (use --refresh to re-download)")
    if jobs:
        http = fetch(jobs, label, tolerate_missing=True)
        _record(http)


def _download_images(images: set[str], refresh: bool) -> None:
    """Trae una copia local de las figuras. **Fuera de la corrida por defecto.**

    El entregable enlaza las figuras a ibm.com, que es donde se verifican: lo que el corpus
    garantiza de una figura es su procedencia, y el texto alternativo en español —que sí va
    en el Markdown— es lo único que un modelo puede leer de ella.

    Con `--images` se bajan igual, para quien quiera leer el paquete sin conexión. Conviene
    saber que **IBM responde 403 a las peticiones de figuras que no vienen de su sitio**,
    así que sin la copia local las imágenes no se ven: el enlace sirve de referencia, no
    de vista previa.

    Se guardan bajo la ruta que IBM les da (`op_grc_admin/security_levels.jpg`) porque el
    mismo nombre de archivo se repite entre guías: `settings_menu_icon_task_focused_ui.jpg`
    está en cuatro de ellas.
    """
    jobs = [
        (f"https://{HOST}/docs/{LANG}/{href}", image_file(href))
        for href in sorted(images)
        if refresh or not image_file(href).exists()
    ]
    cached = len(images) - len(jobs)
    if cached:
        print(f"  {cached} images already in cache")
    if jobs:
        _record(fetch(jobs, "images", tolerate_missing=True))


def _record(http: dict) -> None:
    path = DATA / "http.json"
    known = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    known.update(http)
    path.write_text(json.dumps(known, ensure_ascii=False, indent=1), encoding="utf-8")
