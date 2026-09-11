---
product: IBM OpenPages 9.0.0
product_key: SSFUEU_9.0.0
file: 10
guide: Guía del creador de informes
covers: Guía del creador de informes — Avisos
chapters: 22
topics: 252
words: 63238
tasks: 72
concepts: 173
references: 1
tables: 65
code_blocks: 173
figures: 170
applies_to: sin declarar
updated: 2025-09-26
lang: es
source: https://www.ibm.com/docs/es/openpages/9.0.0?topic=report-authors-guide
extracted: 2026-09-11
---

# 10 · Guía del creador de informes

> **Qué hay en este archivo.** «Guía del creador de informes» de IBM OpenPages 9.0.0, completa: 22 capítulos. 252 temas, 72 de ellos procedimientos paso a paso, 65 tablas, 173 bloques de código, 170 figuras y 63.238 palabras.
>
> **Capítulos:** Guía del creador de informes · Modelos de bases de datos · Modelos de datos del entorno · Modelo de objeto · Entorno de elaboración de informes · Optimización del rendimiento · Idioma de diseño de informe · Trabajar con datos relacionales · Trabajar con entidades de negocios · Trabajar con objetos compartidos · Trabajar con objetos recursivos · Internacionalización y localización · y 10 más.
>
> **Si lo que buscas no está acá.** El índice de los 2.511 temas del producto, con su archivo y su ancla, está en `index.md`.

**Términos propios de este archivo:** listmain, cruzadas, arrastre, caja, suelte, unión, explorador, filtro, insertables, asunto, expresión, numérico, regional, febrero.

## Índice de este archivo

- [Guía del creador de informes](#guía-del-creador-de-informes)
- [Modelos de bases de datos](#modelos-de-bases-de-datos)
  - [Modelo de datos de aplicación](#modelo-de-datos-de-aplicación)
  - [Diseño de tabla de informes](#diseño-de-tabla-de-informes)
    - [Tablas de objetos](#tablas-de-objetos)
    - [Vistas de objeto](#vistas-de-objeto)
    - [Tablas de enumeración](#tablas-de-enumeración)
    - [Tabla de relaciones](#tabla-de-relaciones)
- [Modelos de datos del entorno](#modelos-de-datos-del-entorno)
  - [Modelo de datos relacional](#modelo-de-datos-relacional)
    - [Terminología de modelado relacional](#terminología-de-modelado-relacional)
    - [Vista de carpetas de un modelo de datos relacional](#vista-de-carpetas-de-un-modelo-de-datos-relacional)
- [Modelo de objeto](#modelo-de-objeto)
  - [Terminología del modelo de objeto](#terminología-del-modelo-de-objeto)
  - [Características del modelo de objeto](#características-del-modelo-de-objeto)
- [Entorno de elaboración de informes](#entorno-de-elaboración-de-informes)
  - [Modelos de entorno](#modelos-de-entorno)
  - [Paquetes de entorno](#paquetes-de-entorno)
  - [Espacios de nombres](#espacios-de-nombres)
    - [Espacio de nombres predeterminado](#espacio-de-nombres-predeterminado)
    - [Convenciones de denominación para espacios de nombres](#convenciones-de-denominación-para-espacios-de-nombres)
  - [Adición de códigos de configuración regional y definición de una configuración regional de orden de clasificación](#adición-de-códigos-de-configuración-regional-y-definición-de-una-configuración-regional-de-orden-de-clasificación)
  - [Las carpetas de nivel superior del modelo relacional](#las-carpetas-de-nivel-superior-del-modelo-relacional)
    - [La carpeta Seguimiento de auditoría (Modelo relacional)](#la-carpeta-seguimiento-de-auditoría-modelo-relacional)
    - [La carpeta Campos calculados (modelo relacional)](#la-carpeta-campos-calculados-modelo-relacional)
    - [La carpeta Enumeraciones (Modelo relacional)](#la-carpeta-enumeraciones-modelo-relacional)
      - [Series enumeradas (modelo relacional)](#series-enumeradas-modelo-relacional)
    - [La carpeta Objetos GRC (modelo relacional)](#la-carpeta-objetos-grc-modelo-relacional)
      - [La carpeta SOXBusEntity (Modelo relacional)](#la-carpeta-soxbusentity-modelo-relacional)
      - [Los asuntos de consulta GPC (modelo relacional)](#los-asuntos-de-consulta-gpc-modelo-relacional)
      - [La carpeta Objeto (modelo relacional)](#la-carpeta-objeto-modelo-relacional)
      - [Elementos de consulta de campos de enumeración (modelo relacional)](#elementos-de-consulta-de-campos-de-enumeración-modelo-relacional)
    - [La carpeta Objetos GRC autónomos (modelo relacional)](#la-carpeta-objetos-grc-autónomos-modelo-relacional)
      - [Las carpetas Objeto secundario (modelo relacional)](#las-carpetas-objeto-secundario-modelo-relacional)
    - [La carpeta Varios (modelo relacional)](#la-carpeta-varios-modelo-relacional)
      - [La carpeta Divisas (modelo relacional)](#la-carpeta-divisas-modelo-relacional)
      - [Carpeta Periodo de elaboración de informes (modelo relacional)](#carpeta-periodo-de-elaboración-de-informes-modelo-relacional)
      - [La carpeta Avanzado (modelo relacional)](#la-carpeta-avanzado-modelo-relacional)
    - [La carpeta Seguridad (modelo relacional)](#la-carpeta-seguridad-modelo-relacional)
- [Optimización del rendimiento](#optimización-del-rendimiento)
  - [Filtrado de entidades de negocios de nivel superior](#filtrado-de-entidades-de-negocios-de-nivel-superior)
  - [Filtrado de periodos de elaboración de informes](#filtrado-de-periodos-de-elaboración-de-informes)
  - [Ignorar el índice](#ignorar-el-índice)
  - [Rendimiento de dirección de la consulta](#rendimiento-de-dirección-de-la-consulta)
  - [Adición de nuevos índices](#adición-de-nuevos-índices)
  - [El valor Uso para la información de parámetro](#el-valor-uso-para-la-información-de-parámetro)
- [Idioma de diseño de informe](#idioma-de-diseño-de-informe)
  - [Establecimiento del entorno local en OpenPages](#establecimiento-del-entorno-local-en-openpages)
    - [Soporte de configuración regional e idioma](#soporte-de-configuración-regional-e-idioma)
  - [Configuración del entorno local en IBM Cognos Analytics](#configuración-del-entorno-local-en-ibm-cognos-analytics)
- [Trabajar con datos relacionales](#trabajar-con-datos-relacionales)
  - [Convenios de sintaxis](#convenios-de-sintaxis)
  - [Trabajar con contenedores de datos](#trabajar-con-contenedores-de-datos)
    - [Trabajar con listas](#trabajar-con-listas)
      - [Selección de columnas de datos](#selección-de-columnas-de-datos)
    - [Trabajar con tablas de referencias cruzadas](#trabajar-con-tablas-de-referencias-cruzadas)
      - [Selección de elementos de datos](#selección-de-elementos-de-datos)
    - [Trabajar con gráficos](#trabajar-con-gráficos)
      - [Creación de un gráfico](#creación-de-un-gráfico)
  - [Trabajar con campos enumerados](#trabajar-con-campos-enumerados)
    - [La estructura de la carpeta Campos enumerados](#la-estructura-de-la-carpeta-campos-enumerados)
    - [Uso de campos enumerados en un informe](#uso-de-campos-enumerados-en-un-informe)
  - [Trabajar con campos de fecha](#trabajar-con-campos-de-fecha)
  - [Trabajar con campos de moneda](#trabajar-con-campos-de-moneda)
    - [Asuntos de consulta de la divisa del sistema](#asuntos-de-consulta-de-la-divisa-del-sistema)
    - [Estructura de carpetas de los campos de moneda](#estructura-de-carpetas-de-los-campos-de-moneda)
    - [Configuración del uso de los campos de divisa en un informe](#configuración-del-uso-de-los-campos-de-divisa-en-un-informe)
  - [Adición de solicitudes](#adición-de-solicitudes)
    - [Creación de una página de solicitudes](#creación-de-una-página-de-solicitudes)
    - [Adición de una solicitud de periodo de elaboración de informes](#adición-de-una-solicitud-de-periodo-de-elaboración-de-informes)
      - [Pasar el parámetro de periodo de elaboración de informes de OpenPages](#pasar-el-parámetro-de-periodo-de-elaboración-de-informes-de-openpages)
    - [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios)
    - [Adición de una solicitud de valor enumerado de selección única](#adición-de-una-solicitud-de-valor-enumerado-de-selección-única)
    - [Adición de una solicitud de valor enumerado de selección múltiple](#adición-de-una-solicitud-de-valor-enumerado-de-selección-múltiple)
      - [Adición de un valor estático Todo a una solicitud de valor enumerado de selección múltiple](#adición-de-un-valor-estático-todo-a-una-solicitud-de-valor-enumerado-de-selección-múltiple)
    - [Adición de una solicitud de fecha](#adición-de-una-solicitud-de-fecha)
    - [Adición de una solicitud de rango de fechas](#adición-de-una-solicitud-de-rango-de-fechas)
    - [Adición de una solicitud de opciones estáticas](#adición-de-una-solicitud-de-opciones-estáticas)
    - [Adición de una solicitud en cascada](#adición-de-una-solicitud-en-cascada)
    - [Adición de solicitudes para asuntos de consulta](#adición-de-solicitudes-para-asuntos-de-consulta)
  - [Adición de campos de texto enriquecido](#adición-de-campos-de-texto-enriquecido)
  - [Adición de imágenes e iconos](#adición-de-imágenes-e-iconos)
  - [Adición de cálculos](#adición-de-cálculos)
  - [Ordenación de datos](#ordenación-de-datos)
    - [Uso de la ordenación simple](#uso-de-la-ordenación-simple)
    - [Uso de la ordenación avanzada](#uso-de-la-ordenación-avanzada)
    - [Uso de la ordenación personalizada](#uso-de-la-ordenación-personalizada)
    - [Uso de la ordenación solicitada](#uso-de-la-ordenación-solicitada)
  - [Filtrado de datos](#filtrado-de-datos)
    - [Uso de mapas de parámetros para filtrado](#uso-de-mapas-de-parámetros-para-filtrado)
    - [Filtrado del ID de periodo de elaboración de informes](#filtrado-del-id-de-periodo-de-elaboración-de-informes)
    - [Filtrado de una enumeración](#filtrado-de-una-enumeración)
  - [Agrupación de datos](#agrupación-de-datos)
    - [Agrupación de datos en un informe de lista](#agrupación-de-datos-en-un-informe-de-lista)
    - [Creación de una cabecera de grupo de lista](#creación-de-una-cabecera-de-grupo-de-lista)
    - [Establecimiento de la extensión de nivel para una columna](#establecimiento-de-la-extensión-de-nivel-para-una-columna)
  - [Agregación de datos](#agregación-de-datos)
  - [Uso del formateo condicional](#uso-del-formateo-condicional)
    - [Uso del formateo condicional para entradas de sangría](#uso-del-formateo-condicional-para-entradas-de-sangría)
    - [Resaltar datos condicionalmente](#resaltar-datos-condicionalmente)
  - [Colores del gráfico de barras](#colores-del-gráfico-de-barras)
    - [Visualización de la variación de color de barra con valores visualizados automáticamente](#visualización-de-la-variación-de-color-de-barra-con-valores-visualizados-automáticamente)
    - [Visualización de la consistencia del color de barra con modificación de informe para los nuevos valores](#visualización-de-la-consistencia-del-color-de-barra-con-modificación-de-informe-para-los-nuevos-valores)
    - [Edición de colores de barra](#edición-de-colores-de-barra)
  - [Creación de uniones](#creación-de-uniones)
    - [Creación de uniones directa](#creación-de-uniones-directa)
    - [Creación de uniones indirectas](#creación-de-uniones-indirectas)
  - [Creación de informes de acceso a detalles](#creación-de-informes-de-acceso-a-detalles)
    - [Creación de un informe padre](#creación-de-un-informe-padre)
    - [Adición de un informe de acceso a detalles al padre](#adición-de-un-informe-de-acceso-a-detalles-al-padre)
  - [Adición de enlaces CrossTrack](#adición-de-enlaces-crosstrack)
    - [Adición de enlaces CrossTrack a informes autónomos y padres](#adición-de-enlaces-crosstrack-a-informes-autónomos-y-padres)
    - [Adición de enlaces CrossTrack a informes de acceso a detalles](#adición-de-enlaces-crosstrack-a-informes-de-acceso-a-detalles)
  - [Creación de un informe maestro-detalle](#creación-de-un-informe-maestro-detalle)
    - [Creación de relaciones entre listas maestras e incorporadas](#creación-de-relaciones-entre-listas-maestras-e-incorporadas)
    - [Formateo de listas integradas](#formateo-de-listas-integradas)
  - [Adición de micrográficos](#adición-de-micrográficos)
- [Trabajar con entidades de negocios](#trabajar-con-entidades-de-negocios)
  - [El asunto de consulta SOXBUSENTITY_GPC](#el-asunto-de-consulta-soxbusentity_gpc)
  - [Jerarquía de entidad definida por el usuario](#jerarquía-de-entidad-definida-por-el-usuario)
  - [Objetos Componente GPC](#objetos-componente-gpc)
  - [El modelo de datos GPC](#el-modelo-de-datos-gpc)
  - [Filtrado de entidades de negocios relacionales](#filtrado-de-entidades-de-negocios-relacionales)
    - [Filtrado utilizando la vía de acceso completa](#filtrado-utilizando-la-vía-de-acceso-completa)
      - [Campos de contexto de entidad relacional](#campos-de-contexto-de-entidad-relacional)
    - [Filtrado de la extensión de jerarquía](#filtrado-de-la-extensión-de-jerarquía)
    - [Filtrado utilizando solicitudes en cascada](#filtrado-utilizando-solicitudes-en-cascada)
    - [Referencia rápida para visualización y filtrado de datos](#referencia-rápida-para-visualización-y-filtrado-de-datos)
- [Trabajar con objetos compartidos](#trabajar-con-objetos-compartidos)
  - [Agregación de datos para objetos compartidos](#agregación-de-datos-para-objetos-compartidos)
  - [Creación de un informe de agregación para objetos compartidos](#creación-de-un-informe-de-agregación-para-objetos-compartidos)
  - [Recuento de objetos compartidos en informes de gráfico](#recuento-de-objetos-compartidos-en-informes-de-gráfico)
  - [Listado de objetos compartidos en los informes de lista](#listado-de-objetos-compartidos-en-los-informes-de-lista)
- [Trabajar con objetos recursivos](#trabajar-con-objetos-recursivos)
- [Internacionalización y localización](#internacionalización-y-localización)
  - [Conversión de datos](#conversión-de-datos)
    - [Datos estáticos](#datos-estáticos)
      - [Traducción de datos de etiqueta dinámicos](#traducción-de-datos-de-etiqueta-dinámicos)
      - [Uso de una variable de condición para traducir datos de campo de texto fijo](#uso-de-una-variable-de-condición-para-traducir-datos-de-campo-de-texto-fijo)
      - [Traducción de un texto de botón](#traducción-de-un-texto-de-botón)
      - [Conversión de texto estático en solicitudes](#conversión-de-texto-estático-en-solicitudes)
    - [Datos de aplicación](#datos-de-aplicación)
      - [Traducción de series enumeradas de valor único](#traducción-de-series-enumeradas-de-valor-único)
        - [Estructura de carpetas del entorno para enumeraciones de valor único](#estructura-de-carpetas-del-entorno-para-enumeraciones-de-valor-único)
        - [Definiciones de campo para enumeraciones de valor único](#definiciones-de-campo-para-enumeraciones-de-valor-único)
      - [Traducción de series enumeradas multivalor](#traducción-de-series-enumeradas-multivalor)
        - [Estructura de carpetas del entorno para enumeraciones multivalor](#estructura-de-carpetas-del-entorno-para-enumeraciones-multivalor)
        - [Definiciones de campo para enumeraciones multivalor](#definiciones-de-campo-para-enumeraciones-multivalor)
      - [Conversión de campos de fecha utilizando formatos de fecha predefinida](#conversión-de-campos-de-fecha-utilizando-formatos-de-fecha-predefinida)
      - [Conversión de campos de fecha utilizando formatos de fecha personalizados](#conversión-de-campos-de-fecha-utilizando-formatos-de-fecha-personalizados)
      - [Conversión de los campos de moneda utilizando formatos predefinidos](#conversión-de-los-campos-de-moneda-utilizando-formatos-predefinidos)
      - [Conversión de campos de moneda utilizando formatos personalizados](#conversión-de-campos-de-moneda-utilizando-formatos-personalizados)
  - [Uso de mapas de parámetros con filtros de serie enumerada traducidos](#uso-de-mapas-de-parámetros-con-filtros-de-serie-enumerada-traducidos)
- [Uso de las funciones de base de datos predefinida](#uso-de-las-funciones-de-base-de-datos-predefinida)
  - [Pasar parámetros](#pasar-parámetros)
  - [Determinación de un ID de tipo de objeto](#determinación-de-un-id-de-tipo-de-objeto)
    - [Uso de SQL para obtener ID de objeto](#uso-de-sql-para-obtener-id-de-objeto)
    - [Uso de un informe para obtener ID de objeto](#uso-de-un-informe-para-obtener-id-de-objeto)
  - [Determinación de los nombres de tabla de base de datos](#determinación-de-los-nombres-de-tabla-de-base-de-datos)
    - [Obtención de una lista de nombres de tabla RT](#obtención-de-una-lista-de-nombres-de-tabla-rt)
  - [Determinación de los nombres de columna de la tabla de base de datos](#determinación-de-los-nombres-de-columna-de-la-tabla-de-base-de-datos)
  - [Uso de funciones generales](#uso-de-funciones-generales)
    - [Conversión de enumeraciones multivalor en nombres](#conversión-de-enumeraciones-multivalor-en-nombres)
    - [Conversiones de enumeraciones de valor único en nombres](#conversiones-de-enumeraciones-de-valor-único-en-nombres)
    - [Recuento del número de apariciones de texto](#recuento-del-número-de-apariciones-de-texto)
    - [Determinación de una relación de entorno entre objetos](#determinación-de-una-relación-de-entorno-entre-objetos)
    - [Determinación de una relación padre primaria entre objetos](#determinación-de-una-relación-padre-primaria-entre-objetos)
    - [Determinación de una relación entre objetos](#determinación-de-una-relación-entre-objetos)
    - [Formateo del valor de divisa](#formateo-del-valor-de-divisa)
    - [Obtención del nombre de visualización de Actor por ID](#obtención-del-nombre-de-visualización-de-actor-por-id)
    - [Obtención del nombre de visualización de Actor por ID de Actor](#obtención-del-nombre-de-visualización-de-actor-por-id-de-actor)
    - [Obtención del nombre de visualización de actor por ID de sesión](#obtención-del-nombre-de-visualización-de-actor-por-id-de-sesión)
    - [Obtención del texto clave externo](#obtención-del-texto-clave-externo)
    - [Obtención de los atributos de un objeto padre primario](#obtención-de-los-atributos-de-un-objeto-padre-primario)
    - [Obtención de atributos directos de un objeto padre primario](#obtención-de-atributos-directos-de-un-objeto-padre-primario)
    - [Obtención de la tasa de cambio](#obtención-de-la-tasa-de-cambio)
    - [Obtención de los ID de recurso de vía de acceso de árbol](#obtención-de-los-id-de-recurso-de-vía-de-acceso-de-árbol)
    - [Resumen de enumeraciones multivalor en una lista](#resumen-de-enumeraciones-multivalor-en-una-lista)
  - [Uso de las funciones dependientes del tiempo](#uso-de-las-funciones-dependientes-del-tiempo)
    - [Obtención del valor de campo personalizado por ID](#obtención-del-valor-de-campo-personalizado-por-id)
    - [Obtención del valor de campo personalizado por nombre](#obtención-del-valor-de-campo-personalizado-por-nombre)
    - [Obtención de la descripción del campo del sistema](#obtención-de-la-descripción-del-campo-del-sistema)
    - [Obtención de la vía de acceso completa del campo del sistema](#obtención-de-la-vía-de-acceso-completa-del-campo-del-sistema)
    - [Obtención del nombre de campo del sistema](#obtención-del-nombre-de-campo-del-sistema)
    - [Obtención del ID de carpeta padre del campo del sistema](#obtención-del-id-de-carpeta-padre-del-campo-del-sistema)
- [Formateo de informes para salida](#formateo-de-informes-para-salida)
  - [Configuración del informe para la salida de PDF](#configuración-del-informe-para-la-salida-de-pdf)
  - [Inclusión de solicitudes en línea para salida en PDF](#inclusión-de-solicitudes-en-línea-para-salida-en-pdf)
  - [Formateo del informe para la salida de PDF](#formateo-del-informe-para-la-salida-de-pdf)
  - [Formato para salida de Microsoft Excel](#formato-para-salida-de-microsoft-excel)
  - [Formateo para salida en CSV](#formateo-para-salida-en-csv)
- [Elaboración de informes](#elaboración-de-informes)
  - [Valores manuales de IBM Cognos Configuration](#valores-manuales-de-ibm-cognos-configuration)
  - [Configuración de informes](#configuración-de-informes)
  - [SQL de informe subyacente](#sql-de-informe-subyacente)
  - [Uso de una plantilla de informe](#uso-de-una-plantilla-de-informe)
  - [Organización del asunto de consulta](#organización-del-asunto-de-consulta)
  - [Construcciones de asunto de consulta](#construcciones-de-asunto-de-consulta)
  - [Dar formato a tablas o listas vacías](#dar-formato-a-tablas-o-listas-vacías)
- [Campos calculados](#campos-calculados)
  - [Creación de un campo calculado](#creación-de-un-campo-calculado)
  - [Suministro de campos necesarios](#suministro-de-campos-necesarios)
  - [Creación de un archivo de datos](#creación-de-un-archivo-de-datos)
  - [Uso de campos calculados en varios espacios de nombres](#uso-de-campos-calculados-en-varios-espacios-de-nombres)
- [Fragmentos de elaboración de informes](#fragmentos-de-elaboración-de-informes)
  - [Creación de fragmentos de elaboración de informes](#creación-de-fragmentos-de-elaboración-de-informes)
  - [Uso de CrossTracks en fragmentos de elaboración de informes](#uso-de-crosstracks-en-fragmentos-de-elaboración-de-informes)
    - [Creación de un enlace Abrir en la misma ventana](#creación-de-un-enlace-abrir-en-la-misma-ventana)
    - [Creación de un enlace a abierto en una ventana nueva](#creación-de-un-enlace-a-abierto-en-una-ventana-nueva)
  - [Suministro de campos de configuración](#suministro-de-campos-de-configuración)
    - [Obtención de la vía de acceso de informe](#obtención-de-la-vía-de-acceso-de-informe)
    - [Obtención del nombre de fragmento](#obtención-del-nombre-de-fragmento)
    - [Obtención de solicitudes de objeto](#obtención-de-solicitudes-de-objeto)
    - [Obtención de altura y anchura](#obtención-de-altura-y-anchura)
  - [Uso de imágenes en Fragmentos de elaboración de informes](#uso-de-imágenes-en-fragmentos-de-elaboración-de-informes)
- [Asuntos de consulta personalizados](#asuntos-de-consulta-personalizados)
  - [Revisión del diseño de informe](#revisión-del-diseño-de-informe)
  - [Creación de un diagrama entidad-relación](#creación-de-un-diagrama-entidad-relación)
  - [Creación de una sentencia SQL](#creación-de-una-sentencia-sql)
  - [Adición de funciones de base de datos](#adición-de-funciones-de-base-de-datos)
  - [Sustitución de variables](#sustitución-de-variables)
  - [Prueba de la sentencia SQL](#prueba-de-la-sentencia-sql)
  - [Creación de un informe](#creación-de-un-informe)
  - [Adición de un objeto SQL](#adición-de-un-objeto-sql)
  - [Adición de SQL al objeto SQL](#adición-de-sql-al-objeto-sql)
  - [Volver a poner las variables en SQL](#volver-a-poner-las-variables-en-sql)
    - [Adición de solicitudes](#adición-de-solicitudes-1)
  - [Completar el desarrollo del informe](#completar-el-desarrollo-del-informe)
  - [Creación de una entrada en el archivo CQS](#creación-de-una-entrada-en-el-archivo-cqs)
    - [Adición de un asunto de consulta de modelo](#adición-de-un-asunto-de-consulta-de-modelo)
    - [Especificación de relaciones](#especificación-de-relaciones)
    - [Creación de cálculos](#creación-de-cálculos)
    - [Uso de mapas de parámetros para crear expresión durante el tiempo de ejecución](#uso-de-mapas-de-parámetros-para-crear-expresión-durante-el-tiempo-de-ejecución)
  - [Regeneración del entorno](#regeneración-del-entorno)
  - [Sustitución de referencias a objetos SQL por referencias a CQS](#sustitución-de-referencias-a-objetos-sql-por-referencias-a-cqs)
    - [Edición del archivo de texto del informe](#edición-del-archivo-de-texto-del-informe)
    - [Eliminación de objeto SQL](#eliminación-de-objeto-sql)
- [Directrices de codificación SQL](#directrices-de-codificación-sql)
  - [Convenciones de denominación](#convenciones-de-denominación)
  - [Cláusula SELECT](#cláusula-select)
  - [Cláusula FROM](#cláusula-from)
  - [Cláusula WHERE](#cláusula-where)
  - [Cláusula ORDER BY](#cláusula-order-by)
- [Definiciones de modelo y espacio de nombres](#definiciones-de-modelo-y-espacio-de-nombres)
  - [Modelos de entorno](#modelos-de-entorno-1)
- [Limitaciones y métodos alternativos](#limitaciones-y-métodos-alternativos)
  - [Limitación de la longitud de ecuación](#limitación-de-la-longitud-de-ecuación)
  - [Problemas de visualización de localización](#problemas-de-visualización-de-localización)
  - [Localización de prestaciones interactivas](#localización-de-prestaciones-interactivas)
  - [Error al agrupar campos de serie grandes](#error-al-agrupar-campos-de-serie-grandes)
  - [Error de cardinalidad no válida RQP-DEF-0162 al ejecutar un informe](#error-de-cardinalidad-no-válida-rqp-def-0162-al-ejecutar-un-informe)
- [Avisos](#avisos)


# Guía del creador de informes

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=report-authors-guide)

La publicación *IBM OpenPages Report Author's Guide* está pensada para los autores de informes que deseen utilizar las herramientas de creación de informes en OpenPages® para desarrollar informes. Necesitan tener conocimientos de Cognos® Analytics. Deben asistir a la formación para creadores de informes de IBM OpenPages y deben tener experiencia con IBM® Cognos Analytics - Reporting.

CommandCenter debe estar instalado y configurado con OpenPages.

## Ámbito

La publicación *IBM OpenPages Report Author's Guide* no está pensada para sustituir la documentación de IBM® Cognos® Analytics , sino un suplemento específico de su implementación en OpenPages.

## IBM OpenPages documentación

IBM mantiene un conjunto de servicios de documentación IBM OpenPages, IBM OpenPages for IBM Cloud Pak for Datay IBM OpenPages on Cloud despliegues. La documentación de IBM OpenPages describe determinadas características y funciones que pueden no estar disponibles en la nube.

Si tiene alguna pregunta sobre la funcionalidad disponible en la versión del producto que está utilizando, póngase en contacto con el soporte deIBM utilizando el [portal de soporte de IBM](https://www.ibm.com/mysupport).

## Funciones de accesibilidad

Las características de accesibilidad ayudan a los usuarios que tienen alguna discapacidad física, por ejemplo movilidad restringida o visión limitada, a utilizar productos de tecnología de la información. La documentación de OpenPages tiene características de accesibilidad. Los documentos PDF son complementarios y no incluyen características de accesibilidad.

## Información sobre herramientas de bases de datos

IBM OpenPages da soporte a la base de datos IBM Db2® y a la base de datos Oracle. (Oracle no está soportado en IBM OpenPages for IBM Cloud Pak for Data).

- Para ejecutar scripts SQL de OpenPages , debe utilizar CLPPlus con Db2y SQL* Plus con Oracle database.
- Para ejecutar consultas, se puede utilizar cualquier herramienta SQL que sea compatible con la base de datos. Por ejemplo, puede utilizar CLPPlus u Optim Development Studio para ejecutar consultas en la base de datos Db2.

## Iconos de entorno de elaboración de informes

En IBM OpenPages, los iconos del entorno de elaboración de informes le proporcionan un marco de referencia en la interfaz de usuario.

La tabla siguiente lista los iconos que se utilizan en el modelo de entorno de elaboración de informes.

**Tabla 1. Iconos de entorno de elaboración de informes**

| Convención | Definición |
| --- | --- |
| ![Icono Espacio de nombres](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-namespace.jpg) | Representa un espacio de nombres raíz o cualquier otro espacio de nombres de un proyecto. |
| ![Icono de asunto de consulta](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-query_subject.jpg) | Representa un asunto de consulta. |
| ![Icono de elemento de consulta](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-query_item.jpg) | Representa un elemento de consulta. |
| ![Icono de medida](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-measure.jpg) | Representa una medida. |
| ![Icono de carpeta](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-folder-closed.jpg) | Representa una carpeta. |
| ![Icono de cálculo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-calculation.jpg) | Representa un cálculo. |
| ![Icono de filtro](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-filter.jpg) | Representa un filtro. |

## IBM Cognos Analytics e información de soporte

IBM Cognos Analytics integra informes, modelado, análisis, paneles de control, historias y gestión de sucesos para que pueda comprender los datos de su organización y tomar decisiones empresariales eficaces.

Puede acceder a IBM Cognos Analytics desde dentro de IBM OpenPages. Pulse **Análisis**.

IBM Cognos Analytics es el punto de partida para ejecutar informes, buscar contenido, ver **Mi contenido**, **Contenido de equipo**y **Recientes** listas, abrir paneles de control, abrir historias y otros elementos, cargar archivos, establecer sus preferencias y página de inicio.

En función del trabajo que realice, utilice distintas áreas de la interfaz de Cognos . Los autores y desarrolladores de informes profesionales, por ejemplo, utilizan IBM Cognos Analytics -Creación de informes para crear y editar una amplia gama de informes sofisticados y gestionados. También pueden crear paneles de control e historiales para ver, supervisar y comunicar comprensión y análisis de datos. Por ejemplo, los administradores pueden acceder a la **Consola de administración** para gestionar usuarios, supervisar el sistema y configurar orígenes de datos. En función del sistema, es posible que también tenga acceso a las aplicaciones complementarias para IBM Cognos Analytics.

Para obtener más información sobre IBM Cognos Analytics, consulte la [documentación deCognos](http://www.ibm.com/support/knowledgecenter/SSEP7J/welcome).

## Modelos de bases de datos

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-database-models)

Los temas de modelo de base de datos proporcionan al autor de informes la información básica necesaria para comprender el proceso de creación de informes utilizando IBM® Cognos® Analytics -Reporting. Esto incluye información sobre la estructura del modelo de datos de aplicación del software de IBM OpenPages® y las tablas de base de datos de informes correspondientes.

### Modelo de datos de aplicación

`Guía del creador de informes › Modelos de bases de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=models-application-data-model)

El modelo de datos de aplicación de IBM OpenPages® se ha diseñado utilizando técnicas orientadas a objetos con fines de mantenimiento, coste y extensibilidad.

El modelo de objeto OpenPages es altamente configurable porque consta de tipos de objeto, propiedades de esos objetos y las relaciones permitidas entre estos tipos de objeto.

El núcleo del diseño de base de datos consta de las tablas siguientes:

- **Recurso**

  Contiene una instancia de cada objeto creado en el sistema.

- **RESRELATIONSHIPS**

  Contiene todas las relaciones entre los objetos del sistema.

- **ASSETTYPES**

  Contiene definiciones del tipo de contenido (tipos de objeto) permitido en el sistema.

- **ASSETTYPESBUNDLEDEFS**

  Contiene la relación entre tipos de activo y BundleDefs.

- **BUNDLEDEFS**

  Contiene grupos de campos asociados a un objeto.

- **PROPERTYDEFS**

  Contiene los campos asociados a una instancia de un objeto.

- **PROPERTYVALS**

  Contiene los valores de campo asociados con una instancia de un objeto.

*Figura 1. Diagrama ER de base de datos principal*

![Diagrama ER de base de datos principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Core_db.jpg)

A través de estas tablas definidas genéricas, se puede crear cualquier tipo de objeto en la base de datos de OpenPages . Esto proporciona a nuestros clientes la capacidad de ampliar los objetos del sistema existentes o añadir nuevos objetos con sus propias definiciones.

Hay muchas otras tablas utilizadas para dar soporte a estas tablas, pero estas incluyen las tablas fundamentales necesarias para crear objetos en OpenPages.

Las ventajas de este diseño de base de datos se pueden ver en que un pequeño conjunto de clases Java™ puede crear y acceder a cualquier objeto de la base de datos. La desventaja de este diseño es que no se puede utilizar ninguna herramienta de creación de informes comercial para generar informes a partir de este diseño debido a los siguientes motivos:

- La relación entre las tablas RESOURCE y RESRELATIONSHIP es recursiva.
- Para crear un informe en un objeto, se deben unir muchas tablas. Finalmente, esto supera los límites de una herramienta de elaboración de informes.
- Para informar de estas tablas a menudo se necesita el conocimiento de los diseñadores de base de datos sobre cómo se construyeron.

> **Nota:** No debe escribir informes en la base de datos principal porque afectará al rendimiento del sistema.

### Diseño de tabla de informes

`Guía del creador de informes › Modelos de bases de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=models-reporting-table-design)

Para facilitar la elaboración de informes desde la base de datos de aplicación, se crea un conjunto de vistas secundario que combina las distintas tablas individuales desde el diseño de datos de la aplicación a un formato más adecuado para generar informes.

La Cuadro 1 lista el convenio de denominación para estas tablas y vistas.

Donde `<OBJECT_TYPE>` es el nombre del tipo de objeto y `<ENUMERATION>` es el nombre de un campo de serie enumerada de varios valores.

**Tabla 1. Convención de denominación de tabla de informes**

| Convenio de denominación | Descripción |
| --- | --- |
| `RV_<OBJECT_TYPE>`<br>(`RV_` con un único guión bajo) | Vista de objeto<br>Por ejemplo: `RV_ENTITY` |
| `RT_<OBJECT_TYPE>_<ENUMERATION>`<br>(`RT_` con un único guión bajo) | Tabla de enumeración multivalor<br>Por ejemplo: `RT_RISKASSESSMENT_DOMAIN` |
| `RT__<OBJECT_TYPE>_<OBJECT TYPE>`<br>(`RT__` con un doble guión bajo) | Tabla de relaciones entre 2 tipos de objeto<br>Por ejemplo: `RT__ENTITY_PROCESS` |

> **Importante:**

> - Oracle tiene un límite de 30 caracteres para el nombre de tabla. Algunos nombres de tabla se truncarán.
> - Las vistas RV son diferentes de las tablas RT en que las vistas tienen la seguridad de datos compilada en ellas y las tablas RT no.

La mayoría de los objetos definidos en IBM OpenPages® tendrán una vista RV_\<OBJECT_TYPE> y una tabla RT_\<OBJECT_TYPE> en la base de datos. Sin embargo, las tablas de unión no tienen vistas porque no necesitan seguridad. Cuando se utiliza SQL directo, es preferible utilizar las vistas RV debido a que el código de seguridad de datos ya está presente.

Las tablas de relaciones representan las relaciones padre-hijo definidas durante la instalación del sistema.

Las tablas de enumeración almacenan la relación de objetos en series enumeradas en un formato relacional adecuado.

Estas tablas se generan automáticamente según los valores de OpenPages. Para obtener más información, consulte la publicación *IBM OpenPages Guía del administrador*.

#### Tablas de objetos

`Guía del creador de informes › Modelos de bases de datos › Diseño de tabla de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=design-object-tables)

Los objetos de tablas pueden incluir muchos campos de sistema.

Este tema lista todos los campos del sistema que se incluirán en todas las tablas de objeto. Los demás campos son específicos del cliente y corresponden a una configuración particular del sistema, no se muestran aquí.

**Tabla 1. Campos del sistema de la tabla de objeto**

| Nombre de columna | Descripción | Tipo nativo |
| --- | --- | --- |
| CHECKED_IN_BY | ID del usuario que modificó este objeto la última vez. | NUMBER |
| CREATION_DATE | Fecha de creación del objeto. | FECHA |
| CREATOR | ID del creador del objeto. | NUMBER |
| DESCRIPCIÓN | Descripción del objeto. | VARCHAR2(2048) |
| DETAIL_PAGE_URL | URL de la página del sistema para este objeto. | VARCHAR2(2083) |
| FULL_PATH | Vía de acceso completa al objeto. | VARCHAR2(1024) |
| IS_LOCKED | Estado de bloqueo del objeto. S o N. | NUMBER |
| LATEST_VERSION | Versión más reciente del objeto. | NUMBER |
| MAJOR_NUMBER | Número de versión principal. | NUMBER |
| MINOR_NUMBER | Número de versión menor. | NUMBER |
| MODIFICATION_DATE | Última fecha de modificación del objeto. | FECHA |
| NAME00 | Nombre de objeto. | VARCHAR2(256) |
| PARENT_FOLDER | Carpeta padre del objeto. ID de recurso. | NUMBER |
| REPORTING_PERIOD_ID | ID de la etiqueta del periodo de elaboración de informes especificado por el usuario. | NUMBER |
| RESOURCE_ID | ID de recurso exclusivo del objeto. | NUMBER |
| TÍTULO | Título de objeto. | VARCHAR2(4000) |
| VERSION_COMMENTS | Comentarios de la versión. | VARCHAR2(2048) |

La Cuadro 2 lista los índices que se encuentran en todas las tablas de objetos:

**Tabla 2. Índices de tabla de objeto**

| Índice | Nombres de columna |
| --- | --- |
| 1 | PARENT_FOLDER, REPORTING_PERIOD_ID |
| 2 | FULL_PATH, REPORTING_PERIOD_ID |
| N | \<ENUMERATION> Campos (un índice para cada campo) |
| N | Campos de moneda (un índice para moneda base y un índice para moneda local) |
| Sistema | ENTITY_ID, REPORTING_PERIOD_ID |

#### Vistas de objeto

`Guía del creador de informes › Modelos de bases de datos › Diseño de tabla de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=design-object-views)

Hay una vista correspondiente para cada objeto definido en el sistema. Las vistas difieren de las tablas de objeto en que tienen la seguridad de datos compilada en la definición.

Cuadro 1 lista campos adicionales incluidos con cada vista:

**Tabla 1. Campos adicionales incluidos con la vista**

| Nombre de columna | Descripción | Tipo nativo |
| --- | --- | --- |
| OP_OBJECT_TYPE_ID | Tipo de objeto de la vista. | NUMBER |
| OP_RECURSIVE_NATIVE_LEVEL | En un objeto jerárquico, nivel de la jerarquía. | NUMBER |
| OP_FLAG_READ_ACCESS | Un distintivo Y o N indica si el usuario tiene el privilegio para ver los datos. | VARCHAR2(4) |

#### Tablas de enumeración

`Guía del creador de informes › Modelos de bases de datos › Diseño de tabla de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=design-enumeration-tables)

Esta clase de tablas contiene listas de variables enumeradas, que se aplican a un tipo de objeto particular, donde los valores enumerados de selección múltiple se almacenan como registros independientes.

Todas las tablas de enumeración contienen los mismos campos, listados en Cuadro 1.

**Tabla 1. Campos de tabla enumerada**

| Nombre de columna | Descripción | Tipo nativo |
| --- | --- | --- |
| \<PARENT>_ID | ID exclusivo del objeto padre. | NUMBER |
| REPORTING_PERIOD_ID | ID de la etiqueta del periodo de elaboración de informes especificado por el usuario. | NUMBER |
| < ENUMERATION> | ID de la serie enumerada. | NUMBER |

Cuadro 2 lista los índices que se encuentran en todas las tablas de enumeración:

**Tabla 2. Índices de la tabla de enumeración**

| Índice | Nombres de columna |
| --- | --- |
| 1 | RESOURCE_ID, REPORTING_PERIOD_ID |
| 2 | < ENUMERATION> |
| Sistema | RESOURCE_ID, REPORTING_PERIOD_ID, \<ENUMERATION> |

#### Tabla de relaciones

`Guía del creador de informes › Modelos de bases de datos › Diseño de tabla de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=design-relationship-table)

Las tablas de relaciones representan las relaciones de muchos a muchos entre objetos IBM OpenPages® .

Todas las tablas de relaciones constan de los mismos campos, listados en Cuadro 1.

**Tabla 1. Campos de la tabla de relaciones**

| Nombre de columna | Descripción | Tipo nativo |
| --- | --- | --- |
| PARENT_ID | ID exclusivo del objeto padre. | NUMBER |
| REPORTING_PERIOD_ID | ID de la etiqueta del periodo de elaboración de informes especificado por el usuario. | NUMBER |
| CHILD_ID | ID exclusivo del objeto hijo. | NUMBER |
| HIER_INSTANCE_ID | Este valor se establece siempre en 1. | NUMBER |
| IS_PRIMARY | Indica si el objeto padre es el padre primario del objeto hijo. Los valores son Y o N. | VARCHAR2(1) |
| DISTANCE | Distancia entre el objeto padre y el objeto hijo. Si la distancia entre los objetos padre e hijo es 1, los objetos están enlazados directamente. | NUMBER |

La Cuadro 2 lista los índices que se encuentran en todas las tablas de relaciones:

**Tabla 2. Índices de la tabla de relaciones**

| Índice | Nombres de columna |
| --- | --- |
| 1 | PARENT_ID, REPORTING_PERIOD_ID |
| 2 | CHILD_ID, REPORTING_PERIOD_ID |
| Sistema | PARENT_ID, CHILD_ID, REPORTING_PERIOD_ID, HIER_INSTANCE_ID |

## Modelos de datos del entorno

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-framework-data-models)

El modelo de datos de entorno tiene una rama de espacio de nombres relacional.

### Modelo de datos relacional

`Guía del creador de informes › Modelos de datos del entorno` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=models-relational-data-model)

El modelo de datos relacional que proporciona IBM OpenPages® está diseñado para permitir al usuario informar sobre objetos basándose en sus relaciones definidas en el sistema.

Los datos están almacenados en un conjunto de tablas normalizado que proporciona un almacenamiento eficaz. El objetivo es evitar la redundancia de datos y proporcionar un alto nivel de rendimiento. La organización de este tipo de datos normalmente permite a un analista empresarial experto o un modelador de datos comprenderlo y no está diseñado para que lo vea un usuario final.

Este tipo de modelo se utiliza generalmente en informes de lista donde se necesitan datos mezclados (numéricos, de fecha, de serie) para transmitir información a los usuarios. Se puede realizar agregación en este tipo de informe pero no es un elemento clave del informe.

La siguiente lista describe las características clave del modelo de datos relacional:

- Modelado como un diagrama Entidad-Relación.
- Datos altamente normalizados.
- Normalmente dividido por objetos relacionados con otros objetos.
- Todos los atributos para un objeto incluido el textual, así como el numérico, pertenecen al objeto.

*Figura 1. Diagrama Entidad-Relación*

![Diagrama Entidad-Relación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/relational_Model.jpg)

El diagrama anterior muestra el diagrama típico de relación de entidad de cuatro de los objetos principales en OpenPages.

#### Terminología de modelado relacional

`Guía del creador de informes › Modelos de datos del entorno › Modelo de datos relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-relational-modeling-terminology)

Es útil para conocer la terminología del modelado relacional.

**Tabla 1. Terminología de modelado relacional**

| Icono | Nombre | Descripción |
| --- | --- | --- |
| ![Icono de asunto de consulta](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-query_subject.jpg) | Asunto de consulta | Consulta SQL que se ha diseñado para exponer un determinado conjunto de datos al usuario con fines de elaboración de informes. |
| ![Icono de elemento de consulta](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-query_item.jpg) | Elemento de consulta | Campo de base de datos. |

#### Vista de carpetas de un modelo de datos relacional

`Guía del creador de informes › Modelos de datos del entorno › Modelo de datos relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-folder-view-relational-data)

Un modelo de datos relacional contiene una determinada estructura de carpetas.

Figura 1 muestra el asunto de consulta SOXRisk y algunos de sus elementos de consulta.

*Figura 1. Vista de carpetas relacional*

![Jerarquía del modelo relacional](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_8_relational_folder_view.jpg)

Habrá un asunto de consulta para cada tipo de objeto definido en el sistema. Cada uno de estos objetos estará relacionado por uniones externas a la izquierda una a otra en base a las relaciones padre-hijo definidas en el sistema. Consulte la publicación *IBM OpenPages Guía del administrador* para obtener más información sobre la configuración del sistema.

## Modelo de objeto

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-object-model)

El modelo de objeto al que se hace referencia en este documento es el modelo estándar (el que viene de fábrica) que está instalado para todas las instalaciones en una primera instalación.

Solo se incluyen objetos dentro del modelo de objeto predeterminado que son comunes a todas las soluciones incluidos y tratados en este documento para mayor simplicidad.

> **Importante:** Todos los ejemplos de este documento se muestran en [Idioma de diseño de informe](#idioma-de-diseño-de-informe) (RDL).

### Terminología del modelo de objeto

`Guía del creador de informes › Modelo de objeto` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-object-terminology)

Es útil conocer los términos básicos necesarios para comprender el modelo de objeto de IBM OpenPages® .

**Tabla 1. Terminología del modelo de objeto**

| Plazo | Descripción |
| --- | --- |
| Múltiples padres | Objeto hijo asociado a más de un padre. |
| Relación padre-hijo | Cuando un objeto se asocia a otro objeto, un objeto se considera objeto padre y el otro objeto hijo. La relación que se forma es una relación padre-hijo. |
| Asociación primaria | Un padre puede tener varios objetos hijo y todos ellos pueden ser primarios. Un hijo puede tener varios objetos padre y solo uno de ellos puede ser primario. Las asociaciones primarias se utilizan para determinar la vía de acceso que debe seguir el sistema al ejecutar varias operaciones que requieren una jerarquía de objetos cruzada. |
| Objeto principal | Un objeto principal de OpenPages. |
| Relación recursiva | Relación en la que un objeto hijo es del mismo tipo de objeto que el padre. |
| Objeto secundario | Objeto que se puede asociar a varios tipos de objeto en la rama común |

### Características del modelo de objeto

`Guía del creador de informes › Modelo de objeto` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-object-characteristics)

El modelo de objetos estándar (predefinido) consta de determinadas características.

La siguiente lista describe las características clave de los modelos de objeto:

- Los tipos de objeto de entidad de negocios y de subproceso son recursivos.
- Los tipos de objeto Problema, Firma, Archivo y Enlace se pueden asociar a cualquier tipo de objeto primario.
- Los tipos de objeto pueden contener tipos de datos de serie enumerada de valor único o multivalor.

> **Nota:** Dependiendo de la configuración, el modelo de objeto que vea puede ser diferente.

La Cuadro 1 lista los tipos de objetos primarios que se comparten entre todas las soluciones. La lista va seguida de Figura 1 que muestra el modelo de objeto y la relación entre los objetos primarios. Todos los objetos tienen una relación padre-hijo directa.

**Tabla 1. Tipos de objeto primario**

| Tipo de objeto | Etiqueta |
| --- | --- |
| SOXBusEntity (recursivo) | Entidad empresarial |
| SOXProcess | Proceso |
| SOXSubprocess (recursivo) | Subproceso |
| SOXRisk | Riesgo |
| SOXControl | Control |
| SOXTest | Plan de pruebas |
| SOXTestResult | Resultado de prueba |
| RiskAssessment | Evaluación de riesgo |

*Figura 1. Relaciones de objetos primarios*

![Relaciones de objetos primarios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/6.0_Object_Model.jpg)

La Cuadro 2 lista los tipos de objeto secundarios que se comparten entre todas las soluciones. La lista va seguida de Figura 2 que muestra los objetos secundarios sin enlaces a los objetos primarios porque las uniones se forman en la herramienta de informes.

**Tabla 2. Tipo de objeto secundario**

| Tipo de objeto | Etiqueta |
| --- | --- |
| SOXIssue | Problema |
| SOXTask | Elemento de acción |
| SOXSignature | Firma |
| SOXExternalDocument | Vínculo |
| SOXDocument | Archivo |

*Figura 2. Objetos secundarios*

![Objetos secundarios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/6.0_Object_Model-2.jpg)

Este modelo representa la relación básica de objetos dentro de IBM OpenPages®. Para conocer las relaciones exactas de su propio sistema, obtenga el diagrama del modelo de objetos que se creó durante el proceso de instalación del sistema o examine las relaciones entre objetos mediante **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Soluciones**.

## Entorno de elaboración de informes

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-reporting-framework)

El entorno de elaboración de informes consta de modelos de entorno de Cognos® configurados y generados en OpenPages®. Dan soporte a los datos relacionales utilizados para crear informes en IBM® Cognos Analytics.

Al generar el entorno de elaboración de informes, los paquetes para los modelos de entorno seleccionados se publican en el servidor de Cognos . Utilizando los asuntos de consulta y los elementos de consulta en estos espacios de nombres, los autores de informes pueden crear informes desde dentro de IBM OpenPages.

Para obtener información sobre la configuración del entorno de elaboración de informes, consulte la publicación *IBM OpenPages Guía del administrador*.

### Modelos de entorno

`Guía del creador de informes › Entorno de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=rf-framework-models)

Los modelos de entorno se basan en el modelo de objeto OpenPages® y definen subconjuntos de objetos y relaciones necesarios para los requisitos de creación de informes.

Los modelos de entornos incluyen los siguientes componentes:

- Metadatos
- Etiquetas
- Asuntos de consulta personalizados

La infraestructura de informes contiene un conjunto de modelos de infraestructura predefinidos, que se utilizan para los informes predefinidos que se suministran con OpenPages. Además de los modelos de infraestructura predefinidos, puede crear sus propios modelos de infraestructura. La capacidad de utilizar varios modelos de entorno permite dirigir un modelo de entorno a específicas, funciones de usuario, o perfiles de objeto específicos.

Hay dos tipos de modelos de entorno que puede crear:

- Estándar
- Básica

Los dos tipos dan soporte al filtrado de perfiles y le permiten definir el nombre de paquete.

#### Modelos de entorno estándares

Los modelos de entorno estándar están pensados para escritores de informes avanzados con amplios conocimientos de IBM® Cognos® Analytics. Utilice este tipo de modelo para informes que requieren la funcionalidad más compleja que ofrece Cognos .

Los modelos de entorno estándares tienen las siguientes características:

- Anidar un subespacio de nombres de relación.
- Utilice la jerarquía de espacios de nombres siguiente:

  - **[etiqueta de paquete]** > **[espacio de nombres]** > **[espacio de nombres] _REL**
- Utilizan la creación de carpetas amplia para asuntos de consulta y elementos de datos.
- Contienen asuntos de consulta y objetos auxiliares tales como Enumeraciones y Relaciones.
- Utilizan representaciones de campos complejos, por ejemplo, monedas que tienen varios elementos de datos para el importe local y base.
- Representan objetos recursivos como varios asuntos de consulta utilizando niveles de objetos recursivos.
- Proporcione objetos de conformidad secundarios, como Archivos o Problemas, como objetos autónomos. Las relaciones con ellos deben generarse en informes.

#### Modelos de entorno básicos

Los modelos básicos están pensados para usuarios finales que no tienen amplios conocimientos de IBM Cognos Analytics. Utilice este tipo de modelo para informes más simples que desea que los usuarios finales puedan crear cuando sea necesario.

Los modelos de entorno básicos tienen las siguientes características:

- Utilice la siguiente jerarquía de espacios de nombres: **[etiqueta de paquete]** > **[espacio de nombres]**

  Los asuntos de consulta se crean en el espacio de nombres raíz. No se ha creado el subespacio de nombres `[namespace]_REL`.
- No crean objetos de consulta auxiliares para enumeraciones, relaciones, etc.
- Generar objetos recursivos, por ejemplo, Entidad de negocios, Submandato y Subproceso, como objetos de consulta únicos.
- Genere niveles de objetos recursivos solo para objetos Entidad de negocios.
- Eliminan elementos de datos a nivel de sistema, por ejemplo, IS_PRIMARY, LATEST_VERSION, etc.
- Utilizan representaciones de campos simplificados, por ejemplo, elementos de datos únicos para monedas y enumeraciones como Importe local y Valor localizado, respectivamente.

### Paquetes de entorno

`Guía del creador de informes › Entorno de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=framework-packages)

Cuando se genera el entorno de elaboración de informes, los paquetes para modelos de entorno seleccionados se publican en el servidor Cognos.

Los modelos generados para los modelos de entorno predefinidos se publican en **Team Content** > **OpenPages Packages**. Para obtener más información, consulte [Modelos de entorno](#modelos-de-entorno-1).

Los modelos generado para los modelos de entorno que se crean se publican bajo el nombre de paquete del modelo de entorno.

### Espacios de nombres

`Guía del creador de informes › Entorno de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=rf-namespaces)

Un espacio de nombres identifica exclusivamente una recopilación de asuntos de consulta, sus relaciones y otros objetos (como cálculos) que puede utilizar para la elaboración de informes.

El generador de infraestructura utiliza la definición de un espacio de nombres (que se define en la interfaz de usuario de IBM OpenPages® ) para crear un espacio de nombres correspondiente en el modelo de entorno.

Los espacios de nombres de los modelos de infraestructura predefinidos los utilizan los informes predefinidos que se suministran con OpenPages. Si realiza cambios en los espacios de nombres, puede afectar a la funcionalidad de los informes y puede hacer que no se ejecuten. Puede añadir sus propios espacios de nombres a los modelos de infraestructura predefinidos para identificar de forma exclusiva una colección de asuntos de consulta y otros objetos (como cálculos) para satisfacer los requisitos de creación de informes

Si define sus propios modelos de entorno estándares y básicos, debe definir espacios de nombres para ellos .

- **Modelos de entorno estándares**

  Al generar el entorno de elaboración de informes, los paquetes para los modelos de entorno estándar se publican en el servidor de Cognos® con un subespacio de nombres de relación:

  - `[namespace]_REL`: este espacio de nombres relacional permite a los autores de informes informar sobre los objetos basándose en sus relaciones definidas. Este tipo de modelo a menudo se utiliza en informes de lista que utilizan datos mezclados (numéricos, datos y serie).

- **Modelos básicos**

  Al generar el entorno de elaboración de informes, los paquetes para los modelos de entorno básicos se publican en el servidor de Cognos . Los asuntos de consulta se crean en el espacio de nombres raíz. Los subespacios de nombres no se crean.

Para obtener información sobre cómo crear o modificar espacios de nombres, consulte la publicación *IBM OpenPages Guía del administrador*.

#### Espacio de nombres predeterminado

`Guía del creador de informes › Entorno de elaboración de informes › Espacios de nombres` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=namespaces-default-namespace)

Cada modelo de entorno predefinido tiene un espacio de nombres `DEFAULT` que contiene asuntos de consulta, cálculos y elementos de consulta predefinidos. No cambie los espacios de nombres predeterminados. Cada espacio de nombres predeterminado contiene una mayoría de objetos y asociaciones presentes para la jerarquía de objetos predefinida de cada solución. Los espacios de nombres predeterminados se han diseñado para cumplir los requisitos de creación de informes más comunes.

El modelo de entorno de creación de informes de plataforma contiene un espacio de nombres predeterminado que incluye un subespacio de nombres (DEFAULT_REL).

Además de los espacios de nombres DEFAULT, están disponibles otros espacios de nombres predefinidos, en función de las soluciones instaladas en el sistema. Para obtener detalles, consulte [Definiciones de modelos y espacios de nombres](#definiciones-de-modelo-y-espacio-de-nombres).

#### Convenciones de denominación para espacios de nombres

`Guía del creador de informes › Entorno de elaboración de informes › Espacios de nombres` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=namespaces-naming-conventions)

Cuando necesite crear un nombre para un espacio de nombres, debe seguir ciertas convenciones de denominación.

- Todos los asuntos de consulta que representan un objeto definido en IBM OpenPages® tienen el mismo nombre que el objeto.
- Todos los elementos de consulta para un objeto tienen un prefijo de identificador exclusivo para ese objeto. La lista de identificadores se puede encontrar en [Convenios de denominación](#convenciones-de-denominación).
- Todos los cálculos asociados con un objeto tiene un nombre que comienza por el nombre de objeto.

### Adición de códigos de configuración regional y definición de una configuración regional de orden de clasificación

`Guía del creador de informes › Entorno de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=framework-adding-locale-codes-defining-sort-order-locale)

Puede añadir códigos de entorno local al entorno de elaboración de informes. También puede controlar el idioma en el que se clasifican los asuntos de consulta y los elementos de datos.

Para obtener información, consulte la publicación *IBM OpenPages Guía del administrador*.

### Las carpetas de nivel superior del modelo relacional

`Guía del creador de informes › Entorno de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=framework-relational-model-top-level-folders)

Las carpetas utilizadas mucho para organizar asuntos de consulta para que los autores de informe puedan encontrar elementos fácilmente de forma intuitiva.

Esta información solo se aplica a modelos de entorno estándares, no a modelos de entorno básicos.

Figura 1 muestra el diseño de carpeta de nivel superior para el subespacio de nombres de datos relacionales DEFAULT_REL.

*Figura 1. Diseño de la carpeta del modelo relacional*

![Jerarquía del subespacio de nombres de datos relacionales DEFAULT_REL](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_default-rel.png)

Las carpetas de nivel superior pueden contener otras carpetas, asuntos de consulta y elementos de consulta, tal como se indica en Cuadro 1.

**Tabla 1. Carpeta de nivel superior**

| Esta carpeta de nivel superior... | Contiene asuntos de consulta para... |
| --- | --- |
| `AUDIT_TRAIL` | Tablas de auditoría del sistema |
| `COMPUTED_FIELDS` | Campos calculados que se han creado en la aplicación |
| `ENUMERATIONS` | Asuntos de consulta de enumeración de solicitudes |
| `GRC_OBJECTS` | Objetos de conformidad primarios |
| `GRC_OBJECTS_STANDALONE` | Objetos de conformidad secundarios |
| `MISCELLANEOUS` | Información no relacionada con ninguna otra carpeta |
| `SECURITY` | Seguridad del sistema |

#### La carpeta Seguimiento de auditoría (Modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=folders-audit-trail-folder-relational-model)

Figura 1 muestra la carpeta Seguimiento de auditoría con todos sus asuntos de consulta.

*Figura 1. Carpeta Seguimiento de auditoría (entorno local de Report Design Language)*

![Jerarquía de la carpeta Seguimiento de auditoría](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_audit_trail.png)

Cuadro 1 lista los asuntos de consulta en esta carpeta.

**Tabla 1. Asuntos de consulta de la carpeta Auditoría**

| Asunto de consulta | Descripción |
| --- | --- |
| `ACTOR_AUDIT_TRAIL` | Contiene registros relacionados con intentos de inicio de sesión del usuario. |
| `AUDIT_CHANGE` | Devuelve una lista de propiedades que han cambiado para cualquier objeto asociado con una entidad del sistema.<br>Se definen las siguientes solicitudes para este asunto de consulta:<br>• Fecha de inicio<br>• Fecha de finalización<br>• ID de entidad<br>• Establecer ID (establecer siempre = 1) |
| `AUDITA_METADATA` | Contiene información de seguimiento de auditoría relacionada con la configuración de registro. |
| `AUDITA_SECURITY` | Contiene información de seguimiento de auditoría relacionada con la seguridad del usuario. |
| `AUDITA_SECURITY_OBJ_ACTOR` | Devuelve información de auditoría para actores y ACL de actor. |
| `AUDITA_SECURITY_OBJ_ROLETPL` | Devuelve información de auditoría para plantillas de funciones, asignaciones de plantillas de funciones, permisos de aplicación de plantillas de funciones y listas de control de acceso (ACI) de objetos de plantillas de funciones. |
| `AUDIT_TRAIL_TYPES` | Contiene los nombres y descripciones de todos los tipos de elementos del seguimiento de auditoría que se pueden registrar. |
| `CLASSIFIER_AUDIT_TRAIL` | Contiene información de auditoría para sugerencias realizadas por Natural Language Classifier. |
| `LOCKS` | Contiene datos de bloqueo de recursos. |
| `LOCKS_AUDIT_TRAIL` | Contiene el seguimiento de auditoría de todos los bloqueos que se aplicaron al sistema. |
| `MODIFIED RESOURCES BY ENTITY` | Devuelve una lista de recursos asociados a una entidad particular, que se ha modificado.<br>Se definen las siguientes solicitudes para este asunto de consulta:<br>• Fecha de inicio<br>• Fecha de finalización<br>• ID de entidad padre<br>• Establecer ID (establecer siempre = 1) |
| `OBJECT AUDIT BY RESOURCE` | Devuelve una lista de todas las definiciones de propiedad del sistema y si se han marcado para su supresión. |
| `PROPERTY_AUDIT_TRAIL` | Contiene todos los registros para las propiedades que se han cambiado en el sistema. |
| `RR_AUDIT_TRAIL` | Contiene datos de seguimiento de auditoría para la tabla resrelationship. Cualquier modificación de relaciones se escribe en esta tabla. |
| `UNIFIED AUDIT TRAIL` | Devuelve una lista de todas las propiedades de objeto del sistema que se han cambiado. |
| `UNIFIED LOG PER RESOURCE` | Devuelve una lista de todas las propiedades de objeto que se han cambiado para el ID de recurso especificado.<br>Se definen las siguientes solicitudes para este asunto de consulta:<br>• Fecha de inicio<br>• Fecha de finalización<br>• ID de recurso<br>• Establecer ID (establecer siempre = 1) |
| `USER PERMISSIONS` | Devuelve una lista de todos los usuarios de sistema y sus derechos en vigor. |

#### La carpeta Campos calculados (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=folders-computed-fields-folder-relational-model)

La Figura 1 muestra un ejemplo de la carpeta de un campo calculado y sus subcarpetas. Esta carpeta solo se crea si tiene un campo calculado definido en el espacio de nombres.

*Figura 1. Carpeta Campos calculados*

![Jerarquía de la carpeta de campos calculados](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_framework_27.jpg)

La Tabla 1 describe las carpetas de la carpeta Campos calculados.

**Tabla 1. Carpeta Enumeración**

| Carpeta | Descripción |
| --- | --- |
| `<Object Name>` `(COMPUTED_FIELDS)` | Se crea una subcarpeta para cada objeto del espacio de nombres que tiene un campo calculado. |
| `<Computed Field Name>` | Cada campo calculado que se ha creado se lista aquí. |

#### La carpeta Enumeraciones (Modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=folders-enumerations-folder-relational-model)

La Figura 1 muestra un ejemplo de la carpeta Enumeraciones y sus subcarpetas. Esta carpeta contiene asuntos de consulta que solo se pueden utilizar para crear solicitudes en informes. Habrá una carpeta para cada tipo de objeto. Los objetos mostrados serán diferentes para cada instalación del usuario.

*Figura 1. Carpeta Enumeraciones*

![Jerarquía de la carpeta de enumeraciones](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_framework_22.jpg)

La Tabla 1 describe las carpetas de la carpeta Enumeraciones.

**Tabla 1. Carpeta Enumeración**

| Carpeta | Descripción |
| --- | --- |
| `<Object Name>` `(ENUMERATIONS)` | Contienen los asuntos de consulta correspondientes a cada una de las series enumeradas definidas para un objeto. Solo se deberían utilizar para crear solicitudes en informes. |

##### Series enumeradas (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Enumeraciones (Modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-enumerated-strings-relational)

Figura 1 muestra un ejemplo de una carpeta ENUMERATIONS abierta:

*Figura 1. Carpeta ENUMERACIONES*

![Jerarquía que incluye la carpeta de enumeraciones](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_framework_28.jpg)

Cada asunto de consulta representa una serie enumerada que se ha definido para ese objeto. Estas series enumeradas pueden ser únicas o multivalor.

Figura 2 muestra un ejemplo de un asunto de consulta abierto:

*Figura 2. Elementos de consulta de serie enumerada*

![Jerarquía que incluye los elementos de consulta de serie enumerada](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_framework_29.jpg)

La tabla siguiente lista los elementos de consulta encontrados en una serie enumerada:

**Tabla 1. serie enumerada multivalor**

| Asunto de consulta | Descripción |
| --- | --- |
| ENUMVALID | ID del valor de serie enumerada. |
| ENUMTYPEID | ID del tipo de variable devuelta. Todos los registros de una serie enumerada devuelven el mismo valor. |
| VALOR | Valor devuelto para cada registro. |
| NOMBRE | Nombre de este registro en la serie enumerada devuelta en RDL. |
| DISPLAY_ORDER | Valor numérico que indica el orden en el que el usuario visualiza el valor. |
| FLAG_IS_HIDDEN | Valor verdadero/falso que indica si el usuario visualiza el valor. |
| I18N_LOCALE_ID | Configuración regional del valor devuelto. |
| RI_DOMAN | Nombre localizado de este registro de la serie enumerada. |

Estos asuntos de consulta solo se pueden utilizar para crear solicitudes. Debe utilizar ENUMVALID como valor devuelto y RI_DOMAIN como valor de visualización, porque está localizado. Se pueden utilizar otros parámetros para el filtrado.

#### La carpeta Objetos GRC (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=folders-grc-objects-folder-relational-model)

La Figura 1 muestra un ejemplo de la carpeta Objetos GRC con todas sus subcarpetas. Los objetos mostrados serán diferentes para cada instalación del usuario.

*Figura 1. Carpeta de objetos GRC (entorno local de idioma de diseño de informe)*

![Jerarquía de la carpeta Objetos GRC](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_framework_4.jpg)

La Tabla 1 lista las carpetas de la carpeta GRC.

**Tabla 1. Carpetas Objetos GRC**

| Carpeta | Descripción |
| --- | --- |
| `<Recursive Object>` `_FOLDER` | Contiene todos los asuntos de consulta relacionados con los objetos recursivos utilizados en este espacio de nombres. |
| `<Object Name>` | Contiene los elementos de datos relacionados con los objetos especificados en este espacio de nombres. |

##### La carpeta SOXBusEntity (Modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Objetos GRC (modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-soxbusentity-folder-relational)

La Figura 1 muestra un ejemplo de una carpeta de objeto SOXBusEntity con todos sus elementos.

*Figura 1. Carpeta de objeto de entidad de negocios SOX*

![Jerarquía de una carpeta de objetos SOXBusEntity](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_framework_5.jpg)

La Tabla 1 lista los elementos de la carpeta SOXBusEntity .

**Tabla 1. Carpeta de objeto de entidad**

| Carpeta/Asunto de consulta | Descripción |
| --- | --- |
| `<Hierarchy>` | Se creará una carpeta para cada nivel de objeto recursivo creado en IBM OpenPages®. |
| `<Level>` `_FOLDER` | Se creará una carpeta para que contenga todos los asuntos de consulta relacionados con un único nivel de objeto recursivo. |
| `ID_FIELDS` | En cada nivel de objeto recursivo, esta carpeta contiene los elementos de consulta del campo de ID. |
| `CURRENCY_FIELDS` | En cada nivel de objeto recursivo, esta carpeta contiene los elementos de consulta del campo de moneda. |
| `ENUMERATION_FIELDS` | En cada nivel de objeto recursivo, esta carpeta contiene las series enumeradas específicas del objeto. |
| `HIERARCHY_CONTEXT` | En cada nivel de objeto recursivo, esta carpeta contiene los elementos de datos que permiten al autor de informe filtrar este nivel de objeto. |
| `<Query Items>` | En cada nivel de objeto recursivo, son todos los elementos de consulta restantes para el nivel. |
| `SOXBUSENTITY_GPC` | Es un asunto de consulta único que contiene todos los elementos de consulta de GPC. |

##### Los asuntos de consulta GPC (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Objetos GRC (modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-gpc-query-subjects-relational)

La Figura 1 muestra la estructura de carpetas Abuelo-Padre-Hijo bajo la carpeta Entidad.

*Figura 1. Elementos de carpeta GPC (entorno local de idioma de definición de informe)*

![Jerarquía de la carpeta GPC](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_be-gpc.png)

La Tabla 1 lista los elementos de la carpeta GPC.

**Tabla 1. Elementos de GPC**

| Carpeta/Asunto de consulta | Descripción |
| --- | --- |
| `SOXBUSENTITY_GPC` | Asunto de consulta que contiene todos los campos para cada uno de los niveles de entidad estándar. |
| `ID_FIELDS` | Todos los campos de ID que están asociados con este nivel de entidad. |
| `CURRENCY_FIELDS` | Todos los campos de moneda que están asociados con este nivel de entidad. |
| `ENUMERATION_FIELDS` | Todos los campos de serie enumerados que están asociados con este nivel de entidad. |
| `JOIN_FIELDS` | En el objeto GPC, esta carpeta contiene los elementos de datos que permiten al autor de informes filtrar los niveles de este objeto. |
| `<Query Items>` | Todos los elementos de consulta que se pueden utilizar en un informe para el nivel de entidad. |

El asunto de consulta SOXBUSENTITY_GPC contiene tres niveles de jerarquía para elementos de datos: abuelo, padre e hijo. La tabla siguiente describe cuándo utilizar cada nivel en un informe.

| Utilice este nivel... | Si desea hacer esto... |
| --- | --- |
| abuelo | filtro o ámbito |
| nivel superior | grupo, agregado o solicitud |
| hijo | filtro o ámbito. |

##### La carpeta Objeto (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Objetos GRC (modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-object-folder-relational)

La Figura 1 muestra un ejemplo de una carpeta de objetos con todos sus elementos.

*Figura 1. Carpeta Objeto*

![Jerarquía de una carpeta de objetos](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_framework_9.jpg)

La Tabla 1 lista los elementos de una carpeta de objetos.

**Tabla 1. Carpeta Objeto**

| Carpeta/Asunto de consulta | Descripción |
| --- | --- |
| `ID_FIELDS` | Contiene campos de ID que están asociados con este objeto. |
| `PARENT_CONTEXT` | Contiene las relaciones entre los objetos y todos los padres posibles. Los elementos de esta carpeta se utilizan para crear uniones en IBM® Cognos® Analytics -Reporting. |
| `ENUMERATION_FIELDS` | Contiene asuntos de consulta para las variables enumeradas asociadas con este objeto. |
| `<Query Items>` | Todos los elementos de consulta restantes que se pueden utilizar en un informe. |

Cuando el campo **Título** del sistema está habilitado para un tipo de objeto, hay disponible un elemento de consulta `<prefix>_SYSTEM_TITLE` .

Por ejemplo, si el campo **Título** del sistema está habilitado para `SOXProcess`, el elemento de consulta `PR_SYSTEM_TITLE` contiene el título del objeto y `PR_NAME00` contiene el **Nombre** (ID) del sistema.

##### Elementos de consulta de campos de enumeración (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Objetos GRC (modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-enumeration-fields-query-items-relational)

La tabla siguiente lista los elementos de consulta encontrados en una serie enumerada de valor único:

**Tabla 1. Serie enumerada de valor único**

| Asunto de consulta | Descripción |
| --- | --- |
| `<Query Item>` `_SYSTEM_NAME` | Nombre de sistema para el campo. |
| `<Query Item>` | Nombre localizado para el campo. |
| `<Query Item>` `_ID` | ID del campo. |

Cuando se visualiza un valor de serie enumerada en un informe, siempre se debe utilizar `<Query Item>` porque está localizado. Al filtrar por un valor de serie enumerada, utilice el campo `<Query Item>` `_ID` porque está indexado.

La tabla siguiente lista los elementos de consulta encontrados en una serie enumerada multivalor:

**Tabla 2. serie enumerada multivalor**

| Asunto de consulta | Descripción |
| --- | --- |
| `<Query Item>` `_SYSTEM_NAME` | Devuelve un registro para cada valor de la serie enumerada. Se devolverá como nombre del sistema. |
| `<Query Item>` | Devuelve un registro para cada valor de la serie enumerada. Se devolverá como nombre localizado. |
| `<Query Item>` `_ID` | Lista separada por barras verticales ( \| ) de los ID de los valores de enumeración. |
| `<Query Item>` `_SYSTEM_LIST` | Lista separada por comas de los valores de serie del sistema de las enumeraciones. |
| `<Query Item>` `_LIST` | Lista separada por comas de los valores de serie localizados de las enumeraciones. |

Para obtener una lista separada por comas de los valores traducidos de la serie, el autor del informe debe seleccionar el campo `<Query Item>`_LIST y utilizarlo en el informe. Este es el mejor campo que se puede utilizar para visualizar el valor de una serie enumerada multivalor.

#### La carpeta Objetos GRC autónomos (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=folders-grc-objects-standalone-folder-relational-model)

La Figura 1 muestra la carpeta Objetos autónomos con todos sus elementos.

*Figura 1. Carpeta de objetos autónomos (entorno local del idioma de diseño de informes)*

![Jerarquía de la carpeta Objetos autónomos](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_standalone.png)

La Tabla 1 es una explicación de los elementos de la carpeta Objetos autónomos.

**Tabla 1. Carpeta Objetos autónomos**

| Carpeta/Asunto de consulta | Descripción |
| --- | --- |
| `<Secondary Object Name>` | Temas de consulta que contienen todos los objetos secundarios definidos para utilizar dentro del sistema. |

> **Importante:** De forma predeterminada, SOXTask (elemento de acción) se deja unido al objeto SOXIssue porque SOXTask sólo se puede unir al objeto SOXIssue del modelo.

##### Las carpetas Objeto secundario (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Objetos GRC autónomos (modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-secondary-object-folders-relational)

La Figura 1 muestra un ejemplo de una carpeta de objetos secundaria con todos sus elementos.

*Figura 1. Carpeta de objeto secundario (entorno local de idioma de diseño de informe)*

![Jerarquía de una carpeta de objetos secundaria](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_soxissue.png)

La Tabla 1 lista los elementos de una carpeta de objetos secundaria.

**Tabla 1. Carpeta Objeto secundario**

| Carpeta/Asunto de consulta | Descripción |
| --- | --- |
| `ID_FIELDS` | Campos de ID que están asociados con este objeto. |
| `PARENT_CONTEXT` | Contiene las relaciones entre los objetos y todos los padres posibles. Los elementos de esta carpeta se utilizan para crear uniones en IBM® Cognos® Analytics -Reporting. |
| `ENUMERATION_FIELDS` | Contiene asuntos de consulta para las variables enumeradas asociadas con este objeto. |
| `<Query Items>` | Elementos de consulta restantes que se pueden utilizar en un informe. |

Cuando el campo **Título** del sistema está habilitado para un tipo de objeto, hay disponible un elemento de consulta `<prefix>_SYSTEM_TITLE` .

Por ejemplo, si el campo **Título** del sistema está habilitado para `SOXIssue`, el elemento de consulta `IS_SYSTEM_TITLE` contiene el título del objeto y `IS_NAME00` contiene el **Nombre** (ID) del sistema.

#### La carpeta Varios (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=folders-miscellaneous-folder-relational-model)

Figura 1 muestra la carpeta Varios.

*Figura 1. Carpeta Varios (entorno local de idioma de diseño de informe)*

![Jerarquía de la carpeta Varios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_misc.png)

Cuadro 1 lista los elementos de la carpeta Varios.

**Tabla 1. Carpeta Varios**

| Carpeta/Asunto de consulta | Descripción |
| --- | --- |
| `CURRENCIES` | Contiene asuntos de consulta relacionados con las monedas del sistema. |
| `REPORTING_PERIODS` | Contiene asuntos de consulta relacionados con los periodos de elaboración de informes del sistema. |
| `ALL_DOCUMENTATION` | Devuelve una lista de todos los objetos del sistema y el recuento/tipo de documentación que está conectado a cada objeto.<br>Se definen las siguientes solicitudes para este asunto de consulta:<br>• ID de entidad<br>• Establecer ID (establecer siempre = 1) |
| `I18N_INT_OP_CALENDAR` | Contiene la definición de todas las fechas del sistema traducidas a otros valores de fecha. Creando una relación con un campo de fecha, puede filtrar el campo por partes de fecha en este asunto de consulta. |
| `CHECKED_OUT_OBJECTS` | Se utiliza para encontrar todos los objetos extraídos.<br>Se define la siguiente solicitud para este asunto de consulta:<br>• Orden de clasificación<br>El orden de clasificación es una solicitud opcional que acepta uno de los siguientes valores:<br>`[NAME] = 3 [FULL_PATH] = 4 [CONTENT_TYPE] = 5 [DESCRIPTION]= 8 [CHECKED_OUT_BY] = 9 [CHECKED_OUT_DATE] = 10 [PARENT_NAME] = 11 [PARENT_FULL_PATH] = 12 [PARENT_CONTENT_TYPE] = 13`<br>**Nota:** Si no se selecciona ningún valor de ordenación, el valor predeterminado es 3 (el elemento de consulta `NAME` ). |
| `LOCALIZED_CONTENT_TYPES` | Devuelve la lista de todos los tipos de objeto definidos en el sistema. |
| `LOCALIZED_PROPERTY_DEFINITIONS` | Devuelve la definición de todas las propiedades definidas en el sistema. |
| `NON_ASSOCIATED_OBJECTS` | Devuelve todos los objetos huérfanos del sistema.<br>Se definen las siguientes solicitudes para este asunto de consulta:<br>• Orden de clasificación<br>• Establecer ID (establecer siempre = 1)<br>El orden de clasificación es una solicitud opcional que acepta uno de los siguientes valores:<br>`[NAME]= 2 [FULL_PATH] = 3 [CONTENT_TYPE] = 4 [DESCRIPTION] = 7 [CREATOR] = 8 [CREATION_DATE] = 9`<br>**Sugerencia:** Si no se selecciona ningún valor de ordenación, el valor predeterminado es 2 (el elemento de consulta `NAME` ). |
| `USERS_AND_PROFILES` | Contiene la relación de usuarios para el perfil de inicio de sesión. |
| `WF_PROCESS_LOG_VIEW` | Contiene el historial de registro de sucesos de cada instancia de proceso de flujo de trabajo. Incluye la información siguiente: sucesos de proceso que se han producido, por ejemplo, suceso de inicio, cambios de etapa, propietario, cambios de responsable y suscriptor, mensajes de éxito y error, etc. |
| `WF_PROCESS_REPORT_INFO` | Contiene información sobre cada instancia de proceso de flujo de trabajo que hay en el sistema. Incluye la información siguiente: metainformación, información de recursos, fechas, etapas, propietarios, responsables, suscriptores, comentarios, etc. |
| `ADVANCED` | Contiene los asuntos de consulta avanzados que se han creado para crear informes complejos. |

##### La carpeta Divisas (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Varios (modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-currencies-folder-relational)

Figura 1 muestra la carpeta Monedas con todos sus asuntos de consulta.

*Figura 1. Carpeta de monedas (entorno local del idioma de diseño de informes)*

![Jerarquía de la carpeta de monedas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_currencies.png)

Cuadro 1 lista los elementos de la carpeta Monedas.

**Tabla 1. Carpeta Divisas**

| Asunto de consulta | Descripción |
| --- | --- |
| `BASE_CURRENCY` | Devuelve la definición de código de divisa base del sistema. |
| `EXCHANGE_RATES` | Devuelve una lista de todas las divisas definidas y sus tasas de cambio. |

##### Carpeta Periodo de elaboración de informes (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Varios (modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-reporting-period-folder-relational)

Figura 1 muestra la carpeta Periodos de creación de informes con todos sus asuntos de consulta.

*Figura 1. Carpeta de periodo de elaboración de informes (entorno local de idioma de diseño de informes)*

![Jerarquía de la carpeta Periodos de elaboración de informes](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_rprt_periods.png)

Cuadro 1 lista los elementos de la carpeta Periodos de creación de informes.

**Tabla 1. Asuntos de consulta de la carpeta Periodo de elaboración de informes**

| Asunto de consulta | Descripción |
| --- | --- |
| `LABELS` | Devuelve la lista de todos los periodos de elaboración de informes definidos en el sistema. |

##### La carpeta Avanzado (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional › La carpeta Varios (modelo relacional)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=model-advanced-folder-relational)

La Figura 1 muestra la carpeta Avanzado con todas sus subcarpetas.

*Figura 1. Carpeta avanzada (entorno local de lenguaje de diseño de informes)*

![Jerarquía de la carpeta Avanzado](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_advanced.png)

La Tabla 1 lista los elementos de la carpeta Avanzado.

**Tabla 1. Carpeta Avanzado**

| Carpeta/Asunto de consulta | Descripción |
| --- | --- |
| `GPC COMPONENT OBJECTS` | Contiene el asunto de consulta GPC dividido en niveles. |
| `RV_ENTITY_GPC` | Expone la vista del objeto GPC para el autor de informe. Tiene incorporada la seguridad de datos de IBM OpenPages® . |
| `<Object>` `PARENTS)` | Contienen tablas puente entre objetos que se pueden utilizan para crear uniones avanzadas en un informe. |

#### La carpeta Seguridad (modelo relacional)

`Guía del creador de informes › Entorno de elaboración de informes › Las carpetas de nivel superior del modelo relacional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=folders-security-folder-relational-model)

Figura 1 muestra la carpeta Seguridad con todos sus asuntos de consulta.

*Figura 1. Carpeta de seguridad (entorno local del idioma de diseño de informes)*

![Jerarquía de la carpeta Seguridad](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_frmwrk_security.png)

Cuadro 1 lista los elementos de la carpeta Seguridad.

**Tabla 1. Asuntos de consulta de la carpeta Seguridad**

| Asunto de consulta | Descripción |
| --- | --- |
| `ACTORINFO` | Devuelve la definición de todos los usuarios en el sistema. |
| `BUSINESS ENTITY GROUPS` | Devuelve la lista de entidades del sistema y su vía de acceso completa. |
| `EFFECTIVE ACTOR MANAGEMENT RIGHTS UNDER AN ENTITY GROUP` | Devuelve una lista de grupos de entidades y los derechos efectivos definidos para ese grupo.<br>Se define la siguiente solicitud para este asunto de consulta:<br>• ID de grupo de entidad |
| `ROLE_TEMPLATES` | Devuelve una lista de todas las plantillas de función. |
| `ROLES ASSIGNED TO BUSINESS UNITS` | Devuelve una lista de todas las funciones asignadas a una entidad. |
| `ROLES ASSIGNED TO USERS AND GROUPS ON BUSINESS UNITS` | Devuelve una lista de todas las funciones asignadas a usuarios y grupos en una entidad. |
| `USER_GROUP_INFO` | Devuelve una lista de todos los usuarios y grupos definidos en el sistema. |

## Optimización del rendimiento

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-optimizing-performance)

Este capítulo lista técnicas que pueden utilizar los autores de informe para mejorar el rendimiento del informe.

### Filtrado de entidades de negocios de nivel superior

`Guía del creador de informes › Optimización del rendimiento` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=performance-filtering-top-level-business-entities)

Para mejorar el rendimiento de un informe, todos los informes deben tener una solicitud que filtre una entidad de negocios específica o un filtro que examina el informe por entidades o entidad de negocios de alto nivel. Si los informes se ejecutan sin estar enfocados a una única entidad, la consulta realiza varias búsquedas a través de la jerarquía. Esto ralentiza mucho el tiempo de respuesta y puede introducir resultados no deseados para el informe o la página de consulta de la solicitud de entidad.

La solicitud puede tener cualquiera de las formas siguientes:

- Una única solicitud visualizando la vía de acceso completa de las entidades válidas que puede seleccionar el usuario.
- Una serie de solicitudes en cascada que permite al usuario abrirse camino hacia la entidad exacta de la que desean informar.

Si no se necesita una solicitud porque el informe siempre se ejecutará desde la misma entidad, el filtro fijo se puede colocar en el asunto de consulta que selecciona siempre la entidad exacta.

> **Nota:** No utilice los ID de recurso como filtros fijos, ya que serán diferentes en cada instalación.

### Filtrado de periodos de elaboración de informes

`Guía del creador de informes › Optimización del rendimiento` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=performance-filtering-reporting-periods)

Todos los informes deben incluir un filtro en el periodo de elaboración de informes. Un periodo de elaboración de informes es una instantánea de todos los datos de la base de datos como una función de tiempo. Esto crea un conjunto de datos muy grande cada vez que se realiza esta operación.

El filtro se puede crear utilizando un valor de solicitud desde una página de solicitudes o creando un filtro de periodo de elaboración de informes que únicamente selecciona (por instancia) el periodo de elaboración de informes actual:

```
[DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_REPORTING_PERIOD_ID] = -1
```

El valor `-1` significa el periodo de elaboración de informes actual.

### Ignorar el índice

`Guía del creador de informes › Optimización del rendimiento` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=performance-bypassing-index)

En las tablas de base de datos, los índices se definen en todos los ID de valor de serie enumerada. Si utiliza los ID de valor de serie enumerada como filtros, es posible que quiera ignorar el índice específico en el campo para un mejor rendimiento general.

Al crear un filtro de valor de serie enumerada, lo que sucede es que en lugar de elegir el índice del sistema para unir dos tablas de objetos (que incluyen el filtro de serie), Oracle elegirá índices menos eficientes debido al filtro de serie enumerada. Ignorando el índice en la serie enumerada, Oracle creará una consulta más rápida.

Por ejemplo, modifique el filtro en el valor de serie enumerada `Effective` tal como se muestra en el ejemplo siguiente:

```
[DEFAULT_REL].[SOXCONTROL].[CN_OPERATING_EFFECTIVENESS_ID] + 0 = 
#$SOXCONTROL_OPERATING_EFFECTIVENES_DEFINITION_MAP{"Effective"}#
```

Al añadir un 0 (cero) a la parte izquierda de la expresión de filtro, Oracle lo trata como una expresión y el índice conectado a ese campo se ignorará.

A menudo es difícil ver la mejora de rendimiento como resultado de este cambio. Es más evidente cuando se devuelve un número de filas grande bien cuando sale en un archivo PDF/Excel bien cuando el valor de retorno de fila se establece en un número grande para el contenedor de datos en lugar del valor estándar de 20 filas.

> **Nota:** Esta técnica de mejora del rendimiento sólo es aplicable para filtros que contienen ID de serie enumerada.

### Rendimiento de dirección de la consulta

`Guía del creador de informes › Optimización del rendimiento` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=performance-query-direction)

Al explorar todas las posibilidades de cálculo, hay una gran diferencia entre lo que se puede y lo que se debe hacer.

Al escribir un informe, es posible consulta el árbol de relación (es decir, los valores calculados basados en sus antecesores) y esta actividad se desaconseja totalmente. La generación de entorno automática se configura de tal manera que crea uniones que favorecen un mejor rendimiento consultando hacia abajo el árbol de relaciones. Una consulta hacia arriba en el árbol da como resultado un rendimiento de campo calculado erróneo igual que colocar mucha carga en la base de datos puede dar como resultado la ralentización de toda la aplicación.

### Adición de nuevos índices

`Guía del creador de informes › Optimización del rendimiento` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=performance-adding-new-indexes)

Si descubre que un modelo de sus informes implica la unión de dos campos que no están indexados, vale la pena investigar si añadir el índice mejoraría el rendimiento del informe.

Si es así, puede añadir el índice de forma permanente a través de IBM OpenPages®. Consulte la publicación *IBM OpenPages Guía del administrador* para añadir índices a las tablas.

### El valor Uso para la información de parámetro

`Guía del creador de informes › Optimización del rendimiento` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=performance-use-parameter-info-setting)

Puede establecer la propiedad **Utilizar para información de parámetro** en todos los asuntos de consulta.

Este valor determina qué consultas obtienen prioridad al determinar la información de parámetro. Para las consultas de solicitud, este valor debe establecerse en **Sí**. Para todas las demás consultas, este parámetro debe establecerse en **No**. Este valor sólo mejora el rendimiento de la página de solicitud.

## Idioma de diseño de informe

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-report-design-language)

El Idioma del diseño de informe (RDL) es el idioma que no se visualiza en el que están almacenados todos los informes. El resultado es que un informe se puede definir completamente en XML y su contenido de origen se puede visualizar en cualquier editor XML.

Se recomienda que los autores de informes utilicen RDL para diseñar sus informes debido a la existencia de limitaciones cuando no se utiliza RDL.

La siguiente lista de limitaciones puede ser aplicable si no desarrolla el informe en RDL:

- Si cambia una etiqueta de campo en IBM OpenPages®, se mostrará correctamente como un nuevo objeto insertable, pero si ya lo ha utilizado en el informe, esa referencia no se actualizará al nuevo nombre. Esto llevará a confusión.
- Los archivos CQS estarán en RDL.
- El editor de expresiones solo se visualizará en RDL.
- Los campos del modelo de entorno están ordenados por nombre en RDL.
- Será más difícil dar soporte a un informe que tiene una mezcla de idioma nativo y campos RDL.

El RDL para OpenPages utiliza inglés (Canadá) (en_CA).

### Establecimiento del entorno local en OpenPages

`Guía del creador de informes › Idioma de diseño de informe` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=language-setting-your-locale-in-openpages)

Todos los usuarios deben tener un entorno local predeterminado en IBM OpenPages®. El entorno local determina el idioma en el que se visualiza la aplicación, junto con el idioma que se ve cuando se ejecuta un informe.

Para obtener más información sobre la configuración del entorno local, consulte la publicación *IBM OpenPages Guía del administrador*.

#### Soporte de configuración regional e idioma

`Guía del creador de informes › Idioma de diseño de informe › Establecimiento del entorno local en OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=openpages-language-locale-support)

Si utiliza IBM OpenPages® en un idioma distinto del inglés, esta información le ayudará a comprender los valores de idioma y entorno local.

##### Preferencias de idioma del navegador web

La preferencia de idioma del navegador web es el valor que elige para especificar el idioma que se puede visualizar en las páginas web. La preferencia de idioma del navegador web sólo afecta a la página de inicio de sesión de OpenPages . La preferencia de idioma del navegador web no afecta al formato de número y fecha en OpenPages.

Si la preferencia de idioma del navegador web se establece en un idioma que no sea uno de los siguientes, tenga en cuenta que la página de inicio de sesión de OpenPages aparece en inglés:

- Alemán
- Español
- Francés
- Italiano
- Japonés
- Portugués
- Chino
- Inglés

##### Valor de cambio de entorno local en OpenPages

Pulse **![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/user_menu_icon_task_focused_ui.jpg)** > **Cambiar entorno local** para ver una lista de idiomas del producto. Esta configuración de idioma controla el idioma del producto excepto para la página de inicio de sesión.

El formato de datos y los idiomas de informes están disponibles en las siguientes culturas en la lista **Cambiar entorno local**:

**Tabla 1. Idiomas en la lista Cambiar entorno local y las culturas que representan**

| Idioma en la lista **Entorno local** | Cultura |
| --- | --- |
| Francés | Francés (Francia) |
| Alemán | Alemán (Alemania) |
| Italiano | Italiano (Italia) |
| Japonés | Japonés (Japón) |
| Portugués | Portugués (Brasil) |
| Español | Español (España) |
| Chino simplificado | Chino (China) |
| Chino tradicional | Chino (Taiwán) |
| U.K. Inglés | Inglés (Reino Unido) |
| U.S. Inglés | Inglés (Estados Unidos) |

##### Consideraciones para idiomas específicos

Cuando OpenPages se establece para utilizar inglés de EE.UU., las fechas se formatean como mm/dd/aa. Por ejemplo, el 3 de enero de 2020, se formatea como 1/3/20 en lugar de 03/01/2020 en inglés británico.

Cuando el producto se configura para utilizar Español (España), los números se formatean como 123.456,78, donde el punto es un separador de miles y la coma se utiliza como separador decimal. Por ejemplo, el número doce mil quinientos tiene el formato 12.500 en Español (España) mientras que es 12,500 en Español (México).

En algunas culturas, la convención es colocar el símbolo de moneda detrás del número. En OpenPages, los símbolos de moneda siempre se muestran antes del número.

El formato de fecha también puede ser poco convencional.

### Configuración del entorno local en IBM Cognos Analytics

`Guía del creador de informes › Idioma de diseño de informe` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=language-setting-your-locale-in-cognos-analytics)

Establezca el entorno local en IBM® Cognos® Analytics en el lenguaje de diseño de informes (RDL) para OpenPages®, que es inglés (Canadá) (`en_CA`).

#### Acerca de esta tarea

El valor **Idioma del contenido** en IBM Cognos Analytics establece el entorno local para las cabeceras de columna y otro texto de definición de informe en la interfaz de usuario de Cognos .

El valor **Idioma del contenido** no cambia el entorno local que se utiliza cuando un usuario ejecuta un informe en OpenPages. Cuando un usuario ejecuta un informe en OpenPages, el entorno local OpenPages del usuario determina el texto que se devuelve y se visualiza en el informe.

> **Nota: Los entornos locales de** OpenPages deben estar definidos en el entorno de elaboración de informes. Para obtener más información, consulte [Adición de códigos de entorno local al entorno de elaboración de informes](3.5-guia-del-administrador.md#adición-de-códigos-de-configuración-regional-al-entorno-de-elaboración-de-informes).

#### Procedimiento

1. Inicie sesión en IBM Cognos Analytics.
2. Pulse ![Icono Menú personal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_user_menu.png) y pulse **Perfil y valores**.
3. Pulse la pestaña **Valores** .
4. Establezca **Idioma del contenido** en **Inglés (Canadá)**.

## Trabajar con datos relacionales

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-working-relational-data)

Este capítulo explica cómo utilizar el entorno de elaboración de informes al trabajar con datos relacionales.

- Esta información se aplica a los modelos de entorno básicos y estándares pero las explicaciones y los ejemplos son para los modelos de entorno estándares.
- Para obtener una lista de los problemas conocidos y las soluciones temporales disponibles, consulte [Limitaciones y soluciones temporales](#limitaciones-y-métodos-alternativos).
- Para obtener una lista de sugerencias y trucos de rendimiento, consulte [Optimización del rendimiento](#optimización-del-rendimiento).

### Convenios de sintaxis

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-syntax-conventions)

#### Sintaxis de expresión de campo

Los ejemplos de este capítulo utilizan la siguiente sintaxis para filtro o expresiones de campo:

```
[NAMESPACE].[QUERY SUBJECT].[QUERY ITEM] = value
```

Por ejemplo:

```
[DEFAULT_REL].[SOXCONTROL].[CN_OPERATING_EFFECTIVENES] = 'Effective'
```

`[DEFAULT_REL]` es un espacio de nombres en la jerarquía de objetos predeterminada predefinida. Si está utilizando un espacio de nombres diferente, sustituya el nombre del espacio de nombres por el espacio de nombres predeterminado.

#### Sintaxis de la navegación por carpetas

Los ejemplos de este capítulo utilizan la sintaxis siguiente para mostrar la navegación a un elemento de consulta bajo el espacio de nombres `DEFAULT`:

`FOLDER` `|[` `QUERY SUBJECT` `]|[` `QUERY ITEM` `]`

Por ejemplo:

```
REPORTING_PERIODS|[LABELS]|[NAME]
```

### Trabajar con contenedores de datos

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-working-containers)

Las siguientes secciones describen cómo crear y dar formato a informes de lista, referencias cruzadas y gráficos.

Para obtener más información sobre cómo modificar listas, tablas de referencias cruzadas y gráficos, consulte la publicación *IBM® Cognos® Analytics -Guía del usuario de informes*.

#### Trabajar con listas

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con contenedores de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=containers-working-lists)

Un objeto de lista se utiliza para crear un informe que mostrará datos en filas y columnas. Cuando decide por primera vez utilizar un objeto de lista, ésta aparecerá vacía.

La fila de cabecera se destaca en azul mientras que los datos de columna se representan en blanco. Cuando un elemento de datos se coloca en una lista, tanto la cabecera de columna como los datos de columna se llenan.

La lista se divide en las siguientes áreas:

- **Celdas individuales**

  Controla el formato.

- **Cuerpo de columna de lista**

  Controla el formato del área de datos de una columna individual.

- **Columna de lista**

  Controla el formato de una columna individual.

- **Estilo de cuerpo de columnas de lista**

  Controla el formato del área de datos de todas las columnas.

- **Estilo de título de columnas de lista**

  Controla el formato de las cabeceras de todas las columnas.

- **Columnas de lista**

  Controla el formato de las columnas de lista.

- **Lista**

  Controla el formato de toda la lista.

Cada uno de los elementos anteriores tiene un conjunto de propiedades que se puede establecer que afectan a cómo aparecen los datos para el usuario. Cada elemento tiene un conjunto de propiedades ligeramente diferente.

##### Selección de columnas de datos

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con contenedores de datos › Trabajar con listas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=lists-selecting-data-columns)

Puede seleccionar columnas de datos para el informe de lista.

###### Procedimiento

1. En el panel **Objetos insertables** de la pestaña **Fuente** , arrastre y suelte los siguientes elementos de datos en la lista:

   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_NAME00]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_DESCRIPTION]`
2. Ejecute el informe.

   Al soltar elementos en la lista, se forma una consulta utilizando los elementos de datos que ha seleccionado.

###### Resultados

Si no le gusta el orden de las columnas, puede seleccionar una columna y moverla con el ratón a cualquier otro sitio de la lista.

#### Trabajar con tablas de referencias cruzadas

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con contenedores de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=containers-working-crosstabs)

Las tablas de referencias cruzadas son un tipo de contenedor de datos que opera en datos agregados. Los campos de fila y de columna de una tabla de referencias cruzadas son normalmente campos de serie o enumeraciones mientras que la intersección de la tabla de referencias cruzadas debe ser siempre un dato resumido, normalmente un valor numérico.

Puede ver tres áreas en un objeto de tabla de referencias cruzadas:

- **Columnas**

  Los elementos de datos colocados aquí generarán cabeceras de columna. Aquí se pueden descartar varios elementos de datos para crear cabeceras de columna anidadas.

- **Filas**

  Los elementos de datos colocados aquí generarán las filas de datos de la tabla de referencias cruzadas. Se pueden colocar varios elementos de datos aquí para generar filas anidadas.

- **Medidas**

  Solo se puede colocar aquí un elemento de datos que se agregará en las filas y columnas seleccionadas.

##### Selección de elementos de datos

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con contenedores de datos › Trabajar con tablas de referencias cruzadas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=crosstabs-selecting-data-items)

Puede seleccionar los elementos de datos que desea incluir como filas y columnas en el informe de tabla de referencias cruzadas y cómo desea formatearlos.

###### Procedimiento

1. Utilizando **Explorador de consultas**, seleccione **Query1**.
2. En el panel **Objetos insertables** , arrastre y suelte los siguientes elementos de datos en el panel de elementos de datos de la tabla de referencias cruzadas:

   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| [CN_CONTROL_ID]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]| ENUMERATION_FIELDS|OPERATING_EFFECTIVENES (ENUMERATION)| [CN_OPERATING_EFFECTIVENES]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]|[SOXBUSENTITY_GPC]|[CEN_NAME00]`
3. Arrastre y suelte [CN_OPERATING_EFFECTIVENES] en el área de columnas desde la pestaña **Elementos de datos** del panel **Objetos insertables** .
4. Arrastre y suelte [CEN_NAME00] en el área de filas desde la pestaña **Elementos de datos** del panel **Objetos insertables** .
5. Arrastre y suelte [CN_CONTROL_ID] en el área de medidas desde la pestaña **Elementos de datos** del panel **Objetos insertables** .
6. Seleccione el área de medidas y complete los pasos siguientes en el panel Propiedades.

   1. En **Elemento de datos**, establezca **Función de agregación** en **Recuento diferenciado**.
   2. Establezca **Función de agregación de resumen** en **Automático**.
7. Ejecute el informe.

   > **Sugerencia:** Para ordenar las filas en orden ascendente, pulse la columna de filas y, a continuación, pulse el icono **Ordenar** ![Icono de ordenación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-sort.jpg). Para añadir resúmenes a las filas y columnas, pulse el icono **Totalización** ![Icono de totalización](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-summation.jpg) y seleccione **Total**.

#### Trabajar con gráficos

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con contenedores de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=containers-working-graphs)

Los gráficos se utilizan para visualizar datos en un formato visual. Hay una variedad de formatos de gráficos incorporados en CommandCenter con los que el autor de informes debe familiarizarse para mostrar mejor los datos a los usuarios finales.

Un gráfico consta de los siguientes componentes:

- **Medida predeterminada**

  Generalmente, es el componente y del gráfico. Es un valor numérico.

- **Series**

  Un grupo o agrupación para el eje y.

- **Categorías**

  Es generalmente el componente del eje x del gráfico.

##### Creación de un gráfico

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con contenedores de datos › Trabajar con gráficos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=graphs-creating-graph)

Puede crear un gráfico con datos relacionales.

###### Procedimiento

1. Para crear un informar de gráfico, realice los siguientes pasos.

   1. Seleccione la agrupación de gráficos **Circular, anillo** .
   2. Seleccione el tipo de gráfico **Circular** .
   3. Pulse **Aceptar**.
2. Arrastre y suelte los siguientes elementos de consulta en varias secciones del gráfico:

   - `Categories (pies)`

     ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
     [SOXBUSENTITY_GPC]|[SOXBUSENTITY_GPC]|[CEN_NAME00]
     ```
   - `Default Measures`

     ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| 
     [CN_CONTROL_ID]
     ```
   - `Series (pie slices)`

     ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
     OPERATING_EFFECTIVENES (ENUMERATION)|[CN_OPERATING_EFFECTIVENES] 
     ```
3. En **Explorador de consultas**, seleccione la consulta.
4. En el panel **Propiedades** en **Varios**, establezca el nombre de la consulta en **chartMain**.
5. En el panel **Elementos de datos** , seleccione `[CN_CONTROL_ID]` y realice los pasos siguientes.

   1. En el panel **Propiedades** bajo **Elemento de datos**, cambie el valor de la propiedad **Función de agregación** a **Recuento diferenciado**.
   2. En el panel **Propiedades** bajo **Elemento de datos**, cambie el valor de la propiedad **Función de agregación de resumen** a **Automático**.
6. Desde el **Explorador de páginas**, crear una **Página de solicitud** y crear una solicitud **Entidad de negocios** tal como se muestra en [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios).
7. Vuelva a la página de informe principal.
8. Efectúe una doble pulsación en el título y establezca el valor en `Operating Effectiveness`.
9. Ejecute el informe.

### Trabajar con campos enumerados

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-working-enumerated-fields)

Puede incluir campos enumerados en los informes.

#### La estructura de la carpeta Campos enumerados

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con campos enumerados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-enumerated-folder-structure)

Cada objeto tiene una carpeta que contiene todos los campos enumerados definidos para ese objeto. Figura 1 muestra el asunto de consulta SOXControl con su subcarpeta de campos enumerados. Esta carpeta contiene los valores específicos del objeto de los campos enumerados.

Como se había mencionado anteriormente, hay una segunda carpeta Campos enumerados en el entorno. Esta carpeta contiene la definición de enumeración que se va a utilizar para las solicitudes. Consulte [Entorno de elaboración de informes](#entorno-de-elaboración-de-informes) para obtener más información sobre la otra carpeta.

En Figura 1 estamos eligiendo la carpeta que contiene los valores de enumeración específicos del objeto.

*Figura 1. Campos enumerados de SOXControl*

![Campos enumerados en el asunto de consulta SOXControl](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_enumerated_folders.jpg)

Hay dos tipos de campos enumerados: de valor único o multivalor.

El campo de valor único tiene los siguientes elementos de consulta:

- **\<Elemento de consulta>_SYSTEM_NAME**

  Es el nombre del sistema para el campo.

- **\<Elemento de consulta>**

  Es el nombre localizado para el campo.

- **\<Elemento de consulta>_ID**

  Es el ID del campo.

Cuando se visualiza el valor en un informe, se debe utilizar siempre \<Query Item>. Al filtrar este valor, utilice el campo \<Query Item>_ID porque está indexado.

Los campos multivalor tienen los siguientes elementos de consulta:

- **\<Elemento de consulta>_SYSTEM_NAME**

  Devuelve un registro para cada valor de la serie enumerada. Se devuelve como nombre del sistema.

- **\<Elemento de consulta>**

  Devuelve un registro para cada valor de la serie enumerada. Se devuelve como nombre localizado.

- **\<Elemento de consulta>_ID**

  Es una lista de ID separados por una barra vertical (|) de los ID de los valores de enumeración.

- **\<Elemento de consulta>_SYSTEM_LIST**

  Es la lista separada por comas de los valores de serie del sistema de las enumeraciones.

- **\<Elemento de consulta>_LIST**

  Es la lista separada por comas de los valores de serie localizados de las enumeraciones.

Para obtener una lista separada por comas de los valores traducidos de la serie, el autor de informes debe seleccionar el campo \<Elemento de consulta>_LISTA y utilizarlo en el informe. Este es el mejor campo que se puede utilizar para visualizar el valor de una serie enumerada multivalor.

#### Uso de campos enumerados en un informe

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con campos enumerados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-using-enumerated-in-report)

Puede utilizar un campo enumerado en un informe.

##### Procedimiento

1. Pulse la pestaña ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg) **Fuente** en el panel **Objetos insertables** y seleccione el elemento de consulta que desea utilizar en el informe.
2. Arrastre y suelte el elemento de consulta en el informe.

### Trabajar con campos de fecha

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-working-date-fields)

Los campos de fecha se listan como elementos de consulta adjuntos al objeto.

En la figura siguiente, puede ver el `[PR_CREATION_DATE]` listado como un elemento de consulta.

*Figura 1. Asunto de consulta SOXProcess*

![Jerarquía del asunto de consulta SOXPROCESS](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_process_query_subject.jpg)

#### Procedimiento

1. Pulse la pestaña **Origen** ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg) en el panel **Objetos insertables** y seleccione el elemento de consulta que desea utilizar en el informe.
2. Arrastre el elemento de consulta al informe.
3. Seleccione el elemento de consulta que acaba de arrastrar al informe.
4. En el panel **Propiedades** , bajo **Datos** seleccione **Formato de datos**.
5. Para dar formato al campo de fecha, realice los siguientes pasos.

   1. Seleccione **Fecha** para **Tipo de formato**.
   2. Seleccione **Corto** para **Estilo de fecha**.
   3. Seleccione la barra inclinada (/) para **Separador de fecha**.
   4. Seleccione **Mes, Día, Año** para **Orden de fecha**.
   5. Seleccione **Mostrar siglo** (para mostrar un año de 4 dígitos) para **Mostrar años**.
   6. Seleccione **Dos dígitos** para **Mostrar meses**.
   7. Seleccione **Dos dígitos** para **Mostrar días**.
6. Pulse **Aceptar**.

#### Resultados

Además del formateo manual de fechas, hay formatos incorporados que están ubicados en función de la configuración regional del usuario. Si no crea un formato para un campo de fecha, estos formatos están en vigor. Para ver los campos de fecha predefinidos, consulte [Traducción de campos de fecha utilizando formatos de fecha predefinidos](#conversión-de-campos-de-fecha-utilizando-formatos-de-fecha-predefinida).

### Trabajar con campos de moneda

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-working-currency-fields)

Puede añadir campos de moneda a los informes.

#### Asuntos de consulta de la divisa del sistema

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con campos de moneda` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-system-currency-query-subjects)

Los objetos de consulta de moneda del sistema se encuentran bajo la carpeta `MISCELLANEOUS|CURRENCIES` en un espacio de nombres y se clasifican en tipos de cambio o moneda base, tal como se muestra en la Figura 1.

*Figura 1. Carpeta Divisa del sistema*

![Jerarquía de la carpeta de moneda del sistema](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_system_currency_folders.jpg)

El objeto de consulta de las tasa de cambio incluyen un registro para cada tasa de cambio que se ha establecido en el sistema. El asunto de consulta de la divisa base solo devuelve un único registro con la información de divisa base.

En esta lista se ofrecen algunos ejemplos de utilización de los objetos de moneda.

- Visualizar la divisa base (código ISO) en un informe.
- Obtenga el tipo de cambio más reciente para un código de moneda determinado (como alternativa, puede utilizar la función de base de datos `GET_EX_RATE_ISO`). Para obtener detalles, consulte [Obtención del tipo de cambio](#obtención-de-la-tasa-de-cambio).
- Visualizar el símbolo de la divisa en lugar del código de divisa en un informe.

#### Estructura de carpetas de los campos de moneda

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con campos de moneda` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-currency-folder-structure)

Además de los asuntos de consulta, cada objeto tiene una carpeta que contiene todos los campos de moneda definidos para ese objeto. Figura 1 muestra el asunto de consulta SOXRisk con su subcarpeta de campos de moneda.

*Figura 1. Campos de moneda de la cuenta SOX*

![Asunto de consulta SOXRisk con subcampos](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_currency_fields_folder.jpg)

Cada campo de moneda se ubicará en su propia carpeta con cinco valores:

- **\<Query Item>_BA**

  Valor de moneda base del campo.

- **\<Query Item>_BA**

  Valor de moneda base del campo.

- **\<Query Item>_ER**

  Tipo de cambio.

- **\<Query Item>_LA**

  Valor de divisa localizado del campo.

- **\<Query Item>_LC**

  Código de divisa local.

En función del requisito, seleccione el campo adecuado para el informe.

#### Configuración del uso de los campos de divisa en un informe

`Guía del creador de informes › Trabajar con datos relacionales › Trabajar con campos de moneda` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-configuring-use-currency-in-report)

Puede utilizar un campo de divisa en un informe. Configure la aplicación para permitir el uso de los campos de divisa.

##### Procedimiento

1. Pulse la **Fuente** pestaña ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg) en el panel **Objetos insertables** . Seleccione el elemento de consulta que se utilizará en el informe.
2. Arrastre y suelte el elemento de consulta en el informe.
3. Seleccione el elemento de consulta que acaba de soltar en el informe.
4. En el panel **Propiedades** , bajo **Datos** seleccione **Formato de datos**.
5. Para dar formato al campo de moneda, realice los siguientes pasos.

   1. Seleccione **Moneda** como **Tipo de formato**.
   2. Seleccione un formato de moneda predefinido como $ (USD) o configure el formato del elemento de consulta.
6. Pulse **Aceptar**.

##### Resultados

Además del formateo manual de las monedas, se incluyen formatos compilados que se ubican en función de la configuración regional del usuario. Si no crea un formato para un campo de moneda, se utilizan los formatos predeterminados. Para obtener información sobre los formatos de moneda predefinidos, consulte [Conversión de campos de moneda utilizando formatos personalizados](#conversión-de-campos-de-moneda-utilizando-formatos-personalizados).

### Adición de solicitudes

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-adding-prompts)

La página de solicitudes añade interactividad para usuarios y actúa como un mecanismo de control de informes para filtrar y limitar los datos recuperados.

#### Creación de una página de solicitudes

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-creating-prompt-page)

Puede crear una página de solicitud en el informe.

##### Procedimiento

1. Cree una página de solicitud utilizando el icono **Página de solicitud de compilación** en la barra de herramientas.
2. En el título, complete los pasos siguientes.

   1. Efectúe una doble pulsación en **Efectúe una doble pulsación para editar el texto** y especifique el título del informe.
   2. En **Panel de propiedades** bajo la categoría **Varios** , establezca la propiedad **Clases** en **vacío**.
   3. Elimine el subrayado del título pulsando el icono **Subrayado** .
3. En el pie de página, complete los pasos siguientes.

   1. Elimine los botones que no crea que necesitará seleccionando el botón y pulsando el icono **Suprimir** .
   2. Pulse el pie de página y, a continuación, el icono **Centro** para centrar los botones en la página.
   3. Pulse los botones restantes y establezca la propiedad **Color de fondo** en **Plata** en el panel **Propiedades** .
4. Pulse la **Caja de herramientas** pestaña ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) en el panel **Objetos insertables** .
5. Arrastre un objeto **Cuadro** al cuerpo de la página de solicitud. Seleccione dos columnas, sin embargo, necesitará muchas filas. Incluya una fila en blanco después de cada solicitud.
6. Cuando tiene una fila en blanco entre los controles, establezca la altura de celda predeterminada en 15 pt y complete los siguientes pasos.

   1. Seleccione la celda de la tabla en la que desea establecer la altura.
   2. En el panel **Propiedades** , en **Posición**, seleccione **Tamaño y desbordamiento**.
   3. En el cuadro de diálogo, establezca **Altura** en 15 pt.
   4. Pulse **Aceptar**.

#### Adición de una solicitud de periodo de elaboración de informes

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-reporting-period-prompt)

Puede añadir una solicitud de periodo de elaboración de informes al informe.

##### Procedimiento

1. Si todavía no tiene una página de solicitud en el informe, siga las instrucciones de [Creación de una página de solicitud](#creación-de-una-página-de-solicitudes).
2. Para crear una solicitud de periodo de elaboración de informes, realice los siguientes pasos.

   1. Arrastre un **Elemento de texto** a la primera columna de la tabla. Introduzca el texto de la solicitud en el elemento de texto, **Periodo de elaboración de informes:**.
   2. Seleccione la celda de tabla con el elemento de texto y establezca la ubicación para que sea a la derecha horizontalmente y arriba verticalmente.
   3. Haga que el texto esté en negrita utilizando el icono **Negrita** .
   4. Arrastre un objeto **Solicitud de valor** a la segunda columna de la página de solicitud.

      El Asistente de solicitudes se abre.
3. En la pantalla **Seleccionar parámetro** del asistente de solicitud, realice los pasos siguientes.

   1. Seleccione la opción **Crear un parámetro nuevo**.
   2. En el recuadro, escriba un nombre para el parámetro. Por ejemplo, **Periodo de creación de informes**.
   3. Pulse **Siguiente**.
4. En la pantalla **Crear filtro** , realice los pasos siguientes.

   1. Seleccione la opción **Crear un filtro parametrizado**.
   2. En el recuadro **Elemento de modelo** , pulse el botón Examinar y vaya al elemento de consulta LABELID tal como se muestra en el ejemplo siguiente:

      ```
      [DEFAULT_REL]|MISCELLANEOUS|REPORTING PERIODS|[LABELS]|[LABELID]
      ```
   3. Se muestran los siguientes valores en el recuadro:

      ```
      [DEFAULT_REL].[LABELS].[LABELID]
      ```
   4. En el recuadro **Operador** , utilice el signo de igual (=) que es el valor predeterminado.
   5. Borre el recuadro de la opción **Hacer que este filtro sea opcional** .
   6. Si tiene varias consultas en el informe, en el recuadro **Aplicar filtro** , seleccione la consulta a la que se debe aplicar el filtro.
   7. Pulse **Siguiente**.
5. En la pantalla **Llenar control** , realice los pasos siguientes.

   1. Seleccione la opción **Crear nueva consulta** .
   2. En el cuadro **Nombre** , escriba un nombre para la consulta, por ejemplo, `Reporting Period Prompt`.
   3. En el recuadro **Valores a visualizar** , pulse el botón Examinar y vaya al elemento de consulta NAME tal como se muestra en el ejemplo siguiente:

      ```
      [DEFAULT_REL]|MISCELLANEOUS|REPORTING_PERIODS|[LABELS]|[NAME]
      ```

      Se muestran los siguientes valores en el recuadro:

      ```
      [DEFAULT_REL].[LABELS].[NAME]
      ```
   4. Pulse **Finalizar**.

##### Pasar el parámetro de periodo de elaboración de informes de OpenPages

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes › Adición de una solicitud de periodo de elaboración de
informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompt-passing-openpages-reporting-period-parameter)

El selector **Periodo de elaboración de informes** en IBM OpenPages® del usuario se puede utilizar para establecer el periodo de elaboración de informes en un informe. Cuando el informe está instalado en la aplicación, se lleva a cabo una configuración adicional para pasar los valores del periodo de elaboración de informes al informe.

Por ejemplo, si un usuario de la aplicación OpenPages selecciona el periodo actual antes de pulsar un informe, este valor de periodo de elaboración de informes se transfiere al informe en el momento en que se inicia el informe.

Cuando se lanza un informe desde la aplicación, se envían los siguientes parámetros del periodo de elaboración de informes:

- **`ReportingPeriodId`**

  Contiene el valor del identificador para el periodo de elaboración de informes seleccionado.

- **`ReportingPeriodName`**

  Contiene el valor del nombre para el periodo de elaboración de informes seleccionado.

Para filtrar informes, debe utilizar el parámetro `ReportingPeriodId` en expresiones de filtro. Si se utilizan estos parámetros del informe, no hay necesidad de crear una página de solicitudes para seleccionar un periodo de elaboración de informes.

Puede aprovechar el valor del periodo de elaboración de informes del usuario para crear un filtro con la siguiente sintaxis exacta introducida en la Definición de expresión:

```
[DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_REPORTING_PERIOD_ID] = ?ReportingPeriodId?
```

A continuación, se utiliza el periodo de elaboración de informes de la aplicación para filtrar el informe. Recuerde que este filtro tendrá que añadirse a cada una de las consultas del informe.

#### Adición de una solicitud de entidad de negocios

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-business-entity-prompt)

Puede añadir una solicitud de entidad de negocios al informe.

##### Procedimiento

1. Si todavía no tiene una página de solicitud en el informe, siga las instrucciones de [Creación de una página de solicitud](#creación-de-una-página-de-solicitudes).
2. Para crear una solicitud de entidad de negocio, realice los siguientes pasos.

   1. Arrastre un **Elemento de texto** a la primera columna de la tabla. Entre el texto para la solicitud en el elemento de texto.
   2. Seleccione la celda de tabla y establezca la ubicación para que sea a la derecha horizontalmente y arriba verticalmente.
   3. Aplique negrita al texto utilizando el icono Negrita.
   4. Arrastre un objeto **Solicitud de valor** a la segunda columna de la página de solicitud.

      El Asistente de solicitudes se abre.
3. En la pantalla **Elegir parámetro** del asistente de solicitud, realice los pasos siguientes.

   1. Seleccione la opción **Crear un parámetro nuevo**.
   2. En el recuadro, escriba un nombre para el parámetro. Por ejemplo, **Entidad de negocios:**.
   3. Pulse **Siguiente**.
4. En la pantalla **Crear filtro** , realice los pasos siguientes.

   1. Seleccione la opción **Crear un filtro parametrizado**.
   2. En el recuadro **Elemento de modelo** , pulse el botón Examinar y vaya al siguiente elemento de consulta:

      ```
      [DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER|  
      [SOXBUSENTITY_GPC]|ID_FIELDS|[PEN_ENTITY_ID]
      ```
   3. En el cuadro **Operador** , utilice el signo de igual (=) (valor predeterminado).
   4. Deseleccione el recuadro para la opción **Hacer que este filtro sea opcional** .
   5. Si tiene varias consultas en el informe, en el recuadro **Aplicar filtro** , seleccione la consulta a la que se debe aplicar el filtro.
   6. Pulse **Siguiente**.
5. En la pantalla **Rellenar control** , realice los pasos siguientes.

   1. Seleccione la opción **Crear nueva consulta** .
   2. En el cuadro **Nombre** , escriba un nombre para la consulta. Por ejemplo, consulta de **Solicitud de entidad de negocios**.
   3. En el recuadro **Valores a visualizar** , pulse el botón Examinar y vaya al siguiente elemento de consulta:

      ```
      [DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER|  
      [SOXBUSENTITY_GPC]|[PEN_FULL_PATH]
      ```
   4. Se muestran los siguientes valores en el recuadro:

      ```
      [DEFAULT_REL].[SOXBUSENTITY_GPC].[PEN_FULL_PATH] 
      ```
   5. Pulse **Finalizar**.
6. Ahora seleccione la solicitud que acaba de crear y, en la categoría **General** del panel **Propiedades** , cambie la propiedad **Seleccionar interfaz de usuario** a **Recuadro de lista**.

#### Adición de una solicitud de valor enumerado de selección única

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-single-select-enumerated-value-prompt)

Si el informe se ha filtrado interactivamente en un valor de serie enumerado, puede utilizar una Solicitud de valor para llevar a cabo esta acción. Siga este procedimiento para añadir una solicitud de valor enumerado al informe.

##### Procedimiento

1. Si todavía no tiene una página de solicitud en el informe, siga las instrucciones de [Creación de una página de solicitud](#creación-de-una-página-de-solicitudes).
2. Para crear una solicitud de valor enumerado, realice los siguientes pasos.

   1. Arrastre un **Elemento de texto** a la primera columna de la tabla. Entre el texto para la solicitud en el elemento de texto.
   2. Seleccione la celda de tabla y establezca la ubicación para que sea a la derecha horizontalmente y arriba verticalmente.
   3. Haga que el texto esté en negrita utilizando el icono **Negrita** .
   4. Arrastre un objeto **Solicitud de valor** a la segunda columna de la página de solicitud.

      El Asistente de solicitudes se abre.
3. En la pantalla **Elegir parámetro** del asistente de solicitud, realice los pasos siguientes.

   1. Seleccione la opción **Crear un parámetro nuevo**.
   2. En el cuadro, escriba un nombre para el parámetro, por ejemplo, `Operating Effectiveness:`.
   3. Pulse **Siguiente**.
4. En la pantalla **Crear filtro** , realice los pasos siguientes.

   1. Seleccione la opción **Crear un filtro parametrizado**.
   2. En el recuadro **Elemento de modelo** , pulse el botón Examinar y vaya al siguiente elemento de consulta:

      ```
      [DEFAULT_REL]|ENUMERATIONS|SOXCONTROL(ENUMERATIONS)| 
      [CN_OPERATING_EFFECTIVENESS]|[ENUMVALID]
      ```
   3. En el cuadro **Operador** , utilice el signo de igual (=) (valor predeterminado).
   4. Deseleccione el recuadro para la opción **Hacer que este filtro sea opcional** .
   5. Si tiene varias consultas en el informe, en el recuadro **Aplicar filtro** , seleccione la consulta a la que se debe aplicar el filtro.
   6. Pulse **Siguiente**.
5. En la pantalla **Rellenar control** , realice los pasos siguientes.

   1. Seleccione la opción **Crear nueva consulta** .
   2. En el cuadro **Nombre** , escriba un nombre para la consulta, por ejemplo, `Operating Effectiveness Prompt Query`.
   3. En el recuadro **Valores a visualizar** , pulse el botón Examinar y vaya al siguiente elemento de consulta:

      ```
      [DEFAULT_REL]|ENUMERATIONS|SOXCONTROL(ENUMERATIONS)|  
      [CN_OPERATING_EFFECTIVENES]|[CN_OPERATING_EFFECTIVENES]
      ```
   4. Se muestran los siguientes valores en el recuadro:

      ```
      [DEFAULT_REL].[CN_OPERATING_EFFECTIVENES].[CN_OPERATING_EFFECTIVENES]
      ```
   5. Pulse **Finalizar**.
6. Seleccione la solicitud que acaba de crear y, en la categoría **General** del panel **Propiedades** , cambie la propiedad **Seleccionar interfaz de usuario** a **Recuadro de lista**.
7. Si hay un número limitado de elementos en la solicitud, puede establecer la altura de la solicitud en un valor que muestra solo las solicitudes y no los espacios en blanco. Complete los pasos siguientes.

   1. Seleccione la solicitud en la tabla que desee establecer la altura.
   2. En el panel Propiedades, en **Posición**, seleccione **Tamaño y desbordamiento**.
   3. En el cuadro de diálogo, establezca la altura en 14 pt el número de filas de la solicitud.
   4. Pulse **Aceptar**.
8. El filtro creado en la consulta seleccionada del informe aparece como en el siguiente ejemplo:

   ```
   [DEFAULT_REL].[CN_OPERATING_EFFECTIVENESS].[ENUMVALID] = ?Operating 
   Effectiveness?
   ```

   1. El problema con la creación del filtro anterior es que hace que Oracle prefiera el índice asociado con la serie enumerada en lugar de un mejor funcionamiento del índice del sistema para unir tablas relacionadas con los objetos anteriores y posteriores a este objeto. Para resolver este problema, modifique el filtro correspondiente a esta solicitud añadiendo un `+ 0` (más cero) a la parte izquierda de la expresión de filtro para inhabilitar el uso de índices en este campo.

      ```
      [DEFAULT_REL].[CN_OPERATING_EFFECTIVENESS].[ENUMVALID] + 0 = ?Operating 
      Effectiveness?
      ```
9. Ejecute el informe.

##### Resultados

Para obtener detalles y más explicaciones, consulte la sección sobre [Optimización del rendimiento](#optimización-del-rendimiento).

#### Adición de una solicitud de valor enumerado de selección múltiple

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-multi-select-enumerated-value-prompt)

Puede añadir una solicitud de valor enumerado de selección múltiple al informe.

##### Procedimiento

1. En la página de solicitudes, seleccione la solicitud de valor que acaba de crear.
2. En **Panel de propiedades** bajo la categoría **General** , establezca el valor de la propiedad **Selección múltiple** en **Sí**.
3. En **Explorador de consultas**, seleccione la consulta donde se encuentra el filtro.
4. Seleccione el filtro que está relacionado con esta solicitud. Cambie el operador del signo igual (=) por **in**. Los paréntesis no son necesarios.
5. Pulse **Aceptar**.
6. Ejecute el informe.

##### Resultados

Ahora puede seleccionar dos valores de la solicitud además de tener los enlaces **Seleccionar todo** y **Deseleccionar todo** para que accedan los usuarios.

##### Adición de un valor estático Todo a una solicitud de valor enumerado de selección múltiple

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes › Adición de una solicitud de valor enumerado de selección
múltiple` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=amsevp-adding-all-static-value-multi-select-enumerated-value-prompt)

Hay instancias en las que el cliente ha ocultado los enlaces Seleccionar todo y Deseleccionar todo pero aún quiere que sus usuarios tengan la capacidad de Seleccionar todo como opción estática. Puede añadir una opción estática Seleccionar todo al informe.

###### Procedimiento

1. En la página de solicitudes, seleccione la solicitud de valor que acaba de crear.
2. En **Panel de propiedades** bajo la categoría **Datos** , pulse la propiedad **Opciones estáticas** y realice los pasos siguientes.

   1. Pulse el icono ![Icono Añadir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-add_new.jpg)Añadir.
   2. En el cuadro de diálogo **Editar**, establezca el valor **Utilizar** en -1 y el valor **Mostrar** en **Todos**.
   3. Pulse **Aceptar**.
   4. Pulse **Aceptar**.
3. Para establecer el valor Todo como valor predeterminado cuando aparezca la página de solicitudes, realice los siguientes pasos.

   1. En el panel **Propiedades** bajo la categoría **General** , pulse **Selecciones predeterminadas**.
   2. Pulse el icono ![Icono Añadir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-add_new.jpg)Añadir.
   3. Escriba `-1` para el valor.
   4. Pulse **Correcto** dos veces.
4. En el panel Propiedades, en **Posición**, seleccione **Tamaño y desbordamiento**y, en el recuadro de diálogo, establezca la altura en **56 pt**.
5. En el filtro para la solicitud de selección múltiple, ahora debe ir y añadir `?Operating Effectiveness? = -1` al filtro.
6. Ejecute el informe.

###### Resultados

Esto arregla la solicitud, pero también tiene que arreglar el filtro. Para tener en cuenta el valor estático de "Todo" que acaba de añadir, cambie el filtro como se muestra en el ejemplo siguiente:

```
[DEFAULT_REL].[SOXCONTROL].[CN_OPERATING_EFFECTIVENESS_ID] in 
?Operating Effectiveness? or ?Operating Effectiveness? = -1
```

Esto ignora el filtro en la base de datos y anula el uso el filtro por lo que se aceptan todos los valores.

#### Adición de una solicitud de fecha

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-date-prompt)

Puede añadir una solicitud de fecha al informe.

##### Procedimiento

1. Si todavía no tiene una página de solicitud en el informe, siga las instrucciones de [Creación de una página de solicitud](#creación-de-una-página-de-solicitudes).
2. Para crear una solicitud de fecha, realice los siguientes pasos.

   1. Arrastre un **Elemento de texto** a la primera columna de la tabla. Entre el texto para la solicitud en el elemento de texto.
   2. Seleccione la celda de tabla y establezca la ubicación para que sea a la derecha horizontalmente y arriba verticalmente.
   3. Haga que el texto esté en negrita utilizando el icono **Negrita** .
   4. Arrastre un objeto **Solicitud de fecha** a la segunda columna de la página de solicitud.

      Se abre el Asistente de solicitudes.
3. En la pantalla **Elegir parámetro** del asistente de solicitud, realice los pasos siguientes.

   1. Seleccione la opción **Crear un parámetro nuevo**.
   2. En el cuadro, escriba un nombre para el parámetro, por ejemplo, `Start Date:`.
   3. Pulse **Siguiente**.
4. En la pantalla **Crear filtro** , realice los pasos siguientes.

   1. Seleccione la opción **Crear un filtro parametrizado**.
   2. En el recuadro **Elemento de modelo** , pulse el botón Examinar y vaya al siguiente elemento de consulta:

      ```
      DEFAULT_REL|GRC_OBJECTS|[SOXCONTROL]|[CN_CREATION_DATE]
      ```
   3. En el cuadro **Operador** , utilice el signo de igual (=) (valor predeterminado).
   4. Deseleccione el recuadro para la opción **Hacer que este filtro sea opcional** .
   5. Si tiene varias consultas en el informe, en el recuadro **Aplicar filtro** , seleccione la consulta a la que se debe aplicar el filtro.
   6. Pulse **Siguiente**.
5. Seleccione la solicitud que acaba de crear y, en la categoría **General** del panel **Propiedades** , cambie el valor de **Seleccionar interfaz de usuario** a **Recuadro de edición**.
6. Ejecute el informe.

#### Adición de una solicitud de rango de fechas

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-date-range-prompt)

El proceso para crear una solicitud de rango de fechas requiere que añada dos objetos Solicitud de fecha a la página de solicitudes (uno para la fecha de inicio y el otro para la fecha de finalización) del informe, y modifique un filtro para la fecha de finalización.

##### Acerca de esta tarea

Por ejemplo, si el usuario selecciona la fecha de inicio 1 de julio de 2006 y la fecha de finalización 7 de julio de 2006 de una solicitud de rango de fechas, de forma efectiva, el filtro se aplicará entre el 1 de julio de 2006 00:00 y el 7 de julio de 2006 00:00. Para recuperar los registros independientemente de la hora de la fecha de finalización, tiene que modificar el filtro.

En el ejemplo siguiente, se ha creado un filtro para el elemento de consulta `[CREATED_ON]` en el asunto de consulta `[ACTOR_AUDIT_TRAIL]`.

##### Procedimiento

1. Cree una solicitud de fecha para la fecha de inicio tal como se describe en [Adición de una solicitud de fecha](#adición-de-una-solicitud-de-fecha). Utilice el nombre de parámetro de **Fecha de inicio**. En el asistente de solicitud, cambie el operador a `>=`.
2. De forma similar, cree una solicitud de fecha para la fecha de finalización tal como se describe en [Añadir una solicitud de fecha](#adición-de-una-solicitud-de-fecha). Utilice el nombre de parámetro de **Fecha de finalización**. En el asistente de solicitud, cambie el operador a `<=`.
3. En el panel **Filtros de detalles** para la consulta, edite el lado derecho de la expresión de filtro para el elemento de consulta añadiendo la función `_add_days(?End Date?,1)` después del operador `<=` . Esto garantizará que el rango de fechas incluye la fecha de finalización completa.

##### Resultados

Por ejemplo, `[OPENPAGES_REL].[ACTOR_AUDIT_TRAIL].[CREATED_ON] <= _add_days(?EndDate?,1)`. La función `_add_days` añade un día más a la fecha de finalización.

#### Adición de una solicitud de opciones estáticas

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-static-choices-prompt)

En algunos casos, una solicitud no se puede llenar con valores basándose en un elemento de consulta. Si, por ejemplo, un informe contiene dos columnas: Estado del problema y Fecha del problema, y desea que el informe ordene por la columna Estado del problema o Fecha del problema dependiendo de la selección del usuario, debe crear una solicitud de valor que utilice opciones estáticas (como una cabecera de columna).

##### Procedimiento

1. Si todavía no tiene una página de solicitud en el informe, siga las instrucciones de [Creación de una página de solicitud](#creación-de-una-página-de-solicitudes).
2. Para crear una solicitud estática, realice los siguientes pasos.

   1. Arrastre un **Elemento de texto** a la primera columna de la tabla. Entre el texto para la solicitud en el elemento de texto.
   2. Seleccione la celda de tabla y establezca la ubicación para que sea a la derecha horizontalmente y arriba verticalmente.
   3. Haga que el texto esté en negrita utilizando el icono **Negrita** .
   4. Arrastre un objeto **Solicitud de valor** a la segunda columna de la página de solicitud.

      El Asistente de solicitudes se abre.
3. En la pantalla **Elegir parámetro** del asistente de solicitud, realice los pasos siguientes.

   1. Seleccione la opción **Crear un parámetro nuevo**.
   2. En el cuadro, escriba un nombre para el parámetro, por ejemplo, `Sort Order`.
   3. Pulse **Finalizar**.
4. Para añadir los valores estáticos a la solicitud, realice los siguientes pasos.

   1. Seleccione el objeto de solicitud recién creado.
   2. En el recuadro **Propiedades** bajo **Datos**, pulse el botón **Opciones estáticas** para abrir el recuadro **Opciones estáticas** .
5. En el recuadro **Opciones estáticas** , realice los pasos siguientes.

   1. Pulse el botón ![Icono Añadir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-add_new.jpg) **Añadir** para abrir el recuadro **Editar** .
   2. En el campo **Utilizar** , especifique el valor que desea utilizar en el filtro. Por ejemplo, 1.
   3. En el campo **Mostrar** , especifique el valor que se va a visualizar en la solicitud. Por ejemplo, Estado del problema.
   4. Para añadir más valores, repita los pasos a-c.

##### Resultados

Puede utilizar el parámetro recién creado, por ejemplo, Orden de clasificación, para filtrar los informes. Para obtener información sobre la ordenación de datos, consulte [Ordenación de datos](#ordenación-de-datos) .

#### Adición de una solicitud en cascada

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-cascading-prompt)

Las solicitudes en cascada son solicitudes que se llenan dinámicamente basándose en una elección realizada en la solicitud anterior. Por ejemplo, si elige un periodo de creación de informes de una solicitud, la segunda solicitud se puede llenar con Entidades de negocios que existen en ese periodo de elaboración de informes.

Siga este procedimiento para añadir una solicitud en cascada a una solicitud de entidad para un periodo de elaboración de informes seleccionado.

##### Procedimiento

1. Si todavía no tiene una página de solicitud en el informe, siga las instrucciones de [Creación de una página de solicitud](#creación-de-una-página-de-solicitudes).
2. Si todavía no ha creado una solicitud de periodo de elaboración de informes, siga las instrucciones de [Adición de una solicitud de periodo de elaboración de informes](#adición-de-una-solicitud-de-periodo-de-elaboración-de-informes).
3. Si todavía no ha creado una solicitud de entidad de negocios, siga las instrucciones de [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios).
4. Seleccione la solicitud **Periodo de elaboración de informes** .
5. En el panel **Propiedades** de la solicitud **Periodo de elaboración de informes** en **General**, realice los pasos siguientes.

   1. Establezca la propiedad **Envío automático** en **Sí**.
   2. Si la propiedad **Selecciones predeterminadas** contiene un valor predeterminado, elimínelo.
6. Seleccione la solicitud **Entidad de negocios** .
7. En el panel **Propiedades** de la solicitud **Entidad de negocios** , establezca la propiedad **Origen de cascada** en el parámetro **Periodo de elaboración de informes**de la solicitud Periodo de creación de informes. Esto habilitará la solicitud en cascada en la solicitud de entidad.
8. En la consulta **Solicitud de entidad empresarial** , realice los pasos siguientes.

   1. Asegúrese de que hay un elemento de consulta del periodo de elaboración de informes.
   2. Crear un filtro utilizando el elemento de consulta de periodo de informe y la solicitud ?¿Periodo de elaboración de informes? ?

##### Resultados

La solicitud de entidad de negocios no se llena porque está esperando por el valor que se va a entrar en la solicitud del periodo de elaboración de informes. Puesto que ha establecido el valor Enviar automáticamente en Sí, tan pronto como el usuario selecciona un valor en la solicitud Periodo de creación de informes, la consulta de solicitud de entidad de negocios se ejecutará con este filtro de periodo de elaboración de informes.

#### Adición de solicitudes para asuntos de consulta

`Guía del creador de informes › Trabajar con datos relacionales › Adición de solicitudes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=prompts-adding-query-subjects)

En el modelo de entorno de IBM OpenPages® , algunos asuntos de consulta contienen macros de solicitud.

Cuando se utiliza ese asunto de consulta en un informe, debe proporcionar valores para esas solicitudes (para macros de solicitud y valores, consulte [Entorno de elaboración de informes](#entorno-de-elaboración-de-informes)). Por ejemplo, el asunto de consulta [MODIFIED RESOURCES BY ENTITY] (localizado en la carpeta DEFAULT|[DEFAULT_REL]| AUDIT_TRAIL) contiene macros de solicitudes. Cuando utiliza ese asunto de consulta en un informe, se genera una página de solicitudes.

La página de solicitudes generada no es fácil de utilizar. Para ayudar al usuario del informe, puede crear su propia página de solicitud del informe utilizando los nombres de las macros de solicitudes existentes. Por ejemplo, puede crear una solicitud de valor para Entidad de negocio utilizando el parámetro existente **ID de entidad padre** como parámetro de solicitud de salida. Cuando ejecuta el informe, primero aparece la página de solicitud del informe y, a continuación, la página de solicitud generada automáticamente con el resto de parámetros.

Puede eliminar la página de solicitud generada automáticamente creando solicitudes para todas las macro de solicitudes de la consulta.

Los métodos para crear estas solicitudes es idéntica a las ya descritas en este capítulo. La única diferencia es que en el asistente de solicitud en la pantalla **Seleccionar parámetro**, selecciona la opción **Usar parámetro existente** y selecciona la solicitud adecuada de la lista.

### Adición de campos de texto enriquecido

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-adding-rich-text-fields)

Si el texto no es HTML o texto enriquecido, se visualizará como texto sin formato en el informe. Los campos de texto en IBM OpenPages® se pueden establecer para visualizar texto enriquecido. Debe realizarse un formateo especial en los informes para visualizar estos campos correctamente.

#### Procedimiento

1. Abra un informe de lista.
2. En el panel **Objetos insertables** , arrastre y suelte los siguientes elementos de datos en la lista:

   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]|[CEN_NAME00]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXPROCESS]|[PR_NAME00]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXPROCESS]|[PR_DESCRIPTION]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXPROCESS]| [PR_ADDITIONAL_DESCRIPTION] (This is defined as a Rich Text field)`
3. Pulse la pestaña ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) **Caja de herramientas** en el panel **Objetos insertables** y, a continuación, arrastre y suelte un objeto **Elemento HTML** en la lista.
4. Para seleccionar el elemento HTML en la lista, realice los siguientes pasos.

   1. En el panel **Propiedades** en **Origen HTML**, establezca la propiedad **Tipo de origen** en **Valor de elemento de datos**.
   2. Establezca la propiedad **Valor de elemento de datos** en [PR_ADDITIONAL_DESCRIPTION].
5. Corte [PR_ADDITIONAL_DESCRIPTION] de la lista.
6. Para seleccionar la cabecera de columna Elemento HTML, realice los siguientes pasos.

   1. En el panel **Propiedades** en **Origen de texto**, establezca la propiedad **Tipo de origen** en **Etiqueta de elemento de datos**.
   2. Establezca la propiedad **Etiqueta de elemento de datos** en [PR_ADDITIONAL_DESCRIPTION].
   3. Ejecute el informe.

   Esto da formato correctamente cuando visualiza el informe en HTML pero cuando representa el informe en formato PDF o Excel, el texto enriquecido se visualiza como un campo en blanco. Para corregir este problema, complete los pasos siguientes.
7. En el **Explorador de consultas**, abra la consulta de lista.
8. Para añadir un nuevo **Elemento de datos** a la consulta, realice los pasos siguientes.

   1. Arrastre un **Elemento de datos** al panel de elementos de datos.
   2. Especifique el código siguiente en el panel **Definición de expresión** :

      - **Db2®**

        ```
        trim(regexp_replace([DEFAULT_REL].[SOXPROCESS].[PR_ADDITIONAL_DESCRIPTION], '<[^>]+>', null))
        ```

      - **Oracle**

        ```
        trim(regexp_replace([DEFAULT_REL].[SOXPROCESS].[PR_ADDITIONAL_DESCRIPTION], '<[^>]+>'))
        ```
   3. ![Icono Validar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) **Val** **ide la expresión** y, a continuación, haga clic en Aceptar.
9. En el panel **Propiedades** del elemento de datos que acaba de añadir, realice los pasos siguientes.

   1. En el grupo **Datos** , establezca la propiedad **Nombre** en **Descripción adicional**.
   2. En el grupo **Datos** , establezca la propiedad **Función de agregación** en **Ninguno**.
   3. En el grupo **Datos** , establezca la propiedad **Función de agregación de resumen** en **Ninguno**.
10. Vaya a la página de informe principal.
11. Arrastre y suelte **Descripción adicional** en la lista.
12. En el panel **Propiedades** del título de columna de lista de **Descripción adicional**, realice los pasos siguientes.

    1. En **Origen de texto**, establezca la propiedad **Tipo de origen** en **Etiqueta de elemento de datos**.
    2. Establezca la **Etiqueta de elemento de datos** en **PR_ADDITIONAL_DESCRIPTION**.
13. Para crear una variable condicional, realice los siguientes pasos.

    1. En el **Explorador de condiciones** , pulse **Variables**.
    2. Arrastre y suelte una **Variable de cadena** en el panel **Variables** .
    3. En el panel **Definición de expresión** , especifique `ReportOutput ()` y pulse **Aceptar**.
    4. Usando **el icono Añadir** de ![Icono Añadir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-add_new.jpg), introduce **HTML** como variable.
    5. En el panel **Propiedades** , en **Varios**, en la propiedad **Nombre** , especifique **Salida de informe**.
14. Vuelva a la página de informe principal y complete los siguientes pasos:

    1. Seleccione la columna con el **elemento HTML**.
    2. Utilizando el selector de ancestros, seleccione **Columna de lista**.
    3. En el panel **Propiedades** bajo **Condicional**, establezca la propiedad **Variable de estilo** en **Resultado del informe**.
    4. En el **Explorador de condiciones** , seleccione **Otros** bajo la variable **Resultado del informe** .
    5. En el panel **Propiedades** bajo **Recuadro**, establezca la propiedad **Tipo de recuadro** en **Ninguno**.
    6. En el **Explorador de condiciones** seleccione **(sin variables)**.
15. Complete los pasos siguientes.

    1. Seleccione la columna con **< Descripción adicional >** en el cuerpo de la lista.
    2. Utilizando el selector de ancestros, seleccione **Columna de lista**.
    3. En el panel **Propiedades** bajo **Condicional**, establezca la propiedad **Variable de estilo** en **Resultado del informe**.
    4. En el **Explorador de condiciones** , seleccione **HTML** bajo la variable **Salida de informe** .
    5. En el panel **Propiedades** bajo **Recuadro**, establezca la propiedad **Tipo de recuadro** en **Ninguno**.
    6. En el **Explorador de condiciones** seleccione **(sin variables)**.
16. Ejecute el informe.

#### Resultados

El informe se parecerá al anterior cuando se ejecutó en formato HTML. Sin embargo, ahora cuando ejecuta el informe como PDF, el texto enriquecido aparecerá como texto sin formato en el informe.

El formato condicional que hemos creado muestra la columna formateada en HTML o la otra columna Descripción adicional cuando HTML no es el formato de salida.

En este ejemplo, hemos utilizado un objeto HTML para visualizar el texto enriquecido. Hay un objeto Texto enriquecido en la caja de herramientas, pero solo soporta una cantidad de propiedades de texto enriquecido extremadamente limitada por lo que no se recomienda su uso.

### Adición de imágenes e iconos

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-adding-images-icons)

Puede mejorar el aspecto de los informes añadiendo iconos o el logotipo de la compañía a los informes.

#### Antes de empezar

Hable con el administrador del sistema sobre la identificación de la vía de acceso del directorio de imagen correcta para una instalación concreta. Las vías de acceso son diferentes para Linux® y el sistema operativo Microsoft Windows .

Se recomienda almacenar los archivos de imagen en el directorio siguiente en el servidor de IBM® Cognos® :

- `C:\<Cognos_Home>\webcontent\bi\images\<icon file name>`

Utilice una vía de acceso relativa:

`../bi/images/<icon file name>`

Los archivos de imagen para informes de versiones anteriores pueden localizarse en los siguientes directorios:

- `C:\<Cognos_Home>\webcontent\skins\branding\<icon file name>`
- `C:\<Cognos_Home>\webcontent\bi\skins\branding\<icon file name>`

#### Procedimiento

1. Cree un nuevo informe de lista.
2. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg)y, a continuación, arrastre un objeto **Imagen** a la primera columna del informe de lista.
3. En la barra de herramientas, pulse el icono **Bloquear** ![Icono de bloqueo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-padlock.jpg) para desbloquear la plantilla (el icono cambia a desbloqueado).
4. Seleccione el objeto **Imagen** .
5. En el panel **Propiedades** del objeto **Imagen** , realice los pasos siguientes.

   1. En la categoría **Fuente URL**, haga clic en la propiedad **URL**.
   2. En el campo **URL la imagen**, introduzca la siguiente ruta de archivo `../bi/images/<icon file name>` para añadir un icono al informe. Debe utilizar una vía de acceso relativa como se muestra en este ejemplo o el informe no se podrá mover entre sistemas. También debe utilizar las mayúsculas correctas para el nombre del icono o no aparecerán correctamente en un sistema Linux.
   3. Pulse **Aceptar**.
6. En la **barra de herramientas**, pulse de nuevo el icono **Bloquear** para bloquear la plantilla (el icono cambia a bloqueado).
7. Ejecute el informe.

#### Resultados

Todas las imágenes se pueden utilizar como enlace CrossTrack de la misma forma que se ha utilizado el objeto de hipervínculo. Las imágenes también se pueden colocar en un hiperenlace para que el usuario pueda pulsar la imagen o el hiperenlace y obtener el mismo comportamiento.

### Adición de cálculos

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-adding-calculations)

Existen dos métodos para la creación de cálculos en el entorno.

- Puede crear campos calculados a través de IBM OpenPages® ([Creación de un campo calculado](#creación-de-un-campo-calculado)).
- Puede crear un cálculo en el archivo de asunto de consulta personalizado ([Creación de cálculos](#creación-de-cálculos)).

Una vez se han creado los cálculos y se regenera el entorno, están disponibles para el autor de informe en la carpeta de campos calculados en cada espacio de nombres.

Los cálculos se pueden incorporar un informe igual que cualquier otro elemento de consulta. Se pueden agregar utilizando el método descrito en [Agregación de datos](#agregación-de-datos).

### Ordenación de datos

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-sorting)

Puede organizar datos en una columna de informes especificando un orden de clasificación. Los datos se pueden organizar en orden ascendente o descendente basándose en los valores de cualquier columna.

#### Uso de la ordenación simple

`Guía del creador de informes › Trabajar con datos relacionales › Ordenación de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-using-simple-sorting)

Puede ordenar una columna utilizando la función de ordenación integrada.

##### Procedimiento

1. Abra un informe.
2. Pulse la columna en la que desea ordenar.
3. Pulse el **Ordenación** icono ![Icono de ordenación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-sort.jpg) en la barra de herramientas y, a continuación, pulse **Orden ascendente** o **Ordenar en orden descendente**.
4. Ejecute el informe.

#### Uso de la ordenación avanzada

`Guía del creador de informes › Trabajar con datos relacionales › Ordenación de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-using-advanced-sorting)

La función de ordenación avanzada se utiliza para aplicar ordenaciones en varias columnas de un informe. Permite al autor del informe especificar el orden de columna y la dirección de ordenación por los que desea que esté ordenado el informe.

##### Procedimiento

1. Abra un informe.
2. Pulse el **Ordenación** icono ![Icono de ordenación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-sort.jpg) en la barra de herramientas y, a continuación, pulse **Ordenación avanzada**.
3. En el diálogo **Ordenación avanzada** , determine por qué columnas desea ordenar y arrástrelas y suéltelas bajo la carpeta **Lista de clasificación de detalles** .
4. Puede cambiar el orden con las flechas arriba y abajo o cambiar la dirección de ordenación.

##### Resultados

Si había grupos creados en esta lista, debe verlos en la carpeta de grupos. La ordenación de grupos tiene lugar antes de la ordenación de detalles de la lista. El diálogo de ordenación avanzada le proporciona el poder de crear un orden que no se basa en el orden en el que aparecen las columnas en el informe.

#### Uso de la ordenación personalizada

`Guía del creador de informes › Trabajar con datos relacionales › Ordenación de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-using-custom-sorting)

Puede haber situaciones en las que los datos ordenados en orden ascendente o descendente no cumplen los requisitos.

##### Acerca de esta tarea

Por ejemplo, tenga en cuenta un informe que muestra nombres de control y si eficacia operativa. El campo `Operating Effectiveness` puede tener uno de estos valores: `Effective`, `Ineffective`o `Not Determined`.

Si desea mostrar los valores de control para el campo `Operating Effectiveness` en este orden: `Ineffective`, `Not Determined`y `Effective`, no puede obtener este resultado ordenando la columna `Operating Effectiveness` en orden ascendente o descendente. Si la columna se ordena por orden ascendente, los valores del informe se mostrarán como `Effective`, `Ineffective`y `Not Determined`. Si la columna se ordena por orden descendente, los valores se mostrarán como `Not Determined`, `Ineffective`y `Effective`.

Para lograr un orden de clasificación personalizado, tiene que crear un elemento de datos nuevo en el **Asunto de consulta** subyacente y, a continuación, ordenar ese elemento de datos.

El ejemplo siguiente muestra cómo crear un orden de clasificación personalizado para el campo `Operating Effectiveness` del objeto de control en un nuevo informe de lista.

##### Procedimiento

1. Cree un nuevo informe de lista con los siguientes elementos de consulta:

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]| ENUMERATION_FIELDS|
           OPERATING_EFFECTIVENES (ENUMERATION)| [CN_OPERATING_EFFECTIVENES]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]| ENUMERATION_FIELDS|
           OPERATING_EFFECTIVENES (ENUMERATION)| [CN_OPERATING_EFFECTIVENES_ID]
     ```
2. Ejecute el informe y observe el orden de los controles.
3. Utilizando **Explorador de consultas** , seleccione la consulta que va a ordenar de forma personalizada.
4. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) en el panel **Objetos insertables** . y, a continuación, arrastre y suelte un objeto **Elemento de datos** en el recuadro **Elementos de datos** de la consulta.
5. En el panel **Definición de expresión** , especifique la expresión siguiente:

   ```
   Case ([CN_OPERATING_EFFECTIVENES_ID] + 0)
   when #$SOXCONTROL_OPERATING_EFFECTIVENES_DEFINITION_MAP
       {"Ineffective"}# then 1
   when #$SOXCONTROL_OPERATING_EFFECTIVENES_DEFINITION_MAP
       {"Not Determined"}# then 2 
   when #$SOXCONTROL_OPERATING_EFFECTIVENES_DEFINITION_MAP
       {"Effective"}# then 3 
   else 4
   end
   ```
6. Pulse el icono **Validar** ![Icono Validar expresión](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) para validar la expresión y, a continuación, pulse **Aceptar**.
7. En el panel **Propiedades** del elemento de datos, realice los pasos siguientes.

   1. En **Datos**, establezca la propiedad **Nombre** escribiendo un nombre para el elemento de datos. Por ejemplo, **Orden de clasificación**.
   2. En Datos, establezca la propiedad **Función de agregación** en **Ninguno**.
   3. En Datos, establezca la propiedad **Función de agregación de resumen** en **Ninguno**.
8. Siguiendo las instrucciones en [Utilización de ordenación avanzada](#uso-de-la-ordenación-avanzada), añada el elemento de datos **Orden de clasificación** a la **Lista de clasificación de detalles**.
9. Ejecute el informe.

#### Uso de la ordenación solicitada

`Guía del creador de informes › Trabajar con datos relacionales › Ordenación de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-using-prompted-sorting)

Puede ordenar un informe en la columna seleccionada por el usuario desde la página de solicitud del informe.

##### Procedimiento

1. Cree un nuevo informe de lista con los siguientes elementos de consulta:

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]| ENUMERATION_FIELDS|
           OPERATING_EFFECTIVENESS (ENUMERATION)|[CN_OPERATING_EFFECTIVENES]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]| ENUMERATION_FIELDS|
           OPERATING_EFFECTIVENESS (ENUMERATION)|[CN_DESIGN_EFFECTIVENES]
     ```
2. Cree una página de solicitudes.
3. Añada un **Solicitud de valor** con opciones estáticas a la página de solicitud. Para obtener detalles sobre cómo añadir una solicitud de valor con opciones estáticas, consulte [Adición de una solicitud de opciones estáticas](#adición-de-una-solicitud-de-opciones-estáticas). Ponga el nombre a la solicitud **Orden de clasificación**.
4. En el recuadro **Propiedades** de **Solicitud de valor**, añada los valores siguientes en el recuadro **Opciones estáticas** :

   - **En el campo Utilizar , especifique esto ...**

     **En el campo Mostrar , especifique esto ...**

   - **1**

     Eficacia operativa

   - **2**

     Eficacia del diseño
5. Utilizando **Explorador de consultas** , seleccione la consulta que va a editar.
6. En el modelo tabular, realice los siguientes pasos.

   1. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) y arrastre un objeto **Elemento de datos** al panel **Elementos de datos** .
   2. En el panel **Definición de expresión** , especifique las expresiones siguientes:

      caso?¿Orden de clasificación?

      when 1 then [CN_OPERATING_EFFECTIVENES]

      when 2 then [CN_DESIGN_EFFECTIVENESS]

      final

      Donde:

      El orden de clasificación es el nombre del parámetro creado en el paso 3 de este ejemplo.

      Los valores 1 y 2 de la expresión anterior son los valores de **Uso** que se han creado en el paso 4. Si los valores son diferentes de los que se muestran aquí, debe cambiar la expresión.
7. En el panel **Propiedades** del elemento de datos, realice los pasos siguientes.

   1. Cambie el nombre del elemento de datos a **Orden de clasificación**.
   2. Cambie la propiedad **Función de agregación** a **Ninguno**.
   3. Cambie la propiedad **Función de agregación de resumen** a **Ninguno**.
8. Siguiendo las instrucciones en [Utilización de ordenación avanzada](#uso-de-la-ordenación-avanzada), añada el elemento de datos **Orden de clasificación** a la **Lista de clasificación de detalles**.
9. Ejecute el informe. Dependiendo de la selección del usuario en la solicitud, se ordenará el informe.

### Filtrado de datos

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-filtering)

Puede utilizar un filtro de informes para centrarse en un informe y minimizar el tipo de proceso excluyendo los datos no deseados.

#### Uso de mapas de parámetros para filtrado

`Guía del creador de informes › Trabajar con datos relacionales › Filtrado de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-using-parameter-maps-filtering)

Para visualizar, por ejemplo, en un informe sólo los objetos de control que tienen un valor de efectividad operativa de `Effective`, aplicaría un filtro en el campo de serie enumerada `Operating Effectiveness` .

El tipo de datos del campo `Operating Effectiveness` es un tipo de datos enumerado (enum). A medida que la aplicación IBM OpenPages® está totalmente internacionalizada, los valores enumerados se traducen al entorno local del usuario que ha iniciado la sesión en la aplicación.

Si tuviera que utilizar el valor de serie de `Effective` en una expresión de filtro, como por ejemplo:

```
[CN_OPERATING_EFFECTIVENES] = 'Effective'
```

El valor enumerado funcionará solo para la configuración regional de inglés EE.UU, no funcionará para otras configuraciones regionales. Por ejemplo, si un usuario cuya configuración regional está en registros japoneses, los valores enumerados se traducirán al japonés y, por lo tanto, la definición de filtro anterior no funcionará.

Para que este filtro funcione en cualquier configuración regional, debe utilizar el ID del valor de serie enumerada en la expresión de filtro en lugar del mismo valor de serie enumerada.

El asunto de consulta para el objeto correspondiente tiene dos elementos de consulta, uno que contiene la información de ID para el valor de serie enumerada y el otro que contiene el valor de serie enumerada real.

Por ejemplo, en el modelo de entorno generado, el asunto de consulta SOXCONTROL contiene dos campos:[CN_OPERATING_EFFECTIVENES_ID] y [CN_OPERATING_EFFECTIVENES].

Para filtrar por el valor de serie enumerada `Effective` para que funcione en todos los entornos locales, tendría que modificar la expresión anterior para utilizar el ID del valor de serie enumerada, tal como se muestra en el ejemplo siguiente:

```
[CN_OPERATING_EFFECTIVENES_ID] = 45
```

donde 45 es el ID del valor de serie enumerada `Effective` para el campo de objeto `Operating Effectiveness` en este conjunto de datos concreto. Sin embargo, el ID de la serie enumerada pueden cambiar de un despliegue a otro. En la práctica, el ID se debe obtener a través de una página de solicitudes o de un mapa de parámetros.

Los mapas de parámetros se crean para todos los campos enumerados de valor único o multivalor.

Puede utilizar mapas de parámetros en la expresión de filtro en lugar de buscar los ID de los valores de serie enumerada. Por ejemplo:

```
[CN_OPERATING_EFFECTIVENES_ID] + 0 = 
#$SOXCONTROL_OPERATING_EFFECTIVENES_DEFINITION_MAP{"Effective"}#
```

Cuando se ejecuta el informe, la definición del mapa de parámetros se sustituye por el ID real del valor `Effective`.

El convenio de denominación para los mapas de parámetros se muestra en el ejemplo siguiente:

```
#$<Object Name>_<Field Name>_DEFINITION_MAP{"Value"}#
```

Donde `<Object Name>` es el nombre del objeto y `<Field Name>` es el nombre del campo enumerado.

#### Filtrado del ID de periodo de elaboración de informes

`Guía del creador de informes › Trabajar con datos relacionales › Filtrado de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-filtering-reporting-period-id)

Todos los informes deben filtrarse por el ID de periodo de elaboración de informes (a través del uso de una solicitud o un filtro) a menos que el usuario desee informar a través de todos los periodos de elaboración de informes.

Puede, por ejemplo, solicitar al usuario explícitamente un periodo de elaboración de informes específico y filtrar por la selección. O, puede filtrar por el valor ID de periodo de elaboración de informes -1 si el informe solo está disponible para el periodo de elaboración de informes actual.

> **Sugerencia:** Al combinar el filtrado en el ID de periodo de creación de informes con el filtrado en la entidad, debe utilizar GEN_REPORTING_PERIOD_ID como elemento de filtrado para el ID de periodo de creación de informes.

#### Filtrado de una enumeración

`Guía del creador de informes › Trabajar con datos relacionales › Filtrado de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-filtering-enumeration)

Hay dos tipos de variables enumeradas, de valor único o multivalor. Para filtrar utilizando enumeraciones, el operador del filtro debe cambiar para dar cabida al tipo de solicitud que se está utilizando.

**Tabla 1. Operadores de filtro**

| Tipo de enumeración | Tipo de solicitud | Operador de filtro | Comentario |
| --- | --- | --- | --- |
| Valor único | Selección única | = |  |
| Valor único | Selección múltiple | en |  |
| Multivalor | Selección única | contiene | Devuelve cualquier registro que contiene el valor de la solicitud. |
| Multivalor | Selección múltiple | * en | Devuelve cualquier registro que contiene cualquiera de los valores seleccionados de la solicitud. |

Para filtrar una serie enumerada multivalor en una solicitud de selección múltiple, debe utilizar la siguiente sintaxis para el filtro:

```
 [DEFAULT_REL].[RI_DOMAIN].[RI_DOMAIN] in ?Domain?
```

Este filtro está utilizando el elemento de datos \<nombre de campo_objeto> de la definición de serie enumerada de dominio (como ejemplo) para compararlo en la solicitud. Este campo devuelve registros individuales para cada uno de los dominios, que el usuario puede haber seleccionado en la aplicación, para compararlo con el valor de solicitud que también puede ser de selecciones múltiples.

Además, debe asegurarse de que la propiedad **Agrupación automática y resumen** del asunto de consulta que contiene este filtro está establecida en **Sí**.

### Agrupación de datos

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-grouping)

Puede eliminar valores duplicados en un informe agrupando elementos de consulta. Por ejemplo, si un informe contiene varios controles para una entidad de negocios y riesgo concretos, puede agrupar las columnas de la entidad de negocios y riesgo así solo una instancia de la entidad de negocios y el riesgo se visualiza en la lista para cada control.

#### Agrupación de datos en un informe de lista

`Guía del creador de informes › Trabajar con datos relacionales › Agrupación de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-grouping-in-list-report)

Puede agrupar datos en un informe de lista. El informe de ejemplo utiliza los elementos de consulta de control, entidad de negocios y riesgo y, después, agrupa las columnas de entidad de negocios y riesgo para eliminar datos duplicados.

> **Nota:** Agrupar por ID de recurso en contraposición a Nombre porque los ID de recurso son exclusivos en todo el sistema pero los nombres no.

##### Procedimiento

1. Cree un nuevo informe de lista con los siguientes elementos de consulta desde el espacio de nombres relacional situado en el panel **Elementos de datos** de la consulta:

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
         [SOXBUSENTITY_GPC]|ID_FIELDS|[CEN_ENTITY_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
          [SOXBUSENTITY_GPC]|[CEN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXRISK]|
          ID_FIELDS|[RI_RISK_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXRISK]|[RI_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|
          ID_FIELDS| [CN_CONTROL_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_NAME00]
     ```
2. Agrupe los datos para las siguientes columnas:

   1. Seleccione la columna `[CEN_ENTITY_ID]` .
   2. Pulse el icono Grupo ![Icono de grupo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-group_rag.jpg). El icono de grupo se visualizará en la columna que acaba de seleccionar.
   3. Seleccione la columna `[RI_RISK_ID]` y `[CN_CONTROL_ID]` y repita el paso b.
3. Corte los siguientes elementos de consulta de la lista para ocultar el identificador de objeto y que no aparezca en la página de informe:

   ```
   [CEN_ENTITY_ID]
   [RI_RISK_ID]
   [CN_CONTROL_ID]
   ```

   > **Importante:** Al cortar una columna de un informe, no se mostrará en el informe, pero seguirá estando presente en la consulta subyacente. Cuando suprima una columna de un informe, se suprimirá del informe y la consulta subyacente si no hay otros objetos en el informe que hace referencia a ese elemento de consulta.
4. Seleccione la columna `[CEN_NAME00]` y en el **Panel de propiedades**, en **Datos**, seleccione **Agrupar espacio** y establézcalo en `[CEN_ENTITY_ID]`.
5. Seleccione la columna `[RI_NAME00]` y en el **Panel de propiedades**, en **Datos**, seleccione **Agrupar espacio** y establézcalo en `[RI_RISK_ID]`.
6. Seleccione la columna `[CN_NAME00]` y en el **Panel de propiedades**, en **Datos**, seleccione **Agrupar espacio** y establézcalo en `[CN_CONTROL_ID]`.
7. Seleccione la columna `[CN_DESCRIPTION]` y en el **Panel de propiedades**, en **Datos**, seleccione **Agrupar espacio** y establézcalo en `[CN_CONTROL_ID]`.
8. Ejecute el informe.

#### Creación de una cabecera de grupo de lista

`Guía del creador de informes › Trabajar con datos relacionales › Agrupación de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-creating-list-group-header)

Puede utilizar el nombre de un objeto (como el nombre de una entidad) como cabecera de grupo de un informe de lista nuevo.

##### Acerca de esta tarea

El informe de ejemplo utiliza los elementos de consulta de control, riesgo y entidad de negocios. Agrupa las columnas de entidad de negocios y riesgo para eliminar datos duplicados y mostrar el nombre de la entidad del asunto de consulta [CEN_NAME00] como cabecera en el informe de ejemplo.

##### Procedimiento

1. Siga los pasos 1-3 tal como se describe en [Agrupación de datos en un informe de lista](#agrupación-de-datos-en-un-informe-de-lista) para crear un informe de lista con agrupaciones.
2. Pulse **Estructura** > **Cabeceras y pies de página** > **Cabeceras de lista y pies de página** para abrir el recuadro **Cabeceras de lista y pies de página** y complete los pasos siguientes.

   1. Seleccione `CEN_NAME00(header)`.
   2. Pulse **Aceptar**.
3. En la página del informe, corte el elemento de consulta `[CEN_NAME00]` de la lista para ocultar que el identificador del objeto aparece como una columna de lista en el informe.
4. Ejecute el informe.

#### Establecimiento de la extensión de nivel para una columna

`Guía del creador de informes › Trabajar con datos relacionales › Agrupación de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-setting-level-span-column)

Cuando las columnas están agrupadas, puede elegir con qué frecuencia mostrar los valores de columna utilizando la expansión de nivel. A diferencia de la agrupación, la expansión de nivel no cambiará la consulta subyacente.

##### Procedimiento

1. Cree un nuevo informe de lista con los siguientes elementos de consulta del espacio de nombres relacional:

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXRISK]|ID_FIELDS|[RI_RISK_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXRISK]|[RI_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXRISK]| ENUMERATION_FIELDS|
        INHERENT_IMPACT (ENUMERATION)| [RI_INHERENT_IMPACT]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXRISK]| ENUMERATION_FIELDS|
        INHERENT_LIKELIHOOD(ENUMERATION)| [RI_INHERENT_LIKELIHOOD]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| 
        [CN_CONTROL_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
        OPERATING_EFFECTIVENES(ENUMERATION)|[CN_OPERATING_EFFECTIVENES]
     ```
2. Para editar la página de informes, realice los siguientes pasos:

   1. Corte los siguientes elementos de consulta de la lista para ocultar el identificador de objeto y que no aparezca en la página de informe:

      ```
      [RI_RISK_ID]
      [CN_CONTROL_ID]
      ```
   2. Agrupar los datos en la columna `[RI_NAME00]` .
3. Ejecute el informe.

   `[RI_NAME00]` no se repite para todos los controles. Sin embargo, `[RI_INHERENT_IMPACT]` y `[RI_INHERENT_LIKELIHOOD]`, que son las propiedades del objeto de riesgo, se repiten para cada objeto de control asociado en el informe generado.

   Para que no se repitan los campos de riesgo adicionales, complete los siguientes pasos:
4. Para ampliar el nivel de los elementos de consulta `[RI_INHERENT_IMPACT]`y `[RI_INHERENT_LIKELIHOOD]` cuando `[RI_NAME00]` cambia, realice los pasos siguientes.

   1. Seleccione la columna `[RI_INHERENT_IMPACT]` en el informe.
   2. En el recuadro **Propiedades** bajo **Datos** para la columna seleccionada, pulse el botón **Agrupar espacio** y seleccione la columna `[RI_NAME00]` .
   3. Repita los pasos a y b para la columna `[RI_INHERENT_LIKELIHOOD]` .

##### Resultados

Los campos de riesgo adicionales ahora expanden el campo de nombre de riesgo.

### Agregación de datos

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-aggregating)

Las agregaciones se utilizan para agrupar y resumir datos numéricos. Las técnicas descritas aquí se utilizan no sólo para generar los resultados deseados, sino también para hacer que CommandCentergenere SQL eficiente.

#### Acerca de esta tarea

Siga este procedimiento para contar el número de controles `Effective`, `Ineffective`y `Not Determined` que están directamente presentes bajo una entidad y, a continuación, totalizar el porcentaje de controles `Ineffective` para dicha entidad.

#### Procedimiento

1. Cree un nuevo informe de lista.
2. Para crear una consulta hijo, realice los siguientes pasos.

   1. En **Explorador de consultas**, abra la consulta.
   2. En el panel **Propiedades** en **Varios**, establezca el nombre en **listMain**.
   3. Vuelva a **Explorador de consultas** y seleccione la carpeta de nivel superior **Consultas**.
   4. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg).
   5. Arrastre un objeto **Query** junto a la consulta **listMain** .
   6. Seleccione el nuevo objeto de consulta.
   7. En el panel **Propiedades** bajo **Varios**, establezca **Nombre** en **listMain1**.
3. Para añadir otro objeto de consulta hijo al objeto de consulta que ha creado en el paso anterior, realice los siguientes pasos.

   1. Arrastre un objeto **Consulta** junto a la consulta **listMain1** .
   2. Seleccione el nuevo objeto de consulta.
   3. En el panel **Propiedades** bajo **Varios**, establezca **Nombre** en **listMain2**.
4. Para añadir elementos de consulta a la consulta **listMain2** que ha creado en el paso anterior, realice los pasos siguientes.

   1. Seleccione la consulta **listMain2** para abrirla.
   2. Pulse la **Fuente** pestaña ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg) en el panel **Objetos insertables** .
   3. Arrastre los siguientes elementos de consulta al recuadro **Elementos de datos** :

      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
            [SOXBUSENTITY_GPC]|[CEN_NAME00]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
            [SOXBUSENTITY_GPC]|ID_FIELDS|[CEN_ENTITY_ID]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| 
            [CN_CONTROL_ID]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
            OPERATING_EFFECTIVENESS (ENUMERATION)| [CN_OPERATING_EFFECTIVENES_ID]
        ```
5. Para añadir un elemento de datos al objeto de consulta, complete los pasos siguientes.

   1. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg).
   2. Arrastre un objeto **Elemento de datos** al recuadro **Elementos de datos** de la consulta.
   3. En el panel **Definición de expresión** del elemento de datos, especifique la expresión siguiente:

      ```
      if([CN_OPERATING_EFFECTIVENES_ID] + 0 = #$SOXCONTROL_OPERATING_EFFECTIVENES_DEFINITION_MAP{"Effective"}#)
        then(1)
        else (0)
      ```
   4. Pulse el icono **Validar** ![Icono Validar expresión](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) para validar la expresión y, a continuación, pulse **Aceptar**.
6. En el panel **Propiedades** del elemento de datos, realice los pasos siguientes.

   1. Cambie la propiedad **Nombre** del elemento de datos a `Effective`.
   2. Cambie la propiedad **Función de agregación** a **Ninguno**.
7. Repita los pasos 5 y 6 para crear dos elementos de datos más: uno para `Ineffective` y otro para `Not Determined`. Asegúrese de cambiar el valor **clave** del mapa de parámetros para cada nuevo elemento de datos.
8. En el menú **Ejecutar** , pulse **Ver datos tabulares** para ver los datos de **listMain2** .

   El informe se ejecuta solo a nivel del objeto **listaPrincipal2**. Las columnas **Efectivo**, **No efectivo** y **No determinado** se llenan con 1 y 0 dependiendo de la eficacia operativa del control.
9. Para agregar los datos en el objeto **listMain1** contando el número total de controles basándose en su eficacia operativa para cada entidad, realice los pasos siguientes.

   1. En **Explorador de consultas**, pulse la consulta **listMain1** .
   2. Pulse la pestaña **Origen** y arrastre y suelte los elementos de consulta `[CEN_ENTITY_ID]` y `[CEN_NAME00]` en el recuadro **Elementos de datos** de **listMain2**.
   3. Cambie la propiedad **Función de agregación** para cada elemento de datos a **Ninguno**.
   4. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) y, a continuación, arrastre un objeto **Elemento de datos** al recuadro **Elementos de datos** del modelo tabular.
   5. En el panel **Definición de expresión** , especifique la expresión siguiente:

      ```
      total([listMain2].[Effective] for [listMain2].[CEN_ENTITY_ID])
      ```
10. En el panel **Propiedades** del elemento de datos recién creado, realice los pasos siguientes.

    1. Cambie la propiedad **Nombre** del elemento de datos a `Effective Count`.
    2. Cambie la propiedad **Función de agregación** a **Ninguno**.
11. Repita los pasos 9 y 10 para crear dos elementos de datos más para los controles de recuento: uno para `Ineffective` y otro para `Not Determined`.
12. Para calcular el porcentaje de controles no efectivos, realice los siguientes pasos.

    1. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg).
    2. Arrastre un **Elemento de datos** al recuadro **Elementos de datos** .
13. En el panel **Propiedades** del elemento de datos recién creado, realice los pasos siguientes.

    1. Cambie la propiedad **Nombre** a `Percent Ineffective`.
    2. Cambie la propiedad **Función de agregación** a **Ninguno**.
    3. Cambie la propiedad **Función de agregación de resumen** a **Ninguno**.
    4. En el panel **Definición de expresión** , cree la expresión siguiente:

       ```
       [Ineffective Count] / ([Effective Count] +
       [Ineffective Count] + [Not Determined Count]))
       ```
14. En el menú **Ejecutar** , pulse **Ver datos tabulares** para ver los datos de nivel tabular del objeto **listMain1** .
15. Para rellenar la consulta **listMain** , realice los pasos siguientes.

    1. En **Explorador de consultas** , seleccione la consulta **listMain** .
    2. Desde la pestaña **Origen** ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg), arrastre los siguientes elementos de consulta al panel **Elementos de datos** de la consulta:

       - `[CEN_NAME00]`
       - `[CEN_ENTITY_ID]`
       - `[Effective Count]`
       - `[Ineffective Count]`
       - `[Not Determined Count]`
       - `[Percent Ineffective]`
16. En el panel **Propiedades** de cada uno de los elementos de datos anteriores, cambie la propiedad **Función de agregación** a **Ninguno**.
17. Para rellenar la página de informe con los elementos de datos, realice los siguientes pasos.

    1. En **Explorador de páginas**, pulse la página de informe para abrirla.
    2. En el panel **Objetos insertables**, seleccione la pestaña **Elementos de consulta** ![Icono de elemento de consulta](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-query_items_tab.jpg) y, a continuación, arrastre y suelte los siguientes elementos de consulta en el objeto de lista de **listMain** :

       - [CEN_NAME00]
       - [CEN_ENTITY_ID]
       - [Effective Count]
       - [Ineffective Count]
       - [Undetermined Count]
       - [Percent Ineffective]
    3. Seleccione la columna `[Percent Ineffective]` en el objeto de lista.
    4. Efectúe una doble pulsación en el recuadro **Formato de datos** del panel **Propiedades** .
    5. Establezca **Tipo de formato** en **Porcentaje**.
    6. Establezca la propiedad **Símbolo de porcentaje** en el símbolo de porcentaje (%).
    7. Pulse **Aceptar**.
18. Ejecute el informe.

#### Resultados

El informe parece tener filas duplicadas para varias entidades de negocios. En función del campo [CEN_ENTITY_ID], en realidad hay entidades vinculadas a diferentes nodos finales de la jerarquía de entidad de negocios.

Una forma mejor de visualizar el nombre de la fila sería utilizar la variable vía_acceso_completa en lugar del nombre hijo. La variable vía_acceso_completa muestra la vía de acceso completa de la entidad de negocios al nodo final con todos los nodos intermedios.

### Uso del formateo condicional

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-using-conditional-formatting)

Las secciones siguientes describen cómo utilizar el formateo condicional.

#### Uso del formateo condicional para entradas de sangría

`Guía del creador de informes › Trabajar con datos relacionales › Uso del formateo condicional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=formatting-using-conditional-indent-entries)

Siga este procedimiento para sangrar nombres de entidad dependiendo del nivel.

##### Procedimiento

1. Cree un nuevo informe de lista.
2. En **Explorador de consultas**, abra la consulta.
3. En el panel **Propiedades** en **Varios**, establezca el nombre en **listMain**.
4. Añada los siguientes elementos de consulta:

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
         [SOXBUSENTITY_GPC]|[CEN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
         [SOXBUSENTITY_GPC]|ID_FIELDS|[CEN_ENTITY_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
         [SOXBUSENTITY_GPC]|[CEN_FULL_PATH]
     ```
5. Corte los siguientes elementos de consulta del informe:

   - `[CEN_ENTITY_ID]`
   - `[CEN_FULL_PATH]`
6. Para establecer el orden de clasificación en el elemento de datos `[CEN_FULL_PATH]` , realice los pasos siguientes.

   1. Seleccione cualquier elemento del objeto de lista.
   2. Pulse el icono de ordenación ![Icono de ordenación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-sort.jpg)en la barra de herramientas y, a continuación, pulse **Clasificación avanzada**.
   3. En el diálogo **Agrupación y ordenación** , arrastre y suelte `[CEN_FULL_PATH]` bajo la carpeta **Lista de clasificación de detalles** .
   4. Pulse **Aceptar**.
7. Seleccione la consulta **listMain** en el **Explorador de consultas**.
8. Pulse la pestaña ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) **Caja de herramientas** y arrastre un **Elemento de datos** al panel **Elementos de datos** .

   > **Nota:** Si tiene una base de datos IBM® Db2® , debe sustituir la función Oracle `INSTR` en la siguiente expresión de ejemplo por la función Db2 correspondiente.

   En el panel **Definición de expresión**, entre la siguiente expresión:

   ```
   case INSTR([CEN_FULL_PATH], '/', 1, 2)
      when 0 then 1
      else
      (case INSTR([CEN_FULL_PATH], '/', 1, 3)
         when 0 then 2
         else
         (case INSTR([CEN_FULL_PATH], '/', 1, 4)
            when 0 then 3
            else
            (case INSTR([CEN_FULL_PATH], '/', 1, 5)
               when 0 then 4
               else
               (case INSTR([CEN_FULL_PATH], '/', 1, 6)
                  when 0 then 5
                  else
                  (case INSTR([CEN_FULL_PATH], '/', 1, 7)
                     when 0 then 6
                     else
                     (case INSTR([CEN_FULL_PATH], '/', 1, 8)
                        when 0 then 7
                     end)
                  end)
               end)
            end)
         end)
      end)
   End
   ```
9. En el panel **Propiedades** , establezca la propiedad **Nombre** del nuevo elemento de datos en `Level`.
10. Para hacer que el elemento de datos **Nivel** sea una propiedad de la lista, realice los pasos siguientes.

    1. Seleccione el objeto **Lista** en la página de informe principal.
    2. En el panel **Propiedades** bajo **Datos** efectúe una doble pulsación en **Propiedades**.
    3. Seleccione `[Level]`.
    4. Pulse **Aceptar**
11. Abra el **Explorador de condiciones** y pulse **Variables**.
12. En el diálogo **Variables** , realice los pasos siguientes.

    1. Arrastre y suelte un objeto **Variable de cadena** en el panel **Variables** .
    2. Arrastre el elemento de consulta **Nivel** al panel **Definición de expresión** .
    3. Pulse **Aceptar**.
13. En el panel **Propiedades** bajo **Varios**, establezca la propiedad **Nombre** en **Sangrar variable**.
14. En la **Panel de valores**, realice los pasos siguientes.

    1. Pulse el icono ![Icono Añadir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-add_new.jpg) **Añadir** y especifique **1** en el recuadro de diálogo.
    2. Repita el paso a para todos los niveles 2-7.
15. Seleccione la página de informe principal en **Explorador de páginas**.
16. En la página del informe, seleccione `[CEN_NAME00]` y, en el recuadro **Propiedades** , realice los pasos siguientes.

    1. Pulse la propiedad **Variable de estilo** y seleccione la variable **Sangrar variable**.
    2. Pulse **Aceptar**.
17. Para aumentar la sangría de niveles diferentes de entidades, realice los pasos siguientes.

    1. Seleccione la columna `[CEN_NAME00]` .
    2. Pase el puntero del ratón sobre la barra **Explorador condicional** .
    3. Seleccione el valor de variable **2** que está presente bajo la variable **Sangrar variable**. La barra del explorador se volverá verde para indicar que está estableciendo el valor de una variable.
    4. En el panel **Propiedades** bajo **Cuadro**, pulse la propiedad **Relleno** y especifique el valor de 50 px para la celda de relleno de la izquierda y pulse **Correcto**.
    5. Repita los pasos c-d y seleccione distintos valores de **Sangrar variable** y especifique valores crecientes para el relleno izquierdo.
    6. En el Explorador de condiciones, pulse **(Sin variable)**.
18. Ejecute el informe.

#### Resaltar datos condicionalmente

`Guía del creador de informes › Trabajar con datos relacionales › Uso del formateo condicional` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=formatting-highlighting-data-conditionally)

Puede resaltar condicionalmente algunas filas de datos cuando esos datos cumplen ciertos criterios.

##### Acerca de esta tarea

El ejemplo siguiente se basa en el informe que se ha creado en [Agregación de datos](#agregación-de-datos). Este ejemplo muestra cómo resaltar condicionalmente la columna `[Percent Ineffective]`.

En este ejemplo, el color de fondo de una celda cambia en base al porcentaje de un control no efectivo. Si el porcentaje de los controles que son efectivos es mayor de 50, el color de fondo de la celda será rojo; si el porcentaje está entre 20 y 50, entonces el color de fondo de la celda será amarillo; si es menor de 20, el color de fondo de la celda será verde.

##### Procedimiento

1. Abra el informe que ha creado en [Agregando datos](#agregación-de-datos).
2. Abra el **Explorador de condiciones** y pulse **Variables**.
3. En el diálogo **Variables** , realice los pasos siguientes.

   1. Arrastre y suelte un objeto **Variable de cadena** en el panel **Variables** .
   2. En el panel **Definición de expresión** , especifique la expresión siguiente:

      ```
      if([Percent Ineffective] >= 0.5)
      then (3)
      else if ( [Percent Ineffective] < 0.5 and [Percent Ineffective] > 0.2)
      then (2)
      else if ( [Percent Ineffective] <= 0.2)
      then (1)
      else (0)
      ```
   3. Pulse **Aceptar**.
4. En el panel **Propiedades** bajo **Varios**, establezca la propiedad **Nombre** en **Resaltar variable**.
5. En el panel **Valores**, pulse el icono ![Icono Añadir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-add_new.jpg) **Añadir** y especifique **3** en el recuadro de diálogo. Repita los pasos para **2**, **1**y **0**.
6. Seleccione la página de informe principal en **Explorador de páginas**.
7. En la página del informe, seleccione `[Percent Ineffective]` y, en el recuadro **Propiedades** , realice los pasos siguientes.

   1. Pulse la propiedad **Variable de estilo** y seleccione la variable **Resaltar variable**.
   2. Pulse **Aceptar**.
8. Para definir los colores de los diferentes valores, realice los siguientes pasos.

   1. Seleccione la columna `[Percent Ineffective]` .
   2. Pase el puntero del ratón sobre la barra **Explorador condicional** .
   3. Seleccione el valor de variable **1** que está presente bajo la variable **Sangrar variable**. La barra del explorador se vuelve verde para indicar que está estableciendo el valor de una variable.
   4. En el panel **Propiedades** bajo **Color y fondo**, establezca la propiedad **Color de fondo** en **Verde**.
   5. Repita los pasos c-d para cada valor de variable **2** y **3**y, a continuación, establezca la propiedad **Color de fondo** en **Amarillo** y **Rojo**, respectivamente.
   6. En el Explorador de condiciones, pulse **(Sin variable)**.
9. Ejecute el informe.

##### Resultados

En el informe, los valores menores del 20% están resaltados en verde y los valores mayores del 20% y menores del 50% están resaltados en amarillo.

### Colores del gráfico de barras

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-bar-chart-colors)

Cuando los datos se representan en gráficos de barras, los autores de informe deben intentar controlar los colores para la consistencia para que los colores particulares signifiquen lo mismo en un informe determinado cada vez que los usuarios ejecuten ese informe.

Esta sección contrasta dos técnicas que puede utilizar para crear informes de gráfico de barras. Para ilustrar los colores del gráfico de barras de cada método, se utiliza el campo **Eficacia operativa** del objeto de control con todos o algunos de sus valores correspondientes (**Efectivo**, **No efectivo**, **No determinado**) de los ejemplos que siguen.

#### Método 1

Este método muestra automáticamente valores que se añaden al campo **Eficacia operativa** en el esquema (valores que no están correlacionados). Sin embargo, los colores del los informes para estos valores se muestran de manera desigual.

Por ejemplo, hay dos entidades de negocios: BE1 y BE2. La siguiente lista muestra el campo **Eficacia operativa** para estas entidades de negocios.

- **BE1**

  Efectivo, No efectivo, No determinado

- **BE2**

  No efectivo, No determinado

Cuando un usuario ejecuta el informe para cada entidad de negocios, los colores de barra que derivan para los valores no son uniformes:

- **BE1**

  Efectivo= negro, No efectivo= rosa, No determinado = púrpura

- **BE2**

  No efectivo = negro, No determinado = rosa

Para obtener más información, consulte [Visualización de variación de color de barra con valores visualizados automáticamente](#visualización-de-la-variación-de-color-de-barra-con-valores-visualizados-automáticamente).

#### Método 2

Este método utiliza una técnica de correlación de parámetros y requiere que se modifique el informe del gráfico de barras cuando se añaden nuevos valores, por ejemplo, al campo **Eficacia operativa** del esquema. Sin embargo, los colores se visualizan de forma constante en los informes para los valores que se están correlacionando.

Utilizando las mismas entidades de negocios con los mismos valores en la **Eficacia operativa** que en el ejemplo del Método 1, los resultados utilizando el Método 2 son diferentes.

Cuando un usuario ejecuta el informe para cada una de las entidades de negocios, los colores de barra que resultan para los valores son uniformes:

- **BE1**

  Efectivo= negro, No efectivo= rosa, No determinado = púrpura

- **BE2**

  No efectivo= rosa, No determinado = púrpura

Para obtener más información, consulte [Visualización de la coherencia de color de barra con modificación de informe para nuevos valores](#visualización-de-la-consistencia-del-color-de-barra-con-modificación-de-informe-para-los-nuevos-valores).

#### Visualización de la variación de color de barra con valores visualizados automáticamente

`Guía del creador de informes › Trabajar con datos relacionales › Colores del gráfico de barras` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=colors-displaying-bar-color-variation-automatically-displayed-values)

Cuando se muestran valores automáticamente, puede visualizar las variaciones de color de la barra.

##### Procedimiento

1. Para crear un informar de gráfico, realice los siguientes pasos.

   1. Seleccione la agrupación de gráficos **Columna** .
   2. Seleccione el tipo de gráfico **Columna** .
   3. Pulse **Aceptar**.
2. Arrastre y suelte los siguientes elementos de consulta en varias secciones del gráfico:

   - `Categories (x-axis)`

     ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
     [SOXBUSENTITY_GPC]|[CEN_NAME00]
     ```
   - `Measures (y-axis)`

     ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| 
     [CN_CONTROL_ID]
     ```
   - `Series`

     ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
     OPERATING_EFFECTIVENES (ENUMERATION)|[CN_OPERATING_EFFECTIVENES] 
     ```
3. En el **Explorador de consultas**, seleccione la consulta y, en el panel **Propiedades** bajo **Varios**, establezca el nombre en **chartMain**.
4. En el panel **Elementos de datos** , seleccione `[CN_CONTROL_ID]` y realice los pasos siguientes.

   1. En el panel **Propiedades** bajo **Elemento de datos**, cambie el valor de la propiedad **Función de agregación** a **Recuento diferenciado**.
   2. En el panel **Propiedades** bajo **Elemento de datos**, cambie el valor de la propiedad **Función de agregación de resumen** a **Automático**.
5. Desde el **Explorador de páginas**, crear una **Página de solicitud** y crear una solicitud **Entidad de negocios** tal como se muestra en [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios).
6. Efectúe una doble pulsación en el título y establezca el valor en **Eficacia operativa**.
7. Abra la **Títulos de eje**y realice los pasos siguientes.

   1. Seleccione el título del eje x y en el panel **Propiedades** .
   2. En **General** , establezca la propiedad **Título predeterminado** en **No**.
   3. Efectúe una doble pulsación en el título del eje y establezca el valor en **Entidad de negocios**.
   4. Repita los pasos a-c para el eje y y establezca el valor en **Recuento de control**.
8. Seleccione la **(Título de leyenda predeterminado)**y realice los pasos siguientes.

   1. En el panel **Propiedades** bajo **General** , establezca la propiedad **Título predeterminado** en **No**.
   2. Efectúe una doble pulsación en el título de la leyenda y establezca el valor en **Eficacia operativa de control**.
9. Ejecute el informe.

#### Visualización de la consistencia del color de barra con modificación de informe para los nuevos valores

`Guía del creador de informes › Trabajar con datos relacionales › Colores del gráfico de barras` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=bcc-displaying-bar-color-consistency-report-modification-new-values)

Cuando se modifica un informe con valores nuevos, puede mostrar el color de barra de manera consistente.

##### Procedimiento

1. Cree un informe de gráfico y complete los pasos siguientes.

   1. Seleccione la agrupación de gráficos **Columna** .
   2. Seleccione el tipo de gráfico **Columna** .
2. Para crear una consulta hijo, realice los siguientes pasos.

   1. En **Explorador de consultas**, seleccione consultas.
   2. Seleccione **Query1** y en el panel **Propiedades** bajo **Varios**, establezca el nombre en **listMain**.
   3. Pulse la pestaña ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) **Caja de herramientas** .
   4. Arrastre un objeto **Query** a la consulta **graphMain** .
   5. Seleccione el nuevo objeto de consulta.
   6. En el panel **Propiedades** bajo **Varios**, establezca **Nombre** en **graphMain1**.
3. Para añadir elementos de consulta a la consulta **graphMain1** que ha creado en el paso anterior, realice los pasos siguientes.

   1. Seleccione la consulta **graphMain1** para abrirla.
   2. Pulse la pestaña ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg) **Origen** en el panel **Objetos insertables** .
   3. Arrastre los siguientes elementos de consulta al recuadro **Elementos de datos** :

      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
           [SOXBUSENTITY_GPC]|[CEN_NAME00]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
           [SOXBUSENTITY_GPC]|ID_FIELDS| [CEN_ENTITY_ID]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| 
           [CN_CONTROL_ID]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
           OPERATING_EFFECTIVENES (ENUMERATION)| [CN_OPERATING_EFFECTIVENES_ID]
        ```
4. Complete los pasos siguientes.

   1. Pulse la pestaña ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) **Caja de herramientas** .
   2. Arrastre un objeto **Elemento de datos** al recuadro **Elementos de datos** de la consulta.
   3. En el panel **Definición de expresión** del elemento de datos, especifique la expresión siguiente:

      ```
      if([CN_OPERATING_EFFECTIVENES_ID] = #$SOXCONTROL_OPERATING_EFFECTIVENES_DEFINITION_MAP{"Effective"}#)
         then(1)
         else (0)
      ```
   4. ![Icono Validar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg)Valide la expresión y, a continuación, pulse **Aceptar**.
5. En el panel **Propiedades** del elemento de datos, realice los pasos siguientes.

   1. Cambie la propiedad **Nombre** del elemento de datos a `Effective`.
   2. Cambie la propiedad **Función de agregación** a **Ninguno**.
6. Repita los pasos 5 y 6 para crear dos elementos de datos más: uno para `Ineffective` y otro para `Not Determined`. Asegúrese de cambiar el valor **clave** del mapa de parámetros para cada nuevo elemento de datos.
7. En el menú **Ejecutar** , pulse **Ver datos tabulares** para ver los datos de **graphMain1** .

   El informe se ejecuta solo a nivel del objeto **gráficoPrincipal1**. Tenga en cuenta que las columnas **Efectivo**, **No efectivo** y **No determinado** se llenan con 1 y 0 dependiendo de la eficacia operativa del control.
8. Para agregar los datos en el objeto **graphMain1** contando el número total de controles basándose en su eficacia operativa para cada entidad, realice los pasos siguientes.

   1. En el **Explorador de consultas**, pulse la consulta **graphMain** .
   2. Arrastre y suelte los elementos de consulta `[CEN_ENTITY_ID]` y `[CEN_NAME00]` en el recuadro **Elementos de datos** de **graphMain**.
   3. Cambie la propiedad **Función de agregación** para cada elemento de datos a **Ninguno**.
   4. Arrastre y suelte los elementos de consulta `[Effective]`, `[Ineffective]` y [No determinado] en el recuadro **Elementos de datos** de **graphMain**.
   5. Cambie la propiedad **Función de agregación** para cada elemento de datos a **Total**.
9. Desde el **Explorador de páginas**, crear una **Página de solicitud** y crear una solicitud **Entidad de negocios** tal como se muestra en [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios).
10. Arrastre y suelte los siguientes elementos de consulta en varias secciones del gráfico:

    - `Categories (x-axis)`

      ```
      [CEN_NAME00]
      ```
    - `Measures (y-axis)`

      ```
      [Effective]
      [Ineffective]
      [Not Determined]
      ```
11. Efectúe una doble pulsación en el título y establezca el valor en **Eficacia operativa**.
12. Abra la **Títulos de eje**y realice los pasos siguientes.

    1. Seleccione el título del eje x.
    2. En el panel **Propiedades** , en **General** establezca la propiedad **Título predeterminado** en **No**.
    3. Efectúe una doble pulsación en el título del eje y establezca el valor en **Entidad de negocios**.
    4. Repita los pasos a-c para el eje y y establezca el valor en **Recuento de control**.
13. Seleccione la **(Título de leyenda predeterminado)** y realice los pasos siguientes.

    1. En el panel **Propiedades** bajo **General** , establezca la propiedad **Título predeterminado** en **No**.
    2. Efectúe una doble pulsación en el título de la leyenda y establezca el valor en **Eficacia operativa de control**.
14. Ejecute el informe.

#### Edición de colores de barra

`Guía del creador de informes › Trabajar con datos relacionales › Colores del gráfico de barras` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=colors-editing-bar)

Siga este procedimiento para establecer los colores que utilizará el gráfico.

##### Procedimiento

1. Seleccione el objeto **Gráfico de combinación** en el informe.
2. En el panel **Propiedades** bajo la categoría **Color y fondo** , pulse la propiedad **Paleta** .
3. Utilizando las flechas **Arriba** y **Abajo** , mueva las barras **Verde**, **Amarillo**y **Rojo** al principio de la paleta.
4. Pulse **Aceptar**.
5. Ejecute el informe.

### Creación de uniones

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-creating-joins)

La sección describirá cómo crear los dos tipos de uniones comunes cuando se crean informes: uniones directas donde solo obtenemos objetos secundarios que se relacionan directamente al objeto primario y uniones indirectas donde vemos todos los objetos secundarios que pueden agruparse bajo el objeto primario.

#### Creación de uniones directa

`Guía del creador de informes › Trabajar con datos relacionales › Creación de uniones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=joins-creating-direct)

Para crear una unión directa, debe crear un informe de entidad para los problemas.

##### Procedimiento

1. Cree un nuevo informe de lista.
2. En **Explorador de consultas**, seleccione las consultas.
3. Arrastre y suelte dos objetos **Consulta** adicionales en el panel derecho.
4. Asigne a las consultas los nombres listaPrinciapl, Entidad y Problema.
5. Seleccione la consulta Problemas.
6. Arrastre los siguientes elementos de consulta al recuadro **Elementos de datos** :

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS_STANDALONE|[SOXISSUE]|
        [IS_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS_STANDALONE|[SOXISSUE]| 
        [IS_DESCRIPTION]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS_STANDALONE|[SOXISSUE]| 
        PARENT_CONTEXT|SOXBUSENTITY_CHILD|[CEN_ENTITY_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS_STANDALONE|[SOXISSUE]| 
        PARENT_CONTEXT|SOXBUSENTITY_CHILD|[CEN_REPORTING_PERIOD_ID]
     ```
7. Seleccione la consulta Entity en **Explorador de consultas**.
8. Arrastre los siguientes elementos de consulta al recuadro **Elementos de datos** :

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
        [SOXBUSENTITY_GPC]|[GEN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
        [SOXBUSENTITY_GPC]|[GEN_FULL_PATH]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
        [SOXBUSENTITY_GPC]|ID_FIELDS|[CEN_ENTITY_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
        [SOXBUSENTITY_GPC]|ID_FIELDS|[CEN_REPORTING_PERIOD_ID]
     ```
9. En **Explorador de consultas**, seleccione las consultas.
10. Arrastre y suelte una **Unión** junto a la consulta listMain y, a continuación, llene la unión con las consultas Entity y Issue.
11. Haga doble clic en la unión y complete los pasos siguientes.

    1. Pulse **Nuevo enlace**.
    2. Seleccione `[CEN_REPORTING_PERIOD_ID]` en ambas columnas.
    3. Pulse **Nuevo enlace.**
    4. Seleccione `[CEN_ENTITY_ID]` en ambas columnas.
    5. Pulse **Aceptar**.
12. Seleccione la consulta listaPrincipal.
13. Arrastre y suelte los siguientes elementos de consulta desde el panel **Objetos insertables** :

    - `GEN_FULL_PATH`
    - `IS_NAME00`
    - `IS_DESCRIPTION`
14. Establezca las propiedades **Función de agregación** y **Función de agregación de resumen** en **Ninguno** para los tres elementos de datos.
15. Vaya a la página de informe principal y coloque los tres elementos de datos en la lista.
16. Ejecute el informe.

##### Resultados

Podrá ver los siguientes elementos en el informe:

- Solo se muestran los problemas que están unidos directamente a las entidades.
- En realidad, solo hay dos problemas aquí, ISS-012-01 unido a la entidad Servicios de agencia bajo EMEA y ISS-012-03 unido a la entidad Servicios de agencia bajo Asia Pac.
- Como estamos mostrando la vía de acceso completa abuelo, vemos todas las entidades que aparecen en la entidad de nivel superior de Servicios financieros globales. Esto hace que parezca que los problemas están conectados a tres ubicaciones pero no lo están.
- Si visualizamos la vía de acceso completa hijo en lugar de la vía de acceso completa abuelo, solo vemos los dos problemas conectados directamente a sus entidades.

#### Creación de uniones indirectas

`Guía del creador de informes › Trabajar con datos relacionales › Creación de uniones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=joins-creating-indirect)

Las uniones indirectas se utilizan para obtener todos los objetos secundarios que están relacionados directa o indirectamente al tipo de objeto primario.

En [Creación de uniones directas](#creación-de-uniones-directa) solo podíamos obtener problemas directamente vinculados a entidades. En esta tarea, obtendremos todos los problemas conectados directamente a entidades y cualquier otro objeto que tiene problemas que están conectados a entidades.

##### Procedimiento

1. Cree un nuevo informe de lista.
2. En **Explorador de consultas**, seleccione las consultas.
3. Arrastre y suelte objetos **Consulta** adicionales en el panel derecho.
4. Asigne a las consultas los nombres listaPrinciapl, Entidad y Problema.
5. Seleccione la consulta Problemas.
6. Arrastre los siguientes elementos de consulta al recuadro **Elementos de datos** :

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS_STANDALONE|[SOXISSUE]|
        [IS_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS_STANDALONE|[SOXISSUE]| 
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS_STANDALONE|[SOXISSUE]| 
         ID_FIELDS|[IS_ISSUE_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS_STANDALONE|[SOXISSUE]| 
         ID_FIELDS|[IS_REPORTING_PERIOD_ID]
     ```
7. Seleccione la consulta Entity en **Explorador de consultas**.
8. Arrastre los siguientes elementos de consulta al recuadro **Elementos de datos** :

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
        [SOXBUSENTITY_GPC]|[GEN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
        [SOXBUSENTITY_GPC]|[GEN_FULL_PATH]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
        [SOXBUSENTITY_GPC]|ID_FIELDS|[CEN_ENTITY_ID]
     ```
9. En **Explorador de consultas**, seleccione las consultas.
10. Arrastre y suelte una **Unión** junto a la consulta listMain y, a continuación, llene la unión con las consultas Entity y Issue.
11. Haga doble clic en la unión y complete los pasos siguientes.

    1. Pulse **Convertir a expresión**.
    2. Especifique el código siguiente en el panel **Definición de expresión** .

       ```
       "OP_RPS_AUX.IS_REL_PARENT_CHILD"(
       [Entity].[CEN_ENTITY_ID],
       [Issue].[IS_ISSUE_ID], 
       [Entity].[CEN_REPORTING_PERIOD_ID]) = 'Y' and
       [Entity].[CEN_REPORTING_PERIOD_ID] = [Issue].[IS_REPORTING_PERIOD_ID]
       ```
    3. Pulse **Aceptar**.
12. Seleccione la consulta listaPrincipal.
13. Arrastre y suelte los siguientes elementos de consulta desde el panel **Objetos insertables** :

    - `GEN_FULL_PATH`
    - `IS_NAME00`
    - `IS_DESCRIPTION`
14. Establezca las propiedades **Función de agregación** y **Función de agregación de resumen** en **Ninguno** para los tres elementos de datos.
15. Vaya a la página de informe principal y coloque los tres elementos de datos en la lista.
16. Ejecute el informe.

##### Resultados

Hay muchos más problemas conectados a la entidad Servicios financieros globales de nivel superior porque se mostrará cualquier problema que pueda estar relacionado a través de un objeto conectado a una entidad debido a cómo hemos modificado la unión.

> **Sugerencia:** Si crea una unión indirecta, los datos devueltos serán del modelo de objeto definido en la aplicación y no estarán limitados por los objetos del espacio de nombres.

### Creación de informes de acceso a detalles

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-creating-drill-through-reports)

Siga este procedimiento para crear informes de acceso a detalles.

Puede adjuntar diferentes subinformes a distintos sitios en un informe como la leyenda o una barra de un gráfico. También puede adjuntar varios informes de accesos a detalles al mismo elemento de datos y dar al usuario la opción de seleccionar uno.

> **Importante:** Los informes relacionales sólo pueden acceder a los detalles de otro informe relacional.

#### Creación de un informe padre

`Guía del creador de informes › Trabajar con datos relacionales › Creación de informes de acceso a detalles` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-creating-parent-report)

Siga este procedimiento para crear un informe padre.

##### Procedimiento

1. Cree un nuevo informe de tabla de referencias cruzadas.
2. Añada una solicitud de entidad de negocios tal como se describe en [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios). Utilice GEN_ENTITY_ID como campos para el origen de datos. La consulta de campos cruzados debe tener el filtro siguiente después de crear la solicitud:

   ```
   [DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_ENTITY_ID] = ?Entity ID?
   ```
3. Utilizando **Explorador de consultas**, seleccione la consulta para la tabla de referencias cruzadas.
4. En el panel **Objetos insertables** , arrastre y suelte los siguientes elementos de datos en el panel **Elementos de datos** de la tabla de referencias cruzadas:

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]|
          [PEN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]|
          ID_FIELDS|[PEN_ENTITY_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| [CN_CONTROL_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
          OPERATING_EFFECTIVENES (ENUMERATION)|[CN_OPERATING_EFFECTIVENES]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
          OPERATING_EFFECTIVENES (ENUMERATION)| [CN_OPERATING_EFFECTIVENES_ID]
     ```
5. Seleccione `CN_CONTROL_ID` y, en el panel Propiedades, realice los pasos siguientes.

   1. En la categoría **Elemento de datos** , establezca la propiedad **Función de agregación** en **Recuento diferenciado**.
   2. En la categoría **Elemento de datos** , establezca **Función de agregación de resumen** en **Automático**.
6. Vuelva a la página principal del informe.
7. Para rellenar la tabla de referencias cruzadas, realice los siguientes pasos.

   1. Arrastre y suelte el campo [CN_OPERATING_EFFECTIVENES] en el área de columnas desde la pestaña **Elementos de datos** del panel **Objetos insertables** .
   2. Arrastre y suelte el campo [PEN_NAME00] en el área de filas desde la pestaña **Elementos de datos** del panel **Objetos insertables** .
   3. Arrastre y suelte el campo [CN_CONTROL_ID] en el área de medidas de la pestaña **Elementos de datos**
8. Para dar formato al informe, realice los siguientes pasos.

   1. Centre los títulos de columna.
   2. Centre la intersección de la tabla de referencias cruzadas.
   3. Establezca el orden de clasificación en las columnas a ascendente.
   4. Establezca el orden de clasificación en las filas a ascendente.
9. Ejecute el informe.

##### Qué hacer a continuación

[Adición de un informe de acceso a detalles al padre](#adición-de-un-informe-de-acceso-a-detalles-al-padre)

#### Adición de un informe de acceso a detalles al padre

`Guía del creador de informes › Trabajar con datos relacionales › Creación de informes de acceso a detalles` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-adding-drill-through-report-parent)

Siga este procedimiento para añadir un informe de acceso a detalles a un informe así el usuario puede obtener información más detallada sobre los controles detrás de los números de la tabla de referencias cruzadas.

##### Procedimiento

1. Seleccione la página principal de un informe.
2. Desbloquee la tabla de referencias cruzadas.
3. Seleccione la cabecera de columna CN_OPERATING_EFFECTIVENES y realice los pasos siguientes.

   1. En el panel **Propiedades** , bajo la categoría **Datos** , seleccione **Propiedades**.
   2. Compruebe CN_OPERATING_EFFECTIVENES_ID para que se pueda utilizar como parámetro de acceso directo al subinforme.
   3. Pulse **Aceptar**.
4. Seleccione la cabecera de fila PEN_NAME00 y realice los pasos siguientes.

   1. En el panel **Propiedades** , bajo la categoría **Datos** , seleccione **Propiedades**.
   2. Compruebe PEN_ENTITY_ID para que se pueda utilizar como parámetro de acceso directo al subinforme.
   3. Pulse **Aceptar.**
5. Seleccione la medida en la tabla de referencias cruzadas.
6. En el panel **Propiedades** , en **Datos**, seleccione **Definiciones de acceso a detalles**.
7. Para añadir una nueva definición de acceso a detalles, pulse el icono ![Icono Añadir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-add_new.jpg) **Añadir** .
8. Para establecer el nombre del acceso a detalles en **Detalle de control**, pulse el icono ![Icono Renombrar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-rename.jpg) **Renombrar** .
9. Seleccione el informe **Acceso a detalles hijo**.
10. Compruebe si se abre el informe en una nueva ventana.
11. Pulse el icono **Editar** para editar los parámetros pasados al subinforme y complete los pasos siguientes.

    1. Para **ID de entidad**, establezca el método en **Pasar valor de elemento de datos** y el **Valor** en **PEN_ENTITY_ID**
    2. Para **ID de eficacia operativa**, establezca el método en **Pasar valor de elemento de datos** y **Valor** en **CN_OPERATING_EFFECTIVENES_ID**.
    3. Pulse **Aceptar**.
12. Ejecute el informe.

##### Resultados

Las medidas de las tablas de referencias cruzadas aparecen ahora en azul y subrayadas, lo que indica que se ha adjuntado un acceso a los detalles a esa celda. Cuando haga clic en la intersección de Asia Pac y No determinado, aparece un informe de acceso a detalles.

El informe de acceso a detalles muestra tres registros con la eficacia operativa de **No determinado** que viene con la entidad de negocios Asia Pac.

##### Qué hacer a continuación

Puede añadir enlaces CrossTrack a informes padre y de acceso a detalles (opcional). Para obtener información, consulte [Adición de enlaces CrossTrack](#adición-de-enlaces-crosstrack).

### Adición de enlaces CrossTrack

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-adding-crosstrack-links)

Un enlace CrossTrack es un hiperenlace en un informe que, cuando se pulsa, le lleva a una vista de tarea en IBM OpenPages®. Por ejemplo, puede crear enlaces CrossTrack en un informe desde un objeto de control a la vista de tarea correspondiente.

#### Adición de enlaces CrossTrack a informes autónomos y padres

`Guía del creador de informes › Trabajar con datos relacionales › Adición de enlaces CrossTrack` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-adding-crosstrack-standalone-parent-reports)

Siga este procedimiento para añadir un enlace CrossTrack a un informe autónomo o padre.

##### Procedimiento

1. Cree un nuevo informe de lista.
2. Desde el **Explorador de consultas**, abra la consulta.
3. En el panel **Propiedades** en **Varios**, establezca el nombre en **listMain**.
4. En el **Explorador de páginas**, seleccione la página de informe principal y realice los pasos siguientes.

   1. Pulse la pestaña **Origen** ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg) en el panel **Objetos insertables** .
   2. Arrastre los siguientes elementos de consulta al cuadro del objeto Lista:

      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_NAME00]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_DESCRIPTION]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
             CLASSIFICATION (ENUMERATION)|[CN_CLASSIFICATION]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
             DESIGN_EFFECTIVENESS (ENUMERATION)|[CN_DESIGN_EFFECTIVENESS]
        ```
      - ```
        DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_DETAIL_PAGE_URL]
        ```
5. Seleccione la columna `[CN_DETAIL_PAGE_URL]` en el informe y cortarla (no suprimirla).
6. Para cambiar los títulos de columna de la lista, realice los pasos siguientes.

   1. Seleccione cada título de columna.
   2. En el panel **Propiedades** en **Origen de texto**, establezca la propiedad **Tipo de origen** en **Texto**.
   3. Efectúe una doble pulsación en la propiedad **Texto** y escriba el valor de título adecuado. Establezca las cabeceras en los siguientes valores:

      - `[CN_NAME00]` a `Control Name`.
      - `[CN_DESCRIPTION]` a `Description`.
      - `[CN_CLASSIFICATION]` a `Classification`.
      - `[CN_DESIGN_EFFECTIVENESS]` a `Design Effectiveness`.
7. Añada JavaScript para enlaces CrossTrack :

   En el menú de navegación, pulse **Informe**. En las propiedades del informe, en **Ejecución y validación**, compruebe el valor del valor **Ejecutar con interactividad completa**.

   - **Si **Ejecutar con interactividad completa** está habilitado:**

     1. En el **Explorador de páginas**, seleccione la página principal del informe,
     2. En **General**, establezca **Vía de acceso del módulo** en `../v1/ext/OpenPages/PageModule`.

   - **Si **Ejecutar con interactividad completa** no está habilitado:**

     1. En el **Explorador de páginas**, seleccione la página principal del informe,
     2. Pulse **Objetos insertables**, pulse ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg)y expanda **Avanzado**.
     3. Arrastre **Referencia del componente de diseño** a la página. Se visualiza la página **Referencia del componente**.
     4. Pulse **Otro informe**y, a continuación, elija el informe **Contenido de equipo** > **OpenPages Informes de plataforma** > **Código común** > **Código común** .
     5. En **Componentes disponibles para referencia**, seleccione **Platform Common Javascript** y, a continuación, pulse **Aceptar**.
8. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg)y, a continuación, arrastre un objeto **Botón de hiperenlace** a la primera columna del informe de lista.
9. En la barra de navegación, pulse el icono **Bloquear** ![Icono Bloquear objetos de página](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-padlock.jpg) para desbloquear la plantilla (el icono cambia a desbloqueado).
10. Para convertir el elemento de datos de hiperenlace en una propiedad de la lista, realice los siguientes pasos.

    1. Seleccione el objeto **Lista** en la página principal del informe.
    2. En el panel **Propiedades** bajo la categoría **Datos** , pulse **Propiedades**.
    3. Seleccione `[CN_DETAIL_PAGE_URL]`.
    4. Pulse **Aceptar**.
11. Para configurar el objeto **Hiperenlace** , realice los pasos siguientes.

    1. Pulse el texto **Hiperenlace** en las celdas de la columna de objeto **Hiperenlace** .
    2. En el panel **Propiedades** bajo la categoría **Origen de texto** , establezca la propiedad **Tipo de origen** en **Valor de elemento de datos** y la propiedad **Valor de elemento de datos** en `[CN_NAME00]`.
    3. En el panel **Propiedades**, en la categoría **Fuente URL**, establezca la propiedad **Tipo de fuente** en **Expresión de informe**.
    4. Pulse la propiedad **Expresión de informe** y especifique el siguiente código JavaScript en el panel **Definición de expresión** :

       ```
       if (ReportOutput()="HTML")
       then
       ("javascript:crosstrack('"+ [listMain].[CN_DETAIL_PAGE_URL] + "');")
       else 
       ([listMain].[CN_DETAIL_PAGE_URL])
       ```

       > **Nota:** Los elementos en cursiva son los valores que deben sustituirse cuando se implementa en el sistema.
    5. Seleccione el texto de cabecera de columna en el objeto **Hiperenlace** .
    6. En el panel **Propiedades** bajo la categoría **Origen de texto** , establezca la propiedad **Texto** en **Nombre de control**.
12. En la **Barra de herramientas**, pulse de nuevo el icono **Padlock** para bloquear la plantilla (el icono cambia a bloqueado).
13. Seleccione la columna `[CN_NAME00]` original (no la columna de hiperenlace) en la página del informe y, a continuación, cortarla.
14. Ejecute el informe.

    > **Nota:** Para probar el enlace CrossTrack , el informe debe publicarse y ejecutarse desde OpenPages®.

##### Resultados

Cuando un usuario pulsa el enlace CrossTrack desde un informe autónomo o padre, la vista de tarea para ese objeto se abre en una pestaña dentro de OpenPages.

#### Adición de enlaces CrossTrack a informes de acceso a detalles

`Guía del creador de informes › Trabajar con datos relacionales › Adición de enlaces CrossTrack` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-adding-crosstrack-drill-through-reports)

Siga este procedimiento para añadir un enlace CrossTrack a un informe de acceso a detalles.

##### Procedimiento

1. Cree un nuevo informe de lista.
2. En el panel **Objetos insertables** , arrastre los siguientes elementos de datos a la lista (lo que se carga en el sistema será diferente de lo que ve aquí):

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
          [SOXBUSENTITY_GPC]|[PEN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_DESCRIPTION]
     ```
   - ```
     DEFAULT|[DEFAULT_REL][DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL] 
          ENUMERATION_FIELDS|OPERATING_EFFECTIVENES(ENUMERATION)|
            [CN_OPERATING_EFFECTIVENES]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL] ENUMERATION_FIELDS|
         OPERATING_EFFECTIVENES(ENUMERATION)| [CN_OPERATING_EFFECTIVENES_ID]
     ```
3. Cortar el campo `CN_OPERATING_EFFECTIVENES_ID` de la lista.
4. Añada JavaScript para enlaces CrossTrack :

   En el menú de navegación, pulse **Informe**. En las propiedades del informe, en **Ejecución y validación**, compruebe el valor del valor **Ejecutar con interactividad completa**.

   - **Si **Ejecutar con interactividad completa** está habilitado:**

     1. En el **Explorador de páginas**, seleccione la página principal del informe,
     2. En **General**, establezca **Vía de acceso del módulo** en `../v1/ext/OpenPages/PageModule`.

   - **Si **Ejecutar con interactividad completa** no está habilitado:**

     1. En el **Explorador de páginas**, seleccione la página principal del informe,
     2. Pulse **Objetos insertables**, pulse ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg)y expanda **Avanzado**.
     3. Arrastre **Referencia del componente de diseño** a la página. Se visualiza la página **Referencia del componente**.
     4. Pulse **Otro informe**y, a continuación, elija el informe **Contenido de equipo** > **OpenPages Informes de plataforma** > **Código común** > **Código común** .
     5. En **Componentes disponibles para referencia**, seleccione **Platform Common Javascript** y, a continuación, pulse **Aceptar**.
5. Vaya al **Explorador de consultas** y añada los filtros siguientes a la consulta:

   - `[DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_ENTITY_ID] = ?Entity ID?`
   - `[CN_OPERATING_EFFECTIVENES_ID] = ?Operating Effectiveness ID?`
   - `[DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_REPORTING_PERIOD_ID] = -1`
6. Valide el informe.
7. Guarde el informe con el nombre **Acceso a detalles hijo**.

##### Resultados

Cuando un usuario pulsa el enlace CrossTrack en el informe, la vista de tarea para ese objeto se abre en una nueva y mínima instancia de OpenPages®, en una ventana de navegador independiente. Esta ventana de navegador no tiene navegación y sólo está pensada para ese objeto en particular. No se recomienda mantener abiertas varias pestañas o ventanas de OpenPages porque pueden desincronizarse. Anime a los usuarios a cerrar estas pestañas y ventanas separadas rápidamente y volver a la ventana principal de OpenPages para realizar los demás trabajos.

### Creación de un informe maestro-detalle

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-creating-master-detail-report)

Un informe maestro-detalle contiene normalmente una segunda lista incorporada en la lista de informe principal. Esto crea una situación en la que tiene una consulta externa para la lista de informe principal y una subconsulta para la lista integrada. Lo que significa en términos de rendimiento es que para cada registro retirado de la base de datos, se ejecutará otra consulta. Solo debe utilizar esta construcción si es su única opción debido a la estructura de los datos.

#### Procedimiento

1. Cree un nuevo informe de lista.
2. Añada una solicitud de entidad de negocios tal como se describe en [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios). Utilice `GEN_ENTITY_ID` como campo para el origen de datos. La consulta de campos cruzados debe tener el filtro siguiente después de crear la solicitud:

   ```
    [DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_ENTITY_ID] = ?Entity ID? 
   ```
3. En el panel **Objetos insertables** , arrastre y suelte los siguientes elementos de datos en la lista (recuerde que lo que se carga en el sistema puede ser diferente de lo que ve aquí):

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| 
         [CN_CONTROL_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_NAME00]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|[CN_DESCRIPTION]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL] ENUMERATION_FIELDS|
         OPERATING_EFFECTIVENES(ENUMERATION)| [CN_OPERATING_EFFECTIVENES]
     ```
4. Cortar el campo `CN_CONTROL_ID` de la lista.
5. Vaya a **Explorador de consultas** y añada los filtros siguientes a la consulta:

   ```
   [DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_REPORTING_PERIOD_ID] = -1
   ```
6. Valide el informe.
7. Vaya a la página de informe principal y complete los siguientes pasos:

   1. Ordene CN_NAME00 de forma ascendente.
   2. En la pestaña Caja de herramientas **Objetos insertables** del panel ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg), seleccione una **Lista** y suéltela en la última columna de la lista existente. La lista debe estar bloqueada.
8. En la nueva lista, arrastre y suelte los siguientes elementos de datos:

   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| [CN_CONTROL_ID]
     ```
   - ```
     DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ENUMERATION_FIELDS| 
          FINANCIAL_STATEMENT_AS(ENUMERATION)|[CN_FINANCIAL_STATEMENT_AS]
     ```
9. Ejecute el informe.

#### Qué hacer a continuación

[Creación de relaciones entre listas maestras e incorporadas](#creación-de-relaciones-entre-listas-maestras-e-incorporadas)

#### Creación de relaciones entre listas maestras e incorporadas

`Guía del creador de informes › Trabajar con datos relacionales › Creación de un informe maestro-detalle` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=report-creating-relationships-between-master-embedded-lists)

El informe es obviamente incorrecto porque los valores de `CN_CONTROL_ID` no coinciden. Esto se debe a que no ha creado la relación entre la lista maestra y la lista incorporada.

##### Procedimiento

1. Seleccione un elemento de la lista incorporada.
2. En el menú **Datos** de la barra de herramientas principal, seleccione **Relaciones maestro-detalle**.
3. Cree una unión entre `CN_CONTROL_ID` en listMain y `CN_CONTROL_ID` en childList.
4. Pulse **Aceptar**.
5. Ejecute el informe.

##### Resultados

Ahora hay menos filas en la lista incorporada y los valores de ID de control coinciden con el registro principal.

##### Qué hacer a continuación

[Formateo de listas integradas](#formateo-de-listas-integradas)

#### Formateo de listas integradas

`Guía del creador de informes › Trabajar con datos relacionales › Creación de un informe maestro-detalle` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=report-formatting-embedded-lists)

Puede realizar algunas actividades de limpieza para hacer que las listas integradas sean menos obvias.

##### Procedimiento

1. Seleccione los campos `CN_CONTROL_ID` en ambas listas y córtelos. Deben estar en la consulta pero no es necesario que se visualicen.
2. Seleccione la cabecera de la lista integrada y realice los siguientes pasos:

   1. Utilizando el selector de ancestro, seleccione la lista.
   2. En el panel **Propiedades** bajo **General**, establezca la propiedad **Títulos de columna** en **Ocultar**.
3. Seleccione la celda de la lista principal en la que se encuentra la lista integrada. En el panel **Propiedades** bajo **Cuadro**, seleccione la propiedad **Relleno** y establezca todos los valores en **cero**.
4. Ejecute el informe.

### Adición de micrográficos

`Guía del creador de informes › Trabajar con datos relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-adding-microcharts)

Un micrográfico es una versión en miniatura de un gráfico que se puede insertar en una tabla de referencias cruzadas o una lista. Operan de la misma manera que una función de informe maestro-detalle en la que el micrográfico es una vista detallada de los datos maestros.

#### Procedimiento

1. Cree un nuevo informe de lista.
2. Añada una solicitud de entidad de negocios tal como se describe en [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios). Utilice GEN_ENTITY_ID como campos para el origen de datos. La consulta de campos cruzados debe tener el filtro siguiente después de crear la solicitud:

   ```
   [DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_ENTITY_ID] = ?Entity ID?
   ```
3. En el panel **Objetos insertables** , arrastre y suelte los siguientes elementos de datos en la lista (recuerde que lo que se carga en el sistema será diferente de lo que ve aquí):

   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]|[PEN_NAME00]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]|ID_FIELDS| [PEN_ENTITY_ID]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL] ENUMERATION_FIELDS| OPERATING_EFFECTIVENES(ENUMERATION)| [CN_OPERATING_EFFECTIVENES]`
4. Cortar el campo `PEN_ENTITY_ID` y el campo `CN_OPERATING_EFFECTIVENES` de la lista.
5. Vaya a **Explorador de consultas** y añada los filtros siguientes a la consulta:

   - `[DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_REPORTING_PERIOD_ID] = -1`
   - `[CN_OPERATING_EFFECTIVENES] is not null`
6. En el **Explorador de consultas**, cambie el nombre de la consulta utilizada por la lista por **listMain**.
7. Valide el informe.
8. Vaya a la página de informe principal y complete los siguientes pasos:

   1. Ordene PEN_NAME00 de forma ascendente.
   2. Establezca la etiqueta para PEN_NAME00 en **Entidad de negocios**.
   3. En la pestaña Caja de herramientas del panel **Objetos insertables** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg), seleccione un **Gráfico** y suéltelo en la última columna de la lista existente. La lista debe estar bloqueada.
   4. Seleccione **Micrográfico** y un diagrama de barras **Columna** .
9. En el nuevo gráfico, arrastre y suelte los siguientes elementos de datos:

   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL]|ID_FIELDS| [CN_CONTROL_ID]`
   - `DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|[SOXCONTROL] ENUMERATION_FIELDS| OPERATING_EFFECTIVENES(ENUMERATION)| [CN_OPERATING_EFFECTIVENES]`
10. En el **Explorador de consultas**, cambie el nombre de la consulta utilizada por la lista por **microChart**.
11. Vaya a **Explorador de consultas** y añada los filtros siguientes a la consulta:

    - `[DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_REPORTING_PERIOD_ID] = -1`
    - `[CN_OPERATING_EFFECTIVENES] is not null`
12. En el panel **Objetos insertables** , arrastre y suelte el siguiente elemento de datos:

    ```
    DEFAULT|[DEFAULT_REL]|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
        [SOXBUSENTITY_GPC]|ID_FIELDS|[PEN_ENTITY_ID]
    ```
13. Seleccione el elemento de datos `CN_CONTROL_ID` y, en el panel **Propiedades** , realice los pasos siguientes.

    1. En la categoría **Elemento de datos** , establezca la propiedad **Función de agregación** en **Recuento diferenciado**.
    2. En la categoría **Elemento de datos** , establezca **Función de agregación de resumen** en **Automático**.
14. En la página principal del informe, cambie el nombre de la columna de gráfico por **Eficacia operativa**.
15. En el menú **Datos** de la barra de herramientas principal, seleccione **Relaciones maestro-detalle**y realice los pasos siguientes.

    1. Cree una unión entre `PEN_ENTITY_ID` en listMain y `PEN_ENTITY_ID` en el micrográfico.
    2. Pulse **Aceptar**.
16. Seleccione el fondo del micrográfico y realice los siguientes pasos.

    1. En el panel **Propiedades** bajo la categoría **Posición**, establezca la propiedad **Tamaño y desbordamiento** en una altura de 100 px.
    2. Establezca el ancho en 150 píxeles.
17. Seleccione el eje y del micrográfico y, en el panel **Propiedades** bajo la categoría **General** , establezca la propiedad **Etiquetas de eje** en **Mostrar**.
18. En **Explorador de condiciones**, seleccione las variables y realice los pasos siguientes.

    1. Añada una nueva variable de tipo serie.
    2. En el editor de expresiones, añada `[microChart].[CN_OPERATING_EFFECTIVENES]`
    3. Pulse **Aceptar**.
    4. Añada tres valores: `Effective`, `Ineffective`y `Not Determined`.
    5. En el panel **Propiedades** en **Varios**, establezca la propiedad **Nombre** en **Eficacia operativa**
19. En la página de informe principal, seleccione el micrográfico y, en el panel **Propiedades** , bajo **Color y fondo**, seleccione **Paleta condicional** y realice los pasos siguientes.

    1. Para **Variable**, seleccione **Eficacia operativa**.
    2. Para **Efectivo** , establezca el color en **Cal**.
    3. Para **Ineficaz** , establezca el color en **rojo**.
    4. Para **No determinado** , establezca el color en **azul**.
    5. Pulse **Aceptar**.
20. Seleccione **Barra de series**. En el panel Propiedades, bajo **Etiquetas de gráfico**, establezca la propiedad **Valores** en **Mostrar**.
21. Ejecute el informe.

#### Resultados

No hay comparación del control Eficacia operativa entre las diferentes entidades de negocios para comparar el progreso sobre cómo están teniendo el proceso bajo control.

## Trabajar con entidades de negocios

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-working-business-entities)

Una entidad de negocios es un objeto jerárquico. Las entidades de negocios pueden tener padres e hijo que son a su vez entidades de negocios. Cualquier nivel de la estructura de entidad de negocios puede tener otros objetos vinculados a ellas como procesos o evaluaciones de riesgo.

Esta información solo se aplica a modelos de entorno estándares, no a modelos de entorno básicos.

Puede realizar las siguientes tareas con entidades de negocios:

- Examinar y filtrar datos de informe
- Determinar cómo se cuentan las instancias de datos
- Determinar cómo se visualizan los números, por ejemplo, números individuales o de resumen para una entidad de negocios seleccionada
- Habilitar la característica detallar menos y detallar más en los informes

Hay dos vistas de entidades de negocios: GPC (abuelo-padre-hijo) que existe en el entorno de forma predeterminada y un modelo jerárquico definido por el usuario.

El modelo definido por el usuario se puede crear en IBM OpenPages®. Para obtener más información sobre cómo configurar estos niveles de objetos recursivos, consulte la publicación *IBM OpenPages Guía del administrador*

### El asunto de consulta SOXBUSENTITY_GPC

`Guía del creador de informes › Trabajar con entidades de negocios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-soxbusentity-gpc-query-subject)

El asunto de consulta SOXBUSENTITY_GPC es el objeto de entidad más básico. Es parecido al objeto Componente GPC excepto que todos los valores son parte del mismo objeto de consulta.

El asunto de consulta tiene tres niveles abstractos de entidades de negocios que puede utilizar en el informe:

- Entidad abuelo (GEN)
- Entidad padre (PEN)
- Entidad hijo (CEN)

En este modelo, solo la entidad hijo tiene otros objetos asociados.

Este es el asunto de consulta primario que utilizará al trabajar con entidades de negocios en el modelo relacional.

### Jerarquía de entidad definida por el usuario

`Guía del creador de informes › Trabajar con entidades de negocios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-user-defined-entity-hierarchy)

En el modelo definido por el usuario, éste define los niveles de objeto recursivo y los nombres de los niveles. Haciendo esto, una vez se regenera el entorno, tendrá objetos en el modelo con los nombres que ha seleccionado en la IU.

Por ejemplo, si la jerarquía consta de regiones, países, estados o ciudades, verá cuatro carpetas en el entorno con estos nombres, asuntos de consulta y las relaciones adecuadas entre ellas.

> **Nota:** Debe configurar el sistema para incluir toda la profundidad de la jerarquía o el modelo de entorno creado no funcionará correctamente.

Cuando se crea una jerarquía definida por el usuario, se crea un asunto de consulta para cada nivel de la jerarquía. Estas son las ventajas y desventajas de esta estructura de objeto:

- Cada nivel de la jerarquía está filtrado previamente y solo devolverá entidad en ese nivel.
- Estos objetos son ideales para la creación de solicitudes de nivel de entidad en cascada.
- Se pueden utilizar como campos individuales en un informe de lista sin tener que crear filtros complejos.
- Las cabeceras de campos reflejarán los nombres que ha seleccionado cuando definió la jerarquía.

### Objetos Componente GPC

`Guía del creador de informes › Trabajar con entidades de negocios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-gpc-component-objects)

Los objetos Componente GPC se incluyen de forma predeterminada en el modelo.

Este objeto solo se puede encontrar en la carpeta `Miscellaneous` > `Advanced` > `GPC Component Objects`. Los tres asuntos de consulta creados son equivalentes a abuelo, padre e hijo. Cuando utilice objetos de componente, tenga en cuenta los siguientes comportamientos:

- Si utiliza asuntos de consulta autónomos, cada una de las entidades aparecerá en los niveles abuelo, padre e hijo.
- Si utiliza los tres niveles de GPC en un informe, debe añadir filtros para obtener los valores correctos en cada nivel.
- Puede utilizar el nivel padre para crear una solicitud que contiene entidades de todos los niveles de la jerarquía.
- Los informes escritos con los objetos GPC se mueven entre diferentes entornos.

Se recomienda que los informes se escriban con el asunto de consulta SOXBUSENTITY_GPC en lugar de este modelo.

### El modelo de datos GPC

`Guía del creador de informes › Trabajar con entidades de negocios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-gpc-data-model)

Hay tres niveles de entidades en el modelo de objeto GPC: abuelo, padre e hijo. Esto forma una abstracción de los datos. Aunque tenga más de tres niveles en la jerarquía de entidad, se puede utilizar este modelo.

Puede ver estos tres niveles:

- Los abuelos no tienen padres, pero tienen hijos.
- Los padres pueden tener padres, pueden tener hijos y pueden ser hijos.
- Los hijos pueden tener padres.

Las columnas numéricas del informe representan la distancia entre entidades de la jerarquía de entidad. Una entidad es siempre padre de sí misma y un padre es siempre un hijo de sí mismo. Esto se puede ver donde la distancia es igual a cero.

**Tabla 1. Uso del nivel de entidad típico**

| Utilice este nivel... | Para ... |
| --- | --- |
| abuelo (GEN_) | Filtrado y limitación |
| padre (PEN_) | Agrupación y agregación de datos, y solicitud |
| hijo (CEN_) | Filtrado y limitación |

### Filtrado de entidades de negocios relacionales

`Guía del creador de informes › Trabajar con entidades de negocios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-filtering-relational-business)

Puede filtrar entidades de negocios relacionales en los informes.

Los temas siguientes describen cómo configurar el filtrado en informes.

- [Filtrado utilizando la vía de acceso completa](#filtrado-utilizando-la-vía-de-acceso-completa)
- [Filtrado de la extensión de jerarquía](#filtrado-de-la-extensión-de-jerarquía)
- [Filtrado utilizando solicitudes en cascada](#filtrado-utilizando-solicitudes-en-cascada)
- [Referencia rápida para visualización y filtrado de datos](#referencia-rápida-para-visualización-y-filtrado-de-datos)

#### Filtrado utilizando la vía de acceso completa

`Guía del creador de informes › Trabajar con entidades de negocios › Filtrado de entidades de negocios relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-filtering-using-full-path)

La variable de vía de acceso completa que existe en todos los objetos de entidad de negocios se utiliza habitualmente para permitir al usuario filtrar el contexto del informe.

Las instrucciones para crear este tipo de solicitud se pueden encontrar en [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios). Una vez se ha creado la solicitud, puede ajustar el filtro que crea el asistente de solicitud para lograr los resultados que desea.

En este primer ejemplo, vamos a visualizar el nombre padre y la vía de acceso completa.

Lo que está haciendo este filtro es permitir al usuario ver la entidad exacta que se ha elegido en la solicitud. El segundo filtro indica que sólo desea ver las entidades que tienen una distancia de cero de la entidad seleccionada, tal como se muestra en la Figura 1. Este filtro solo puede devolver la entidad que se ha elegido.

*Figura 1. Filtrado de entidad de negocios - G2P = 0*

![Tabla de referencias cruzadas filtrada para mostrar las entidades con una distancia de cero de la entidad seleccionada](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_business_entity_filtering_1.jpg)

Si elimino el segundo filtro, obtengo lo siguiente, tal como se muestra en la Figura 2:

*Figura 2. Filtrado de entidad de negocios - Sin filtrado G2P*

![Tabla de referencias cruzadas sin filtros aplicados](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_business_entity_filtering_2.jpg)

Esto muestra la entidad seleccionada en la solicitud y los hijos directos debajo de esa entidad.

Si cambio el filtro G2P a 1 (mostrar los padres que están a una unión del abuelo), obtengo lo siguiente, tal como se muestra en la Figura 3:

*Figura 3. Filtrado de entidad de negocios - G2P = 1*

![Tabla de referencias cruzadas filtrada para mostrar las entidades con una distancia de 1 de la entidad seleccionada](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_business_entity_filtering_4.jpg)

Esto solo muestra los hijos de la entidad seleccionada.

Ahora, si cambio la variable de visualización a la entidad hijo y elimino el filtro de distancia, obtengo lo siguiente cuando ejecuto el informe, tal como se muestra en Figura 4:

*Figura 4. Filtrado de entidad de negocios - Todos los niveles*

![Tabla de referencias cruzadas filtrada para mostrar la entidad seleccionada y las entidades hijo de la entidad seleccionada](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_business_entity_filtering_3.jpg)

Lo ve ahora (solo se muestran parte de los datos) es la entidad seleccionada y todas las entidades debajo de lo que estaba seleccionado. Esto es útil cuando desea hacer un resumen de toda la información debajo de una entidad seleccionada.

Lo que muestran estos ejemplos es la flexibilidad que tiene al filtrar un objeto de entidad de negocios para obtener datos en una entidad específica, entidades hijo o todo resumen para una entidad de negocios.

##### Campos de contexto de entidad relacional

`Guía del creador de informes › Trabajar con entidades de negocios › Filtrado de entidades de negocios relacionales › Filtrado utilizando la vía de acceso completa` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=path-relational-entity-context-fields)

Puede utilizar campos de contexto de entidad relacional para filtrar entidades en el modelo relacional.

Cuadro 1 explica los campos de contexto utilizados para filtrar entidades en el modelo relacional.

**Tabla 1. campos de contexto de entidad relacional**

| Nombre de campo | Descripción |
| --- | --- |
| G2P_DISTANCE | El número de niveles entre un abuelo y un padre. El valor es 0 o 1. |
| G2P_IS_PRIMARY | Indica si el objeto abuelo es el padre principal del objeto padre. Los valores son Y y N. |
| P2C_DISTANCE | El número de niveles entre un padre y un hijo. Los valores pueden ser de 0 a N. |
| P2C_IS_PRIMARY | Indica si el objeto padre es padre principal del objeto hijo. Los valores son Y y N. |

#### Filtrado de la extensión de jerarquía

`Guía del creador de informes › Trabajar con entidades de negocios › Filtrado de entidades de negocios relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-filtering-hierarchy-depth)

Puede crear una solicitud basada en la profundidad de una entidad en la jerarquía.

> **Nota:** Si tiene una base de datos IBM® Db2® , debe sustituir la función Oracle `INSTR` en la siguiente expresión de ejemplo por la función Db2 correspondiente.

Por ejemplo, supongamos que tiene una jerarquía de entidad de negocios distribuida uniformemente y desea que el usuario únicamente seleccione desde el tercer nivel de la jerarquía. Puede colocar el siguiente filtro en la solicitud para que solo puedan ver el tercer nivel de la jerarquía:

```
instr([PEN_FULL_PATH],'/',1,3) > 0 and
```

```
instr([PEN_FULL_PATH],'/',1,4) = 0
```

Este filtro utiliza las barras diagonales de la variable de vía de acceso completa para determinar la profundidad absoluta de una entidad en la jerarquía.

Todos los elementos tienen tres barras inclinadas que es lo que se ha diseñado que muestre el filtro.

#### Filtrado utilizando solicitudes en cascada

`Guía del creador de informes › Trabajar con entidades de negocios › Filtrado de entidades de negocios relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-filtering-using-cascaded-prompts)

Las solicitudes en cascada se utilizan cuando el usuario desea ver únicamente valores de solicitud basados en una selección de una solicitud anterior.

##### Acerca de esta tarea

Este ejemplo le muestra cómo utilizar los objetos en las carpetas GPC para crear una serie de solicitudes en cascada.

##### Procedimiento

1. Cree un nuevo informe de lista.
2. Siga las instrucciones de [Creación de una página de solicitud](#creación-de-una-página-de-solicitudes).
3. Para crear una solicitud de nivel global, realice los siguientes pasos.

   1. Arrastre un **Elemento de texto** a la primera columna de la tabla. Entre el texto para la solicitud en el elemento de texto.
   2. Seleccione la celda de tabla y establezca la ubicación para que sea a la derecha horizontalmente y arriba verticalmente.
   3. Haga que el texto esté en negrita utilizando el icono **Negrita** .
   4. Arrastre un objeto **Solicitud de valor** a la segunda columna de la página de solicitud.

      El Asistente de solicitudes se abre.
4. En la pantalla **Elegir parámetro** del asistente de solicitud, realice los pasos siguientes.

   1. Seleccione la opción **Crear un parámetro nuevo**.
   2. En el cuadro, escriba un nombre para el parámetro, por ejemplo, `Global Entity`.
   3. Pulse **Siguiente**.
5. En la pantalla **Crear filtro** , realice los pasos siguientes.

   1. Seleccione la opción **Crear un filtro parametrizado**.
   2. En el recuadro **Elemento de paquete** , pulse el botón Examinar y vaya al siguiente elemento de consulta (los nombres de estos elementos de consulta están definidos por el usuario, por lo que pueden ser diferentes en el sistema):

      ```
      DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER|REGIONAL HIERARCHY|
      1_GLOBAL_FOLDER|ID_FIELDS|[GLOBAL]|ID_FIELDS|[GLOBAL_ENTITY_ID]
      ```
   3. En el cuadro **Operador** , utilice el signo de igual (=) (valor predeterminado).
   4. Deseleccione el recuadro para la opción **Hacer que este filtro sea opcional** .
   5. Si tiene varias consultas en el informe, en el recuadro **Aplicar filtro** , seleccione la consulta a la que se debe aplicar el filtro.
   6. Pulse **Siguiente**.
6. En la pantalla **Rellenar control** , realice los pasos siguientes.

   1. Seleccione la opción **Crear nueva consulta** .
   2. En el cuadro **Nombre** , escriba un nombre para la consulta, por ejemplo, `Global Entity Prompt`.
   3. En el recuadro **Valores a visualizar** , pulse el botón Examinar y vaya al siguiente elemento de consulta:

      ```
      DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER|REGIONAL HIERARCHY|
      1_GLOBAL_FOLDER|[GLOBAL]|[GLOBAL_NAME00]
      ```
   4. Se mostrarán los siguientes valores en el recuadro:

      ```
      [DEFAULT_REL].[GLOBAL].[GLOBAL_NAME00] 
      ```
   5. Pulse **Finalizar**.
7. Seleccione la solicitud que acaba de crear y, en la categoría **General** del panel **Propiedades** , cambie el valor de **Seleccionar interfaz de usuario** a **Recuadro de lista**.
8. En el panel **Propiedades** bajo **Datos**, establezca la propiedad **Ordenación** para que sea el nombre de la entidad empresarial.
9. Si hay un número limitado de elementos en la solicitud, puede establecer la altura de la solicitud en un valor que muestra solo las solicitudes y no los espacios en blanco. Complete los pasos siguientes.

   1. Seleccione la solicitud en la tabla que desee establecer la altura.
   2. En el panel Propiedades, en **Posición**, seleccione **Tamaño y desbordamiento**.
   3. En el cuadro de diálogo, establezca la altura en **14 pt** veces el número de filas de la solicitud.
10. Para añadir un botón Nueva solicitud a la página de solicitud, realice los pasos siguientes.

    1. Arrastre un **Botón de solicitud** a la celda de tabla bajo la solicitud de valor que acaba de crear.
    2. En el panel **Propiedades** bajo **General**, establezca la propiedad **Tipo** en **Volver a solicitar**.
    3. Arrastre un **Elemento de texto** al botón de solicitud y especifique el texto siguiente: `Update Regional Entity`.
    4. En el panel **Correcciones** bajo **Color y fondo**, establezca la propiedad **Color de fondo** en **Plata**.
    5. Seleccione la celda de tabla en la que se ha colocado el botón.
    6. En el panel **Propiedades** bajo **Posición**, establezca la propiedad **Tamaño y desbordamiento** en **40 px**.
11. En **Explorador de consultas**, seleccione el asunto de consulta **Solicitud de entidad global** y realice los pasos siguientes.

    1. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) en el panel **Objetos insertables** .
    2. Arrastre y suelte un objeto **Filtro** en el panel **Filtro** de la consulta.
    3. En el panel **Definición de expresión** , especifique la expresión siguiente:

       ```
       [DEFAULT_REL].[GLOBAL].[IS_ROW_PUSHED_DOWN]='N'
       ```

       El elemento de datos se puede encontrar en la siguiente carpeta:

       ```
       DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER|REGIONAL HIERARCHY|
       1_GLOBAL_FOLDER|[GLOBAL]|HIERARCHY_CONTEXT|[IS_ROW_PUSHED_DOWN]
       ```
    4. Pulse **Aceptar**.
12. Para crear una solicitud de nivel regional, realice los siguientes pasos.

    1. Arrastre un **Elemento de texto** a la primera columna de la tabla. Entre el texto para la solicitud en el elemento de texto.
    2. Seleccione la celda de tabla y establezca la ubicación para que sea a la derecha horizontalmente y arriba verticalmente.
    3. Haga que el texto esté en negrita utilizando el icono **Negrita** .
    4. Arrastre un objeto **Solicitud de valor** a la página de solicitud.

       Se abre el Asistente de solicitudes.
13. En la pantalla **Elegir parámetro** del asistente de solicitud, realice los pasos siguientes.

    1. Seleccione la opción **Crear un parámetro nuevo**.
    2. En el cuadro, escriba un nombre para el parámetro, por ejemplo, `Region Entity`.
    3. Pulse **Siguiente**.
14. En la pantalla **Crear filtro** , realice los pasos siguientes.

    1. Seleccione la opción **Crear un filtro parametrizado**.
    2. En el recuadro **Elemento de paquete** , pulse el botón Examinar y vaya al siguiente elemento de consulta (los nombres de estos elementos de consulta están definidos por el usuario, por lo que pueden ser diferentes en el sistema):

       ```
       DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER|REGIONAL HIERARCHY|
       2_REGIONS_FOLDER|[REGIONS]|ID_FIELDS|[REGIONS_ENTITY_ID]
       ```
    3. En el cuadro **Operador** , utilice el signo de igual (=) (valor predeterminado).
    4. Deseleccione el recuadro para la opción **Hacer que este filtro sea opcional** .
    5. Si tiene varias consultas en el informe, en el recuadro **Aplicar filtro** , seleccione la consulta a la que se debe aplicar el filtro.
    6. Pulse **Siguiente**.
15. En la pantalla **Rellenar control** , realice los pasos siguientes.

    1. Seleccione la opción **Crear nueva consulta** .
    2. En el cuadro **Nombre** , escriba un nombre para la consulta, por ejemplo, `Region Entity Prompt`.
    3. En el recuadro **Valores a visualizar** , pulse el botón Examinar y vaya al siguiente elemento de consulta:

       ```
       DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER|REGIONAL HIERARCHY|
       2_REGIONS_FOLDER|[REGIONS]|[REGIONS_NAME00]
       ```
    4. Se mostrarán los siguientes valores en el recuadro:

       ```
       [DEFAULT_REL].[REGIONS].[REGIONS_NAME00] 
       ```
    5. En la lista **Origen de cascada** , seleccione **Entidad global**.
    6. Pulse **Finalizar**.
16. Seleccione la solicitud que acaba de crear y, en la categoría **General** del panel **Propiedades** , cambie el valor de **Seleccionar interfaz de usuario** a **Recuadro de lista**.
17. En el panel **Propiedades** bajo **Datos**, establezca la propiedad **Ordenación** para que sea el nombre de la entidad empresarial.
18. Si hay un número limitado de elementos en la solicitud, puede establecer la altura de la solicitud en un valor que muestra solo las solicitudes y no los espacios en blanco. Complete los pasos siguientes.

    1. Seleccione la solicitud en la tabla que desee establecer la altura.
    2. En el panel Propiedades, en **Posición**, seleccione **Tamaño y desbordamiento**.
    3. En el cuadro de diálogo, establezca la altura en **14 pt** veces el número de filas de la solicitud.
19. En **Explorador de consultas**, seleccione el asunto de consulta **Solicitud de entidad global** y realice los pasos siguientes.

    1. Pulse la pestaña ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) **Caja de herramientas** en el panel **Objetos insertables** .
    2. Arrastre y suelte un objeto **Filtro** en el panel **Filtro** de la consulta.
    3. En el panel **Definición de expresión** , especifique lo siguiente:

       ```
       [DEFAULT_REL].[REGIONAL].[IS_ROW_PUSHED_DOWN]='N'
       ```

       El elemento de datos se puede encontrar en la siguiente carpeta:

       ```
       DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER|REGIONAL HIERARCHY|
       2_REGIONS_FOLDER|[GLOBAL]|HIERARCHY_CONTEXT|[IS_ROW_PUSHED_DOWN]
       ```
    4. Pulse **Aceptar**.
20. Para añadir un botón Nueva solicitud a la página de solicitud, realice los pasos siguientes.

    1. Arrastre un **Botón de solicitud** a la celda de tabla bajo la solicitud de valor que acaba de crear.
    2. En el panel **Propiedades** bajo **General**, establezca la propiedad **Tipo** en **Volver a solicitar**.
    3. Arrastre un **Elemento de texto** al botón de solicitud y especifique el texto siguiente: `Update Regional Entity`.
    4. En el panel **Correcciones** bajo **Color y fondo**, establezca la propiedad **Color de fondo** en **Plata**.
    5. Seleccione la celda de tabla en la que se ha colocado el botón.
    6. En el panel **Propiedades** bajo **Posición**, establezca la propiedad **Tamaño y desbordamiento** en **40 px**.
21. Repita los pasos 11-17 y cree la solicitud Departamento. No necesita añadir un botón de nueva solicitud después de esta solicitud.

##### Resultados

Cuando se representa el primer informe, solo se llena la solicitud global.

Cuando selecciona una valor de la lista y pulsa **Actualizar entidad regional**, el cuadro de lista de la entidad de región se llena solo con entidades que son hijos directos de la entidad **Servicios financieros globales**.

De nuevo, cuando selecciona **Norteamérica** y pulsa **Actualizar Entidad de departamento**, el cuadro de lista **Entidad de departamento** se llena con entidades que son hijos directos de la entidad **Norteamérica**.

#### Referencia rápida para visualización y filtrado de datos

`Guía del creador de informes › Trabajar con entidades de negocios › Filtrado de entidades de negocios relacionales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=entities-quick-reference-displaying-filtering-data)

Puede utilizar la información de consulta rápida para crear solicitudes.

Cuadro 1 contiene información de referencia que puede utilizar al crear solicitudes.

Para utilizar esta información de referencia rápida, seleccione una de las opciones de visualización de datos de informe y, después, implemente cada una de las configuraciones de esa fila.

Para cada opción de visualización, seleccione los siguientes valores de entidad en los campos **Solicitud de valor**:

- Para **Elemento de paquete**, seleccione `GEN_ENTITY_ID`
- En **Operador**, seleccione el signo de igual (=)
- Para **Valor a utilizar**, seleccione `PEN_ENTITY_ID`
- Para **Valor a visualizar**, seleccione `PEN_FULL_PATH`

**Tabla 1. Referencia rápida de entidades**

| Opciones de visualización de datos de informe | Valor de elemento de consulta (página de informe) | Elemento de consulta y valor en una expresión de filtro (asunto de consulta de informe) |
| --- | --- | --- |
| Solo la entidad seleccionada<br>Este informe puede soportar una solicitud de lista de selección múltiple. Utilice `in` para el operador **Solicitud de valor**. | GEN_NAME00 | G2P_DISTANCE=0 |
| La entidad seleccionada Y el siguiente nivel | PEN_NAME00 | No se aplica |
| La entidad seleccionada y todos los niveles por debajo de la entidad | CEN_NAME00 | No se aplica |
| El siguiente nivel por debajo de la entidad seleccionada | PEN_NAME00 | G2P_DISTANCE=1<br>La selección de la entidad de nivel inferior en la solicitud da como resultado un informe nulo. |
| Todos los niveles por debajo de la entidad seleccionada | CEN_NAME00 | G2P_DISTANCE=1<br>La selección de la entidad de nivel inferior en la solicitud da como resultado un informe nulo. |
| Un resumen solo de la entidad seleccionada<br>Utilice esta opción solo con un informe de tabla de referencias cruzadas. | GEN_NAME00 | No se aplica |

## Trabajar con objetos compartidos

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-working-shared-objects)

Los objetos compartidos son objetos que pueden ser hijo de varios tipos de objeto padre. Por ejemplo, varios objetos de riesgo padre pueden hacer referencia a un único objeto de control compartido o un objeto de control puede tener varios padres.

### Agregación de datos para objetos compartidos

`Guía del creador de informes › Trabajar con objetos compartidos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-aggregating-data-shared)

Si un objeto hijo compartido tiene varios padres del mismo tipo de objeto, el objeto compartido se puede contar varias veces dando como resultado un recuento impreciso.

Por ejemplo, supongamos que se produce una pérdida de 1.000 dólares y esa pérdida se ha compartido entre dos eventos de pérdida diferentes para el mismo riesgo identificado. Figura 1 muestra las asociaciones que existirían entre los objetos Riesgo, Evento de pérdida e Impacto de pérdida:

*Figura 1. Asociación de objetos Evento de pérdida padre-hijo*

![La figura muestra un objeto padre que tiene dos objetos hijo de evento de pérdida. Están asociados a un objeto de impacto de pérdida por 1000 $.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_shared_objects_7.jpg)

Si intenta agregar valores para el Impacto de pérdida a nivel Riesgo utilizando la siguiente función:

El valor de retorno será 2000,00 (en lugar de 1000,00), porque Impacto de pérdida-1 se contará una dos veces.

Riesgo-1 > Evento de pérdida-1 > Impacto de pérdida-1

Riesgo-1 > Evento de pérdida-2 > Impacto de pérdida-1

Para obtener un recuento distinto de objetos compartidos, utilice la siguiente fórmula:

```
[average(Loss Impacts for Risk)] * [count (distinct Loss Impacts for Risk)]
```

el valor de retorno será 1000,00 ya que Impacto de pérdida-1 se contará una vez.

También, se puede expresar la fórmula matemáticamente como se muestra en el siguiente ejemplo:

```
average * distinct_count = total/count * distinct_count = 
       total * distinct_count/count
```

Así, si está intentando totalizar los impactos de pérdida para un riesgo como vemos en el ejemplo anterior, se debe realizar un total en el impacto repetido y, a continuación, multiplicar por 1/2 para factorizar las repeticiones.

### Creación de un informe de agregación para objetos compartidos

`Guía del creador de informes › Trabajar con objetos compartidos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-creating-aggregation-report-shared)

Este procedimiento crea un informe de ejemplo que cuenta el número de controles **Ineficaz** y **Efectivo** exclusivos bajo una entidad empresarial.

#### Acerca de esta tarea

Figura 1 muestra la asociación entre objetos Entity, Process, Risk y Control en este escenario. Puesto que los objetos Control hijo pueden tener varios objetos Riesgo padre, es importante que el valor de un control se cuente solo una vez en el informe.

*Figura 1. Asociaciones de control padre-hijo*

![Diagrama de flujo que muestra la relación entre entidades, procesos, riesgos y controles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_shared_objects_6.jpg)

#### Procedimiento

1. Cree un nuevo informe de lista.
2. Cree una consulta hijo:

   1. En **Explorador de consultas**, abra la consulta.
   2. En el panel **Propiedades** en **Varios**, establezca el nombre en **listMain**.
   3. Vuelva a **Explorador de consultas** y seleccione la carpeta de nivel superior **Consultas**.
   4. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg).
   5. Arrastre un objeto **Query** junto a la consulta **listMain** .
   6. Seleccione el nuevo objeto de consulta.
   7. En el panel **Propiedades** bajo **Varios**, establezca **Nombre** en **listMain1**.
3. Para añadir otro objeto de consulta hijo al objeto de consulta que ha creado en el paso anterior, realice los siguientes pasos.

   1. Arrastre un objeto **Consulta** a la consulta **listMain1** .
   2. Seleccione el nuevo objeto de consulta.
   3. En el panel **Propiedades** bajo **Varios**, establezca **Nombre** en **listMain2**.
4. Para añadir elementos de consulta a la consulta **listMain2** que ha creado en el paso anterior, realice los pasos siguientes.

   1. Seleccione la consulta **listMain2** para abrirla.
   2. Pulse la pestaña ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg) **Origen** en el panel **Objetos insertables** .
   3. Arrastre los siguientes elementos de consulta al recuadro **Elementos de datos** :

      - `DEFAULT|DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]| [SOXBUSENTITY_GPC]|[PEN_NAME00]`
      - `DEFAULT|DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]| [SOXBUSENTITY_GPC]|ID_FIELDS|[PEN_ENTITY_ID]`
      - `DEFAULT|DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER| [SOXBUSENTITY_GPC]| [SOXBUSENTITY_GPC]|ID_FIELDS| [GEN_REPORTING_PERIOD_ID]`
      - `DEFAULT|DEFAULT_REL|GRC_OBJECTS|SOXCONTROL_FOLDER|[SOXCONTROL]| ID_FIELDS| [CN_CONTROL_ID]`
      - `DEFAULT|DEFAULT_REL|GRC_OBJECTS|SOXCONTROL_FOLDER|[SOXCONTROL] | ENUMERATION_FIELDS| OPERATING_EFFECTIVENES (ENUMERATION)| [CN_OPERATING_EFFECTIVENES_ID]`
5. Añada filtros al informe:

   1. Seleccione el elemento de datos `[GEN_REPORTING_PERIOD_ID]` que acaba de añadir y arrástrelo al panel **Filtros de detalles** .
   2. En el panel **Definición de expresión** , defina la expresión de filtro:

      ```
      [GEN_REPORTING_PERIOD_ID] = -1 
      ```
   3. Pulse **Aceptar**.
   4. Seleccione el elemento de datos `[CN_CONTROL_ID]` que acaba de añadir y arrástrelo al panel **Filtros de detalles** .
   5. En el panel **Definición de expresión** , defina la expresión de filtro:

      ```
      [CN_CONTROL_ID] is not null
      ```
   6. Pulse el icono **Validar** ![Icono Validar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) para validar la expresión y, a continuación, pulse **Aceptar**.
6. Para añadir un elemento de datos al objeto de consulta, complete los pasos siguientes.

   1. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg).
   2. Arrastre un objeto **Elemento de datos** al recuadro **Elementos de datos** de la consulta.
   3. En el panel **Definición de expresión** del elemento de datos, especifique la expresión siguiente:

      ```
      IF([CN_OPERATING_EFFECTIVENES_ID] = 
         #$SOXCONTROL_OPERATING_EFFECTIVENES_DEFINITION_MAP
            {"Ineffective"}#)THEN ([CN_CONTROL_ID])ELSE (NULL)
      ```
   4. Pulse el icono **Validar** ![Icono Validar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) para validar la expresión y, a continuación, pulse **Aceptar**.
7. En el panel **Propiedades** del elemento de datos, realice los pasos siguientes.

   1. Cambie la propiedad **Nombre** del elemento de datos a `Ineffective Control`.
   2. Cambie la propiedad **Función de agregación** a **Ninguno**.
8. Para ver los datos tabulares, pulse **Ejecutar** > **Ver datos tabulares**.
9. Abra el asunto de consulta **listMain1** en **Explorador de consultas**. Para hacer un recuento del número de controles distintos de cada entidad, realice los siguientes pasos.

   1. Pulse la pestaña **Origen** ![Icono de origen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-model.jpg) y arrastre y suelte el elemento de consulta [`PEN_NAME00]` en el panel **Elementos de datos** .
   2. En el panel **Propiedades** bajo **Elemento de datos**, establezca **Función de agregación** en **Ninguno**.
   3. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg)y arrastre un objeto **Elemento de datos** al panel **Elementos de datos** .
   4. En el recuadro **Definición de expresión** , especifique la expresión siguiente para contar el número total de controles distintos:

      ```
      count(distinct [listMain2].[CN_CONTROL_ID] for [listMain2].[PEN_NAME00])
      ```
   5. Pulse el icono **Validar** ![Icono Validar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) para validar la expresión y, a continuación, pulse **Aceptar**.
10. En el panel **Propiedades** para el elemento de datos, realice los pasos siguientes.

    1. En **Elemento de datos** , establezca la propiedad **Nombre** en **Recuento de controles**.
    2. Establezca la propiedad **Función de agregación** en **Ninguno**.
    3. Establezca la propiedad **Función de agregación de resumen** en **Ninguno**.
11. Para hacer un recuento del número de controles no efectivos de cada entidad, realice los siguientes pasos.

    1. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) y arrastre un objeto **Elemento de datos** al panel **Elementos de datos** .
    2. En el recuadro **Definición de expresión** , especifique la expresión siguiente para contar el número total de controles distintos:

       ```
       count(distinct [listMain2].[Ineffective Control] for 
        [listMain2].[PEN_NAME00])
       ```
    3. Pulse el icono **Validar** ![Icono Validar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) para validar la expresión y, a continuación, pulse **Aceptar**.
12. En el panel **Propiedades** para el elemento de datos, realice los pasos siguientes.

    1. En **Elemento de datos** establezca la propiedad **Nombre** en `Count of Ineffective Controls`.
    2. Establezca la propiedad **Función de agregación** en **Ninguno**.
    3. Establezca la propiedad **Función de agregación de resumen** en **Ninguno**.
13. Ejecute el modelo tabular en este nivel.
14. Abra el asunto de consulta **listMain** en el **Explorador de consultas** y realice los pasos siguientes.

    1. Arrastre y suelte los siguientes elementos de consulta en el panel **Elementos de datos** :

       - `[PEN_NAME00]`
       - `[Count of Controls]`
       - `[Count of Ineffective Controls]`
    2. En el panel **Propiedades** para cada uno de los controles anteriores, establezca **Función de agregación** en **Ninguno**.
15. En **Explorador de páginas**, vaya a **Page1** y realice los pasos siguientes.

    1. Pulse la pestaña **Elementos de datos** .
    2. Arrastre los objetos siguientes desde la consulta **listMain** a la lista:

       - `[PEN_NAME00]`
       - `[Count of Controls]`
       - `[Count of Ineffective Controls]`
16. Añada una solicitud de entidad empresarial tal como se describe en [Añadir una solicitud de entidad empresarial](#adición-de-una-solicitud-de-entidad-de-negocios).
17. Ejecute el informe.

#### Resultados

En este ejemplo, existían cuatro riesgos que compartían dos controles. Si no se hubiera utilizado este método para calcular el recuento de controles, el valor se habría devuelto de manera incorrecta como 4.

### Recuento de objetos compartidos en informes de gráfico

`Guía del creador de informes › Trabajar con objetos compartidos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-counting-shared-in-chart-reports)

Tendrá que llevar a cabo algunas tareas adicionales al contar el número de objetos bajo una entidad en un gráfico cuando se comparten algunos objetos. Por ejemplo, es posible que desee crear informes sobre los controles totales bajo una entidad de negocios cuando algunos controles tengan varios riesgos padre.

#### Procedimiento

1. Cree un informe de gráfico y complete los pasos siguientes.

   1. Seleccione la agrupación de gráficos **Columna** .
   2. Seleccione el tipo de gráfico **Columna** .
   3. Pulse **Aceptar**.
2. Crear una página de solicitud siguiendo las instrucciones de [Creación de una página de solicitud](#creación-de-una-página-de-solicitudes)
3. Añada una solicitud de entidad de negocios tal como se describe en [Adición de una solicitud de entidad de negocios](#adición-de-una-solicitud-de-entidad-de-negocios).
4. En el Explorador de consultas, seleccione **Query1** y realice los pasos siguientes.

   1. En el panel **Propiedades** en **Varios**, establezca el **Nombre** en **graphMain**.
   2. Arrastre los siguientes elementos de consulta al panel **Elementos de datos** :

      - ```
        DEFAULT|DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
          [SOXBUSENTITY_GPC]|[CEN_NAME00]
        ```
      - ```
        DEFAULT|DEFAULT_REL|GRC_OBJECTS|SOXBUSENTITY_FOLDER| 
          [SOXBUSENTITY_GPC]|ID_FIELDS|[CEN_ENTITY_ID]
        ```
      - ```
        DEFAULT|DEFAULT_REL|GRC_OBJECTS|SOXCONTROL_FOLDER|
          [SOXCONTROL]| ID_FIELDS|[CN_CONTROL_ID]
        ```
5. Arrastre y suelte los siguientes elementos de consulta en varias secciones del gráfico:

   - `Categories (x-axis) - [CEN_NAME00]`
   - `Measures (y-axis) - [CN_CONTROL_ID]`
6. En el Explorador de consultas, seleccione la consulta gráficoPrincipal y realice los siguientes pasos.

   1. Seleccionar `CN_CONTROL_ID.`
   2. En el panel **Propiedades** bajo la categoría Elemento de datos, establezca la propiedad **Función de agregación** en **Recuento diferenciado**.
   3. Establezca la propiedad **Función de agregación de resumen** en **Automático**.
7. Efectúe una doble pulsación en el título y establezca el valor en **Recuento de control**.
8. Abra la **Títulos de eje** y realice los pasos siguientes.

   1. Seleccione el título del eje x y en el panel **Propiedades** .
   2. En **General** , establezca la propiedad **Título predeterminado** en **No**.
   3. Efectúe una doble pulsación en el título del eje y establezca el valor en **Entidad de negocios**.
   4. Repita los pasos a-c para el eje y y establezca el valor en **Recuento de control**.
9. Seleccione todo el gráfico y, en el panel **Propiedades** bajo la categoría **Anotaciones de gráfico** , establezca la propiedad **Leyenda** en **Ocultar**.
10. Ejecute el informe.

#### Resultados

El informe muestra los resultados del recuento de control que ha filtrado la entidad de negocios que fue seleccionada. Debe elegir una entidad de negocios donde pueda verificar los valores del gráfico.

### Listado de objetos compartidos en los informes de lista

`Guía del creador de informes › Trabajar con objetos compartidos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-listing-shared-in-list-reports)

Puede listar objetos compartidos en informes de lista.

Hay una propiedad denominada **Agrupación automática y resumen** conectada a todos los asuntos de consulta que ayuda a eliminar o mostrar registros duplicados. Dispone de las siguientes opciones en la propiedad:

- **Sí**

  Si desea visualizar cada uno de los controles solo una vez sin importar cuántos riesgos padre tiene. Este es el valor predeterminado.

- **No**

  Si desea visualizar un control una vez para cada objeto de riesgo al que está asociado. Así, si un control tiene tres riesgos padre, el control se visualizará tres veces.

Dependiendo de cómo haya escrito el informe y si su objetivo es mostrar los objetos compartidos, tendrá que ajustar este valor en su asunto de consulta.

## Trabajar con objetos recursivos

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-working-recursive-objects)

Para ver todos los elementos conectados a los distintos niveles de jerarquía recursiva del informe, hay una construcción denominada, triángulo de elaboración de informes.

Esta información solo se aplica a modelos de entorno estándares, no a modelos de entorno básicos.

Para obtener información sobre cómo se manejan los objetos recursivos en los modelos de entorno básicos, consulte [Modelos de entorno](#modelos-de-entorno).

### Triángulos de elaboración de informes

En [Trabajar con entidades de negocios](#trabajar-con-entidades-de-negocios), se ha tratado el trabajo con objetos de entidad de negocios recursivos. Sin embargo, hay otros tres objetos recursivos en IBM OpenPages que existirán en el sistema si tiene las soluciones adecuadas:

- Subproceso
- Submandato
- Subcuenta

Normalmente, desde el punto de vista de un autor de informe, quiere ver todos los elementos conectados a los diferentes niveles de jerarquía recursiva del informe. Para ello, debe crear una relación en el espacio de nombres donde un objeto tiene más de un padre, pero esto no está permitido.

Para solucionar este problema, hemos creado una construcción llamada triángulo de elaboración de informes. Se pueden crear tres tipos de triángulo, como vemos en las siguientes figuras:

*Figura 1. Proceso, Subproceso, Triángulo de riesgo*

![Diagrama de flujo que muestra cómo una entidad empresarial se relaciona con un proceso, subproceso y riesgo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_triangle_1.jpg)

*Figura 2. Mandato, Submandato, Triángulo de requisito*

![Diagrama de flujo que muestra cómo se relaciona una entidad empresarial con un mandato, submandato y requisito](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_triangle_3.jpg)

*Figura 3. Cuenta, Subcuenta, Triángulo de declaración*

![Diagrama de flujo que muestra cómo se relaciona una entidad empresarial con una cuenta, subcuenta y aserción](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_triangle_2.jpg)

El factor común aquí es que el objeto recursivo es el centro del triángulo. Por lo tanto, creando un triángulo cada vez que trata con un objeto recursivo, el autor de informe no tiene que escribir un código aparte para gestionar el caso donde los datos están adjuntos al objeto principal y el caso donde los datos están adjuntos al subobjeto.

Si el triángulo no se admite en el espacio de nombres que está utilizando, siempre puede unir los resultados de dos espacios de nombres para conseguir los mismos valores que si existiera el triángulo.

La publicación *IBM OpenPages Guía del administrador* describe cómo crear un triángulo. La única advertencia es que cada vez que cree un nuevo triángulo o añada uno a otro espacio de nombres, debe ejecutar un script SQL que habilite la relación de triángulo específica y, a continuación, debe volver a crear el esquema.

## Internacionalización y localización

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-internationalization-localization)

La aplicación IBM OpenPages® está totalmente internacionalizada y localizada.

### Conversión de datos

`Guía del creador de informes › Internacionalización y localización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=localization-data-translation)

IBM OpenPages® contiene datos estáticos y de aplicación (instancia).

Normalmente, todos los datos estáticos se convierten a través de un entorno de elaboración de informes o por medio del informe mientras que los datos de aplicación no se convierten, con la excepción de las series enumeradas.

El idioma en el que un usuario ve estos datos se basa en el valor de entorno local del usuario que se establece en OpenPages cuando se crea el usuario o se modifica posteriormente. Esto es lo que determina cómo se traducirá el informe.

Es posible establecer el entorno local del usuario en IBM® Cognos® Analytics, lo que lo separaría del entorno local establecido en la aplicación OpenPages . Normalmente lo hace el autor de informes para dejar a un usuario determinado con un entorno local en la aplicación OpenPages y otro entorno local cuando se utilizan informes. Consulte [Establecimiento del entorno local en IBM Cognos Analytics](#configuración-del-entorno-local-en-ibm-cognos-analytics).

#### Datos estáticos

`Guía del creador de informes › Internacionalización y localización › Conversión de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=translation-static-data)

Existen cuatro categorías de datos estáticos: etiquetas dinámicas, campos de texto fijos, texto de botón y texto en solicitudes.

- **Datos de etiqueta dinámica**

  Incluyen el texto de etiqueta visualizado para tipos de objeto (como entidad de negocios, cuenta, control, etc.) y nombres de campo de objeto (como Eficiencia operativa, etc.) así como botones, etiquetas, cuadros de texto, cabeceras de columna, etc. Estos datos (y las traducciones) se crean cuando los campos se definen en la aplicación IBM OpenPages®.

- **Datos de campo de texto fijo**

  Incluyen cualquier serie de texto fijo que ha añadido el autor del informe al informe utilizando un objeto de texto.

- **Texto de botón**

  Incluye el texto mostrado por el botón de solicitud o los botones en la página de solicitudes.

- **Texto estático en solicitudes**

  Incluye cualquier texto añadido a una solicitud (como Todo) o una solicitud que es todo texto estático.

##### Traducción de datos de etiqueta dinámicos

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos estáticos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-dynamic-label)

Al crear un informe utilizando el lenguaje de diseño de informes, tanto el panel **Objetos insertables** como la ventana de diseño de informe muestran los nombres de objeto y campo utilizando el nombre interno del sistema.

Cuando ejecuta el informe, el texto estático se visualiza en el entorno local del usuario definido en IBM OpenPages®:

- Si la configuración regional del usuario se establece en Idioma del diseño de informe (RDL), los títulos de las columnas están en RDL, pero los datos están en inglés.
- Si el entorno local del usuario se establece en inglés de Estados Unidos en la aplicación OpenPages , cuando se ejecuta el informe, los títulos de columna se traducen al inglés de Estados Unidos.
- Si el entorno local del usuario se establece en español en la aplicación OpenPages , cuando el informe se ejecuta en el entorno local español, los títulos de columna se traducen al español.

Estos ejemplos demuestran por qué utilizamos Report Design Language como idioma predeterminado para diseñar el informe y cómo el sistema traduce internamente los títulos estáticos basándose en las definiciones cargadas en la aplicación OpenPages . Esto ahorra tiempo y esfuerzo al autor de informe si se están creando informes para una compañía con múltiples configuraciones regionales.

Los datos de aplicación entrados por el usuario no se traducen. Si un usuario español ha entrado los datos, debe ver las descripciones en español para cada configuración regional porque los datos de aplicación no se traducen por configuración regional.

##### Uso de una variable de condición para traducir datos de campo de texto fijo

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos estáticos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=sd-using-condition-variable-translate-fixed-text-field-data)

Los objetos de texto (títulos de informe, subtítulos y etiquetas) que añade a un informe tendrán que localizarse. Puede utilizar variables de condición para realizar esta traducción a texto estático. Para hacer esto, primero se debe crear una variable de condición.

###### Procedimiento

1. Abra el menú **Explorador de condiciones** y seleccione **Variables**.
2. Arrastre y suelte un objeto **Variable de idioma del informe** de la caja de herramientas en el recuadro **Variables** .

   Se abre el cuadro de diálogo **Idiomas**.
3. Complete los pasos siguientes.

   1. Seleccione los idiomas para los que necesita que esté localizado el texto. La lista siguiente muestra los idiomas soportados en OpenPages®:

      - Inglés (Reino Unido)
      - Inglés (Estados Unidos)
      - Francés (Francia)
      - Alemán (Alemania)
      - Italiano (Italia)
      - Japonés (Japón)
      - Español
   2. Pulse **Aceptar**.
4. En el panel **Propiedades** , especifique el nombre de la variable en **Nombre, campo**. Utilice **Localización** como nombre.
5. Para traducir un campo de texto a un idioma específico del informe, seleccione una de las etiquetas que necesite traducción. En este ejemplo, se ha seleccionado el título de informe **Lista de prueba**.
6. En el panel **Propiedades** del elemento de texto seleccionado, bajo el grupo **Condicional** , en la propiedad **Variable de origen de texto** , seleccione la variable **Localización** que acaba de crear.
7. En **Explorador de condiciones**, seleccione uno de los idiomas bajo la variable de idioma.
8. En el panel **Propiedades** bajo **Origen de texto**, realice los pasos siguientes.

   1. En la propiedad **Texto** , especifique la serie localizada de la etiqueta, por ejemplo, `Prueba Lista`.
   2. Pulse **Aceptar**.
   3. Repita los pasos 3-4 y defina la serie de texto para todos los idiomas.
   4. Cuando todas las series de idiomas estén definidas, seleccione **Ninguna variable** en **Explorador de condiciones**.
9. Para ver el informe, realice los siguientes pasos.

   1. Inicie sesión utilizando un usuario que tiene la configuración regional establecida en español (si todavía no ha iniciado sesión con un usuario con configuración regional de español).
   2. Ejecute el informe.

###### Resultados

El título del informe aparece ahora traducido.

Se puede seguir esta metodología con cualquier etiqueta de texto del informe. La variable de condición que se ha creado se puede volver a utilizar para cada objeto que tenga que traducirse.

##### Traducción de un texto de botón

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos estáticos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-button-text)

Generalmente, los botones de texto en la página de solicitudes no requieren localización porque la gestiona la herramienta de elaboración de informes. Por otro lado, si crea su propio botón de solicitud y necesita localizar su texto, siga este procedimiento.

###### Procedimiento

1. Identifique el botón que desea localizar.
2. Seleccione un **Elemento de texto** en la caja de herramientas y complete los pasos siguientes.

   1. Suelte el **Elemento de texto** en el botón.
   2. Especifique **Actualizar línea de negocio** como serie de texto predeterminada.
   3. En el panel de propiedades de **Elemento de texto**, especifique la variable de condición **Localización** como la propiedad **Variable de origen de texto** .
3. En la **Explorador de condiciones**, realice los pasos siguientes.

   1. Mientras **Elemento de texto** está seleccionado, seleccione cada idioma en la variable **Localización** que desee especificar.
   2. Especifique la serie de texto adecuada en la propiedad **Texto** .
   3. Repítalo para cada idioma que desea especificar.
4. Para ver el informe, realice los siguientes pasos.

   1. Inicie sesión utilizando un usuario cuya configuración regional es diferente del usuario actual.
   2. Ejecute el informe.

##### Conversión de texto estático en solicitudes

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos estáticos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-static-text-in-prompts)

Es posible que tenga que convertir texto estático en solicitudes para la configuración regional del usuario.

###### Procedimiento

1. Identifique la solicitud que desea localizar dentro del texto estático. En este ejemplo, localizaremos el texto estático en la solicitud **Región**.
2. Seleccione la solicitud **Región** y realice los pasos siguientes.

   1. Seleccione la propiedad **Opciones estáticas** en el panel **Propiedades** .
   2. En la lista **Variables** , seleccione **Localización**, la variable de condición que se ha creado para traducir texto a otros idiomas.
   3. En la lista **Valor** , seleccione **Inglés (Estados Unidos)**.
   4. Utilizando el icono **Añadir** , especifique los valores de la lista de selección estática para inglés.
   5. Seleccione **Español** en la lista **Valor** y especifique los valores en español utilizando el icono **Editar** .
   6. Pulse **Correcto** para guardar los valores.
3. Para ver el informe, realice los siguientes pasos.

   1. Inicie sesión utilizando un usuario que tenga un entorno local predeterminado establecido en **Español** (si todavía no ha iniciado sesión con un usuario de entorno local español).
   2. Ejecute el informe.

###### Resultados

El texto de la solicitud aparece traducido a español.

Cuando la configuración regional se configura en **Inglés (Estados Unidos)**, la solicitud Región aparece con los valores en inglés.

#### Datos de aplicación

`Guía del creador de informes › Internacionalización y localización › Conversión de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=translation-application-data)

Hay cuatro categorías de datos de aplicación: datos entrados por el usuario, series enumeradas, campos de moneda y campos de fecha.

- **Datos especificados por el usuario**

  Esto incluye todos los datos especificados por los usuarios. No se traduce.

- **Datos de serie enumerada**

  Esto incluye todos los datos seleccionados por usuario de una lista de valores de serie enumerada. Estos datos (y las conversiones) se crean cuando la lista de series enumeradas se define en la aplicación IBM OpenPages® .

- **Campos de moneda**

  Esto incluye datos configurados como moneda.

- **Campos de fecha**

  Esto incluye datos que tienen formato de fecha o de fecha y hora.

##### Traducción de series enumeradas de valor único

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-single-valued-enumerated-strings)

Un campo de serie enumerada de valor único permite a un usuario seleccionar un solo valor de una lista. Por ejemplo, el tipo de objeto de riesgo tiene un campo de serie enumerada denominado impacto inherente desde el que solo se puede seleccionar un valor de la lista.

En un campo de serie enumerada de valor único, la serie se traduce dentro del asunto de consulta basándose en la configuración regional del usuario.

Cuando inicia sesión en la aplicación con la configuración regional del usuario establecida en español, aparece el mismo campo.

Cuando la serie enumerada de impacto inherente se ha definido a través de la aplicación IBM OpenPages® , los valores en español para la serie también se han especificado en el sistema.

###### Estructura de carpetas del entorno para enumeraciones de valor único

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación › Traducción de series enumeradas de valor único` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=strings-framework-folder-structure-single-value-enumerations)

Cada asunto de consulta para un objeto contiene una carpeta llamada ENUMERATION_FIELDS con las series enumeradas para ese objeto particular.

El ejemplo de Figura 1 muestra el objeto SOXRisk y la enumeración INHERENT_IMPACT que es de un solo valor.

*Figura 1. Estructura de carpetas SOXRisk*

![Jerarquía de carpetas en la carpeta SOXRisk](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_risk_inherent_inpact.jpg)

###### Definiciones de campo para enumeraciones de valor único

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación › Traducción de series enumeradas de valor único` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=strings-field-definitions-single-value-enumerations)

Cada enumeración de valor único tiene los siguientes elementos de consulta: `<field_name>_SYSTEM_NAME`, `<field_name>`y `<field_name>_ID`.

- **`<field_name>_SYSTEM_NAME`**

  Contiene los valores de serie en el Idioma del diseño de informe.

- **`<field_name>`**

  Contiene los valores de serie basados en el valor de entorno local de la aplicación IBM OpenPages® del usuario que ha iniciado la sesión.

- **`<field_name>_ID`**

  Contiene el identificador numérico para un valor de serie enumerada. No se garantiza que este identificador sea el mismo en todas las instalaciones.

Cuando se visualiza el valor en un informe, se debe utilizar siempre `<field_name>`. Cuando filtre por este valor, utilice el campo `<field_name>_ID` porque está indexado.

La Figura 1 muestra las enumeraciones de impacto inherente en el entorno local inglés de EE.UU. Tanto el nombre del sistema como el nombre de la configuración regional son el mismo porque no se han hecho cambios en el valor inglés cuando se cargó el elemento de datos en el sistema. Es posible que el nombre del sistema (en RDL) y el nombre inglés sean diferentes.

*Figura 1. Impacto inherente en inglés de EE.UU*

![Impacto inherente en inglés de EE.UU](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Single_Value_Enumeration_US-English.jpg)

La Figura 2 muestra las enumeraciones de impacto inherente en el entorno local español. El nombre del sistema permanece en RDL mientras el nombre de configuración regional se traduce a español.

*Figura 2. Impacto inherente en español*

![Impacto inherente en español](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Single_Value_Enumeration_spanish.jpg)

##### Traducción de series enumeradas multivalor

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-multivalued-enumerated-strings)

Un campo de serie enumerada multivalor permite a un usuario seleccionar varios valores de serie de una lista.

En un campo de serie enumerada multivalor, la serie se traduce dentro del asunto de consulta en base a la configuración regional del usuario.

Cuando la serie enumerada de dominio se ha definido a través de la aplicación IBM OpenPages® , los valores en español de la serie se han especificado en el sistema y, por lo tanto, los usuarios verán los valores traducidos en el entorno local español.

###### Estructura de carpetas del entorno para enumeraciones multivalor

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación › Traducción de series enumeradas multivalor` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=strings-framework-folder-structure-multivalued-enumerations)

La estructura de carpetas para enumeraciones contiene enumeraciones de un único valor o multi valor.

Figura 1 muestra la carpeta de enumeraciones para el objeto SOXProcess expandido con la carpeta de dominio abierta para mostrar sus campos. El campo de dominio es un campo multivalor.

*Figura 1. Estructura de carpetas*

![Jerarquía de carpetas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_multivalued_folder_structure.jpg)

###### Definiciones de campo para enumeraciones multivalor

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación › Traducción de series enumeradas multivalor` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=strings-field-definitions-multivalued-enumerations)

Cada enumeración multivalor tiene los siguientes elementos de consulta: `<field_name>_SYSTEM_NAME`, `<field_name>`, `<field_name>_ID`, `<field_name>_SYSTEM_LIST`y `<field_name>_LIST`.

- **`<field_name>_SYSTEM_NAME`**

  Contiene los valores de serie en el Idioma del diseño de informe. Habrá un registro para cada enumeración seleccionada. Esto devuelve un registro para cada valor seleccionado por el usuario.

- **`<field_name>`**

  Contiene los valores de serie traducidos basados en el valor de entorno local de la aplicación IBM OpenPages® del usuario. Esto devuelve un registro para cada valor seleccionado por el usuario.

- **`<field_name>_ID`**

  Contiene el identificador numérico para un valor de serie enumerada. No se garantiza que este identificador sea el mismo en todas las instalaciones. Se devuelve como una lista separada por una barra vertical (|).

- **`<field_name>_SYSTEM_LIST`**

  Contiene una lista separada por comas de los valores de serie basados en el Idioma de diseño de informe.

- **`<field_name>_LIST`**

  Contiene una lista separada por comas de los valores de serie basados en el valor de configuración regional del usuario.

Para obtener una lista separada por comas de los valores traducidos de la serie, el autor del informe debe seleccionar el campo `<field_name>_LIST` y utilizarlo en el informe. Este es el mejor campo que se puede utilizar para visualizar el valor de una serie enumerada multivalor.

La Figura 1 muestra los campos de dominio, en el entorno local inglés de Estados Unidos, para los riesgos que se cargan en el sistema. Solo devuelve un registro por riesgo cuando se utiliza cualquiera de los tres campos agregados.

*Figura 1. Campos multivalor de dominio en inglés*

![Campos multivalor de dominio en inglés](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_multi-valued_english.jpg)

Cuando incluye los campos RI_DOMAIN_SYSTEM_NAME o RI_DOMAIN, verá el siguiente resultado (se coloca un filtro en el informe para un riesgo que tenía varios valores de dominio):

*Figura 2. Todos los campos de dominio en inglés*

![Todos los campos de dominio en inglés](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_multi-valued_single_fields_english.jpg)

Estos campos devuelven un único registro para cada valor que ha seleccionado el usuario.

Estos dos campos se utilizan para el filtrado y no se muestran datos al usuario debido a los registros duplicados. El filtro típico utilizado para el dominio de riesgo se parecería a:

```
[DEFAULT_REL].[SOXRISK].[RI_DOMAIN] in ?Domain? or ?Domain? = 'All'
```

Este filtro se utiliza junto con una solicitud de selección múltiple para filtrar valores de dominio. También incluye un valor para **Todos** que se añade como valor estático a la solicitud.

Cuando cambia a un usuario con configuración regional de español, ve lo siguiente para los campos agregados del ID de dominio de riesgo, Lista del sistema de dominio de riesgo y Lista de dominio de riesgo:

*Figura 3. Campos multivalor de dominio en español*

![Campos multivalor de dominio en español](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_multi-valued_spanish_2.jpg)

Vemos que los valores de ID de dominio de riesgo y los valores de Lista de sistemas de dominio de riesgo son idénticos a los valores vistos en Figura 1. La Lista de dominio de riesgo y los títulos de las cabeceras de campos están ahora en la configuración regional en español del usuario.

El ejemplo de [Figura 1](#estructura-de-carpetas-del-entorno-para-enumeraciones-de-valor-único) muestra el objeto SOXRisk y la enumeración de impacto inherente que es de un solo valor. Figura 4 muestra lo que vemos cuando añadimos el nombre del sistema de dominio de riesgo y el dominio de riesgo al informe (se ha añadido un filtro al informe para un riesgo con varios valores de dominio):

*Figura 4. Todos los campos de dominio en español*

![Todos los campos de dominio en español](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_multi-valued_single_fields_spanish.jpg)

Una vez más, ve que estos campos devuelven un único registro para cada valor que ha seleccionado el usuario.

##### Conversión de campos de fecha utilizando formatos de fecha predefinida

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-date-fields-using-predefined-date-formats)

Hay formatos de fecha predefinidos para todos los entornos locales de OpenPages® .

###### Acerca de esta tarea

Se pueden utilizar los formatos descritos aquí, o los autores de informe pueden especificar sus propios formatos personalizados.

La tabla siguiente especifica el formato para cada configuración regional.

**Tabla 1. Formatos de fecha predefinida**

| Entorno local | Formato de fecha formateado |
| --- | --- |
| Inglés (Reino Unido) | dd mmm aaaa |
| Inglés (Estados Unidos) | mmm dd, aaaa |
| Francés (Francia) | dd mmm. aa |
| Alemán (Alemania) | dd.mm.yyyy |
| Italiano (Italia) | dd/mmm/aa |
| Japonés (Japón) | aaaa/mm/dd |
| Español (España) | dd/mm/aaaa |

###### Procedimiento

1. En este ejemplo, vamos a localizar la fecha de creación de riesgo. Cree un informe simple mostrando el nombre del riesgo, la descripción del riesgo y la fecha de creación del riesgo.

   El informe debería ser similar al siguiente ejemplo:

   ![Informe de lista, incluyendo el nombre del riesgo, la descripción del riesgo y la fecha de creación del riesgo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_date_format_1.jpg)
2. Seleccione el campo de fecha **FECHA_CREACIÓN_RÍO** y realice los pasos siguientes.

   1. Pulse con el botón derecho del ratón y seleccione **Estilo** > **Formato de datos**.
   2. Establezca **Tipo de formato** en **Fecha** , pero no establezca ninguna de las propiedades.
   3. Pulse **Aceptar**.
3. Guarde el informe.

###### Resultados

Estableciendo el campo para que sea un campo de fecha sin propiedades de formato, la fecha tiene el formato predeterminado para la configuración regional de inglés de EE.UU como se ve en la tabla al comienzo de este tema.

Ahora ejecute el informe con un usuario que tiene una configuración regional de español y la fecha tiene el formato predeterminado para la configuración regional de español como se ve en la tabla al comienzo de este tema.

##### Conversión de campos de fecha utilizando formatos de fecha personalizados

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-date-fields-using-custom-date-formats)

Para crear un formato de fecha personalizado para varios idiomas, tendrá que localizar el campo de fecha con un formato condicional y establecer los formatos para cada idioma.

###### Procedimiento

1. En este ejemplo, vamos a localizar la fecha de creación de riesgo para tener formatos personalizados para configuraciones regionales de alemán y francés. Cree un informe simple mostrando el nombre del riesgo, la descripción del riesgo y la fecha de creación del riesgo.
2. Seleccione el campo de datos **FECHA_CREACIÓN_RÍO** .
3. En el panel **Propiedades** , bajo la cabecera **Condicional** , establezca **Variable de estilo** en la variable condicional Localización.
4. En la **Explorador de condiciones** seleccione **Alemania** que está presente bajo la variable **Localización** .
5. Pulse con el botón derecho del ratón y seleccione **Estilo** > **Formato de datos**.
6. En la pantalla Formato de datos, defina las siguientes propiedades:

   1. Establezca **Tipo de formato** en **Fecha**.
   2. Establezca **Separador de fecha** en un punto (.).
   3. Establezca **Orden de fecha** en **Día, Mes, Año**.
   4. Establezca **Mostrar años** en **Mostrar siglo**.
   5. Establezca **Mostrar meses** en **Nombre abreviado**.
   6. Establezca **Mostrar días** en **Dos dígitos**.
7. Pulse **Aceptar**.
8. En la **Explorador de condiciones** seleccione **Francés** que está presente bajo la variable **Localización** .
9. Pulse con el botón derecho del ratón y seleccione **Estilo** > **Formato de datos**.
10. En la pantalla Formato de datos, defina las siguientes propiedades:

    1. Establezca **Tipo de formato** en **Fecha**.
    2. Establezca **Separador de fecha** en un punto (.).
    3. Establezca **Orden de fecha** en **Día, Mes, Año**.
    4. Establezca **Mostrar años** en **Mostrar siglo**.
    5. Establezca **Mostrar meses** en **Nombre abreviado**.
    6. Establezca **Mostrar días** en **Dos dígitos**.
11. Pulse **Aceptar**.
12. Guarde el informe.

###### Resultados

Optando por establecer las propiedades del campo de fecha personalizada, la fecha ahora tiene el formato que se ha definido de forma personalizada en lugar del formato de fecha predeterminado para la configuración regional de francés.

Ahora ejecute el informe con un usuario que tiene una configuración regional de alemán y la fecha tiene el formato predeterminado para la configuración regional de alemán en lugar del formato de fecha predeterminado.

##### Conversión de los campos de moneda utilizando formatos predefinidos

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-currency-fields-using-pre-defined-formats)

Existen formatos de moneda predefinidos para todos los entornos locales de IBM OpenPages® .

Siga este procedimiento para utilizar un formato predefinido.

###### Acerca de esta tarea

Se pueden utilizar los formatos descritos aquí, o los autores de informe pueden especificar sus propios formatos personalizados.

La tabla siguiente especifica el formato para cada configuración regional.

**Tabla 1. Formatos de moneda predefinidos**

| Entorno local | Formato de moneda formateado |
| --- | --- |
| Inglés (Reino Unido) | £ NNN,NNN.NN |
| Inglés (Estados Unidos) | $ NNN,NNN.NN |
| Francés (Francia) | NNN NNN,NN € |
| Alemán (Alemania) | NNN.NNN,NN € |
| Italiano (Italia) | NNN.NNN,NN |
| Japonés (Japón) | ¥ NNN,NNN |
| Español (España) | NNN.NNN,NN € |

###### Procedimiento

1. En este ejemplo, vamos a localizar la inclinación al riesgo de entidad. Cree un informe sencillo mostrando el nombre de entidad, la descripción de entidad y toda inclinación al riesgo de entidad para el nivel abuelo.
2. Seleccione el campo de moneda **GEN_RISK_APETE_BA** y realice los pasos siguientes.

   1. Pulse con el botón derecho del ratón y seleccione **Estilo** > **Formato de datos**.
   2. Establezca **Tipo de formato** en **Moneda** , pero no establezca ninguna de las propiedades.
   3. Pulse **Aceptar**.
3. Guarde el informe.

###### Resultados

Estableciendo el campo para que sea un campo de moneda sin propiedades de formato, la moneda tiene el formato predeterminada para la configuración regional de EE.UU como se ve en la tabla al comienzo de este tema.

Ahora, ejecute el informe con un usuario que tiene una configuración regional española.

La moneda tiene ahora el formato predeterminado para la configuración regional española como se ve en la tabla al comienzo de este tema.

##### Conversión de campos de moneda utilizando formatos personalizados

`Guía del creador de informes › Internacionalización y localización › Conversión de datos › Datos de aplicación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=data-translating-currency-fields-using-custom-formats)

Para crear un formato de moneda personalizado para varios idiomas, tendrá que localizar el campo de moneda con un formato condicional y establecer los formatos para cada idioma.

###### Procedimiento

1. En este ejemplo, vamos a localizar la inclinación al riesgo de entidad. Cree un informe sencillo mostrando el nombre de entidad, la descripción de entidad y toda inclinación al riesgo de entidad para el nivel abuelo. Estableceremos el formato para alemán e inglés británico.
2. Seleccione el campo de datos **GEN_RISK_APETE_BA** .
3. En el panel **Propiedades** , bajo la cabecera **Condicional** , establezca **Variable de estilo** en la variable condicional Localización.
4. En la **Explorador de condiciones** seleccione **Alemania** que está presente bajo la variable **Localización** .
5. Pulse con el botón derecho del ratón y seleccione **Estilo** > **Formato de datos**.
6. En la pantalla Formato de datos, defina las siguientes propiedades:

   1. Establezca **Número de posiciones decimales** en **0**.
   2. Establezca **Separador decimal** en una coma (,).
   3. Establezca **Utilizar separador de miles** en **Sí**.
   4. Establezca **Separador de miles** en una coma (,).
7. Pulse **Aceptar**.
8. En la **Explorador de condiciones** seleccione **Inglés del Reino Unido** que está presente bajo la variable **Localización** .
9. Pulse con el botón derecho del ratón y seleccione **Estilo** > **Formato de datos**.
10. En la pantalla Formato de datos, establezca **Posición de símbolo de moneda** en **Fin**.
11. Pulse **Aceptar**.
12. Guarde el informe.

###### Resultados

Optando por establecer las propiedades del campo de moneda personalizada (el separador es una coma), la moneda ahora tiene el formato que se ha definido de forma personalizada en lugar del formato de moneda predeterminado para la configuración regional de alemán.

Ahora ejecute el informe con un usuario que tiene una configuración regional de inglés del Reino Unido.

La moneda ahora tiene el formato personalizado (el símbolo de moneda al final) para la configuración regional de inglés del Reino Unido en lugar del formato de moneda predeterminado.

### Uso de mapas de parámetros con filtros de serie enumerada traducidos

`Guía del creador de informes › Internacionalización y localización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=localization-using-parameter-maps-translated-enumerated-string-filters)

Para crear filtros basados en series enumeradas que sean independientes de las configuraciones regionales, debe utilizar mapas de parámetros. El mapa de parámetro se considera que es la configuración regional RDL así que debe utilizar valores en inglés y realizar la comparación en campos de ID.

En cada una de las definiciones de serie enumerada, se crea un mapa de parámetro correspondiente en el entorno. El mapa de parámetros devuelve el ID para cada valor de serie enumerada pasado a él.

Utilice el siguiente convenio de denominación para mapas de parámetros:

`<Object Name>_<Enumerated String>_DEFINITION_MAP`

Los mapas de parámetro se deben utilizar en todos los filtros que implican enumeraciones que se pueden traducir porque siempre devolverán el mismo ID independientemente de la configuración regional establecida para el usuario.

Por ejemplo, queremos filtrar un valor de solicitud de Alto para el campo de impacto inherente en el objeto SOXRisk. Debemos escribir lo siguiente en un campo de filtro:

```
?Inherent Impact Id? = #$SOXRISK_INHERENT_IMPACT_DEFINITION_MAP("High")#
```

`?Inherent Impact Id?` es el parámetro de solicitud definido en el informe.

## Uso de las funciones de base de datos predefinida

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-predefined-database-functions)

IBM OpenPages® ha expuesto determinadas funciones de base de datos para que las utilicen los autores de informes con el fin de resolver determinados problemas técnicos que son comunes entre entornos.

Este capítulo describe estas funciones y proporciona ejemplos sobre cómo utilizarlas.

### Pasar parámetros

`Guía del creador de informes › Uso de las funciones de base de datos predefinida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-passing-parameters)

En SQL, los parámetros se pasan en posición (el primer valor al primer parámetro, el segundo valor al segundo parámetro, el tercer valor al tercer parámetro y así, sucesivamente).

Por ejemplo, aunque no pueda pasar un valor al tercer parámetro al saltarse el segundo parámetro, puede aprovechar los parámetros con valores predeterminados.

#### Ejemplo

La siguiente función predefinida (se ha encontrado [Obteniendo ID de recurso de vía de acceso de árbol](#obtención-de-los-id-de-recurso-de-vía-de-acceso-de-árbol)) tiene siete parámetros:

`"OP_RPS_AUX.IS_REL_PARENT_CHILD" (P1, P2, P3, P4, P5, P6, P7)`

Los parámetros `P1` y `P2` no tienen valores predeterminados, los parámetros de `P3` a `P7` tienen valores predeterminados.

Por ejemplo, puede especificar valores para los parámetros de `P1` a `P3` y omitir valores para los parámetros de `P4` a `P7`. En este caso, la función utilizaría los valores predeterminados para `P4` a `P7`, como en la siguiente expresión de ejemplo:

```
"OP_RPS_AUX.IS_REL_PARENT_CHILD" ([DEFAULT_REL].[SOXPROCESS].[PR_PROCESS_ID], 
  [DEFAULT_REL].[SOXCONTROL].[CN_CONTROL_ID], -1)
```

Debido a la naturaleza posicional de los parámetros en SQL, si desea utilizar un valor distinto del valor predeterminado para el parámetro *P6* (el valor predeterminado es Y pero queremos N), también tendría que incluir los valores predeterminados para `P4` (que es N) y `P5` (que es Y), como en la siguiente expresión de ejemplo:

```
"OP_RPS_AUX.IS_REL_PARENT_CHILD" ([DEFAULT_REL].[SOXPROCESS].[PR_PROCESS_ID], 
   [DEFAULT_REL].[SOXCONTROL].[CN_CONTROL_ID], -1, 'N', 'Y', 'Y')
```

### Determinación de un ID de tipo de objeto

`Guía del creador de informes › Uso de las funciones de base de datos predefinida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-determining-object-type-id)

Algunas de las funciones de bases de datos predefinidas tienen parámetros que requieren un ID de tipo de objeto (un identificador numérico para el tipo de objeto). Para determinar el valor de ID numérico de un tipo de objeto determinado, puede ejecutar una consulta utilizando una herramienta SQL o crear y ejecutar un informe.

#### Uso de SQL para obtener ID de objeto

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Determinación de un ID de tipo de objeto` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=id-using-sql-obtain-object-ids)

Para obtener una lista de objetos y de ID de tipo de objetos de la base de datos, ejecute un mandato SQL.

Utilizando una herramienta SQL, ejecute el siguiente mandato SQL para obtener una lista de los objetos y los ID de tipo de objeto de la base de datos.

```sql
SELECT
    name,
    assettypeid
FROM
    assettypes
ORDER BY
    name
```

De un entorno a otro, el ID tipo de activo puede ser diferente.

Algunas funciones de SQL son diferentes en IBM® Db2® que en Oracle. Si utiliza una función Oracle que se lista en la tabla siguiente, debe sustituir la función Db2 correspondiente.

**Tabla 1. Correlación de Oracle con las funciones de Db2**

| Sustituir esta función de DB2... | Por esta función de Oracle... |
| --- | --- |
| `INSTR (P1, P2, P3, P4 {CODEUNITS32})` | `INSTR (P1, P2, P3, P4)` |
| `SUBSTR2` | `SUBSTR` |
| `LISTAGG` | `STRAGG` |
| `OP_LENGTH (P1)` | `LENGTH (P1)` |

Donde `P1, P2, P3, P4` representa parámetros.

El siguiente código de ejemplo muestra la función de Oracle `INSTR`:

`INSTR([CEN_FULL_PATH], ’/’, 1, 2)`

Para Db2, sustituiría este código por la función `INSTR` :

`INSTR([CEN_FULL_PATH], ’/’, 1, 2, {CODEUNITS32})`

#### Uso de un informe para obtener ID de objeto

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Determinación de un ID de tipo de objeto` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=id-using-report-obtain-object-ids)

Puede crear un informe y, a continuación, ejecutarlo para obtener los nombres de objeto y los ID de tipo de objeto.

##### Acerca de esta tarea

Por ejemplo, la columna `CONTENT_TYPE_ID` del informe de ejemplo, que se muestra en la figura siguiente, lista todos los ID de tipo de objeto disponibles que podría utilizar. Supongamos que desea utilizar la función OP_RPS_AUX.IS_REL_PARENT_CHILD_PRIM. Los parámetros P1 y P3 de esta función requieren los ID de tipo de objeto del tipo de objeto padre e hijo. Puede utilizar, por ejemplo, 18 en P1 (ID de tipo de objeto RiskAssessment hijo) y 4 en P3 (SOXBusEntity padre).

*Figura 1. Informe de ejemplo mostrando el identificador numérico de tipo de objeto*

![Lista que muestra los ID de tipo de objeto](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/object-type-numeric-identifier.jpg)

##### Procedimiento

1. Cree un nuevo informe de lista.
2. Vaya a `DEFAULT_REL|MISCELLANEOUS`.
3. En el asunto de consulta: `LOCALIZED_CONTENT_TYPES` , arrastre SYSTEM_NAME y CONTENT_TYPE_ID a la plantilla de informe.
4. Cambie el valor del campo **Ordenar** a **Ordenar ascendente** para la cabecera `SYSTEM_NAME` .
5. Ejecute el informe en PDF.
6. Guarde el archivo PDF resultante en la unidad local.

### Determinación de los nombres de tabla de base de datos

`Guía del creador de informes › Uso de las funciones de base de datos predefinida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-determining-database-table-names)

Los nombres de tabla de base de datos tienen convenciones de denominación específicas.

Donde:

`<OBJECT TYPE>` es el nombre del tipo de objeto.

`<ENUMERATION>` es el nombre de un campo de serie enumerada de varios valores.

| Esta convención de denominación... | Indica que es un... |
| --- | --- |
| `RT_<OBJECT TYPE>`<br>(`RT_` con un único guión bajo) | Tabla principal<br>Por ejemplo: `RT_RISKASSESSMENT` |
| `RT_<OBJECT TYPE>_<ENUMERATION>`<br>(`RT_` con un único guión bajo) | Tabla de enumeración multivalor<br>Por ejemplo: `RT_RISKASSESSMENT_DOMAIN` |
| `RT__<OBJECT TYPE>_<OBJECT TYPE>`<br>(`RT__` con un doble guión bajo) | Tabla puente entre 2 tipos de objeto<br>Por ejemplo: `RT__RISKASSESSMENT_PROCESS` |

> **Importante:**

> - La base de datos de Oracle tiene una limitación de 30 caracteres para un nombre de tabla. Algunos nombres de tabla se truncarán.
> - Las tablas 'RT_' deben estar todas en mayúsculas y entre comillas simples, como 'RT_RISK'.
> - Cualquier entrada 'RT_' con más de un guion bajo en una serie es una tabla de selección multivalor. Por ejemplo, en los registros Riesgo, hay un campo de selección multivalor etiquetado **Declaraciones de sentencias financieras**. Esta información de campo se almacena en la tabla RT_RISK_FINANCIAL_STATEMENT_AS.

#### Obtención de una lista de nombres de tabla RT

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Determinación de los nombres de tabla de base de
datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=names-obtaining-list-rt-table)

Puede utilizar una herramienta SQL para obtener una lista de nombres de tabla RT.

Utilice una herramienta SQL para ejecutar el siguiente mandato:

```sql
SELECT
  object_name
FROM
  dba_objects
WHERE
   object_name like 'RT_%'
ORDER BY
  object_name
```

El resultado es la lista de todas las tablas RT de la base de datos.

### Determinación de los nombres de columna de la tabla de base de datos

`Guía del creador de informes › Uso de las funciones de base de datos predefinida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-determining-database-table-column-names)

Hay tres técnicas para determinar los nombres de columna de la tabla de base de datos.

Muchos de los nombres de columna de tabla se pueden determinar por uno de los métodos siguientes:

- Expansión de un asunto de consulta en IBM® Cognos® Analytics -Creación de informes para obtener los nombres de campo
- Abriendo la carpeta de tablas en una herramienta SQL y expandiendo la definición de tabla que está buscando
- Utilización de la función `DESCRIBE <table_name>` en SQL para obtener la definición de tabla

> **Nota:**

> - Los nombres de campo largos que superan los 22 caracteres están truncados después del carácter 22 (por ejemplo, FINANCIAL_STATEMENT_ASSERTIONS se convierte en FINANCIAL_STATEMENT_AS). Sin embargo, si dos o más nombres de campo tienen los mismos 22 primeros caracteres, los nombres se truncan en el carácter 20 y se añade un identificador secuencial de dos dígitos. Por ejemplo:

>   ```
>   FINANCIAL_STATEMENT_ASSERTIONS becomes FINANCIAL_STATEMENT_00
>   FINANCIAL_STATEMENT_ASSERTIONS_MINOR becomes FINANCIAL_STATEMENT_01
>   ```
> - Si se necesitan varios atributos, puede concatenar varios valores de campo con un delimitador, por ejemplo:

>   ```
>   'NAME00' || '||' || '''=''' || '||' || 'FULL_PATH'
>   ```

>   El nombre concatenado y delimitado más 'FULL_PATH’ es un aumento de rendimiento para evitar llamar la función dos veces. Solo puede utilizar este método con propiedades regulares no enumeradas.
> - El recorte de variables será diferente en entornos diferentes.

### Uso de funciones generales

`Guía del creador de informes › Uso de las funciones de base de datos predefinida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-using-general)

Esta sección describe las funciones de base de datos generales.

#### Conversión de enumeraciones multivalor en nombres

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-converting-multivalue-enumerations-names)

Esta función convierte una lista separada por símbolos de ID de valores enumerados en una lista separada y ordenada de nombres localizados.

> **Consejo:** Muchos objetos incluyen un `_LIST` elemento de datos que puede utilizar en lugar de esta función.

Los autores de informes pueden utilizar esta función para transformar un ID de enumeración multivalor en una serie única. Esta función elimina la necesidad de utilizar sentencias SQL personalizada o asuntos de consulta adicionales.

> **Importante:** Para Oracle, la longitud máxima de la serie que la función puede devolver es de 4000 bytes.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RPS_AUX.CONVERT_EVIDLIST_TO_NAME" (P1, P2, P3, P4, P5)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El nombre de variable de la variable enumerada multivalor que se va a convertir en una serie. |
| P2 | Necesario. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |
| P3 | Opcional.<br>Especifica el carácter delimitador que se va a utilizar como separador para elementos en la lista de selección con varios valores (enumeraciones multivalor).<br>Generalmente, este valor puede ser un carácter coma (,), punto y coma (;) o barra vertical (\|).<br>Valor predeterminado: `','` |
| P4 | Opcional.<br>Especifica la columna en la que se ordenarán los valores de lista de selección (enumeraciones multivalor).<br>Posibles valores:<br>- **`'EV_DISPLAY_ORDER'`**<br>  Se utiliza para ordenar los valores de lista por el orden de la visualización del valor enumerado cuando aparecen en la interfaz de usuario de aplicación (valor predeterminado).<br>- **`'EV_NAME'`**<br>  Se utiliza para ordenar los valores de lista por nombre de valor enumerado localizado. |
| P5 | Opcional.<br>Especifica la dirección de ordenación para elementos en las listas de selección con varios valores (enumeraciones multivalor).<br>Posibles valores:<br>- **`'ASC'`**<br>  Ordena los valores de lista en orden ascendente (valor predeterminado).<br>- **`'DESC'`**<br>  Ordena los valores de lista en orden descendente (valor predeterminado). |

##### Ejemplo de uso

La siguiente figura muestra un ejemplo de la salida del informe. En este ejemplo, el campo Dominio de la`RT_PROCESS` La tabla se convierte en una lista de cadenas de texto.

*Figura 1. Conversión de EVIDLIST en salida de nombre*

![La figura muestra una tabla con tres columnas: Nombre del proceso, ID de dominio y Convertir EVIDLIST. La columna ID de dominio muestra valores numéricos (como 228) mientras que la columna Convertir EVIDLIST muestra texto (como Auditoría interna).](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/convert_evidlist_to_name_ex1.jpg)

#### Conversiones de enumeraciones de valor único en nombres

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-converting-single-value-enumerations-names)

Esta función convierte un ID de valor enumerado único en un nombre localizado.

Los autores de informe pueden utilizar esta función para cambiar un ID de enumeración por un nombre. Esta función elimina la necesidad de utilizar sentencias SQL personalizada o asuntos de consulta adicionales.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RPS_AUX.CONVERT_EVID_TO_NAME" (P1, P2)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. EL ID numérico de la variable enumerada de valor único que se va a convertir en una serie. |
| P2 | Necesario. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |

##### Ejemplo de uso

El ejemplo siguiente muestra cómo tomar el ID de nivel de madurez del proceso del objeto SOXProcess y convertirlo en serie de texto. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Conversión de EVID en salida de nombre*

![Salida de informe de ejemplo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/convert_evid_to_name_ex1.jpg)

#### Recuento del número de apariciones de texto

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-counting-number-text-occurrences)

Esta función devuelve el recuento del texto especificado en una serie determinada.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_UTILITIES.COUNT_TEXT_OCCURENCE" (P1, P2)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| *P1* | Necesario. La serie de texto que se va a evaluar. |
| P2 | Necesario. La serie que se va a contar. |

##### Ejemplo de uso

El ejemplo siguiente cuenta el número de barras diagonales (/) de la vía de acceso completa de una entidad de negocios abuelo. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Recuento de la salida de apariciones de texto*

![Salida de informe de ejemplo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/count_text_occurrence.jpg)

#### Determinación de una relación de entorno entre objetos

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-determining-framework-relationship-between-objects)

Esta función identifica si existe una relación padre-hijo (directa o indirecta, primaria o no primaria) entre dos objetos cualesquiera.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RPS_AUX.IS_FM_REL_PARENT_CHILD" (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del tipo de objeto padre que es mayor en la jerarquía de objetos que el objeto proporcionado en el parámetro *P2*. |
| P2 | Necesario. El ID de objeto (un valor numérico) del tipo de objeto hijo que es inferior en la jerarquía de objetos que el objeto proporcionado en el parámetro *P1*. |
| P3 | Necesario. El ID de periodo de elaboración de informes (un valor numérico).<br>Valor predeterminado: -1 (el identificador numérico para el periodo de elaboración de informes actual)<br>**Nota:** El valor del ID de periodo de creación de informes también se puede pasar como una variable de parámetro de solicitud (por ejemplo, `?rpid?` donde `rpid` representa un nombre de variable). Proporcionando un valor optimizará el rendimiento de informe. |
| P4 | Necesario. La extensión de jerarquía basada en el tipo de objeto de recurso padre (por ejemplo, el número de niveles en la jerarquía). Este número debe ser 1 para jerarquías de tipo de objeto no recursivo, y 1 o superior para los recursivos.<br>Valor predeterminado: 1 |
| P5 | Necesario. El Nivel nativo de OP del recurso raíz de la jerarquía padre. Este número debe ser 1 para jerarquías de tipo de objeto que no son entidad, y 1 o superior para los que sí lo son.<br>Valor predeterminado: 1 |
| P6 | Necesario. El Nivel nativo de OP del recurso padre.<br>Valor predeterminado: 1 |
| P7 | Necesario. Indicador para que el tipo de relación padre-hijo busque entre los objetos designados en los parámetros *P1* y *P2*.<br>Posibles valores:<br>- **`'N'`**<br>  Comprueba cualquier relación (primaria o no primaria) entre objetos (valor predeterminado)<br>- **`'Y'`**<br>  Comprueba una relación solo primaria entre objeto. |
| P8 | Opcional. Indicador que dirige cómo debe ejecutar el motor SQL su sentencia ConnectBy.<br>Posibles valores:<br>- **`'Y'`**<br>  Ejecuta la sentencia ConnectBy desde la parte inferior a la parte superior (desde abajo) (valor predeterminado)<br>- **`'N'`**<br>  Ejecuta la sentencia ConnectBy desde la parte superior a la parte inferior (desde arriba).<br>**Nota:** Este parámetro se ignora si el parámetro *P4* se establece en relación sólo primaria. |
| P9 | Opcional. Define el resultado si alguno de los recursos (padre o hijo) son nulos.<br>Posibles valores:<br>- **`'Y'`**<br>  Devuelve Y cuando los objetos padre o hijo son nulos.<br>- **`'N'`**<br>  Devuelve N cuando los objetos padre o hijo son nulos (valor predeterminado) |
| P10 | Opcional. Identificador numérico establecido.<br>Valor predeterminado: 1 (utilice siempre el valor predeterminado) |

##### Ejemplo de uso

La siguiente función de ejemplo se utiliza en una unión entre un asunto de consulta de entidad y un asunto de consulta de problemas para obtener todos los problemas relacionados directa o indirectamente con una entidad. Esta función se ha utilizado porque el subinforme que contenía esta unión se ha invocado desde un informe dimensional y se necesitaban las cantidades de los dos informes para coincidir.

"OP_RPS_AUX.IS_FM_REL_PARENT_CHILD"([Entidad].[ID_ENTIDAD_FUNCIÓN_LOB], [Problema].[ID_PROBLEMA_IS], [Entidad].[ID_PERIODO_CREACIÓN_INFORMES_FUNCIÓN_LOB], 3, 1, [Entidad].[Nivel nativo]) = 'Y'

El valor [Entidad].[Nivel nativo] se ha pasado del informe de llamada como un parámetro. Como esto implicaba una jerarquía de entidad fija, la extensión de jerarquía y el nivel nativo estaban codificados.

#### Determinación de una relación padre primaria entre objetos

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-determining-primary-parent-relationship-between-objects)

Esta función identifica si una relación (ya sea directa o indirecta) entre dos objetos cualquiera es primaria o no.

Los autores de informes pueden utilizar esta función, por ejemplo, para visualizar un informe cuyo objeto es el padre primario para objetos hijo con varios padres, o como filtro para devolver detalles sobre esos objetos con una relación primaria.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RPS_AUX.IS_REL_PARENT_CHILD_PRIM" (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del objeto padre. Este tipo de objeto debe estar más arriba en la jerarquía de objetos que el objeto hijo proporcionado en el parámetro `P2`. |
| P2 | Necesario. El ID de objeto (un valor numérico) del objeto hijo. Este tipo de objeto debe estar más abajo en la jerarquía de objetos que el objeto padre proporcionado en el parámetro `P1`. |
| P3 | Necesario. El ID de periodo de elaboración de informes (un valor numérico) para el que se devolverá el atributo padre primario.<br>**Nota:** El valor del ID de periodo de creación de informes también se puede pasar como una variable de parámetro de solicitud (por ejemplo, `?rpid?` donde `rpid` representa un nombre de variable). Proporcionando un valor optimizará el rendimiento de informe.<br>Valor predeterminado: -1 (el identificador numérico para el periodo de elaboración de informes actual) |
| P4 | Necesario. El ID de tipo de objeto (un valor numérico) del objeto padre. Este valor se buscará dimámicamente para relaciones directas.<br>Valor predeterminado: `NULL` (sin comillas y sin distinción entre mayúsculas y minúsculas; utilice siempre el valor predeterminado) |
| P5 | Necesario. El ID de tipo de objeto (un valor numérico) del objeto hijo. Este valor se buscará dimámicamente para relaciones directas.<br>Valor predeterminado: `NULL` (sin comillas y sin distinción entre mayúsculas y minúsculas; utilice siempre el valor predeterminado) |
| P6 | Necesario. Indicador para utilizar siempre Connect By SQL.<br>Valor predeterminado: ‘N’ (utilice siempre el valor predeterminado) |
| P7 | Necesario. Indicador que identifica si una relación (ya sea directa o indirecta) entre dos objetos cualquiera es primaria o no.<br>Posibles valores:<br>- **`'Y'`**<br>  Devuelve Y cuando dos objetos tiene una relación directa y primaria (por ejemplo, entre objetos Prueba y Resultado de prueba) (valor predeterminado)<br>- **`'N'`**<br>  Devuelve Y si el objeto hijo puede hacer un seguimiento de la relación primaria a través de la jerarquía de objeto al objeto padre. Utilice este valor cuando los objetos especificados tengan una relación de tipo padre-hijo indirecta dentro de la jerarquía de objeto (por ejemplo, los objetos Proceso y Control tienen una relación indirecta donde los objetos Riesgo y Objetivo de control se establecen entre Proceso y Control en la jerarquía). |
| P8 | Necesario. Función reservada.<br>Valor predeterminado: `NULL` (sin comillas y sin distinción entre mayúsculas y minúsculas; utilice siempre el valor predeterminado) |
| P9 | Necesario. Solicita el resultado si alguno de los recursos (padre o hijo) son nulos.<br>Posibles valores:<br>- **`'Y'`**<br>  Devuelve Y cuando la relación entre dos objetos es primaria (valor predeterminado)<br>- **`'N'`**<br>  Devuelve una N cuando la relación entre dos objetos no es primaria. |
| P10 | Opcional. Identificador numérico establecido.<br>Valor predeterminado: 1 (utilice siempre el valor predeterminado) |

##### Ejemplo de uso

La siguiente función de ejemplo devuelve Y o N en una fila para un control particular si ese control puede hacer seguimiento de una relación primaria en la jerarquía a través de Riesgo, Objetivo de control y, finalmente, hasta Proceso dentro del periodo de creación de informes actual.

La columna calculada **Proceso a controlar** en Figura 1 describe si hay una relación primaria entre un objeto de proceso determinado y un objeto de control.

*Figura 1. Es salida primaria padre-hijo relativa*

![Ejemplo de una relación padre primaria entre objetos](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/is_rel_parent_child_ex1.jpg)

La adición de un filtro para el parámetro `P7`, como cambiar N a Y para **Proceso a control**, eliminará todos los detalles de fila donde no hay una relación primaria (vía de acceso) entre un determinado objeto de proceso y de control.

#### Determinación de una relación entre objetos

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-determining-relationship-between-objects)

Esta función identifica si existe una relación padre-hijo (directa o indirecta, primaria o no primaria) entre dos objetos cualesquiera.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RPS_AUX.IS_REL_PARENT_CHILD" (P1, P2, P3, P4, P5, P6, P7)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del tipo de objeto padre que está más arriba en la jerarquía de objetos que el objeto proporcionado en el parámetro `P2`. |
| P2 | Necesario. El ID de objeto (un valor numérico) del tipo de objeto hijo que está más abajo en la jerarquía de objetos que el objeto proporcionado en el parámetro `P1`. |
| P3 | Necesario. El ID de periodo de elaboración de informes (un valor numérico).<br>Valor predeterminado: -1 (el identificador numérico para el periodo de elaboración de informes actual)<br>**Nota:** El valor del ID de periodo de creación de informes también se puede pasar como una variable de parámetro de solicitud (por ejemplo, `?rpid?` donde `rpid` representa un nombre de variable). Proporcionando un valor optimizará el rendimiento de informe. |
| P4 | Opcional. Indicador para que el tipo de relación padre-hijo busque entre los objetos designados en los parámetros *P1* y *P2*.<br>Posibles valores:<br>- **`'N'`**<br>  Comprueba cualquier relación (primaria o no primaria) entre objetos (valor predeterminado).<br>- **`'Y'`**<br>  Comprueba una relación solo primaria entre objeto. |
| P5 | Opcional. Indicador que dirige cómo debe ejecutar el motor SQL su sentencia ConnectBy.<br>Posibles valores:<br>- **`'Y'`**<br>  Ejecuta la sentencia ConnectBy desde la parte inferior a la parte superior (desde abajo).<br>- **`'N'`**<br>  Ejecuta la sentencia ConnectBy desde la parte superior a la parte inferior (desde arriba).<br>**Nota:** Este parámetro se ignora si el parámetro `P4` se establece en relación sólo primaria. |
| P6 | Opcional. Define el resultado si alguno de los recursos (padre o hijo) son nulos.<br>Posibles valores:<br>- **`'Y'`**<br>  Devuelve Y cuando los objetos padre o hijo son nulos.<br>- **`'N'`**<br>  Devuelve N cuando los objetos padre o hijo son nulos (valor predeterminado). |
| P7 | Opcional. Identificador numérico establecido.<br>Valor predeterminado: 1 (utilice siempre el valor predeterminado) |

##### Ejemplo de uso

La siguiente función de ejemplo indica si existe algún tipo de relación entre el registro Riesgo y el registro Control (primario o no primario, directo o indirecto).

La columna **Está relacionado** en Figura 1 devuelve la información que indica si existe una relación padre-hijo entre un determinado objeto Riesgo y Control.

*Figura 1. Es salida padre-hijo relativa*

![Tabla con una columna Es relacionado](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/is_rel_parent_child_2_ex1.jpg)

#### Formateo del valor de divisa

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-formatting-currency-value)

Esta función da formato a un valor de divisa con el número de posiciones decimales y separadores adecuados para la configuración regional especificada. Esta función puede ser útil para campos calculados.

> **Nota:** El símbolo de moneda NO se visualiza en la salida.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_CURRENCY_MGR.FORMAT_CURRENCY_VALUE" (P1, P2, P3)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El número (como cantidad de moneda) que desea formatear. |
| P2 | Necesario. El código de moneda ISO de 3 caracteres que determina el número de posiciones decimales que se va a visualizar. |
| P3 | Necesario. Identificador numérico del entorno local del usuario OpenPages® que determina el tipo de separadores de grupo.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |

##### Ejemplo de uso 1

El siguiente ejemplo convierte el valor para 1234,5 en un formato para la configuración regional de EE.UU.

*Figura 1. Dar formato de moneda para USD*

![Tabla de referencias cruzadas que muestra el formato de moneda para el entorno local de EE.UU.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/format_currency_value_ex1.jpg)

##### Ejemplo de uso 2

El siguiente ejemplo convierte el valor para 1234,5 en un formato para la configuración regional de Alemania. La Figura 2 muestra la salida de informe de ejemplo.

*Figura 2. Dar formato de moneda para EUR*

![Tabla de referencias cruzadas que muestra el formato de moneda para el entorno local alemán](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/format_currency_value_ex2.jpg)

##### Ejemplo de uso 3

El siguiente ejemplo convierte el valor para 1234,5 en un formato para la configuración regional de Japón. La Figura 3 muestra la salida de informe de ejemplo.

*Figura 3. Dar formato de moneda para JPY*

![Tabla de referencias cruzadas que muestra el formato de moneda para el entorno local japonés](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/format_currency_value_ex3.jpg)

#### Obtención del nombre de visualización de Actor por ID

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-actors-display-name-by-id)

Esta función sólo se aplica a entornos Oracle y devuelve el nombre de visualización formateado de un actor (usuario o grupo) utilizando el número de ID de actor interno.

Si el actor es un grupo, solo se devuelve el nombre de cuenta del grupo, y se ignora la serie de formato proporcionada. Si se proporciona un nombre de actor no válido, se devuelve el valor proporcionado.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_ACTOR_MGR.GET_DISPLAY_NAME" (P1, P2, P3)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. Un ID numérico para el actor (usuario o grupo) que se va a visualizar. |
| P2 | Necesario. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |
| P3 | Opcional. Puede utilizar las siguientes opciones de visualización de formato:<br>- **`%FN;`**<br>  Para mostrar el nombre del usuario.<br>- **`%LN;`**<br>  Para mostrar el apellido del usuario.<br>- **`%EM;`**<br>  Para mostrar la dirección de correo electrónico del usuario.<br>Valor predeterminado: Se visualiza el nombre de cuenta de inicio de sesión del actor si no se especifica formato. |

##### Ejemplo de uso 1

El ejemplo siguiente muestra el nombre y apellido del ID de actor 281. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Nombre de visualización por Nombre y apellido del ID*

![Tabla de referencias cruzadas que muestra el nombre y el apellido del ID de actor 281](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_display_name_by_id-ex1.jpg)

##### Ejemplo de uso 2

El ejemplo siguiente muestra el correo electrónico del ID de actor 281. La Figura 2 muestra la salida de informe de ejemplo.

*Figura 2. Nombre de visualización por correo electrónico del ID*

![Tabla de referencias cruzadas que muestra el correo electrónico para el ID de actor 281](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_display_name_by_id-ex2.jpg)

##### Ejemplo de uso 3

El ejemplo siguiente muestra el nombre del ID de actor 281. La Figura 3 muestra la salida de informe de ejemplo.

*Figura 3. Nombre de visualización por nombre del ID*

![Tabla de referencias cruzadas que muestra el nombre del ID de actor 281](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_display_name_by_id-ex3.jpg)

#### Obtención del nombre de visualización de Actor por ID de Actor

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-actors-display-name-by-actor-id)

Esta función sólo se aplica a entornos IBM® Db2® y devuelve un nombre de visualización con formato de actor (usuario o grupo) utilizando el número de ID de actor interno.

Si el actor es un grupo, solo se devuelve el nombre de cuenta del grupo, y se ignora la serie de formato proporcionada. Si se proporciona un nombre de actor no válido, se devuelve el valor proporcionado.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_ACTOR_MGR.GET_DISPLAY_NAME_BY_ACTOR_ID" (P1, P2, P3)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. Un ID numérico para el actor (usuario o grupo) que se va a visualizar. |
| P2 | Necesario. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |
| P3 | Opcional. Puede utilizar las siguientes opciones de visualización de formato:<br>- **`%FN;`**<br>  Para mostrar el nombre del usuario.<br>- **`%LN;`**<br>  Para mostrar el apellido del usuario.<br>- **`%EM;`**<br>  Para mostrar la dirección de correo electrónico del usuario.<br>Valor predeterminado: Se visualiza el nombre de cuenta de inicio de sesión del actor si no se especifica formato. |

##### Ejemplo de uso 1

El ejemplo siguiente muestra el nombre y apellido del ID de actor 281. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Nombre de visualización por Nombre y apellido del ID*

![Tabla de referencias cruzadas que muestra el nombre y el apellido del ID de actor 281](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_display_name_by_id-ex1.jpg)

##### Ejemplo de uso 2

El ejemplo siguiente muestra el correo electrónico del ID de actor 281. La Figura 2 muestra la salida de informe de ejemplo.

*Figura 2. Nombre de visualización por correo electrónico del ID*

![Tabla de referencias cruzadas que muestra el correo electrónico para el ID de actor 281](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_display_name_by_id-ex2.jpg)

##### Ejemplo de uso 3

El ejemplo siguiente muestra el nombre del ID de actor 281. La Figura 3 muestra la salida de informe de ejemplo.

*Figura 3. Nombre de visualización por nombre del ID*

![Tabla de referencias cruzadas que muestra el nombre del ID de actor 281](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_display_name_by_id-ex3.jpg)

#### Obtención del nombre de visualización de actor por ID de sesión

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-actors-display-name-by-logon-id)

Esta función devuelve los nombres de visualización formateados del actor (usuarios o grupos).

Si los actores son un grupo, solo se devuelven los nombres de cuenta de grupo y la serie de formato proporcionada se ignora. Si se proporciona un ID de inicio de sesión de actor no válido, se devuelve el valor proporcionado.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_ACTOR_MGR.GET_DISPLAY_NAME" (P1, P2, P3, P4)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. Nombres de usuario de inicio de sesión de valor de serie para los actores (usuarios o grupos) que se deben visualizar. |
| P2 | Necesario. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |
| P3 | Opcional. Las opciones de visualización de formato son:<br>- **`%FN;`**<br>  Para mostrar el nombre del usuario.<br>- **`%LN;`**<br>  Para mostrar el apellido del usuario.<br>- **`%EM;`**<br>  Para mostrar la dirección de correo electrónico del usuario.<br>Valor predeterminado: Se visualiza el ID de inicio de sesión del actor si no se especifica formato. |
| P4 | Opcional. Separador para nombres de visualización devueltos. Valor predeterminado: Una coma seguida de un espacio. |

##### Ejemplo de uso 1

En el ejemplo siguiente, se muestra el nombre y el apellido de los usuarios designados como Propietario del control en la aplicación. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Nombre y apellido del propietario del control*

![Tabla de referencias cruzadas que muestra los nombres y apellidos de los propietarios de control](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get-display-name-ex1.jpg)

##### Ejemplo de uso 2

En el ejemplo siguiente, se muestra la dirección de correo electrónico de los usuarios designados como Propietario del control en la aplicación. La Figura 2 muestra la salida de informe de ejemplo.

*Figura 2. Correo electrónico del propietario del control*

![Tabla de referencias cruzadas que muestra las direcciones de correo electrónico de los propietarios de control](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get-display-name-ex2.jpg)

##### Ejemplo de uso 3

En el ejemplo siguiente, se muestra el nombre de los usuarios designados como Propietario del control de la aplicación. La Figura 3 muestra la salida de informe de ejemplo.

*Figura 3. Nombre del propietario del control*

![Tabla de referencias cruzadas que muestra los nombres de los propietarios de control](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get-display-name-ex3.jpg)

#### Obtención del texto clave externo

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-external-key-text)

Esta función devuelve una serie clave externa localizada.

Esta función puede ser útil para la localización de campos calculados con un tipo de datos de Serie simple cuando la aplicación no ha localizado estos tipos de campos. Cuando se necesitan series localizadas para un campo calculado (excluyendo los nombres de etiqueta de campo, que ya están localizados), un autor de campo calculado puede añadir una nueva clave de texto de aplicación a través de la interfaz de usuario de IBM OpenPages® y, a continuación, hacer referencia a ella con esta función. De esta forma, puede gestionar todo el texto localizado en un único lugar y evitar la codificación de la lógica específica de la configuración regional en ecuaciones.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_I18N_MGR.GET_EXTERNAL_KEY_TEXT" (P1, P2, P3)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. Nombre de la clave de texto de la aplicación. |
| P2 | Necesario. Categoría de texto de la aplicación. |
| P3 | Necesario. Identificador numérico del entorno local del usuario OpenPages .<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |

##### Ejemplo de uso

El siguiente ejemplo muestra cómo tomar el valor de clasificación del riesgo de ‘crítico’ y sustituir un valor de serie localizado para él. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Obtención de la salida del texto clave externo*

![Tabla de referencias cruzadas que muestra series en inglés y alemán que significan "crítico"](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/getting_external_key_text_ex1.jpg)

#### Obtención de los atributos de un objeto padre primario

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-attributes-primary-parent-object)

Esta función devuelve el valor para uno o más atributos de un objeto padre primario.

Los autores de informes pueden utilizar esta función, por ejemplo, para buscar directamente un valor de campo de propiedad (normal o con un valor enumerado o multivalor) para un objeto determinado sin tener que consulta toda la jerarquía de objetos completa. Debe tener mucho cuidado al utilizar esta función en situaciones en las que un objeto puede tener varios padres.

> **Nota:** Revise también la obtención de los atributos directos de un objeto padre primario antes de utilizar esta función porque esta última función es más fácil de utilizar.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RPS_AUX.GET_PRIM_PARENT_ATTRIBUTE" (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. ID de objeto (un valor numérico) del objeto hijo para el que se devolverán los atributos padre primarios. |
| P2 | Necesario. ID de periodo de elaboración de informes (un valor numérico) del objeto hijo para el que se devolverán los atributos padre primarios.<br>**Nota:** El valor del ID de periodo de creación de informes también se puede pasar como una variable de parámetro de solicitud (por ejemplo, `?rpid?` donde `rpid` representa un nombre de variable). Proporcionando un valor optimizará el rendimiento de informe.<br>Valor predeterminado: -1 (el identificador numérico para el periodo de elaboración de informes actual) |
| P3 | Necesario. ID de tipo de objeto del objeto padre (este valor numérico es diferente del valor de ID de objeto en el parámetro *P1*). Por ejemplo, si el objeto padre es una Entidad de negocio, es el ID de tipo de objeto del tipo de objeto Entidad de negocio (`SOXBusEntity`).<br>**Nota:** Es posible que los informes no sean portables entre instalaciones (ya que los mismos tipos de objeto pueden tener ID diferentes) |
| P4 | Necesario. Nivel del objeto padre primario en la jerarquía. Utilizado únicamente para objetos recursivos como: Entidad de negocio, Subproceso, Submandato, Subcuenta.<br>Posibles valores:<br>- **1**<br>  Nivel padre más alto nivel (valor predeterminado)<br>- **0**<br>  Nivel principal más cercano al objeto.<br>- **4**<br>  Cuarto nivel padre. Si no existe, utilice el nivel 0.<br>- **-1**<br>  Segundo nivel padre más bajo.<br>- **-4**<br>  Cuarto nivel padre desde la parte inferior. Si no existe, utilice el nivel 1.<br>Puede especificar cualquier nivel según sea necesario. Si un valor especificado no existe en la jerarquía, se utilizará el objeto padre de nivel más alto.<br>**Nota:** Si el tipo de objeto padre no es recursivo, utilice 1. |
| P5 | Necesario. Nombre de tabla RT del tipo de objeto padre en el esquema de elaboración de informes.<br>**Nota:** Este valor NO es el nombre del asunto de consulta que ve un autor de informes en IBM® Cognos® Analytics -Creación de informes. Un autor de informes debe poder determinar los nombres de las tablas conectándose a la base de datos.<br>Valor predeterminado: `'RT_ENTITY'` |
| P6 | Necesario. Nombre de columna del ID de objeto en la tabla RT del tipo de objeto padre en el esquema de elaboración de informes.<br>**Nota:** NO es el nombre del elemento de consulta que el autor del informe ve en IBM Cognos Analytics -Creación de informes. Un autor de informes debe poder determinar los nombres de las columnas conectándose a la base de datos.<br>Valor predeterminado: `'ENTITY_ID'` |
| P7 | Necesario. Nombre de columna del ID de periodo de elaboración de informes en la tabla RT del tipo de objeto padre en el esquema de elaboración de informes.<br>**Nota:** NO es el nombre del elemento de consulta que el autor del informe ve en IBM Cognos Analytics -Creación de informes. Un autor de informes debe poder determinar los nombres de las columnas conectándose a la base de datos.<br>Valor predeterminado: `'REPORTING_PERIOD_ID'` |
| P8 | Necesario. Nombre de columna del atributo en la tabla RT del tipo de objeto padre en el esquema de elaboración de informes. Esto representa un elemento de datos que incluirá una salida posterior al informe o filtro.<br>**Nota:** NO es el nombre del elemento de consulta que el autor del informe ve en IBM Cognos Analytics -Creación de informes. Un autor de informes debe poder determinar los nombres de las columnas conectándose a la base de datos.<br>Valor predeterminado: `'FULL_PATH'` |
| P9 | Necesario. Especifica el tipo de atributo para los valores devueltos en el parámetro de columna *P8*.<br>**Nota:** Los valores no distinguen entre mayúsculas y minúsculas.<br>Posibles valores:<br>- **`'NONE'`**<br>  Usar para campos comunes (no enumerados) (valor predeterminado).<br>- **`'SINGLE'`**<br>  Utilizar para enumeraciones con un valor.<br>- **`'MULTI'`**<br>  Utilizar para enumeraciones multivalor. |
| P10 | Necesario. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |
| P11 | Opcional.<br>Especifica el carácter delimitador que se va a utilizar como separador para elementos en la lista de selección con varios valores (enumeraciones multivalor).<br>Generalmente, este valor puede ser un carácter coma (,), punto y coma (;) o barra vertical (\|).<br>Valor predeterminado: `','` |
| P12 | Opcional.<br>Especifica la columna en la que se ordenarán los valores de lista de selección (enumeraciones multivalor).<br>Posibles valores:<br>- **`'EV_DISPLAY_ORDER'`**<br>  Se utiliza para ordenar los valores de lista por el orden de la visualización del valor enumerado cuando aparecen en la interfaz de usuario de aplicación (valor predeterminado).<br>- **`'EV_NAME'`**<br>  Se utiliza para ordenar los valores de lista por nombre de valor enumerado localizado. |
| P13 | Opcional.<br>Especifica la dirección de ordenación para elementos en las listas de selección con varios valores (enumeraciones multivalor).<br>Posibles valores:<br>- **`'ASC'`**<br>  Ordena los valores de lista en orden ascendente (valor predeterminado).<br>- **`'DESC'`**<br>  Ordena los valores de lista en orden descendente (valor predeterminado). |
| P14 | Opcional. Identificador numérico establecido.<br>Valor predeterminado: 1 (utilice siempre el valor predeterminado) |

##### Ejemplo de uso 1

El ejemplo siguiente muestra los valores del atributo `ENTITY_TYPE` para la entidad padre de un proceso. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Obtener salida del atributo padre primario*

![Tabla de referencias cruzadas que muestra el nombre de entidad, el nombre de proceso y el tipo de entidad del padre primario](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_prim_parent_attribute.jpg)

##### Ejemplo de uso 2

Mediante la función `OP_RPS_AUX.GET_PRIM_PARENT_ATTRIBUTE` se puede crear un informe exclusivamente a partir del asunto de consulta de problema sin tener que añadir objetos adicionales. La consulta generada por el informe no necesita, en este ejemplo, atravesar la jerarquía completa y, debe devolver todos los elementos de datos necesarios para la salida de informe o filtro. El resultado de este uso es que es posible mejorar significativamente el tiempo de ejecución del informe.

El ejemplo siguiente devuelve el Nombre de entidad de nivel superior para un ID de problema determinado. La Figura 2 muestra la salida de informe de ejemplo.

*Figura 2. Obtener salida del atributo padre primario*

![Tabla de referencias cruzadas que muestra el nombre de entidad del padre principal, el nombre del problema y la ubicación del problema](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_prim_parent_attribute_ex2.jpg)

#### Obtención de atributos directos de un objeto padre primario

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-direct-attributes-primary-parent-object)

Esta función devuelve el valor para un atributo de un objeto padre primario.

Los autores de informes pueden utilizar esta función para buscar directamente ciertos valores de propiedad para un objeto determinado sin tener que consulta toda la jerarquía de objetos completa. Esta función no requiere que el autor de informes sepa qué tipo de objeto padre primario se está consultando.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RPS_AUX.GET_DIRECT_PRIM_PRNT_VALUE" (P1, P2, P3, P4, P5)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. ID de objeto (un valor numérico) del objeto hijo para el que se devolverán los atributos padre primarios. |
| P2 | Necesario. ID de periodo de elaboración de informes (un valor numérico) para el que se devolverá el valor.<br>Por defecto: `NULL` (sin comillas y sin distinguir mayúsculas de minúsculas) devuelve el ID del periodo de informe actual, que es -1. Proporcionando un valor optimizará el rendimiento de informe. |
| P3 | Necesario. ID de actor del usuario que ha iniciado sesión. Se utiliza para determinar qué acceso de datos posee el usuario. |
| P4 | Necesario. Nombre de propiedad del atributo de un tipo de objeto padre en el Esquema de elaboración de informes. Esto representa un elemento de datos que incluirá una salida posterior al informe o filtro. A continuación, tiene una lista de los nombres de propiedad válidos:<br>- **RESOURCE_ID**<br>  ID de recurso del sistema exclusivo<br>- **RESOURCE_NAME**<br>  Nombre padre.<br>- **RESOURCE_NAME_RAW**<br>  Nombre padre completo con identificadores internos<br>- **RESOURCE_LOCATION**<br>  Vía de acceso completa padre.<br>- **RESOURCE_LOCATION_RAW**<br>  Vía de acceso completa padre sin los identificadores retirados<br>- **RESOURCE_URL**<br>  URL de página de detalle padre.<br>- **OBJECT_TYPE_ID**<br>  ID de recurso del objeto padre<br>- **OBJECT_TYPE_NAME_SYS**<br>  Nombre de objeto del sistema padre.<br>- **OBJECT_TYPE_NAME_I18N**<br>  Nombre de objeto localizado padre. |
| P5 | Necesario. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |

##### Ejemplo de uso 1

El ejemplo siguiente devuelve el tipo padre para un ID de problema determinado. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Tipo padre primario*

![Tabla de referencias cruzadas que muestra el tipo de padre primario para un problema](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_get_direct_primary_parent_value_1.jpg)

##### Ejemplo de uso 2

El ejemplo siguiente devuelve el ID de recurso padre para un ID de problema determinado. La Figura 2 muestra la salida de informe de ejemplo.

*Figura 2. ID de padre primario*

![Tabla de referencias cruzadas que muestra el ID padre de un problema](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_get_direct_primary_parent_value_2.jpg)

#### Obtención de la tasa de cambio

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-exchange-rate)

Esta función devuelve la tasa de cambio para la fecha y código de moneda ISO especificados.

Si no se especifica fecha, se utiliza la fecha del sistema actual. Esta función puede ser útil para campos calculados.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_CURRENCY_MGR.GET_EX_RATE_ISO" (P1, P2)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El código de moneda ISO de 3 caracteres. |
| P2 | Opcional. La fecha de la tasa de cambio se hace efectiva en el sistema.<br>Valor predeterminado: la fecha del sistema actual se utiliza si no se ha especificado una fecha. |

##### Ejemplo de uso 1

El siguiente valor devuelve la tasa de cambio actual para Euros. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Tipo de cambio de moneda*

![Tabla de referencias cruzadas que muestra el tipo de cambio actual para Euros](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_ex_rate_iso_ex1.jpg)

##### Ejemplo de uso 2

El ejemplo siguiente devuelve la tasa de cambio para Euros para la fecha que se modificó por última vez 1 de enero de 1970. La [Figura 2](#obtención-de-atributos-directos-de-un-objeto-padre-primario) muestra la salida de informe de ejemplo.

*Figura 2. Tipo de cambio de moneda por fecha*

![Tabla de referencias cruzadas que muestra el tipo de cambio de euros el 1 de enero de 1970](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_ex_rate_iso_ex2.jpg)

#### Obtención de los ID de recurso de vía de acceso de árbol

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-tree-path-resource-ids)

Esta función devuelve los ID de los objetos que están en la vía de acceso de los dos objetos facilitados como entradas para la función.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RESOURCES_MGR.GET_TREE_PATH_RESOURCE_IDS" (P1, P2, P3, P4, P5)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El identificador de recurso para el comienzo del segmento de árbol. |
| P2 | Necesario. El identificador de recurso para el final del segmento de árbol. |
| *P3* | Necesario. Una lista de tipos de objeto entre paréntesis y separados por comas que se va a visitar. |
| *P4* | Opcional. El ID de periodo de elaboración de informes.<br>Valor predeterminado: la elaboración de informes actual se utiliza si no se ha especificado un periodo de elaboración de informes.<br>**Nota:** El valor del ID de periodo de creación de informes también se puede pasar como una variable de parámetro de solicitud (por ejemplo, `?rpid?` donde `rpid` representa un nombre de variable). Proporcionando un valor optimizará el rendimiento de informe. |
| *P5* | Opcional. El ID de jerarquía. Los valores predeterminados para la jerarquía soportada actualmente.<br>Valor predeterminado: 1 (utilice siempre el valor predeterminado) |

##### Ejemplo de uso

El siguiente ejemplo muestra que ?ControlObjectiveID? (Inicio_id) y ?TestID? (id_end) son parámetros para el informe para los objetos listados (SOXControlObjective, SOXRisk, SOXControl y SOXTest). La Figura 1 muestra la salida de informe de ejemplo.

```
"OP_RESOURCES_MGR.GET_TREE_PATH_RESOURCE_IDS"(?ControlObjectiveID?,?TestID?, 
'(' || '''SOXControlObjective''' || ',' || '''SOXRisk''' || ',' ||
 '''SOXControl''' || ',' || '''SOXTest''' || ')' )
```

*Figura 1. Obtención de la salida de vía de acceso de árbol*

![Tabla de referencias cruzadas que muestra la salida de vía de acceso de árbol](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/getting_tree_path_ex1.jpg)

Otros resultados pueden ser:

- `-1` si solo existe una vía de acceso directa entre recursos
- `-2` si no existe ninguna vía de acceso entre recursos

#### Resumen de enumeraciones multivalor en una lista

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de funciones generales` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-rolling-up-multivalued-enumerations-into-list)

Esta función devuelve una lista delimitada de nombres de enumeración multivalor localizados para un campo de propiedad de recurso de enumeración multivalor especificado.

Los autores de informes pueden utilizar esta función para resumir enumeraciones multivalor en una lista separada por comas (u otro delimitador que desee). Esta función elimina la necesidad de utilizar sentencias SQL personalizada o un enfoque maestro-detalle.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RPS_AUX.GET_MVAL_STRAGG_GENERIC" (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. Nombre de tabla RT que almacena los valores enumerados multivalor para una propiedad determinada de un tipo de objeto determinado |
| P2 | Necesario. Nombre de columna de la tabla RT especificada en P1 que almacena el ID de recurso. |
| P3 | Necesario. Nombre de columna de la tabla RT especificada en P1 que almacena los ID de valor enumerado. |
| P4 | Necesario. Nombre de columna de la tabla RT especificado en P1 que almacena el ID de periodo de elaboración de informes. |
| P5 | Necesario. ID de recurso (un valor numérico) para el que se devolverá la lista. Es el elemento de consulta del asunto de consulta que contiene el ID de recurso principal por el que se agregarán los valores enumerados. |
| P6 | Necesario. ID de periodo de elaboración de informes (un valor numérico) para el que se devolverá la lista.<br>Por defecto: `NULL` (sin comillas y sin distinguir mayúsculas de minúsculas) devuelve el ID del periodo de informe actual, que es -1. Proporcionando un valor optimizará el rendimiento de informe. |
| P7 | Necesario. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |
| P8 | Necesario.<br>Especifica el carácter delimitador que se va a utilizar como separador para elementos en la lista de selección con varios valores (enumeraciones multivalor).<br>Generalmente, este valor puede ser un carácter coma (,), punto y coma (;) o barra vertical (\|).<br>Valor predeterminado: `','` |
| P9 | Necesario.<br>Especifica la columna en la que se ordenarán los valores de lista de selección (enumeraciones multivalor).<br>Posibles valores:<br>- **`'EV_DISPLAY_ORDER'`**<br>  Se utiliza para ordenar los valores de lista por el orden de la visualización del valor enumerado cuando aparecen en la interfaz de usuario de aplicación (valor predeterminado).<br>- **`'EV_NAME'`**<br>  Se utiliza para ordenar los valores de lista por nombre de valor enumerado localizado. |
| P10 | Necesario.<br>Especifica la dirección de ordenación para elementos en las listas de selección con varios valores (enumeraciones multivalor).<br>Posibles valores:<br>- **`'ASC'`**<br>  Ordena los valores de lista en orden ascendente (valor predeterminado).<br>- **`'DESC'`**<br>  Ordena los valores de lista en orden descendente (valor predeterminado). |

##### Ejemplo de uso

El ejemplo siguiente devuelve una lista de valores seleccionados separados por comas para un campo Riesgo de selección múltiple llamado Declaraciones de balances financieros, para cada riesgo filtrado por el periodo de elaboración de informes seleccionado. La Figura 1 muestra la salida de informe de ejemplo.

*Figura 1. Obtener salida MVAL STRAGG*

![Tabla de referencias cruzadas que muestra una lista delimitada por comas de enumeraciones multivalor acumuladas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/get_mval_stragg_ex1.jpg)

### Uso de las funciones dependientes del tiempo

`Guía del creador de informes › Uso de las funciones de base de datos predefinida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-using-time-dependent)

Esta sección describe las funciones de base de datos basadas en el tiempo.

#### Obtención del valor de campo personalizado por ID

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de las funciones dependientes del tiempo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-custom-field-value-by-id)

Esta función devuelve el valor para un campo personalizado de un objeto a partir de cierta fecha.

Utiliza PropertyDefId para identificar el valor de campo personalizado que se va a devolver.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RESOURCES_MGR.GET_CUSTOM_FIELD_VALUE_BY_ID" (P1, P2, P3, P4, P5, P6)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del objeto para el que se devolverá el valor de campo personalizado. |
| P2 | Necesario. "A partir de la fecha" del campo personalizado. |
| P3 | Necesario. El PropertyDefId del campo personalizado (un valor numérico). |
| P4 | Opcional. Utilizar solo la tabla de seguimiento de auditoría del sistema.<br>Posibles valores:<br>- **No**<br>  Se devolverá un valor para la propiedad independientemente de si está en la tabla de auditoría del sistema<br>- **Sí**<br>  Solo se devolverá un valor si el valor está en la tabla de seguimiento de auditoría del sistema.<br>**Nota:** Cuando se crea por primera vez una propiedad, no se especifica un valor en la tabla de seguimiento de auditoría del sistema.<br>Valor predeterminado: Falso |
| P5 | `Optional. This field determines the type of output for this function.`<br>Posibles valores:<br>• EV_ID<br>• EV_CODE<br>• EV_SYSTEM_NAME<br>• EV_NAME_I18N<br>Valor predeterminado: EV_ID |
| P6 | Opcional. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |

> **Nota:** Se devolverá un valor de error si la solicitud precede a la creación de la variable.

##### Ejemplo de uso

El siguiente ejemplo muestra cómo obtener un valor de campo personalizado utilizando su PropertyDefId. En este ejemplo, queremos obtener la clasificación de riesgo inherente como función de tiempo. El valor 140 es el propertyDefId para la clasificación de riesgo inherente que se había buscado en la tabla propertydefs utilizando el siguiente SQL:

select * from propertydefs where name = 'Inherent Risk Rating'

Una vez se conoce propertydefId, debe decidir el formato de la salida. El ejemplo muestra la salida como EV_NAME_118N que es el nombre de la propiedad traducida a la del ID de configuración regional.

A continuación, vemos el código que hemos utilizado en este ejemplo:

`"OP_RESOURCES_MGR.GET_CUSTOM_FIELD_VALUE_BY_ID" ([RI_RISK_ID], to_date(?Date?,'DD-MON-YYYY'), 140, 'N', 'EV_NAME_I18N', #$account.parameters.openPagesLocaleId#)`

Si selecciono la fecha 1-Jan-1970 (antes de que se creara el campo), obtengo lo siguiente, que se muestra en Figura 1:

*Figura 1. Clasificación de riesgo inherente - 1-ene-1970*

![Tabla de referencias cruzadas que muestra la clasificación de riesgo el 1 de enero de 1970](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_custom_as_of_date_1.jpg)

Como puede ver en los resultados, el valor actual de clasificación de riesgo es Medio, pero en la fecha solicitada, no se ha encontrado el valor. Si selecciono la fecha 24-Feb-2011, obtengo lo siguiente, que se muestra en Figura 2:

*Figura 2. Clasificación de riesgo inherente - 24-feb-2011*

![Tabla de referencias cruzadas que muestra la clasificación de riesgo el 24 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_custom_as_of_date_2.jpg)

Ahora puede ver que en la fecha 24-Feb-2011, el valor de la clasificación de riesgo inherente era Bajo. Si entro la fecha de hoy, obtengo lo siguiente, que se muestra en Figura 3:

*Figura 3. Clasificación de riesgo inherente - 1-abril-2011*

![Tabla de referencias cruzadas que muestra la clasificación de riesgo el 1 de abril de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_custom_as_of_date_3.jpg)

El valor del campo es igual a la clasificación de riesgo inherente.

#### Obtención del valor de campo personalizado por nombre

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de las funciones dependientes del tiempo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-custom-field-value-by-name)

Esta función devuelve el valor para una propiedad personalizada por nombre de grupo de campo y nombre de propiedad como una función de fecha.

> **Nota:** La función ' `GET_CUSTOM_PROPERTY_FIELD_VALUE_BY_NAME` ' sustituye a la función ' `GET_CUSTOM_FIELD_VALUE_BY_NAME` ' en el fix pack 9.0.0.5 y posteriores.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

```
"OP_RESOURCES_MGR.GET_CUSTOM_PROPERTY_FIELD_VALUE_BY_NAME" (P1, P2, P3, P4, P5, P6, P7)
```

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del objeto para el que se devolverá el valor de campo personalizado. |
| P2 | Necesario. "A partir de la fecha" del campo personalizado. |
| P3 | Necesario. El nombre del grupo de campos que contiene el campo personalizado. |
| P4 | Necesario. El nombre de la propiedad personalizada. |
| P5 | Opcional. Utilizar solo la tabla de seguimiento de auditoría del sistema.<br>Posibles valores:<br>- **No**<br>  Se devolverá un valor para la propiedad independientemente de si está en la tabla de auditoría del sistema (valor predeterminado).<br>- **Sí**<br>  Sólo se devolverá un valor si éste se encuentra en la tabla de auditoría del sistema.<br>**Nota:** Cuando se crea por primera vez una propiedad, no se especifica un valor en la tabla de seguimiento de auditoría del sistema. |
| P6 | Opcional. Este parámetro determina el tipo de salida de esta función.<br>Posibles valores:<br>• EV_ID<br>• EV_CODE<br>• EV_SYSTEM_NAME<br>• EV_NAME_I18N<br>Valor predeterminado: EV_ID |
| P7 | Opcional. ID de configuración regional (como identificador numérico). Utilizado para traducir el texto de series enumeradas a la configuración regional del usuario que ejecuta el informe.<br>**Nota:** Se puede utilizar un valor de `NULL` (sin comillas); sin embargo, proporcionar el parámetro de sesión de entorno local o el ID de entorno local proporciona el mejor rendimiento de procesamiento. El uso de `NULL` obligará a la función a utilizar el ID de configuración regional predeterminado en todo el sistema.<br>Para devolver el parámetro de sesión que proporciona el valor de configuración regional del usuario que está ejecutando el informe, utilice la siguiente expresión:<br>`#$account.parameters.openPagesLocaleId#`<br>Valor predeterminado: `NULL` (sin comillas y no distingue entre mayúsculas y minúsculas) |

Se devuelve un valor de error si su solicitud es anterior a la creación de la variable.

##### Ejemplo de uso

El siguiente ejemplo muestra cómo obtener un valor de campo personalizado utilizando el grupo de campos y el nombre de propiedad. En este ejemplo, queremos obtener la clasificación de riesgo inherente como función de tiempo. Utilizamos la IU para buscar el nombre de grupo de campos para el objeto de riesgo que contiene la clasificación de riesgo inherente.

Una vez conocido el ' `propertydefId` ', hay que decidir el formato de la salida. El ejemplo muestra la salida como ' `EV_NAME_118N`, que es el nombre de la propiedad traducido al del ID de la configuración regional.

A continuación, vemos el código que hemos utilizado en este ejemplo:

```
"OP_RESOURCES_MGR.GET_CUSTOM_PROPERTY_FIELD_VALUE_BY_NAME" ([RI_RISK_ID], to_date(?Date?,'DD-MON-YYYY'), 'OPSS-Risk-Qual', 'Inherent Risk Rating', 'N', 'EV_NAME_I18N', #$account.parameters.openPagesLocaleId#)
```

Si selecciona la fecha 1-Jan-1970 (antes de que se creara el campo), obtendrá el siguiente resultado:

*Figura 1. Clasificación de riesgo inherente - 1-ene-1970*

![Tabla cruzada que muestra que no se encontró la clasificación de riesgo a 1 de enero de 1970.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_custom_as_of_date_4.jpg)

Como puede ver en los resultados, el valor actual de clasificación de riesgo es Medio, pero en la fecha solicitada, no se ha encontrado el valor.

Si selecciona la fecha 24-Feb-2021 (una fecha posterior a la creación del campo), obtendrá el siguiente resultado:

*Figura 2. Calificación del riesgo inherente - 24-Feb-2021*

![Tabla cruzada que muestra que la calificación de riesgo a 24 de febrero de 2011 era Baja.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_custom_as_of_date_5.jpg)

Ahora puede ver que en la fecha 24-Feb-2011, el valor de la clasificación de riesgo inherente era Bajo.

Si introduce la fecha de hoy20-Nov-2024), obtendrá el siguiente resultado:

*Figura 3. Calificación del riesgo inherente - 20-Nov-2024*

![Tabla cruzada que muestra que la calificación de riesgo. Ambas columnas muestran el valor Medio.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_custom_as_of_date_6.jpg)

El valor del campo es igual a la clasificación de riesgo inherente.

#### Obtención de la descripción del campo del sistema

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de las funciones dependientes del tiempo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-system-field-description)

Esta función devuelve el valor para la propiedad de descripción de un objeto como función de tiempo.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RESOURCES_MGR.GET_SYSTEM_FIELD_VALUE_DESC" (P1, P2, P3)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del objeto para el que se devolverá el valor de campo personalizado. |
| P2 | Necesario. "A partir de la fecha" del campo del sistema. |
| P3 | Opcional. Utilizar solo la tabla de seguimiento de auditoría del sistema.<br>Posibles valores:<br>- **No**<br>  Se devolverá un valor para la propiedad independientemente de si está en la tabla de auditoría del sistema (valor predeterminado).<br>- **Sí**<br>  Solo se devolverá un valor si el valor está en la tabla de seguimiento de auditoría del sistema.<br>**Nota:** Cuando se crea por primera vez una propiedad, no se especifica un valor en la tabla de seguimiento de auditoría del sistema. |

> **Nota:** Se devolverá un valor de error si la solicitud precede a la creación de la variable.

##### Ejemplo de uso 1

El ejemplo siguiente muestra el uso de esta llamada a función para obtener la propiedad de descripción del sistema como una función de tiempo. Se ha utilizado la siguiente expresión:

En el primer ejemplo, hemos obtenido el valor de descripción del sistema a partir del 1-Feb-2011. Esto es después de que se haya creado el objeto pero antes de que se haya modificado. El campo `Current Risk Description` siempre muestra el valor del campo tal como existe cuando se ejecuta el informe, que se muestra en la figura siguiente.

*Figura 1. Obtener valor de descripción del sistema - 1 de febrero de 2011*

![Tabla de referencias cruzadas que muestra el valor de descripción del sistema el 1 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_get_system_field_value_description_1.jpg)

##### Ejemplo de uso 2

En el ejemplo siguiente, que vemos en la figura siguiente, hemos obtenido el valor de descripción del sistema a partir del 11-Feb-2011. Observe que la descripción a partir de la fecha es ahora igual al valor de `Current Risk Description`. Esto es después de la modificación final del objeto.

*Figura 2. Obtener valor de descripción del sistema - 11 de febrero de 2011*

![Tabla de referencias cruzadas que muestra el valor de descripción del sistema el 11 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_get_system_field_value_description_2.jpg)

##### Ejemplo de uso 3

En el ejemplo final que vemos en la figura siguiente, hemos obtenido el valor de descripción del sistema a partir del 11-Feb-2009, antes de que existiera.

*Figura 3. Obtener valor de descripción del sistema - 11 de febrero de 2009*

![Tabla de referencias cruzadas que muestra el valor de descripción del sistema el 11 de febrero de 2009](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_8_get_system_description_value.jpg)

Vemos que el sistema devuelve un valor de error porque no se ha encontrado la propiedad.

#### Obtención de la vía de acceso completa del campo del sistema

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de las funciones dependientes del tiempo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-system-field-full-path)

Esta función devuelve el valor para la propiedad de vía de acceso completa de un objeto como función de tiempo.

##### Sintaxis

Esta función tiene la sintaxis `"OP_RESOURCES_MGR.GET_SYSTEM_FIELD_VALUE_FULLPTH" (P1, P2, P3)` donde la tabla siguiente describe las variables.

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del objeto para el que se devolverá el valor de campo personalizado. |
| P2 | Necesario. "A partir de la fecha" del campo del sistema. |
| P3 | Opcional. Utilizar solo la tabla de seguimiento de auditoría del sistema.<br>Posibles valores:<br>- **No**<br>  Se devolverá un valor para la propiedad independientemente de si está en la tabla de auditoría del sistema (valor predeterminado).<br>- **Sí**<br>  Solo se devolverá un valor si el valor está en la tabla de seguimiento de auditoría del sistema.<br>**Nota:** Cuando se crea por primera vez una propiedad, no se especifica un valor en la tabla de seguimiento de auditoría del sistema. |

> **Nota:** Se devolverá un valor de error si la solicitud precede a la creación de la variable.

##### Ejemplo de uso 1

El ejemplo siguiente muestra el uso de esta llamada a función para obtener la propiedad de vía de acceso completo al sistema como una función de tiempo. Se ha utilizado la siguiente expresión:

En el primer ejemplo, que se muestra en Figura 1, hemos obtenido el valor de vía de acceso completa del sistema a partir de 1-Feb-2011. Esto es después de que se haya creado el objeto pero antes de que se haya modificado.

*Figura 1. Obtener el valor de vía de acceso completa al sistema - Ejemplo 1*

![Tabla de referencias cruzadas que muestra la vía de acceso completa del sistema el 1 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_get_system_full_path_value_2.jpg)

##### Ejemplo de uso 2

En el ejemplo siguiente, que vemos en la figura siguiente, hemos obtenido el valor de vía de acceso completa al sistema a partir del 11-Feb-2011. Observe que la vía de acceso completa a partir de esa fecha equivale ahora al valor de vía de acceso completa actual. Esto es después de la modificación final de la vía de acceso completa.

*Figura 2. Obtener el valor de vía de acceso completa al sistema - Ejemplo 2*

![Tabla de referencias cruzadas que muestra la ruta completa del sistema el 11 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_get_system_full_path_value_3.jpg)

##### Ejemplo de uso 3

En el ejemplo final, que vemos en la figura siguiente, hemos obtenido el valor de vía de acceso completa del sistema a partir del 11-Feb-2009, antes de que existiera.

*Figura 3. Obtener el valor de vía de acceso completa al sistema - Ejemplo 3*

![Tabla de referencias cruzadas que muestra la ruta completa del sistema el 11 de febrero de 2009](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_get_system_full_path_value_1.jpg)

Vemos que el sistema devuelve un valor de error porque no se ha encontrado la propiedad.

#### Obtención del nombre de campo del sistema

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de las funciones dependientes del tiempo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-system-field-name)

Esta función devuelve el valor para la propiedad de nombre de un objeto como función de tiempo.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RESOURCES_MGR.GET_SYSTEM_FIELD_VALUE_NAME" (P1, P2, P3)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del objeto para el que se devolverá el valor de campo personalizado. |
| P2 | Necesario. "A partir de la fecha" del campo del sistema. |
| P3 | Opcional. Utilizar solo la tabla de seguimiento de auditoría del sistema.<br>Posibles valores:<br>- **No**<br>  Se devolverá un valor para la propiedad independientemente de si está en la tabla de auditoría del sistema (valor predeterminado).<br>- **Sí**<br>  Solo se devolverá un valor si el valor está en la tabla de seguimiento de auditoría del sistema.<br>**Nota:** Cuando se crea por primera vez una propiedad, no se especifica un valor en la tabla de seguimiento de auditoría del sistema. |

> **Nota:** Se devolverá un valor de error si la solicitud precede a la creación de la variable.

##### Ejemplo de uso 1

El ejemplo siguiente muestra el uso de esta llamada a función para obtener la propiedad de nombre del sistema como una función de tiempo. Se ha utilizado la siguiente expresión:

En el primer ejemplo, que se muestra en Figura 1, hemos obtenido el valor de nombre de sistema a partir de 1-Feb-2011. Esto es después de que se haya creado el nombre pero antes de que se haya modificado.

*Figura 1. Obtener valor de nombre del sistema - 1 de febrero de 2011*

![Tabla de referencias cruzadas que muestra el nombre del sistema el 1 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_system_field_value_name_1.jpg)

##### Ejemplo de uso 2

En el ejemplo siguiente, que se muestra en Figura 2, hemos obtenido el valor de nombre de sistema a partir de 11-Feb-2011. Observe que el Nombre a la fecha es ahora igual al Nombre actual del riesgo. Esto es después de la modificación final del nombre.

*Figura 2. Obtener valor de nombre del sistema - 11 de febrero de 2011*

![Tabla de referencias cruzadas que muestra el nombre del sistema el 11 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_system_field_value_name_2.jpg)

##### Ejemplo de uso 3

En el ejemplo final, que se muestra en Figura 3, hemos obtenido el valor de nombre de sistema a partir de 11-Feb-2009, antes de que existiera.

*Figura 3. Obtener valor de nombre del sistema - 11 de febrero de 2009*

![Tabla de referencias cruzadas que muestra el nombre del sistema el 11 de febrero de 2009](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_8_get_system_name_value_1.jpg)

Puede ver que no se ha encontrado el nombre del sistema.

#### Obtención del ID de carpeta padre del campo del sistema

`Guía del creador de informes › Uso de las funciones de base de datos predefinida › Uso de las funciones dependientes del tiempo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=functions-getting-system-field-parent-folder-id)

Esta función devuelve el valor para la propiedad de ID de carpeta padre de un objeto como función de tiempo.

##### Sintaxis

Esta función tiene la sintaxis siguiente:

`"OP_RESOURCES_MGR.GET_SYSTEM_FIELD_VALUE_PFLDRID" (P1, P2, P3)`

Donde:

**Tabla 1. Parámetros de función**

| Parámetro | Descripción |
| --- | --- |
| P1 | Necesario. El ID de objeto (un valor numérico) del objeto para el que se devolverá el valor de campo personalizado. |
| P2 | Necesario. "A partir de la fecha" del campo del sistema. |
| P3 | Opcional. Utilizar solo la tabla de seguimiento de auditoría del sistema.<br>Posibles valores:<br>- **No**<br>  Se devolverá un valor para la propiedad independientemente de si está en la tabla de auditoría del sistema (valor predeterminado).<br>- **Sí**<br>  Solo se devolverá un valor si el valor está en la tabla de seguimiento de auditoría del sistema.<br>**Nota:** Cuando se crea por primera vez una propiedad, no se especifica un valor en la tabla de seguimiento de auditoría del sistema. |

> **Nota:** Se devolverá un valor de error si la solicitud precede a la creación de la variable.

##### Ejemplo de uso 1

El ejemplo siguiente muestra el uso de esta llamada a función para obtener la propiedad de ID de la carpeta padre del sistema como una función de tiempo. Se ha utilizado la siguiente expresión:

```
"OP_RESOURCES_MGR.GET_SYSTEM_FIELD_VALUE_PFLDRID" ([RI_RISK_ID],
  to_date(?Date?,'DD-MON-YYYY'))
```

En este primer ejemplo, hemos obtenido el ID de la carpeta padre del sistema como 1-Feb-2011. Esto es después de que se haya creado el objeto pero antes de que se haya modificado de alguna forma. Podemos ver en Figura 1 que la modificación de un atributo en un objeto no afecta al ID de carpeta padre.

> **Nota:** Los tipos de objeto autocontenidos modifican la carpeta si cambia el nombre del objeto.

*Figura 1. Obtener el ID de la carpeta padre del sistema - 1 de febrero de 2011*

![Tabla de referencias cruzadas que muestra el ID de carpeta padre el 1 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_8_get_system_parent_folder_Id_3.jpg)

##### Ejemplo de uso 2

En el ejemplo siguiente, que se muestra en Figura 2, hemos obtenido el ID de carpeta padre del sistema a partir de 11-Feb-2011. Observe que una vez más, este valor no ha cambiado. Esto es después de la modificación final del nombre.

*Figura 2. Obtener el ID de la carpeta padre del sistema - 11 de febrero de 2011*

![Tabla de referencias cruzadas que muestra el ID de carpeta padre el 11 de febrero de 2011](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_8_get_system_parent_folder_Id_2.jpg)

##### Ejemplo de uso 3

En el ejemplo final, que se muestra en Figura 3, hemos obtenido el ID de carpeta padre del sistema a partir de 11-Feb-2009, antes de que existiera.

*Figura 3. Obtener el ID de la carpeta padre del sistema - 11 de febrero de 2009*

![Tabla de referencias cruzadas que muestra el ID de carpeta padre el 11 de febrero de 2009](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/cognos_8_get_system_parent_folder_Id_1.jpg)

Vemos que el sistema devuelve un valor de error porque no se ha encontrado la propiedad.

## Formateo de informes para salida

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-formatting-reports-output)

Además de la salida HTML estándar, los tres formatos de salida más populares son PDF, Excel y CSV.

Para poder utilizar los formatos de forma eficaz, este capítulo describe algunos métodos recomendados para formatear los informes para que aparezcan bien formateados en la salida.

### Configuración del informe para la salida de PDF

`Guía del creador de informes › Formateo de informes para salida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=output-setting-up-report-pdf)

Puede configurar el informe para la salida de PDF.

#### Procedimiento

1. Pulse **Archivo** > **Configuración de página PDF**.
2. En la página de configuración PDF, seleccione el modo vertical u horizontal dependiendo del tamaño y estilo del informe. Deje el tamaño de página predeterminado para no obligar a la impresora a tener un determinado tamaño de papel.

### Inclusión de solicitudes en línea para salida en PDF

`Guía del creador de informes › Formateo de informes para salida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=output-including-in-line-prompts-pdf)

Puede ver una solicitud de entidad de negocios en la salida en PDF.

#### Acerca de esta tarea

Las solicitudes en línea no aparecerán en un archivo PDF. Al convertir un informe en PDF, notará que la solicitud y el botón han desaparecido del formato.

#### Procedimiento

1. Coloque una segunda línea de cabecera en el informe con solo el nombre de solicitud y valor en la línea.
2. Cree una condición de serie utilizando **Explorador condicional** con el código siguiente:

   ```
   if (ReportOutput() starts with 'XL') 
   then ('XLS')
   else (ReportOutput())
   ```
3. Cambie el nombre de la variable por **Salida de informe**.
4. Añada como valores, XLS, PDF, HTML.
5. En **fila de tabla** con la solicitud en línea, establezca **Variable de estilo** en **Salida de informe**.
6. En **Explorador condicional**, seleccione **PDF** en **Salida de informe**.
7. En **Panel de propiedades**, en **Cuadro**, establezca **Tipo de recuadro** en **Ninguno**.
8. Repita los mismos pasos para la fila sin la solicitud en línea pero seleccione HTML en lugar de PDF.
9. Ejecute el informe en HTML.

#### Resultados

El informe se parece al que tenía antes en HTML. Ahora cuando lo convierte a PDF, ve la fila de solicitud que acaba de crear.

### Formateo del informe para la salida de PDF

`Guía del creador de informes › Formateo de informes para salida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=output-formatting-report-pdf)

El formateo del informe para la salida de PDF o para la salida de HTML comparte muchas de las técnicas de formateo. Cualquiera de las técnicas de formateo utilizadas para ajustar el diseño en una página HTML se puede utilizar para ajustar el formato de un archivo PDF. Si está utilizando salidas de HTML y PDF, debe decidir qué formato desea optimizar.

Si comienza con un informe sencillo que muestra un nombre de entidad hiperenlazada y la vía de acceso completa de la misma entidad, puede hacer cambios en el informe y mostrar cómo se reflejan en la salida de PDF.

#### Procedimiento

1. Establezca el font de la variable de vía de acceso completa en **Negrita**.
2. Establezca el ancho de la variable de nombres en 300 píxeles.
3. Establezca el borde en 1 1/2 puntos y rojo.
4. Ejecute el informe.

#### Resultados

Las técnicas de formateo básicas que utiliza para HTML también se aplican al formato PDF.

### Formato para salida de Microsoft Excel

`Guía del creador de informes › Formateo de informes para salida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=output-formatting-microsoft-excel)

Al diseñar un informe para que se formatee para el software de hoja de cálculo de Microsoft Excel, la limitación clave es que todos los contenedores del informe deben tener el mismo número de columnas.

Las hojas de cálculo de Microsoft Excel no dependen de valores de ancho de columna como un informe con formato PDF o HTML. Dependen estrictamente de la cantidad de columna para alinear un contenedor con otro.

Por lo tanto, cabeceras, pies de página, listas y tablas deben tener columnas ficticias añadidas a ellos para hacer que éstas se alineen en la salida. Estas columnas no requieren datos, solo necesitan salir.

Añadiendo columnas extra, la alineación de columnas del informe Excel mejora.

### Formateo para salida en CSV

`Guía del creador de informes › Formateo de informes para salida` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=output-formatting-csv)

El formato CSV (valores separados por comas) es el formato de salida más básico porque no hay formateo de estilo.

Este tipo de salida está diseñada para que salga de forma que la puedan leer otros sistemas. La única limitación conocida de este formato es que no puede tener uniones en la consulta o IBM® Cognos® producirá un error. Para evitar este problema, puede crear un CQS único que puede utilizar para la salida en CSV.

Al generarse el informe, aparecerá en formato Excel y se abrirá el cuadro de diálogo **Descarga de archivo**. Es parecido al cuadro de diálogo de Excel sin indicación de que es para un archivo CSV.

Cuando abra el archivo, verá que está formateado correctamente para CSV (mostrando dos columnas, con una segunda columna recortada debido a su tamaño). En el formateo en CSV, no puede tener recorte de palabras.

Para guardarlo en su formato final, pulse **Guardar como** y seleccione un nombre de archivo y el tipo de archivo como **CSV**.

Cuando abra el archivo TXT en el Bloc de notas, verá las comas que separan las dos columnas. Cuando hay una coma en sí misma en los datos, también puede ver las comillas dobles al principio de la segunda columna para algunos registros que indican que este problema se ha resuelto.

## Elaboración de informes

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-authoring-reports)

Esta sección describe las técnicas utilizadas para crear informes utilizando la infraestructura de IBM OpenPages® .

Proporciona un ejemplo detallado de las tareas utilizadas para desarrollar informes y cuándo aplicarlos.

### Valores manuales de IBM Cognos Configuration

`Guía del creador de informes › Elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-manual-cognos-configuration-settings)

Hay numerosos valores de entorno de IBM® Cognos® en IBM OpenPages®. Algunos de estos se han establecido mediante el instalador de OpenPages , mientras que otros se han establecido manualmente.

Esta sección describe los valores que deben configurarse manualmente.

#### Opciones de validación

De forma predeterminada, IBM Cognos mostrará mensajes de aviso cuando valide una fórmula o el informe completo. Tiene la opción de suprimirlos. Para ello, vaya a la barra de menús y pulse **Herramientas** > **Opciones de validación**.

Establezca el **Nivel de validación:** en **Error** y los mensajes de aviso ya no aparecerán.

#### Formatos de datos predeterminados

Si está desarrollando informes que requieren datos diseñados en determinados formatos, es posible que desee establecer los formatos de datos predeterminados en la plantilla del informe de proyecto. Para establecerlas, vaya a la barra de menús y pulse **Datos** > **Formatos de datos predeterminados**.

Establezca las propiedades predeterminadas de los tipos de elemento de datos así cuando inserta un elemento de ese tipo en el informe heredará estas propiedades.

### Configuración de informes

`Guía del creador de informes › Elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-configuring)

Hay numerosos elementos que deben configurarse en IBM OpenPages® antes de que pueda empezar el autor del informe.

La lista siguiente describe algunos de los elementos que debe tener en cuenta.

- **Modelos de entorno**

  La infraestructura de informes contiene un conjunto de modelos de infraestructura predefinidos, que se utilizan para los informes predefinidos que se suministran con OpenPages. Además de los modelos de infraestructura predefinidos, puede crear sus propios modelos de infraestructura. La capacidad de utilizar varios modelos de entorno permite dirigir un modelo de entorno a específicas, funciones de usuario, o perfiles de objeto específicos.

- **Espacios de nombres**

  Se le habrán proporcionado espacios de nombres OOB que dan soporte a los informes suministrados con OpenPages. Esto puede dar soporte o no a las necesidades de la elaboración de informes. Puede ampliar estos espacios de nombres o crear espacios de nombres completamente nuevos para satisfacer sus necesidades. Si define sus propios modelos de entorno, debe definir espacios de nombres para ellos. Los espacios de nombres son objetos globales.

- **Entornos locales**

  ¿A qué idiomas desea que dé soporte su infraestructura? Es un valor global que afecta a todos los espacios de nombres.

- **Triángulos**

  ¿Su informe necesita utilizar un triángulo debido a un objeto recursivo? Este valor se define a nivel global y de espacio de nombres.

- **Tablas auxiliares**

  ¿Necesita extraer tablas/CQS en un espacio de nombres para dar soporte a los informes? Se define a nivel de espacio de nombres.

- **Prefijos de objeto**

  Si se han añadido objetos personalizados al sistema, el prefijo de objeto se tiene que definir. Esto son valores globales.

- **Niveles de objeto recursivo de entidad de negocios**

  Estas son las jerarquías de entidad empresarial definidas por el usuario que se pueden utilizar para crear, por ejemplo, una estructura de informes legal frente a empresarial.

- **Niveles de objetos recursivos de entidad**

  ¿Qué niveles de objeto recursivo de entidad empresarial desea en cada espacio de nombres?

- **Creación de índice**

  Dependiendo del diseño del informe, es posible que tenga que añadir un índice al campo para mejorara el rendimiento. Esto sólo afectará a la tabla a la que añada el índice.

Además de los elementos configurables, también hay definiciones de campo personalizadas que se deben cargar para iniciar el desarrollo de informes. La siguiente lista describe algunos de estos elementos.

- **Grupos/Paquetes de campo**

  Son colecciones de campos que se asignan a un objeto.

- **Campos**

  Es la definición de un campo individual que ha solicitado el cliente para facilitar la configuración del sistema.

- **Valores de cadena enumerada**

  Hay una lista de los valores permitidos para series enumeradas.

Todos los elementos anteriores requieren que el entorno se regenere cada vez que se realiza un cambio en ellos. El objetivo aquí es investigar qué necesidades se van a definir, hacer cambios de configuración y, a continuación, generar el entorno.

### SQL de informe subyacente

`Guía del creador de informes › Elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-underlying-report-sql)

Debe tomar decisiones en relación con el tipo de construcción subyacente que se utilizará para crear el informe.

Debe tomar las siguientes decisiones.

- **Uso de espacios de nombres**

  Añada espacios de nombres para crear los informes.

- **Uso de los Asuntos de consulta personalizados (CQS)**

  Los archivos CQS deben utilizarse cuando el SQL subyacente que debe generarse no sigue el enfoque de arriba a abajo o requiere uniones entre objetos que son no estándar. La decisión de utilizar un CQS para un informe ya no se basa únicamente en el rendimiento esperado del informe. El modelo de entorno genera código SQL que se ejecuta igual o mejor que el que se puede crear a mano. La decisión se basa en si el entorno puede soportar la construcción de SQL subyacente para crear el informe.

Vamos a suponer que el informe que se va a crear utilizará espacios de nombres para crear el SQL subyacente. La creación de asuntos de consulta personalizados se explica en [Asuntos de consulta personalizados](#asuntos-de-consulta-personalizados).

### Uso de una plantilla de informe

`Guía del creador de informes › Elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-using-report-template)

El mejor lugar para empezar es con la plantilla de informe que se ha estado desarrollando durante la fase de requisitos de informe del proyecto. La plantilla refleja también el estilo en el que se deben desarrollar todos los informes para este proyecto.

Esta plantilla incluye fórmulas condicionales útiles, el diseño para la página de solicitudes, el diseño para la página de informe y asuntos de consulta predefinidos para entidades de negocios y periodos de creación de informes. Comenzando con una plantilla, es más probable que cree informes uniformes que los informes que puede editar cualquier autor de informes de su organización.

- La página de solicitudes contiene las dos solicitudes más habituales y su SQL subyacente. Estas solicitudes se obtienen a partir del espacio de nombres DEFAULT, si se utiliza otro espacio de nombres en este informe, ajuste el origen de estos campos de datos. Además, se ha establecido el espaciado predeterminado de las celdas de tabla.
- La página de informe tiene la cabecera configurada con el logotipo, el javascript para hiperenlaces cargado, el diseño de las subcabeceras definido, se ha añadido una lista ficticia y se ha configurado el pie de página.
- El logotipo está ubicado en la página como ejemplo para el cliente. Puede ir en los dos lados. Para sustituir el logotipo, debe sustituir el archivo logo.gif por el logotipo correcto en el servidor IBM® Cognos® .
- El objeto html contiene el javascript para los hiperenlaces. Si no utiliza hiperenlaces en este informe, puede eliminar el objeto. La lista ficticia contiene la parte de visualización del código de hiperenlace como una expresión definida en el objeto de hiperenlace.
- La cabecera está configurada para que se pueda *reducir*, por lo tanto, cuando desee que el informe sea más pequeño que la pantalla completa, los títulos se reducirán adecuadamente.
- No se ha configurado un valor de datos visualizados en el objeto de lista ficticio. Aparece cuando el usuario selecciona una combinación de solicitudes que no dan datos en el informe.
- Por último, el pie de página se ha configurado para que se pueda localizar. Los formatos de fecha y hora se configuran como genéricos para que IBM Cognos localice estos campos en función del entorno local asociado al inicio de sesión del usuario.
- Se han incluido fórmulas condicionales comunes en la plantilla:

  - **Localización**

    Esta fórmula se utiliza para traducir campos de texto a los idiomas soportados además del británico.

  - **Cabecera de informe**

    Puesto que no existe ningún concepto de cabecera de informe en IBM Cognos, esta fórmula simula una con la cabecera de página.

  - **Resaltado de fila**

    Se utiliza para resaltar una fila sí una no en un informe de lista. Esto solo es útil para informes de lista simples.

  - **Salida de informe**

    Se utiliza cuando necesita crear una condición dependiendo del tipo de salida de informe.

> **Nota:** Póngase en contacto con el responsable del proyecto para obtener una copia de la plantilla IBM OpenPages® .

### Organización del asunto de consulta

`Guía del creador de informes › Elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-query-subject-organization)

Al crear asuntos de consulta para informes, debe seguir varios directrices.

Al crear asuntos de consulta para informes, se deben observar las siguientes directrices:

- Coloque las consultas de solicitud al final de la página. Se utilizan con poca frecuencia y no desea desplazarse constantemente por ellas.
- Coloque las consultas de soporte para una unión directamente bajo esa construcción. Hace que sean más fáciles de encontrar.
- Ponga nombre a los asuntos de consulta de una forma lógica para que el siguiente autor de informe pueda entender el informe.

Normalmente, los asuntos de consulta se diseñan desde el final hasta el principio, con las consultas más detalladas al final y las consultas más agregadas al principio, tal como se muestra en la Figura 1. La idea es llenar los asuntos de consulta con los valores que se necesitan para cumplir los requisitos del informe. Las construcciones como filtros se colocan en el asunto de consulta del nivel más bajo de la jerarquía para acelerar el rendimiento.

*Figura 1. Hijos del asunto de consulta*

![Paneles que muestran los elementos hijo de un asunto de consulta, incluidos elementos de datos, filtros de detalles y filtros de resumen](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_query_subject_child.jpg)

Este ejemplo muestra la siguiente información:

- Hay campos incluidos en el informe del objeto de entidad de negocios y del objeto riesgo.
- Hay elementos de datos personalizados añadidos a esta consulta.
- Hay filtros añadidos a esta consulta porque es la consulta hijo del informe.

Cuando crea cada asunto de consulta, debe comprobar los datos que se están produciendo para asegurarse de que se extraen los datos correctos de la base de datos y no se incluyen datos duplicados. Haciendo esto en cada asunto de consulta, aumenta la calidad de lo que está construyendo y mejora su comprensión de cómo se están construyendo los datos. Debe tener en cuenta que IBM OpenPages® es un sistema muy flexible que permite una cantidad ilimitada de configuración. Si su comprensión del modelo de datos difiere de la comprensión del cliente, tendrá resultados erróneos.

Puede producir una salida desde cualquiera de los asuntos de consulta seleccionando un elemento en el asunto de consulta y utilizando la opción **Ver datos tabulares**. Esto dará las solicitudes que están incluidas en el asunto de consulta (y cualquier asunto de consulta que es hijo del asunto de consulta que está visualizando). Para llevar a cabo esta acción, seleccione lo siguiente desde el menú **Ejecutar**.

Aparecerá una página de solicitudes que tendrá que llenarse con valores válidos y la salida del asunto de consulta se visualizará en un formato de lista básico. Esto muestra todos los datos que devuelve la consulta de la base de datos y puede revisarlos para determinar si son los datos que esperaba.

### Construcciones de asunto de consulta

`Guía del creador de informes › Elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-query-subject-constructs)

Todos los objetos autónomos deben unirse manualmente junto con los objetos primarios que deben unirse debido a la complejidad de un informe.

Además, algunas de las construcciones se han actualizado. En las uniones de instancia, ahora puede manejar más de dos asuntos de consulta. Esto crea SQL más eficiente que en las versiones anteriores de IBM® Cognos®.

La unión ahora también incluye las siguientes propiedades:

- **Operación de conjunto**

  Permite al usuario cambiar la operación a otro tipo de operador de conjunto. Esto debe establecerse siempre en **Unión**.

- **Duplicados**

  Determina si se eliminan las filas duplicadas del conjunto de resultados. Normalmente se establece en **Eliminar**.

- **Lista de proyecciones**

  Determina si el conjunto de elementos de datos que es resultado de esta unión se genera automática o manualmente. Se recomienda que esté siempre establecido en **Generado automáticamente**. Esto se debe a problemas que hemos visto cuando no se han incluido todos los elementos del conjunto de datos en el conjunto de resultados (cuando la selección se realizó manualmente) y ha provocado problemas de validación.

### Dar formato a tablas o listas vacías

`Guía del creador de informes › Elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-formatting-empty-tables-lists)

Un problema que debe abordarse es el de las listas, tablas y tablas de referencias cruzadas vacías en un informe. Si el contenedor primario no devuelve datos, utilizando la propiedad **No contiene datos** del contenedor se informará al usuario de que se han elegido valores de solicitud que no proporcionan ningún dato. La segunda situación es cuando tiene una subtabla o lista en un informe y no tiene datos en ella cuando se ejecuta el informe. Lo que ve es una cabecera y nada más.

#### Acerca de esta tarea

En el ejemplo siguiente, tenemos un informe que muestra información de entidad, y en el pie de página de la lista visualizamos una lista de problemas unidos a esa entidad. Cuando ejecutamos por primera vez el informe, vemos lo siguiente, que se muestra en Figura 1:

*Figura 1. Sección en blanco mostrada*

![Lista que muestra algunas secciones en blanco](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_hiding_blank_sections_1.jpg)

Lo que vemos es que en la primera sección hay un problema listado mientras que en las secciones segunda y tercera no se han encontrado datos y aparece la cabecera de la lista.

#### Procedimiento

1. Utilizando la **Explorador de condiciones**, realice los pasos siguientes.

   1. Cree un nuevo **Variable booleana**.
   2. En la variable booleana, introduzca la fórmula siguiente:

      ```
      [Issue].[IS_ISSUE_ID] is missing or
      [Issue].[IS_ISSUE_ID] is null
      ```
   3. Pulse **Aceptar**.
   4. En el panel **Propiedades** , en **Varios**, establezca la propiedad **Nombre** en **Ocultar títulos**.
2. En la página de informe principal, realice los siguientes pasos.

   1. Seleccione una cabecera de lista en la lista de problemas.
   2. Utilizando el selector de ancestros, seleccione **Estilo de título de columnas de lista.**
   3. En el panel **Propiedades** , en la sección **Condicional** , establezca **Variable de estilo** en **Ocultar títulos**.
3. En la **Explorador de condiciones**, realice los pasos siguientes.

   1. Seleccione **Sí** bajo la variable **Ocultar títulos** .
   2. En el panel **Propiedades** , en la sección **Cuadro** , establezca **Tipo de recuadro** en **Ninguno**.
4. Ejecute el informe.

#### Resultados

Lo que ahora ve, que se muestra en Figura 2, cuando ejecuta el informe es que el título de cabecera de lista se ha eliminado cuando no hay elementos de datos en la lista.

*Figura 2. Ocultar lista en blanco*

![Lista que no incluye secciones en blanco](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_hiding_blank_sections_3.jpg)

## Campos calculados

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-computed-fields)

Los campos calculados proporcionan la capacidad de definir campos en un objeto cuyo valor se calcula a partir de los valores de otros campos. Estos otros campos pueden existir en el mismo objeto o en otro objeto relacionado. Estos cálculos estarán disponibles en la aplicación así como para fines de creación de informes.

Loa campos calculados se definen en la interfaz de usuario de la aplicación. Para obtener información sobre cómo definir un nuevo campo calculado, consulte la publicación *IBM OpenPages Guía del administrador* o póngase en contacto con el administrador del sistema para obtener ayuda.

### Limitaciones de los campos calculados

- Existe una limitación en el tamaño del valor del atributo de cálculo que puede almacenar la aplicación. El atributo de preocupación principal es **Ecuación** donde una ecuación nivelada compleja puede ser muy larga.

  Hay un límite de 20.000 bytes en el tamaño del texto entrado. Tenga en cuenta que la aplicación soporta caracteres multibyte y así que puede que esto no sea equivalente a 20.000 caracteres.

  Si se necesitan más de 20.000 bytes de información para la ecuación, debe crear el cálculo en el archivo de asunto de consulta personalizado tal como se describe en [Creación de cálculos](#creación-de-cálculos).
- Al explorar todas las posibilidades de cálculo, hay una gran diferencia en lo que se debe hacer. Aunque es posible consultar el árbol de relaciones (es decir, calcular valores en base a los ancestros) se desaconseja totalmente.

  La generación de entorno automática se configura de tal manera que crea uniones que favorecen un mejor rendimiento consultando hacia abajo el árbol de relaciones.

  > **Nota:** Una consulta hacia arriba en el árbol dará como resultado un rendimiento de campo calculado erróneo, así como una gran carga en la base de datos que puede hacer que se ralentice toda la aplicación.
- Los campos calculados pueden actuar algunas veces como bloques de creación para otros campos calculados. Se describen como cálculos intermedios. Actualmente, la aplicación IBM OpenPages® no da soporte a definiciones de cálculo intermedias a través de la interfaz de usuario de la aplicación. Si desea hacer referencia a otro campo calculado, debe duplicar la ecuación utilizada en ese campo calculado dentro de la ecuación para el campo actual.

  Ejemplo

  Por ejemplo, si tenemos un campo calculado `A` y lo definimos como `A = B * C` y también conocemos `C = D + E`, solo crearíamos un campo calculado `A` en la aplicación, donde la ecuación sería `B * (D + E)`. Aunque este enfoque puede ser muy prolijo, algunas veces es el más sencillo.
- Las definiciones utilizadas en un campo calculado deben estar presentes en el espacio de nombres que está utilizando y deben estar relacionados con el objeto dentro del que está creando el campo calculado. Es posible crear un campo calculado que se validará en el formulario pero no dará ningún resultado debido a esta limitación.

### Consideraciones sobre el diseño

Tenga en cuenta lo siguiente al diseñar el campo calculado:

- **Localización**

  Todos los tipos de datos calculados se localizarán mediante la aplicación, excepto Serie simple, que debe localizarse como parte del cálculo (ecuación).

- **Campos calculados dependientes**

  Cálculo que utiliza otro cálculo como parte de su ecuación no se admite.

- **Cálculo entre productos**

  Al escribir un cálculo que se agrega entre varios tipos de objetos, habitualmente nos encontramos con un problema en el que algunos objetos se cuentan varias veces y por lo tanto debe tenerlo en cuenta .

- **Manejo de valores nulos**

  Al escribir una ecuación debe tener en cuenta que si parte de la ecuación se evalúa como nulo y se utiliza en alguna otra operación aritmética, la segunda operación también devolverá nulo. La solución a este problema es la función `nvl()` que toma dos argumentos: una expresión para evaluar y comprobar si es nulo y un valor a utilizar en el caso de que sea nulo. Por ejemplo:

  ```
  average (nvl(Loss Impacts, 0) for Loss Events) * count 
         ( nvl(distinct Loss Impacts for Loss Events, 0)) 
  ```

### Creación de un campo calculado

`Guía del creador de informes › Campos calculados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-creating-computed-field)

Puede crear un campo calculado.

#### Procedimiento

1. Cree un nuevo informe de lista.
2. Añada los siguientes elementos de consulta a la lista:

   - ```
     DEFAULT|DEFAULT_REL|GRC_OBJECTS|[SOXRISK]|ID_FIELDS|
         [RI_REPORTING_PERIOD_ID]
     ```
   - ```
     DEFAULT|DEFAULT_REL|GRC_OBJECTS|[SOXRISK]|ID_FIELDS|[RI_RISK_ID]
     ```
3. Pulse la pestaña **Caja de herramientas** ![Icono de caja de herramientas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-toolbox.jpg) en el panel **Objetos insertables** .
4. Arrastre y suelte un objeto **Cálculo de consulta** en **lista**.
5. Asigne un nombre al cálculo de consulta `Computed Field`.
6. En el panel **Definición de expresión** , especifique la expresión siguiente:

   ```
   total([DEFAULT_REL].[SOXRISK].[RI_INHERENT_SEVERIT_BA] for
    [DEFAULT_REL].[SOXRISK].[RI_RISK_ID]) / 100 
   ```
7. Pulse el icono **Validar** ![Icono Validar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) para validar la expresión y, a continuación, pulse **Aceptar**.

   El informe debería ser similar al siguiente ejemplo:

   *Figura 1. Campo calculado añadido a un informe de lista*

   ![Lista que muestra el resultado de esta tarea, incluido un campo calculado](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/Cognos_8_computed_field_2.jpg)
8. Ejecute el informe.

### Suministro de campos necesarios

`Guía del creador de informes › Campos calculados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-supplying-required)

Para que el administrador del sistema pueda crear el campo calculado en IBM OpenPages®, debe proporcionar los campos siguientes: Ecuación, Espacio de nombres primario, Espacios de nombres alternativos, Columna de ID de objeto, Columna de ID de periodo de elaboración de informes y Nombre de paquete.

Cree los siguientes campos.

- **Ecuación**

  La ecuación es el SQL utilizado para definir el valor calculado para el campos de objeto. Puede ser una referencia a un elemento de datos existente del entorno publicado o una ecuación que implica varios elementos de consulta.

- **Espacio de nombres principal**

  El espacio de nombres principal es el espacio de nombres del entorno al que se añadirá el cálculo durante la generación de entorno de elaboración de informes.

  > **Nota:** Todos los elementos de consulta referenciados en los valores para **Ecuación**, **Columna de ID de objeto**y **Columna de ID de periodo de elaboración de informes** deben estar en el mismo espacio de nombres.

- **Espacios de nombres alternativos**

  El espacio de nombres alternativo es otro espacio de nombres de entorno al que se añadirá el cálculo durante la generación de entorno de elaboración de informes.

- **Columna ID de objeto**

  La columna ID de objeto es una referencia a un elemento de consulta de entorno que contiene el ID de recurso del tipo de objeto del campo calculado. Este valor debe ser el mismo para todos los campos calculados en un espacio de nombres determinado para un tipo de objeto.

- **Columna ID de periodo de elaboración de informes**

  La columna de ID de periodo de elaboración de informes es el elemento de consulta de entorno que contiene el ID del periodo de elaboración de informes del tipo de objeto del campo calculado. Este valor debe ser el mismo para todos los campos calculados en un espacio de nombres determinado para un tipo de objeto.

  > **Nota:** El ID de recurso y el ID de periodo de creación de informes deben coincidir dentro del grupo de campos y el tipo de objeto. Si estos valores no coinciden, la validación fallará.

- **Nombre de paquete**

  El nombre del paquete define el paquete de informes contra el que se ejecuta el cálculo. Si el nombre de paquete está vacío, se utiliza el paquete para el modelo de entorno `Platform_Reporting`.

### Creación de un archivo de datos

`Guía del creador de informes › Campos calculados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-creating-data-file)

Para obtener los valores de campo necesarios, el mejor método es cortar y pegar los valores a un archivo de texto y enviarlos al administrador del sistema para que se pueda crear el campo. Siga este procedimiento para obtener los valores.

#### Procedimiento

1. Al principio del archivo, cree una etiqueta denominada **Nombre** y asigne un nombre al campo calculado.
2. Cree una etiqueta denominada **Descripción** y especifique un valor para la descripción del campo calculado.
3. Efectúe una doble pulsación en la columna **Campo calculado** .
4. Corte y pegue la ecuación desde el panel **Definición de expresión** en un archivo de texto. Asegúrese de etiquetarlo como **Expresión** en el archivo.
5. Pulse **Cancelar**.
6. Cree una etiqueta para **Espacio de nombres primario** y especifique el nombre del espacio de nombres en el archivo de texto. Este es el espacio de nombres de nivel superior, no el subespacio de nombres.
7. Si hay **Espacios de nombres alternativos** que utilizará este cálculo, cree el elemento adecuado en el archivo de texto.
8. Repita los pasos del 3 al 5 para los campos **ID de objeto** y **Periodo de elaboración de informes** etiquetándolos adecuadamente en el archivo de texto.

#### Resultados

Ahora debe enviar el archivo de texto al administrador del sistema y pueden añadir el campo calculado al sistema. Las instrucciones para hacerlo se encuentran en la publicación *IBM OpenPages Guía del administrador*.

### Uso de campos calculados en varios espacios de nombres

`Guía del creador de informes › Campos calculados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-using-computed-in-multiple-namespaces)

En la aplicación IBM OpenPages® , permitimos varios tipos de objeto padre para un tipo de objeto hijo determinado.

Esto no es cierto en IBM® Cognos® para un espacio de nombres determinado debido a algunas de las limitaciones técnicas de IBM Cognos. Por ejemplo, en el espacio de nombres ORM, la única vía de acceso a un evento de pérdida es a través de una entidad de negocio. Esto significa que si un evento de pérdida está asociado a un riesgo, pero no a una entidad de negocio, ese evento de pérdida no se mostrará en las consultas en ese espacio de nombres. Para encontrar una solución a este problema introducimos varios espacios de nombres donde cada uno de los espacios de nombres tiene una vía de acceso diferente a un tipo de objeto.

Para que los cálculos estén disponibles en varios espacios de nombres para los autores de informe, tenemos el campo Espacios de nombres adicionales. Esta es una lista de espacios de nombres alternativos delimitada por comas para la que se debe crear un objeto Cálculo durante el proceso de generación de entorno. Durante este proceso, se crea primero un objeto Cálculo para el espacio de nombres primario utilizando el valor del atributo Ecuación. A continuación, se crean otros objetos de cálculo en otros espacios de nombres tomando la ecuación y sustituyendo los espacios de nombres alternativos para el espacio de nombres primario.

> **Importante:** Una ecuación puede ser válida en un espacio de nombres pero no válida en otros. En la mayoría de los casos esto no es un problema, pero si el nombre del asunto de consulta o el nombre del elemento de consulta varía entre los espacios de nombres, es posible que tenga que crear instancias del campo calculado separadas con ecuaciones diferentes.

## Fragmentos de elaboración de informes

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-reporting-fragments)

Un fragmento de elaboración de informes es normalmente un gráfico, una tabla de referencias cruzadas o una lista que se puede colocar en una página de la aplicación para que el usuario pueda ver una representación visual de los datos al lado de los datos de página.

### Limitaciones en los fragmentos de elaboración de informes

Los fragmentos de elaboración de informes tienen las siguientes limitaciones:

- Los saltos de página no se admiten.
- Las ayudas contextuales no se admiten.
- No se puede utilizar un informe que tiene solicitudes necesarias distintas del ID de objeto y el ID de periodo de elaboración de informes.
- Las solicitudes en línea en la página de informe no se admiten.
- No puede establecer el color de fondo de un fragmento en transparente.
- El método para implementar CrossTracks es diferente en un fragmento de elaboración de informes.
- Solo puede haber un fragmento de elaboración de informes en un informe. La colocación de varios fragmentos de elaboración de informes en un único informe provocará que todos los fragmentos se ejecuten cada vez que se ejecuta un solo fragmento en la IU.
- El fragmento solo se puede utilizar con el objeto que se está pasando al informe como solicitud.
- Los accesos a detalles no se admiten.
- La propiedad **No contiene datos** no funciona para los contenedores de datos.

### Creación de fragmentos de elaboración de informes

`Guía del creador de informes › Fragmentos de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fragments-creating-reporting)

Los fragmentos de elaboración de informes se desarrollan de la misma manera que los de un informe. Un fragmento de elaboración de informes es un contenedor de datos único (probablemente un gráfico o una lista) con datos. No hay cabeceras, pies de página u otros adornos.

El fragmento de informe, cuando se representa en la aplicación, es una imagen (en el caso de un gráfico) o una tabla HTML en el caso de una lista o una tabla de referencias cruzadas. La única función interactiva que está disponible es un hiperenlace que se describe en la siguiente sección.

Hay unos cuantos requisitos al crear el fragmento:

- Debe pasar un ID de recurso al fragmento. En el informe, esto tendrá la forma de un filtro:

  ```
  [DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_ENTITY_ID] = ?Business Entity?
  ```
- También debe pasar el ID de periodo de elaboración de informes al informe. Una vez más, tomará la forma de un filtro:

  ```
  [DEFAULT_REL].[SOXBUSENTITY_GPC].[GEN_REPORTING_PERIOD_ID] = 
  ?Reporting Period ID?
  ```
- Tendrá que proporcionar un nombre al elemento de informe que desee publicar como fragmento:

  1. Seleccione el contenedor de datos (gráfico, lista o tabla de referencias cruzadas) y utilizando un selector en el panel **Propiedades**, seleccione el contenedor.
  2. Bajo la categoría **Varios**, establezca la propiedad **Nombre** en listaPrincipal o lo que prefiera.

El último elemento tiene que ver con la configuración del alto y el ancho del fragmento. Hay dos formas:

- Estableciendo la altura y el ancho en el informe del contenedor de datos. Funciona mejor con listas y tablas de referencias cruzadas.
- Estableciendo la altura y la anchura en la aplicación IBM OpenPages® cuando se define el campo de fragmento de elaboración de informes. Esto funciona mejor con gráficos.

### Uso de CrossTracks en fragmentos de elaboración de informes

`Guía del creador de informes › Fragmentos de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fragments-using-crosstracks-in-reporting)

Los CrossTracks se admiten en los fragmentos de elaboración de informes. Sin embargo, la forma en que normalmente creamos enlaces CrossTrack (con un objeto Hyperlink en IBM® Cognos®) no funciona a partir de fragmentos de informes.

Para obtener funcionalidad crosstrack, tendrá que utilizar etiquetas HTML en lugar de hiperenlaces.

#### Creación de un enlace Abrir en la misma ventana

`Guía del creador de informes › Fragmentos de elaboración de informes › Uso de CrossTracks en fragmentos de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fragments-creating-link-open-in-same-window)

Puede crear un hiperenlace en un fragmento de elaboración de informes que se abra en la misma ventana de navegador.

> **Sugerencia:** En este ejemplo, estamos utilizando el objeto Riesgo, pero puede sustituir cualquier objeto.

##### Procedimiento

1. Utilizando el **Explorador de consultas**, seleccione la consulta principal para el fragmento de creación de informes.
2. En el informe de lista existente, arrastre y suelte un **elemento HTML** como columna en el informe y realice los pasos siguientes.

   1. En el panel **Propiedades** , en **Origen HTML**, establezca la propiedad **Tipo de origen** en **Expresión**.
   2. En la propiedad **Expresión de informe** , especifique lo siguiente:

      ```
      '<a href="' + [DEFAULT_REL].[SOXRISK].[RI_DETAIL_PAGE_URL] + '">' + 
          [DEFAULT_REL].[SOXRISK].[RI_NAME00] + '</a>' 
      ```
   3. Pulse **Aceptar**.
3. Seleccione el texto del título de columna y, en el panel **Propiedades** , en **Origen de texto**, establezca la propiedad **Texto** en **Nombre de riesgo**.
4. Corte la columna Nombre de riesgo original del informe.
5. Para convertir RI_NAME00 en una propiedad de la lista, realice los siguientes pasos.

   1. Seleccione el objeto **Lista** en la página principal del informe.
   2. En el panel **Propiedades** bajo la categoría **Datos** , efectúe una doble pulsación en **Propiedades**.
   3. Seleccione `[RI_NAME00]`.
   4. Pulse **Aceptar**.
6. Guarde el informe.
7. Pida al administrador del sistema que configure un campo de fragmento de elaboración de informes para este informe.

##### Resultados

Cuando el campo de fragmento de informes se ejecuta en IBM OpenPages®, aparecerá como un widget en la vista.

Cuando haga clic en CrossTrack,, accederá a la vista de tareas del objeto en la misma ventana.

#### Creación de un enlace a abierto en una ventana nueva

`Guía del creador de informes › Fragmentos de elaboración de informes › Uso de CrossTracks en fragmentos de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fragments-creating-link-open-in-new-window)

Puede crear un hiperenlace en un fragmento de creación de informes que abra la vista de tareas del objeto en una ventana de navegador nueva.

##### Procedimiento

1. En el Explorador de consultas, realice los siguientes pasos.

   1. Arrastre y suelte un **Elemento de datos** en el panel **Elementos de datos** .
   2. En el panel **Propiedades** , en la categoría **Elemento de datos** , efectúe una doble pulsación en la propiedad **Expresión** .
   3. Escriba la siguiente expresión:

      ```
      '<a href="#"' + ' onclick="' + 'javascript:window.open(' + chr(39) + 
          [DEFAULT_REL].[SOXRISK].[RI_DETAIL_PAGE_URL] + chr(39) + ')' + '">' + 
              [DEFAULT_REL].[SOXRISK].[RI_NAME00] + '</a>'
      ```
   4. Establezca la propiedad **Name** en **URL Info**.
   5. Establezca la **Función de agregación** en **Ninguna**.
   6. Establezca la **Función de agregación de resumen** en **Ninguna**.
   7. Pulse **Aceptar**.
2. En la página principal del informe de lista, arrastre y suelte un **Elemento HTML** como columna en el informe y realice los pasos siguientes.

   1. En el panel **Propiedades** , en **Origen HTML**, establezca la propiedad **Tipo de origen** en **Valor de elemento de datos**.
   2. Establezca la propiedad **Valor del elemento de datos** en **Información de URL**.
   3. En el panel **Propiedades** , en **Origen de texto**, establezca la propiedad **Texto** en **Nombre de riesgo**.
3. Corte la columna Nombre de riesgo original del informe.
4. Para convertir a RI_DETAIL_PAGE_URL en una propiedad de la lista, realice los siguientes pasos.

   1. Seleccione el objeto **Lista** en la página principal del informe.
   2. En el panel **Propiedades** bajo la categoría **Datos** , efectúe una doble pulsación en **Propiedades**.
   3. Seleccione `[RI_DETAIL_PAGE_URL]`.
   4. Pulse **Aceptar**.
5. Guarde el informe.
6. Pida al administrador del sistema que configure un campo de fragmento de elaboración de informes para este informe.

##### Resultados

Cuando el fragmento de creación de informes se ejecuta en IBM OpenPages®, aparecerá como un widget en la vista.

Cuando pulse el enlace CrossTrack , le llevará a la vista de tarea de objeto en una nueva ventana emergente.

### Suministro de campos de configuración

`Guía del creador de informes › Fragmentos de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fragments-supplying-configuration-fields)

Para que el administrador del sistema pueda crear el campo de fragmento en la aplicación IBM OpenPages® , debe proporcionar los campos siguientes: **Vía de acceso de informe**, **Nombre de fragmento**, **Solicitud de ID de objeto**, **Solicitud de ID de periodo de creación de informes**, **Altura**y **Anchura**.

Cree los siguientes campos.

- **Ruta de informe**

  La ubicación del informe en el repositorio de CommandCenter . Consulte [Obtención de la vía de acceso del informe](#obtención-de-la-vía-de-acceso-de-informe).

- **Nombre de fragmento**

  El nombre del elemento de informe que se va a visualizar en el fragmento de elaboración de informes. Suele ser el nombre de un contenedor de datos. Consulte [Obtención del nombre de fragmento](#obtención-del-nombre-de-fragmento).

- **Solicitud de ID de objeto**

  El nombre de la solicitud de ID de objeto en el informe. Es un campo opcional. Consulte [Obtención de solicitudes de objeto](#obtención-de-solicitudes-de-objeto).

- **Solicitud de ID de periodo de elaboración de informes**

  El nombre de la solicitud del periodo de elaboración de informes. Es un campo opcional. Consulte [Obtención de solicitudes de objeto](#obtención-de-solicitudes-de-objeto).

- **Altura** Y **Anchura**

  La altura y ancho del área de visualización en píxeles. Normalmente, solo se utiliza cuando se está visualizando una lista. Consulte [Obtención de altura y anchura](#obtención-de-altura-y-anchura).

Para obtener los valores anteriores, el mejor método es cortar y pegar los valores de CommandCenter en un archivo de texto y enviarlos al administrador del sistema. Cree etiquetas en el archivo de texto correspondientes a los campos anteriores. Inicie el archivo de texto con un campo **Nombre** y **Descripción** para el fragmento de elaboración de informes.

#### Obtención de la vía de acceso de informe

`Guía del creador de informes › Fragmentos de elaboración de informes › Suministro de campos de configuración` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-obtaining-report-path)

Puede obtener la **Vía de acceso de informe** para un fragmento de creación de informes.

##### Procedimiento

1. En el portal de elaboración de informes, vaya a la carpeta con el informe de fragmento de elaboración de informes.
2. Pulse el icono **Establecer propiedades** .
3. Haga clic en el hipervínculo **Ver la ruta de búsqueda, ID y URL**.
4. En la ventana emergente, corte y pegue **Vía de acceso de búsqueda** en el archivo de texto como **Vía de acceso de informes**.
5. Pulse **Cerrar**.

#### Obtención del nombre de fragmento

`Guía del creador de informes › Fragmentos de elaboración de informes › Suministro de campos de configuración` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-obtaining-fragment-name)

Puede obtener el **Nombre de fragmento** para un fragmento de creación de informes.

##### Procedimiento

1. Seleccione la página principal del informe.
2. Seleccione el elemento de informe que desea visualizar en el fragmento. Será una lista, un gráfico o una referencia cruzada.
3. En **Panel de propiedades** bajo **Varios**, corte y pegue la propiedad **Nombre** en el archivo de texto.

#### Obtención de solicitudes de objeto

`Guía del creador de informes › Fragmentos de elaboración de informes › Suministro de campos de configuración` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-obtaining-object-prompts)

Puede obtener una **Solicitud de ID de objeto** para un fragmento de elaboración de informes.

##### Procedimiento

1. Si no existe una página de solicitud, seleccione el asunto de consulta principal del fragmento en **Explorador de consultas** y busque el nombre de solicitud en uno de los filtros. Sáltese el resto de esta selección.
2. De lo contrario, utilice **Explorador de páginas** y vaya a la página de solicitud. Seleccione el control que contiene la **Solicitud de ID de objeto**.
3. En **Panel de propiedades** bajo **General**, corte y pegue la propiedad **Parámetro** en el archivo de texto.
4. Repita el paso 3 para obtener el **Solicitud de ID de periodo de creación de informes** (si existe).

#### Obtención de altura y anchura

`Guía del creador de informes › Fragmentos de elaboración de informes › Suministro de campos de configuración` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fields-obtaining-height-width)

Los parámetros de altura y anchura son opcionales. Si el informe es un gráfico, los valores pueden quedar en blanco y el gráfico se escalará automáticamente. Si el informe es una lista o referencia cruzada, determine una **Altura** y **Anchura** óptimas para minimizar el desplazamiento.

### Uso de imágenes en Fragmentos de elaboración de informes

`Guía del creador de informes › Fragmentos de elaboración de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=fragments-using-images-in-reporting)

Puede insertar una imagen en un informe que se utiliza en Fragmentos de elaboración de informes.

#### Antes de empezar

Las imágenes que inserte primero deben cargarse en el servidor de IBM® Cognos® Analytics y en el servidor de IBM OpenPages® . El formato de las imágenes debe ser gif o jpg.

#### Acerca de esta tarea

Después de cargar la imagen, debe utilizar una vía de acceso relativa para hacer referencia a la imagen. La vía de acceso relativa debe ser válida tanto en el servidor de IBM Cognos Analytics como en el servidor de IBM OpenPages .

Siga estas prácticas recomendadas:

- Copie la imagen en las carpetas siguientes:

  - `<COGNOS_HOME>\webcontent\bi\images`
  - `<OP_HOME>/wlp-usr/shared/apps/op-apps.ear/sosa.war/images`
- Acceda a la imagen del informe que se utiliza para el fragmento de informe mediante la vía de acceso relativa `../images/<image file name>`.

## Asuntos de consulta personalizados

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-custom-query-subjects)

Los asuntos de consulta personalizados (CQS) son una característica que ofrece IBM OpenPages® para que un autor de informes pueda crear una sentencia SQL definida por el usuario para resolver un problema que no se puede resolver mediante el uso de la infraestructura. El modelo de entorno de fábrica representa un entorno que normalmente resuelve la mayoría de las necesidades de creación de informes del cliente; el resto se resuelven utilizando asuntos de consulta personalizados.

La lista que figura a continuación describe el flujo de proceso para la creación de informes utilizando un asunto de consulta personalizado

1. [Revise el documento de diseño de informe](#revisión-del-diseño-de-informe).
2. [Cree un diagrama ER de los objetos necesarios](#creación-de-un-diagrama-entidad-relación).
3. [Crear sentencias SQL en la herramienta de desarrollo SQL](#creación-de-una-sentencia-sql).
4. [Añadir funciones de base de datos OpenPages](#adición-de-funciones-de-base-de-datos).
5. [Variables de sustitución](#sustitución-de-variables).
6. [Completar pruebas en la herramienta de desarrollo SQL](#prueba-de-la-sentencia-sql).
7. [Cree un nuevo informe](#creación-de-un-informe).
8. [Añadir SQL a un objeto SQL](#adición-de-sql-al-objeto-sql).
9. [Volver a colocar variables en el SQL](#volver-a-poner-las-variables-en-sql).
10. [Completar el desarrollo de informes](#completar-el-desarrollo-del-informe).
11. [Cree una entrada en el archivo CQS](#creación-de-una-entrada-en-el-archivo-cqs).
12. [Regenerar infraestructura](#regeneración-del-entorno).
13. [Sustituir referencias de objeto SQL por CQS](#sustitución-de-referencias-a-objetos-sql-por-referencias-a-cqs).

### Revisión del diseño de informe

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-reviewing-your-report-design)

El primer paso para diseñar un asunto de consulta personalizado es revisar el diseño de informe.

Debe prestar especial atención a los campos y objetos necesarios para generar el informe. Esto le permitirá decidir si crear un asunto de consulta personalizado o utilizar el modelo de entorno de elaboración de informes existente.

### Creación de un diagrama entidad-relación

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-creating-entity-relationship-diagram)

A partir de IBM OpenPages® puede determinar los campos adjuntos a un objeto y las relaciones entre objetos.

El siguiente paso en la creación de un asunto de consulta personalizado es generar un diagrama entidad-relación (ER).

Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de soluciones** > **Soluciones** y haga clic en una solución para ver sus tipos de objeto. Para ver detalles sobre un tipo de objeto, incluidos los campos y grupos de campos correspondientes, pulse el nombre. Para obtener más información, consulte [Visualizaciones de esquema de solución](3.2-guia-del-administrador.md#visualizaciones-de-esquemas-de-soluciones).

O bien, haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Tipos de objeto**. La lista muestra todos los tipos de objeto definidos en el sistema. Para ver detalles sobre un tipo de objeto, incluidos los campos y grupos de campos correspondientes, pulse el nombre.

Los grupos de campos del tipo de objeto contienen las definiciones de todos los campos definidos para el objeto. Esta lista no incluye claves ni otros campos de ID que puedan ser necesarios para crear solicitudes o uniones entre tablas. Consulte [Modelos de base de datos](#modelos-de-bases-de-datos) para obtener más información sobre los campos necesarios para unir tablas.

Utilizando esta información, puede determinar qué objetos se necesitan en la sentencia SQL. Tal como se especifica en [Modelos de base de datos](#modelos-de-bases-de-datos), cada uno de estos objetos corresponde a una tabla de informes y a un conjunto de tablas de puente. Necesita determinar la relación entre los objetos además del tipo de unión requerido y las tablas puente que se van a utilizar.

En este punto, puede crear un diagrama ER en una herramienta de diagramación que formará la base de la sentencia SQL. Se recomienda revisar el diagrama con uno de los arquitectos del sistema para verificar su precisión.

### Creación de una sentencia SQL

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-creating-sql-statement)

Utilizando la herramienta de desarrollo SQL, puede crear la sentencia SQL.

Siguiendo los estándares de codificación SQL listados en [Directrices de codificación SQL](#directrices-de-codificación-sql), escriba el SQL asegurándose de que se incluyan todos los campos necesarios para el informe. Compruebe el conjunto de resultados para obtener registros duplicados y una agrupación adecuada. Cuando lo haya hecho, podrá cortar y pegar esta sentencia SQL en los informes.

Acuérdese de utilizar las vistas `RV_` al crear la sentencia de SQL. Cada vista `RV_` contiene una columna Seguridad de OpenPages, `OP_FLAG_READ_ACCESS`, con estos valores posibles:

- **Y**

  Si el usuario que ejecuta el informe tiene acceso de lectura al registro.

- **N**

  Si el usuario que ejecuta el informe no tiene acceso de lectura al registro.

Por ejemplo, si desea que la seguridad deIBM OpenPages® se integre en CQS, debe añadir el filtro en esta columna:

`OP_FLAG_READ_ACCESS ='Y'`

Si está utilizando Oracle SQL Developer, hay instancias en las que SQL Developer no opera adecuadamente debido a un problema por no establecer correctamente el ID de usuario en el valor predeterminado. Puede establecer manualmente la variable de configuración regional ejecutando la siguiente sentencia SQL en la sesión:

```
begin OP_SESSION_MGR.SET_ACTOR_ID_PRIVATE (#$account.parameters.openPagesUserId#);
  end;
```

Donde sustituye la macro IBM® Cognos® por un valor de ID de usuario válido.

#### Sentencias SQL con cifrado a nivel de campo

Cuando utilice la tabla `PROPERTY.AUDIT.TRAIL` en la consulta SQL y el cifrado de nivel de campo esté habilitado, descifre el valor de la propiedad de la tabla `PROPERTY.AUDIT.TRAIL` para permitir que los usuarios vean los valores de texto con claridad.

La función de base de datos siguiente se utiliza para descifrar valores de propiedad: `op_crypt_mgr.decrypt_property_value`, esto se utiliza para descifrar valores en la tabla `PROPERTY.AUDIT.TRAIL`.

Se utilizan las propiedades de entrada siguientes para la función de base de datos `op_crypt_mgr.decrypt_property_value`:

- Propiedad 1: `propertydefs.propertydefid` (ID de PropertyDef del campo.)
- Propiedad 2: `propertyvals.value` (valor de propiedad del campo.)

Por ejemplo, seleccione op_crypt_mgr.decrypt_property_value(t.propertydefid, t.old_value) en property_audit_trail t.

### Adición de funciones de base de datos

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-adding-database-functions)

Puede utilizar muchas funciones de base de datos en IBM OpenPages®.

[Utilización de funciones de base de datos predefinidas](#uso-de-las-funciones-de-base-de-datos-predefinida) describe todas las funciones de base de datos de IBM OpenPages que se han expuesto al autor del informe. Hay tres funciones clave que tendrá que utilizar:

- **`OP_ACTOR_MGR.GET_DISPLAY_NAME`**

  Se utiliza para convertir los ID de usuario en nombres de usuario reales.

- **`OP_RPS_AUX.CONVERT_EVID_TO_NAME`**

  Se utiliza para convertir una serie enumerada de selección única en su texto.

- **`OP_RPS_AUX.CONVERT_EVIDLIST_TO_NAME`**

  Se utiliza para convertir una serie enumerada de selección múltiple en una lista de texto separada por comas.

Después de crear la sentencia SQL, podrá ver en el conjunto de resultados qué elementos se devuelven como ID y cuáles se devuelve como texto. Tendrá que convertir las series devueltas como ID en texto legible para hacer que el informe resulte útil. Debe verificar que los campos que está convirtiendo son series enumeradas reales. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Tipos de objeto** y busque los campos en los tipos de objeto individuales.

La función `GET_DISPLAY_NAME` se utiliza (según los requisitos de la organización) para mostrar los nombres de usuario en los informes en lugar del nombre de inicio de sesión.

### Sustitución de variables

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-substituting-variables)

Después de incluir las funciones de base de datos, habrá referencias a series de sustitución que solo están disponibles en el entorno de informes de IBM® Cognos® .

Para probar el SQL, necesitará hacer las siguientes sustituciones.

- **`#$account.parameters.openPagesLocaleId#`**

  Este es la configuración regional del usuario que ha iniciado sesión en el sistema. Utilice 1 (ES_ES).

- **`#$account.parameters.openPagesUserId#`**

  Este es el número de ID del usuario que ha iniciado sesión en el sistema. Consulte la tabla `actorinfo` y utilice el valor `actorId` para OpenPagesAdministrator en lugar de esta variable.

### Prueba de la sentencia SQL

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-testing-sql-statement)

Después de crear una sentencia SQL válida, debe probarla.

Debe examinar el conjunto de resultados para los siguientes elementos:

- Registros duplicados
- Uniones erróneas
- Datos que necesitan conversión
- Campos que faltan o campos incorrectos
- Campos nombrados erróneamente
- Rendimiento de prueba

### Creación de un informe

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-creating-report)

Puede seleccionar un tipo de informe para crear un informe nuevo.

En este punto, tiene una sentencia SQL completamente funcional que contiene todos los campos que necesita para completar el informe.

Seleccione un tipo de informe para crear un informe nuevo.

### Adición de un objeto SQL

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-adding-sql-object)

Puede añadir un objeto SQL al informe.

#### Procedimiento

1. Abra el explorador y seleccione la consulta que se ha creado para el informe.
2. Seleccione un objeto SQL del menú de la caja de herramientas y suéltelo en el asunto de consulta al lado del asunto de consulta existente.
3. Seleccione el objeto SQL y cambie la propiedad Origen de datos a `OpenPages DataSource`. Es el nombre asignado al controlador que se conecta a la base de datos de IBM OpenPages® .

### Adición de SQL al objeto SQL

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-adding-sql-sql-object)

Puede añadir código SQL a un objeto SQL.

Puede añadir el código efectuando doble pulsación en el objeto SQL y pegando el código SQL en el cuadro de diálogo **SQL**.

Pulse el **Validar** icono ![Icono Validar expresión](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg) para asegurarse de que no hay errores en el código SQL. Pulse **Aceptar** para continuar.

Ahora puede seleccionar el asunto de consulta del explorador de consultas y ver que aparece el objeto SQL como un asunto de consulta con elementos de consulta que se pueden seleccionar.

En este punto puede completar el diseño de informe utilizando el SQL personalizado como base para el informe.

### Volver a poner las variables en SQL

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-putting-variables-back-into-sql)

Después de copiar la sentencia SQL en el objeto SQL, deberá sustituir los valores predeterminados por funciones de base de datos, seguridad y solicitudes por los valores y solicitudes correctos.

#### Adición de solicitudes

`Guía del creador de informes › Asuntos de consulta personalizados › Volver a poner las variables en SQL` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=sql-adding-prompts)

Una solicitud le pide al usuario un valor durante la ejecución de una sentencia SQL. Una solicitud es una macro en IBM® Cognos® y no puede ser ejecutada por las herramientas de desarrollo de SQL. Esto es por lo que añade solicitudes después de añadir el SQL al objeto SQL.

El siguiente ejemplo muestra la sintaxis básica de la solicitud:

```
prompt (Name, Data Type, Default Text)
```

Las siguientes variables se utilizan en la macro de solicitud:

- **`Name`**

  Es el nombre de la solicitud. También puede tener el mismo nombre que un parámetro en la página de solicitudes. Si utiliza el parámetro como nombre de solicitud, aparecerá la página de solicitud de informe. Esto es obligatorio.

- **`Data Type`**

  Es el tipo de datos devuelto por la solicitud. Los valores incluyen: entero, fecha y serie. Esto es obligatorio.

- **`Default Text`**

  Es el valor predeterminado de la solicitud. Esto es opcional.

los siguientes ejemplos muestran la sintaxis para utilizar solicitudes:

- **Solicitud de cadena**

  `#prompt("bundle_name", "string")#`

- **Solicitud de entero**

  `#prompt("resourceId", "integer", "1")#`

- **Solicitud de fecha**

  `#prompt("Start Date", "date")#`

Añada solicitudes al SQL solo cuando utilice sentencias SQL anidadas. Siempre es mejor poner las solicitudes en el informe. Además, cuando añade CQS al archivo xml, debe añadir una sección de solicitud a la consulta.

Para obtener más información sobre cómo utilizar solicitudes, consulte la documentación de *IBM Cognos Framework Manager* .

### Completar el desarrollo del informe

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-completing-report-development)

En este punto, puede completar todo el desarrollo del informe utilizando el objeto SQL como base para el informe.

Es posible que, a medida que continúa el desarrollo del informe, le falten campos o sea necesario aplicar las funciones de IBM OpenPages® a algunos de los campos de la consulta. Puede editar el objeto SQL y añadir estos elementos que faltan ya que aún no ha convertido el informe para ejecutarlo con un asunto de consulta personalizado.

### Creación de una entrada en el archivo CQS

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-creating-entry-in-cqs-file)

La generación de entorno contiene dos partes, la parte generada dinámicamente y la parte personalizada.

La parte dinámica del entorno se crea por medio del generador de entorno basándose en los metadatos del usuario. La parte personalizada de la infraestructura está contenida en los archivos siguientes: `static-modelquerysubjects*.xml` y `custom-static-modelquerysubjects*.xml`. Estos archivos contienen asuntos de consulta definidos por el usuario y las relaciones entre ellos.

Los archivos `static-modelquerysubjects*.xml` de fábrica los utiliza IBM OpenPages® para definir asuntos de consulta personalizados que incluyen la auditoría, la seguridad, el permiso de usuario, el archivo desasociado y los archivos extraídos. Estos archivos se envían con cada instalación y se sobrescriben cuando se aplican actualizaciones. No realice ninguna modificación en estos archivos.

Si desea añadir sus propios asuntos de consulta personalizados, cree un archivo nuevo. Utilice el convenio de denominación: `custom-static-modelquerysubjects*.xml`. Coloque el archivo en el directorio `<OP_HOME>/aurora/framework/conf/mqs` del servidor de aplicaciones.

La siguiente lista muestra las vías de acceso predeterminadas:

- **Utilización del entorno en un sistema operativo Windows**

  `C:\OpenPages\aurora\framework\conf\mqs`

- **Utilización de la infraestructura en un sistema operativo Linux®**

  `/opt/OpenPages/aurora/framework/conf/mqs`

El archivo que contiene el CQS es un archivo XML. El mejor método que se puede utilizar para añadir un asunto de consulta adicional es copiar uno existente y sustituir todos los datos. Al editar el archivo, debe tener cuidado para crear las etiquetas de principio y final adecuadamente.

El archivo utiliza las etiquetas siguientes:

- **`<MODELQUERYSUBJECTS>`**

  Es la etiqueta colocada más hacia el exterior del archivo. Esta es una colección de definiciones `<MODELQUERYSUBECT>`.

- **`<MODELQUERYSUBJECT>`**

  Es un asunto de consulta personalizado individual.

- **`<RELATIONSHIPS>`**

  Es la relación entre dos asuntos de consulta.

- **`<CALCULATIONS>`**

  Es un cálculo personalizado.

- **`<PARAMETERMAPS>`**

  Se trata de una correlación de parámetros definida por el usuario.

Las siguientes secciones describen el uso adecuado de los elementos de cada sección del archivo XML.

#### Adición de un asunto de consulta de modelo

`Guía del creador de informes › Asuntos de consulta personalizados › Creación de una entrada en el archivo CQS` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=file-adding-model-query-subject)

Este asunto de consulta de modelo es la definición de la sentencia SQL que desea añadir al entorno. Contiene la definición de dónde desea añadir la consulta, la misma consulta, las columnas de la consulta y las solicitudes (si se utilizan).

Es una buena idea colocar un comentario antes del asunto de consulta de modelo que indica el nombre del informe donde se utiliza el CQS y el autor de CQS.

Las siguientes secciones listan los elementos contenidos en un asunto de consulta de modelo, los atributos de esos elementos, los elementos que contienen y los elementos en los que están contenidos.

##### MODELQUERYSUBJECTS

Contiene: MODELQUERYSUBJECT

Contenido por: Ninguno.

##### MODELQUERYSUBJECT

Atributos:

- **`name`**

  Nombre del asunto de consulta personalizado. Todos los nombres de asunto de consulta deben ser exclusivos. No puede utilizar un guion en el nombre de un asunto de consulta.

  Necesario.

- **`models`**

  El modelo de entorno que se va a añadir a la consulta. Puede ser `ALL` o una lista separada por comas de nombres de modelo de entorno. Si se omite este campo, se utiliza `Platform_Reporting`.

  Opcional.

- **`namespaces`**

  El espacio de nombres que se va a añadir a la consulta. Puede ser `ALL` o una lista separada por comas de espacios de nombres. Si se omite este campo, se utilizará `DEFAULT`.

  Opcional.

- **`passthrough`**

  Establézcalo en `true` si se omitirá la optimización de IBM® Cognos® , `false` si se aplicará la optimización de IBM Cognos .

  Opcional.

- **`folder`**

  La carpeta que se creará/utilizará para almacenar el nuevo asunto de consulta personalizado bajo cada espacio de nombres definido. La ubicación recomendada es: /MISCELLANEOUS/CUSTOM QUERY SUBJECTS

  Opcional.

- **`childId`**

  Opcional.

- **`parentId`**

  Opcional.

Contiene: <![CDATA[ Sentencia SQL ]]>, COLUMNS, PROMPTS, KEYS

Contenido por: MODEQUERYSUBJECTS.

##### <![CDATA [sentencia SQL]] >

Esta sección del XML contiene la expresión SQL real.

Atributos: Ninguno.

Contiene: Ninguno.

Contenido por: MODELQUERYSUBJECT

##### COLUMNAS

Atributos: Ninguno.

Contiene: columna

Contenido por: MODELQUERYSUBJECT

##### columna

Este elemento contiene todas las columnas expuestas de la sentencia SQL real.

Atributos:

- **`name`**

  Todos los nombres de columna deben aparecer en mayúsculas.

  Necesario.

Contiene: Ninguno.

Contenido por: COLUMNS

##### PROMPTS

Atributos: Ninguno.

Contiene: solicitud

Contenido por: MODELQUERYSUBJECT

##### solicitud

Atributos:

- **`name`**

  El nombre de solicitud que aparece en el asunto de consulta. Debe coincidir exactamente.

- **`defaultvalue`**

  El valor predeterminado para la solicitud.

  Opcional.

Contiene: Ninguno.

Contenido por: PROMPTS

##### KEYS

Atributos: Ninguno.

Contiene: Ninguno.

Contenido por: MODELQUERYSUBJECT

##### Ejemplo de MODELQUERYSUBJECT

```sql
            <!-- Control Owner Assignment Report - Author: J. Doe -->
<MODELQUERYSUBJECT
  name="Control_Owner_Assignment"
  passthrough="false"
  folder="/MISCELLANEOUS/CUSTOM QUERY SUBJECT">
  <![CDATA[
    SELECT
      RA.CHECKED_IN_BY as RA_OWNER,
      RA.NAME00 as RA_NAME,
      RI.CHECKED_IN_BY AS RI_OWNER,
      CN.CONTROL_ID as CN_CONTROL_ID,
      CN.NAME00 as CN_NAME,
      CN.DESCRIPTION as CN_DESCRIPTION,
      CN.CHECKED_IN_BY as CN_OWNER
      FROM
        RV_RISKASSESSMENT RA,
        RT__RISKASSESSMENT_RISK RA2RI,
        RV_RISK RI,
        RT__RISK_CONTROL RI2CN,
        RV_CONTROL CN
      WHERE
        RA.RISKASSESSMENT_ID = RA2RI.RISKASSESSMENT_ID  AND
        RA.REPORTING_PERIOD_ID = RA2RI.REPORTING_PERIOD_ID AND
        RA2RI.RISK_ID = RI.RISK_ID AND
        RA2RI.REPORTING_PERIOD_ID = RI.REPORTING_PERIOD_ID AND
        RA2RI.IS_PRIMARY = 'Y' AND
        RA2RI.HIER_INSTANCE_ID = 1 AND
        RI.RISK_ID = RI2CN.RISK_ID AND
        RI.REPORTING_PERIOD_ID = RI2CN.REPORTING_PERIOD_ID AND
        RI2CN.CONTROL_ID = CN.CONTROL_ID AND
        RI2CN.REPORTING_PERIOD_ID = CN.REPORTING_PERIOD_ID  AND
        RI2CN.IS_PRIMARY = 'Y' AND
        RI2CN.HIER_INSTANCE_ID = 1 AND
        RA.REPORTING_PERIOD_ID  = #prompt("reportingperiodid", "integer")#
        AND RA.OP_FLAG_READ_ACCESS ='Y'
        AND RI.OP_FLAG_READ_ACCESS ='Y'
        AND CN.OP_FLAG_READ_ACCESS ='Y'
       ]]>
  <COLUMNS>
    <column name="RA_OWNER"/>
    <column name="RA_NAME"/>
    <column name="RI_OWNER"/>
    <column name="CN_NAME"/>
    <column name="CN_DESCRIPTION"/>
    <column name="CN_OWNER"/>
  </COLUMNS>
  <PROMPTS>
    <prompt name="reportingperiodid" defaultValue="-1"/>
  </PROMPTS>
</MODELQUERYSUBJECT>
```

#### Especificación de relaciones

`Guía del creador de informes › Asuntos de consulta personalizados › Creación de una entrada en el archivo CQS` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=file-specifying-relationships)

Esta sección de relaciones se utiliza para crear uniones entre asuntos de consulta personalizados o entre asuntos de consulta personalizados y asuntos de consulta predefinidos. Si está diseñando un conjunto de consultas que están relacionadas unas con otras, esa relación debe especificarse. Esta parte del archivo XML le permite crear esas relaciones.

Las siguientes secciones listan los elementos de relación, los atributos de esos elementos, los elementos que contienen y los elementos en los que están contenidos.

##### RELACIONES

Atributos:

Contiene: relación

Contenido por: MODELQUERYSUBJECTS

##### relación

Atributos:

- **`parent`**

  El nombre del asunto de consulta padre.

  Necesario.

- **`child`**

  El nombre del asunto de consulta hijo.

  Necesario.

- **`pid`**

  El campo al que unirse en el padre.

  Necesario.

- **`cid`**

  El campo al que unirse en el hijo.

  Necesario.

- **`innerjoin`**

  ¿Es una unión interna? Los valores son `true` o `false`.

  Opcional.

- **`useReportingPeriodId`**

  Si se va a unir en el periodo de elaboración de informes. Los valores son `true` o `false`.

  Opcional.

- **`one-to-n-left-outer-join`**

  ¿Es una unión externa a la izquierda? Los valores son `true` o `false`.

  Opcional.

Contiene: Ninguno.

Contenido por: RELACIONES

##### Ejemplo de RELACIONES

```xml
<RELATIONSHIPS>
  <relationship
    parent="RISKEVAL-BY-SOXRISK"
    child="RISK_RATINGS"
    pid="RE_RISKEVAL_ID"
    cid="RE_RISKEVAL_ID"
    useReportingPeriodId="true"
    one-to-n-left-outer-join="true"/>

  <relationship
    parent="RISKEVAL-BY-SOXRISK"
    child="RISK_ALLOCATED"
    pid="RE_RISKEVAL_ID"
    cid="RE_RISKEVAL_ID"
    useReportingPeriodId="true"
    one-to-n-left-outer-join="true"/>

</RELATIONSHIPS>
```

#### Creación de cálculos

`Guía del creador de informes › Asuntos de consulta personalizados › Creación de una entrada en el archivo CQS` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=file-creating-calculations)

Puede crear cálculos personalizados para proporcionar a los autores de informes valores calculados que utilizan normalmente. Los cálculos pueden utilizar elementos de consulta, parámetros, variables, miembros calculados, expresiones y componentes de expresiones como, por ejemplo, funciones.

Las siguientes secciones listan los elementos de cálculo, los atributos de esos elementos, los elementos que contienen y los elementos en los que están contenidos.

##### Cálculos

Atributos:

Contiene: cálculo

Contenido por: MODELQUERYSUBJECTS

##### Cálculo

Atributos:

- **`name`**

  Nombre del cálculo. No se permiten espacios.

  Opcional.

- **`namespace`**

  El espacio de nombres en el que se debe crear el objeto de cálculo.

  Necesario.

- **`folder`**

  La vía de acceso a carpeta en la que anidar el objeto de cálculo. Como estándar, el cálculo se almacena en la carpeta de cálculos bajo el objeto relacionado más estrechamente con el cálculo.

  Opcional.

- **`level`**

  Esto se utiliza para definir el orden en el que se crean los cálculos. Un nivel más alto significa que se creará más tarde en comparación con otros cálculos.

  Opcional.

Contiene: expresión

Contenido por: CÁLCULOS

##### expresión

Atributos: Ninguno.

Contiene: <![CDATA[ expresión ]]>

Contenido por: cálculo

##### <![CDATA[ expresión ]]>

La expresión SQL. Es obligatoria.

Atributos: Ninguno.

Contiene: Ninguno.

Contenido por: expresión

##### Ejemplo de CÁLCULOS

```xml
<CALCULATIONS>
  <calculation
    name = "RISK_LOSS"
    namespace = "DEFAULT_REL"
    folder = "/GRC_OBJECTS/SOXRISK_FOLDER/COMPUTED FIELDS"
    level = "2">
    <expression>
      <![CDATA[nvl(average([DEFAULT_REL].[SOXRISK].
         [RI_INHERENT_SEVERIT_BA] for
       [DEFAULT_REL].[SOXRISK].[RI_RISK_ID]),0)]]>
    </expression>
  </calculation>
</CALCULATIONS>
```

#### Uso de mapas de parámetros para crear expresión durante el tiempo de ejecución

`Guía del creador de informes › Asuntos de consulta personalizados › Creación de una entrada en el archivo CQS` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=file-using-parameter-maps-create-expressions-run-time)

Los mapas de parámetros se utilizan para crear sustituciones durante el tiempo de ejecución.

Por ejemplo, el valor de ID de una categoría de riesgo con el nombre de `Fraud` puede ser diferente en los sistemas de producción y de prueba. En lugar de crear una expresión con el ID numérico, cree la expresión con el nombre de la variable y, a través del uso del mapa de parámetros, el valor de ID se llena durante el tiempo de ejecución.

Las siguientes secciones listan los elementos del mapa de parámetros, los atributos de esos elementos, los elementos que contienen y los elementos en los que están contenidos.

##### PARAMETERMAPS

Atributos:

Contiene: parametermap

Contenido por: MODELQUERYSUBJECTS

##### parametermap

Atributos:

- **`name`**

  El nombre del mapa de parámetros que desea crear. No se permiten espacios.

  Opcional.

Contiene: Parám

Contenido por: PARAMETERMAPS

##### param

Atributos:

- **`key`**

  La clave que será sustituida por el valor.

  Opcional.

- **`value`**

  El valor que se utilizará en la expresión del mapa de parámetros.

  Opcional.

Contiene: Ninguno.

Contenido por: parametermap

##### Ejemplo de PARAMETERMAPS

```xml
<PARAMETERMAPS>
  <parametermap name = "CUSTOM_RISK_CATEGORY">
    <param key = "Internal Fraud" value = "2345"/>
    <param key = "External Fraud" value = "2346"/>
    <param key = "Employee Theft" value = "2347"/>
  </parametermap>
</PARAMETERMAPS>
```

### Regeneración del entorno

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-regenerating-framework)

Puede seguir los procedimientos de la publicación *IBM OpenPages Guía del administrador* para actualizar la infraestructura. Puede elegir generar todos los modelos de entorno o los modelos de entorno seleccionados.

Se pueden emitir los errores siguientes cuando se genera el marco de trabajo:

- Ha olvidado añadir una etiqueta de columna para cada campo de la sentencia SQL.
- Tiene un tipo en uno de los atributos de MODELQUERYSUBJECT.
- Le falta una etiqueta de cierre.
- Olvidó definir una etiqueta de solicitud para cada solicitud del código SQL.
- El número de sentencias de columna debe ser el mismo que el de los campos de la sentencia SQL.
- Los nombres de columna de la sentencia SQL no se deletrean igual que en las etiqueta de columna.
- Los nombres de columna deben estar en el mismo orden que las etiquetas de columna.
- No puede utilizar un guion ( - ) en el nombre del CQS.
- El límite de caracteres para los nombres de campo es de 30 caracteres (esto truncará el nombre de campos).

El detalle de los mensajes de error se puede encontrar en el archivo `script-player-error.log`, ubicado en el servidor de informes en `C:\OpenPages\CommandCenter\framework\logs`

Si se detecta un error de análisis en el archivo, el error se listará en `framework-generator.log`, en el mismo directorio.

> **Nota:** Linux® y Windows tienen ubicaciones predeterminadas diferentes.

### Sustitución de referencias a objetos SQL por referencias a CQS

`Guía del creador de informes › Asuntos de consulta personalizados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=subjects-replacing-sql-object-references-cqs-references)

Debe eliminar las referencias al objeto SQL del informe y sustituirlas por las referencias al nuevo asunto de consulta personalizado.

Esto puede hacerlo campo a campo, abriendo cada variable en el informe y cambiando las referencias de objeto de `[SQL<N>]` por el nombre del nuevo CQS `[<CQS Name>]`.

También puede guardar el informe en un archivo de texto, realizar una búsqueda global y sustituir `[SQL<N>]` por `[<CQS Name>]` en el archivo.

Es posible que tenga que suprimir todos los objetos SQL que ha creado porque no se están utilizando.

#### Edición del archivo de texto del informe

`Guía del creador de informes › Asuntos de consulta personalizados › Sustitución de referencias a objetos SQL por referencias a CQS` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=references-editing-report-text-file)

Puede editar el archivo de texto del informe para sustituir el contenido que se debe actualizar.

##### Acerca de esta tarea

Puede guardar el informe en un archivo de texto y realizar una operación de búsqueda y sustitución global de `[SQL<N>]` por `[<CQS Name>]` en el archivo. A continuación, vuelva a cargar el archivo y valídelo para asegurarse de que sus ediciones son correctas.

##### Procedimiento

1. Para copiar el informe en el portapapeles, pulse **Herramientas** > **Copiar informe en portapapeles**.
2. Abra un editor de texto y pegue el portapapeles en el documento.
3. Busque en `[SQL<N>]` y sustitúyalo por `[<CQS Name>]`.
4. Guarde el archivo.
5. Seleccione todo el archivo.
6. Copie el informe en el portapapeles.
7. Guarde el informe existente.
8. Abra un nuevo informe en blanco.
9. Pulse **Herramientas** > **Abrir informe desde portapapeles** para restaurar el informe desde el portapapeles.
10. Pruebe que el informe funciona.
11. Guarde el informe.

#### Eliminación de objeto SQL

`Guía del creador de informes › Asuntos de consulta personalizados › Sustitución de referencias a objetos SQL por referencias a CQS` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=references-removing-sql-object)

Puede suprimir todos los objetos SQL que ha creado porque si no se están utilizando.

##### Procedimiento

1. En el informe, abra **Explorador de consultas** y seleccione **Consultas**.
2. Seleccione el **Objeto SQL** que desea eliminar.
3. Pulse el icono **Suprimir** en la barra de herramientas.
4. Pulse el **Validar** icono ![Icono Validar expresión](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/icon-validate_expression.jpg). Si ha realizado la sustitución correctamente, el informe se validará.

## Directrices de codificación SQL

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-sql-coding-guidelines)

Este tema describe información general que hay que seguir al trabajar con sentencias SQL en el archivo del asunto de consulta personalizado.

### Directrices generales

Utilice las siguientes directrices con sentencias SQL en el archivo del asunto de consulta personalizado.

- Todas las sangrías se deben guardar como espacios no como pestañas.
- La sangría debe constar de tres espacios.
- Cada sentencia anidada debe comenzar con un nuevo nivel de sangría.
- Todas las palabras reservadas de base de datos estarán en mayúscula.
- La longitud de las líneas no debe exceder los 80 caracteres.
- Se deben utilizar comentarios en SQL para describir funcionalidad. Los comentarios deben tener el formato `/* <text> */`.
- Los filtros y la agrupación no se pueden colocar en CQS a menos que sea absolutamente necesario. Estos deben llevarse a cabo en el informe.
- Utilice UNION ALL en lugar de UNION porque es mucho más rápido. UNION eliminará las filas duplicadas, pero UNION ALL no lo hará. Las filas duplicadas se pueden eliminar del informe a través del uso de la propiedad Grupo automático y resumen.
- Utilizará las vistas RV_ en lugar de las tablas RT_ porque las vistas tienen seguridad de usuario compiladas en ellas.

### Convenciones de denominación

`Guía del creador de informes › Directrices de codificación SQL` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guidelines-naming-conventions)

Los términos nemotécnicos listados en este tema se utilizan como nombres de tabla y como prefijos para nombres de columna.

Los prefijos de tabla alternativos siguientes se utilizan cuando el prefijo de objeto es una palabra reservada de base de datos:

- Incident: INC
- SOXIssue: ISU
- SOXTask: ATI

**Tabla 1. Etiquetas y nombres de tipo de objeto**

| Nombre de tipo de objeto | Etiqueta de tipo de objeto | Prefijo de objeto |
| --- | --- | --- |
| AscentSupportingInformation | Información de soporte de ascenso |  |
| Assertion | Declaración | AO |
| Attestation | Atestación | AN |
| AuditableEntity | Entidad auditable | AE |
| Auditor | Auditor | AD |
| AuditPhase | Sección de auditoría | AH |
| AuditProgram | Auditoría | AU |
| BCBusinessImpactAnalysis | Análisis de impacto empresarial | BI |
| BCEvent | Suceso de continuidad de negocio | BV |
| BCPlan | Plan de continuidad de negocio | PS |
| BCTest | Plan de prueba de continuidad de negocio | BT |
| BCTestResult | Resultado de prueba de continuidad de negocio | BE |
| BusService | Servicio empresarial | SV |
| BusServiceEval | Evaluación de servicios empresariales | ET |
| Campaign | Campaña | CP |
| Challenge | Reto | CH |
| ChangeRequest | Solicitud de cambio | CR |
| Committee | Comité | CI |
| CompliancePlan | Plan de conformidad | CA |
| CompliancePlanEval | Evaluación del plan de conformidad | PV |
| ComplianceTheme | Tema de conformidad | CE |
| ComplianceThemeEval | Evaluación de temas de conformidad | TV |
| ComplianceReviewComment | Comentario de revisión de conformidad | CR |
| Contract | Contrato | CT |
| CostCenter | Centro de costes | CC |
| CtlEval | Evaluación de control | CV |
| DisclosureStatement | Declaración de divulgación | DS |
| Employee | Empleado | EE |
| Engagement | Compromiso | EG |
| Finding | Conclusión | FD |
| FIRSTLoss | FIRST Pérdida | FL |
| Incident | Incidente | ENTRADA |
| KeyPerfIndicator | KPI | KP |
| KeyPerfIndicatorValue | Valor de KPI | KY |
| KeyRiskIndicator | Indicador clave de riesgo | KR |
| KeyRiskIndicatorValue | Valor KRI | KE |
| Location | Ubicación | LC |
| LossEvent | Evento de pérdida | LE |
| LossImpact | Impacto de pérdida | LO |
| LossRecovery | Recuperación de pérdidas | LR |
| Mandate | Mandato | MD |
| Metric | Métrica | ME |
| MetricValue | Valor de métrica | MV |
| Model | Modelo | ML |
| ModelAttestation | Atestación de modelo | MK |
| ModelInput | Entrada de modelo | MT |
| ModelLink | Enlace de modelo | MN |
| ModelOutput | Salida del modelo | MP |
| ModelScorecard | Tarjeta de puntuación de riesgo modelo | MC |
| ModelVersion | Versión del modelo | VN |
| Obligation | Obligación | OB |
| OblEval | Evaluación de la obligación | OE |
| OblEvalValue | Valor de evaluación de la obligación | OV |
| Objetivo | Objetivo estratégico | DO |
| ORICLoss | Pérdida ORIC | O |
| ORXLoss | Pérdida ORX | OL |
| Plan | Plan | PN |
| Policy | Política | PL |
| PolicyReviewComment | Comentario de revisión de política | RP |
| Preference | Preferencia | PF |
| PrefGrp | Grupo de preferencias | PG |
| Procedure | Procedimiento | PC |
| ProcessEval | Evaluación de proceso | PE |
| Product | Producto | PT |
| Program | Program | QP |
| Project | Proyecto | PJ |
| QuestionnaireAssessment | Evaluación de cuestionario | QA |
| QuestionnaireTemplate | Plantilla de cuestionario | QT |
| QuestionTemplate | Plantilla de preguntas | QQ |
| RAEval | Evaluación de evaluación de riesgos | AV |
| RRRating | RapidRatings Calificaciones |  |
| RegApp | Aplicabilidad de la normativa | RB |
| RegChange | Cambio regulador | RD |
| RegInt | Interacción con la autoridad reguladora | RF |
| Register | Caso de uso de modelo | RJ |
| RegTask | Tarea reguladora | RT |
| RegTrackRegEvent | Reg-Track Evento normativo |  |
| RegTrackRegSeries | Reg-Track Serie de eventos reguladores |  |
| Regulator | Autoridad reguladora | RE |
| RegulatoryEvent | Evento normativo |  |
| RegulatoryInitiative | Iniciativa reguladora | RG |
| Requirement | Requisito | RQ |
| ReqEval | Evaluación de requisitos | RY |
| ReqEvalValue | Valor de evaluación de requisito | RZ |
| RequirementVersion | Versión de requisito |  |
| Resource | Activo | RU |
| ResourceLink | Enlace de activo | RL |
| Review | Revisar | RW |
| ReviewComment | Comentario de revisión de auditoría | RC |
| RICat | Componente RI | RH |
| RIReq | Subcomponente RI | RR |
| RiskAssessment | Evaluación de riesgo | RA |
| RiskEntity | Sistema | RN |
| RiskEval | Evaluación de riesgos | RV |
| RiskReconRatings | RiskRecon Calificaciones |  |
| RiskSubEntity | Línea base | RS |
| ScenarioAnalysis | Análisis de escenario | BS |
| ScenarioResult | Resultado del caso de ejemplo | BR |
| SectionTemplate | Plantilla de sección | QS |
| SOXAccount | Cuenta | AC |
| SOXBusEntity | Entidad empresarial | EN |
| SOXControl | Control | CN |
| SOXControlObjective | Objetivo de control | CO |
| SOXDocument | Archivo | FI |
| SOXExternalDocument | Vínculo | LI |
| SOXIssue | Problema | ES |
| SOXProcess | Proceso | PR |
| SOXRisk | Riesgo | RI |
| SOXSignature | Firma | SI |
| SOXSubaccount | Subcuenta | SU |
| SOXSubprocess | Subproceso | SB |
| SOXTask | Elemento de acción | AT |
| SOXTest | Plan de pruebas | TE |
| SOXTestResult | Resultado de prueba | TR |
| SubContractor | Subcontratista | SC |
| Submandate | Submandato | SM |
| SubSectionTemplate | Plantilla de subsección | SS |
| SummaryAuditPlan | Plan de auditoría de resumen | SA |
| SupplyWisdom | Supply Wisdom |  |
| SupplyWisdomParentAlert | Alerta padre de Supply Wisdom |  |
| Team | Equipo | TM |
| Threat | Amenaza | TH |
| Timesheet | Hoja de registro horario | TI |
| TRRIRegEvent | Evento regulador TRRI |  |
| TRRIRegSeries | Serie de eventos reguladores TRRI |  |
| Usage | Despliegue de modelos | EE.UU. |
| Vendor | Proveedor | VE |
| VendorSubsidiary | Filial del proveedor | VS |
| Vulnerability | Vulnerabilidad | VU |
| Waiver | Renuncia | WV |
| WKRegEvent | Evento regulador WK |  |
| Workpaper | Documento de trabajo | WP |

### Cláusula SELECT

`Guía del creador de informes › Directrices de codificación SQL` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guidelines-select-clause)

Utilice las siguientes directrices al utilizar cláusulas SELECT.

- Coloque cada campo de la cláusula SELECT en una línea independiente.
- No utilice sentencias comodín en la cláusula SELECT. Por ejemplo:

  ```sql
  SELECT * from RV_ENTITY 
  ```

  seleccionará todos los campos desde la vista de entidad pero será lento.
- Los valores de campo de SELECT siempre utilizan alias:

  ```
        PR.NAME00 as PR_NAME
  ```
- Todas las variables de informe tendrá como prefijo el nombre de objeto. Por ejemplo, el nombre de proceso aparecerá en el informe como PR_NAME. [Convenios de denominación](#convenciones-de-denominación) lista los prefijos aceptables y se alterna cuando el prefijo es una palabra reservada de base de datos.
- Si CQS se va a unir con otros asuntos de consulta, una de las columnas se debe llamar REPORTING_PERIOD_ID. No puede tener un prefijo.
- Incluya siempre columnas clave (RESOURCE_ID, REPORTING_PERIOD_ID) de cada una de las tablas de tipo de objeto (RV_) como un campo en la cláusula SELECT. El rendimiento no se ve afectado y son útiles para filtrar el informe.
- Incluya siempre las columnas IS_PRIMARY y DISTANCE de cada tabla puente (RT_) de la cláusula SELECT. El rendimiento no se ve afectado y son útiles para filtrar el informe.
- Utilice subselecciones SQL para convertir series enumeradas de valor único y conversiones de nombre de usuario. Por ejemplo, utilice lo siguiente para obtener un valor de estado de problema:

  ```
          (SELECT 
              EV.LCLTXT_NAME
           FROM 
              I18N_INT_ENUM_VALS EV
           WHERE 
              EV.ENUM_VAL_ID  = ISS.STATUS AND 
              EV.I18N_LOCALE_ID = #$account.parameters.openPagesLocaleId#
           ) AS IS_STATUS
  Use the following to obtain the first and last names from a userId:
           (SELECT 
              UI.FIRSTNAME||' '||UI.LASTNAME
           FROM
              ACTORINFO ACI, 
              USERINFO UI 
           WHERE 
              PR.ITRM_RISK_MGR = ACI.NAME AND 
              ACI.ACTORID = UI.ACTORID
           ) AS PR_RISK_MANAGER_NAME
  ```
- Utilice la función de base de datos IBM OpenPages® CONVERT_EVIDLIST_TO_NAME para convertir series enumeradas de varios valores en listas.

### Cláusula FROM

`Guía del creador de informes › Directrices de codificación SQL` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guidelines-from-clause)

Utilice las siguientes directrices al utilizar cláusulas FROM.

- Coloque cada tabla en una cláusula FROM en su propia línea.
- Liste tablas en la cláusula FROM en el orden en el que se accederá a ellas.
- Los nombres de tabla también se alias con mnemotécnicos de [Convenios de denominación](#convenciones-de-denominación). Por ejemplo, la vista RV_PROCESS será: RV_PROCESS como PR y la vista Incident será RV_INCIDENT como INC.
- A las tablas de puente se les pondrá el nombre desde y hacia objetos, por ejemplo, Entidad de negocio a Proceso, EN2PR.

### Cláusula WHERE

`Guía del creador de informes › Directrices de codificación SQL` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guidelines-where-clause)

Utilice las siguientes directrices al utilizar cláusulas WHERE.

- Utilice el formato ANSI-92 de uniones:

  ```
  EV.REPORTING_PERIOD_ID (+)= EN.REPORTING_PERIOD_ID 
  ```

  para una unión externa a la izquierda. Esto sirve para mejorar la legibilidad de SQL.
- Debe utilizar columnas indexadas en uniones o al filtrar. Esto creará SQL de mayor rendimiento.
- Cada unión debe ser una unión INNER si es posible. No utilice nunca CROSS JOIN, solo INNER y OUTER.
- Evite también buscar con operadores no de igualdad (< > y NOT), ya que dan como resultado exploraciones de tabla e índice.
- Evite caracteres comodín al principio de la búsqueda en una columna indexada utilizando la palabra clave LIKE. Esto da como resultado una exploración del índice que es lenta. El primer ejemplo da como resultado una exploración de índice, mientras que el segundo ejemplo da como resultado una búsqueda de índice:

  ```sql
  SELECT entity_id FROM rv_entity as EN WHERE en.full_path LIKE '
        %Financial Services'
  '%Financial Services’ AND EN.RA.OP_FLAG_READ_ACCESS ='Y'
  SELECT entity_id FROM rv_entity as EN WHERE en.full_path LIKE 
        '/%Financial Services'
  ’/%Financial Services’ AND EN.RA.OP_FLAG_READ_ACCESS ='Y'
  ```
- Las uniones típicas serán por ID de recurso (ID de objeto) e ID de periodo de elaboración de informes. Ambos son campos indexados.
- Utilice únicamente HEIR_INSTANCE_ID = 1 en una unión cuando está uniendo a una tabla puente y desde una tabla puente. Estas uniones utilizarán \<parent>_ID, \<child>_ID y REPORTING_PERIOD_ID y forzarán el uso del índice del sistema en esta tabla.
- Si está utilizando el campo IS_PRIMARY, no utilice el campo HEIR_INSTANCE_ID.

### Cláusula ORDER BY

`Guía del creador de informes › Directrices de codificación SQL` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guidelines-order-by-clause)

Utilice la siguiente directriz cuando utilice las cláusulas ORDER BY.

- No utilice los números de columna en la cláusula ORDER BY, utilice únicamente nombres de columna.

## Definiciones de modelo y espacio de nombres

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-model-namespace-definitions)

Este apéndice contiene las definiciones de todos los modelos de entorno y espacios de nombres predefinidos de IBM OpenPages® . Según la configuración del sistema y las soluciones utilizadas, no todos estos modelos y espacios de nombres estarán disponibles.

Estos modelos y espacios de nombres dan soporte a los informes predefinidos que se suministran con el sistema. Estos espacios de nombres se pueden volver a utilizar para obtener requisitos de elaboración de informes y se pueden editar para satisfacer sus necesidades.

> **Nota:** Si edita un espacio de nombres suprimiendo o cambiando la relación entre objetos, es posible que los informes predefinidos ya no funcionen.

La definición más precisa de los modelos y espacios de nombres se puede encontrar en los valores de registro del sistema.

1. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_report_authors/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Configuración**.
2. Expanda la carpeta **Plataforma** > **Entorno de elaboración de informes V6** > **Modelos** .
3. Expanda la carpeta de un modelo y, a continuación, pulse **Espacios de nombres**.

### Modelos de entorno

`Guía del creador de informes › Definiciones de modelo y espacio de nombres` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=definitions-framework-models)

OpenPages® incluye un conjunto de modelos de entorno. La tabla siguiente lista los modelos y los correspondientes espacios de nombres.

**Tabla 1. Modelos de entorno**

| Modalidad de entorno | Descripción | Espacios de nombres |
| --- | --- | --- |
| Seguros y pruebas | Para casos de uso de auditoría y gestión de seguros | AUD1, AUD2, DEFAULT |
| Riesgo de modelo y privacidad de datos | Para casos de uso de riesgo de modelo y privacidad de datos | DEFAULT, DPM1, MRG1, MRG2 |
| Riesgo operativo y control | Para casos de uso de gestión de riesgos operativos y control financiero | DEFAULT, ORM1, ORM2, ORM3, RA1, RA2, SOX1 |
| Política y conformidad | Para casos de uso de normativa y de gestión de políticas | DEFAULT, MAND1, MAND2, POL1, RCM1, RCM2, RCM3, REGAPP1 |
| Resiliencia y continuidad | Para casos de uso de gobierno de TI, continuidad de negocio, gestión de terceros y resiliencia operativa | BCM1, BCM2, BCM3, BCM4, BCM5, BCM6, BCM7, BCM8, BCM9, DEFAULT, ITG1, ITG2, TPRM1 |
| Creación de informes de plataforma | El modelo de entorno de nivel 0, que se utiliza para ejecutar informes de plataforma | DEFAULT |

## Limitaciones y métodos alternativos

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-limitations-workarounds)

Este apéndice lista problemas y limitaciones conocidos que pueden encontrarse los autores de informes al crear informes, y posibles métodos alternativos.

### Limitación de la longitud de ecuación

`Guía del creador de informes › Limitaciones y métodos alternativos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workarounds-equation-length-limitation)

Existe una limitación en el tamaño del valor de atributo de cálculo que puede almacenar la aplicación IBM OpenPages® .

El atributo de preocupación principal es **Ecuación** donde una ecuación compleja puede ser muy larga. Hay un límite de 20.000 bytes en el tamaño del texto entrado. Tenga en cuenta que OpenPages da soporte a caracteres de varios bytes y, por lo tanto, es posible que no sea el equivalente a 20.000 caracteres si está utilizando un idioma de varios bytes.

#### Método alternativo

Puede crear el cálculo en el archivo CQS.

### Problemas de visualización de localización

`Guía del creador de informes › Limitaciones y métodos alternativos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workarounds-localization-display-issues)

Si va a diseñar informes para utilizar con varios idiomas, es posible que encuentre en algunas ocasiones problemas de formato.

Si está diseñando informes para utilizarlos con varios idiomas, pueden surgir problemas de formato originales como los siguientes:

- Puede aparecer una barra de desplazamiento horizontal en la ventana de informe. Por ejemplo, todos los informes de IBM OpenPages® proporcionados están diseñados para mostrar los datos generados en un tamaño de ventana establecido. Cuando se localizan algunos de estos informes en otros idiomas, como alemán o francés, el ancho de página aumenta y aparece una barra de desplazamiento horizontal.

#### Método alternativo

Los siguientes métodos alternativos pueden ayudarle a resolver el problema del desplazamiento horizontal:

- Establezca la característica en IBM® Cognos® Analytics -Creación de informes para permitir saltos de palabras automáticos.
- Divida manualmente una palabra larga en partes más pequeñas utilizando, por ejemplo, caracteres de espacio y guión (la palabra se dividirá después del espacio). Es posible que tenga que experimentar con la división de palabras manualmente para que se visualice adecuadamente dentro de la columna.

### Localización de prestaciones interactivas

`Guía del creador de informes › Limitaciones y métodos alternativos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workarounds-localization-interactive-capabilities)

Algunas características interactivas más recientes de IBM® Cognos® Analytics , que se utilizan en informes de IBM OpenPages® , no se adaptan a la globalización de varios idiomas. Estas características incluyen Cognos Dashboards y tablas de datos interactivas (introducidas en IBM Cognos Analytics 11.1.6). Como resultado, es posible que vea texto en inglés en los informes listos para usar.

#### Método alternativo

Utilice los métodos alternativos siguientes:

- Para los paneles de control de Cognos , realice una copia del panel de control para cada entorno local necesario y actualice manualmente las etiquetas específicas según sea necesario.

### Error al agrupar campos de serie grandes

`Guía del creador de informes › Limitaciones y métodos alternativos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workarounds-error-when-grouping-large-string-fields)

Si agrupa un campo de serie grande con una longitud no especificada, ya sea implícita o explícitamente, la agrupación da como resultado un error de columna no indexado.

Según el informe, es posible que vea un error similar al texto siguiente: `Using a blob column in this query requires that the query subject [TABLES].[PROPERTYVALS_CLOB] must have either a key or a unique index.`

Un ejemplo de agrupación explícita sería si establece la propiedad de consulta **Agrupar automáticamente y resumir** en `Yes` para una consulta que incluye un campo de serie grande. Un ejemplo de agrupación implícita sería si añade una agrupación en un campo de serie grande en un informe de lista.

#### Método alternativo

Si desea agrupar un campo de serie grande, primero debe convertirlo en un tipo de datos de caracteres con una longitud máxima soportada por la base de datos, por ejemplo:

`cast ([MAND1_REL].[REQUIREMENT].[RQ_SUPPORTING_REQUIREMENT], varchar (4000))`

### Error de cardinalidad no válida RQP-DEF-0162 al ejecutar un informe

`Guía del creador de informes › Limitaciones y métodos alternativos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=lw-rqp-def-0162-illegal-cardinality-error-when-you-run-report)

Al abrir un informe, obtiene el siguiente error: `RQP-DEF-0162 Illegal cardinality cardTwo.`

El error se puede producir cuando una palabra reservada, como un nombre de tipo de objeto, se utiliza en el nombre de un campo de cadena o serie enumerada.

Para evitar este error, no utilice palabras reservadas al crear campos de cadena o serie enumerada.

#### Método alternativo

Utilice una herramienta SQL como, por ejemplo, SQL*Plus o CLPPlus para cambiar el nombre del campo y vaciar la tabla `RPS_PRESET_COLS`.

Por ejemplo:

```sql
UPDATE rps_obj_col_presets
SET column_name   = 'keyriskindicatr'
WHERE column_name = 'keyriskindicator'
AND property_def_id =
  SELECT propertydefid
  FROM propertydefs
  WHERE enumtypeid =
    (SELECT enumtypeid FROM enumtypes WHERE upper(name) LIKE ‘KEYRISKINDICATOR’
    )
  );
COMMIT;
```

## Avisos

`Guía del creador de informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=rag-notices)

Esta información se ha desarrollado para productos y servicios que se ofrecen en Estados Unidos.

Puede que IBM no ofrezca los productos, servicios o características tratados en este documento en otros países. Póngase en contacto con el representante local de IBM para obtener información acerca de los productos y servicios disponibles actualmente en su zona. Las referencias a un producto, programa o servicio de IBM no pretenden establecer ni indicar que únicamente se pueda utilizar dicho producto, programa o servicio de IBM. También se podrán usar productos, programas o servicios cuyas funciones sean equivalentes y que no infrinjan los derechos de propiedad intelectual de IBM. No obstante, es responsabilidad del usuario evaluar y verificar el funcionamiento de cualquier producto, programa o servicio que no sea de IBM. Este documento puede incluir descripciones de productos, servicios o características que no forman parte de la titularidad de licencia o programa que ha adquirido.

IBM puede tener patentes o aplicaciones pendientes de patentes que cubran el tema descrito en este documento. La posesión de este documento no confiere ninguna licencia sobre dichas patentes. Puede enviar consultas sobre licencias, por escrito, a:

IBM Director of Licensing  
 IBM Corporation  
 North Castle Drive  
 Armonk, NY 10504-1785  
 U.S.A.

Para consultas sobre licencias relativas a información de doble byte (DBCS), póngase en contacto con el Departamento de propiedad intelectual de IBM de su país o envíe las consultas, por escrito, a:

Intellectual Property Licensing  
 Legal and Intellectual Property Law  
 IBM Japan Ltd.  
 19-21, Nihonbashi-Hakozakicho, Chuo-ku  
 Tokyo 103-8510, Japan

El siguiente párrafo no se aplica al Reino Unido ni a ningún otro país en el que dichas disposiciones sean incompatibles con la legislación local: INTERNATIONAL BUSINESS MACHINES CORPORATION PROPORCIONA ESTA PUBLICACIÓN Y TODAS LAS MUESTRAS DE CÓDIGO "TAL CUAL" SIN GARANTÍA DE NINGÚN TIPO, YA SEA EXPRESA O IMPLÍCITA, INCLUIDAS, ENTRE OTRAS, LAS GARANTÍAS IMPLÍCITAS DE NO INFRACCIÓN, COMERCIABILIDAD O IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Algunos estados no permiten la declaración de limitación de responsabilidad de las garantías explícitas o implícitas en determinadas transacciones, por lo tanto, es posible que esta sentencia no sea aplicable en su caso.

Esta información puede contener imprecisiones técnicas o errores tipográficos. Periódicamente se realizan cambios en la información incluida en este documento, estos cambios se incorporan en ediciones nuevas de la publicación. IBM puede efectuar, en cualquier momento y sin previo aviso, mejoras y cambios en los productos y programas descritos en esta publicación.

Cualquier referencia incluida en esta información a sitios Web que no sean de IBM sólo se proporciona para su comodidad y en ningún modo constituye una aprobación de dichos sitios web. El contenido de esos sitios web no forma parte del contenido de este producto de IBM, por lo que la utilización de esos sitios web se realiza bajo la responsabilidad del usuario.

IBM puede utilizar o distribuir cualquier información que se le suministre del modo que considere oportuno sin incurrir en ninguna obligación para con el remitente.

Los licenciatarios de este programa que deseen obtener información sobre él con el fin de permitir: (i) el intercambio de información entre programas creados independientemente y otros programas (incluido este) y (ii) el uso mutuo de información que se haya intercambiado, deben ponerse en contacto con:

IBM Corporation   
 Location Code IE9  
 Tower 3   
 900 Chelmsford Street  
 Lowell, MA 01851-5114   
 U.S.A.

Dicha información puede estar disponible, sujeta a los términos y condiciones correspondientes, incluyendo, en algunos casos, el pago de una tarifa.

El programa con licencia descrito en este documento y todo el material con licencia disponible para el mismo son suministrados por IBM bajo los términos del Acuerdo de cliente de IBM, el Acuerdo Internacional de Programas bajo Licencia u otro acuerdo equivalente entre IBM y nosotros.

Los datos de rendimiento aquí contenidos se han determinado en un entorno controlado. Por lo tanto, los resultados obtenidos en otros entornos operativos pueden variar de forma significativa. Es posible que algunas medidas se hayan desarrollado con sistemas en nivel de desarrollo y no hay garantía de que estas medidas sean las mismas en sistemas con disponibilidad general. Además, algunas medidas se pueden haber estimado mediante extrapolación. Los resultados reales pueden variar. Los usuarios de este documento deben verificar los datos aplicables a su entorno específico.

La información relativa a productos no IBM se ha obtenido de los proveedores de estos productos, su publicidad u otras fuentes públicamente disponibles. IBM no ha probado estos productos y no puede confirmar la precisión de su rendimiento, su compatibilidad o cualquier otra reclamación relacionada con productos que no sean de IBM. Las preguntas relacionadas con las prestaciones de los productos que no son de IBM deberán dirigirse a los proveedores de estos productos.

Todas las declaraciones relacionadas con futuras directrices o intenciones de IBM están sujetas a cambios o a su retirada sin previo aviso y sólo representan objetivos.

Esta información contiene ejemplos de datos e informes utilizados en operaciones comerciales diarias. Para ilustrarlas de la forma más completa posible, los ejemplos incluyen los nombres de personas, empresas, marcas y productos. Todos estos nombres son ficticios y cualquier similitud a los nombres y direcciones que haya utilizado una empresa real es pura coincidencia.

Si ha optado por visualizar la copia software de esta información, puede que no aparezcan las fotografías y las ilustraciones a color.

Esta oferta de software no utiliza cookies ni otro tipo de tecnología para recopilar información de identificación personal.
