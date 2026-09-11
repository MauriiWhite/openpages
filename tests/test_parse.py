"""Comprobación del convertidor. Se corre sola: `uv run python tests/test_parse.py`.

Cada caso es una forma que el HTML de IBM trae de verdad y que costó acertar. Si alguna
se rompe, el corpus sale peor sin que ninguna invariante de `guard.py` lo note: las cotas
cuentan tablas y figuras, no si una negrita anidada salió con los asteriscos a la vista.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from openpages.parse import parse_topic  # noqa: E402


def md(html: str) -> str:
    return parse_topic(html)["markdown"]


def test_title_leaves_the_body():
    document = parse_topic('<h1 class="topictitle1">Configurar X</h1><p>Texto.</p>')
    assert document["title"] == "Configurar X"
    assert document["markdown"] == "Texto."


def test_headings_are_relative_to_the_topic():
    # El `<h2>` del original es el primer nivel DENTRO del tema: `export` lo baja después
    # según a qué profundidad quede el tema en su archivo.
    assert md('<h2 class="sectiontitle">Procedimiento</h2>') == "# Procedimiento"
    assert md("<h3>Sub</h3>") == "## Sub"


def test_table_promotes_its_header_and_keeps_the_caption():
    out = md(
        '<table><caption><span class="tablecap">Tabla 1. Campos</span></caption>'
        "<thead><tr><th>Nombre</th><th>Uso</th></tr></thead>"
        "<tbody><tr><td>A</td><td>B</td></tr></tbody></table>"
    )
    assert "**Tabla 1. Campos**" in out
    assert "| Nombre | Uso |" in out and "| --- | --- |" in out and "| A | B |" in out


def test_colspan_keeps_the_row_width():
    out = md("<table><tbody><tr><td colspan='2'>ancho</td><td>x</td></tr></tbody></table>")
    assert "| ancho |  | x |" in out


def test_pipe_inside_a_cell_does_not_break_the_table():
    out = md("<table><tbody><tr><td>a|b</td></tr></tbody></table>")
    assert "| a\\|b |" in out


def test_nested_bold_is_not_emitted_twice():
    # El original anida `<strong>` con `uicontrol` dentro; `****` no es negrita en GFM.
    out = md('<p><strong>Tipo nuevo: <span class="ph uicontrol">Amenaza</span></strong></p>')
    assert out == "**Tipo nuevo: Amenaza**"


def test_menu_cascade_keeps_one_level_of_bold():
    out = md(
        '<p><span class="ph menucascade"><span class="ph uicontrol">Archivo</span>'
        '<abbr title="y luego"> &gt; </abbr><span class="ph uicontrol">Salir</span></span></p>'
    )
    assert out == "**Archivo** > **Salir**"


def test_placeholders_that_look_like_tags_are_escaped():
    # 139 casos reales: `<OP_HOME>`, `<server_name>`. IBM los escribe escapados en su
    # HTML; sin volver a escaparlos en Markdown, el renderizador se los traga como una
    # etiqueta y el marcador desaparece de la página.
    assert md("<p>Vaya a &lt;OP_HOME&gt;/bin</p>") == "Vaya a \\<OP_HOME>/bin"


def test_code_keeps_its_content_literal():
    assert md('<pre class="codeblock"><code>a &lt;b&gt; c</code></pre>') == "```\na <b> c\n```"
    assert md('<p>Use <span class="ph filepath">/opt/op</span></p>') == "Use `/opt/op`"


def test_note_becomes_a_quote_with_its_label():
    out = md(
        '<div class="note cds--inline-notification--warning">'
        '<span class="notetitle">Aviso:</span> No borre el archivo.</div>'
    )
    assert out == "> **Aviso:** No borre el archivo."


def test_untitled_note_still_says_what_kind_it_is():
    out = md('<div class="note cds--inline-notification--error">Falla.</div>')
    assert out == "> **Atención:** Falla."


def test_nested_steps_keep_their_nesting():
    out = md(
        '<ol class="steps"><li class="step"><span class="cmd">Uno</span>'
        '<ol class="substeps"><li class="substep"><span class="cmd">Uno.a</span></li></ol>'
        "</li><li class='step'><span class='cmd'>Dos</span></li></ol>"
    )
    assert out == "1. Uno\n\n   1. Uno.a\n2. Dos"


def test_several_dd_belong_to_the_same_dt():
    out = md(
        '<dl><dt class="dlterm">Campo</dt><dd>Valor: A</dd><dd>Rango: 1-9</dd></dl>'
    )
    assert out == "- **Campo**\n\n  Valor: A\n\n  Rango: 1-9"


def test_navigation_is_dropped_and_figures_are_kept():
    out = md(
        '<figure><figcaption>Figura 1. Panel</figcaption>'
        '<img src="/docs/es/x/p.png" alt="El panel"></figure>'
        '<aside><nav><a href="/docs/es/y.html">Tema principal</a></nav></aside>'
    )
    assert out == "*Figura 1. Panel*\n\n![El panel](https://www.ibm.com/docs/es/x/p.png)"


def test_in_page_anchors_keep_the_text_and_drop_the_link():
    assert md('<p>Vea <a href="#wp1030174">Cuadro 1</a>.</p>') == "Vea Cuadro 1."
    out = md('<p><a href="/docs/es/x/t.html">Tema</a></p>')
    assert out == "[Tema](https://www.ibm.com/docs/es/x/t.html)"


def test_last_modified_is_metadata_not_body():
    document = parse_topic(
        '<div id="lastModifiedDate"><span>Last Updated</span>: 2025-02-13</div><p>Hola</p>'
    )
    assert document["last_modified"] == "2025-02-13"
    assert document["markdown"] == "Hola"


def test_blocks_inside_a_cell_are_separated():
    # El 37,7% de las 10.291 celdas del corpus tiene bloques dentro. Sin separarlos,
    # `Tabla principal` y `Por ejemplo:` salían como una palabra que no existe.
    out = md(
        "<table><tbody><tr>"
        "<td>Tabla principal<p>Por ejemplo: <code>RT_X</code></p></td>"
        "<td>Opciones<ul><li>uno</li><li>dos</li></ul></td>"
        "</tr></tbody></table>"
    )
    assert "| Tabla principal<br>Por ejemplo: `RT_X` | Opciones<br>• uno<br>• dos |" in out


def test_a_wrapper_div_in_a_header_cell_adds_no_break():
    out = md('<table><thead><tr><th><div class="x"><p>ESG</p></div></th></tr></thead></table>')
    assert "| ESG |" in out and "<br>" not in out


def test_code_is_tagged_only_when_the_signal_is_unambiguous():
    from openpages.parse import language

    assert language("SELECT * FROM RT_RISK") == "sql"
    assert language('<?xml version="1.0"?><a/>') == "xml"
    assert language("export OP_HOME=/opt/op") == "bash"
    assert language("keystore.path=/opt/k\nkeystore.pass=x\n") == "properties"
    # Sin señal clara no se etiqueta: una etiqueta equivocada es peor que ninguna.
    assert language("1 record(s) selected.") == ""
    assert language("EUR,0.1789,2/21/2025") == ""


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for test in tests:
        test()
        print(f"  ok  {test.__name__}")
    print(f"{len(tests)} checks passed")
