"""Invariantes del corpus. La red que impide degradarse en silencio.

El peor fallo de un extractor no es caerse: es seguir corriendo y devolver menos. Si IBM
cambia la forma de su HTML y `class="note"` deja de existir, o el API empieza a servir el
inglés cuando se le pide español, el pipeline escribiría un corpus más pobre encima del
bueno sin decir nada.

Por eso se valida **antes** de escribir y se aborta conservando la salida anterior.

Las cotas están MEDIDAS sobre el corpus real (2026-09-11) con ~10% de holgura. Si una
estorba, la respuesta es entender por qué se violó, no bajarle el umbral: una invariante
mal calibrada llora lobo hasta que deja de significar algo.
"""

from __future__ import annotations

import json
import os
import re
from datetime import UTC, datetime

from . import DATA, MIN_TOPICS, Node

MIN_WITH_TITLE = 0.99      # medido: 2.465 de 2.465
MIN_WITH_BODY = 0.98       # medido: 99,3% pasan de 80 caracteres
MIN_TABLES = 475           # medido: 529
MIN_FIGURES = 1580         # medido: 1.758 (las 922 píldoras de aplicabilidad
                           # salen como rótulo, no como imagen: no son figuras)
MIN_CODE_BLOCKS = 1580     # medido: 1.759
# El índice lista una página que el servidor no sirve (`Bienvenido`, el marcador de la
# portada). Una es normal; si mañana son cien, el árbol cambió y hay que mirarlo.
MAX_MISSING = 3
# El español es el punto del ejercicio. IBM sirve el inglés como respaldo cuando le falta
# una traducción, y eso no da error: da un tema en otro idioma. Medido: 2.457 de 2.465.
MIN_SPANISH = 0.97
# Variación de volumen entre corridas. Un fixpack mueve páginas, no un cuarto del texto.
MAX_TEXT_DRIFT = 0.25

OVERRIDE = "OPENPAGES_FORCE"
SPANISH = re.compile(r"\b(el|la|los|las|para|que|con|una|del|por)\b", re.IGNORECASE)


def metrics(documents: dict[str, dict]) -> dict:
    """Salud del corpus en una línea. Se acumula por corrida para que la deriva lenta sea
    visible: un descenso gradual no dispara ninguna invariante, pero en la serie se ve."""
    values = list(documents.values())
    return {
        "at": datetime.now(UTC).isoformat(timespec="seconds"),
        "topics": len(values),
        "chars": sum(d["chars"] for d in values),
        "tables": sum(d["tables"] for d in values),
        "figures": sum(len(d["figures"]) for d in values),
        "code_blocks": sum(d["markdown"].count("```") // 2 for d in values),
    }


def check(nodes: dict[str, Node], documents: dict[str, dict]) -> list[str]:
    """Invariantes violadas. Lista vacía significa corpus sano."""
    problems: list[str] = []
    total = len(documents)
    expected = sum(1 for n in nodes.values() if n.depth > 0)

    # `documents` trae los temas del índice más los que solo están enlazados desde el
    # texto, así que puede superar a `expected`. Lo que se acota es el déficit.
    listed = sum(1 for d in documents.values() if d.get("listed", True))
    missing = expected - listed
    if missing > MAX_MISSING:
        problems.append(f"{missing} topics in the toc were not parsed, at most {MAX_MISSING} tolerated")
    if not total:
        return problems + ["no documents at all"]

    per_guide: dict[str, int] = {}
    for document in documents.values():
        per_guide[document["guide"]] = per_guide.get(document["guide"], 0) + 1
    for guide, floor in MIN_TOPICS.items():
        found = per_guide.get(guide, 0)
        if found < floor:
            problems.append(f"guide {guide}: only {found} topics, expected >={floor}")

    ratios = [
        ("have a title", sum(1 for d in documents.values() if d["title"]) / total, MIN_WITH_TITLE),
        ("have a body", sum(1 for d in documents.values() if d["chars"] > 80) / total, MIN_WITH_BODY),
        ("are in Spanish",
         sum(1 for d in documents.values() if SPANISH.search(d["markdown"])) / total, MIN_SPANISH),
    ]
    for label, ratio, floor in ratios:
        if ratio < floor:
            problems.append(f"only {ratio:.1%} {label}, expected >={floor:.0%}")

    counts = metrics(documents)
    for key, floor in (("tables", MIN_TABLES), ("figures", MIN_FIGURES),
                       ("code_blocks", MIN_CODE_BLOCKS)):
        if counts[key] < floor:
            problems.append(f"only {counts[key]} {key}, expected >={floor}")

    problems += _sitemap(documents)

    previous = _previous()
    if previous and previous["chars"]:
        drift = (counts["chars"] - previous["chars"]) / previous["chars"]
        if abs(drift) > MAX_TEXT_DRIFT:
            problems.append(
                f"text volume changed {drift:+.0%} ({previous['chars']:,} -> "
                f"{counts['chars']:,} chars), over the {MAX_TEXT_DRIFT:.0%} tolerated"
            )
    return problems


def _sitemap(documents: dict[str, dict]) -> list[str]:
    """El sitemap que IBM publica aparte es el único testimonio **independiente** de qué
    temas existen. El índice y el sitemap se generan por caminos distintos: si los dos
    coinciden, el árbol está entero; si el índice se encogiera, el sitemap lo diría."""
    path = DATA / "sitemap.xml"
    if not path.exists():
        return ["sitemap.xml missing: the independent check on the tree did not run"]
    listed = set(re.findall(r"\?topic=([^<&]+)</loc>", path.read_text(encoding="utf-8")))
    absent = listed - set(documents)
    if absent:
        sample = ", ".join(sorted(absent)[:5])
        return [f"{len(absent)} topics in IBM's sitemap are missing from the corpus: {sample}"]
    return []


def _previous() -> dict | None:
    path = DATA / "runs.jsonl"
    if not path.exists():
        return None
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return json.loads(lines[-1]) if lines else None


def enforce(nodes: dict[str, Node], documents: dict[str, dict]) -> None:
    """Aborta si el corpus está degradado, sin tocar la salida anterior."""
    problems = check(nodes, documents)
    if problems:
        detail = "\n".join(f"  - {p}" for p in problems)
        if not os.environ.get(OVERRIDE):
            raise SystemExit(
                f"\nDEGRADED CORPUS — nothing was written:\n{detail}\n\n"
                f"IBM may have changed the shape of its HTML. Check parse.py against a real\n"
                f"topic before continuing. If the change is legitimate:"
                f" {OVERRIDE}=1 uv run openpages parse\n"
            )
        print(f"WARNING: invariants violated, continuing because {OVERRIDE}=1:\n{detail}")

    DATA.mkdir(parents=True, exist_ok=True)
    with (DATA / "runs.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(metrics(documents), ensure_ascii=False) + "\n")
