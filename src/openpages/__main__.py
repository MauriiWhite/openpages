"""Línea de comandos: las etapas, en el orden en que se escriban.

    uv run openpages                  # crawl, parse, export
    uv run openpages parse export     # solo esas, en ese orden
    uv run openpages crawl --refresh  # re-descarga todo en vez de usar el caché
    uv run openpages crawl --images   # además baja una copia local de las figuras
    uv run openpages verify           # comprueba que no se perdió ni una palabra
"""

from __future__ import annotations

import sys
import time

from . import crawl, export, parse, verify

STAGES = {
    "crawl": ("Baja el índice y el cuerpo de cada tema desde el API de IBM", crawl.run),
    "parse": ("Convierte el HTML a Markdown y valida las invariantes", parse.run),
    "export": ("Arma output/: una guía por archivo, más el índice maestro", export.run),
    "verify": ("Contrasta la fuente contra el entregable, palabra por palabra", verify.run),
}
DEFAULT = ["crawl", "parse", "export"]


def main() -> None:
    arguments = sys.argv[1:]
    refresh = "--refresh" in arguments
    images = "--images" in arguments
    names = [a for a in arguments if not a.startswith("-")] or DEFAULT

    if {"-h", "--help"} & set(arguments):
        print(__doc__)
        for name, (what, _) in STAGES.items():
            print(f"  {name:8} {what}")
        return

    unknown = [n for n in names if n not in STAGES]
    if unknown:
        raise SystemExit(f"unknown stage(s): {', '.join(unknown)}. Valid: {', '.join(STAGES)}")

    for name in names:
        what, run = STAGES[name]
        print(f"\n== {name}: {what}")
        started = time.time()
        run(refresh=refresh, images=images) if name == "crawl" else run()
        print(f"   {name} done in {time.time() - started:.1f}s")


if __name__ == "__main__":
    main()
