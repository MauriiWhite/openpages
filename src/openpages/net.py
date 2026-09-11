"""Transporte: `curl` en HTTP/2, por lotes.

Va aparte del recorrido porque es la parte que costó acertar, y la conclusión no es obvia:

  - **HTTP/2 es obligatorio.** MEDIDO: con las mismas cabeceras, el WAF de IBM responde
    `403` a HTTP/1.1 y `200` a HTTP/2. `http.client` de la biblioteca estándar solo habla
    HTTP/1.1, así que no sirve para este sitio — el `403` no es por el User-Agent ni por
    la frecuencia, es por la versión del protocolo.
  - **Por eso el cliente es `curl`** y no `urllib`: es el único cliente ya instalado que
    habla h2. Sigue sin haber dependencias de Python que instalar.
  - **Un lote, una invocación.** `--parallel` multiplexa las transferencias sobre la misma
    conexión h2, así que no hay handshake por tema ni hilos que coordinar. En un archivo de
    configuración `curl` empareja `url`, `output` y `dump-header` por posición.
  - **Las cabeceras se guardan.** No se usan todavía para revalidar, pero son la
    procedencia: qué devolvió el servidor y cuándo.
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from . import CONFIG, LANG, SITE_URL

PARALLEL = CONFIG["transport"]["parallel"]
RETRIES = CONFIG["transport"]["retries"]
TIMEOUT = CONFIG["transport"]["timeout"]

# Cabeceras de navegador. El WAF mira `sec-fetch-*` además del protocolo; sin ellas, el
# API de contenido responde 403 aunque la petición sea h2.
HEADERS = [
    "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/140.0.0.0 Safari/537.36",
    "accept: */*",
    f"accept-language: {LANG}-ES,{LANG};q=0.9,en;q=0.8",
    'sec-ch-ua: "Chromium";v="140", "Not=A?Brand";v="24"',
    "sec-ch-ua-mobile: ?0",
    'sec-ch-ua-platform: "Linux"',
    "sec-fetch-dest: empty",
    "sec-fetch-mode: cors",
    "sec-fetch-site: same-origin",
    f"referer: {SITE_URL}",
]


def _require_curl() -> str:
    curl = shutil.which("curl")
    if not curl:
        raise SystemExit(
            "curl is required: this site answers 403 over HTTP/1.1 and Python's stdlib\n"
            "http client does not speak HTTP/2. Install curl and run again."
        )
    return curl


def fetch(
    jobs: list[tuple[str, Path]], label: str = "", tolerate_missing: bool = False
) -> dict[str, dict[str, str]]:
    """Descarga `(url, destino)` en lotes. Devuelve las cabeceras por URL.

    Escribe cada cuerpo en su destino solo si la transferencia fue `200`: un `403` o un
    `404` dejarían un archivo con la página de error del WAF, que es HTML válido y que el
    parser habría dado por tema vacío. Fallar cerrado, no abierto.

    `tolerate_missing` no afloja esa regla, la reparte: un `404` se anota y sigue, y
    cualquier otro fallo —el `403` del WAF, un `5xx`, una conexión cortada— aborta igual.
    Existe porque el índice de IBM lista una página inexistente a propósito (`Bienvenido`,
    el marcador de la portada), y abortar por ella sería llorar lobo. Cuántos `404` se
    toleran no lo decide el transporte: lo acota `guard.py` sobre el corpus entero.
    """
    if not jobs:
        return {}
    curl = _require_curl()
    results: dict[str, dict[str, str]] = {}

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        config = tmpdir / "curl.cfg"
        lines = []
        for index, (url, _) in enumerate(jobs):
            body = tmpdir / f"{index}.body"
            head = tmpdir / f"{index}.head"
            lines += [f'url = "{url}"', f'output = "{body}"', f'dump-header = "{head}"']
        config.write_text("\n".join(lines), encoding="utf-8")

        command = [
            curl, "--http2", "--compressed", "--parallel",
            "--parallel-max", str(PARALLEL),
            "--retry", str(RETRIES), "--retry-delay", "2", "--retry-connrefused",
            "--location",  # IBM redirige algunos recursos; sin seguirla, un 302 es un fallo

            "--max-time", str(TIMEOUT),
            "-sS", "-K", str(config),
            "-w", "%{exitcode} %{http_code} %{url_effective}\n",
        ]
        for header in HEADERS:
            command += ["-H", header]

        if label:
            print(f"  {label}: {len(jobs)} requests, {PARALLEL} in parallel...")
        done = subprocess.run(command, capture_output=True, text=True)
        if done.returncode != 0 and not done.stdout:
            raise SystemExit(f"curl failed ({done.returncode}): {done.stderr[:400]}")

        codes = {}
        for line in done.stdout.splitlines():
            parts = line.split(" ", 2)
            if len(parts) == 3:
                codes[parts[2]] = (parts[0], parts[1])

        failed = []
        for index, (url, destination) in enumerate(jobs):
            body = tmpdir / f"{index}.body"
            head = tmpdir / f"{index}.head"
            status = codes.get(url, ("?", "?"))[1]
            headers = _parse_headers(head)
            results[url] = {"status": status, **headers}
            if status == "200" and body.exists():
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(body.read_bytes())
            elif tolerate_missing and status == "404":
                results[url]["missing"] = "404"
            else:
                failed.append((url, status))

        if failed:
            detail = "\n".join(f"  - HTTP {status} {url}" for url, status in failed[:10])
            more = f"\n  ... and {len(failed) - 10} more" if len(failed) > 10 else ""
            raise SystemExit(
                f"\n{len(failed)} of {len(jobs)} requests failed — nothing was overwritten:\n"
                f"{detail}{more}\n"
            )
    return results


def _parse_headers(path: Path) -> dict[str, str]:
    """Las cabeceras que interesan, en minúsculas. `curl` acumula los bloques de cada
    redirección en el mismo archivo; gana el último, que es el de la respuesta final."""
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip().lower()
            if key in ("etag", "last-modified", "content-type", "date"):
                out[key] = value.strip()
    return out
