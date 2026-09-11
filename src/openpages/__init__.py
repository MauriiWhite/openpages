"""Extracción de IBM Documentation (OpenPages 9.0.0, español) a Markdown verificable.

El árbol, las rutas y la configuración. Todo lo demás cuelga de acá.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG = tomllib.loads((ROOT / "config.toml").read_text(encoding="utf-8"))

PRODUCT: str = CONFIG["source"]["product"]
LANG: str = CONFIG["source"]["lang"]
HOST: str = CONFIG["source"]["host"]
SITE_URL: str = CONFIG["source"]["site_url"]

DATA = ROOT / CONFIG["paths"]["data"]
OUTPUT = ROOT / CONFIG["paths"]["output"]
CACHE = DATA / "cache"
IMAGES = DATA / "images"

# Cotas por guía, indexadas por slug. El slug es el directorio con que IBM nombra la guía.
MIN_TOPICS: dict[str, int] = {g["slug"]: g["min_topics"] for g in CONFIG["guides"]}


def cache_file(href: str) -> Path:
    """El archivo de caché de un tema. El `href` lleva `/`, el nombre de archivo no."""
    return CACHE / (href.replace("/", "__"))


def image_file(href: str) -> Path:
    """La copia local de una figura, bajo la ruta que IBM le da. El nombre a secas no basta:
    `settings_menu_icon_task_focused_ui.jpg` existe en cuatro guías distintas."""
    return IMAGES / "/".join(href.split("/")[1:])


def topic_url(topic_id: str) -> str:
    """La URL que ve una persona. Es la que va como procedencia en el Markdown: la del API
    devuelve un fragmento sin navegación y no sirve para volver a la fuente."""
    return f"{SITE_URL}?topic={topic_id}"


def content_url(href: str) -> str:
    """La URL del API que sí devuelve el cuerpo del tema, ya en español."""
    from urllib.parse import quote

    return f"https://{HOST}/docs/api/v1/content/{quote(href)}?parsebody=true&lang={LANG}"


@dataclass
class Node:
    """Un nodo del índice de IBM. Es a la vez el árbol y la lista de documentos: en este
    corpus **todo** nodo tiene contenido propio, incluidos los que tienen hijos."""

    topic_id: str
    href: str
    label: str
    depth: int
    parent: str | None
    guide: str
    path: list[str] = field(default_factory=list)
    children: list[str] = field(default_factory=list)


def guide_of(href: str) -> str:
    """La guía a la que pertenece un `href`.

    `SSFUEU_9.0.0/op_grc_admin/c_foo.html` -> `op_grc_admin`. Las dos páginas sueltas del
    producto (`Bienvenido`, `PDF`) no cuelgan de un directorio de guía; ahí el segmento
    intermedio es el que hay, y para `Bienvenido` no existe: se queda con su propio nombre.
    """
    parts = href.split("/")
    return parts[1] if len(parts) >= 3 else Path(parts[-1]).stem.replace("_", "-")


def walk(toc: dict) -> dict[str, Node]:
    """Aplana el índice de IBM a nodos, en orden de lectura.

    El orden es el que IBM lista, que es el orden en que la documentación se lee y se
    imprime. Ordenar por `topicId` daría otra cosa y no habría forma de volver a éste.
    """
    nodes: dict[str, Node] = {}

    def visit(raw: dict, depth: int, parent: str | None, guide: str, path: list[str]) -> str:
        topic_id = raw["topicId"]
        node = Node(
            topic_id=topic_id,
            href=raw["href"],
            label=raw["label"],
            depth=depth,
            parent=parent,
            guide=guide,
            path=path,
        )
        nodes[topic_id] = node
        for child in raw.get("topics") or []:
            child_guide = guide_of(child["href"]) if depth == 0 else guide
            node.children.append(
                visit(child, depth + 1, topic_id, child_guide, [*path, raw["label"]])
            )
        return topic_id

    # La raíz es el producto, no una guía: su `href` es `SSFUEU_9.0.0` a secas.
    visit(toc, 0, None, "", [])
    return nodes
