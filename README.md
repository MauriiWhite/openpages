# openpages

Extrae la documentación de **IBM OpenPages 9.1.3 en español** a Markdown verificable.

Entrada: <https://www.ibm.com/docs/es/openpages/9.1.x> (el set de 9.1, que llega hasta el fixpack 9.1.3).
Salida: `output/`, **17 archivos** Markdown con los 2.417 temas del producto, sus 438 tablas,
sus 1.786 bloques de código y sus 1.664 figuras referenciadas, pensados para dárselos a un
modelo.

```bash
uv run openpages                  # crawl → parse → export (~5 min desde cero, 10 s con caché)
uv run openpages verify           # contrasta la fuente contra el entregable, palabra por palabra
uv run openpages crawl --images   # opcional: baja una copia local de las figuras
uv run python tests/test_parse.py # 19 comprobaciones del convertidor
```

Sin dependencias de Python. Necesita `curl` en el sistema, y más abajo está el porqué.

---

## Qué produce

```
output/
  index.md                             índice maestro: cómo elegir archivo + los 2.417 temas
  prompt.md                            instrucciones listas para el agente de Copilot Studio
  01-notas-del-release.md
  02-caracteristicas-nuevas.md
  03.1-guia-del-administrador.md       …03.2 a 03.6, las seis partes de la guía
  04-guia-del-usuario.md
  05.1-guia-de-instalacion-y-despliegue-solo-local.md
  …
```

El número es `<guía>.<parte>`, y solo lleva parte cuando de verdad hay varias: la guía 3 son
seis archivos (`03.1`…`03.6`) y la 4 es uno solo (`04`). Un `.1` que nunca tiene un `.2` al
lado no dice nada. El relleno a dos dígitos existe porque sin él la guía 10 se lista entre
la 1 y la 2.

Cada archivo abre con una cabecera pensada para que un modelo decida **si la respuesta está
acá o en otro archivo**, sin abrir los diecisiete:

```markdown
---
file: "03.2"
guide: Guía del administrador
part: 2 de 6
covers: Tipos de objeto — Configuración de GRC Calculations
chapters: 6
topics: 108
words: 81089
tasks: 63
concepts: 43
references: 1
tables: 50
code_blocks: 33
figures: 227
applies_to: Todos los tipos de despliegue
---

# 03.2 · Guía del administrador — parte 2 de 6

> **Qué hay en este archivo.** «Guía del administrador» de IBM OpenPages 9.1.3, parte 2 de 6:
> capítulos «Tipos de objeto» a «Configuración de GRC Calculations». 108 temas,
> 63 de ellos procedimientos paso a paso, 50 tablas, 33 bloques de código, 227 figuras y
> 81.089 palabras.
>
> **Capítulos:** Tipos de objeto · Perfiles · Configuración de la interfaz de usuario · …
>
> **Se aplica a:** Todos los tipos de despliegue.
>
> **Si lo que buscas no está acá.** El resto de esta guía está en 03.1, 03.3, 03.4, 03.5,
> 03.6. El índice de los 2.417 temas del producto está en `index.md`.

**Términos propios de este archivo:** campo, relación, cuadrícula, filtro, colores, paleta, …
```

Sigue el índice del archivo y después los temas anidados como encabezados, en el orden en
que IBM los lista. Bajo cada encabezado va una línea de ubicación:

```markdown
`Guía del administrador › Seguridad › Reglas de seguridad` · [origen](https://www.ibm.com/…)
```

| | |
| --- | ---: |
| Temas | 2.417 |
| De ellos, fuera del índice de IBM | 44 |
| Archivos Markdown | 17 + índice |
| Markdown | 6,44 MB |
| Figuras referenciadas | 1.664 |
| Tablas | 438 |
| Bloques de código | 1.786 |
| Cobertura del texto de origen | **99,985%** |

## Las cuatro etapas

```
ibm.com/docs/api ──▶ crawl ──▶ data/cache/ ──▶ parse ──▶ data/documents.json ──▶ export ──▶ output/
                       │        data/images/     │                                  │
                   toc.json                  guard.py                            verify
                   sitemap.xml            (aborta si el corpus                (fuente vs. entregable,
                   manifest.json           salió degradado)                    palabra por palabra)
```

| Etapa | Lee | Escribe |
| --- | --- | --- |
| `crawl` | el API de IBM Documentation | `data/cache/`, `toc.json`, `sitemap.xml`, `manifest.json`, `http.json` (y `data/images/` con `--images`) |
| `parse` | `data/cache/` | `data/documents.json`, `data/aliases.json`, `data/runs.jsonl` |
| `export` | `documents.json`, `manifest.json`, `aliases.json` | `output/*.md`, `index.md`, `prompt.md` |
| `verify` | `data/cache/`, `documents.json`, `output/` | nada; informa y falla si algo no cuadra |

---

## Decisiones que costó entender

> Las cifras de esta sección se midieron sobre el corpus 9.0.0, que es donde se tomaron
> estas decisiones. Las vigentes de 9.1.3 están arriba y en «Las dos redes».

### El sitio no se puede leer como una página

`https://www.ibm.com/docs/es/openpages/9.1.x?topic=…` es una SPA: su HTML trae **17
caracteres** de texto visible y el contenido llega después por el API. Descargar las
páginas públicas daría 2.467 archivos vacíos.

El contenido sale de `/docs/api/v1/content/<href>?parsebody=true&lang=es`, y el árbol
entero de una sola petición a `/docs/api/v1/toc/SSFUEU_9.1?lang=es`.

### HTTP/2 no es una optimización, es el requisito

MEDIDO, con las mismas cabeceras y desde la misma IP:

| Protocolo | Respuesta |
| --- | --- |
| HTTP/1.1 | `403` |
| HTTP/2 | `200` |

El WAF de IBM mira la versión del protocolo. `http.client` de la biblioteca estándar solo
habla HTTP/1.1, así que **no sirve para este sitio**. El transporte es `curl --http2
--parallel`, que ya está instalado y multiplexa sobre una sola conexión.

### El índice de IBM no lista todo lo que IBM publica

El árbol declara 2.467 temas. Siguiendo los enlaces del **cuerpo** de esos temas aparecen
86 destinos más del mismo producto. Cuarenta son el mismo tema bajo otro nombre de archivo
—IBM renombró archivos al traducir y los enlaces del texto quedaron apuntando al nombre
inglés—, y se detectan por el `sha256` de su Markdown para reapuntar esos 1.306 enlaces.

Los otros **46 son contenido que no está en ninguna otra parte**: 194.362 caracteres, entre
ellos el diseñador de vistas completo (vistas de cuadrícula, de tarea, de creación, de
informe), los diagramas de gráfico, las acciones sobre campos de relación y la integración
de la API REST con WebSphere Liberty. Van al final de su guía, marcados como tales.

Por eso el recorrido no termina con el índice: sigue los enlaces internos hasta que no
aparecen destinos nuevos. La navegación del pie (`<aside>`) se recorta antes de buscar,
porque sus destinos salen del propio índice y solo arrastran alias.

### Las figuras se enlazan, no se copian

Lo que el corpus garantiza de una figura es su **procedencia**: quien lea el documento tiene
que poder abrir la imagen tal como la publica IBM, sin intermediarios. Y lo que un modelo
puede leer de ella es su **texto alternativo en español**, que sí va en el Markdown, muchas
veces con una descripción completa del diagrama.

El costo es explícito y está medido: `https://www.ibm.com/docs/es/…/security_levels.jpg`
responde **403** a cualquier cliente que no venga del propio sitio de IBM, así que el enlace
vale como referencia verificable y no como vista previa. Para verlas:

```bash
uv run openpages crawl --images && uv run openpages export
```

Eso baja las 708 figuras a `data/images/`, las copia a `output/imagenes/` y reapunta cada
una a su copia local. Se guardan bajo la ruta que IBM les da porque el mismo nombre de
archivo se repite entre guías: `settings_menu_icon_task_focused_ui.jpg` está en cuatro.

### Los bloques dentro de una celda necesitan `<br>`

El **37,7% de las 10.291 celdas** del corpus tiene hijos de bloque: 2.775 `<p>`, 1.553
`<div>`, 216 `<ul>`. Una tabla Markdown vive en una línea, así que sin separador
`<td>Tabla principal<p>Por ejemplo…</p></td>` salía como `Tabla principalPor ejemplo` —una
palabra que no existe. Fue la pérdida más extendida del proyecto y la encontró `verify`,
no una invariante de conteo.

### El HTML es DITA, y eso es una suerte

Lo que sirve el API es DITA compilado y envuelto en clases de Carbon Design System. La
semántica original sigue ahí, en los nombres de clase:

| Original | Markdown | Ocurrencias |
| --- | --- | ---: |
| `uicontrol`, `wintitle` | `**negrita**` | 15.801 |
| `codeph`, `filepath`, `varname`, `cmdname` | `` `código` `` | 13.178 |
| `<aside>`/`<nav>` | se descarta | 2.428 |
| `pre.codeblock` | bloque cercado, con lenguaje si la señal es clara | 1.759 |
| `div.note` | `> **Nota:** …` | 1.128 |
| `img[src*=pill_]` | el texto del despliegue, no una imagen | 922 |
| `<table>` con `<thead>` | tabla Markdown con encabezado y título | 529 |
| `<dl>`/`<dt>`/`<dd>` | ítem con el término en negrita | 517 |

### El lenguaje de los bloques de código se deduce, y solo si es inequívoco

IBM no lo declara: los 1.759 bloques son `<pre class="codeblock">` a secas. Se etiquetan
los que dan una señal clara (`sql`, `xml`, `bash`, `bat`, `properties`, `json`, `java`) —
562 de ellos—. El resto queda sin etiqueta: una etiqueta equivocada colorea mal y engaña,
y la mitad de los no etiquetados son órdenes de una línea o salida de consola, que no
tienen lenguaje.

### El archivo se numera `<guía>.<parte>`, y la parte solo si existe

`03.2-guia-del-administrador.md` es la parte 2 de la guía 3; `04-guia-del-usuario.md` es la
guía 4 entera. Es como se citan entre personas («mándame la 3.2») y lo que hace que el
índice maestro, el front matter y el encabezado del archivo digan todos lo mismo.

### `prompt.md` se genera, no se escribe

Lleva las cifras del corpus —cuántos temas, cuántos procedimientos, cuántos son exclusivos
de instalación local— porque un prompt que le diga al agente «2.511 temas» cuando el corpus
tiene otros tantos le está mintiendo sobre su propia fuente. Cada reextracción lo rehace.

Lo único que el paquete no puede saber solo es el tipo de despliegue de la instalación: va
marcado `>>> AJUSTA ESTO <<<` para que se fije a mano antes de publicar el agente.

### Los términos propios salen de contrastar los archivos entre sí

No hay lista de palabras vacías: «para» y «que» están en los diecisiete archivos, así que su
peso inverso es cero y se caen solas. Lo que queda es la jerga del producto —`opbackup`,
`sysdba`, `jsonata`, `rabbitmq`, `saml`, `rcsa`— que es justo lo que un buscador léxico
necesita para elegir archivo y lo que no aparece en ningún título de capítulo.

Se recorta antes el código, el código en línea y los destinos de los enlaces: sin eso la
lista la encabezaban `op_grc_admin` y los nombres de archivo de las capturas de pantalla.

### Una guía por archivo, no un capítulo

Por capítulo eran 158 archivos. Ninguna ganancia para el modelo: todo canal de ingesta
trocea el documento igual, así que el número de archivos es un problema de administración,
no de recuperación. Lo que sí decide el rendimiento es que **cada trozo diga dónde está**,
y de eso se encarga la línea de ubicación bajo cada encabezado.

Una guía se parte solo si pasa de `export.max_bytes` (700 KB), y el corte cae siempre entre
capítulos: partir dentro de uno dejaría media configuración de seguridad en cada archivo.

### Lo que no se toca

Las erratas del original se conservan: `deIBM OpenPages`, `Java™y`, `Thomson Reutersy`,
`OpenPages .` son de IBM, están así en su HTML y el navegador las muestra igual.
Corregirlas sería inventar contenido. Lo mismo con `[Link title](URL)`, que es un ejemplo
de sintaxis que la propia documentación imprime.

---

## Las dos redes

### `guard.py` — cuenta, y aborta antes de escribir

| Invariante | Cota | Medido |
| --- | --- | ---: |
| Temas por guía | `config.toml` | 1 a 1.151 |
| Temas del índice sin descargar | `<= 3` | 2 |
| Con título | `>= 99%` | 100% |
| Con cuerpo (>80 caracteres) | `>= 98%` | 99,5% |
| En español | `>= 97%` | 99,8% |
| Tablas | `>= 395` | 438 |
| Figuras | `>= 1.500` | 1.664 |
| Bloques de código | `>= 1.600` | 1.786 |
| Temas del sitemap de IBM presentes | todos | 2.294 de 2.294 |
| Variación de volumen entre corridas | `<= ±25%` | — |

Para forzar —solo cuando ya entendiste por qué se violó—:

```bash
OPENPAGES_FORCE=1 uv run openpages parse
```

### `verify` — contrasta, palabra por palabra

Los conteos no pueden ver una pérdida *dentro* de un tema. `verify` compara el texto del
HTML de origen contra el Markdown producido:

```
source text: 862.192 words · not in the Markdown: 132 · coverage 99,9847%
IBM's sitemap: 2294 topics, 0 missing from the corpus
package: 1664 figures (linked to ibm.com, 0 unresolved), 9240 internal links (13 unresolved)
```

Las 132 palabras que faltan son las que IBM escribe pegadas a una etiqueta
(`<span>Thomson Reuters</span>y`): se transcriben tal cual, así que aparecen como ausentes
sin serlo. Los 13 enlaces son texto literal de IBM dentro de bloques de código.

## Convenciones

| Qué | Idioma | Por qué |
| --- | --- | --- |
| Código: identificadores, funciones | Inglés | Convención del lenguaje |
| Claves de JSON y del front matter | **Inglés** | Son contrato de datos, no prosa |
| Texto de la documentación | **Español, intacto** | Se transcribe tal como lo publica IBM |
| Salida de la consola | Inglés | Va en el mismo idioma que el código |
| Documentación y comentarios | **Español** | Es para quien mantiene el proyecto |

## Lo que no está

- **Revalidación condicional (`ETag`).** Una corrida completa cuesta cinco minutos; el
  caché en disco cubre el resto.
- **Detección de cambios entre corridas.** `data/runs.jsonl` guarda las métricas de cada
  corrida y `guard` acota la deriva, pero no hay changelog por tema.
- **El material que no es prosa.** IBM publica 17 archivos sueltos —los PDF de la API REST
  y de los desencadenantes, el `swagger2.json`, los ZIP del SDK y el Javadoc—. Están
  inventariados en `output/index.md` y enlazados a su origen, pero no entran al corpus.
- **Los vídeos de 39 temas.** Se conservan como enlace con su descripción en español; su contenido
  está en píxeles y no se interpreta.
- **Solo 9.1.3.** IBM publica 8.3.0, 9.0.0 y 9.2.0 en español. Cambiar de versión es
  `[source]` en `config.toml` (versión, clave de producto, URL), volver a correr y
  re-medir las cotas de `guard.py` y `min_topics` si las invariantes saltan.
