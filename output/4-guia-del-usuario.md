---
product: IBM OpenPages 9.0.0
product_key: SSFUEU_9.0.0
file: 4
guide: Guía del usuario
covers: Guía del usuario — Avisos
chapters: 23
topics: 250
words: 70345
tasks: 75
concepts: 153
references: 3
tables: 26
code_blocks: 17
figures: 245
applies_to: En cloud
updated: 2025-09-26
lang: es
source: https://www.ibm.com/docs/es/openpages/9.0.0?topic=user-guide
extracted: 2026-09-11
---

# 4 · Guía del usuario

> **Qué hay en este archivo.** «Guía del usuario» de IBM OpenPages 9.0.0, completa: 23 capítulos. 250 temas, 75 de ellos procedimientos paso a paso, 26 tablas, 17 bloques de código, 245 figuras y 70.345 palabras.
>
> **Capítulos:** Guía del usuario · Novedades · Cómo empezar con la interfaz de usuario · Su cuadro de mandos · Trabajo con objetos · Creación y asociación de objetos · Utilización de filtros en vistas de cuadrícula · Búsqueda global · Trabajar con archivos y enlaces · Trabajar con informes · Cuestionarios · Aplicación de firmas y bloqueos · y 11 más.
>
> **Se aplica a:** En cloud.
>
> **Si lo que buscas no está acá.** El índice de los 2.511 temas del producto, con su archivo y su ancla, está en `index.md`.

**Términos propios de este archivo:** cuadrícula, encuestado, filtro, subsecciones, conformidad, respuestas, comentarios, subsección, reguladora, vencimiento, masivo, reguladores, inserta, gráfico.

## Índice de este archivo

- [Guía del usuario](#guía-del-usuario)
- [Novedades](#novedades)
  - [Novedades de la versión 9.0.0.5](#novedades-de-la-versión-9005)
  - [Novedades de la versión 9.0.0.4](#novedades-de-la-versión-9004)
  - [Características nuevas de la versión 9.0.0.3](#características-nuevas-de-la-versión-9003)
  - [Características nuevas de la versión 9.0.0.2](#características-nuevas-de-la-versión-9002)
  - [Características nuevas de la versión 9.0.0.1](#características-nuevas-de-la-versión-9001)
  - [Características nuevas de la versión 9.0.0.0](#características-nuevas-de-la-versión-9000)
  - [Características nuevas de la versión 8.3.0.2](#características-nuevas-de-la-versión-8302)
  - [Características nuevas de la versión 8.3.0.1](#características-nuevas-de-la-versión-8301)
  - [Nuevas características en la versión 8.3.0](#nuevas-características-en-la-versión-830)
  - [Nuevas características en la versión 8.2.0.3](#nuevas-características-en-la-versión-8203)
  - [Nuevas características en la versión 8.2.0.2](#nuevas-características-en-la-versión-8202)
  - [Nuevas características en la versión 8.2.0.1](#nuevas-características-en-la-versión-8201)
  - [Características nuevas de la versión 8.2.0](#características-nuevas-de-la-versión-820)
- [Cómo empezar con la interfaz de usuario](#cómo-empezar-con-la-interfaz-de-usuario)
  - [Utilización de la IU](#utilización-de-la-iu)
  - [Inicio de sesión en IBM OpenPages for IBM Cloud Pak for Data](#inicio-de-sesión-en-ibm-openpages-for-ibm-cloud-pak-for-data)
  - [Inicio de sesión](#inicio-de-sesión)
  - [Cierre de sesión](#cierre-de-sesión)
  - [Navegación por la interfaz de usuario](#navegación-por-la-interfaz-de-usuario)
  - [Uso del **menú principal**](#uso-del-menú-principal)
  - [Uso de la barra de navegación](#uso-de-la-barra-de-navegación)
  - [Cambiar configuración regional](#cambiar-configuración-regional)
  - [Cambio de la contraseña](#cambio-de-la-contraseña)
  - [Modificación del perfil](#modificación-del-perfil)
  - [Cambiar el tema](#cambiar-el-tema)
  - [Cambio del periodo de elaboración de informes](#cambio-del-periodo-de-elaboración-de-informes)
  - [Utilización de IBM watsonx Assistant](#utilización-de-ibm-watsonx-assistant)
  - [Traducción de valores en campos de texto](#traducción-de-valores-en-campos-de-texto)
  - [Modelos de aprendizaje automático](#modelos-de-aprendizaje-automático)
  - [Proporcionar comentarios utilizando una encuesta NPS](#proporcionar-comentarios-utilizando-una-encuesta-nps)
  - [Ciclos de vida configurables](#ciclos-de-vida-configurables)
  - [Servicios de procesamiento de lenguaje natural](#servicios-de-procesamiento-de-lenguaje-natural)
  - [Etiquetas](#etiquetas)
- [Su cuadro de mandos](#su-cuadro-de-mandos)
  - [Pestaña Inicio](#pestaña-inicio)
  - [Pestaña Mis tareas](#pestaña-mis-tareas)
  - [Pestaña Tareas de suscripción](#pestaña-tareas-de-suscripción)
  - [Pestaña Tareas de supervisión](#pestaña-tareas-de-supervisión)
  - [Añadir un informe o una ficha personalizada](#añadir-un-informe-o-una-ficha-personalizada)
  - [Añadir paneles y widgets a una pestaña](#añadir-paneles-y-widgets-a-una-pestaña)
    - [Adición de un panel de gráfico](#adición-de-un-panel-de-gráfico)
    - [Adición de un panel personalizado](#adición-de-un-panel-personalizado)
    - [Adición de un panel de favoritos](#adición-de-un-panel-de-favoritos)
    - [Adición de un panel de informes](#adición-de-un-panel-de-informes)
    - [Adición de un panel Mis tareas](#adición-de-un-panel-mis-tareas)
    - [Adición de un panel de tareas de suscripción](#adición-de-un-panel-de-tareas-de-suscripción)
    - [Adición de un panel de tareas de supervisión](#adición-de-un-panel-de-tareas-de-supervisión)
- [Trabajo con objetos](#trabajo-con-objetos)
  - [Utilización de las vistas de cuadrícula para buscar, abrir y trabajar con objetos](#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos)
  - [Completar el trabajo asignado](#completar-el-trabajo-asignado)
  - [Compartición de información clave sobre un objeto](#compartición-de-información-clave-sobre-un-objeto)
  - [Visualización de información en gráficos](#visualización-de-información-en-gráficos)
  - [Visualización de la información en un diagrama de árbol](#visualización-de-la-información-en-un-diagrama-de-árbol)
  - [Validación de una acción de flujo de trabajo](#validación-de-una-acción-de-flujo-de-trabajo)
  - [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula)
  - [Cómo abrir una vista rápida](#cómo-abrir-una-vista-rápida)
  - [Aplicación de cambios a varios objetos con actualización masiva en una vista de cuadrícula](#aplicación-de-cambios-a-varios-objetos-con-actualización-masiva-en-una-vista-de-cuadrícula)
  - [Adición y eliminación de etiquetas de varios objetos en una vista de cuadrícula](#adición-y-eliminación-de-etiquetas-de-varios-objetos-en-una-vista-de-cuadrícula)
  - [Visualización del historial de cambios en la pestaña Actividad](#visualización-del-historial-de-cambios-en-la-pestaña-actividad)
  - [Exportación de datos de los resultados filtrados](#exportación-de-datos-de-los-resultados-filtrados)
  - [Imprimir una vista en PDF](#imprimir-una-vista-en-pdf)
  - [Edición de objetos en una vista de tarea](#edición-de-objetos-en-una-vista-de-tarea)
  - [Comentar objetos](#comentar-objetos)
  - [Copia de objetos](#copia-de-objetos)
  - [Supresión de objetos](#supresión-de-objetos)
  - [Renombrar un objeto desde una vista de tarea](#renombrar-un-objeto-desde-una-vista-de-tarea)
  - [Cierre de sesión](#cierre-de-sesión-1)
- [Creación y asociación de objetos](#creación-y-asociación-de-objetos)
  - [Creación de instancias de objeto](#creación-de-instancias-de-objeto)
  - [Reglas para la denominación de objetos](#reglas-para-la-denominación-de-objetos)
  - [Creación de objetos desde una vista de cuadrícula](#creación-de-objetos-desde-una-vista-de-cuadrícula)
  - [Creación de objetos desde un panel de control](#creación-de-objetos-desde-un-panel-de-control)
  - [Creación de objetos hijo desde una vista de tarea](#creación-de-objetos-hijo-desde-una-vista-de-tarea)
  - [Asociaciones entre objetos](#asociaciones-entre-objetos)
  - [Disociación de objetos](#disociación-de-objetos)
  - [Asociación padre principal](#asociación-padre-principal)
    - [Cambio de la asociación padre principal](#cambio-de-la-asociación-padre-principal)
- [Utilización de filtros en vistas de cuadrícula](#utilización-de-filtros-en-vistas-de-cuadrícula)
  - [Búsqueda de objetos con el recuadro Buscar](#búsqueda-de-objetos-con-el-recuadro-buscar)
  - [Utilización de filtros de carpeta (Entidad de negocios)](#utilización-de-filtros-de-carpeta-entidad-de-negocios)
  - [Utilización de filtros públicos](#utilización-de-filtros-públicos)
  - [Utilización de filtros privados](#utilización-de-filtros-privados)
  - [Definición de filtros privados](#definición-de-filtros-privados)
  - [Utilización de filtros ad hoc](#utilización-de-filtros-ad-hoc)
  - [Edición de filtros privados](#edición-de-filtros-privados)
  - [Supresión de filtros guardados](#supresión-de-filtros-guardados)
  - [Borrar resultados de filtro](#borrar-resultados-de-filtro)
- [Búsqueda global](#búsqueda-global)
  - [Búsqueda de objetos mediante la búsqueda global](#búsqueda-de-objetos-mediante-la-búsqueda-global)
  - [Técnicas avanzadas de búsqueda global](#técnicas-avanzadas-de-búsqueda-global)
- [Trabajar con archivos y enlaces](#trabajar-con-archivos-y-enlaces)
  - [Acerca de archivos adjuntos](#acerca-de-archivos-adjuntos)
    - [Reglas para la denominación de carpetas y archivos](#reglas-para-la-denominación-de-carpetas-y-archivos)
  - [Añadir y trabajar con archivos (adjuntos) en objetos](#añadir-y-trabajar-con-archivos-adjuntos-en-objetos)
  - [Añadir y gestionar todos los archivos (adjuntos)](#añadir-y-gestionar-todos-los-archivos-adjuntos)
  - [Enlaces de URL externos](#enlaces-de-url-externos)
    - [Creación de enlaces de URL en objetos](#creación-de-enlaces-de-url-en-objetos)
- [Trabajar con informes](#trabajar-con-informes)
  - [Acerca de los informes](#acerca-de-los-informes)
  - [Generar y visualizar informes](#generar-y-visualizar-informes)
  - [Enviar un informe por correo electrónico](#enviar-un-informe-por-correo-electrónico)
  - [Visualizar informes en un formato diferente](#visualizar-informes-en-un-formato-diferente)
- [Cuestionarios](#cuestionarios)
  - [Resumen del cuestionario](#resumen-del-cuestionario)
    - [Puntuación de la plantilla de cuestionario y métodos de puntuación](#puntuación-de-la-plantilla-de-cuestionario-y-métodos-de-puntuación)
    - [Fórmulas de puntuación de la plantilla de cuestionario](#fórmulas-de-puntuación-de-la-plantilla-de-cuestionario)
  - [Plantillas de cuestionario](#plantillas-de-cuestionario)
    - [Creación de un objeto de plantilla de cuestionario](#creación-de-un-objeto-de-plantilla-de-cuestionario)
    - [Edición de una plantilla de cuestionario](#edición-de-una-plantilla-de-cuestionario)
    - [Añadido de secciones y subsecciones a una plantilla de cuestionario](#añadido-de-secciones-y-subsecciones-a-una-plantilla-de-cuestionario)
    - [Añadido de preguntas a una plantilla de cuestionario](#añadido-de-preguntas-a-una-plantilla-de-cuestionario)
      - [Creación de dependencias de preguntas](#creación-de-dependencias-de-preguntas)
      - [Supresión de dependencias de pregunta](#supresión-de-dependencias-de-pregunta)
      - [Asociar respuestas a un campo](#asociar-respuestas-a-un-campo)
    - [Establecer los valores de campo de un objeto basándose en las respuestas de un encuestado](#establecer-los-valores-de-campo-de-un-objeto-basándose-en-las-respuestas-de-un-encuestado)
    - [Creación de un objeto basado en las respuestas de un encuestado](#creación-de-un-objeto-basado-en-las-respuestas-de-un-encuestado)
    - [Copia de un objeto basado en las respuestas de un encuestado](#copia-de-un-objeto-basado-en-las-respuestas-de-un-encuestado)
    - [Adición de variables de objeto a una plantilla de cuestionario](#adición-de-variables-de-objeto-a-una-plantilla-de-cuestionario)
    - [Adición de enlaces a una plantilla de cuestionario](#adición-de-enlaces-a-una-plantilla-de-cuestionario)
      - [Enlaces fijos en las plantillas de cuestionario](#enlaces-fijos-en-las-plantillas-de-cuestionario)
      - [Enlaces dinámicos en plantillas de cuestionario](#enlaces-dinámicos-en-plantillas-de-cuestionario)
      - [Enlaces a informes de IBM Cognos Analytics en plantillas de cuestionario](#enlaces-a-informes-de-ibm-cognos-analytics-en-plantillas-de-cuestionario)
  - [evaluaciones de cuestionarios](#evaluaciones-de-cuestionarios)
    - [Completar una evaluación de cuestionario](#completar-una-evaluación-de-cuestionario)
    - [Revisión de una evaluación de cuestionario](#revisión-de-una-evaluación-de-cuestionario)
    - [Creación de una evaluación de cuestionario ad hoc](#creación-de-una-evaluación-de-cuestionario-ad-hoc)
  - [Programas](#programas)
    - [Creación y configuración de un programa](#creación-y-configuración-de-un-programa)
    - [Lanzamiento de un programa](#lanzamiento-de-un-programa)
- [Aplicación de firmas y bloqueos](#aplicación-de-firmas-y-bloqueos)
  - [Añadir una firma](#añadir-una-firma)
  - [Revocación de firmas](#revocación-de-firmas)
  - [Visualización de firmas](#visualización-de-firmas)
  - [Bloqueo y desbloqueo de objetos](#bloqueo-y-desbloqueo-de-objetos)
- [Utilización de objetos de OpenPages Platform](#utilización-de-objetos-de-openpages-platform)
  - [Entidades empresariales](#entidades-empresariales)
  - [Evaluaciones de riesgos](#evaluaciones-de-riesgos)
  - [Evaluaciones de evaluación de riesgos](#evaluaciones-de-evaluación-de-riesgos)
  - [Objetivos de control](#objetivos-de-control)
  - [Procesos](#procesos)
  - [Evaluaciones de proceso](#evaluaciones-de-proceso)
  - [Subprocesos](#subprocesos)
  - [Controles](#controles)
  - [Planes de conformidad y Temas de conformidad](#planes-de-conformidad-y-temas-de-conformidad)
    - [Despliegue de varios temas de conformidad en una entidad de negocios](#despliegue-de-varios-temas-de-conformidad-en-una-entidad-de-negocios)
    - [Despliegue de un tema de conformidad en varias entidades de negocio](#despliegue-de-un-tema-de-conformidad-en-varias-entidades-de-negocio)
  - [Evaluaciones de control](#evaluaciones-de-control)
  - [Riesgos](#riesgos)
  - [Evaluaciones de riesgos](#evaluaciones-de-riesgos-1)
  - [Planes de pruebas](#planes-de-pruebas)
    - [Planes de pruebas](#planes-de-pruebas-1)
    - [Resultados de prueba](#resultados-de-prueba)
  - [Problemas y elementos de acción](#problemas-y-elementos-de-acción)
    - [Adición de comentarios a un elemento de acción](#adición-de-comentarios-a-un-elemento-de-acción)
    - [Completar elementos de acción](#completar-elementos-de-acción)
  - [Preferencias y Grupos de preferencias](#preferencias-y-grupos-de-preferencias)
- [Utilización de OpenPages Internal Audit Management (IAM)](#utilización-de-openpages-internal-audit-management-iam)
  - [Objetos de OpenPages Internal Audit Management](#objetos-de-openpages-internal-audit-management)
    - [Planes de auditoría de resumen](#planes-de-auditoría-de-resumen)
    - [Auditorías](#auditorías)
    - [Entidades auditables](#entidades-auditables)
    - [Secciones de auditoría](#secciones-de-auditoría)
    - [Planes](#planes)
    - [Informes](#informes)
    - [Conclusiones](#conclusiones)
    - [Auditores](#auditores)
    - [Comentarios de revisión de auditoría](#comentarios-de-revisión-de-auditoría)
- [Utilización de OpenPages IT Governance (ITG)](#utilización-de-openpages-it-governance-itg)
  - [Términos de OpenPages IT Governance que debe conocer](#términos-de-openpages-it-governance-que-debe-conocer)
  - [Objetos de gobierno de TI interno de OpenPages](#objetos-de-gobierno-de-ti-interno-de-openpages)
    - [Activos y enlaces de activos](#activos-y-enlaces-de-activos)
      - [Activos](#activos)
      - [Enlaces de activos](#enlaces-de-activos)
    - [Líneas base](#líneas-base)
    - [Incidencias](#incidencias)
    - [KRI y valores de KRI](#kri-y-valores-de-kri)
    - [KPI y valores de KPI](#kpi-y-valores-de-kpi)
    - [Mandatos](#mandatos)
    - [Políticas](#políticas)
    - [Procedimientos](#procedimientos)
    - [Requisitos](#requisitos)
    - [Submandatos](#submandatos)
    - [Sistemas](#sistemas)
    - [Amenazas](#amenazas)
    - [Vulnerabilidades](#vulnerabilidades)
    - [Renuncias](#renuncias)
- [Uso de objetos de OpenPages Operational Risk Management](#uso-de-objetos-de-openpages-operational-risk-management)
  - [Objetos de OpenPages Operational Risk Management](#objetos-de-openpages-operational-risk-management)
    - [KRI y valores de KRI](#kri-y-valores-de-kri-1)
    - [KPI y valores de KPI](#kpi-y-valores-de-kpi-1)
    - [Eventos de pérdida](#eventos-de-pérdida)
    - [Impactos de pérdida](#impactos-de-pérdida)
    - [Recuperaciones de pérdidas](#recuperaciones-de-pérdidas)
    - [Análisis de escenario](#análisis-de-escenario)
    - [Resultados del caso de ejemplo](#resultados-del-caso-de-ejemplo)
    - [Pérdidas FIRST](#pérdidas-first)
    - [Pérdidas ORIC](#pérdidas-oric)
    - [Pérdidas ORX](#pérdidas-orx)
    - [Centros de costes](#centros-de-costes)
- [Utilización de OpenPages Policy Management](#utilización-de-openpages-policy-management)
  - [Términos de IBM OpenPages Policy Management que debe conocer](#términos-de-ibm-openpages-policy-management-que-debe-conocer)
  - [Objetos de gestión de políticas de OpenPages](#objetos-de-gestión-de-políticas-de-openpages)
    - [Aplicabilidades del reglamento](#aplicabilidades-del-reglamento)
    - [Mandatos](#mandatos-1)
    - [Submandato](#submandato)
    - [Requisito](#requisito)
    - [KRI y valores de KRI](#kri-y-valores-de-kri-2)
    - [Incidencias](#incidencias-1)
    - [Renuncias](#renuncias-1)
    - [KPI y valores de KPI](#kpi-y-valores-de-kpi-2)
    - [Políticas](#políticas-1)
    - [Comentario de revisión de política](#comentario-de-revisión-de-política)
    - [Procedimientos](#procedimientos-1)
    - [Campañas](#campañas)
    - [Empleados](#empleados)
    - [Atestaciones](#atestaciones)
    - [Autoridades reguladoras](#autoridades-reguladoras)
    - [Interacciones de las autoridades reguladoras, categorías de RI y solicitudes de RI](#interacciones-de-las-autoridades-reguladoras-categorías-de-ri-y-solicitudes-de-ri)
      - [Categorías de RI](#categorías-de-ri)
      - [Solicitudes de RI](#solicitudes-de-ri)
    - [Cambios reguladores y tareas reguladoras](#cambios-reguladores-y-tareas-reguladoras)
- [Utilización de IBM OpenPages Financial Controls Management](#utilización-de-ibm-openpages-financial-controls-management)
  - [Objetos OpenPages Financial Controls Management](#objetos-openpages-financial-controls-management)
    - [Subcuentas](#subcuentas)
    - [Declaraciones](#declaraciones)
    - [Cuentas](#cuentas)
- [Utilización de OpenPages Regulatory Compliance Management](#utilización-de-openpages-regulatory-compliance-management)
  - [Objetos de OpenPages Regulatory Compliance Management](#objetos-de-openpages-regulatory-compliance-management)
- [objetos de OpenPages Model Risk Governance](#objetos-de-openpages-model-risk-governance)
  - [OpenPages Model Risk Governance](#openpages-model-risk-governance)
  - [objetos de OpenPages Model Risk Governance](#objetos-de-openpages-model-risk-governance-1)
    - [Solicitud de cambio](#solicitud-de-cambio)
    - [Comité](#comité)
    - [Métrica](#métrica)
    - [Valor de métrica](#valor-de-métrica)
    - [Modelo](#modelo)
    - [Atestación de modelo](#atestación-de-modelo)
    - [Entrada de modelo](#entrada-de-modelo)
    - [Enlace de modelo](#enlace-de-modelo)
    - [Salida del modelo](#salida-del-modelo)
    - [Tarjeta de puntuación de riesgo modelo](#tarjeta-de-puntuación-de-riesgo-modelo)
    - [Caso de uso de modelo](#caso-de-uso-de-modelo)
    - [Revisar](#revisar)
    - [Despliegue de modelos](#despliegue-de-modelos)
- [Utilización de OpenPages Third Party Risk Management](#utilización-de-openpages-third-party-risk-management)
  - [OpenPages Objetos de gestión de riesgos de terceros](#openpages-objetos-de-gestión-de-riesgos-de-terceros)
- [Utilización de OpenPages Business Continuity Management](#utilización-de-openpages-business-continuity-management)
- [Avisos](#avisos)


# Guía del usuario

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=user-guide)

La publicación *IBM OpenPages Guía del usuario* está pensada para su uso con OpenPages®. Esta guía contiene instrucciones para utilizar la aplicación OpenPages .

## IBM OpenPages documentación

IBM® mantiene un conjunto de servicios de documentación IBM OpenPages, IBM OpenPages for IBM Cloud Pak for Datay IBM OpenPages on Cloud despliegues. La documentación de IBM OpenPages describe determinadas características y funciones que pueden no estar disponibles en la nube.

Si tiene alguna pregunta sobre la funcionalidad disponible en la versión del producto que está utilizando, póngase en contacto con el soporte deIBM utilizando el [portal de soporte de IBM](https://www.ibm.com/mysupport).

## Funciones de accesibilidad

Las características de accesibilidad ayudan a los usuarios que tienen alguna discapacidad física, por ejemplo movilidad restringida o visión limitada, a utilizar productos de tecnología de la información. La documentación de OpenPages tiene características de accesibilidad. Los documentos PDF son complementarios y no incluyen características de accesibilidad.

## Novedades

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ug-whats-new)

Hay características nuevas y modificadas disponibles para IBM OpenPages®.

Para obtener información sobre todas las características nuevas de este release, consulte la publicación *IBM OpenPages New Features Guide*.

### Novedades de la versión 9.0.0.5

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-9005)

Las novedades de la versión 9.0.0.4 de " IBM OpenPages® " se describen en las tablas siguientes.

Para conocer las nuevas funciones de la versión 9.0.0.5, consulte la [*Guía de nuevas funciones deIBM OpenPages*](2-caracteristicas-nuevas.md#características-nuevas).

### Novedades de la versión 9.0.0.4

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-9004)

Las novedades de la versión IBM OpenPages® 9.0.0.4 se describen en las siguientes tablas.

Para obtener más información, consulte la [*IBM OpenPages*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras en la interfaz de usuario

**Tabla 1. UI centrada en tareasmejoras**

| Mejora | Enlaces a la documentación |
| --- | --- |
| Puede hacer clic en **¿Ha olvidado la contraseña?** en la pantalla de inicio de sesión si olvida su contraseña. | [iniciando sesión](#inicio-de-sesión) |
| El término *tablero* se refiere ahora a la página de inicio en su conjunto. El cuadro de mandos es la página inicial que se muestra a los usuarios cuando inician sesión en OpenPages. | [Tu panel de control](#su-cuadro-de-mandos) |
| Puedes añadir informes y pestañas personalizadas a tu panel de control. El cuadro de mandos puede contener hasta tres pestañas para Cognos® y OpenPages y hasta tres pestañas personalizadas. | [Añadir un informe o una ficha personalizada](#añadir-un-informe-o-una-ficha-personalizada) |
| Si no desea que una acción de respuesta intente volver a crear un objeto nuevo si ya existe un objeto con el mismo nombre, seleccione **Omitir si existe**. | [Crear un objeto a partir de las respuestas de un encuestado](#creación-de-un-objeto-basado-en-las-respuestas-de-un-encuestado) |
| Puede utilizar una expresión al establecer los valores de campo de un objeto basándose en las respuestas de un encuestado. | [Establecimiento de los valores de campo de un objeto en función de las respuestas de un encuestado](#establecer-los-valores-de-campo-de-un-objeto-basándose-en-las-respuestas-de-un-encuestado) |
| Ya está disponible el tipo de gráfico de barras apiladas. | [Ejemplo: Barra apilada](3.6-guia-del-administrador.md#ejemplos-de-diagrama-de-gráfico) |

### Características nuevas de la versión 9.0.0.3

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-9003)

Las nuevas características de IBM OpenPages® versión 9.0.0.3 se describen en las tablas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras en la interfaz de usuario

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Mejora | Enlaces a la documentación |
| --- | --- |
| Puede editar y suprimir comentarios en cuestionarios. | [Completar una evaluación de cuestionario](#completar-una-evaluación-de-cuestionario)<br>[Revisión de una evaluación de cuestionario](#revisión-de-una-evaluación-de-cuestionario) |
| En un cuestionario, puede hacer que una respuesta sea exclusiva para una pregunta de varias opciones. Cuando un encuestado elige una respuesta exclusiva, no puede seleccionar ninguna otra respuesta para la pregunta después de seleccionar una respuesta exclusiva. | [Añadido de preguntas a una plantilla de cuestionario](#añadido-de-preguntas-a-una-plantilla-de-cuestionario)<br>[Completar una evaluación de cuestionario](#completar-una-evaluación-de-cuestionario) |

### Características nuevas de la versión 9.0.0.2

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-9002)

Las características nuevas de IBM OpenPages® versión 9.0.0.2 se describen en las tablas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras en la interfaz de usuario

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Mejora | Enlaces a la documentación |
| --- | --- |
| Puede configurar una acción de respuesta en una plantilla de cuestionario para crear un objeto nuevo o copiar un objeto existente. | [Creación de un objeto basado en las respuestas de un encuestado](#creación-de-un-objeto-basado-en-las-respuestas-de-un-encuestado)<br>[Copia de un objeto basado en las respuestas de un encuestado](#copia-de-un-objeto-basado-en-las-respuestas-de-un-encuestado) |
| Cuando está revisando una evaluación de cuestionario, puede establecer un filtro para que solo vea las preguntas con puntuaciones bajas. | [Revisión de una evaluación de cuestionario](#revisión-de-una-evaluación-de-cuestionario) |
| Ahora puede tener varias vistas de informe disponibles al visualizar un objeto. | [Compartir información clave sobre un objeto](#compartición-de-información-clave-sobre-un-objeto) |

### Características nuevas de la versión 9.0.0.1

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-9001)

Las nuevas características de IBM OpenPages® versión 9.0.0.1 se describen en las tablas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras en la interfaz de usuario

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Mejora | Enlaces a la documentación |
| --- | --- |
| Puede configurar una acción de respuesta en una plantilla de cuestionario para establecer los valores de los campos en los objetos basándose en las respuestas que proporciona un encuestado en una evaluación de cuestionario. | [Establecimiento de los valores de campo de un objeto basándose en las respuestas de un encuestado](#establecer-los-valores-de-campo-de-un-objeto-basándose-en-las-respuestas-de-un-encuestado) |
| Una vista de informe muestra información de sólo lectura sobre un objeto. Se configura de forma similar a una vista de tarea. Mientras que una vista de tarea está diseñada para que una persona o grupo trabaje en esa actividad o tarea, una vista de informe es un resumen de la información clave sobre el objeto. Con una vista de informe, los usuarios pueden centrarse en, y resaltar, los aspectos más esenciales del objeto. | [Compartir información clave sobre un objeto](#compartición-de-información-clave-sobre-un-objeto) |
| Al seleccionar **Imprimir** ![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/print_button.png) en una vista, puede imprimirlo en PDF. El archivo se puede imprimir o guardar como PDF. Incluye texto enriquecido, estado de flujo de trabajo, etiquetas, enlaces a objetos, toda la información de cuadrícula tabular y la fecha y hora de la exportación para la auditabilidad. | [Impresión de una vista en PDF](#imprimir-una-vista-en-pdf) |
| Hay nuevas opciones de filtro en la vista Actividad. Ahora puede refinar la búsqueda de acuerdo con fechas, horas y usuarios específicos. | [Visualización del historial de cambios en la pestaña Actividad](#visualización-del-historial-de-cambios-en-la-pestaña-actividad) |
| Ahora puede utilizar etiquetas para filtrar una vista de cuadrícula.<br>Además, ahora puede restringir una condición de objeto relacionada para mostrar solo los padres primarios. | [Definición de filtros privados](#definición-de-filtros-privados) |

### Características nuevas de la versión 9.0.0.0

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-9000)

Las nuevas características de IBM OpenPages® versión 9.0.0.0 se describen en las tablas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras en la interfaz de usuario

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Visualización de informes como archivos formateados o sin formato de Microsoft Excel | [Visualizar informes en un formato diferente](#visualizar-informes-en-un-formato-diferente) |
| Selección del perfil al iniciar la sesión | [iniciando sesión](#inicio-de-sesión) |
| Utilización de una plantilla de cuestionario para especificar lógica compleja para que las dependencias oculten o muestren preguntas | [Creación de dependencias de pregunta](#creación-de-dependencias-de-preguntas) |

### Características nuevas de la versión 8.3.0.2

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-8302)

Las características nuevas de IBM OpenPages® versión 8.3.0.2 se describen en las tablas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras en la interfaz de usuario

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Si desea editar la declaración de limitación de responsabilidad en una plantilla de cuestionario, debe modificar el texto de la aplicación `questionnaire.intro.label.informationDetails`. | [Edición de una plantilla de cuestionario](#edición-de-una-plantilla-de-cuestionario) |
| Cuando edita archivos de Microsoft Office directamente desde OpenPages, el botón **Ver** ya no se visualiza de forma predeterminada y el archivo se extrae ahora cuando pulsa el botón **Editar** . | [Añadir y trabajar con archivos (adjuntos) en objetos](#añadir-y-trabajar-con-archivos-adjuntos-en-objetos) |
| Puede utilizar la característica de asistencia de contenido para ayudarle a añadir variables de objeto a una plantilla de cuestionario. | [Adición de variables de objeto a una plantilla de cuestionario](#adición-de-variables-de-objeto-a-una-plantilla-de-cuestionario) |

### Características nuevas de la versión 8.3.0.1

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-8301)

Las características nuevas de IBM OpenPages® versión 8.3.0.1 se describen en las tablas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras en la interfaz de usuario

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Adición de etiquetas para categorizar objetos y realizar búsquedas basadas en dichas categorías | [Adición y eliminación de etiquetas](#etiquetas) |
| Cómo los encuestados pueden elegir copiar respuestas, comentarios y archivos adjuntos de una evaluación de cuestionario existente para ahorrar tiempo | [Completar una evaluación de cuestionario](#completar-una-evaluación-de-cuestionario) |

### Nuevas características en la versión 8.3.0

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-830)

Las nuevas características de IBM OpenPages® versión 8.3.0 se describen en las tablas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras de la interfaz de usuario centrada en tareas

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Mejoras en los cuestionarios | [Cuestionarios](#cuestionarios) |

#### IU estándar

Se ha eliminado la IU estándar .

Se ha eliminado el elemento de menú **![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg)** > **Cambiar a IU estándar** .

### Nuevas características en la versión 8.2.0.3

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-8203)

Las nuevas características de IBM OpenPages® versión 8.2.0.3 se describen en las tablas siguientes.

#### Mejoras de la interfaz de usuario centrada en tareas

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| IBM Watson® Discovery se ha añadido como un servicio de procesamiento de lenguaje natural. | [Servicios de procesamiento de lenguaje natural](#servicios-de-procesamiento-de-lenguaje-natural) |
| La capacidad de buscar campos en Vistas de tareas, Vistas de creación y Vistas rápidas | [Navegar por la interfaz de usuario](#navegación-por-la-interfaz-de-usuario), [Abrir una vista rápida](#cómo-abrir-una-vista-rápida) |
| Los administradores ahora pueden configurar los campos que están disponibles para la actualización masiva en Vistas de cuadrícula. | [Aplicación de cambios a varios objetos con actualización masiva en una vista de cuadrícula](#aplicación-de-cambios-a-varios-objetos-con-actualización-masiva-en-una-vista-de-cuadrícula) |
| Ahora los usuarios pueden definir pestañas de informes en su panel de control. Anteriormente, los administradores sólo podían crear pestañas de informes utilizando la tarea **Gestionar paneles de control**. | [Añadir un informe o una ficha personalizada](#añadir-un-informe-o-una-ficha-personalizada) |

### Nuevas características en la versión 8.2.0.2

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-8202)

Las nuevas características de IBM OpenPages® versión 8.2.0.2 se describen en las tablas siguientes.

#### Mejoras de la interfaz de usuario centrada en tareas

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Aplicación de un tema de color utilizando la nueva tarea **![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg)** > **Cambiar tema** . | [Cambiar el tema](#cambiar-el-tema) |
| Usabilidad mejorada para desasociar objetos. Se ha añadido un botón **Eliminar** en los campos de relación de cuadrícula que tienen una acción Asociar. | [Completar el trabajo asignado](#completar-el-trabajo-asignado) |
| Recibir recordatorios por correo electrónico cuando las tareas vencen o se retrasan. | [Completar el trabajo asignado](#completar-el-trabajo-asignado) |
| Completar tareas de flujo de trabajo masivo:<br>• Mediante vistas de cuadrícula para dar soporte a acciones de flujo de trabajo masivo.<br>• Mediante la ventana **Tareas completadas con acciones de flujo de trabajo masivo** en el panel Mis tareas y el panel, la pestaña Tareas de suscripción y el panel y la pestaña Tareas de supervisión y el panel. | [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula) |
| Utilización del nuevo icono ![Icono Mover](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/move_icon_tfui.jpg) en las vistas de cuadrícula para mover objetos de una carpeta a otra. | [Utilización de las vistas de cuadrícula para buscar, abrir y trabajar con objetos](#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos) |

### Nuevas características en la versión 8.2.0.1

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-8201)

Las nuevas características de IBM OpenPages® versión 8.2.0.1 se describen en las tablas siguientes.

#### IBM OpenPages for IBM Cloud Pak for Data

OpenPages ahora se puede instalar en IBM OpenPages for IBM Cloud Pak for Data.

#### Mejoras de la interfaz de usuario centrada en tareas

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Utilizando IBM Watson® Language Translator para traducir los valores de los campos de texto al idioma asociado a su entorno local. | [Traducción de valores en campos de texto](#traducción-de-valores-en-campos-de-texto) |
| Cómo abrir y editar documentos de Microsoft Office directamente desde OpenPages. | [Añadir y trabajar con archivos (adjuntos) en objetos](#añadir-y-trabajar-con-archivos-adjuntos-en-objetos) |
| Proporcionar comentarios sobre una encuesta de Net Promoter Score (NPS). | [Proporcionar comentarios utilizando una encuesta NPS](#proporcionar-comentarios-utilizando-una-encuesta-nps) |
| El conmutador **Modalidad de edición** se ha renombrado como **Mostrar campos editables**. | [Navegación por la interfaz de usuario](#navegación-por-la-interfaz-de-usuario) |
| El botón **Analytics** para IBM Cognos® Analytics se ha movido de la cabecera al menú principal. | [Uso del menú Principal](#uso-del-menú-principal) |
| Ahora se puede aplicar el modo seguro a los paneles de control. | [Añadir paneles y widgets a una pestaña](#añadir-paneles-y-widgets-a-una-pestaña) |

### Características nuevas de la versión 8.2.0

`Guía del usuario › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=new-features-in-version-820)

Las nuevas características de IBM OpenPages® versión 8.2.0 se describen en las tablas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### Mejoras de la interfaz de usuario centrada en tareas

**Tabla 1. Mejoras de Interfaz de usuario centrada en tareas**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| La nueva solución IBM OpenPages Business Continuity Management . | [Utilización de OpenPages Business Continuity Management](#utilización-de-openpages-business-continuity-management) |
| Acceso a IBM Watson® Assistant con el icono ![Icono Iniciar conversación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/start_chat_icon.jpg) . | [Navegación por la interfaz de usuario](#navegación-por-la-interfaz-de-usuario) |
| El proceso de revisión para las evaluaciones de cuestionario ahora puede ser controlado por GRC Workflow. | [Resumen del cuestionario](#resumen-del-cuestionario) |
| Evaluaciones de cuestionario ad hoc. | [Creación de una evaluación de cuestionario ad hoc](#creación-de-una-evaluación-de-cuestionario-ad-hoc) |
| Los campos de clasificador se muestran ahora utilizando un botón y panel de IBM Watson Insights. | [Servicios de procesamiento de lenguaje natural](#servicios-de-procesamiento-de-lenguaje-natural)<br>[Creación de objetos desde una vista de cuadrícula](#creación-de-objetos-desde-una-vista-de-cuadrícula) |
| Gráficas de Gantt en paneles de control | [Adición de un panel de gráfico](#adición-de-un-panel-de-gráfico) |
| Nuevo tipo de método y campo de agregación para las suma, promedio, mín y máx en gráficos en los paneles de control. | [Adición de un panel de gráfico](#adición-de-un-panel-de-gráfico) |
| Pestaña Actividad en la vista de tarea. | [Visualización del historial de cambios en la pestaña Actividad](#visualización-del-historial-de-cambios-en-la-pestaña-actividad) |
| El botón Suprimir en un diseño de cuadrícula de una vista de tarea. | [Completar el trabajo asignado](#completar-el-trabajo-asignado) |
| Al definir filtros privados en las vistas de cuadrícula, el nuevo conmutador **Mostrar valores ocultos** controla si se visualizan los valores ocultos para los campos de valores enumerados. | [Definición de filtros privados](#definición-de-filtros-privados) |
| Un panel Informes en el panel de control ahora puede listar todos los informes por categoría, según como se haya establecido el nuevo campo **Origen de datos**. | [Adición de un panel de informes](#adición-de-un-panel-de-informes) |
| Un panel de búsqueda en el panel de control utiliza la búsqueda global para encontrar información. | [Búsqueda de objetos mediante la búsqueda global](#búsqueda-de-objetos-mediante-la-búsqueda-global) |
| Cómo se manejan los Cálculos de GRC en Vistas de creación y Vistas de tarea. | [Creación de objetos desde una vista de cuadrícula](#creación-de-objetos-desde-una-vista-de-cuadrícula)<br>[Completar el trabajo asignado](#completar-el-trabajo-asignado) |
| Se ha hecho más coherente la función de incorporación y extracción de archivos. | [Añadir y trabajar con archivos (adjuntos) en objetos](#añadir-y-trabajar-con-archivos-adjuntos-en-objetos) |

#### Mejoras de la interfaz de usuario estándar

El **Portal de procesos** de la página de inicio se ha eliminado. Daba soporte a la integración de IBM OpenPages con IBM® Business Process Manager, que se ha eliminado.

#### Mejoras en las soluciones

Consulte la publicación *IBM OpenPages Guía de soluciones* para obtener una lista completa de todos los cambios realizados en las soluciones.

## Cómo empezar con la interfaz de usuario

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-getting-started-ui)

Aprenda a navegar por la interfaz de usuario para acceder a la información, cambiar la contraseña, el entorno local, el perfil y el tema.

### Utilización de la IU

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-using)

Utilice la interfaz de usuario para completar las tareas que tiene asignadas y para buscar información en OpenPages®.

Si es un implementador o administrador responsable de definir vistas en la interfaz de usuario, consulte el tema [Configuración de la interfaz de usuario](3.2-guia-del-administrador.md#configuración-de-la-interfaz-de-usuario) en la *IBM OpenPages*.

Si es un implementador o administrador responsable de definir los flujos de trabajo, consulte el tema [Configuración del flujo de trabajo de GRC](3.3-guia-del-administrador.md#configuración-de-flujos-de-trabajo) en la *IBM OpenPages*.

### Inicio de sesión en IBM OpenPages for IBM Cloud Pak for Data

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-logging-in-openpages-cloud-pak-data)

Utilice este procedimiento para iniciar sesión en IBM OpenPages® for IBM Cloud Pak for Data.

#### Acerca de esta tarea

Antes de iniciar sesión, obtenga la URL de la instancia de IBM OpenPages for IBM Cloud Pak for Data de su administrador, así como el nombre de usuario y la contraseña.

#### Procedimiento

1. Abra un navegador web soportado. En la **barra de ubicación**, introduzca la URL de la instancia de IBM OpenPages for IBM Cloud Pak for Data, por ejemplo:

   `https://your-server.com/openpages-openpagesinstance1/`
2. Escriba su nombre de usuario y contraseña.
3. Pulse **Iniciar sesión**.

   Ha iniciado sesión automáticamente en IBM OpenPages for IBM Cloud Pak for Data.
4. Si aparece la página **Seleccionar perfil**, haga clic en el perfil que desea utilizar.

   Un perfil determina el aspecto de la aplicación. Su perfil determina el contenido del Panel de control, la disposición y el contenido de las vistas, los tipos de objetos que ve, etc. Su administrador configura uno o varios perfiles para usted. Cada perfil puede adaptarse a una tarea específica.

#### Qué hacer a continuación

Complete su trabajo. Cuando haya terminado, puede finalizar la sesión realizando los pasos siguientes:

1. Suprima el texto que sigue al nombre del servidor en la **Barra de ubicación** del navegador. Por ejemplo, cambie `https://your-server.com/openpages-openpagesinstance1/` por `https://your-server.com/`.

   Se visualiza la interfaz de Cloud Pak for Data.
2. Pulse el botón **Perfil y valores** en la parte superior derecha de la pantalla.

   ![Menú de cierre de sesión de Cloud Pak for Data](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/cpd_logout.png)
3. Cuando se visualice el menú, pulse **Cerrar sesión**.
4. Cuando se le solicite que confirme que desea finalizar la sesión, pulse **Cerrar sesión**.

### Inicio de sesión

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-logging-in)

Puede iniciar sesión en IBM OpenPages® utilizando el navegador.

#### Acerca de esta tarea

Antes de iniciar sesión, obtenga la URL OpenPages y su nombre de usuario y contraseña, si el inicio de sesión único no está configurado.

#### Procedimiento

1. Abra Google Chrome, Apple Safari o Microsoft Edge. En la **barra de direcciones**, introduzca la URL OpenPages, por ejemplo:

   `https://opserver:10111/openpages`
2. Escriba su nombre de usuario y contraseña.

   Si estos campos no se visualizan, se configura el inicio de sesión único y se abre la aplicación. Vaya al paso 4.

   **Se aplica a:** [En cloud](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue) [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

   Si olvidas tu contraseña, puedes hacer clic en **¿Olvidaste la contraseña?** en la pantalla de inicio de sesión. En la página **Olvidaste la contraseña**, introduce tu nombre de usuario para recibir un mensaje de correo electrónico explicándote cómo restablecer tu contraseña.

   Si tu acceso a OpenPages está controlado mediante el inicio de sesión único (SSO) como método de autenticación, o si tu acceso está controlado por un servidor de autenticación LDAP (Lightweight Directory Access Protocol), recibes un mensaje de correo electrónico en el que se te explica que no puedes restablecer tu contraseña.

   > **Importante:** Si un administrador desactiva esta función configurando `/Platform/Security/Password/Reset/Enabled` como **false**, aparecerá el mensaje **¿Ha olvidado la contraseña?** no aparece en la pantalla de inicio de sesión.
3. Pulse **Iniciar sesión**.
4. Si se muestra la página **Seleccionar perfil** , pulse el perfil que desea utilizar.

   Un perfil determina el aspecto de la aplicación. El perfil determina el contenido del panel de control, el diseño y el contenido de las vistas, los tipos de objetos que ve, etc. El administrador configura uno o varios perfiles. Cada perfil se puede adaptar a una tarea específica.

#### Qué hacer a continuación

Complete su trabajo. Cuando haya terminado, pulse ![Icono de menú de usuario](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) para abrir el menú **Usuario** y pulse **Cerrar sesión**.

### Cierre de sesión

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-logging-out)

Puede finalizar una sesión y salir de la aplicación.

#### Acerca de esta tarea

Es una práctica recomendada cerrar la sesión en lugar de cerrar simplemente la ventana del navegador.

OpenPages® excede automáticamente el tiempo de espera y se cierra después de un periodo de inactividad del sistema.

Si intenta realizar una operación después de que OpenPages haya excedido el tiempo de espera, el sistema se mueve automáticamente a la página Iniciar sesión en la que puede volver a iniciar la sesión.

#### Procedimiento

1. Pulse ![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) para abrir el menú Usuario.
2. Pulse **Cerrar sesión**.

### Navegación por la interfaz de usuario

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-navigating)

La interfaz de usuario está diseñada para facilitar la navegación.

*Figura 1. Ejemplo de la interfaz de usuario*

![La interfaz de usuario tiene una barra de navegación, un área de trabajo y menús.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_new_ui_menu_navigation.png)

La interfaz de usuario tiene los componentes siguientes:

**Tabla 1. Componentes de IU**

| Componentes de IU | Descripción |
| --- | --- |
| ![Atajo del panel de control de IBM OpenPages](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/dashboard_shortcut_task_focused_ui.jpg)<br>![Acceso directo de la página de inicio](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_home_page.jpg) | Ambos muestran el cuadro de mandos en el área de trabajo. Para obtener más información sobre el cuadro de mandos, consulte [Su cuadro de mandos](#su-cuadro-de-mandos). |
| menú Principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png) | Abre el menú Principal.<br>Para obtener más información, consulte [Uso del menú principal](#uso-del-menú-principal). |
| Barra de navegación | La barra de navegación contiene ![Acceso directo de la página de inicio](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_home_page.jpg) y una pestaña para cada vista que tenga abierta.<br>Para obtener más información, consulte [Uso de la barra de navegación](#uso-de-la-barra-de-navegación). |
| ![Icono WalkMe](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/walkme_icon.png) | Abre WalkMe. WalkMe es una herramienta de terceros que puede utilizar para guiarle a través de OpenPages. WalkMe le proporciona visitas guiadas, visiones generales de características y recursos incorporados para ayudarle a sacar el máximo provecho de su implementación deOpenPages .<br>Los administradores utilizan los valores de registro para inhabilitar o habilitar WalkMe. El icono ![Icono WalkMe](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/walkme_icon.png) no se muestra en la interfaz si WalkMe está desactivado.<br>Si haces clic en ![Icono WalkMe](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/walkme_icon.png) y WalkMe no se inicia, actualiza la página de tu navegador.<br>WalkMe se abre en inglés de forma predeterminada, pero puede cambiar el valor de idioma. |
| ![Icono de menú Notificaciones (campana)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/notifications_menu_icon_task_focused_ui.jpg) | Abre la lista de notificaciones.<br>La lista no incluye notificaciones sobre el trabajo que es necesario completar. |
| ![Ver icono de información de valor](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/view_insights_icon.png) | Identifica un campo de entrada necesario para ejecutar un modelo de aprendizaje automático personalizado.<br>Para obtener más información sobre los modelos de aprendizaje automático personalizados, consulte [Modelos de aprendizaje automático](#modelos-de-aprendizaje-automático). |
| Abrir menú de administración ![Icono de menú de valores (engranaje)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_menu_icon_task_focused_ui.jpg) | Abre el menú **Administración** . |
| ![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) | Abre el menú **Usuario** . |
| ![Icono Iniciar conversación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/start_chat_icon.jpg) | Abre un chat bot donde puede hacer preguntas que utilizan IBM watsonx Assistant™. El botón **Iniciar chat** solo aparece si hay un asistente configurado y se le permite acceder a él.<br>Para obtener más información, consulte [Uso de IBM watsonx Assistant](#utilización-de-ibm-watsonx-assistant). |
| ![Botón de búsqueda (lupa)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-search-tfui.png) | En una vista de cuadrícula, puede buscar objetos en la cuadrícula.<br>En otras vistas, puede buscar campos. |
| ![Botón Mostrar campos editables](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/reveal_editable_fields.png) | En una vista de tarea, puede pasar el cursor por encima de los campos para ver cuáles son editables. Cuando el icono ![icono de edición](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_icon.jpg) aparece junto a un campo, puede hacer clic en el campo para ponerlo en modo de edición.<br>Si desea poner todos los campos en modo de edición en lugar de editar un campo cada vez, haga clic en ![Botón Mostrar campos editables](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/reveal_editable_fields.png) en la barra de herramientas de la vista.<br>Este icono y botón están ocultos en determinadas situaciones, como cuando el objeto está bloqueado o no tiene permiso de control de acceso para editarlo. |
| ![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/print_button.png) | En una vista de tarea o una vista de informe, imprime la vista o la guarda en un PDF. |
| ![Botón Watson Language Translator](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png) | En una vista de tarea, los valores de los campos de texto se convierten al idioma asociado a su entorno local.<br>Para obtener más información, consulte [Traducción de valores en campos de texto](#traducción-de-valores-en-campos-de-texto). |
| ![Botón de comentarios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_feedback.jpg) | Abre una encuesta Net Promoter Score (NPS) en la que puede proporcionar comentarios sobre el producto a IBM®. Si usted es elegible para recibir una encuesta, siempre se muestra en la página de inicio. Puede proporcionar comentarios en cualquier momento y con la frecuencia que desee. También es posible que se le solicite periódicamente que envíe una encuesta cuando inicie la sesión.<br>Para obtener más información, consulte [Proporcionar opiniones mediante una encuesta NPS](#proporcionar-comentarios-utilizando-una-encuesta-nps). |
| Área de trabajo | El área de trabajo muestra el panel de control y las vistas.<br>Para obtener más información, consulte los siguientes temas:<br>• [Pestaña Inicio](#pestaña-inicio)<br>• [Pestaña Mis tareas](#pestaña-mis-tareas)<br>• [Pestaña Tareas de suscripción](#pestaña-tareas-de-suscripción)<br>• [Pestaña Tareas de supervisión](#pestaña-tareas-de-supervisión)<br>• [Utilización de las vistas de cuadrícula para buscar, abrir y trabajar con objetos](#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos)<br>• [Creación de objetos desde una vista de cuadrícula](#creación-de-objetos-desde-una-vista-de-cuadrícula)<br>• [Completar el trabajo asignado](#completar-el-trabajo-asignado) |
| ![Icono de lista de opciones](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/close_task_focused_ui.jpg) | Contiene una lista de pestañas que puede seleccionar. También puede cerrar todas las pestañas. |
| ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg) | Abre un menú que se utiliza para configurar pestañas y paneles.<br>Para obtener más información, consulte [Añadir paneles y widgets a una pestaña](#añadir-paneles-y-widgets-a-una-pestaña). |
| Botón Atrás del navegador | Abre la última página web que se ha almacenado en la sesión. |
| Botón Adelante del navegador | Avanza en el historial de sesiones del navegador de páginas web. |

### Uso del **menú principal**

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-using-primary-menu)

El menú Principal lista las categorías de tipos de objeto a las que puede acceder en IBM OpenPages®.

Introduzca un tipo de objeto en el cuadro **Buscar tipo de objeto** para encontrar el tipo de objeto que desea o amplíe las categorías para ver los tipos de objeto.

En función de la configuración, **Análisis** puede mostrarse como el primer elemento de menú. Púlselo para abrir IBM® Cognos® Analytics.

Al hacer clic en un tipo de objeto, como Entidades empresariales, se abre una lista de objetos. Para obtener información, consulte [Utilización de vistas de cuadrícula para buscar, abrir y trabajar con objetos](#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos).

*Figura 1. Ejemplo del menú Principal*

![Menú principal que muestra una lista de objetos OpenPages](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_task_focused_ui.png)

### Uso de la barra de navegación

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-using-navigation-bar)

La barra de navegación contiene ![Acceso directo de la página de inicio](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_home_page.jpg) y una pestaña para cada vista que tenga abierta. Pulse en las pestañas para ir de una vista a otra.

*Figura 1. Ejemplo de barra de navegación*

![Barra de navegación con pestañas abiertas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_navgiation_bar_task_focused_ui.jpg)

Los iconos se describen en la tabla siguiente:

**Tabla 1. Iconos de la barra de navegación**

| Icono | Descripción |
| --- | --- |
| ![Acceso directo de la página de inicio](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_home_page.jpg) | Ambos muestran el cuadro de mandos en el área de trabajo. Para obtener más información sobre el cuadro de mandos, consulte [Su cuadro de mandos](#su-cuadro-de-mandos). |
| ![icono de vista de cuadrícula en la barra de navegación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_navgiation_bar_grid_icon_task_focused_ui.jpg) | La pestaña es una vista que lista los objetos del tipo de objeto seleccionado. Este tipo de vista se denomina Vista de cuadrícula. |
| ![icono de vista de creación en la barra de navegación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_navgiation_bar_creation_icon_task_focused_ui.jpg) | La pestaña es una vista en la que se está creando un objeto pero que no está abierto para editarlo. Este tipo de vista se denomina Vista de creación. |
| ![vista de creación - abrir para editar - icono en la barra de navegación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_navgiation_bar_creation_edit_icon_task_focused_ui.jpg) | La pestaña es una vista en la que se está creando un objeto, que además se puede editar. Este tipo de vista se denomina Vista de creación. |
| ![icono de vista de tarea en la barra de navegación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_navgiation_bar_task_icon_task_focused_ui.jpg) | La pestaña es una vista en la que se está completando una tarea, pero el objeto no está abierto para editarlo. Este tipo de vista se denomina Vista de tarea. |
| ![vista de tarea - abrir para editar - icono en la barra de navegación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_navgiation_bar_task_edit_icon_task_focused_ui.jpg) | La pestaña es una vista en la que se está completando una tarea, y el objeto se puede editar. Este tipo de vista se denomina Vista de tarea. |
| ![Icono Eclipse (tres puntos)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/close_task_focused_ui.jpg) | Le permite elegir una pestaña o cerrar todas las pestañas abiertas en la barra de navegación. |

Se puede abrir un objeto para editarlo en una sola vista. Si hay un objeto abierto para su edición en una vista e intenta abrirlo en otra vista, recibirá una advertencia.

### Cambiar configuración regional

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-changing-your-locale)

Puede cambiar el valor de configuración regional. Con esto, cambia el idioma de la interfaz de usuario, así como el formato de visualización de los números y las fechas.

#### Acerca de esta tarea

#### Procedimiento

1. Pulse ![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) para abrir el menú Usuario.
2. Pulse **Cambiar entorno local** y seleccione un idioma.
3. Pulse **Guardar**.

### Cambio de la contraseña

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-changing-your-password)

Puede cambiar la contraseña.

#### Procedimiento

1. Pulse ![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) para abrir el menú Usuario.
2. Pulse **Cambiar contraseña**.
3. Escriba la contraseña antigua en **Contraseña actual**.
4. Especifique una nueva contraseña en **Nueva contraseña**y confírmela.

   Tenga en cuenta los siguientes requisitos de contraseña:

   - La longitud máxima es de 32 caracteres.
   - Las contraseñas distinguen entre mayúsculas y minúsculas.
   - Si su empresa utiliza el inicio de sesión único o LDAP, no puede cambiar una contraseña con IBM OpenPages®. Debe cambiarlo con el inicio de sesión único o la aplicación LDAP.
5. Pulse **Guardar**.

### Modificación del perfil

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-changing-your-profile)

Un perfil determina el aspecto de la experiencia de usuario en la interfaz de usuario. Determina el contenido del panel de control, el diseño y el contenido de todas las vistas, y cualquier filtro disponible para el uso en la vista de cuadrícula. El administrador configura uno o varios perfiles automáticamente, que se pueden adaptar a una tarea específica.

#### Acerca de esta tarea

Si su administrador configura varios perfiles, puede cambiar el perfil mediante **Cambiar perfil** en el menú de usuario.

> **Importante:** Asegúrese de guardar el trabajo antes de cambiar el perfil.

#### Procedimiento

1. Pulse ![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) para abrir el menú Usuario.
2. Pulse **Cambiar perfil**.

   *Figura 1. Cambiar perfil*

   ![Se muestra el menú. Cambiar perfil está resaltado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/change_profile.png)

   > **Nota:** Si no ve **Cambiar perfil** en el menú, sólo tiene un perfil.
3. Seleccione el perfil que desea utilizar y, a continuación, pulse **Guardar**.

#### Qué hacer a continuación

El cambio surte efecto de inmediato sin necesidad de cerrar sesión. Después de cambiar el perfil, el panel de control y la funcionalidad de las vistas podrían cambiar.

### Cambiar el tema

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-changing-your-theme)

Un tema determina el diseño de color que se aplica en la interfaz de usuario. El administrador puede configurar uno o más temas para que los utilice.

#### Acerca de esta tarea

Si no elige ningún tema, se aplica un tema predeterminado.

Después de elegir un tema, se conserva la próxima vez que inicie la sesión.

#### Procedimiento

1. Pulse ![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) para abrir el menú Usuario.
2. Pulse **Cambiar tema**.
3. Seleccione un tema.
4. Pulse **Guardar**.

#### Resultados

El cambio tiene lugar inmediatamente.

### Cambio del periodo de elaboración de informes

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-changing-reporting-period)

Puede ver los datos de un periodo de elaboración de informes actual o pasado. Sin embargo, sólo puede modificar datos en el periodo de elaboración de informes actual.

#### Acerca de esta tarea

Si se definen periodos de informes pasados, puede cambiar el periodo de elaboración de informes en la interfaz de usuario.

Si la opción **Cambiar periodo de elaboración de informes** del menú Usuario no se visualiza, sólo hay un periodo de elaboración de informes (el periodo de elaboración de informes actual).

#### Procedimiento

1. Abra el objeto con el que desea trabajar.
2. Pulse ![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) para abrir el menú Usuario.

   El periodo de elaboración de informes elegido actualmente se visualiza encima de **Cambiar periodo de elaboración de informes**.
3. Pulse **Cambiar periodo de elaboración de informes**.
4. Seleccione un periodo de elaboración de informes.
5. Pulse **Guardar**.

   La vista se renueva en función del periodo de elaboración de informes. Si cambia a un periodo de creación de informes pasado, el objeto pasa a ser de sólo lectura. Los campos no se pueden cambiar y los flujos de trabajo no se pueden iniciar ni pueden avanzar.

#### Qué hacer a continuación

Repita los pasos para seleccionar el periodo de elaboración de informes actual u otro periodo de elaboración de informes anterior. Si cambia al periodo de elaboración de informes actual, el objeto se convierte en editable y los flujos de trabajo se pueden iniciar y avanzar.

### Utilización de IBM watsonx Assistant

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-using-watsonx-assistant)

Utilice IBM watsonx Assistant™ para acceder a la asistencia las 24 horas del día para OpenPages®.

IBM watsonx Assistant es un bot de conversación que proporciona respuestas de texto interactivas, búsqueda en lenguaje natural y enlaces directos a páginas específicas en OpenPages, por ejemplo, a una vista de creación donde puede especificar un problema o evento de pérdida.

Cuando IBM watsonx Assistant está configurado y tiene permiso para acceder a él, el icono ![Icono Iniciar conversación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/start_chat_icon.jpg) se muestra en todas las páginas de la interfaz de usuario.

Pulse ![Icono Iniciar conversación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/start_chat_icon.jpg) y haga una pregunta en el bot de conversación.

#### Tutorial

Este vídeo proporciona una visión general del uso de IBM watsonx Assistant.

[Este vídeo proporciona una visión general de IBM watsonx Assistant.](https://video.ibm.com/embed/channel/25817967/video/op-watson-assistant)

### Traducción de valores en campos de texto

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-translating-values-in-text-fields)

Puede traducir valores en campos de texto al idioma asociado con el entorno local utilizando ![Botón Conversión automática](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png).

En una vista de tarea, pulse ![Botón Conversión automática](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png). Los valores de los campos de texto se traducen al idioma asociado a su entorno local. Para cada campo traducido, puede conmutar entre los idiomas pulsando **Ver original** y **Ver traducción**. Pulse el icono Información para ver una puntuación de confianza. Pulse ![Botón Conversión automática](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png) de nuevo para desactivar los valores traducidos.

- Los valores de campo de texto (series simples y series largas) se traducen. Los campos de texto enriquecido y los valores de campo enumerados no se traducen.
- No hay diferenciación entre el inglés de Estados Unidos y el Reino Unido.
- Los valores traducidos en una vista de tarea no se pueden editar.
- No se guardan en el objeto.

#### Ejemplo 1

Su entorno local está establecido en inglés de Estados Unidos. Puede ver objetos de cambio normativo en una vista de tarea.

- En primer lugar, ve un objeto de cambio regulador que procede de un organismo regulador francés. Contiene valores de campo en francés. Pulse ![Botón Conversión automática](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png). Los valores de campo de texto en francés se traducen al inglés.
- A continuación, puede ver un objeto de cambio normativo que procede de un organismo regulador de la UE. Contiene valores de campo de texto en inglés, francés y portugués. Pulse ![Botón Conversión automática](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png). Los valores del campo de texto en inglés permanecen sin cambios. Los valores de campo de texto en francés y portugués se traducen al inglés.

#### Ejemplo 2

El entorno local está establecido en japonés. Puede ver objetos de cambio normativo en una vista de tarea.

- En primer lugar, puede ver un objeto de cambio regulador que procede de un organismo regulador de EE.UU. Contiene valores de campo en inglés. Pulse ![Botón Conversión automática](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png). Los valores de campo de texto en inglés se convierten en japonés.
- A continuación, puede ver un objeto de cambio normativo que procede de un organismo regulador de la UE. Contiene valores de campo en inglés, francés y portugués. Pulse ![Botón Conversión automática](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png). Los valores de campo de texto se convierten en japonés.

### Modelos de aprendizaje automático

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-machine-learning-models)

Su organización puede crear modelos de aprendizaje automático que el administrador puede configurar para que se ejecuten en OpenPages®. Cuando se ejecuta un modelo de aprendizaje automático, utiliza los datos de entrada de los campos OpenPages para generar información y sugerencias en directo en las vistas de OpenPages . Puede ejecutar estos modelos para extraer información de valor de los datos y aplicar sugerencias del modelo para establecer valores de campo y etiquetas.

Al abrir una vista, es posible que vea el icono **Ver información** ![Ver icono de información de valor](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/view_insights_icon.png). Este icono muestra que un modelo de aprendizaje automático está disponible para el campo. Los resultados se muestran en un panel lateral como se muestra en la Figura 1.

*Figura 1. Un ejemplo de un control en una vista de tarea que muestra información en el panel lateral*

![Un ejemplo de una vista de control que muestra el panel Insights](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/wml_generated_control.png)

#### Cómo se ejecuta un modelo

Los administradores pueden configurar modelos para que se ejecuten automática o manualmente. Tanto para manual como para automático, el modelo sólo se puede ejecutar cuando todos los campos necesarios tienen datos.

- Automáticamente

  Si el administrador ha configurado el modelo para que se ejecute automáticamente, especifique o modifique valores para un campo de entrada que el modelo requiere y pulse en cualquier lugar fuera de ese campo para ejecutar el modelo. Si el administrador ha configurado notificaciones para el modelo, se muestra una notificación cuando el modelo termina de ejecutarse.

  Si desea ver los resultados después de que se ejecute el modelo, pulse ![Ver icono de información de valor](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/view_insights_icon.png) asociado con el campo de entrada que ha modificado. Los resultados se muestran en un panel lateral.
- Manualmente

  Si el administrador ha configurado el modelo para que se ejecute manualmente, el modelo sólo se ejecuta cuando pulsa ![Ver icono de información de valor](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/view_insights_icon.png) asociado a un campo de entrada. Si el administrador ha configurado las notificaciones, se muestra una notificación cuando el modelo termina de ejecutarse. Los resultados se muestran en un panel lateral.

#### Cómo se aplican las sugerencias de modelo

Un administrador configura un modelo para determinar cómo se aplican las sugerencias o los conocimientos del modelo a los campos o etiquetas.

- Conjunto de usuarios

  Si el administrador ha configurado el modelo para proporcionar sugerencias para campos o etiquetas, puede seleccionar las sugerencias que desea aplicar. Si se define una puntuación de confianza, OpenPages se muestra en el orden de la puntuación de confianza decreciente. De lo contrario, las sugerencias se muestran en el orden en el que se devuelven del modelo. Una puntuación de confianza, que se muestra como un porcentaje, indica la probabilidad de que el resultado se haya determinado correctamente.

  Para establecer campos, pulse el conjunto de sugerencias que desea aplicar.

  *Figura 2. Un ejemplo de un evento de pérdida en una vista de tarea. Los valores de campo se muestran en el panel lateral.*

  ![Un ejemplo de un evento de pérdida en una vista de tarea que muestra el panel lateral](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/set_fields_output.png)

  Para establecer etiquetas, seleccione los recuadros de selección para cada etiqueta que desee aplicar.

  *Figura 3. Un ejemplo de un problema en una vista de tarea. Las etiquetas sugeridas se muestran en el panel lateral.*

  ![Un ejemplo de un problema en una vista de tarea que muestra el panel lateral](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/set_tags_output.png)

  Si desea saber qué campos de entrada se han utilizado para determinar las sugerencias, pulse **Cómo se han determinado las sugerencias** en el panel lateral.
- Umbral establecido

  A veces, el administrador configura el modelo para establecer campos o etiquetas automáticamente basándose en la puntuación de confianza que se muestra en el panel lateral.

  - Etiquetas

    Después de que se ejecute el modelo, al pulsar ![Ver icono de información de valor](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/view_insights_icon.png), el panel lateral muestra las etiquetas sugeridas. Cuando cierre el panel lateral, verá las etiquetas que se aplican al objeto. Si el modelo tiene puntuaciones de confianza, las etiquetas aplicadas incluyen las etiquetas que cumplen o superan el umbral de confianza especificado. De lo contrario, las etiquetas aplicadas incluyen todas las etiquetas sugeridas.
  - Campos

    Después de que se ejecute el modelo, al pulsar ![Ver icono de información de valor](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/view_insights_icon.png), el panel lateral muestra los valores de campo seleccionados. Si el modelo tiene puntuaciones de confianza, se selecciona el conjunto de valores de campo con la puntuación de confianza más alta. De lo contrario, se selecciona el primer conjunto de valores de campo de la lista. Puede ver los valores de campo aplicados a los campos de objeto. Sólo se establecen los campos sin ningún valor existente, a menos que el administrador configure el modelo para sobrescribir los valores de campo existentes cuando se ejecute el modelo.

    Puede optar por pulsar **Guardar** para guardar el objeto con los nuevos valores de campo, o **Cancelar** para mantener el objeto tal como estaba.

### Proporcionar comentarios utilizando una encuesta NPS

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-providing-feedback-using-nps-survey)

Si se ha configurado una encuesta Net Promoter Score , puede enviar comentarios sobre OpenPages® a IBM®.

Los comentarios de los usuarios ayudan a IBM a mejorar OpenPages.

Si una encuesta de Net Promoter Score está habilitada, se le presentan dos posibilidades para completar una encuesta:

- Un botón de comentarios de NPS
- Un formulario de encuesta de NPS después de iniciar sesión

Un botón de comentarios de NPS aparece siempre en la página de inicio si es apto para recibirlos. Puede proporcionar comentarios en cualquier momento y con la frecuencia que desee.

*Figura 1. Botón de comentarios de NPS en la página de inicio*

![Botón de comentarios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_nfg_8201_nps_2.jpg)

Es posible que se muestre un formulario de encuesta NPS cuando inicie la sesión. El hecho de recibir una encuesta y la frecuencia de la misma depende de la configuración y del proveedor de la encuesta.

*Figura 2. Formulario de encuesta de NPS visualizado después de iniciar sesión*

![Formulario de encuesta de NPS](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_nfg_8201_nps_1.jpg)

La encuesta se visualiza en el idioma del entorno local que ha seleccionado. Si cambia la configuración regional, el idioma de la encuesta cambia. Responda a las preguntas, proporcione capturas de pantalla (opcional) y pulse **Enviar**.

### Ciclos de vida configurables

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-configurable-lifecycles)

Los ciclos de vida configurables definen las fases que un tipo de objeto puede seguir.

Los ciclos de vida configurables son una característica heredada que se puede configurar para determinados tipos de objetos y procesos de su organización. La característica se ha sustituido por GRC Workflow. Hasta que su organización haya realizado una transición completa a GRC Workflow, es posible que siga utilizando el ciclo de vida configurable en algunas áreas.

Los ciclos de vida trabajan con evaluaciones de cuestionario e incidentes pero se pueden ampliar a otros objetos. Los usuarios son informados por correo electrónico de que deben completar una tarea, como responder preguntas en una evaluación de cuestionario. Cuando el usuario completa la tarea, el objeto se mueve a la siguiente tarea y al siguiente usuario. El proceso del ciclo de vida finaliza cuando se han completado todas las tareas. Cuenta con un registro de quién ha realizado qué tarea y cuándo.

En cada fase del ciclo de vida, el sistema:

- Identifica un responsable del ciclo de vida
- Define las acciones disponibles para moverse a una fase diferente
- Envía un correo electrónico al nuevo responsable del ciclo de vida
- Define otros atributos (de sólo lectura y en revisión) relacionados con la fase actual

La información del ciclo de vida se almacena en la instancia de objeto. Abra un objeto para ver su información de ciclo de vida. Los campos de ciclo de vida son de sólo lectura, excepto **Responsable de actualización**. El responsable para una fase se define en el activador del ciclo de vida. Un objeto solo puede tener un responsable del ciclo de vida por fase. Un usuario puede añadir un comentario con cada transición.

Para obtener más información, consulte la publicación *IBM OpenPages Guía de soluciones*.

### Servicios de procesamiento de lenguaje natural

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-natural-language-processing-services)

Implementación y configuración de un servicio de proceso de lenguaje natural es una característica opcional en IBM OpenPages®. Si el administrador ha implementado y configurado un servicio de procesamiento de lenguaje natural, puede utilizarlo para interpretar y clasificar el texto que especifique en OpenPages. Un servicio de procesamiento de lenguaje natural entiende la intención detrás del texto y devuelve las clasificaciones sugeridas correspondientes, junto con una puntuación de confianza.

Puede utilizar un servicio de proceso de lenguaje natural con cualquier objeto en OpenPages , pero normalmente se utiliza para clasificar sucesos de pérdida, renuncias, problemas e incidencias. Por ejemplo, puede utilizarlo para dar soporte a la toma de decisiones cuando se clasifica un evento de pérdida en la correcta categorización de Basilea II. También puede utilizarlo para dar soporte a la toma de decisiones cuando clasifica renuncias como excepciones a la conformidad reguladora. La descripción de texto que especifique se utiliza como entrada para un servicio de procesamiento de lenguaje natural que se ha entrenado con conocimientos de los especialistas del dominio.

#### Términos que se deben comprender

- **servicio de procesamiento del lenguaje natural**

  Un servicio de proceso de lenguaje natural utiliza algoritmos de aprendizaje automático para devolver las clases predefinidas coincidentes principales para entradas de texto corto.

- **IBM Watson® Discovery**

  IBM Watson Discovery es un servicio de procesamiento de lenguaje natural en IBM Cloud Pak® for Data. Se configura un servicio IBM Watson Discovery y luego se integra con ' OpenPages. Utiliza la API de Analizar.

- **IBM Watson Natural Language Understanding**

  IBM Watson Natural Language Understanding es un servicio de procesamiento de idiomas en IBM Cloud. Puede entrenar y desplegar modelos de clasificador de texto y, a continuación, integrarlos con OpenPages. IBM Watson Natural Language Understanding aprende de sus datos y puede predecir clasificaciones para textos en los que no está entrenado. IBM Watson Natural Language Understanding es un clasificador de varias etiquetas y varias clases. Asume que el texto probablemente pertenece a más de una clase y puede predecir mejor los textos con múltiples clasificaciones.

- **Configuración del clasificador**

  Una configuración de clasificador en OpenPages define información de conexión a una instancia de un servicio de proceso de lenguaje natural. Para clasificaciones de taxonomía, especifica los campos de destino de clasificador para la instancia. Para asociaciones de objetos, especifica el tipo de objeto que se va asociar, tanto si es una relación hija o padre, y otros atributos.

- **Campo de clasificador**

  Un campo de clasificador es un grupo de campos en OpenPages que contiene el nombre de una configuración de clasificador y un campo de entrada de clasificador. Se muestra un botón IBM Watson Insights en lugar de un campo de clasificador (clasificaciones de taxonomía) o como una acción (asociaciones de objetos).

- **Campo de entrada del clasificador**

  Un campo de entrada de clasificador es un campo de OpenPages que contiene la entrada de texto corto que un servicio de proceso de lenguaje natural interpreta y clasifica. Normalmente es un campo **Descripción**. El texto *Añadir una descripción mejora IBM Watson Sugerencias* se muestra automáticamente debajo de un campo de entrada de clasificador.

- **Campos de destino de clasificador**

  Para las clasificaciones de taxonomía, los campos de destino de clasificador son campos en OpenPages que se establecen cuando un usuario elige sugerencias para un campo de clasificador.

- **Watson Insights**

  La infraestructura subyacente en OpenPages está vinculada a IBM Watson Insights. Se muestra un botón IBM Watson Insights y las sugerencias se muestran en un panel **Watson Insights** .

  Un botón IBM Watson Insights sólo aparece si el clasificador puede realizar una sugerencia basada en el texto especificado. El botón no aparece si el texto no genera sugerencias.

  La interacción del usuario en el panel **Watson Insights** es la misma independientemente de si el servicio es IBM Watson Discovery o IBM Watson Natural Language Understanding.

### Etiquetas

`Guía del usuario › Cómo empezar con la interfaz de usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ui-tags)

En OpenPages®, puede utilizar etiquetas para categorizar objetos y realizar búsquedas basadas en dichas categorías.

Puede añadir etiquetas a los objetos y eliminar etiquetas de los objetos. Sólo los administradores con el permiso de administración de etiquetado pueden habilitar e inhabilitar la característica de etiquetado, y crear, editar e inhabilitar etiquetas. Además, los administradores pueden inhabilitar el etiquetado para tipos de objeto específicos.

Puede añadir y eliminar etiquetas de un objeto sólo bajo las condiciones siguientes:

- El tipo de objeto tiene habilitado el etiquetado.
- El objeto debe estar desbloqueado.
- Debe tener acceso de escritura al objeto.
- Debe estar en el periodo de elaboración de informes actual.
- Al añadir etiquetas, el número de etiquetas debe ser menor que el máximo de 25 etiquetas por objeto.

Cuando una etiqueta está inhabilitada, puede eliminarla de un objeto y puede buscarla, pero no puede añadir una etiqueta inhabilitada a un objeto.

#### Añadir y eliminar etiquetas

Puede añadir etiquetas a objetos y eliminar etiquetas de objetos.

##### Antes de empezar

Sólo puede añadir y eliminar etiquetas en determinadas condiciones. Para más información, consulte [Etiquetas](#etiquetas).

##### Procedimiento

1. Abra una vista de cuadrícula.

   Para obtener más información, consulte [Uso de vistas de cuadrícula para buscar, abrir y trabajar con objetos](#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos).
2. Haga clic en el objeto al que desea añadir o eliminar etiquetas.

   Aparece la pestaña **Tarea**.
3. Para añadir etiquetas si todavía no se ha aplicado ninguna:

   1. En el panel **Etiquetas**, haga clic en " ![Añadir icono de etiquetas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add_tags_icon.png).
   2. Puede escribir caracteres para buscar etiquetas o puede hacer clic en la flecha del cuadro desplegable para mostrar una lista de etiquetas.
   3. Seleccione las etiquetas que desea añadir.
4. Para añadir etiquetas si el objeto ya tiene etiquetas:

   1. Haga clic en el icono del lápiz en el panel **Etiquetas**.
   2. Puede escribir caracteres para buscar etiquetas o puede hacer clic en la flecha del cuadro desplegable para mostrar una lista de etiquetas.
   3. Seleccione las etiquetas que desea añadir.
5. Para eliminar etiquetas, puede elegir uno de los siguientes métodos:

   - Haz clic en la **X** de las etiquetas que quieras eliminar.
   - Escriba caracteres para encontrar las etiquetas que desea eliminar. Deseleccione las etiquetas que desee eliminar.
   - Haga clic en la flecha del cuadro desplegable para mostrar una lista de etiquetas. Deseleccione las etiquetas que desee eliminar.
   - Haga clic en la **X** del número de etiquetas únicas que aparece en el cuadro desplegable para eliminar todas las etiquetas de los objetos seleccionados.

##### Resultados

Los cambios se aplican inmediatamente. Si hace clic fuera del panel **Etiquetas**, el panel sale del modo de edición.

## Su cuadro de mandos

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-your-dashboard)

El cuadro de mandos es el punto central de acceso a la información en OpenPages®.

Su administrador define los cuadros de mando que se aplican a perfiles específicos. Esto significa que verás un panel de control basado en tu perfil actual. Puedes personalizar tu panel de control de las siguientes maneras:

- Reorganizar y ocultar paneles definidos por el administrador en la pestaña Inicio
- Añada, elimine y modifique sus propios paneles en la pestaña Inicio
- Reordenar y ocultar pestañas personalizadas y de informes definidas por el administrador
- Añada, elimine y modifique sus propias fichas personalizadas y de informes.

En el panel de control, puede ver los avisos del sistema si se utiliza el inicio de sesión único (SSO). Si se utiliza SSO, se muestran avisos del sistema cuando se accede al panel de control. El aviso del sistema puede cambiar cuando cierre la sesión y vuelva a acceder al sistema.

El cuadro de mandos organiza la información y las tareas. Contiene las siguientes partes:

- Pestaña Inicio
- Pestañas de tareas
- Fichas de informe
- Pestañas personalizadas

### Pestaña Inicio

La pestaña Inicio muestra paneles con contenidos personalizados para ti. Para obtener más información, consulte [Pestaña Inicio](#pestaña-inicio) y [Añadir paneles y widgets a una pestaña](#añadir-paneles-y-widgets-a-una-pestaña).

### Pestañas de tareas

Las pestañas de tareas resumen los tres tipos de tareas con las que puede trabajar:

- Tareas que se le han asignado.

  Para obtener más información, consulte [Pestaña Mis tareas](#pestaña-mis-tareas).
- Tareas a las que está suscrito.

  Para obtener más información, consulte [Pestaña Tareas de suscripción](#pestaña-tareas-de-suscripción).
- Tareas para las que tiene responsabilidad de supervisión.

  Para obtener más información, consulte [pestaña Tareas de supervisión](#pestaña-tareas-de-supervisión).

Puede completar rápidamente sus tareas utilizando acciones de flujo de trabajo masivo en los paneles Mis tareas, Tarea de suscripción y Tarea de supervisión. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).

### Fichas personalizadas y de informes

Las pestañas personalizadas y de informes forman parte del panel de control que un administrador define para el perfil al que perteneces. Los administradores pueden añadir o modificar el informe y las fichas personalizadas en cualquier momento. Si lo deseas, puedes ocultar las pestañas que un administrador haya definido para tu perfil. Además, puedes definir tus propias pestañas para personalizar tu panel de control.

Siempre debe haber una pestaña de Inicio, pero se pueden añadir y eliminar pestañas personalizadas. Puedes configurar las pestañas personalizadas del mismo modo que configuras la pestaña Inicio.

Es posible que desee crear pestañas personalizadas en lugar de añadir a la ficha Inicio para mantenerlo ordenado y mantener el rendimiento. Además, es posible que desee utilizar pestañas personalizadas para agrupar paneles y widgets relacionados en lugares separados.

Para obtener más información, consulte [Añadir un informe o una ficha personalizada](#añadir-un-informe-o-una-ficha-personalizada).

### Pestaña Inicio

`Guía del usuario › Su panel de control` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=dashboard-home-tab)

La pestaña Inicio consta de paneles con contenido personalizado para ti.

La pestaña Inicio proporciona un acceso personalizado y rápido a las tareas, la información, los objetos y los informes en los que trabaja con más frecuencia.

*Figura 1. Ejemplo de pestaña Inicio*

![Pestaña de inicio con varios paneles de información](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_dashboard_1.png)

En la pestaña Inicio puede realizar las siguientes tareas:

- Pulse elementos accionables en cualquier panel para detallar más rápidamente en qué desea trabajar o ver.
- Reorganizar los paneles
- Ocultar y eliminar paneles
- Añade tus propios paneles. Por ejemplo, puede crear paneles que contengan gráficos, informes y tareas. Para obtener más información, consulte [Añadir paneles y widgets a una pestaña](#añadir-paneles-y-widgets-a-una-pestaña).
- Si un administrador configuró un panel de Búsqueda, puede utilizarlo para buscar texto y valores por tipo de objeto. Para obtener más información, consulte [Búsqueda de objetos mediante la búsqueda global](#búsqueda-de-objetos-mediante-la-búsqueda-global).

Es posible que en la pestaña Inicio aparezcan paneles que no hayas definido. El administrador puede definir paneles para el perfil al que perteneces. Estos paneles se muestran automáticamente en la pestaña Inicio. Puede reordenarlos y ocultarlos. Los administradores pueden añadir o modificar en cualquier momento los paneles que hayan definido. Si has configurado la pestaña Inicio y más tarde un administrador añade un panel a la pestaña Inicio, tu diseño no cambia y el nuevo panel aparece en la parte inferior de la pestaña Inicio.

### Pestaña Mis tareas

`Guía del usuario › Su panel de control` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=dashboard-my-tasks-tab)

Utilice la pestaña Mis tareas para acceder a las tareas que le han sido asignadas.

*Figura 1. Ejemplo de la pestaña Mis tareas*

![Un ejemplo de la ficha Mis tareas que muestra asignaciones y una lista de informes.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/dashboard_task_focused_ui.jpg)

La pestaña Mis tareas contiene dos partes:

- Gráfico
- Cuadrícula

El gráfico resume las tareas que se le han asignado. Puede:

- Filtrar los datos
- Controlar cómo se apilan los datos en cada barra cambiando **Apilar por**
- Pasar el cursor por encima de una barra para ver un resumen de los datos subyacentes
- Seleccionar Semana, Mes o Año para cambiar la vista de fecha

La cuadrícula muestra en una lista sus asignaciones. Cuando selecciona un objeto en la cuadrícula, el objeto se abre y puede empezar a trabajar en él. Para obtener más información, consulte [Completar el trabajo que se le ha asignado](#completar-el-trabajo-asignado).

Puede controlar qué tareas desea incluir tanto en el gráfico como en la cuadrícula mediante la aplicación de un filtro. Puede filtrar sus asignaciones utilizando el siguiente criterio de selección: Nivel de importancia, Nombre de flujo de trabajo, Etapa y Tipo. Por ejemplo, puede elegir incluir solo las tareas cuyo Nivel de importancia sea Alto. Las tareas que no coinciden con el filtro se excluyen del gráfico y de la cuadrícula.

La ventana **Tarea completada con acciones de flujo de trabajo masivo** aparece si la característica está configurada y tiene elementos de trabajo que le pertenecen como responsable. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).

El contenido y el diseño de la pestaña Mis tareas se han configurado para usted y no se pueden cambiar.

### Pestaña Tareas de suscripción

`Guía del usuario › Su panel de control` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=dashboard-subscription-tasks-tab)

Utilice la pestaña Tareas de suscripción para acceder a las tareas a las que está suscrito.

*Figura 1. Ejemplo de la pestaña Tareas de suscripción*

![Un ejemplo de la pestaña Tareas de suscripción que muestra asignaciones en un gráfico y cuadrícula](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/subscriber_dashboard_task_focused_ui.jpg)

La pestaña Tareas de suscripción contiene dos partes:

- Gráfico
- Cuadrícula

En el gráfico puede:

- Filtrar los datos
- Controlar cómo se apilan los datos en cada barra cambiando **Apilar por**
- Pasar el cursor por encima de una barra para ver un resumen de los datos subyacentes
- Seleccionar Semana, Mes o Año para cambiar la vista de fecha

En la cuadrícula se muestran en una lista las tareas a las que está suscrito. Cuando selecciona un objeto en la cuadrícula, el objeto se abre y puede empezar a trabajar en él. Para obtener más información, consulte [Completar el trabajo que se le ha asignado](#completar-el-trabajo-asignado).

Puede controlar qué tareas desea incluir tanto en el gráfico como en la cuadrícula mediante la aplicación de un filtro. Puede filtrar sus asignaciones utilizando el siguiente criterio de selección: Nivel de importancia, Nombre de flujo de trabajo, Etapa y Tipo. Por ejemplo, puede elegir incluir solo las tareas cuyo Nivel de importancia sea Alto. Las tareas que no coinciden con el filtro se excluyen del gráfico y de la cuadrícula.

La ventana **Tarea completada con acciones de flujo de trabajo masivo** se muestra si la característica está configurada y tiene elementos de flujo de trabajo que le pertenecen como suscriptor. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).

El contenido y el diseño de la pestaña Tareas de suscripción se han configurado automáticamente y no se pueden modificar.

### Pestaña Tareas de supervisión

`Guía del usuario › Su panel de control` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=dashboard-oversight-tasks-tab)

Utilice la pestaña Tareas de supervisión para ver un resumen de trabajo asignado a las personas de su área de responsabilidad.

Si tiene acceso a una ficha de Tareas de supervisión, se le designa como responsable de un flujo de trabajo. Los flujos de trabajo generan tareas que puede ver en la pestaña Tareas de supervisión y en su propia pestaña Mis tareas. Estos flujos de trabajo guían una tarea a través de un proceso empresarial definido. Por ejemplo, un flujo de trabajo guía cómo se revisan y finalizan las incidencias. Los asignados y las opciones del botón **Acciones** cambian a medida que un objeto avanza hacia la finalización de su proceso. Un flujo de trabajo puede tener ninguno, uno o muchos usuarios supervisores.

Aunque los diseños de las pestañas Mis tareas y Tareas de supervisión son similares, el contenido y la finalidad son diferentes. La pestaña Mis tareas resume las tareas de un único responsable y la pestaña Tareas de supervisión resume las tareas de varios responsables bajo un usuario supervisor. En calidad de usuario supervisor este panel se utiliza para obtener una descripción general del trabajo asignado a las personas de su equipo, evaluar la carga de trabajo global y acceder a las cargas de trabajo de individuos específicos. Todos los usuarios tienen una pestaña Tareas de supervisión, pero la pestaña está vacía si no se ha designado como usuario supervisor en un flujo de trabajo.

La pestaña Tareas de supervisión tiene dos partes:

- Gráfico
- Cuadrícula

*Figura 1. Ejemplo de la pestaña Tareas de supervisión*

![Un ejemplo de la pestaña Tareas de supervisión que muestra las tareas para las personas asignadas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/oversight_dashboard_task_focused_ui.jpg)

El gráfico muestra en una lista las tareas que pertenecen a las personas de su área de responsabilidad. Puede:

- Filtrar los datos
- Controlar cómo se apilan los datos en cada barra cambiando **Apilar por**
- Pase el ratón por encima de una barra para ver un resumen de los datos subyacentes
- Seleccionar Fecha de vencimiento de etapa o Fecha de vencimiento del flujo de trabajo para cambiar la vista de fecha
- Seleccionar Semana, Mes o Año para cambiar la vista de fecha

La cuadrícula muestra en una lista las tareas que pertenecen a las personas de su área de responsabilidad. En la cuadrícula, puede hacer clic en un usuario que aparece en la columna **Asignatario**. La lista y el gráfico cambian para mostrar sólo las tareas asignadas a esa persona. Puede obtener una descripción general de su carga de trabajo y del trabajo vencido.

También puede seleccionar un objeto pulsando el **Nombre**. Se abre el objeto y, si tiene acceso a la tarea, puede empezar a trabajar en él.

Si aplica un filtro, puede controlar qué tareas desea incluir tanto en el gráfico como en la cuadrícula. Puede filtrar las tareas que utilizan los siguientes criterios de selección: Criticidad, Nombre del flujo de trabajo, Etapa y Tipo. Por ejemplo, puede elegir incluir solo las tareas cuyo Nivel de importancia sea Alto. Las tareas que no coinciden con el filtro se excluyen del gráfico y de la cuadrícula.

La ventana **Tarea completada con acciones de flujo de trabajo masivo** se visualiza si la característica está configurada y tiene elementos de flujo de trabajo que le pertenecen como usuario de supervisión. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).

El contenido y el diseño de la pestaña Tareas de supervisión se han configurado automáticamente y no se pueden modificar.

### Añadir un informe o una ficha personalizada

`Guía del usuario › Su panel de control` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=dashboard-adding-report-custom-tab)

Puedes añadir informes y pestañas personalizadas a tu panel de control. El cuadro de mandos puede contener hasta tres pestañas para Cognos® y OpenPages® y hasta tres pestañas personalizadas.

Es posible que desee crear pestañas personalizadas en lugar de añadir a la ficha Inicio para mantenerlo ordenado y mantener el rendimiento. Además, es posible que desee utilizar pestañas personalizadas para agrupar paneles y widgets relacionados en lugares separados.

#### Acerca de esta tarea

Es posible que tu administrador haya creado informes y fichas personalizadas para el perfil al que perteneces. Si este es el caso, puedes conservar las pestañas o eliminarlas y añadir las tuyas propias, como pestañas para los informes a los que accedes con más frecuencia.

#### Procedimiento

1. En cualquier pestaña, haz clic en ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg).
2. Seleccione **Tablas**.
3. Haz clic en **Nueva pestaña**.
4. Para crear una ficha de informe, realice los siguientes pasos:

   1. haz clic en **Añadir ficha de informe**.
   2. Introduzca una **etiqueta**.

      > **Consejo:** La etiqueta se muestra como título de la pestaña. Para que la lengüeta encaje fácilmente en el salpicadero, utilice una etiqueta lo más corta posible.

      Pulse **Editar** para especificar valores localizados.

      Si se visualiza, pulse ![Botón de traducción automática](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png) para rellenar los valores traducidos a idiomas. Para obtener más información, consulte [Servicios de traducción](3.5-guia-del-administrador.md#servicios-de-traducción).
   3. Seleccione un **Informe**.
   4. Haz clic en **Hecho**.
5. Para crear una pestaña personalizada, realice los siguientes pasos:

   1. haz clic en **Añadir pestaña personalizada**.
   2. Introduzca una **etiqueta**.

      > **Consejo:** La etiqueta se muestra como título de la pestaña. Para que la lengüeta encaje fácilmente en el salpicadero, utilice una etiqueta lo más corta posible.
   3. Haga clic en **Nuevo panel** y seleccione el **Tipo de panel**.

      Para obtener más información sobre cómo añadir un panel, consulte [Añadir paneles y widgets a una pestaña](#añadir-paneles-y-widgets-a-una-pestaña).
   4. Haz clic en **Hecho**.
6. Cuando haya terminado con los cambios, haga clic en **Guardar**.

### Añadir paneles y widgets a una pestaña

`Guía del usuario › Su panel de control` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=dashboard-adding-panels-widgets-tab)

La pestaña Inicio y las pestañas personalizadas te permiten crear tus propios paneles personalizados.

Se pueden añadir los siguientes tipos de paneles:

- Gráficos

  Para obtener más información, consulte [Adición de un panel de gráfico](#adición-de-un-panel-de-gráfico).
- Paneles personalizados

  Para obtener más información, consulte [Adición de un panel personalizado](#adición-de-un-panel-personalizado).
- Objetos favoritos

  Para obtener más información, consulte [Adición de un panel de favoritos](#adición-de-un-panel-de-favoritos).
- Mis tareas

  Para obtener más información, consulte [Adición de un panel Mis tareas](#adición-de-un-panel-mis-tareas).
- Tareas de supervisión

  Para obtener más información, consulte [Adición de un panel de tarea de supervisión](#adición-de-un-panel-de-tareas-de-supervisión).
- Informes

  Para obtener más información, consulte [Adición de un panel de informes](#adición-de-un-panel-de-informes).
- Tareas suscritas

  Para obtener más información, consulte [Panel Añadir una tarea de suscripción](#adición-de-un-panel-de-tareas-de-suscripción).

Puede añadir tantos paneles como desee a una ficha. Sin embargo, antes de añadir un panel, tenga en cuenta que las pestañas con más paneles tardan más en cargarse.

Es posible que desee crear pestañas personalizadas en lugar de añadir a la ficha Inicio para mantenerlo ordenado y mantener el rendimiento. Además, es posible que desee utilizar pestañas personalizadas para agrupar paneles y widgets relacionados en lugares separados.

Es posible que en la pestaña Inicio aparezcan paneles que no hayas definido. El administrador puede definir paneles para el perfil al que perteneces. Estos paneles se muestran automáticamente en la pestaña Inicio. Puede reordenarlos y ocultarlos. Los administradores pueden añadir o modificar en cualquier momento los paneles que hayan definido. Si has configurado la pestaña Inicio y más tarde un administrador añade un panel a la pestaña Inicio, tu diseño no cambia y el nuevo panel aparece en la parte inferior de la pestaña Inicio.

Además, los administradores pueden definir paneles de búsqueda que utilicen la búsqueda global. Para obtener más información, consulte [Búsqueda de objetos mediante la búsqueda global](#búsqueda-de-objetos-mediante-la-búsqueda-global).

Independientemente de la procedencia de los paneles, puedes cambiar la posición de un panel arrastrándolo y colocándolo donde quieras.

La configuración de cada pestaña se guarda en la base de datos y no en la caché del navegador web. Esto significa que puede borrar la memoria caché, pasar a un navegador distinto o iniciar sesión desde un sistema distinto sin cambiar la configuración del panel de control.

Los paneles se muestran uno al lado del otro y hacia abajo en la pantalla. El ancho de pantalla dicta cuántos paneles del panel de control se visualizan uno al lado del otro. En pantallas más pequeñas, por ejemplo, en tabletas y teléfonos, los paneles pueden visualizarse en sentido descendente en la pantalla. Desplácese hacia abajo para ver todos los paneles. Puede utilizar una lista desplegable para pasar de una pestaña a otra.

> Problema:

Si el panel de control encuentra un problema y no puede representarse, puede aplicar la modalidad segura añadiendo `?safeMode=1` al final del URL. El proceso de representación se detiene y puede acceder a la configuración del panel de control para depurar el problema. Elimine `?safeMode=1` del URL para salir de la modalidad segura.

#### Adición de un panel de gráfico

`Guía del usuario › Su panel de control › Añadir paneles y widgets a una pestaña` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tab-adding-chart-panel)

Configura un panel de gráficos en la pestaña Inicio o en una pestaña personalizada para mostrar gráficos de datos a los que accedes con frecuencia.

##### Antes de empezar

Obtenga más información sobre los diagramas de gráfico. Para obtener más información, consulte la publicación *IBM OpenPages Guía del administrador*. Para configurar colores para gráficos, póngase en contacto con el administrador.

##### Acerca de esta tarea

Un gráfico se crea a partir de un tipo de objeto y uno de sus campos. Este campo debe ser una enumeración, que se puede visualizar como una lista, una serie de botones de selección o un menú desplegable. En los gráficos sólo están disponibles las enumeraciones en las que puede seleccionar un único valor. Estas enumeraciones se denominan *campos de serie enumerada de valor único*. Por ejemplo, el tipo de objeto **Riesgo** tiene un campo enumerado denominado **Impacto inherente**. Sólo puede seleccionar un valor de esta enumeración.

Puede profundizar en el gráfico y abrir los objetos relacionados.

Los gráficos en un panel son similares en función a los gráficos en una Vista de Tarea con la excepción de que un gráfico en un panel tiene una suma total de objetos. Pulse la suma total para abrir una vista de cuadrícula de todos los objetos del gráfico.

##### Procedimiento

1. En la pestaña Inicio, o en cualquier pestaña personalizada, haz clic en ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg).
2. Seleccione **Paneles**.
3. Pulse **Panel nuevo**.
4. En el menú **Tipo de panel** , seleccione **Gráfico**.
5. Especifique el nuevo panel **Nombre**.
6. Especifique una **Etiqueta**. La etiqueta se visualiza como un título para el panel.
7. Elija un tipo de objeto . Los tipos de objeto que se listan dependen de los derechos de acceso que le haya asignado un administrador.

   1. Opcional: Seleccione un **Filtro**. Si no se visualizan filtros, no hay filtros asociados al tipo de objeto. Póngase en contacto con el administrador para obtener ayuda.
8. Elija un **Tipo de gráfico**. Los valores válidos son:

   - **Barra**
   - **Anillo**
   - **Gantt**
   - **Barra horizontal**
   - **Gráfico circular**
   - **Barra apilada**

   Si elige un **Tipo de gráfico** de **Barra**, **Tuerca de anillos**, **Barra horizontal**o **Circular** y hay más de 10 valores para mostrar, los valores de campo se muestran para 9 valores. Los otros valores se agrupan y se muestran como **Otros** en el gráfico.
9. Si selecciona Gantt, complete los campos de Configuración del diagrama de Gantt:

   1. Seleccione un **Campo de fecha de inicio**.
   2. Seleccione un **Campo de fecha de finalización**.
   3. Seleccione un **Campo de fila primaria**.
   4. Opcional: Seleccione un **Campo de fila secundaria**.
   5. Seleccione un **Campo de definición de color**.
   6. Pulse **Terminado**.
10. Elija un campo en **Campo de datos de gráfico** (se muestra para todos los tipos de gráficos excepto Gantt).
11. En **Tipo de método** elija Recuento, Suma, Promedio, Mín o Máx (se muestra para todos los tipos de gráficos excepto Gantt). Si elige Suma, Promedio, Mín o Máx, proporcione un campo en el **Campo de agregación**. En el **Campo de agregación** solo se muestran los campos de tipo de moneda, decimal y entero.
12. Seleccione la **Dirección de ordenación**.

    Para los gráficos de barras, puede seleccionar las opciones siguientes:

    - Seleccione **Orden de definición de campo** para visualizar los valores en el gráfico en el mismo orden en que se visualizan en el tipo de objeto.

      Cuando hay más de diez valores para visualizar, los primeros nueve elementos, independientemente de su valor, se muestran en el gráfico y el resto se recopilan en **Otros**.
    - Seleccione **Ascendente** O **Descendente** para visualizar los valores en el gráfico basándose en sus valores.

      Cuando hay más de diez valores para mostrar, los nueve elementos con los valores más altos se muestran en el gráfico y el resto se recopilan en **Otros**.

    Para gráficos de anillos y gráficos circulares, la **Dirección de ordenación** controla lo que sucede cuando hay más de diez valores para mostrar.

    - Con **Ascendente** O **Descendente**, los nueve elementos con los valores más altos se muestran en el gráfico y el resto se recopilan en **Otros**.
    - Con **Orden de definición de campo**, los nueve primeros elementos, independientemente de su valor, se muestran en el gráfico y el resto se recopilan en **Otros**.
13. Pulse **Terminado**.
14. Haz clic en la pestaña para actualizarla y comprueba que el panel se muestra correctamente. Haz clic en un panel y muévelo hasta donde quieras que se muestre en la pestaña.

#### Adición de un panel personalizado

`Guía del usuario › Su panel de control › Añadir paneles y widgets a una pestaña` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tab-adding-custom-panel)

Configura un panel personalizado en la pestaña Inicio o una pestaña personalizada para organizar la información a la que quieras acceder rápidamente.

##### Acerca de esta tarea

El panel personalizado es un tipo de panel muy flexible. Puede contener varios widgets de distintos tipos, por ejemplo, puede colocar un widget Nuevo y un widget Orientación (texto informativo que escribe) en un único panel personalizado.

Los siguientes tipos de widgets se pueden añadir a un panel personalizado:

- **Nuevo**

  Un widget Nuevo muestra un botón **Nuevo** para un tipo de objeto. Se abre una vista de creación para el tipo de objeto.
- **Chart**

  Un gráfico se crea a partir de un tipo de objeto y uno de sus campos. Este campo debe ser una enumeración, que se puede visualizar como una lista, una serie de botones de selección o un menú desplegable. En los gráficos sólo están disponibles las enumeraciones en las que puede seleccionar un único valor. Estas enumeraciones se denominan *campos de serie enumerada de valor único*. Por ejemplo, el tipo de objeto **Riesgo** tiene un campo enumerado denominado **Impacto inherente**. Sólo puede seleccionar un valor de esta enumeración.

  Para obtener más información sobre los gráficos, consulte [Adición de un panel de gráficos](#adición-de-un-panel-de-gráfico). Para configurar colores para gráficos, póngase en contacto con el administrador.

  Puede seleccionar el tipo de gráfico (barras, anillos, barras horizontales o circular), el tipo de objeto y el campo o campos en que se basa el gráfico.
- **Recuento de filtro**

  Un widget de recuento de filtros muestra un recuento de objetos para un tipo de objeto y un filtro. Pulse el recuento para abrir una vista de cuadrícula que liste los objetos que coinciden con el filtro. Puede ver cuántos objetos existen y detallar más en el recuento.
- **Orientación**

  Un widget de orientación muestra el texto informativo que escribe. Puede aplicar formato, por ejemplo, negrita y cursiva, al texto.
- **Enlace estático**

  Un widget de enlace estático visualiza una etiqueta en la que se puede pulsar para un URL.

##### Procedimiento

1. En la pestaña Inicio, o en cualquier pestaña personalizada, haz clic en ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg).
2. Seleccione **Paneles**.
3. Pulse **Panel nuevo**.
4. Seleccione **Personalizado** en **Tipo de panel**.
5. Especifique una **Etiqueta**. La etiqueta se visualiza como un título para el panel.
6. Pulse **Nuevo widget** y seleccione un tipo de widget:

   - **Nuevo**
   - **Chart**
   - **Recuento de filtro**
   - **Orientación**
   - **Enlace estático**
7. Si elige **Nuevo**, realice los pasos siguientes:

   1. Seleccione un **Tipo de objeto**.
   2. Pulse **Terminado**.
8. Si elige **Gráfico**, realice los pasos siguientes:

   1. Especifique una **Etiqueta**.
   2. Seleccione un **Tipo de objeto**.
   3. Seleccione un **Tipo de gráfico**.

      - Barra
      - Anillo
      - Barra horizontal
      - Gráfico circular
   4. Elija un campo en **Campo de datos de gráfico**.
   5. Elija un **Tipo de método**:

      - Recuento
      - Suma
      - Promedio
      - Mín
      - Máx
   6. En el menú **Dirección de ordenación** , elija el orden de clasificación para el gráfico:

      - Seleccione **Orden de definición de campo** para visualizar los valores en el gráfico en el mismo orden en que se visualizan en el tipo de objeto.
      - Seleccione **Ascendente** para visualizar los valores en el gráfico del más bajo al más alto.
      - Seleccione **Descendente** para visualizar los valores en el gráfico desde el más alto al más bajo.
   7. Pulse **Terminado**.
9. Pulse **Terminado**.
10. Si elige **Recuento de filtros**, realice los pasos siguientes:

    1. Seleccione un **Tipo de objeto**.
    2. Opcional: Seleccione un **Filtro**. Si no se visualizan filtros, no hay filtros asociados al tipo de objeto. Póngase en contacto con el administrador para obtener ayuda.
    3. Pulse **Terminado**.
11. Si elige **Orientación**, realice los pasos siguientes:

    1. Especifique texto informativo en **Orientación**.

       Puede aplicar el siguiente formato al texto:

       - `*text*` muestra texto como cursiva.
       - `**text**` muestra el texto como negrita.
       - Un URL completo inserta un hiperenlace. Por ejemplo, `https://www.ibm.com` se muestra en una vista como un hiperenlace denominado **https://www.ibm.com**.
       - `[Link title](URL)` inserta un hiperenlace como título de enlace, donde `[Link title]` es un título de texto y `(URL)` es un URL completo. Por ejemplo, `[Click here to visit IBM](https://www.ibm.com)` se muestra en una vista como un hiperenlace denominado **Pulse aquí para visitar IBM**.

       > **Nota:** Compruebe la ubicación del texto y realice los ajustes necesarios. Es posible que tenga que añadir espacios y/o nuevas líneas para situar el texto con la alineación correcta.
    2. Pulse **Terminado**.
12. Si elige **Enlace estático**, realice los pasos siguientes:

    1. Especifique una **Etiqueta**, por ejemplo, **Vaya a IBM**. La etiqueta es un nombre que se puede pulsar en el widget.
    2. Introduzca una URL completa en **Enlace**, por ejemplo, `https://www.ibm.com`.
    3. Pulse **Terminado**.
13. Pulse **Terminado**.
14. Haz clic en la pestaña para actualizarla y comprueba que el panel se muestra correctamente. Haz clic en un panel y muévelo hasta donde quieras que se muestre en la pestaña.

#### Adición de un panel de favoritos

`Guía del usuario › Su panel de control › Añadir paneles y widgets a una pestaña` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tab-adding-favorites-panel)

Configura un panel de favoritos en la pestaña Inicio o en una pestaña personalizada para mostrar los objetos marcados como favoritos.

##### Acerca de esta tarea

La primera columna de un panel de favoritos es el nombre de objeto. La segunda columna se puede configurar, donde puede ser la descripción, la ubicación de carpeta o el tipo de objeto de un objeto. Puede definir varios paneles de favoritos, cada uno con un campo distinto definido como segunda columna.

Los objetos se ordenan por indicación de fecha y hora cuando los objetos se marcan como favoritos.

Se pueden marcar como favoritos 20 objetos como máximo.

##### Procedimiento

1. En la pestaña Inicio, o en cualquier pestaña personalizada, haz clic en ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg).
2. Seleccione **Paneles**.
3. Pulse **Panel nuevo**.
4. Seleccione **Objetos favoritos** en **Tipo de panel**.
5. Especifique una **Etiqueta**. La etiqueta se visualiza como un título para el panel.
6. En **Segunda columna** , defina qué campo se muestra en la segunda columna del panel de favoritos.

   La segunda columna puede ser:

   - Descripción
   - Carpeta
   - Tipo de objeto
7. Pulse **Terminado**.
8. Pulse **Terminado**.

   El nuevo panel aparece en la pestaña. Se listan los objetos que ya están marcados como favoritos.
9. Para marcar un objeto como favorito:

   1. Haga clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)**, amplíe una categoría, elija un tipo de objeto y abra un objeto. Por ejemplo, abra una entidad de negocios a la que tenga que acceder con frecuencia.
   2. Haz clic en ![estrella de favoritos](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/favorites_star.jpg).

      La estrella de favoritos se vuelve de color amarillo sólido.
   3. Vuelve a la pestaña.

      El objeto que ha marcado se lista en el panel de favoritos.
10. Para desmarcar un objeto como favorito, abra el objeto y haga clic en ![estrella de favoritos (activo)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/favorites_star_filled.jpg).

#### Adición de un panel de informes

`Guía del usuario › Su panel de control › Añadir paneles y widgets a una pestaña` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tab-adding-reports-panel)

Configure un panel Informes en la pestaña Inicio o en una pestaña personalizada para mostrar una lista de todos los informes por categoría o una lista alfabética de los informes que están asignados al perfil al que pertenece.

##### Acerca de esta tarea

Cuando se define un panel de informes, el campo **Origen de datos** determina la organización y el contenido del panel:

- Todos los informes

  Un panel de informes lista los informes organizados por categorías. El panel contiene informes que se encuentran en la carpeta `Reporting`. El panel contiene sólo los informes que el usuario tiene permiso para ver, ya sea por perfil o por los permisos en el propio informe.
- Informes de perfil

  Un panel de informes lista los informes alfabéticamente. La lista contiene solo informes que están asignados al perfil del usuario.

##### Procedimiento

1. En la pestaña Inicio, o en cualquier pestaña personalizada, haz clic en ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg).
2. Seleccione **Paneles**.
3. Pulse **Panel nuevo**.
4. Seleccione **Informes** en **Tipo de panel**.
5. Especifique una **Etiqueta**. La etiqueta se visualiza como un título para el panel.
6. Seleccione Todos los informes o informes de perfil en **Origen de datos**.
7. Pulse **Terminado**.
8. En el menú Orden de datos, elija cómo debe visualizarse la información del gráfico: por definición de campo, por orden ascendente o por orden descendente.
9. Haz clic en la pestaña para actualizarla y comprueba que el panel se muestra correctamente. Haz clic en un panel y muévelo hasta donde quieras que se muestre en la pestaña.

#### Adición de un panel Mis tareas

`Guía del usuario › Su panel de control › Añadir paneles y widgets a una pestaña` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tab-adding-my-tasks-panel)

Configura un panel Mis tareas en la pestaña Inicio o una pestaña personalizada para organizar las tareas que se te asignan por fecha de vencimiento, en relación con un *plazo de vencimiento próximo*.

##### Acerca de esta tarea

Defina cuántas semanas constituyen el periodo de tiempo de *vencimiento en breve*. Puede utilizar el periodo de tiempo para establecer un sentido de urgencia personalizado para este tipo de tarea. Una tarea puede clasificarse en una de estas tres categorías:

- Vencido (la fecha de vencimiento de la tarea es anterior al periodo de tiempo de vencimiento en breve)
- Vencimiento en breve (la fecha de vencimiento de la tarea está dentro del periodo de tiempo de vencimiento en breve)
- Vencimiento posterior (la fecha de vencimiento de la tarea es posterior al periodo de tiempo de vencimiento en breve)

La ventana **Tarea completada con acciones de flujo de trabajo masivo** se muestra en el panel Mis tareas si la característica está configurada y tiene elementos de flujo de trabajo que le pertenecen a usted como responsable. Aparece automáticamente y no requiere configuración en la definición del panel. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).

##### Procedimiento

1. En la pestaña Inicio, o en cualquier pestaña personalizada, haz clic en ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg).
2. Seleccione **Paneles**.
3. Pulse **Panel nuevo**.
4. Pulse **Mis tareas**en **Tipo de panel**.
5. Especifique una **Etiqueta**. La etiqueta se visualiza como un título para el panel.
6. En la definición de **'Vence pronto' (en semanas)** especifique el número de semanas que definen el periodo de tiempo de vencimiento pronto.
7. Deje los colores predeterminados tal como están o elija otros colores en **Colores de gráfico**.
8. Pulse **Terminado**.
9. Haz clic en la pestaña para actualizarla y comprueba que el panel se muestra correctamente. Haz clic en un panel y muévelo hasta donde quieras que se muestre en la pestaña.

#### Adición de un panel de tareas de suscripción

`Guía del usuario › Su panel de control › Añadir paneles y widgets a una pestaña` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tab-adding-subscription-task-panel)

Configure un panel de Tareas de suscripción en la pestaña Inicio o en una pestaña personalizada para organizar sus tareas de suscripción por fecha de vencimiento, en relación con un plazo de "vencimiento próximo".

##### Acerca de esta tarea

Defina cuántas semanas constituyen el periodo de tiempo de *vencimiento en breve*. Puede utilizar el periodo de tiempo para establecer un sentido de urgencia personalizado para este tipo de tarea. Una tarea puede clasificarse en una de estas tres categorías:

- Vencido (la fecha de vencimiento de la tarea es anterior al periodo de tiempo de vencimiento en breve)
- Vencimiento en breve (la fecha de vencimiento de la tarea está dentro del periodo de tiempo de vencimiento en breve)
- Vencimiento posterior (la fecha de vencimiento de la tarea es posterior al periodo de tiempo de vencimiento en breve)

Aparece la ventana **Tarea completa con acciones de flujo de trabajo masivo** en un panel de tareas de suscripción si la característica está configurada y tiene elementos de flujo de trabajo que le pertenecen como suscriptor. Aparece automáticamente y no requiere configuración en la definición del panel. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).

##### Procedimiento

1. En la pestaña Inicio, o en cualquier pestaña personalizada, haz clic en ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg).
2. Seleccione **Paneles**.
3. Pulse **Panel nuevo**.
4. Seleccione **Tareas suscritas** en **Tipo de panel**.
5. Especifique una **Etiqueta**. La etiqueta se visualiza como un título para el panel.
6. En la definición de **'Vence pronto' (en semanas)** especifique el número de semanas que definen el periodo de tiempo de vencimiento pronto.
7. Deje los colores predeterminados tal como están o elija otros colores en **Colores de gráfico**.
8. Pulse **Terminado**.
9. Haz clic en la pestaña para actualizarla y comprueba que el panel se muestra correctamente. Haz clic en un panel y muévelo hasta donde quieras que se muestre en la pestaña.

#### Adición de un panel de tareas de supervisión

`Guía del usuario › Su panel de control › Añadir paneles y widgets a una pestaña` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tab-adding-oversight-task-panel)

Configure un panel de Tareas de supervisión en la pestaña Inicio o en una pestaña personalizada para organizar sus tareas de supervisión por fecha de vencimiento, en relación con un *plazo próximo*.

##### Acerca de esta tarea

Defina cuántas semanas constituyen el periodo de tiempo de *vencimiento en breve*. Puede utilizar el periodo de tiempo para establecer un sentido de urgencia personalizado para este tipo de tarea. Una tarea puede clasificarse en una de estas tres categorías:

- Vencido (la fecha de vencimiento de la tarea es anterior al periodo de tiempo de vencimiento en breve)
- Vencimiento en breve (la fecha de vencimiento de la tarea está dentro del periodo de tiempo de vencimiento en breve)
- Vencimiento posterior (la fecha de vencimiento de la tarea es posterior al periodo de tiempo de vencimiento en breve)

La ventana **Tarea completada con acciones de flujo de trabajo masivo** se muestra en un panel de tareas de supervisión si la característica está configurada y tiene elementos de flujo de trabajo que le pertenecen como usuario supervisor. Aparece automáticamente y no requiere configuración en la definición del panel. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).

##### Procedimiento

1. En la pestaña Inicio, o en cualquier pestaña personalizada, haz clic en ![Configurar pestañas y paneles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_config_dashboard_icon_task_focused_ui.jpg).
2. Seleccione **Paneles**.
3. Pulse **Panel nuevo**.
4. Seleccione **Tareas de supervisión** en **Tipo de panel**.
5. Especifique una **Etiqueta**. La etiqueta se visualiza como un título para el panel.
6. En la definición de **'Vence pronto' (en semanas)** especifique el número de semanas que definen el periodo de tiempo de vencimiento pronto.
7. Deje los colores predeterminados tal como están o elija otros colores en **Colores de gráfico**.
8. Pulse **Terminado**.
9. Haz clic en la pestaña para actualizarla y comprueba que el panel se muestra correctamente. Haz clic en un panel y muévelo hasta donde quieras que se muestre en la pestaña.

## Trabajo con objetos

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-working-objects)

Puede completar el trabajo que se le ha asignado, crear objetos y editar y copiar objetos.

### Utilización de las vistas de cuadrícula para buscar, abrir y trabajar con objetos

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-using-grid-views-find-open-work)

Una vista de cuadrícula es una lista de objetos.

En una vista de cuadrícula, puede realizar las tareas siguientes:

- Filtrar la lista.
- Exportar la lista.
- Seleccionar un objeto específico para abrirlo.
- Crear, suprimir, bloquear y desbloquear objetos.
- Cambiar campos en varios objetos.
- Aplicar o eliminar etiquetas en varios objetos.

#### Acerca de esta tarea

Las vistas de cuadrícula funcionan de la misma manera en todos los tipos de objeto. Las columnas de campo varían dependiendo del tipo de objeto.

*Figura 1. Ejemplo de una lista de objetos (vista de cuadrícula)*

![Lista de objetos de riesgo que se muestran en una cuadrícula con Descripción, Estado, Clasificación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_grid_view.png)

#### Procedimiento

1. Abra una vista de cuadrícula.

   Hay varios puntos de acceso para las vistas de cuadrícula, por ejemplo:

   - Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)**. Busque el tipo de objeto con el que desea trabajar. Se abre una vista de cuadrícula.
   - Pulse un color de un gráfico de una vista de tarea o del panel de control. Se abre una vista de cuadrícula con objetos en esa parte del gráfico.
2. Realice alguna de las acciones siguientes:

   - Pulse el nombre de un objeto con el que desea trabajar para abrirlo. o pulse ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_quick_view_icon.jpg) junto al objeto que desea abrir en una vista rápida.
   - Pulsar en el recuadro de búsqueda y especificar los criterios de búsqueda.

     Para obtener más información, consulte [Búsqueda de objetos con el recuadro de búsqueda](#búsqueda-de-objetos-con-el-recuadro-buscar).
   - Pulse ![icono de filtro](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/filter_icon_task_focused_ui.jpg) para acceder a los filtros que le ayudan a encontrar rápidamente objetos con los que desea trabajar.

     Para obtener más información, consulte:

     - [Utilización de filtros de carpeta (Entidad de negocios)](#utilización-de-filtros-de-carpeta-entidad-de-negocios)
     - [Utilización de filtros privados](#utilización-de-filtros-privados)
     - [Utilización de filtros públicos](#utilización-de-filtros-públicos)
     - [Utilización de filtros ad hoc](#utilización-de-filtros-ad-hoc)

     Después de aplicar un filtro, puede especificar opcionalmente criterios de búsqueda en el recuadro de búsqueda para acotar aún más la búsqueda.

     Pulse en el nombre de filtro en la cabecera para eliminar el filtro.
   - Seleccionar o borrar el filtro que se visualiza en la parte superior de la cuadrícula, si se visualiza alguno. El nombre del filtro depende de cómo se haya configurado su sistema. Si el tipo de objeto utiliza flujos de trabajo, puede que se visualice el filtro **Sólo activos**. Desmarque **Sólo activos** para incluir los objetos de la lista que han completado un flujo de trabajo. En la lista siempre figuran los objetos que no se han sometido a un flujo de trabajo y aquellos que están en un flujo de trabajo de forma activa. Si no se visualiza **Sólo activos**, no existe ningún flujo de trabajo para el tipo de objeto.
   - Exportar todos los objetos o los objetos seleccionados a una hoja de cálculo. Para obtener información, consulte [Exportación de datos de resultados de filtro](#exportación-de-datos-de-los-resultados-filtrados).
   - Pulse **Completar tarea con acciones de flujo de trabajo masivo**, si se visualiza, para completar rápidamente los elementos de flujo de trabajo. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).
   - Seleccione todos, uno o varios objetos con la marca de selección y, a continuación, podrá suprimirlos, bloquearlos, desbloquearlos o exportarlos.
   - Seleccione todos, uno o muchos objetos con la marca de selección y pulse ![Actualización masiva](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/bulk_update_icon_tfui.jpg) para cambiar los valores de campo entre varios objetos. Para obtener más información, consulte [Aplicación de cambios a varios objetos con una actualización masiva en una vista de cuadrícula](#aplicación-de-cambios-a-varios-objetos-con-actualización-masiva-en-una-vista-de-cuadrícula).
   - Seleccione todos, uno o muchos objetos con la marca de selección y pulse ![Gestionar etiquetas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/manage_tags_icon.png) para aplicar o eliminar etiquetas en varios objetos. Para obtener más información, consulte [Adición y eliminación de etiquetas de varios objetos en una vista de cuadrícula](#adición-y-eliminación-de-etiquetas-de-varios-objetos-en-una-vista-de-cuadrícula).
   - Seleccione todos, uno o varios objetos con la marca de selección y pulse ![Icono Mover](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/move_icon_tfui.jpg) para mover los objetos a otra carpeta. Elija el destino de los objetos seleccionados y pulse **Confirmar**. Para entidades empresariales, objetos autocontenidos y objetos de modelo de seguridad, los objetos seleccionados se mueven utilizando un proceso de larga ejecución. Esto permite a un usuario reorganizar las estructuras de la entidad empresarial. No se puede deshacer un movimiento.

     Si puede mover objetos depende de los permisos y de cómo se haya configurado el sistema.

     > **Nota:** Si un movimiento implica un gran número de objetos, realice el movimiento después de horas laborables para reducir el impacto en el rendimiento del sistema.
   - Pulsar un nombre de campo de la fila de cabecera para ordenar la lista por ese campo en orden ascendente. Pulse el nombre de nuevo para aplicar el orden descendente.
   - Pulse ![Botón Nuevo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add_new_icon_task_focused_ui.jpg) para crear un objeto nuevo. La visualización del botón depende de cómo se ha configurado el sistema.
   - Elija un valor en **Elementos por página** para controlar cuantos objetos se listan en una sola página.

Si accede a un tipo de objeto que no tiene una vista de cuadrícula válida habilitada, no se visualiza ninguna vista.

### Completar el trabajo asignado

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-completing-work-that-is-assigned-you)

Puede completar una tarea que se le haya asignado.

#### Acerca de esta tarea

Las acciones que puede realizar en la tarea dependerá de cómo se haya configurado.

#### Procedimiento

1. Puede acceder a las tareas que tiene asignadas de varias maneras:

   - Desde el panel de control, puede encontrar y abrir las tareas que se le han asignado. Para obtener más información, consulte [Pestaña Inicio](#pestaña-inicio).
   - Desde la pestaña Mis tareas, puede abrir las tareas que se le han asignado. Para obtener más información, consulte [Pestaña Mis tareas](#pestaña-mis-tareas).
   - Pulse **Tarea completa con acciones de flujo de trabajo masivo** para completar los elementos de flujo de trabajo. Para obtener más información, consulte [Completar acciones de flujo de trabajo masivo en una vista de cuadrícula](#completar-acciones-de-flujo-de-trabajo-masivo-en-una-vista-de-cuadrícula).
   - Desde una notificación por correo electrónico que ha recibido, pulse un URL. El sistema abre una tarea que se le asigna. Las notificaciones de correo electrónico se pueden enviar cuando un cambio de etapa o un flujo de trabajo finaliza. Las notificaciones de correo electrónico se pueden enviar a los destinatarios y a los suscriptores de la tarea. Si recibe notificaciones por correo electrónico depende de cómo esté configurado el sistema.
   - Desde un recordatorio de correo electrónico que ha recibido, pulse un URL. El sistema abre una tarea que se le asigna. Los recordatorios de correo electrónico se pueden enviar antes, en o después de la fecha de vencimiento de una tarea. Es posible que reciba varios recordatorios. Los recordatorios de correo electrónico se pueden enviar a ambos destinatarios y suscriptores de tareas. Si y con qué frecuencia recibe los recordatorios de correo electrónico depende de cómo esté configurado el sistema.
2. Trabaje en la tarea:

   - Revise la información del objeto.
   - Complete los campos necesarios que están vacíos.

     Pase el cursor por encima de los campos para ver cuáles son editables. Cuando se visualiza el icono ![icono de edición](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_icon.jpg) junto a un campo, puede pulsar el campo para colocarlo en modo de edición. Pulse el tabulador para moverse de un campo a otro.

     > **Sugerencia:** Para poner todos los campos en modo de edición en lugar de editar un campo a la vez, pulse ![Botón Mostrar campos editables](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/reveal_editable_fields.png) en la barra de herramientas de la vista.
   - Corrija los campos necesarios y opcionales que tienen valores no válidos.
   - Revise los campos opcionales que tienen valores.
   - Si es posible, complete los campos opcionales que están vacíos.
   - Pulse ![Icono de orientación de campo incorporado](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/fieldguidance_icon_task_focused_ui.jpg) para ver la orientación del campo para todos los campos de una sección.
   - Para buscar un campo en la vista, pulse ![Botón de búsqueda (lupa)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-search-tfui.png) y, a continuación, escriba el nombre del campo.
   - Si desea imprimir la vista o guardarla en un PDF, pulse ![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/print_button.png).

   En función de cómo esté configurada la vista de tarea es posible que también pueda llevar a cabo cualquiera de las acciones siguientes:

   - Utilice la información de soporte en la orientación en línea para ayudarle a comprender lo que es necesario hacer.
   - Utilice el texto de información y la barra de progreso en la orientación de usuario para ver el estado de una tarea:

     **Tabla 1. Los colores en la barra de progreso**

     | Color | Estado | Incluye |
     | --- | --- | --- |
     | Rojo | No preparado | • Los campos necesarios están vacíos.<br>• Campos necesarios que tienen valores no válidos.<br>• Campos opcionales que tienen valores no válidos. |
     | Verde | Preparado | Campos necesarios y opcionales que están terminados y tienen valores válidos. |
     | Gris | Preparado | Campos opcionales que están vacíos. |
     | Negro | No preparado | Campos que es necesario volver a validar. Pulse **Guardar**. |

     Proporcione un valor válido para los campos que se muestran en rojo en la barra de progreso. Revise todos los campos opcionales y, si es posible, proporcione valores para los campos que se muestran en gris.

     Utilice los elementos clave que se listan en la orientación del usuario como punto de navegación para los campos importantes. Filtre la lista de elementos clave por todos los elementos clave, elementos clave que necesitan atención, o elementos clave que están incompletos. Los elementos clave que necesitan atención se incluyen en rojo en la barra de progreso.
   - Añadir o cambiar información sobre el objeto.

     Otros valores de campo pueden cambiarse automáticamente y establecerse en solo lectura. Por ejemplo, si el campo que modifica es un campo de entrada para un cálculo, el campo de salida se cambia como resultado del cálculo y se establece en sólo lectura. Para obtener más información sobre la característica GRC Calculations , consulte la publicación *IBM OpenPages Guía del administrador*.

     Un campo que es de sólo lectura no se valida cuando se modifican otros campos en una vista. Por ejemplo, si el campo A es de sólo lectura, el valor del campo A no se valida cuando modifica otros campos de la vista y guarda los cambios.

     La misma regla se aplica a los campos dependientes. Por ejemplo, supongamos que el campo A es de sólo lectura y que el campo B es editable. Además, supongamos que el valor del Campo A debe ser **Sí** si el Campo B es **No** y el Campo A debe ser **No** si el Campo B es **Sí**. Cuando el campo A es **Sí** y el usuario cambia el valor del campo B de **No** a **Sí**, pueden guardar los cambios porque el campo A es de sólo lectura. El campo A conserva el valor no válido y no se visualiza ningún mensaje de error.
   - Asociar el objeto a otro objeto. Si es necesaria la asociación, el campo de relación se lista como elemento clave.
   - Desasociar un objeto de otro objeto:

     - En un campo de relación de cuadrícula, pulse **Eliminar**.
     - En un campo de relación de tarjeta, pulse **Asociar** (la etiqueta puede ser diferente) y, a continuación, desasocie el objeto.
   - Añadir objetos. Para obtener más información, consulte [Creación de objetos desde una vista de cuadrícula](#creación-de-objetos-desde-una-vista-de-cuadrícula).
   - Suprimir objetos hijo.
   - Ver un diagrama de gráfico y detallar más los objetos subyacentes. Para obtener más información, consulte [Visualización de información en gráficos](#visualización-de-información-en-gráficos).
   - Ver diagramas de relaciones de objetos y navegar por una estructura de relaciones de objetos. Para obtener más información, consulte [Visualización de información en un diagrama de árbol](#visualización-de-la-información-en-un-diagrama-de-árbol).
   - Si una tarea forma parte de un flujo de trabajo, se visualiza el botón **Acciones**. Por ejemplo, para un objeto Problema, es posible que vea una o varias de las siguientes opciones en el botón **Acciones**:

     - **Aprobar**
     - **Denegar**
     - **Aprobar solicitud de cierre**
     - **Denegar solicitud de cierre**
     - **Solicitar cambio de fecha de vencimiento**
     - **Conceder cambio de fecha de vencimiento**

     Para un objeto Renuncia puede ver una o varias de las opciones siguientes:

     - **Enviar para revisión**
     - **Rechazar**
     - **Aprobar y cerrar**

     El hecho de que se muestre o no el botón **Acciones** depende del flujo de trabajo que controla el proceso de negocio del tipo de objeto. Las opciones del botón **Acciones** cambian a medida que el objeto avanza en el proceso de flujo de trabajo.

     La información de la tarjeta de información de flujo de trabajo es dinámica y también cambia a través del proceso de flujo de trabajo. Le ayuda a comprender en qué punto del proceso de flujo de trabajo se encuentra el objeto. Muestra la etapa actual, la fecha de vencimiento de la etapa y el asignado actual.

     Si los campos de flujo de trabajo no se actualizan automáticamente con los últimos cambios, pulse el botón Renovar en la tarjeta de información de flujo de trabajo. Los campos que se visualizan en la tarjeta de información de flujo de trabajo se renuevan. Si las pestañas del panel de control o de tareas están abiertas, la información incluida allí también se renueva.

     La información del panel de orientación del usuario, si se ha configurado, también es dinámica y puede cambiar a través del proceso de flujo de trabajo. Ofrece más información sobre el proceso de flujo de trabajo y qué debe hacer en esta fase. Pulse **Seleccionar una acción para validar** para comprobar si una acción puede pasar la validación antes de completar la acción. Para obtener más información, consulte [Validación de una acción de flujo de trabajo](#validación-de-una-acción-de-flujo-de-trabajo).
   - Añadir un comentario después de elegir una opción en el botón **Acciones**. Si puede añadir un comentario y si es obligatorio u opcional depende de cómo se configuren las opciones del botón **Acciones**. Un comentario puede tener hasta 4000 caracteres.
   - Mover un objeto hacia la siguiente fase o etapa en un ciclo de vida, si los ciclos de vida se han configurado para el tipo de objeto. Por ejemplo, para un objeto Problema, es posible que vea un botón **Acciones** con una o varias opciones.

     Los objetos configurados para utilizar ciclos de vida muestran distintas opciones en el botón **Acciones** pero no tienen una tarjeta de información de flujo de trabajo o un panel de orientación del usuario.

     Para obtener más información, consulte [Ciclos de vida configurables](#ciclos-de-vida-configurables).
   - Utilice la tecnología cognitiva IBM Watson para realizar sugerencias de taxonomía y sugerencias de asociación de objetos para padres o hijos. Para obtener más información, consulte [Creación de objetos desde una vista de cuadrícula](#creación-de-objetos-desde-una-vista-de-cuadrícula).
   - Vea información sobre los datos en una vista. Si un campo tiene un enlace a un modelo de IA, puede pulsar el enlace para ver información sobre los datos en el campo. En este ejemplo, el campo **Descripción** tiene un enlace a un modelo de IA:

     ![Se muestra un campo Descripción. También se muestra un enlace denominado View Cognitive Controls Model Insights.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/wml_description_with_link.png)
   - Si se visualiza, pulse ![Botón Watson Translator](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/translate.png) para convertir los valores de los campos de texto al idioma asociado a su entorno local. Para obtener más información, consulte [Translating values in text fields](#traducción-de-valores-en-campos-de-texto).
   - Añadir y trabajar con archivos (adjuntos). Para obtener más información, consulte [Adición y trabajo con archivos (adjuntos) en objetos](#añadir-y-trabajar-con-archivos-adjuntos-en-objetos).
   - En un campo Relación de cuadrícula, pulse ![Icono de vista rápida](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_quick_view_icon.jpg) para abrir un objeto en una vista rápida. El objeto se abre en el panel lateral. Para obtener más información sobre cómo utilizar la vista rápida, consulte [Apertura de una vista rápida](#cómo-abrir-una-vista-rápida).
3. Si está disponible, pulse la pestaña **Actividad** para ver el historial de cambios. Para obtener más información, consulte [Visualización del historial de cambios en la pestaña Actividad](#visualización-del-historial-de-cambios-en-la-pestaña-actividad).
4. Pulse ![Icono de guardar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/save_icon_task_focused_ui.jpg).

#### Resultados

Una vez finalizada una tarea, cierre la pestaña.

Si accede a un tipo de objeto que no tiene una vista de tareas válida habilitada, no se visualiza ninguna vista.

### Compartición de información clave sobre un objeto

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-sharing-key-information-about-object)

Una vista de informe muestra información de sólo lectura sobre un objeto. Se configura de forma similar a una vista de tarea. Sin embargo, mientras que una vista de tarea está diseñada para que una persona o grupo trabaje en esa actividad o tarea, una vista de informe es una compilación de la información clave sobre el objeto. Con una vista de informe, los usuarios pueden centrarse en, y resaltar, los aspectos más esenciales del objeto y comunicarse fácilmente y compartir información de GRC con otros, tanto dentro como fuera de la organización. Para compartir la información en una vista de informe, un usuario puede imprimirla o guardarla en un PDF.

Al abrir un objeto, verá pestañas como, por ejemplo, una pestaña **Tarea** . Una vista de informe aparece como una pestaña con un título determinado por el administrador. Si hay varias vistas de informe en el tipo de objeto, las vistas de informe disponibles se listan en un menú de la pestaña. La primera vista de informe de la lista se muestra de forma predeterminada. Pulse la pestaña para seleccionar la vista de informe que desea ver.

En la Figura 1, la pestaña **Análisis de riesgo por informe de entidad** muestra una vista de informe creada por el administrador. **Análisis de riesgos por informe de entidad** es la etiqueta establecida por el administrador que ha diseñado la vista.

*Figura 1. Ejemplo de una vista de informe*

![Una entidad de negocios abierta en una vista de informe.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/report_view.png)

Si desea compartir información sobre un objeto y no hay ninguna vista de informe disponible, comente lo que necesita con el administrador.

En una vista de informe, puede realizar las acciones siguientes:

- Revise la información del objeto. No puede editar el contenido de una vista de informe porque las vistas de informe son de sólo lectura.
- Pulse ![Botón de búsqueda (lupa)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-search-tfui.png) para buscar campos en la vista.
- Pulse ![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/print_button.png) para imprimir la vista o guardarla como PDF. El PDF no incluye controles de navegador y elementos de navegación, como botones, campos de búsqueda, menús, barras de desplazamiento, recuadros de selección y URL.

### Visualización de información en gráficos

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-viewing-information-in-charts)

Un diagrama de gráfico muestra una vista gráfica de los objetos relacionados basándose en un campo específico.

#### Ejemplo: Gráfico de barras horizontales

En el ejemplo siguiente, un diagrama de barras horizontal muestra documentos de trabajo por estado de revisión. Rápidamente se puede entender que la mayoría de los papeles de trabajo están terminados.

*Figura 1. Ejemplo de un gráfico de barras horizontales*

![Gráfico de barras horizontales que muestra informes de trabajo por estado de revisión](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/chart_horizontal_bar.png)

Pulse en las diferentes áreas de un gráfico para abrir una vista de cuadrícula que lista los objetos subyacentes para ese valor.

Por ejemplo, al pulsar en el área de la barra **Completado**, se abrirá una vista de cuadrícula que lista los documentos de trabajo que tienen un estado de revisión de **Completado**.

Los indicadores de la vista de cuadrícula muestran los filtros que se aplican y el número de objetos de la lista. Pulse el icono de flecha para abrir un objeto padre. Pulse **X** para eliminar un filtro y actualizar la lista en la vista de cuadrícula.

*Figura 2. Vista de cuadrícula de objetos subyacentes en un gráfico*

![Una vista de cuadrícula que muestra los objetos subyacentes para los datos en el gráfico](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/chart_horizontal_bar_grid.png)

### Visualización de la información en un diagrama de árbol

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-viewing-information-in-tree-diagram)

Un diagrama de árbol muestra un diagrama de relaciones de objetos que puede utilizar para averiguar cómo se relaciona un objeto con otros, profundizar en el diagrama y abrir los objetos relacionados.

En la imagen siguiente se muestra un diagrama de árbol de una entidad de negocios.

*Figura 1. Diagrama de árbol*

![Vista de tarea abierta a un diagrama de árbol](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_tree1_task_focused_ui.jpg)

En un diagrama de árbol, puede llevar a cabo las acciones siguientes:

- Pulsar en un círculo para expandir o contraer dicho nivel.
- Pulse el título de un círculo para abrir un objeto o lista de objetos.

  - Si pulsa en un nombre de objeto, el objeto se abre en una vista rápida. Para obtener más información, consulte [Apertura de una vista rápida](#cómo-abrir-una-vista-rápida).
  - Si pulsa en un nombre de tipo de objeto, se visualiza una lista de objetos como tarjetas. Pulse en un nombre de objeto para abrirlo en una pestaña nueva.
- Pasar el cursor sobre el título de un objeto para ver el nombre completo sin abrir dicho objeto.
- Pulse ![Icono expandir árbol](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_tree_expand_icon_task_focused_ui.jpg) para abrir el diagrama de árbol en una nueva pestaña.

En la imagen siguiente se muestra un diagrama de árbol expandido después de haber accedido a los objetos hijo.

*Figura 2. Diagrama de árbol expandido*

![Diagrama de árbol expandido](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_tree2_task_focused_ui.jpg)

### Validación de una acción de flujo de trabajo

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-validating-workflow-action)

Si una tarea forma parte de un flujo de trabajo que se ha iniciado, puede comprobar si una acción pasará la validación antes de completar la acción.

#### Acerca de esta tarea

Si una tarea forma parte de un flujo de trabajo que se ha iniciado, se visualiza **Seleccionar una acción para validar** en el panel de orientación del usuario.

Al validar una acción, el sistema le guía a través de los problemas que deben ser abordados. Puede:

- Utilizar la lista de elementos clave como punto de navegación.
- Pulsar un elemento clave para ir directamente a un campo.
- Seguir los mensajes para comprender cómo resolver problemas.

La lista de elementos clave incluye los campos necesarios y otros elementos que un administrador ha designado como elementos clave. Puede filtrar la lista de elementos clave por todos los elementos clave, elementos clave que necesitan atención, o elementos clave incompletos. Los elementos clave que necesitan atención se incluyen en rojo en la barra de progreso. Los símbolos junto a un elemento clave indican su estado. Al pulsar en un elemento de clave, el cursor se mueve al campo en modalidad de edición.

#### Procedimiento

1. Abra la tarea en la que desea trabajar.

   Si se ha configurado, el panel de orientación del usuario se visualiza en la esquina superior derecha de la vista.
2. Pulse **Seleccionar una acción para validar** y elija una acción.

   Se producen varios cambios en el panel de orientación del usuario:

   - Los símbolos junto a los elementos clave cambian basándose en la acción que elija.
   - Los mensajes pueden visualizarse en la vista de tareas bajo los cambios que tienen errores de validación.
   - Los elementos clave que son específicos para la acción se añaden a la lista de elementos clave bajo el título **Elementos clave para esta acción**.
3. Pulse los elementos clave que contengan errores o que necesiten ser corregidos. Utilice el selector para filtrar los elementos clave por todos los elementos clave, los que necesitan atención o los que están incompletos. Los elementos clave que necesitan atención se incluyen en rojo en la barra de progreso.
4. Seguir los mensajes para comprender cómo resolver problemas.

   Una vez que se hayan resuelto todos los problemas y la barra de progreso no tenga color rojo, la acción se validará.
5. Opcional: Pulse **Seleccionar una acción para validar** y validar una acción diferente. En el panel de orientación del usuario se producen cambios en función de la acción que haya elegido. Realice los mismos pasos para resolver los problemas.
6. Una vez que se hayan resuelto los problemas y la tarea esté lista para finalizar, pulse **Acciones** y seleccione la acción que ha validado.

   La acción se completa y ha finalizado el trabajo.

### Completar acciones de flujo de trabajo masivo en una vista de cuadrícula

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-completing-bulk-workflow-actions-in-grid-view)

Utilice la ventana **Completar tarea con acciones de flujo de trabajo masivo** para completar rápidamente tareas de flujo de trabajo.

#### Acerca de esta tarea

La ventana **Completar tarea con acciones de flujo de trabajo masivo** se visualiza si la característica está configurada y tiene elementos de flujo de trabajo que le pertenecen como responsable, suscriptor o usuario de supervisión. Para obtener más información sobre cómo configurar la característica **Acción de flujo de trabajo masivo** , consulte [Definición de una etapa estándar](3.3-guia-del-administrador.md#definición-de-una-etapa-estándar).

La ventana se puede visualizar en el panel de control y la pestaña Mis tareas, el panel de control y la pestaña Tareas de suscripción y el panel de control y la pestaña Tarea de supervisión. Después de pulsar una categoría, se visualiza una vista de cuadrícula para acciones de flujo de trabajo masivo.

Por ejemplo, usted es el responsable de las tareas de Riesgos, Evaluaciones de control y Problemas. Si va a un panel **Mis tareas** en el panel de control, se visualiza la ventana **Completar tarea con acciones de flujo de trabajo masivo** como en el ejemplo siguiente:

*Figura 1. Ejemplo de un panel de control Mis tareas con una ventana **Completar tareas con acciones de flujo de trabajo masivo***

![Un panel de control para Mis tareas muestra la ventana Completar tareas con acciones de flujo de trabajo masivas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_dashboard_panel_bulk_workflow_actions.jpg)

El número 3 corresponde al número de categorías (flujos de trabajo) que se le han asignado, no al número de tareas reales.

Si va a la pestaña **Mis tareas** del cuadro de mandos, aparecerá la ventana **Tareas completas con acciones de flujo de trabajo masivo**. Pulse el recuento para expandir la vista:

*Figura 2. Ejemplo de una pestaña Mis tareas con una ventana **Completar tareas con acciones de flujo de trabajo masivo***

![Una pestaña Mis tareas muestra la ventana Completar tareas con acciones de flujo de trabajo masivo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_task_tab_bulk_workflow_actions.jpg)

Desde el punto de acceso, al pulsar en una categoría, se abre una vista de cuadrícula en la que puede trabajar con tareas. En el ejemplo siguiente, ha seleccionado trabajar con tareas relacionadas con riesgos (el flujo de trabajo RCSA). El flujo de trabajo se muestra en **Nombre de flujo de trabajo** en la cabecera. La etapa se visualiza junto al nombre del flujo de trabajo. En este ejemplo, tiene 43 evaluaciones de riesgo para revisar. Seleccione una o más filas con la marca de selección. Las opciones que se muestran en la barra de herramientas son **Aprobar**, **Rechazar**y **Devolver**.

*Figura 3. Ejemplo de una vista de cuadrícula para acciones de flujo de trabajo masivo*

![Vista de cuadrícula para evaluaciones de riesgo. Se muestran los botones Aprobar, Rechazar, Devolver y Actualización masiva.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_grid_view_bulk_workflow_actions.jpg)

#### Procedimiento

1. Vaya a la pestaña **Mis tareas** o al panel de control, a la pestaña **Tareas de suscripción** o al panel de control, o a la pestaña **Tarea de supervisión** o al panel de control.
2. Expandir **Completar tarea con acciones de flujo de trabajo masivo**.
3. Elija una categoría.

   Se abre una vista de cuadrícula.
4. Opcional: Seleccione todos, uno o varios objetos con la marca de selección y pulse **Actualización masiva**. Para obtener más información, consulte [Aplicación de cambios a varios objetos con una actualización masiva en una vista de cuadrícula](#aplicación-de-cambios-a-varios-objetos-con-actualización-masiva-en-una-vista-de-cuadrícula).
5. Seleccione una o más filas con la marca de selección y elija una opción en la barra de herramientas.
6. Pulse **Confirmar**.
7. Repita los pasos hasta que haya completado las tareas.

### Cómo abrir una vista rápida

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-opening-quick-view)

Utilice una vista rápida para ver o editar un objeto seleccionado o relacionado o crear un objeto en una barra lateral pequeña sin dejar el objeto original.

#### Acerca de esta tarea

Se accede a una vista rápida desde varios lugares del sistema, por ejemplo, una vista de cuadrícula, un campo de relación de cuadrícula en una vista de tarea o un diagrama de árbol.

Si abre una vista rápida desde una vista de tarea, la vista de tarea en la que se inició pasa a ser de sólo lectura.

Toda la funcionalidad disponible en una vista de tarea también está disponible en una vista rápida con las excepciones siguientes:

- Acciones en campos de relación excepto para Nuevo (sólo hijos directos)
- Orientación del usuario
- El botón IBM Watson® Insights que da soporte a la tecnología cognitiva de IBM Watson

#### Procedimiento

1. Abra una vista de cuadrícula o una vista de tarea.

   Para obtener información sobre cómo acceder a una vista de cuadrícula, consulte [Utilización de vistas de cuadrícula para buscar, abrir y trabajar con objetos](#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos).

   Para obtener información sobre cómo acceder a una vista de tarea, consulte [Completar el trabajo que tiene asignado](#completar-el-trabajo-asignado).
2. Pulse ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_quick_view_icon.jpg) junto al objeto que desea abrir.

   El objeto se abre en la vista rápida.
3. En un diagrama de árbol, pulse en un círculo de título donde solo hay un objeto a ese nivel.

   El objeto se abre en una vista rápida.
4. En una vista rápida, puede:

   - Ver un objeto.
   - Editar un objeto, ya sea campo por campo o en modalidad de edición.
   - Pulse ![Botón de búsqueda (lupa)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-search-tfui.png) para buscar campos en la vista rápida.
   - Marcar un objeto como favorito.
   - Iniciar una acción de flujo de trabajo
   - Crear un nuevo objeto hijo del objeto que está abierto.
   - Si se visualiza un diagrama de árbol, acceder a otros objetos inferiores.
   - Pulse ![Icono Expandir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_expand_quick_view_icon.jpg) para expandir la vista rápida para abrir el objeto en una nueva pestaña. El objeto se abre en la vista de tarea de ese tipo de objeto. La funcionalidad completa está disponible.
5. Cierre la vista rápida.

### Aplicación de cambios a varios objetos con actualización masiva en una vista de cuadrícula

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wo-applying-changes-multiple-objects-bulk-update-in-grid-view)

Los administradores pueden editar información de varios objetos utilizando la función de actualización masiva.

#### Antes de empezar

Debe tener el permiso Bulk Update All Fields para acceder a la función de actualización masiva.

#### Acerca de esta tarea

- Identifique los valores de campo que se van a cambiar y los objetos que se van a actualizar. Los campos que identifica está actualizados en todos los objetos que selecciona.
- También puede dejar los campos sin cambiar o borrar los valores de un campo.
- La configuración de administración puede impedir que se actualice un objeto.
- Todos los objetos que no generan errores se actualizan.
- Las dependencias de campo, bloqueos y permisos pueden impedir que se modifiquen objetos seleccionados. Los objetos que puede modificar se guardan con los cambios, mientras que los otros no se cambian.
- No puede borrar los campos obligatorios.

Los administradores configuran los campos que están disponibles en la actualización masiva. En función de cómo esté configurada la vista, es posible que se visualicen más campos en edición masiva que los que se visualizan en la vista de cuadrícula.

Los campos de sólo lectura, por ejemplo, los campos calculados, los campos de flujo de trabajo y los campos del sistema que se leen sólo no están disponibles para la selección en la actualización masiva.

Cambiar el valor de una lista de selección que es el controlador de otras listas de selección puede invalidar los valores de las listas de selección dependientes. Por lo tanto, si utiliza la actualización masiva para cambiar un controlador o una lista de selección dependiente, todas las demás listas de selección que están implicadas en la dependencia se añaden automáticamente como campos de la actualización masiva. Actualice los valores de campo basándose en la lista de nuevas opciones.

#### Procedimiento

1. Abra una vista de cuadrícula.

   Para obtener más información, consulte [Utilización de vistas de cuadrícula para buscar, abrir y trabajar con objetos](#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos).
2. Seleccione todos, uno o varios objetos con la marca de selección y pulse **Actualización masiva**.

   Se abre el panel lateral de actualización masiva. Se visualiza el número de objetos que hay seleccionados.
3. En **Seleccionar campos para actualizar de forma masiva**, elija los campos que desea cambiar. Escriba letras para buscar campos.
4. Indique los cambios:

   - Introduzca nuevos valores en los campos.
   - Pulse **Borrar valores** para borrar los valores de un campo.

     Si un campo es obligatorio, no se pueden borrar sus valores.
5. Revise la lista de cambios que se van a aplicar. Si aparece algún campo en la lista que no se debe actualizar, pulse en el icono Eliminar para eliminarlo de la actualización masiva.
6. Pulse **Actualizar**.
7. Se visualiza un resumen de las actualizaciones propuestas. Revise los cambios y pulse **Confirmar**.

#### Qué hacer a continuación

Se actualizan los objetos. Si permanece en la ventana de confirmación durante el proceso, se visualiza la ventana Informe de actualización masiva cuando finaliza el proceso. Muestra el número de actualizaciones de objetos que se han realizado correctamente y las que han fallado. Además, en las actualizaciones de objetos que han fallado se indica un motivo. Si cierra la ventana de confirmación durante el procesamiento, puede revisar los resultados de la actualización masiva en Notificaciones o en el correo electrónico que recibirá.

### Adición y eliminación de etiquetas de varios objetos en una vista de cuadrícula

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wo-adding-removing-tags-from-multiple-objects-in-grid-view)

Puede editar las etiquetas para varios objetos utilizando el botón **Gestionar etiquetas** en la vista de cuadrícula.

#### Antes de empezar

Puede añadir y eliminar etiquetas de un objeto sólo bajo las condiciones siguientes:

- El tipo de objeto tiene habilitado el etiquetado.
- El objeto debe estar desbloqueado.
- Debe tener acceso de escritura al objeto.
- Debe estar en el periodo de elaboración de informes actual.
- Al añadir etiquetas, el número de etiquetas debe ser menor que el máximo de 25 etiquetas por objeto.

- El tipo de objeto tiene habilitado el etiquetado.
- El objeto debe estar desbloqueado.
- Debe tener acceso de escritura al objeto.
- Debe estar en el periodo de elaboración de informes actual.
- Al añadir etiquetas, el número de etiquetas debe ser menor que el máximo de 25 etiquetas por objeto.

Debido a que está editando varios objetos, es posible que algunos objetos cumplan estas condiciones, mientras que otros no. Los objetos que no cumplen las condiciones no se cambian. Por ejemplo, si selecciona dos objetos y uno ya tiene 25 etiquetas, no se añaden etiquetas a ese objeto, sino que se añaden al otro objeto. Si un objeto es de sólo lectura debido a las reglas de seguridad, los cambios de etiqueta no se aplican a ese objeto, pero se aplican a los otros objetos. Si se producen anomalías, se visualiza un informe para explicar las anomalías.

Para obtener más información sobre las etiquetas, consulte [Etiquetas](#etiquetas).

#### Procedimiento

1. Abra una vista de cuadrícula.

   Para obtener más información, consulte [Utilización de vistas de cuadrícula para buscar, abrir y trabajar con objetos](#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos).
2. Seleccione todos, uno o varios objetos con la marca de selección y pulse **Gestionar etiquetas**.

   Se abre el panel **Gestionar etiquetas** . Se visualiza el número de objetos que hay seleccionados.
3. Para añadir etiquetas:

   1. En el recuadro desplegable **Seleccionar etiquetas para añadir** , puede escribir caracteres para buscar etiquetas o puede pulsar la flecha para visualizar una lista de etiquetas.
   2. Seleccione las etiquetas que desea añadir.
4. Para eliminar etiquetas:

   1. En el recuadro desplegable **Seleccionar etiquetas para eliminar** , puede escribir caracteres para buscar etiquetas o puede pulsar la flecha para visualizar una lista de etiquetas.
   2. Seleccione las etiquetas que desea eliminar.
5. Pulse **Guardar**.

#### Resultados

En la vista de cuadrícula, puede ver los cambios que ha realizado en las etiquetas para los objetos seleccionados en la columna **Etiquetas** .

### Visualización del historial de cambios en la pestaña Actividad

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-viewing-change-history-activity-tab)

Utilice la pestaña **Actividad** de una tarea para ver los cambios realizados en un objeto.

Si es miembro del grupo de administradores de OpenPages® , puede ver todas las actividades en todos los campos. Si no es así, sólo puede ver actividades para los campos que están en la vista y a los que tiene acceso en función de su perfil.

#### Acerca de esta tarea

No puede editar los detalles en la pestaña **Actividad** . El historial de cambios se visualiza para el periodo de elaboración de informes seleccionado. Para obtener más información, consulte [Modificación del periodo de elaboración de informes](#cambio-del-periodo-de-elaboración-de-informes).

#### Procedimiento

1. Abra una tarea.

   Para obtener más información, consulte [Completar el trabajo que se le ha asignado](#completar-el-trabajo-asignado).
2. Pulse la pestaña **Actividad** .

   Se muestran los detalles sobre los cambios que se han realizado en el objeto.
3. Compare los valores en las columnas **Valor antiguo** y **Valor nuevo** .
4. Opcional: Pulse ![Botón de filtrado](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/filter_button.png) para ver los detalles del historial de cambios basándose en los criterios siguientes:

   - **Campo** : muestra los cambios en los valores de campo
   - **Relación** : muestra los cambios en las asociaciones de objetos
   - **Flujo de trabajo** : muestra los cambios en las etapas y estados del flujo de trabajo
   - **Usuarios** : las personas que han realizado los cambios
   - **Fecha de inicio** y **Hora de inicio** : la fecha y hora de inicio del intervalo de tiempo en el que se han realizado los cambios
   - **Fecha de finalización** y **Hora de finalización** : la fecha y hora de finalización del intervalo de tiempo en el que se han realizado los cambios

     > **Nota:** Cuando defina una fecha y una hora, verifique el huso horario, ya que puede ser diferente del huso horario del servidor de OpenPages .
5. Para exportar los datos a Microsoft Excel, pulse ![botón Exportar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/export_button.png).

   El archivo se descarga automáticamente.

   > **Atención:** No puede utilizar FastMap para importar datos que se han exportado desde la pestaña **Actividad** .

### Exportación de datos de los resultados filtrados

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-exporting-data-from-filter-results)

Puede exportar datos a una hoja de cálculo (formato`.xlsx` ) desde una vista de cuadrícula. Todos los objetos que coinciden con los criterios de filtro, si se aplican, se exportan.

#### Acerca de esta tarea

Puede adaptar los campos y los objetos que se exportan en función de lo que quiera hacer con los datos.

Su administrador establece el número máximo de elementos que puede exportar. Si supera este límite, debe reducir el número de elementos en los resultados del filtro o seleccionar menos niveles de tipos de objeto para exportar.

Los campos de texto grandes (campos de serie larga grandes) no se exportan porque estos campos pueden ser demasiado grandes para almacenarse en una celda (el almacenamiento máximo para una celda es de 32 KB).

#### Procedimiento

1. Abra una vista de cuadrícula.

   Puede acceder a una vista de cuadrícula desde varias partes de la aplicación. Los pasos siguientes son ejemplos de cómo puede acceder a una vista de cuadrícula.

   - Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)**. Pulse el tipo de objeto con el que desea trabajar. Se abre una vista de cuadrícula.
   - Pulse un color de un gráfico de una vista de tarea o del panel de control. Se abre una vista de cuadrícula con objetos en esa parte del gráfico.
2. Seleccione los filtros que necesite.
3. Puede seleccionar los objetos que desea exportar o puede exportar todos los objetos en una hoja de cálculo.

   - Seleccione los recuadros de selección para los objetos que desea exportar y, a continuación, pulse ![botón Exportar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_export_icon.JPG).
   - Para exportar todos los objetos, pulse ![botón Exportar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_export_icon.JPG).
4. En el recuadro de diálogo **Exportar** , seleccione **FastMap** o **Vista de cuadrícula**.

   - Si selecciona **FastMap**, se exportan los campos especificados por su Administrador.
   - Si selecciona **Vista de cuadrícula**, se exportarán los campos visibles en la vista de cuadrícula actual.

     > **Nota:** Si elige **Vista de cuadrícula**, no puede importarla con **FastMap**.
5. Si ha seleccionado **FastMap**, seleccione los tipos de objeto que desea exportar.

   El perfil determina los tipos de objeto que se visualizan. El administrador configura el número de niveles en la vía de acceso de tipo de objeto.

   Por ejemplo, si está exportando Políticas, es posible que vea también la opción de exportar Procedimientos.

   ![Exportar FastMap seleccionado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/export_fastmap.png)
6. Pulse **Exportar**. Se crea un archivo de Microsoft Excel en formato FastMap o en formato de vista de cuadrícula. Se muestra un enlace en la bandeja.

   Se exportan todos los campos que están disponibles para su perfil.

   FastMap tiene una función de importación, que el administrador puede configurar automáticamente. Puede editar los datos en el libro de trabajo y, a continuación, importarlos con FastMap.

   Para obtener más información, consulte [Utilización de FastMap](3.5-guia-del-administrador.md#importación-de-datos-de-objetos-a-openpages-con-fastmap).

### Imprimir una vista en PDF

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-printing-view-pdf)

Puede imprimir una vista en PDF.

#### Acerca de esta tarea

Al seleccionar **Imprimir** ![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/print_button.png), puede imprimir una vista, guardarla y compartirla como un archivo PDF. El archivo es fácil de leer y no muestra los controles del navegador ni los elementos de navegación, como botones, campos de búsqueda, menús, barras de desplazamiento, recuadros de selección y URL.

> **Nota:** Para la pestaña Actividad, exporte los datos a Microsoft Excel y, a continuación, imprima el archivo de Microsoft Excel.

#### Procedimiento

1. Abra la vista Tarea, Admin o Informe que desea imprimir.
2. Pulse ![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/print_button.png).
3. Opcional: Especifique el **Título de impresión**. Este es el título que aparecerá en su archivo de impresión o PDF.
4. Ajuste los valores según sea necesario. Asegúrese de que **Scale** esté establecido en **Default**.

   El cambio de **Escala** puede provocar problemas de diseño en el PDF.
5. Haga clic en **Imprimir**.

   Si tiene OpenPages® establecido en una modalidad oscura, la salida impresa o el archivo toma de forma predeterminada un tema claro.

### Edición de objetos en una vista de tarea

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-editing-in-task-view)

Puede editar campos para un único objeto desde una vista de tarea.

#### Antes de empezar

Tenga en cuenta la siguiente información antes de editar un objeto en una vista de tarea.

- No puede editar los siguientes campos de objeto: Carpeta, Fecha de creación, Creado por, Fecha de la última modificación, Modificado por última vez por.
- Elimine todos los bloqueos de firma, incluidos los bloqueos heredados, antes de editar un objeto.
- Si usted y otro usuario editan simultáneamente el mismo objeto, o si otro usuario cambia el objeto después de recuperarlo, un mensaje de error le notifica de un conflicto.
- No edite la misma instancia de objeto simultáneamente en dos pestañas o ventanas de navegador separadas. De hacerlo, podrían aparecer resultados inesperados.
- Puede editar un elemento asociado a un objeto de la página de objetos.

#### Procedimiento

1. Acceda al objeto que desea editar. Abra el objeto en una vista de tarea. Para obtener más información, consulte [Completar el trabajo que se le ha asignado](#completar-el-trabajo-asignado).
2. Pase el encima de los campos para ver cuáles son editables. Cuando se visualiza el icono ![icono de edición](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_icon.jpg) junto a un campo, puede pulsar el campo para colocarlo en modo de edición.

   Si desea encontrar un campo determinado, pulse ![Botón de búsqueda (lupa)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-search-tfui.png) en la barra de herramientas de la vista y especifique el nombre del campo que está buscando.

   Si desea poner todos los campos en modalidad de edición en lugar de editar un campo a la vez, pulse ![Botón Mostrar campos editables](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/reveal_editable_fields.png) en la barra de herramientas de la vista.
3. Realice el cambio.
4. Edite otros campos.
5. Pulse **Guardar**.

#### Resultados

Si desea imprimir la vista o guardarla en un PDF, pulse ![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/print_button.png).

### Comentar objetos

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-commenting)

Puedes añadir comentarios a los objetos si tu administrador te ha dado permiso y ha configurado ' OpenPages® ' para permitir comentarios en los objetos. Por ejemplo, puede añadir un comentario a un asunto para hacer una pregunta, una observación o dejar constancia de sus pensamientos sobre el asunto.

En la ficha Tarea o Admin de un objeto, haga clic en **Comentarios** ' ![Ver comentarios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add-comment.svg) para mostrar el panel **Comentarios**.

Cuando añades un comentario sobre un objeto, puedes mencionar a otros usuarios que puedan estar interesados en él. Se envía un correo electrónico con un enlace y una vista previa de tu comentario a todos los usuarios que has añadido al comentario.

Puedes editar o eliminar los comentarios que hayas añadido. El texto **Editado** se muestra en los comentarios que han sido editados por el autor. El texto **Comentario eliminado por \<nombredeusuario>** se muestra en los comentarios que se han eliminado.

#### Añada sus comentarios

Puedes añadir tus comentarios a los objetos si tu administrador te ha dado permiso para ello.

##### Procedimiento

1. Haga clic en " **Menú principal " ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** " y seleccione el tipo de objeto que desea comentar.
2. Seleccione el objeto que desea comentar.
3. En la pestaña **Tarea** o **Admin**, haga clic en **Comentarios** ' ![Ver comentarios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add-comment.svg).
4. Introduzca su comentario en el cuadro de texto.
5. Opcional: Para enviar tu comentario en un correo electrónico a otro usuario, haz clic en **Añadir usuario** ' ![Botón Añadir usuario](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add-user.svg) e introduce el nombre de usuario del usuario, o selecciona el nombre de usuario de la lista de nombres usados recientemente.
6. Haga clic en **Comentario**.

##### Resultados

El comentario aparece con tu nombre de usuario.

#### Editar sus comentarios

Puede editar los comentarios que haya añadido a los objetos.

##### Procedimiento

1. Haga clic en " **Menú principal " ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** " y seleccione el tipo de objeto.
2. Seleccione el objeto para el que desea editar el comentario.
3. En la pestaña **Tarea** o **Admin**, haga clic en **Comentarios** ' ![Ver comentarios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add-comment.svg).
4. Seleccione **Editar** para editar el comentario. Sobrescribir el comentario en el cuadro de texto.
5. Opcional: Para enviar tu comentario en un correo electrónico a otro usuario, haz clic en **Añadir usuarios para enviar este comentario a** ' ![Botón Añadir usuario](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add-user.svg) e introduce el nombre de usuario del usuario, o selecciona el nombre de usuario de la lista de nombres usados recientemente.

   Los correos electrónicos no se reenvían a los usuarios que ya están en la lista.
6. Pulse **Guardar**.

##### Resultados

El texto **Editado** aparece en el comentario que ha editado.

#### Borrar tus comentarios

Puede eliminar los comentarios que haya añadido a los objetos.

##### Procedimiento

1. Haga clic en " **Menú principal " ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** " y seleccione el tipo de objeto.
2. Seleccione el objeto del que desea eliminar el comentario.
3. En la pestaña **Tarea** o **Admin**, haga clic en **Comentarios** ' ![Ver comentarios](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add-comment.svg).
4. En el comentario que desea editar, haga clic en ![Más](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/overflow-menu--vertical.svg) y seleccione **Eliminar** para borrar el comentario.

##### Resultados

El comentario se sustituye por el texto **Comentario borrado por \<nombredeusuario>**.

### Copia de objetos

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-copying)

Si está configurado, puede copiar un objeto existente para crear rápidamente un objeto con valores similares.

#### Acerca de esta tarea

Si puede copiar objetos depende de sus permisos y de cómo se haya configurado el sistema.

Si se ha configurado una copia para un tipo de objeto, hay un botón de copia disponible en una vista de tarea. Se puede visualizar en un campo de relación de tarjeta o cuadrícula.

La funcionalidad de la función de copia, incluido cómo se denominan los objetos hijo y cómo se resuelven los conflictos, depende de cómo se defina la acción de copia recursiva en el campo de relación de tarjeta o cuadrícula.

Para obtener más información, consulte [Adición de una acción Copiar recurrente](3.6-guia-del-administrador.md#adición-de-una-acción-copia-recurrente).

#### Procedimiento

1. Acceda al objeto que desea editar. Abra el objeto en una vista de tarea. Para obtener información, consulte [Completar el trabajo que se le ha asignado](#completar-el-trabajo-asignado).
2. Recorra la vista de tarea y localice el botón Copiar.
3. Pulse **Copiar** (el botón puede tener un nombre diferente).
4. Finalice su tarea.
5. Pulse **Copiar**.

   Se crea una instancia duplicada del objeto o de los objetos hijo.

   > **Atención:**

   > - No puede copiar una entidad de negocios en sí misma.
   > - Si el número de objetos seleccionados para la copia es mayor que un valor específico, las copias se crearán en segundo plano como proceso de larga ejecución.

   >   Vaya a procesos en segundo plano para revisar el estado de los procesos de larga ejecución.

   >   Recibirá un correo electrónico cuando las copias estén finalizadas. El correo electrónico contiene enlaces a un informe de proceso y a la vista de tareas del objeto.

   >   El administrador puede cambiar el número predeterminado de copias para los procesos de larga ejecución.

### Supresión de objetos

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-deleting)

Si está configurado, puede suprimir un objeto del periodo de elaboración de informes actual.

#### Acerca de esta tarea

La posibilidad de suprimir objetos depende de sus permisos y de cómo se ha configurado su sistema.

Un objeto debe estar desbloqueado antes de ser suprimido. Después de suprimir un objeto, éste no se puede recuperar. Sin embargo, si el objeto suprimido estaba incluido en un periodo de creación de informes anterior, puede ver detalles asociados a ese objeto a través de los informes. Las carpetas generadas por el sistema no se pueden suprimir. Tenga en cuenta la siguiente información antes de suprimir un objeto:

- Cuando suprime un objeto padre, los objetos hijo, problemas asociados o elementos de acción también se suprimen.
- Cuando suprime una entidad de negocios, los objetos hijo, objetos asociados o subentidades que están en la misma carpeta, incluidos documentos adjuntos externos, se suprimen.
- Si suprime un objeto de control, las pruebas asociadas y los documentos adjuntos externos también se suprimen.
- Asegúrese de que toda la información importante contenida en una prueba asociada se protege antes de suprimir un control.
- Puede suprimir sólo los objetos de una carpeta y no la carpeta. Si tiene permiso para suprimir una carpeta, se suprime todo el contenido. En un archivo, se suprimen todas las versiones.
- Si la característica Incorporar/Reservar está configurada, el archivo debe incorporarse para poder suprimirlo.

#### Procedimiento

1. En el menú principal, seleccione el tipo de objeto.
2. En la vista de cuadrícula, utilice la marca de selección para seleccionar cada objeto que desee suprimir.
3. Pulse ![icono de papelera](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/delete_icon.jpg).
4. Haga clic en **Suprimir** para verificar la supresión.

### Renombrar un objeto desde una vista de tarea

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-renaming-object-from-task-view)

Puede renombrar objetos desde una vista de tarea.

#### Acerca de esta tarea

El hecho de que se le permita cambiar el nombre de los objetos depende de los permisos y de cómo se haya configurado el sistema. Esto sólo se aplica a objetos autocontenidos. Sólo puede cambiar el nombre de los objetos de una carpeta, no de la carpeta.

Los objetos que residen en la misma carpeta deben tener un nombre exclusivo. Cuando cambia el nombre de una carpeta, su contenido (asociaciones primarias) también se moverá a la carpeta a la que se ha cambiado el nombre. Si la característica Incorporar/Reservar está habilitada, sólo puede cambiar el nombre del archivo que se haya incorporado. No se puede cambiar el nombre de las carpetas generadas por el sistema.

#### Procedimiento

1. Acceda al objeto que desea editar. Abra el objeto en una vista de tarea. Para obtener información, consulte [Completar el trabajo que se le ha asignado](#completar-el-trabajo-asignado).
2. Pulse ![icono de edición](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_icon.jpg) junto a **Nombre**.
3. Pulse **Guardar**.

### Cierre de sesión

`Guía del usuario › Trabajo con objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-logging-out)

Puede finalizar una sesión y salir de la aplicación.

#### Acerca de esta tarea

Es una práctica recomendada cerrar la sesión en lugar de cerrar simplemente la ventana del navegador.

OpenPages® excede automáticamente el tiempo de espera y se cierra después de un periodo de inactividad del sistema.

Si intenta realizar una operación después de que OpenPages haya excedido el tiempo de espera, el sistema se mueve automáticamente a la página Iniciar sesión en la que puede volver a iniciar la sesión.

#### Procedimiento

1. Pulse ![Icono de menú de usuario (persona)](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_menu_icon_task_focused_ui.jpg) para abrir el menú Usuario.
2. Pulse **Cerrar sesión**.

## Creación y asociación de objetos

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-creating-associating-objects)

Puede crear instancias de objeto y crear asociaciones entre objetos, o entre objetos y archivos adjuntos.

### Creación de instancias de objeto

`Guía del usuario › Creación y asociación de objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-creating-object-instances)

En IBM OpenPages®, puede crear instancias de objeto desde varios puntos de ejecución.

La posibilidad de crear instancias de objetos y el modo de hacerlo depende de cómo esté configurado el sistema y de los permisos que haya otorgado el administrador.

Hay varios posibles puntos de lanzamiento:

- Desde una vista de cuadrícula.

  Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **[tipo de objeto]**. Se visualiza una vista de cuadrícula para ese tipo de objeto. Pulse ![Icono Añadir nuevo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add_new_icon_task_focused_ui.jpg).
- Desde un panel de pestañas configurado para añadir nuevos objetos.

  Pulse ![Acceso directo de la página de inicio](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_home_page.jpg). Se visualiza el panel de control. Busca en las pestañas un panel que te permita crear objetos. El panel contendrá un botón con una etiqueta como Nuevo control o Nuevo riesgo.

  Si no tiene un panel de este tipo, es posible que pueda crear uno, en función de sus permisos. Para obtener más información, consulte [Adición de un panel personalizado](#adición-de-un-panel-personalizado).
- Desde una vista de tarea que le permite crear objetos hijo.

  En función del tipo de objeto, una vista de tarea puede mostrar botones en los que puede crear objetos hijo. Acceda a una vista de tarea trabajando en una tarea que se le asigne o abriendo un objeto desde una vista de cuadrícula. En este caso, el padre primario se establece en el objeto de la tarea en la que estaba trabajando.
- Desde una vista de tarea que le permite copiar objetos hijo.

  Acceda a una vista de tarea trabajando en una tarea que se le asigne o abriendo un objeto desde una vista de cuadrícula. En función del tipo de objeto, es posible que una vista de tarea muestre un botón Copiar. Puede hacer una copia de un objeto hijo y, a continuación, editar el nuevo objeto para que cumpla los requisitos.

  Para obtener más información, consulte [Copia de objetos](#copia-de-objetos).

El siguiente ejemplo muestra la pantalla, denominada Vista de creación, que se muestra al hacer clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Evaluaciones** > **Controles** y, a continuación, hacer clic en ![Icono Añadir nuevo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add_new_icon_task_focused_ui.jpg).

*Figura 1. Ejemplo de creación de un objeto de control*

![crear un nuevo objeto de riesgo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_creation_view_task_focused_ui.jpg)

El proceso de creación de una instancia de objeto tiene las características siguientes:

- El botón ![Icono Añadir nuevo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add_new_icon_task_focused_ui.jpg) y la etiqueta **Nuevo [tipo de objeto]** pueden tener diferentes nombres, en función de la configuración.
- Si el administrador habilita el valor de denominación automática para un tipo de objeto, se asigna automáticamente un nombre a la instancia de objeto nueva.
- Al crear un objeto hijo, en función del punto de acceso, es posible que tenga que seleccionar el objeto padre o que se pueda establecer para usted.

  Busque los botones **Establecer padre primario** y **Añadir** en la sección **Padre** de la pestaña **Administración** correspondiente al objeto.
- Al crear un objeto padre, es posible que pueda seleccionar objetos hijo para enlazar con la nueva instancia de objeto.

  Busque los botones **Nuevo** o **Añadir** en la pestaña **Admin** para el objeto.
- Los botones **Nuevo**, **Establecer padre primario** y **Añadir** pueden denominarse de forma diferente, en función de la configuración.
- Es posible que pueda añadir archivos adjuntos.

  Busque los botones **Añadir** y **Nuevo/Actualizar**.
- No se puede guardar una nueva instancia de objeto hasta que se hayan completado todos los campos necesarios.
- Si el texto *Añadir una descripción mejora IBM Watson® Sugerencias* se muestra debajo de un campo, se ha implementado la tecnología cognitiva IBM Watson . Puede ayudarle proporcionando sugerencias de taxonomía y/o sugerencias de asociación de objetos. Para obtener más información, consulte [Servicios de proceso de lenguaje natural](#servicios-de-procesamiento-de-lenguaje-natural).
- Utilice la información de soporte en la orientación en línea para ayudarle a comprender lo que es necesario hacer.
- Utilice el texto de información y la barra de progreso en la orientación de usuario para ver el estado de una tarea:

  **Tabla 1. Los colores en la barra de progreso**

  | Color | Estado | Incluye |
  | --- | --- | --- |
  | Rojo | No preparado | • Los campos necesarios están vacíos.<br>• Campos necesarios que tienen valores no válidos.<br>• Campos opcionales que tienen valores no válidos. |
  | Verde | Preparado | Campos necesarios y opcionales que están terminados y tienen valores válidos. |
  | Gris | Preparado | Campos opcionales que están vacíos. |
  | Negro | No preparado | Campos que es necesario volver a validar. Pulse **Guardar**. |

  Proporcione un valor válido para los campos que se muestran en rojo en la barra de progreso. Revise todos los campos opcionales y, si es posible, proporcione valores para los campos que se muestran en gris.

  Utilice los elementos clave que se listan en la orientación del usuario como punto de navegación para los campos importantes. Filtre la lista de elementos clave por todos los elementos clave, elementos clave que necesitan atención, o elementos clave que están incompletos. Los elementos clave que necesitan atención se incluyen en rojo en la barra de progreso.
- Utilice la información de soporte en la orientación en línea para ayudarle a comprender lo que es necesario hacer.

### Reglas para la denominación de objetos

`Guía del usuario › Creación y asociación de objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-rules-naming)

Utilice las siguientes convenciones para poner nombre a los objetos:

- La longitud máxima de un nombre de objeto es de 252 caracteres.
- Sólo se permiten espacios únicos.
- Si está habilitada la denominación automática, el nombre del objeto se crea automáticamente.
- Sólo se permiten los siguientes caracteres especiales:

  ```
  ~@^()_+`[]{};',.!#%&*,'<>:"|?
  ```

  La barra inclinada `/` y la barra inclinada invertida `\` no están permitidas.
- El nombre debe ser exclusivo dentro de una carpeta.

Si el campo Título está habilitado para un tipo de objeto, utilice los convenios siguientes:

- El objeto **ID** debe cumplir los requisitos para los nombres de objeto.
- La longitud máxima de un objeto **Título** es de 4.000 caracteres.

### Creación de objetos desde una vista de cuadrícula

`Guía del usuario › Creación y asociación de objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-creating-from-grid-view)

Puede crear objetos, por ejemplo, Riesgos, Evaluaciones de riesgos, Controles y Procesos.

#### Acerca de esta tarea

Puede crear objetos pulsando ![Nuevo icono](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add_new_icon_task_focused_ui.jpg) desde una vista de cuadrícula.

Desde este punto de acceso, el objeto padre no se conoce. La vista contiene un campo de relación que permite seleccionar un objeto padre.

#### Procedimiento

1. Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)**.
2. Pulse el tipo de objeto.

   Se abre la vista de cuadrícula.
3. Pulse ![Botón Nuevo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/add_new_icon_task_focused_ui.jpg). Si está creando un objeto trabajando en una tarea que se le ha asignado, empiece aquí.
4. Escriba o revise el nombre del objeto.

   Si la denominación automática no está habilitada, debe especificar un nombre.

   Si se ha habilitado la denominación automática, el nombre se habrá especificado de forma automática y puede que sea de solo lectura, dependiendo de la configuración.
5. Complete los campos obligatorios.
6. Complete los campos opcionales, según sea necesario. Utilice la información de soporte de la orientación de campo, la orientación en línea y la orientación del usuario, si está configurada.
7. A medida que se completan los campos, otros valores de los campos pueden establecerse automáticamente como valores y ser de solo lectura. Esto ocurre si el campo que ha rellenado es un campo de entrada para un cálculo. Para obtener más información sobre la característica GRC Calculations , consulte la publicación *IBM OpenPages Guía del administrador*
8. Proporcione las asociaciones de objetos padre e hijo según sea necesario. Para la mayoría de los tipos de objeto necesitará un objeto padre primario. Las etiquetas dependen del tipo de objeto que está creando. Por ejemplo, cuando crea un problema, es posible que los botones estén etiquetados como **Seleccionar entidad empresarial afectada**, **Seleccionar control afectado** y **Seleccionar política afectada**. Al crear un nuevo control, el botón puede ser etiquetado como **Seleccionar riesgo**. Para obtener más información sobre cómo realizar asociaciones, consulte [Asociaciones entre objetos](#asociaciones-entre-objetos).
9. Si el texto *Añadir una descripción mejora IBM Watson® Sugerencias* se muestra debajo de un campo, se ha implementado la tecnología cognitiva IBM Watson . Puede ayudarle proporcionando sugerencias de taxonomía y/o sugerencias de asociación de objetos. Para obtener más información, consulte [Servicios de proceso de lenguaje natural](#servicios-de-procesamiento-de-lenguaje-natural).

   1. Pulse el botón IBM Watson Insights. La etiqueta de botón se muestra brevemente como IBM Watson Insights y, a continuación, cambia a la etiqueta de campo de clasificador o a la etiqueta de acción. El botón sólo se muestra si Watson puede hacer sugerencias dado el valor introducido en el campo señalado por el texto *Añadir una descripción mejora Sugerencias de IBM Watson*.

      Se muestra una lista de sugerencias en el panel IBM Watson Insights junto con puntuaciones de confianza.

      - Si la tecnología cognitiva se ha configurado para realizar sugerencias de taxonomía, se muestra una lista de clasificaciones sugeridas.
      - Si la tecnología cognitiva se ha configurado para realizar sugerencias de asociación de objetos, se muestra una lista de objetos sugeridos.
   2. Realizar una selección.

      - Si se ha configurado la tecnología cognitiva para realizar sugerencias de taxonomía, el sistema llena hasta tres campos de objetivo de clasificador, por ejemplo, los campos Categoría de riesgo, Subcategoría de riesgo y Ejemplo de riesgo. Puede rellenar manualmente los campos de destino de clasificador si se han incluido en la vista.
      - Si la tecnología cognitiva se ha configurado para realizar sugerencias de asociación de objetos, el sistema actualiza las asociaciones padre o hijo del objeto.

        Es posible que pueda elegir varias sugerencias.
   3. Si no desea utilizar ninguna de las sugerencias, cierre el panel. Para generar una nueva lista de sugerencias, cambie el texto en el campo de entrada del clasificador, por ejemplo, el campo **Descripción**. Pulse de nuevo el botón IBM Watson Insights.
10. Pulse ![Icono de guardar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/save_icon_task_focused_ui.jpg).

### Creación de objetos desde un panel de control

`Guía del usuario › Creación y asociación de objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-creating-from-dashboard-panel)

Puede crear objetos desde un panel de panel de control.

#### Antes de empezar

Verifique que el panel de control contiene un panel que le permite crear objetos. Si no tiene un panel de este tipo, es posible que pueda crear uno, en función de sus permisos. Para obtener más información, consulte [Adición de un panel personalizado](#adición-de-un-panel-personalizado).

#### Acerca de esta tarea

Desde este punto de acceso, el objeto padre no se conoce. La vista contiene un campo de relación que permite seleccionar un objeto padre.

#### Procedimiento

1. Pulse ![Acceso directo de la página de inicio](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_home_page.jpg).
2. Busque un panel que le permita crear objetos. Pulse un botón de creación en un panel que tiene un botón con una etiqueta como Crear control o Crear riesgo.

   Se abre la vista Creación.
3. Complete los pasos tal como se describe en [Creación de objetos desde una vista de cuadrícula](#creación-de-objetos-desde-una-vista-de-cuadrícula).
4. Pulse **Guardar**.

### Creación de objetos hijo desde una vista de tarea

`Guía del usuario › Creación y asociación de objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-creating-child-from-task-view)

Puede crear objetos hijo, por ejemplo, Problemas y Acciones, desde sus objetos padre.

#### Acerca de esta tarea

En función del tipo de objeto, una vista de tarea puede mostrar botones en los que puede crear objetos hijo. Acceda a una vista de tarea trabajando en una tarea que se le asigne o abriendo un objeto desde una vista de cuadrícula.

Desde este punto de acceso, el padre primario se establece en el objeto de la tarea en la que estaba trabajando. La vista puede contener un campo de relación que le permita seleccionar un objeto padre y objetos hijo diferentes.

#### Procedimiento

1. Abra un objeto desde una vista de cuadrícula o acceda a una tarea que se le haya asignado. Para obtener más información, consulte [Completar el trabajo que se le ha asignado](#completar-el-trabajo-asignado).
2. Revise el objeto.
3. Busque una sección con una etiqueta para el tipo de objeto hijo y botones como **Nuevo problema**o **Nuevo control**. Para obtener más información sobre cómo realizar asociaciones, consulte [Asociaciones entre objetos](#asociaciones-entre-objetos).

   La vista de creación se abre en una nueva pestaña o en la barra lateral, en función de la configuración.
4. Complete los pasos tal como se describe en [Creación de objetos desde una vista de cuadrícula](#creación-de-objetos-desde-una-vista-de-cuadrícula). La única diferencia es que no se debe proporcionar el objeto padre.
5. Pulse **Guardar**.

### Asociaciones entre objetos

`Guía del usuario › Creación y asociación de objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-associations-between)

Puede enlazar objetos para formar una vista de árbol jerárquico de la estructura de gobierno, gestión de riesgos y conformidad de una empresa. La vista de árbol puede extenderse desde el nivel de entidad empresarial hasta los detalles de cada riesgo individual, control y prueba.

El proceso de enlazar objetos se llama de asociación. Las asociaciones son relaciones que existen entre objetos o entre objetos y archivos adjuntos. Se pueden crear o eliminar asociaciones sin que ello afecte al objeto o el archivo relacionado.

IBM OpenPages® Object Model Framework contiene lógica empresarial que rige las reglas siguientes:

- El tipo de objetos que se pueden asociar juntos. Por ejemplo, en el modelo de objeto estándar, un objeto de control se puede asociar con un plan de prueba y riesgo, pero no con un proceso.
- Cómo se relacionan los objetos entre sí en la jerarquía, como padre-hijo.

En una relación jerárquica padre-hijo, el objeto que inicializa la asociación es el objeto padre, y el objeto que es el destino de la asociación es el objeto hijo. Dependiendo del modelo de objeto, si un tipo de objeto puede tener varios objetos padre a través de la asociación, ese objeto hijo puede tener sólo una asociación padre principal. La relación padre-hijo que existe entre objetos afecta al modo en que la aplicación realiza determinadas operaciones como, por ejemplo, copiar, suprimir, asociar y bloquear. Por ejemplo, cuando un usuario bloquea un objeto padre, todos sus objetos hijo asociados también están bloqueados y no se pueden modificar hasta que se elimina el bloqueo.

En función del tipo de objeto, se pueden enlazar varios objetos padre o hijo a él. Por ejemplo, un objeto Riesgo, puede tener varios objetos padre, como Objetivos de control y Evaluaciones de riesgo, objetos hijo como Controles y Problemas, y archivos y enlaces. Se pueden crear o eliminar asociaciones sin que ello afecte al objeto o el archivo relacionado.

Las asociaciones se pueden mostrar y crear en vistas como campos de relación. Los campos de relación de tarjeta y cuadrícula son similares pero se ven un poco diferentes.

Su administrador define las etiquetas y funciones de los botones para cada campo de relación. Por ejemplo, la etiqueta del botón que copia objetos de forma recursiva podría tener la etiqueta **Copiar objeto y descendientes** o **Copiar recursivo**. Consulte a su administrador si no está seguro de la función de los botones.

Para trabajar con asociaciones, cree un objeto nuevo o acceda al objeto en el que desea trabajar. En la vista de tarea, las secciones y los campos de relación dependen de cómo haya configurado el administrador la vista.

El ejemplo siguiente muestra una tarjeta y un campo de relación de cuadrícula en una sección que se utiliza para mostrar los hijos de un riesgo. El campo de relación de tarjeta es para Problemas y el campo de relación de cuadrícula es para Controles. Puede asociar o añadir objetos, crear objetos nuevos y copiar objetos de forma recursiva en ambos campos de relación.

*Figura 1. Ejemplo de una tarjeta y una relación de cuadrícula*

![Se muestra una sección para objetos hijo de un riesgo. La sección contiene un campo de relación de tarjeta y un campo de relación de cuadrícula. El campo de relación de tarjeta muestra tres paneles, cada uno de los cuales muestra un problema. El campo de relación de tarjeta incluye tres botones: Añadir problema, Nuevo problema y Copiar recurrente. El campo de relación de cuadrícula muestra tres filas, cada una de las cuales muestra un control. El campo de relación de cuadrícula incluye tres botones: Añadir control, Nuevo control y Copiar recursivo.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/grid_and_card_relationships.png)

#### Asociación de un nuevo objeto secundario

Para un campo de relación de hijo, es posible que el administrador haya configurado un botón que cree y asocie un objeto hijo. Al hacer clic en el botón se abre la Vista de creación para el tipo de objeto.

#### Asociar un objeto existente

Para un campo de relación, es posible que el administrador haya configurado un botón que asocie un objeto existente. Al hacer clic en el botón se abre una Vista de cuadrícula donde puede seleccionar objetos.

Por ejemplo, en la vista de tarea de un proceso, puede tener una vista de cuadrícula que muestre los hijos de riesgo del proceso.

*Figura 2. Ejemplo de una relación de cuadrícula que muestra los objetos hijo Riesgo de un objeto Proceso*

![Se muestra una sección para objetos hijo Riesgo. La sección contiene el campo de relación de cuadrícula. El campo de relación de cuadrícula muestra tres filas, cada una de las cuales muestra un riesgo. El campo de relación de cuadrícula incluye tres botones: Nuevo riesgo, Añadir riesgos y Copiar.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_add_action1.png)

El administrador ha configurado la Vista de cuadrícula para que tenga los siguientes botones:

- Un botón **Nuevo riesgo** en el que se hace clic para crear y asociar un riesgo como hijo del proceso.
- Un botón **Añadir riesgos** en el que se hace clic para asociar un riesgo existente como hijo del proceso.
- Un **botón Copiar** en el que se hace clic para hacer una copia de los Riesgos seleccionados y sus descendientes.

Al hacer clic en **Añadir riesgos**, se muestra una vista de cuadrícula.

*Figura 3. Ejemplo de una cuadrícula para añadir objetos hijo de riesgo con un filtro público aplicado*

![Se muestra una cuadrícula para añadir objetos hijo de riesgo. No se muestran riesgos porque el filtro público Riesgo de interrupción del negocio se aplica a la cuadrícula.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_add_action2.png)

En la Figura 3, no se muestran riesgos porque el filtro público Riesgo de interrupción de negocio se aplica a la cuadrícula. Si el administrador no le ha prohibido eliminar el filtro público, puede pulsar **X** para eliminar el filtro y actualizar la lista de riesgos.

*Figura 4. Ejemplo de una cuadrícula para añadir objetos hijo de riesgo sin aplicar el filtro público*

![Se muestra una cuadrícula para añadir objetos hijo de riesgo. Los riesgos se muestran porque el filtro público Riesgo de interrupción de negocio se ha inhabilitado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_add_action3.png)

Si desea aplicar un filtro, haga clic en ![Icono de filtro](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-filter.jpg) y seleccione el filtro que desea aplicar.

Si tiene un campo de relación que muestra los hijos del objeto actual, es posible que no haya un botón que asocie un objeto existente. Si se da uno de los siguientes casos, el botón no se muestra:

- Tu administrador no configuró el campo de relación para que tenga un botón que asocie un objeto existente.
- Su administrador configuró su sistema para que un tipo de objeto secundario solo pueda tener un objeto principal del tipo de objeto actual. En este caso, el botón no se muestra para ese tipo de objeto secundario porque los objetos secundarios existentes podrían tener ya un objeto principal de ese tipo.

Puede tener un campo de relación que muestre los padres del objeto actual. Si el campo está definido con un botón que asocia un objeto existente, puede hacer clic en el botón para añadir un elemento principal. Si su administrador configuró su sistema de manera que solo se permite un padre de un tipo de objeto específico para el tipo de objeto actual, puede hacer clic en el botón para reemplazar el padre existente. Se muestra una advertencia con la cuadrícula de selección para indicar que se reemplazará la asociación existente.

Cuando selecciona uno o más objetos asociados en un campo de relación, verá los siguientes botones:

- Aparece un botón que elimina los objetos.
- Si el campo de relación tiene un botón que asocia objetos existentes, también se muestra un botón que elimina objetos. Con este botón, puede desvincular objetos. No elimina objetos. Si el campo de relación es obligatorio, se pueden eliminar todos los objetos asociados excepto uno.

#### Copiar objetos y sus descendientes

Puede hacer clic en un botón para copiar los objetos seleccionados y sus descendientes si su administrador configuró el campo de relación para mostrar ese botón. Por ejemplo, puede hacer clic en el botón de una vista de tareas para los objetos de proceso y hacer copias de los objetos de riesgo y control existentes. En la Figura 5, **el botón Copiar objeto y descendientes** inicia este proceso de copia recursivo. Cuando accede a la pestaña Tarea de un proceso, un campo de relación de cuadrícula muestra los objetos Riesgo que ya están asociados como hijos con el objeto Proceso abierto y que coinciden con un **Filtro público**, si se ha definido uno.

Dependiendo de cómo se defina el botón de copia recursiva, se realizan copias de los objetos secundarios y descendientes del objeto de origen, para una relación de tipo de objeto especificada. Solo se copian los objetos hijo que tienen el objeto de origen como padre primario. Por ejemplo, cuando se copia un objeto de riesgo, también se pueden realizar copias de todos los objetos de control hijo que tienen el riesgo como padre primario.

Además, dependiendo de cómo esté definido el botón de copia recursiva, las asociaciones principales de un objeto de origen pueden replicarse en objetos recién copiados. Por ejemplo, un control recién copiado puede estar asociado a los mismos objetos de requisito padre no primario que el objeto de control de origen.

Por ejemplo, el proceso denominado « RB-01 » tiene los elementos secundarios que se muestran en la Figura 5.

*Figura 5. Una cuadrícula en una pestaña de Tarea que muestra los objetos secundarios de Riesgo del Proceso llamado RB-01*

![Se muestra una cuadrícula que muestra objetos hijo de riesgo en una pestaña Tarea. Los riesgos son hijos del proceso denominado RB-01.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_copy_recursive_action1.png)

El riesgo denominado RB-01-Risk00189 es uno de los hijos. RB-01-Risk00189 o de riesgos tiene el niño Controlar objetos que se muestran en la Figura 6.

*Figura 6. Una cuadrícula en una pestaña de Tarea que muestra Controlar objetos secundarios del Riesgo llamado RB-01-Risk00189*

![Se muestra una cuadrícula que muestra objetos hijo de control en una pestaña Tarea. Los controles son hijos del riesgo denominado RB-01-Risk00189.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_copy_recursive_action2.png)

Al hacer clic en el botón **Copiar objeto y descendientes** que se muestra en la Figura 5, se inicia el proceso de copia recursiva. Se listan los riesgos que cumplen los criterios **Filtro de carpeta** y **Reglas de filtro** . La lista incluye los riesgos que ya están asociados con el proceso y los riesgos que no lo están.

*Figura 7. El recuadro de diálogo **Copiar objetos y descendientes** muestra los objetos hijo Riesgo que se pueden copiar.*

![Un cuadro de diálogo que muestra los objetos hijo de riesgo que se pueden copiar.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_copy_recursive_action3.png)

Cuando seleccionas el riesgo que se llama " RB-01-Risk00189 " y haces clic en **"Done** ", se crea una copia del objeto de riesgo seleccionado y sus descendientes. El nuevo riesgo, denominado RB-01_RIS_0000001, está asociado al proceso que está abierto en la vista.

*Figura 8. La cuadrícula de objetos hijo Riesgo que muestra el riesgo copiado indicado por un círculo rojo.*

![Un recuadro de diálogo que muestra el nuevo objeto Riesgo que se ha copiado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_copy_recursive_action4.png)

Se han realizado copias de los objetos Control hijo. En la Figura 9, se muestran los hijos del nuevo riesgo RB-01_RIS_0000001 .

*Figura 9. La cuadrícula de objetos hijo de control que se han copiado.*

![Un cuadro de diálogo que muestra los nuevos objetos de control hijo que se han copiado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/user_copy_recursive_action5.png)

#### Establecer el padre principal

Puede establecer un padre principal si los objetos del campo de relación son padres y su administrador ha configurado un botón para establecer un padre principal. Al hacer clic en el botón, puede asociar un objeto principal o cambiar el principal actual. Al hacer clic en el botón que establece un elemento principal, se abre una vista de cuadrícula donde puede seleccionar un objeto. Si el objeto no tiene un padre primario, el objeto padre que ha elegido se establece en el padre primario. Si el objeto tiene un objeto primario, el objeto primario que eligió lo anula como objeto primario, pero el anterior primario permanece como objeto primario.

Para obtener más información sobre la asociación de padres principales, consulte [Asociación de padres principales](#asociación-padre-principal).

### Disociación de objetos

`Guía del usuario › Creación y asociación de objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-disassociating)

Puede asociar un objeto padre o hijo, archivo o enlace a un objeto. Por ejemplo, desde un objeto Riesgo, puede añadir enlaces a objetos padre, como Objetivos de control y Evaluaciones de riesgo. También puede eliminar enlaces de objetos hijo, archivos o enlaces. Cuando disocia un objeto, sólo se elimina la asociación o enlace entre los objetos. Los objetos no se ven afectados.

#### Procedimiento

1. Acceda al objeto sobre el que desea trabajar.
2. En un campo de relación de cuadrícula, seleccione el objeto con una marca de selección. Pulse **Eliminar**.
3. En un campo de relación de tarjeta, pulse ![Icono expandir árbol](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_tree_expand_icon_task_focused_ui.jpg) (Iniciar página de cuadrícula). En la página de cuadrícula, seleccione el objeto con una marca de selección y, a continuación, pulse **Eliminar**.

### Asociación padre principal

`Guía del usuario › Creación y asociación de objetos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-primary-parent-association)

Cuando se añade un objeto hijo desde la vista Admin de un objeto padre, se considera que es un «“hijo primario”». El objeto hijo se asocia automáticamente con ese objeto padre primario al crearlo y el objeto hijo tiene la misma vía de acceso de carpeta que el padre primario.

Los tipos de objeto que pueden tener varios objetos padre a través de la asociación pueden sólo pueden tener una asociación padre principal. Por ejemplo, si Control-01 se ha añadido desde la Vista de tareas de Risk-01 y también se ha asociado a Risk-02, Control-01 tendría dos padres: Risk-01 y Risk-02. Sin embargo, sólo Riesgo-01 debe considerarse padre principal de Control-01.

Un objeto padre primario se identifica con el icono ![Icono de objeto padre](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon_parentobject.jpg) en los campos de relación de cuadrícula y tarjeta y la etiqueta **Padre primario**en un diagrama de árbol.

Cuando las asociaciones primarias están habilitadas:

- Puede cambiar una asociación principal del objeto de un objeto padre a otro reasignando el padre principal.
- Cualquier reasignación de la asociación primaria de un objeto padre a otro objeto padre se refleja en la pestaña Actividad de un objeto.
- Un objeto hijo con varios padres que se desasocia de su objeto padre primario se reasigna automáticamente a un nuevo padre primario.
- Las operaciones en cascada en objetos (como validación, supresión, bloqueo o desbloqueo) se basan en asociaciones primarias.
- Los objetos con varios padres que no están incluidos en una operación de supresión en cascada (por ejemplo, problemas y elementos de acción) se reasignan automáticamente a un nuevo padre primario.
- Las operaciones de copia en objetos duplican las asociaciones existentes (incluidas las asociaciones primarias) siempre que sea posible. Una asociación padre principal también se asigna a la primera asociación.

#### Cambio de la asociación padre principal

`Guía del usuario › Creación y asociación de objetos › Asociación padre principal` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=association-changing-primary-parent)

Un objeto sólo puede tener un padre principal. Si un objeto tiene varios objetos padre, puede cambiar la asociación principal de un objeto padre a otro.

##### Acerca de esta tarea

Cualquier padre primario anterior permanece asociado pero pasa a ser secundario, incluso si el padre primario anterior era de un tipo de objeto diferente. Si sólo se permite un padre de ese tipo, el padre recién seleccionado sustituye a cualquier padre previamente seleccionado del mismo tipo.

##### Procedimiento

1. Acceda al objeto sobre el que desea trabajar.
2. Busque la sección que contiene los objetos padre.
3. Pulse **Seleccionar primario**.
4. Elija un objeto diferente.
5. Pulse **Terminado**.

   El icono **Asociación primaria** se muestra junto al nombre del nuevo objeto padre primario.

## Utilización de filtros en vistas de cuadrícula

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-filters-in-grid-views)

Los filtros son herramientas útiles que hacen que la búsqueda de información en una vista de cuadrícula sea más personalizada y gestionable.

Utilice filtros para limitar la información que se visualiza en una lista de objetos, ya que sólo se visualizan en la lista los objetos que coinciden con los criterios.

A veces hay miles de objetos entre los que elegir en una vista de cuadrícula o una cuadrícula de asociación de una vista de tarea. Aplique un filtro para las cuadrículas que tienen un gran número de objetos. Los filtros optimizan el rendimiento visualizando sólo los objetos que son relevantes para usted.

Sólo los filtros públicos y privados están disponibles en una cuadrícula de asociación de una vista de tarea.

Los siguientes tipos de filtros están disponibles en las vistas de cuadrícula:

### Búsqueda de objetos con el recuadro Buscar

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-finding-objects-search-box)

Utilice el recuadro Buscar para buscar valores específicos en los objetos listados en una vista de cuadrícula.

#### Acerca de esta tarea

Puede buscar en el idioma de su entorno local. Por ejemplo, si su entorno local es Francia, puede buscar en francés.

También puede buscar en inglés en cualquier entorno local. Por ejemplo, si el entorno local es Francia, puede buscar en inglés y un filtro devuelve los objetos coincidentes y los muestra en francés.

La búsqueda sólo devuelve resultados que son una coincidencia exacta. Si busca objetos con descripciones que contienen «“ `bids and justifications` ”» pero la descripción de un objeto contiene «“ `bid and justification` ”» o «“ `bids and justifications` ”» (espacios adicionales), el objeto no se devuelve en los resultados de la búsqueda.

> **Nota:** Los criterios de búsqueda se conservan la próxima vez que acceda a la vista en la misma sesión de navegador.

#### Procedimiento

1. Abra una vista de cuadrícula.
2. Pulse el recuadro **Buscar** y busque por las opciones siguientes:

   | Valor del campo | Descripción de campo |
   | --- | --- |
   | Nombre y descripción | Especifique todo o parte del nombre o descripción de un objeto. |
   | Campo enumerado o etiqueta | Especifique todo o parte de un campo o etiqueta. Por ejemplo, la búsqueda en `Status` devuelve una lista de campos enumerados que contienen `Status`, como por ejemplo **Estado del modelo** o **Estado de despliegue**. |
   | Varios campos enumerados | Especifique varios campos o etiquetas de enumeración. Por ejemplo, la búsqueda de `Model Status:Awaiting Approval` y `Final tier: Tier 1` devuelve objetos que tienen un estado de **En espera de aprobación** y un nivel de **Nivel 1**. |
   | Valores de un único campo enumerado | Especifique un valor de un campo o etiqueta enumerado. Por ejemplo, la búsqueda de `Model Status:Approved for Deployment` o `Model Status:Awaiting Approval` devuelve objetos que tienen un estado de **Aprobado para despliegue** o **En espera de aprobación**. |
   | Valores de varios campos enumerados | Especifique un valor de un campo o etiqueta enumerado. Por ejemplo, buscando `Model Status:Approved for Deployment`, `Model Status:Awaiting Approval`y `Risk Level:High`. La lista devuelve objetos con un estado de **Aprobado** o **En espera de aprobación** y un nivel de riesgo de **Alto**. |
3. Opcional: Para refinar más la búsqueda, puede aplicar un filtro público, privado o de carpeta.

   Para obtener más información sobre los filtros públicos y privados, consulte [Utilización de filtros públicos](#utilización-de-filtros-públicos) y [Utilización de filtros privados](#utilización-de-filtros-privados). Para obtener más información sobre los filtros de carpeta, consulte [Utilización de filtros de carpeta (Entidad de negocios)](#utilización-de-filtros-de-carpeta-entidad-de-negocios)
4. Para eliminar el filtro y renovar la lista, pulse el nombre del filtro en la cabecera.

### Utilización de filtros de carpeta (Entidad de negocios)

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-using-folder-filters-business-entity)

Utilice un filtro de carpeta (Entidad de negocios) para identificar objetos basándose en la jerarquía de carpetas a la que pertenece el tipo de objeto.

#### Acerca de esta tarea

Los administradores definen jerarquías de carpetas mediante **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Archivos de sistema**. Si no es un administrador, puede seleccionar carpetas en la jerarquía pero no puede añadir ni editar la jerarquía.

#### Procedimiento

1. Desde una vista de cuadrícula, pulse ![icono de filtro](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/filter_icon_task_focused_ui.jpg) para acceder a los filtros.
2. En la sección **Entidad de negocios** , pulse **Seleccionar** y vea la jerarquía de carpetas.
3. Navegue por la jerarquía y seleccione una carpeta. **No se pueden seleccionar varias carpetas.**

   El nombre de filtro y el número de resultados se muestran en la cabecera. Los objetos que coinciden con los criterios de filtro se listan en la vista de cuadrícula.
4. Pulse **Terminado** para confirmar el filtro de carpeta.
5. Opcional: Para refinar más la búsqueda, utilice el recuadro Buscar.

   Para obtener más información, consulte [Búsqueda de objetos con el recuadro de búsqueda](#búsqueda-de-objetos-con-el-recuadro-buscar).
6. Opcional: Para refinar más la búsqueda, aplique un filtro público o privado.

   Para obtener información, consulte [Utilización de filtros públicos](#utilización-de-filtros-públicos) y [Utilización de filtros privados](#utilización-de-filtros-privados).
7. Para eliminar un filtro de carpeta y renovar la vista de cuadrícula, pulse el nombre de carpeta en la jerarquía de carpetas.

### Utilización de filtros públicos

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-using-public-filters)

Utilice filtros públicos para buscar objetos en una vista de cuadrícula basándose en criterios de búsqueda.

#### Acerca de esta tarea

Un administrador define filtros públicos y sólo se puede aplicar un filtro público a la vez.

Puede utilizar simultáneamente un filtro público, un filtro de carpeta (entidad empresarial) y criterios de búsqueda. Un objeto debe coincidir con todos los criterios listados para visualizarse en la vista de cuadrícula.

No puede utilizar simultáneamente un filtro público y un filtro privado.

#### Procedimiento

1. Desde una vista de cuadrícula, pulse ![Icono de filtro](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/filter_icon_task_focused_ui.jpg) para acceder a los filtros.
2. En **Filtros públicos**, seleccione un filtro.

   Se indica el nombre de filtro y el número de resultados. Los objetos que coinciden con los criterios de filtro se listan en la cuadrícula.
3. Opcional: Para refinar más la búsqueda, especifique los criterios de búsqueda en el recuadro Buscar.

   Para obtener más información, consulte [Búsqueda de objetos con el recuadro de búsqueda](#búsqueda-de-objetos-con-el-recuadro-buscar).
4. Opcional: Para refinar más la búsqueda, aplique un filtro de carpeta.

   Para obtener información, consulte [Utilización de filtros de carpeta (Entidad de negocios)](#utilización-de-filtros-de-carpeta-entidad-de-negocios).
5. Para eliminar el filtro y renovar la lista, pulse el nombre del filtro en la cabecera.

### Utilización de filtros privados

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-using-private-filters)

Utilice y personalice filtros privados para buscar objetos basados en criterios sobre valores de campo en objetos y, opcionalmente, objetos padre.

#### Acerca de esta tarea

Los usuarios pueden personalizar filtros privados para su propio uso.

Solo se puede aplicar un filtro privado a la vez.

Puede aplicar un filtro privado, un filtro de carpeta (entidad empresarial) y criterios de búsqueda simultáneamente. Un objeto debe coincidir con todos los criterios que se van a visualizar en la vista de cuadrícula.

No puede aplicar un filtro público y un filtro privado.

#### Procedimiento

1. Desde una vista de cuadrícula, pulse ![Icono de filtro](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/filter_icon_task_focused_ui.jpg) para acceder a los filtros.
2. En **Mis filtros**, seleccione un filtro de la lista.

   Si no ve ningún filtro, puede crear un filtro. Consulte [Definición de filtros privados](#definición-de-filtros-privados).

   El nombre de filtro y el número de resultados se muestran en la cabecera. Los objetos que coinciden con los criterios de filtro se listan en la cuadrícula.
3. Opcional: Para refinar más la búsqueda, especifique los criterios de búsqueda en el recuadro de búsqueda.

   Para obtener más información, consulte [Búsqueda de objetos con el recuadro de búsqueda](#búsqueda-de-objetos-con-el-recuadro-buscar).
4. Opcional: Para refinar más la búsqueda, aplique un filtro de carpeta.

   Para obtener información, consulte [Utilización de filtros de carpeta (Entidad de negocios)](#utilización-de-filtros-de-carpeta-entidad-de-negocios).
5. Para eliminar el filtro y renovar la lista, pulse el nombre del filtro en la cabecera.

### Definición de filtros privados

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-defining-private-filters)

Defina un filtro privado en una vista de cuadrícula para guardar los criterios de búsqueda a los que accede con frecuencia.

#### Antes de empezar

Cuando define un filtro privado, OpenPages® sólo muestra los campos que están disponibles para su perfil. Si desea crear un filtro basado en un campo que no se visualiza, solicite al administrador que compruebe el perfil.

#### Acerca de esta tarea

Una definición de filtro privado especifica los siguientes tipos de criterios:

- Criterios de objeto base que constan de condiciones en el tipo de objeto que se visualiza en la vista de cuadrícula.

  - Si define varias condiciones en el tipo de objeto, se deben cumplir todas las condiciones. Para alterar temporalmente esta regla, defina la lógica avanzada para combinar la condición de una forma específica.

    Por ejemplo, si define tres condiciones, la lógica predeterminada es recuperar los objetos que coinciden con las tres condiciones: `1 and 2 and 3`. Sin embargo, si define la lógica avanzada, puede utilizar los números de condición junto con los operadores `and`, `or`, `not`y paréntesis para crear una sentencia más refinada. Por ejemplo, una sentencia puede ser `1 or 2 or 3` o una sentencia puede ser `1 and (2 or 3)`.
- Criterios de objeto relacionados que constan de condiciones en los padres, hijos, ancestros y descendientes del tipo de objeto que se visualiza en la vista de cuadrícula.

  Por ejemplo, en una vista de cuadrícula para riesgos, un filtro basado en padre puede restringir la lista de objetos Riesgo a solo aquellos riesgos que tienen un objeto Proceso como padre. Sin embargo, debe añadir al menos una condición. Por ejemplo, puede añadir una condición para mostrar sólo los riesgos en los que el objeto de proceso padre tiene un estado de En espera de aprobación. También puede limitar los objetos relacionados a los del árbol padre primario.

  Si un filtro tiene ambos tipos de criterios, ambos deben cumplirse para visualizar un objeto en la vista de cuadrícula.

#### Procedimiento

1. Desde una vista de cuadrícula, pulse ![Icono de filtro](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/filter_icon_task_focused_ui.jpg) para acceder a los filtros.
2. En **Mis filtros**, pulse **Nuevo filtro** y añada un nombre.
3. Pulse **Nueva condición**.

   Puede crear una condición utilizando etiquetas o campos. Puede crear un filtro que utilice una combinación de condiciones de etiqueta y condiciones de campo.

   > **Nota:** Si no ve una opción **Etiqueta** , el etiquetado no está habilitado. Solo puede crear condiciones de campo. Vaya al paso 5.
4. Para crear una condición que utilice etiquetas, pulse **Etiqueta**y, a continuación, seleccione una etiqueta.

   > **Nota:** Si la lista está vacía, no hay etiquetas disponibles.
5. Para crear una condición que utilice campos, pulse **Campo**. Realice los pasos siguientes para cada campo por el que desee filtrar.

   1. Seleccione un **Campo** y una **Operación** a la que se aplicará el filtro.

      Las operaciones disponibles y los campos restantes dependen del campo que seleccione. Por ejemplo, las operaciones siguientes están disponibles para el campo Descripción: **Empieza con**, **Finaliza con**, **Contiene**, **No contiene**, **Igual a**, **No igual a**, **Finaliza con**, **Está vacío**y **No está vacío**.

      > **Nota:** el texto no distingue entre mayúsculas y minúsculas.

      La tabla siguiente describe las operaciones disponibles para cada tipo de campo.

      **Tabla 1. Condiciones de filtro**

      | Tipo de campo | Operaciones |
      | --- | --- |
      | Usuario | Puede seleccionar las operaciones siguientes:<br>• **Está vacío** o **No está vacío**<br>• **Coincide con el usuario seleccionado** y añade uno o más usuarios en la lista bajo **Otro usuario** o puede establecer **Me** en **True** para establecerse como usuario. |
      | Grupo | Seleccione la operación **Incluye todos los usuarios seleccionados** y añada uno o más grupos en la lista bajo **Otros grupos**. O bien, puede establecer **Usuario final** para que se resuelva en el usuario que ha iniciado la sesión. |
      | Valor enumerado | Puede seleccionar **Está vacío** o la operación **No está vacío** , o puede seleccionar la operación **Cualquiera de los valores siguientes** y añadir valores enumerados en la lista bajo **Seleccionar valores**. También puede establecer **Mostrar valores ocultos**. |
      | Valor de serie | Puede seleccionar la operación **Está vacía** o la operación **No está vacía** , o puede seleccionar una operación (por ejemplo, **Empieza por**, **Finaliza con**, **Contiene**, **No contiene**, **Igual a**, **No es igual a**o **Finaliza con**) y, a continuación, especificar un valor de texto. El texto no distingue entre mayúsculas y minúsculas. |
      | Fecha | Seleccione una operación (por ejemplo, **En el último**, **En el siguiente**, **En una fecha específica**,**No en una fecha específica**o **En el rango**) y, a continuación, especifique un valor. |
      | Valor numérico | Puede seleccionar la operación **Está vacía** o **No está vacía** , o puede seleccionar una operación (por ejemplo, **Igual a**, **No igual a**, **Mayor que**, **Menor que**o **En el rango**) y, a continuación, especificar un valor. |
      | Booleano | Seleccione **true** o **false**. |

      > **Nota:** Los filtros privados no admiten campos calculados, campos de serie larga o fragmentos de informes.
   2. Pulse **Terminado**.
6. Opcional: Los filtros se establecen automáticamente para cumplir todas las condiciones listadas. Para alterar temporalmente esta regla predeterminada, establezca **Lógica avanzada** en `True` y escriba una sentencia en **Lógica**.

   Para escribir una sentencia lógica, establezca los números de condición con los operadores `AND`, `OR`, `NOT`y paréntesis.

   El orden de las operaciones es: `()` then `NOT` then `AND` then `OR`.

   Por ejemplo:

   - `1 OR 2 OR 3`
   - `1 AND (2 OR 3)`
   - `1 NOT (2 OR 3)`
7. Opcional: Expanda **Criterios de objetos relacionados** para filtrar por objetos relacionados.

   Para filtrar basándose en los campos de los objetos relacionados, realice los pasos siguientes:

   1. Seleccione un **Tipo de relación** y un **Tipo de objeto**.

      Los campos restantes dependen del tipo de objeto que seleccione.
   2. En **Condiciones de objeto relacionadas**, pulse **Nueva condición**.

      Repita el paso 3 para configurar la condición.
   3. Pulse **Terminado**.

   Si elige **Ancestros** o **Descendientes** para el **Tipo de relación**, especifique la vía de acceso de relación que se utilizará para el filtro y, a continuación, especifique una condición.

   1. Pulse **Editar**. Se visualiza un panel lateral.
   2. Utilice el árbol para seleccionar las vías de acceso entre el objeto y sus ancestros o descendientes.
   3. En **Condiciones de objeto relacionadas**, pulse **Nueva condición**.

      Repita el paso 3 para configurar la condición.

   Para limitar el filtro a los padres primarios, pulse **Sólo jerarquía de padres primarios**.
8. Haga clic en **Guardar** para aplicar el filtro.

#### Resultados

El filtro se aplica y se visualizan los objetos que coinciden con los criterios de filtro. En la cabecera se muestran el nombre del filtro y el número de resultados.

Para editar el filtro, pulse ![icono de edición](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_icon.jpg).

> **Sugerencia:** Cuando crea un filtro que utiliza **Ancestros** o **Descendientes** y la vía de acceso de la relación sólo utiliza padres o hijos, el filtro muestra **Padres** o **Hijos** para el **Tipo de relación** cuando edita el filtro.

Para eliminar el filtro, pulse el nombre del filtro en la cabecera.

### Utilización de filtros ad hoc

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-using-ad-hoc-filters)

Los filtros ad hoc son filtros privados que no se guardan y sólo se utilizan en una sesión. Utilice un filtro ad hoc si no accede con frecuencia a los criterios de búsqueda.

#### Acerca de esta tarea

Solo se puede aplicar un filtro ad hoc a la vez.

No puede aplicar un filtro público y un filtro ad hoc.

Puede aplicar un filtro ad hoc, un filtro de carpeta y los criterios de búsqueda que especifique en el recuadro Buscar. Un objeto debe coincidir con todos los criterios que se van a visualizar en la vista de cuadrícula.

#### Procedimiento

1. Desde una vista de cuadrícula, pulse ![Icono de filtro](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/filter_icon_task_focused_ui.jpg) para acceder a los filtros.
2. En **Mis filtros**, pulse **Nuevo filtro**.
3. No complete el campo **Nombre** . Si deja el campo **Nombre** incompleto, se asegura de que no se guarde el filtro.
4. Complete los campos y condiciones restantes y pulse **Aplicar**. Para obtener más detalles sobre cómo crear un filtro privado, consulte [Definición de filtros privados](#definición-de-filtros-privados).

   Cuando se aplica el filtro, se indica un filtro denominado `Unsaved Filter` y el número de resultados en la cabecera de la vista de cuadrícula.
5. Para editar el filtro ad hoc, especifique los cambios en el panel de filtros y pulse **Aplicar**. Repítalo tantas veces como sea necesario.

   > **Sugerencia:** Si decide guardar el filtro, complete el campo **Nombre** y pulse **Guardar**.
6. Para suprimir el filtro ad hoc, pulse `Unsaved Filter` en la cabecera y renueve la lista.
7. Opcional: Para refinar más la búsqueda, especifique los criterios de búsqueda en el recuadro Buscar.

   Para obtener más información, consulte [Búsqueda de objetos con el recuadro de búsqueda](#búsqueda-de-objetos-con-el-recuadro-buscar).
8. Opcional: Para refinar más la búsqueda, aplique un filtro de carpeta.

   Para obtener información, consulte [Utilización de filtros de carpeta (Entidad de negocios)](#utilización-de-filtros-de-carpeta-entidad-de-negocios).

### Edición de filtros privados

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-editing-private-filters)

Después de crear y guardar un filtro privado, puede modificar los criterios de búsqueda y los valores de campo para el filtro.

#### Procedimiento

1. Desde una vista de cuadrícula, acceda a los filtros privados en **Mis filtros**.
2. Elija el filtro privado que desea editar y pulse ![icono de edición](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_icon.jpg).
3. Realice los cambios editando los valores de campo.

   Por ejemplo, para renombrar el filtro, edite el valor en el campo **Nombre** .
4. Haga clic en **Guardar** para confirmar todos los cambios.

### Supresión de filtros guardados

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-deleting-saved-filters)

Cuando ya no necesite un filtro privado, puede suprimir el filtro.

#### Procedimiento

1. Desde una vista de cuadrícula, acceda a los filtros privados en **Mis filtros**.
2. Elija el filtro privado que desea suprimir y pulse ![icono suprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/delete_icon.jpg).
3. Pulse **Suprimir** y renueve la vista de cuadrícula.

### Borrar resultados de filtro

`Guía del usuario › Utilización de filtros en vistas de cuadrícula` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=views-clearing-filter-results)

Puede borrar los filtros de la vista de cuadrícula que no los suprime de los filtros guardados.

#### Procedimiento

1. En la vista de cuadrícula, busque el `nombre de filtro` en la cabecera.
2. Pulse el `nombre de filtro` en la cabecera para eliminar el filtro.

   El filtro se elimina y la vista de cuadrícula se renueva.

## Búsqueda global

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-global-search)

la búsqueda global IBM OpenPages® ' utiliza técnicas avanzadas de procesamiento y análisis de textos para buscar en todos los tipos de objetos y encontrar registros relevantes para sus términos de búsqueda.

### ¿Cómo funciona la búsqueda global?

- La búsqueda global busca los criterios especificados en todos los tipos de objetos en diferentes disposiciones y devuelve los resultados por relevancia de palabras. La búsqueda global también puede buscar en cualquier archivo adjunto, si esta opción está activada. Los resultados de la búsqueda se clasifican en orden de mayor a menor relevancia. Se puede configurar un panel de búsqueda para ver todos los tipos de objeto o algunos específicos.
- La búsqueda global no hace una correspondencia textual de lo que se busca, sino que realiza un análisis léxico con procesamiento de lenguaje natural. La búsqueda global divide la secuencia de datos en símbolos y, a continuación, divide los símbolos en el significado raíz de cada palabra.

  Por ejemplo, si busca «“gestionar”», la búsqueda encuentra registros que contienen todas las variaciones de la palabra raíz «“gestionar”», como «“gestión”», «“gestiones”», «“gestor”», etc.
- La búsqueda global no intenta encontrar una coincidencia exacta de letras, palabras o patrones de caracteres como «“-”», «“:”», «“#”», «“(, )”», «“<,”» «“>”», etc., que pueden aparecer en un texto.
- La búsqueda global hace caso omiso del orden o colocación de los términos de búsqueda, salvo cuando se buscan frases. Por ejemplo, si se busca «“cios finan”» no se devuelve el resultado «“Servicios financieros”». Si se busca «“Con”» no se muestra el resultado «“Contabilidad”». Del mismo modo, si se busca «“Con”» no se devuelve «“Con”» porque «“con”» se considera una palabra común y no se indexa. La indexación de palabras comunes y su inclusión en los resultados de la búsqueda puede desviar los resultados de la búsqueda y la clasificación por importancia. Esto se debe a que las palabras comunes aparecen con tanta frecuencia que pueden pasar por delante de otras palabras más relevantes en la clasificación por importancia. Para obtener información sobre la búsqueda de frases, consulte [Frases](#técnicas-avanzadas-de-búsqueda-global).

> **Nota:**

> A continuación se muestra una lista de otras palabras comunes que se deben evitar (en inglés): a, an, and, are, as, at, be, by for, if, in, into, is, it, no, not, of, on, or, such, that, the, their, then, there, these, they, this, to, was, will y with.

> Estas son palabras comunes en inglés. Evite este tipo de palabras en otros idiomas distintos del inglés.

La siguiente tabla muestra algunas formas en que la búsqueda global responde a una búsqueda inicial.

| Si busca... | Puede esperar ver registros que contienen... |
| --- | --- |
| «“ `trade` ”» | «“comercios”», «“comerciar”» y «“comerciante”» es decir, las palabras no tienen que estar en su forma exacta. |
| «“ `step missing` ”» (sin comillas) | «“faltan pasos de proceso”», es decir, las palabras no tienen que estar en orden. |
| «“ `security breach` ”» (con comillas) | «“infracción de seguridad”», pero no «“seguridad de infracción”», es decir, el orden de palabras sí importa en cuando se buscan frases. |
| «“ `BaNk` ”» | «“>Banco”», «“banco”», «“BANCO”» y «“BANCA”», es decir, no se diferencia entre mayúsculas y minúsculas. |

### Comparación de métodos de búsqueda

Los siguientes métodos de búsqueda están disponibles en " IBM OpenPages:

- La búsqueda global está disponible si la ha configurado un administrador.
- La búsqueda global está disponible cuando se utiliza un panel de búsqueda en el panel de control. Sólo los administradores pueden añadir paneles de búsqueda.
- La búsqueda global utiliza análisis y técnicas avanzadas de procesamiento de texto, como la lematización, la simbolización y el procesamiento del lenguaje natural, para encontrar y mostrar registros relevantes para los términos de búsqueda.
- La búsqueda de vista de cuadrícula limita la información que se visualiza en una lista de objetos. Las búsquedas de vista de cuadrícula buscan una coincidencia exacta de las palabras o los caracteres que se escriben. No utilizan la búsqueda global. Para obtener más información, consulte [Uso de filtros en vistas de cuadrícula](#utilización-de-filtros-en-vistas-de-cuadrícula).

Utilice el método adecuado según el punto de acceso y lo que está buscando. Si necesita encontrar registros que deben coincidir con una corriente de texto exacta, utilice la búsqueda de vista de cuadrícula. Si desea encontrar registros relevantes para los términos de búsqueda, utilice la búsqueda global.

### Más información sobre la búsqueda global

### Búsqueda de objetos mediante la búsqueda global

`Guía del usuario › Búsqueda global` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=search-searching-objects-using-global)

Es posible buscar rápidamente y realizar acciones sobre los objetos relevantes para sus tareas de GRC mediante el empleo de la búsqueda global.

#### Antes de empezar

Compruebe que existe un panel de Búsqueda en la pestaña Inicio. El nombre puede variar, según cómo lo haya configurado por el administrador. Puede haber varios paneles de búsqueda, para todos los tipos de objeto o para tipos de objeto específicos. Si no hay ningún panel de búsqueda, informe al administrador. Los paneles de búsqueda sólo pueden ser añadidos por los administradores.

#### Procedimiento

1. Accede al panel de control.
2. Ve a la pestaña Inicio.
3. Busque un panel de búsqueda.
4. Especifique texto en el panel de búsqueda.

   Se visualizan hasta 25 objetos coincidentes con la búsqueda, clasificados de más a menos relevante. Cada resultado muestra un enlace que incluye el nombre de recurso y el tipo de objeto. Si el panel de búsqueda está configurado para buscar en el contenido de los archivos adjuntos, los objetos de archivo también se listan. Sólo se visualizan los objetos que tiene permiso para ver.
5. Pulse un objeto en la lista de resultados del panel de búsqueda para abrirlo en una pestaña nueva.
6. Haga clic en ' ![estrella de favoritos](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/favorites_star.jpg) ' para marcar un objeto como favorito.

   El objeto se añade al panel Favoritos.

#### Qué hacer a continuación

Obtenga información sobre las muchas maneras en que puede buscar información utilizando la búsqueda global. Para más información, consulte [Técnicas avanzadas de búsqueda global](#técnicas-avanzadas-de-búsqueda-global).

### Técnicas avanzadas de búsqueda global

`Guía del usuario › Búsqueda global` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=search-global-advanced-techniques)

En la mayoría de los casos, la búsqueda con términos y frases encuentra el registro que busca. También puede refinar su búsqueda utilizando sintaxis de búsqueda avanzada, como comodines, lógica booleana, agrupación, coincidencias difusas, proximidad y potenciación.

#### Términos

La manera más sencilla de utilizar la búsqueda global pasa por buscar uno o varios términos.

Un término es una palabra simple, como *riesgo*, *seguridad* o *gestión*. Los resultados de la búsqueda son más relevantes y específicos cuantos más términos se utilizan en la búsqueda. El orden y el uso de mayúsculas y minúsculas de los términos se omiten. Por ejemplo, buscar *Gestión del RIESGO de seguridad* es lo mismo que buscar *gestión de riesgos de seguridad* si no se utilizan comillas.

#### Frases

Las frases son parecidas a los términos, pero las palabras están entre comillas.

Todas las palabras de una frase tienen que aparecer y estar en el orden en el que se hayan especificado, sin otras palabras en medio. Por ejemplo, la frase «“gestión de riesgos de seguridad”» no es lo mismo que «“gestión de riesgos de seguridad”» o «“gestión de riesgos”» cuando se utilizan comillas. Además, la búsqueda de «“gestión de riesgos”» excluye registros con la frase «“gestión de la aversión al riesgo”» debido a que aparece la palabra «“aversión”» en medio de la frase.

Puede combinar varias frases para refinar más los resultados de la búsqueda. Por ejemplo, la búsqueda de «“gestión de”» «“riesgos de seguridad”» como dos frases, cada una entre comillas, encuentra registros que contienen ambas frases.

#### Comodines

La búsqueda global da soporte a las búsquedas con comodines que sustituyen a uno o varios caracteres dentro de un único término.

Para realizar una búsqueda con comodín de un solo carácter, utilice el símbolo «“`?`”». Para realizar una búsqueda con varios caracteres comodín, utilice el símbolo «“`*`”» símbolo .

La búsqueda con un comodín de un único carácter busca términos que coinciden con el único carácter sustituido. Por ejemplo, para buscar tanto «“test”» como «“texto”», utilice `te?t`.

La búsqueda con un comodín de varios caracteres busca 0 o más caracteres. Por ejemplo, para buscar «“gestión”» y «“directivos”» utilice `manag*`.

Los comodines pueden estar en cualquier posición dentro de un término, salvo al principio. Es decir, «“`*siness`”» y «“`?usiness`”» no son compatibles.

No se admite el uso de comodines en búsquedas de frase.

#### Booleano

Los operadores booleanos permiten combinar términos y frases mediante operadores lógicos para refinar en mayor medida los términos de búsqueda.

La búsqueda global admite AND, OR, NOT, «“+”» y «“-”» como operadores booleanos. Los operadores booleanos deben estar en mayúsculas.

El operador AND es el predeterminado para la búsqueda global. Si se buscan más términos, se devuelven menos resultados de búsqueda. Por ejemplo, buscar «“US UK”» es igual que buscar «“«US OR UK»”» (sin comillas) y devuelve registros que tienen «“US”» y «“UK”».

Utilice el operador OR para encontrar registros que contengan cualquiera de los términos de búsqueda. Por ejemplo, si busca «“US OR UK”» (sin comillas), se devuelven los registros que contienen únicamente US o UK, o que contienen ambos.

Utilice el operador NOT para excluir los registros que contengan términos de búsqueda específicos. Por ejemplo, al buscar «“gestión de riesgos US NOT UK”» (sin comillas) se encuentran registros que contienen los términos «“riesgo”», «“gestión”» y «“US”», pero aquellos que contengan «“UK”» se excluirán de los resultados de la búsqueda.

El operador «“+”» es idéntico al operador AND. Utilícelo para especificar explícitamente que es necesario que exista un término en un resultado de búsqueda. Por ejemplo, si busca «“+US UK gestión de riesgos”» (sin comillas), se devolverán registros que contengan «“US”». Sin embargo, dado que la búsqueda global utiliza por defecto el operador booleano AND, el uso del operador «“+”» no tiene ningún efecto a menos que se utilice con una sintaxis de búsqueda compleja como «“+US OR UK OR risk OR management”» (sin comillas).

El operador «“-”» es idéntico al operador NOT. Utilícelo para especificar explícitamente que es necesario excluir un término del resultado de búsqueda. Por ejemplo, la búsqueda «“-US UK risk management”» (sin comillas) devuelve todos los registros que contengan «“UK”», «“risk”» y «“management”» pero no contengan «“US”».

#### Agrupación

La búsqueda global admite los paréntesis para agrupar términos de búsqueda y formar sub-búsquedas.

Puede utilizar la agrupación para controlar y refinar los términos de búsqueda, especialmente con la lógica booleana. Por ejemplo, para buscar «“gestión de riesgos”» para «“US”» y «“UK”», especifique «“(US OR UK) AND gestión de riesgos”» (sin comillas). O, para buscar la frase gestión de riesgos y excluir «“EE.UU.”» o «“Reino Unido”», utilice «“-(EE.UU. O Reino Unido) «gestión de riesgos». ”»

#### Coincidencias aproximadas

Una coincidencia aproximada utiliza una virgulilla (~) para buscar un término de ortografía parecida a la de otras palabras.

Por ejemplo, para buscar un término similar a «“roam”», utilice «“roam˜”» (sin comillas). Esta búsqueda encuentra registros que contienen palabras como foam y «“roams”».

#### Proximidad

Utiliza una tilde (~) para buscar los términos de una frase que estén separados por `N` o menos palabras.

Por ejemplo, «“negocio de riesgo”»~10 (con comillas) encuentra registros que contienen las palabras «“riesgo”» y «“negocio ”» a 10 palabras de distancia o menos.

#### Aumento

La potenciación utiliza un acento circunflejo (^) para dar a algunos términos relevancia sobre otros.

Por ejemplo, la búsqueda «“gestión de riesgos US^5 UK”» (sin comillas) daría a los registros con «“US”» prioridad sobre los registros con «“UK”».

## Trabajar con archivos y enlaces

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-working-files-links)

Puede realizar muchas acciones en archivos y enlaces en OpenPages®.

### Acerca de archivos adjuntos

`Guía del usuario › Trabajar con archivos y enlaces` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-about-file-attachments)

Los archivos adjuntos se pueden añadir y gestionar en el repositorio de archivos de IBM OpenPages® .

Cuando se añaden archivos a OpenPages, se carga una copia del archivo en el repositorio de archivos. Los tipos de archivos que puede añadir están configurados para el sistema. Por ejemplo, puede añadir archivos PDF, archivos de texto, archivos gráficos y archivos de Microsoft Office.

OpenPages utiliza el control de versiones y el bloqueo de archivos en el repositorio de archivos. Cuando trabaja en un entorno de equipo de colaboración, los archivos se incorporan y se revisan para asegurarse de que un miembro del equipo no sobrescribirá los cambios realizados por otro miembro del equipo.

Los archivos se pueden añadir a OpenPages desde dos puntos de acceso:

- Utilice la tarea **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Archivos adjuntos** > **Archivos** para añadir y gestionar todos los archivos a los que tenga acceso, en todos los tipos de objetos.

  Para obtener más información, consulte [Adición y gestión de todos los archivos (adjuntos)](#añadir-y-gestionar-todos-los-archivos-adjuntos).
- Utilice la vista de tarea de un tipo de objeto para añadir y gestionar archivos adjuntos a objetos.

  Para obtener más información, consulte [Adición y trabajo con archivos (adjuntos) en objetos](#añadir-y-trabajar-con-archivos-adjuntos-en-objetos).

La funcionalidad es la misma excepto que con la tarea **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Archivos adjuntos** > **Archivos** se puede acceder a todos los archivos a través de todos los tipos de objetos. Las etiquetas de iconos son ligeramente diferentes en las dos tareas.

#### Reglas para la denominación de carpetas y archivos

`Guía del usuario › Trabajar con archivos y enlaces › Acerca de archivos adjuntos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=attachments-rules-naming-folders-files)

Se permiten caracteres especiales en determinados casos. Consulte la tabla siguiente para conocer las restricciones de caracteres especiales.

**Tabla 1. Restricciones de caracteres especiales**

| Carácter especial | Descripción | ¿Permitido en el nombre de carpeta? | ¿Permitido en el nombre de archivo? |
| --- | --- | --- | --- |
| & | Símbolo & | Sí | No |
| * | Asterisco | Sí | No |
| \ | Barra inclinada invertida | No | No |
| : | Dos puntos | Sí | No |
| " | Comillas dobles | Sí | No |
| ! | Signo de exclamación | Sí | No |
| / | Barra inclinada | No | No |
| > | Mayor que | Sí | No |
| < | Menor que | Sí | No |
| % | Porcentaje | Sí | No |
| \| | Área de conexión de memoria | Sí | No |
| # | Libra | Sí | No |
| ? | Signo de interrogación | Sí | No |
|  | un solo espacio | Sí | Sí |
|  | doble espacio | Sí, pero evítelo | No |

Para un nombre de carpeta,

- **Correcto**

  Reclamaciones y gestión de responsabilidad, Reclamaciones & Gestión de responsabilidad

- **Incorrecto**

  Reclamaciones \ Gestión de responsabilidad, Reclamaciones\Gestión de responsabilidad

### Añadir y trabajar con archivos (adjuntos) en objetos

`Guía del usuario › Trabajar con archivos y enlaces` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-adding-working-files-attachments-objects)

En función de cómo esté configurada la vista de tarea, es posible que pueda añadir archivos (archivos adjuntos) y trabajar con ellos.

#### Antes de empezar

Para trabajar con archivos adjuntos, debe tener acceso de lectura, escritura, asociación y supresión al tipo de objeto de archivo (`SOXDocument`).

#### Acerca de esta tarea

Cuando añade un archivo, se asocia con el objeto en la vista que tiene abierta.

Cuando añade un archivo, se carga una copia del archivo en el repositorio de archivos de OpenPages®. Después de añadir un archivo:

- Pulse el nombre del archivo para ver los detalles del archivo y acceder a varias versiones del archivo si existen.
- Pulse ![Icono Descargar archivo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_download_file.jpg) para descargarlo.

Pulse ![Icono de extracción de archivo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_checkout_file_icon.jpg) para extraer un archivo.

Un archivo reservado tiene las características siguientes:

- Se visualiza una marca de selección junto al nombre de archivo. Si está verde, lo ha incorporado. Si es azul, otro usuario lo ha extraído.
- El archivo está bloqueado y no se puede sobrescribir en el repositorio de archivos.
- Otros usuarios pueden ver y descargar la última versión reincorporada y todas las versiones anteriores del archivo.

El archivo también se puede asociar con otros objetos.

Al incorporar un archivo, puede añadir un comentario. Después de incorporar el archivo, el archivo se desbloquea y la nueva versión con los últimos cambios está disponible para otros usuarios para ver y extraer.

En el ejemplo siguiente, el archivo de la segunda fila tiene una marca de selección para indicar que el archivo se ha extraído.

![en una lista de archivos, una marca de selección junto a un archivo indica que se ha extraído](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_files_checkedout_tfui.png)

En función de cómo esté configurado el sistema, es posible que pueda abrir y editar archivos de Microsoft Office (Word, Excel y PowerPoint) directamente desde OpenPages. Si esta característica está habilitada, los iconos ![icono de vista](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_view_file_icon.jpg) (Ver) y ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_file_icon.jpg) (Editar) se muestran junto a los archivos de Microsoft Office.

En lugar de acceder a los archivos desde una Vista de tareas, también puede acceder a los archivos haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Anexos** > **Archivos**. Pulse el archivo que desea ver o editar. En una vista de tarea o de administración para el tipo de objeto Archivo, vaya a la sección **Versiones** . Para obtener más información, consulte [Adición y gestión de todos los archivos (adjuntos)](#añadir-y-gestionar-todos-los-archivos-adjuntos).

#### Procedimiento

1. Abra la tarea en la que desea trabajar.
2. Localice la sección que contiene archivos adjuntos.

   Por ejemplo, esta sección se podría denominar **Soporte de archivos y artefactos**.
3. Para añadir archivos al objeto:

   1. Pulse **Añadir/Actualizar** y seleccione el archivo. De forma alternativa, puede arrastrar archivos a la sección de archivos.
   2. Complete los campos de la ventana **Archivos a añadir** .
   3. Pulse **Cargar**.

      El archivo se añade y se incorpora automáticamente.

Después de añadir un archivo, puede utilizar dos métodos para cargar una nueva versión del archivo. Con cualquier método, si otro usuario ha extraído el archivo antes de intentar cargarlo, recibirá un mensaje de error al cargar el archivo.

1. Para actualizar un archivo utilizando la extracción manual:

   Utilice este método para evitar que otros usuarios editen el archivo mientras trabaja en los cambios.

   No utilice este método al editar archivos de Microsoft Office directamente desde OpenPages pulsando **Ver** o ![icono de vista](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_view_file_icon.jpg), o **Editar** o ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_file_icon.jpg).

   1. Pulse ![Icono de extracción de archivo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_checkout_file_icon.jpg) para extraer el archivo. Si el archivo ya está reservado, el icono está oculto.
   2. Descargue el archivo.
   3. Realice y guarde los cambios en el archivo.
   4. Pulse **Añadir/Actualizar** y seleccione el archivo. De forma alternativa, puede arrastrar el archivo a la sección de archivos.
   5. Complete los campos de la ventana **Archivos a añadir** .
   6. Pulse **Cargar**. La copia se carga y el archivo se incorpora.

   Puede pulsar ![icono para cancelar extracción de archivo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_cancelcheckout_file_icon.jpg) para cancelar una extracción. Si cancela una extracción, OpenPages revierte a la última versión seleccionada de un archivo en el repositorio de archivos.
2. Si está realizando cambios rápidos en un archivo, puede actualizar el archivo sin utilizar la extracción manual:

   > **Restricción:** No utilice este método al editar archivos de Microsoft Office directamente desde OpenPages pulsando **Ver** o ![icono de vista](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_view_file_icon.jpg), o **Editar** o ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_file_icon.jpg).

   1. Descargue el archivo.
   2. Realice y guarde los cambios en el archivo.
   3. Pulse **Añadir/Actualizar** y seleccione el archivo. De forma alternativa, puede arrastrar el archivo a la sección de archivos.
   4. Complete los campos de la ventana **Archivos a añadir** .
   5. Pulse **Cargar**. El archivo se extrae automáticamente y se devuelve.
3. Para ver un archivo de Microsoft Office cuando se visualiza el botón **Ver** o el icono ![icono de vista](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_view_file_icon.jpg), realice los pasos siguientes:

   1. Pulse **Ver** o ![icono de vista](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_view_file_icon.jpg).
   2. Pulse **Abrir [App]** en el recuadro de diálogo que abre la aplicación Microsoft Office.
   3. Vea el archivo.
   4. Si tiene los derechos para editar el archivo, puede editar el archivo aunque haya elegido verlo. Pulse **Habilitar edición** en la aplicación de Microsoft Office y empiece a realizar los cambios. El archivo se extrae automáticamente. Realice y guarde los cambios. Pulse **Incorporar** o ![Icono de incorporación](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_checkin_file_icon.jpg) para incorporar el archivo en OpenPages cuando haya terminado.

      Si aparece el siguiente mensaje al pulsar **Habilitar edición**, el archivo está bloqueado por otro usuario. Espere hasta que el archivo esté desbloqueado para realizar las ediciones. Sólo puede elegir la primera opción, **Ver una copia de sólo lectura**. Las otras dos opciones no funcionan.

      ![Un diálogo muestra un mensaje que indica que el archivo está bloqueado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_files_ms_lock_message.jpg)
4. Para ver un archivo de Microsoft Office cuando no se visualiza el botón **Ver** o el icono ![icono de vista](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_view_file_icon.jpg) , pulse **Editar** o ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_file_icon.jpg) y cancele la extracción o incorpore el archivo después de visualizarlo. Si no ve el botón **Editar** o el icono ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_file_icon.jpg) , descargue el archivo y ábralo manualmente.
5. Para abrir y editar un archivo de Microsoft Office:

   1. Pulse **Editar** o ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_file_icon.jpg).

      Se muestran dos recuadros de diálogo:

      - Un recuadro de diálogo OpenPages que le recuerda que debe incorporar el archivo cuando haya terminado.
      - Un recuadro de diálogo de Microsoft que abre la aplicación de Microsoft Office.
   2. Deje abierto el recuadro de diálogo OpenPages con el recordatorio hasta que haya terminado de editar el archivo. O bien, puede pulsar el botón **Cancelar extracción** en el recuadro de diálogo para cerrarlo. Al cerrar el recuadro de diálogo no se cancela la extracción. Recuerde incorporar el archivo cuando haya terminado.
   3. Pulse **Abrir [App]** en el recuadro de diálogo que abre la aplicación Microsoft Office.
   4. Pulse **Habilitar edición** en la aplicación Microsoft Office si la modalidad protegida está habilitada.

      Si aparece el siguiente mensaje al pulsar **Habilitar edición**, el archivo está bloqueado por otro usuario. Espere hasta que el archivo esté desbloqueado para realizar las ediciones. Sólo puede elegir la primera opción, **Ver una copia de sólo lectura**. Las otras dos opciones no funcionan.

      ![Un diálogo muestra un mensaje de que el archivo está bloqueado](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_files_ms_lock_message.jpg)
   5. Realice los cambios y guárdelos con frecuencia porque el guardado automático no está habilitado. Cuando guarde manualmente, los cambios se guardarán en el archivo del repositorio de archivos OpenPages . Sin embargo, otros usuarios no pueden ver los cambios hasta que se haya incorporado el archivo.
   6. Cuando haya terminado, pulse **Incorporar** en el recuadro de diálogo para incorporar el archivo.

      Si desea incorporar el archivo más adelante, puede pulsar **Incorporar más adelante**.

      > **Nota:** Si la sesión de OpenPages excede el tiempo de espera o si hay un problema de conectividad, es posible que reciba un mensaje que indique que el archivo no se ha podido guardar en el servidor. Para asegurarse de que el archivo se ha guardado, guarde localmente y pulse **Actualizar** para cargar manualmente el archivo en OpenPages.

### Añadir y gestionar todos los archivos (adjuntos)

`Guía del usuario › Trabajar con archivos y enlaces` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-adding-managing-all-files-attachments)

Utilice **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Archivos adjuntos** > **Archivos** para añadir y gestionar todos los archivos a los que tenga acceso, en todos los tipos de objetos. La tarea sólo muestra archivos que no son del sistema del tipo de objeto Archivo (SOXDocument). No visualiza archivos del sistema.

#### Acerca de esta tarea

En función de cómo esté configurado el sistema, es posible que pueda abrir y editar archivos de Microsoft Office (Word, Excel y PowerPoint) directamente desde OpenPages®. Si esta característica está habilitada, los botones **Vista** y **Editar** se muestran para los archivos de Microsoft Office (Word, Excel y PowerPoint).

También puede añadir archivos directamente a objetos utilizando una vista de tarea. Para obtener más información, consulte [Adición y trabajo con archivos (adjuntos) en objetos](#añadir-y-trabajar-con-archivos-adjuntos-en-objetos).

#### Procedimiento

1. Haz clic en " **Menú principal " ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Archivos adjuntos** > **Archivos**.
2. Para añadir archivos:

   1. Pulse **Nuevo**.

      Los campos y las etiquetas de botón pueden ser diferentes en función de cómo esté configurado el sistema.
   2. Opcional: Añada valores en **Palabras clave**.
   3. Opcional: Seleccione un **Tipo de documento**.
   4. Pulse **Añadir archivo** y seleccione el archivo. De forma alternativa, puede arrastrar un archivo a la página.
   5. Pulse **Seleccionar carpeta** y asocie el archivo a un objeto de negocio padre.
   6. Pulse **Guardar**.

      El archivo se añade y se incorpora automáticamente.

Después de añadir un archivo, hay dos métodos para cargar una nueva versión del mismo. Utilizando cualquiera de los dos métodos, recibirá un mensaje de error al subir el archivo si otro usuario lo ha extraído.

1. Para actualizar un archivo utilizando la extracción manual:

   Utilice este método para evitar que otros usuarios editen el archivo mientras trabaja en los cambios.

   No utilice este método al editar archivos de Microsoft Office directamente desde OpenPages pulsando **Ver** y **Editar**.

   1. Seleccione el archivo.
   2. Pulse **Extraer**. El icono está oculto si el archivo ya está extraído.
   3. Descargue el archivo.
   4. Realice y guarde los cambios en el archivo.
   5. Pulse **Actualizar** y seleccione el archivo. De forma alternativa, puede arrastrar el archivo a la página.
   6. Complete los campos de la ventana emergente **Archivos a actualizar** .
   7. Pulse **Cargar**. La copia se carga y el archivo se incorpora.

   Puede pulsar **Cancelar extracción** para cancelar una extracción. Si cancela una extracción, OpenPages revierte a la última versión seleccionada de un archivo en el repositorio de archivos.
2. Para actualizar un archivo sin utilizar la extracción manual:

   Utilice este método si realiza cambios rápidos en el archivo.

   No utilice este método al editar archivos de Microsoft Office directamente desde OpenPages pulsando **Ver** y **Editar**.

   1. Seleccione el archivo.
   2. Descargue el archivo.
   3. Realice y guarde los cambios en el archivo.
   4. Pulse **Actualizar** y seleccione el archivo. De forma alternativa, puede arrastrar el archivo a la página.
   5. Complete los campos de la ventana emergente **Archivos a actualizar** .
   6. Pulse **Cargar**. El archivo se extrae automáticamente y se devuelve.
3. Para ver un archivo de Microsoft Office:

   1. Seleccione el archivo.
   2. Pulse **Ver**.
   3. Pulse **Abrir [App]**, por ejemplo **Abrir Word**, en el recuadro de diálogo que abre la aplicación Microsoft Office.
   4. Vea el archivo.
   5. Es posible editar el archivo aunque haya elegido verlo, si tiene los derechos para editar el archivo. Pulse **Habilitar edición** en la aplicación de Microsoft Office y empiece a realizar los cambios. El archivo se extrae automáticamente. Realice y guarde los cambios. Pulse **Incorporar** para incorporar el archivo en OpenPages cuando haya terminado.

      Si aparece el siguiente mensaje al pulsar **Habilitar edición**, el archivo está bloqueado por otro usuario y no se puede editar. Debe esperar hasta que el archivo esté desbloqueado para realizar las ediciones. Sólo puede elegir la primera opción, **Ver una copia de sólo lectura**. Las otras dos opciones no funcionan.

      ![Un diálogo muestra un mensaje que indica que el archivo está bloqueado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_ug_files_ms_lock_message.jpg)
4. Para abrir y editar un archivo de Microsoft Office:

   1. Seleccione el archivo.
   2. Pulse **Editar**.

      Se muestran dos recuadros de diálogo:

      - Un recuadro de diálogo OpenPages que le recuerda que debe incorporar el archivo cuando haya terminado.
      - Un recuadro de diálogo de Microsoft que abre la aplicación de Microsoft Office.
   3. Deje abierto el recuadro de diálogo OpenPages con el recordatorio hasta que haya terminado de editar el archivo. O bien, puede pulsar el botón Cancelar en el recuadro de diálogo para cerrarlo. Al cerrar el recuadro de diálogo no se cancela la extracción. Pero debe recordar incorporar el archivo cuando haya terminado.
   4. Pulse **Abrir [App]**, por ejemplo **Abrir Word**, en el recuadro de diálogo que abre la aplicación Microsoft Office.
   5. Pulse **Habilitar edición** en la aplicación Microsoft Office. El archivo se extrae automáticamente.
   6. Realice los cambios y pulse guardar con frecuencia. Cada vez que guarde manualmente los cambios se guardarán en el archivo del repositorio de archivos de OpenPages . Sin embargo, otros usuarios no pueden ver los cambios hasta que se haya incorporado el archivo.

      > **Nota:** No puede guardar automáticamente en las aplicaciones de Microsoft Office.
   7. Incorpore el archivo cuando haya terminado. Puede pulsar **Incorporar** en el recuadro de diálogo que se ha visualizado anteriormente, si todavía está abierto. O bien, puede pulsar **Incorporar** en el archivo.

      > **Nota:** Si recibe un mensaje que indica que el archivo no se ha podido guardar en el servidor, guarde el archivo localmente y, a continuación, pulse **Actualizar** para cargar manualmente el archivo en OpenPages. Esto puede ocurrir si la sesión de OpenPages excede el tiempo de espera o si hay un problema de conectividad.

### Enlaces de URL externos

`Guía del usuario › Trabajar con archivos y enlaces` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-external-url)

Un enlace externo es un URL que abre una ventana de navegador y muestra el contenido de ese destino. Tanto si añade un enlace externo autónomo como si adjunta un enlace externo directamente a un objeto, se almacena una copia de ese enlace externo en el repositorio de archivos.

Puede añadir un enlace externo a un objeto.

#### Creación de enlaces de URL en objetos

`Guía del usuario › Trabajar con archivos y enlaces › Enlaces de URL externos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-creating-url-objects)

Un enlace externo es un URL que abre una ventana de navegador y muestra el contenido de ese destino. Una copia del enlace externo se almacena en el repositorio de archivos de IBM OpenPages® .

##### Procedimiento

1. Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Anexos** > **Enlaces**.
2. Pulse **Nuevo**.
3. Especifique un **Nombre**.
4. Especifique una **Descripción**.
5. Introduzca el valor de la URL en **URL**.
6. Adjunte el URL a un objeto.
7. Pulse **Guardar**.

## Trabajar con informes

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-working-reports)

IBM OpenPages® viene con una variedad de informes informativos y de excepción predefinidos, como informes de panel de control de resumen gráfico, informes de tareas específicos que se asignan a los usuarios, informes de supervisión de problemas e informes de gestión. Algunos informes también se pueden enlazar a subinformes, que contienen información más detallada en un área en particular. Los informes se pueden generar a petición en cualquier momento.

Ejemplo del uso de un Informe operativo - Desea descubrir qué tendencias de evento de pérdida había para la seguridad en el trabajo en un mes determinado. Puede seleccionar, por ejemplo, el *Informe de resumen de eventos de pérdida*. Se muestra un gráfico de la pérdida financiera, la pérdida no financiera y un recuento de eventos de pérdida para el mes seleccionado.

Para acotar el alcance de los datos devueltos para la seguridad en el trabajo, puede seleccionar la categoría Riesgo denominada Prácticas de empleo y Seguridad en el trabajo y una Categoría causal de personas.

Ejemplo de uso de un Informe financiero - Trabaja en controles financieros eficaces y no eficaces y desea ver todos los controles financieros eficaces y no eficaces para una división de la compañía. Puede seleccionar, por ejemplo el *Informe de eficacia operativa de controles financieros*. Para acotar el alcance de los datos de control devueltos para la división que desea, seleccione el nombre de la división en la página de solicitud de informe.

Dependiendo de la configuración, también puede seleccionar informes incorporados o listados en la página de inicio. Los informes se clasifican de la siguiente manera:

- Interactivo - Informes que le solicitan que seleccione o entre valores que filtren datos en el informe. Por ejemplo, estos informes le pueden solicitar que seleccione una entidad de negocios, un periodo de creación de informes o fechas de inicio y finalización. El informe limita el alcance de los datos devueltos. Informes que solicitan que una entidad de negocios devuelva datos sobre objetos por debajo de esa entidad.
- Estático - Informes que se generan tan pronto como pulsa el nombre del informe.

Puede acceder a una lista de informes disponibles añadiendo un panel **Informes** al panel de control. También puede añadir un informe a su cuadro de mandos creando una pestaña de informe. Para obtener más información, consulte [Añadir un panel Informes](#adición-de-un-panel-de-informes) y [Añadir un informe o una ficha personalizada](#añadir-un-informe-o-una-ficha-personalizada).

### Acerca de los informes

`Guía del usuario › Trabajar con informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-about)

Este tema proporciona enlaces a información sobre los informes.

- [Trabajar con informes](#trabajar-con-informes)
- [Enviar un informe por correo electrónico](#enviar-un-informe-por-correo-electrónico)
- [Generar y visualizar informes](#generar-y-visualizar-informes)
- [Visualizar informes en un formato diferente](#visualizar-informes-en-un-formato-diferente)

### Generar y visualizar informes

`Guía del usuario › Trabajar con informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-generating-viewing)

Puede abrir un informe desde el elemento de menú **Analítica** o desde un panel o pestaña de su cuadro de mandos.

#### Acerca de esta tarea

Puede acceder a una lista de informes disponibles añadiendo un panel **Informes** al panel de control. También puede añadir un informe a su cuadro de mandos creando una **pestaña Informe**. Para obtener más información, consulte [Añadir un panel Informes](#adición-de-un-panel-de-informes) y [Añadir un informe o una ficha personalizada](#añadir-un-informe-o-una-ficha-personalizada).

En función de la configuración, **Análisis** puede mostrarse como el primer elemento de menú en el menú principal. Haga clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Analítica** para abrir IBM® Cognos Analytics, donde podrá trabajar con los informes.

#### Procedimiento

1. Pulse en el nombre del informe.
2. En informes interactivos, complete todos los campos y selecciones necesarios.
3. Haga clic en **Finalizar** para generar el informe.

### Enviar un informe por correo electrónico

`Guía del usuario › Trabajar con informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-emailing-report)

Si el sistema está configurado, puede generar un informe y enviarlo por correo electrónico.

#### Procedimiento

1. En el informe generado, pulse el enlace **Mantener esta versión** .
2. Pulse **Enviar informe por correo electrónico**.
3. En la ventana **Establecer las opciones de correo electrónico** , escriba una dirección de correo electrónico en el recuadro Para.
4. Para enviar el informe a varias direcciones, separe cada dirección con un punto y coma (;).
5. Escriba una línea de asunto y un mensaje.
6. Seleccione si el informe se envía como un archivo adjunto o como un enlace.
7. Pulse **Aceptar**.

### Visualizar informes en un formato diferente

`Guía del usuario › Trabajar con informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-viewing-in-different-format)

Si el sistema está configurado para mostrar informes en diferentes formatos, puede generar un informe y, a continuación, visualizarlo o guardarlo en otro formato. El formato estándar es HTML.

#### Procedimiento

1. Abra el informe.
2. Si está viendo el informe en OpenPages®, pulse **Ver como** y seleccione un formato.

   *Figura 1. Selección de un formato de informe en OpenPages![Se muestra el menú Ver como en OpenPages . Las opciones del menú son HTML, PDF, Excel y Datos de Excel.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_export_formats.png)*

   O, si está viendo el informe en Cognos®, pulse **HTML** y seleccione un formato.

   > **Sugerencia:** Para descargar el informe como un archivo formateado de Microsoft Excel, utilice **Excel**. Para descargar el informe como un archivo sin formato, elija **Datos de Excel**.

   *Figura 2. Selección de un formato de informe en Cognos![Se muestra el menú de formato de informe en Cognos . La opción HTML está seleccionada de forma predeterminada. Las otras opciones del menú son PDF, Excel y Excel Data, CSV y XML.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/cognos_export_formats.png)*
3. Siga las indicaciones de la pantalla.

## Cuestionarios

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-questionnaires)

Utilice cuestionarios para evaluar el riesgo y el cumplimiento o para recopilar información para procesos específicos y riesgos de activos. IBM OpenPages® agiliza, estandariza y centraliza la recopilación de información de evaluación basada en cuestionarios.

### Resumen del cuestionario

`Guía del usuario › Cuestionarios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=questionnaires-questionnaire-overview)

Obtenga información sobre la característica del cuestionario y, a continuación, configúrela para su organización.

Las evaluaciones de cuestionario se utilizan en los objetos siguientes:

- Activos
- Plantillas de cuestionario
- Programas
- evaluaciones de cuestionarios

Los activos son los objetos existentes que las evaluaciones de cuestionario evalúan y miden. Pueden ser recursos, procesos, subprocesos, empleados, proveedores o compromisos. Las plantillas de cuestionario se utilizan para diseñar y escribir las preguntas. Los programas se utilizan para definir, iniciar y distribuir evaluaciones de cuestionario a encuestados. También puede crear evaluaciones de cuestionario ad hoc, que son evaluaciones de cuestionario individuales que son independientes de los programas.

Las evaluaciones de cuestionario se mueven a través de un proceso de revisión. El proceso de revisión se gestiona en segundo plano mediante GRC Workflow. Para asegurarse de que el proceso de revisión se gestiona correctamente, debe especificar un valor para los campos de ciclo de vida y de fecha de vencimiento para las evaluaciones de programas y cuestionario. El valor del campo de ciclo de vida puede ser **Ciclo de vida de 2 fases (sin revisión)**, **Ciclo de vida de 3 fases (con revisión)**o **Ciclo de vida de 4 fases (con revisión y aprobación)**.

Para obtener más información sobre GRC Workflow, consulte la publicación *IBM OpenPages Guía del administrador*.

Para configurar y utilizar evaluaciones de cuestionario:

1. Planifique las evaluaciones de cuestionario y los programas que desea crear. Decida qué recursos desea medir, el flujo de trabajo que desea que siga y el programa que desea utilizar para iniciarlo.
2. Trabaje con su administrador para determinar qué flujo de trabajo se utiliza para dirigir el proceso de revisión. Revise el flujo de trabajo y asegúrese de que comprende las etapas del proceso de revisión.
3. Planifique el contenido de la plantilla de cuestionario (secciones, subsecciones y preguntas) y la puntuación.

   Cuando planifique el contenido, tenga en cuenta que IBM recomienda los siguientes límites máximos en los elementos de una plantilla de cuestionario:

   - 1000 preguntas por plantilla de cuestionario
   - 199 subsecciones y preguntas por sección
   - 50 preguntas, incluidas preguntas dependientes, por subsección
4. Cree un objeto de plantilla de cuestionario.
5. Edite la plantilla de cuestionario para añadir contenido a la misma.
6. Si no existen, cree los activos (recursos, procesos, subprocesos, empleados, proveedores o compromisos) que mide la evaluación de cuestionario. Identifique los propietarios de los activos.
7. Cree un programa. Asígnele la plantilla de cuestionario, un ciclo de vida y activos. Inícielo. El sistema crea las evaluaciones de cuestionario y envía un correo electrónico con un enlace a los encuestados. Empieza el flujo de trabajo en las evaluaciones de cuestionario y la primera fase se establece en la fase de recopilación de información.
8. Cree cuestionarios ad hoc. Para obtener más información, consulte [Creación de una evaluación de cuestionario ad hoc](#creación-de-una-evaluación-de-cuestionario-ad-hoc).
9. Los encuestados reciben las evaluaciones de cuestionario y las responden. A medida que trabajan, el sistema calcula su progreso y sus puntuaciones de conformidad y de riesgo. Los revisores pueden ver esta información y supervisar su progreso.
10. Los encuestados terminan las respuestas y envían sus evaluaciones de cuestionario. Las evaluaciones de cuestionario pasan por el flujo de trabajo hasta que se cierran.
11. Ejecute los informes de cuestionario para revisar las puntuaciones, el progreso y las respuestas. Hay disponibles dos informes de cuestionario:

    - Informe de programa
    - Informe de evaluación único

Las plantillas de cuestionario, los recursos y los programas deben estar en el periodo de elaboración de informes actual. El sistema emitirá un mensaje si un encuestado abre una evaluación de cuestionario asignada a un recurso que esté en un periodo de elaboración de informes distinto al periodo de elaboración de informes actual. También emitirá un mensaje si se inicia una plantilla de cuestionario o un programa que esté en un periodo de elaboración de informes distinto al periodo de elaboración de informes actual.

#### Puntuación de la plantilla de cuestionario y métodos de puntuación

`Guía del usuario › Cuestionarios › Resumen del cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=overview-questionnaire-template-scores-scoring-methods)

El sistema calcula la puntuación de conformidad y la puntuación de riesgo cuando un encuestado completa una evaluación de cuestionario. Cómo se calculan estas puntuaciones depende del método de puntuación, promedio del riesgo ponderado o simple, que asigna a una plantilla de cuestionario.

Utilice el método simple si el centro de la plantilla de cuestionario está a nivel de pregunta. La ponderación de pregunta define la importancia de cada pregunta. Para ocultar todas las puntuaciones de ponderación y respuesta, inhabilite **Ponderación y puntuación** en los **valores de Formato** de la plantilla de cuestionario.

Utilice el método de media ponderada si el foco de la plantilla de cuestionario está a nivel de subsección. Utilice este método si algunas subsecciones tienen una importancia mayor que otras subsecciones. La diferencia entre los dos métodos es que el método simple no calcula una media ponderada en el nivel de subsección, lo que afecta a los resultados generales en las puntuaciones de conformidad y de riesgo.

Para planificar la puntuación de una plantilla de cuestionario, realice los pasos siguientes:

- Decida si desea utilizar el método de media ponderada o simple.
- Decida qué ponderación asignar a cada sección y subsección y sea coherente.
- Decida qué puntuaciones de respuesta desea aplicar a las preguntas de respuesta única o múltiple. Utilice una puntuación de respuesta mayor para las mejores respuestas; por ejemplo, emplee el 10 para la mejor respuesta. Mantenga el intervalo tan pequeño como pueda; por ejemplo, del 1 al 10. Utilice un intervalo mayor solo si una pregunta tiene muchas respuestas; por ejemplo, más de 10.

  La puntuación para las respuestas a una pregunta de varias opciones se calcula utilizando la siguiente fórmula, donde `answerSum` es la suma de las puntuaciones de las respuestas elegidas por el encuestado y `maxScore` es la suma de todas las respuestas posibles:

  ```
  score = (answerSum * 10 * weight) / maxScore
            
  ```

  En el ejemplo siguiente, tiene una pregunta de varias respuestas con una ponderación de `1` y A, B, C y D como posibles respuestas.

  **Tabla 1.**

  | Respuesta | Puntuación |
  | --- | --- |
  | A | 10 |
  | B | 2 |
  | C | 1 |
  | D | 0 |

  En este escenario, `maxScore = 13`. Si el encuestado elige las respuestas B y C, entonces `answerSum = 3`. Utilizando la fórmula, `score = 2.31`.
- Considere cómo se puntúan las preguntas dependientes. La respuesta de un encuestado a una pregunta de control puede hacer que se oculte una pregunta dependiente. Solo las preguntas visibles para el encuestado se incluyen en la puntuación. Aquellas preguntas ocultas al encuestado, se excluyen.
- Tenga en cuenta que las preguntas de texto largo, texto breve y tabla están excluidas de la puntuación.

Para obtener más información sobre las fórmulas que se utilizan en la puntuación, consulte [Fórmulas de puntuación de plantilla de cuestionario](#fórmulas-de-puntuación-de-la-plantilla-de-cuestionario).

#### Fórmulas de puntuación de la plantilla de cuestionario

`Guía del usuario › Cuestionarios › Resumen del cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=overview-questionnaire-template-scoring-formulas)

Cuando un encuestado está respondiendo a una evaluación de cuestionario, el sistema calcula y actualiza la puntuación de conformidad y la puntuación de riesgo cada vez que se guarda. El sistema también calcula la puntuación total y la puntuación máxima pero el encuestado no las puede visualizar. Para calcular dichos valores, el sistema utiliza fórmulas que consideran el método de puntuación del cuestionario y los valores que se proporcionan en la plantilla del cuestionario.

En una plantilla de cuestionario se proporcionan los valores siguientes:

**Tabla 1. Puntuaciones y ponderaciones de la plantilla de cuestionario**

| Código | Nombre | Valor |
| --- | --- | --- |
| QW | Peso de la pregunta | **0** - **9999**, **0** excluye la pregunta |
| AS | Puntuación de respuesta | **-1** a **9999**, **-1** excluye la respuesta |
| SW | Peso de la sección | **0** - **9999**, **0** excluye la sección |
| SSW | Peso de la subsección | **0** - **9999**, **0** excluye la subsección |

El sistema utiliza las siguientes fórmulas:

**Tabla 2. Fórmulas de puntuación**

| Código | Nombre | Fórmula |
| --- | --- | --- |
| QS | Puntuación de la pregunta | 0-10, la fórmula depende de si una pregunta es de opción única o de varias opciones. ^{1} |
| WQS | Puntuación de la pregunta ponderada | QS * QW |
| SSS | Puntuación de subsección para puntuación total | La fórmula depende del método de puntuación del cuestionario. ^{2} |
| MSSS | Puntuación de subsección para puntuación máxima | La fórmula depende del método de puntuación del cuestionario. ^{3} |
| SS | Puntuación de la sección | SS = SW * SUM (SSS) |
| TS | Puntuación total | TS = Sum SS |
| MS | Puntuación máxima | MS = Suma MSSS |
| CS | Puntuación de conformidad | CS = [TS / MS] *100 |
| RS | Puntuación de riesgo | RS = MS – TS |

##### Cómo calcula el sistema las puntuaciones de las preguntas^{1}

Las puntuaciones del cuestionario se calculan para las preguntas de opción única utilizando la fórmula siguiente:

```
QS = [AS / MAX(AS)] * 10
```

Las puntuaciones de cuestionario se calculan para preguntas de varias opciones utilizando la fórmula siguiente:

```
QS = [SUM(Selected AS) / SUM(All AS)] * 10 
```

Para texto corto, texto largo y preguntas de tabla, no se calcula ninguna puntuación de pregunta.

##### Cómo calcula el sistema las puntuaciones de las subsecciones para la puntuación total^{2}

Cuando el método de puntuación es simple, las puntuaciones de las subsecciones se calculan para la puntuación total utilizando la fórmula siguiente:

```
SSS = SSW * SUM(WQS)
```

Cuando el método de puntuación es el promedio ponderado, las puntuaciones de las subsecciones se calculan para la puntuación total utilizando la fórmula siguiente:

```
SSS = SSW * [SUM(WQS) / SUM(QW) * 10]    
```

##### Cómo calcula el sistema las puntuaciones de las subsecciones para la puntuación máxima^{3}

El número máximo de preguntas de `10` se utiliza para calcular puntuaciones de las subsecciones para la puntuación máxima.

Cuando el método de puntuación es simple, las puntuaciones de las subsecciones se calculan para la puntuación máxima utilizando la fórmula siguiente:

```
MSSS = SSW * [SUM(QW * 10)]
```

Cuando el método de puntuación es el promedio ponderado, las puntuaciones de las subsecciones se calculan para la puntuación máxima utilizando la fórmula siguiente:

```
MSSS = SSW * 10 
```

### Plantillas de cuestionario

`Guía del usuario › Cuestionarios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=questionnaires-questionnaire-templates)

Las plantillas de cuestionario se utilizan en programas para iniciar evaluaciones de cuestionario. Contienen preguntas organizadas en secciones y subsecciones. Los encuestados responden a las preguntas de las evaluaciones de cuestionario.

Antes de utilizar plantillas de cuestionario, consulte [Visión general del cuestionario](#resumen-del-cuestionario).

#### Creación de un objeto de plantilla de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-creating-questionnaire-template-object)

Las plantillas de cuestionario contienen las preguntas que responden los encuestados cuando completan una evaluación de cuestionario.

Para crear un cuestionario nuevo, puede empezar con un cuestionario en blanco o con una copia de un cuestionario existente.

##### Procedimiento

1. Abra el **Menú primario** y seleccione **Evaluaciones** > **Plantillas de cuestionario**.
2. Pulse **Nuevo**.
3. Complete la siguiente información en el formulario para crear el nuevo objeto de cuestionario:

   1. En el cuadro **Nombre** , especifique el nombre de la plantilla de cuestionario.
   2. En el recuadro **Descripción** , especifique la descripción de la plantilla de cuestionario.
   3. En el recuadro desplegable **Método de puntuación de cuestionario** , puede dejar el valor predeterminado, **Simple**, o seleccionar el método **Promedio de ponderación**.
   4. En el recuadro desplegable **Propietario principal** , seleccione un usuario de la lista de nombres **Utilizados recientemente** o especifique un nombre y seleccione en la lista de usuarios que se muestra. De forma similar, puede especificar un **Revisor** y un **Aprobador**.
   5. Pulse **Seleccionar carpeta**, seleccione una carpeta en el recuadro de diálogo y pulse **Terminado**.
4. Cuando haya terminado de completar el formulario, pulse **Guardar**.

   La página **Plantilla de cuestionario** se abre en la pestaña **Tarea**.
5. Pulse la pestaña **Editor** .
6. Para copiar las preguntas y los valores de una plantilla de cuestionario existente, pulse el mosaico **Desde plantilla** .

   En el cuadro de diálogo **Seleccionar cuestionario para copiar** , seleccione un cuestionario que desea copiar y haga clic en **Hecho**.

   Omita los pasos 7 a 9.

   > **Importante:**

   > Si ya existe una copia de una plantilla en la carpeta actual, asegúrese de crear cada copia posterior en su propia carpeta. Si no especifica una carpeta diferente, la segunda copia en la misma carpeta se creará a partir de la primera copia, en lugar de la plantilla original.
7. Para empezar desde un cuestionario en blanco, pulse el mosaico **En blanco** .
8. Complete la información del recuadro de diálogo **Valores de formato** .

   1. En el recuadro **Primera sección de nombre** , especifique el nombre de la primera sección en la plantilla de cuestionario.
   2. En el recuadro **Nombre de la primera subsección** , especifique el nombre de la primera subsección en la plantilla de cuestionario.
   3. Establezca **Títulos** en **Activado** si desea añadir más contexto para sus preguntas. Cuando **Títulos** se establece en **Off**, se necesitan títulos para cada pregunta.
   4. Establezca **Numeración automática** en **Activado** si desea que las preguntas se numeren en secuencia.
   5. Deje el valor predeterminado de **Activado** para **Ponderación y puntuación** si desea poder añadir ponderación y puntuación a preguntas, subsecciones y secciones.
9. Pulse **Crear**.

   La página **Plantilla de cuestionario** se abre en la pestaña **Editor**. Muestra la primera sección y subsección que ha añadido en el último paso. En el panel de navegación, tanto **Total de secciones** como **Total de preguntas** muestran que hay una sección y una pregunta.

##### Qué hacer a continuación

Ahora puede editar la nueva plantilla. Para más información, véase [Editar una plantilla de cuestionario](#edición-de-una-plantilla-de-cuestionario).

#### Edición de una plantilla de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-editing-questionnaire-template)

Después de crear una plantilla de cuestionario, puede editarla para añadir secciones, subsecciones y preguntas.

Para obtener más información sobre cómo crear un cuestionario, consulte [Creación de un objeto de plantilla de cuestionario](#creación-de-un-objeto-de-plantilla-de-cuestionario).

Cualquier persona que pueda acceder a una plantilla de cuestionario también puede editarla.

> **Nota:** Puede cambiar una plantilla de cuestionario hasta que se inicie con un programa y se envíe a los encuestados. A partir de entonces, el sistema la bloquea y solo los usuarios con las credenciales adecuadas pueden desbloquearla, editarla y volver a bloquearla. Los cambios surten efecto de forma inmediata.

##### Antes de empezar

Planifique el contenido de la plantilla del cuestionario y decida qué método utilizar para la puntuación. Para obtener más información, consulte [Puntuación de plantillas de cuestionario y métodos de puntuación](#puntuación-de-la-plantilla-de-cuestionario-y-métodos-de-puntuación).

##### Acerca de esta tarea

Para empezar a editar una plantilla de cuestionario, debe estar en la pestaña **Editor** de la página **Plantilla de cuestionario**. Si todavía no está en la página **Plantilla de cuestionario** , realice los pasos siguientes:

1. Abra el **Menú principal** y seleccione **Evaluaciones** > **Plantillas de cuestionario**.
2. Pulse el nombre de la plantilla de cuestionario que desea editar.
3. Pulse la pestaña **Editor**.

> **Nota:** Si ha actualizado desde una versión anterior de IBM OpenPages®, elimine todas las referencias al campo **AuthQuest** de todos los perfiles. Este campo puede causar confusión porque dirige a los usuarios a una versión anterior de la interfaz de usuario de creación de plantillas de cuestionario.

##### Procedimiento

1. Opcional: Pulse **Introducción** en el panel izquierdo.

   Edite la introducción que los encuestados ven cuando reciben el cuestionario.

   - Puede editar **Título** y **Descripción** de la plantilla de cuestionario que ha especificado al crear el objeto de plantilla de cuestionario.

     El número máximo de caracteres permitidos para el campo **Título** es 4000.

     El número máximo de caracteres permitidos para el campo **Descripción** es 2048.
   - Si desea utilizar un logotipo para todas las plantillas de cuestionario, copie el archivo .png en `<OP_HOME>/wlp-usr/shared/apps/op-apps.ear/taskui.war/` `images/questionnaire` y especifique el nombre del archivo .png en el recuadro **Logotipo personalizado** .

     La imagen del logotipo no debe ser mayor de 350 x 200 píxeles.

   Si desea editar la **Declaración de limitación de responsabilidad**, modifique el texto de la aplicación **questionnaire.intro.label.informationDetails**. El número máximo de caracteres permitidos para el campo **Declaración de limitación de responsabilidad** es 4000. Para obtener más información sobre cómo modificar el texto de la aplicación, consulte [Modificación del texto de la aplicación](3.3-guia-del-administrador.md#modificación-del-texto-de-la-aplicación).
2. Cree las secciones y las subsecciones. Para obtener más información, consulte [Adición de secciones y subsecciones a una plantilla de cuestionario](#añadido-de-secciones-y-subsecciones-a-una-plantilla-de-cuestionario).
3. Escriba las preguntas. Para obtener más información, consulte [Adición de preguntas a una plantilla de cuestionario](#añadido-de-preguntas-a-una-plantilla-de-cuestionario).
4. Revise la plantilla de cuestionario y edítela según sea necesario.

   Si desea cambiar los valores de **Títulos**, **Numeración automática** y **Ponderación y puntuación** que ha especificado al crear la plantilla, pulse **Valores de formato** en el panel izquierdo.

##### Qué hacer a continuación

El paso siguiente es iniciar la plantilla de cuestionario con un programa. Para obtener más información, consulte [Inicio de un programa](#lanzamiento-de-un-programa).

#### Añadido de secciones y subsecciones a una plantilla de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-adding-sections-subsections-questionnaire-template)

Las secciones y subsecciones proporcionan la estructura a una plantilla de cuestionario.

##### Antes de empezar

Cree una plantilla de cuestionario y planifique cómo se organizarán las secciones y subsecciones y su ponderación para la puntuación. Para obtener más información, consulte [Creación de un objeto de plantilla de cuestionario](#creación-de-un-objeto-de-plantilla-de-cuestionario).

##### Acerca de esta tarea

Utilice esta tarea para añadir, editar y suprimir secciones y subsecciones de una plantilla de cuestionario.

Para empezar a editar una plantilla de cuestionario, debe estar en la pestaña **Editor** de la página **Plantilla de cuestionario**. Si todavía no está en la página **Plantilla de cuestionario** , realice los pasos siguientes:

1. Abra el **Menú principal** y seleccione **Evaluaciones** > **Plantillas de cuestionario**.
2. Pulse el nombre de la plantilla de cuestionario que desea editar.
3. Pulse la pestaña **Editor**.

##### Procedimiento

1. Para añadir una sección, pulse **Nueva sección** en el panel izquierdo.

   Aparece el recuadro de diálogo **Nueva sección**.
2. Especifique un **Título**. Este valor se mostrará en la evaluación de cuestionario.
3. Escriba el nombre de la primera subsección en el campo **Nombre de la primera subsección** .
4. Especifique una **Descripción**. Este valor se mostrará en la evaluación de cuestionario.
5. Si **Peso y puntuación** está habilitado en **Valores de formato**, puede especificar un valor **0** - **9999** en **Peso**. Especifique **0** para excluir todas las preguntas de la sección de la puntuación. La ponderación no se muestra en la evaluación del cuestionario.
6. Especifique una referencia de . Este valor no se mostrará en la evaluación de cuestionario.
7. Escriba una **Rationale**. Este valor no se mostrará en la evaluación de cuestionario.
8. Pulse **Crear**. El sistema crea la sección, subsección y una pregunta predeterminada. La sección se añade al final de la plantilla. Ahora puede añadir más subsecciones a la misma.
9. Para añadir una subsección, expanda la sección a la que desea añadir una subsección y pulse **+** que aparece después de la última subsección de la sección.
10. Complete todos los campos de la subsección. Son los mismos que para una sección excepto para el requisito de un nombre de subsección porque las subsecciones sólo pueden contener preguntas.
11. Pulse **Crear**. El sistema añade la subsección y una pregunta predeterminada al final de la sección.
12. Añada más secciones y subsecciones según sea necesario.
13. La barra de estado del panel izquierdo muestra cuántas secciones y preguntas están en la plantilla de cuestionario.
14. Para cambiar el orden de las secciones o subsecciones, pulse **Mover y reordenar elementos** en el panel de navegación, arrastre el elemento que desea mover a su nueva ubicación y pulse **Guardar**.

    Puede desplazar una subsección hacia arriba o hacia abajo en la sección o puede moverla a otra sección.
15. Para editar una sección o subsección, pulse el icono de lápiz situado a la derecha del nombre de sección o subsección en el panel derecho, especifique los cambios y pulse **Terminado**.
16. Para suprimir una sección o subsección, pulse el icono de papelera a la derecha de la sección o el nombre de subsección en el panel derecho, y confirme la supresión cuando se le solicite.

    Cuando se suprime una sección, las subsecciones y las preguntas también se suprimen. Cuando se suprime una subsección, las preguntas que contiene también se suprimen.
17. Para dejar de trabajar en la plantilla de cuestionario, cierre la pestaña de plantilla.

    La plantilla se guarda automáticamente.

##### Qué hacer a continuación

El siguiente paso es añadir preguntas a las subsecciones. Para obtener más información, consulte [Adición de preguntas a una plantilla de cuestionario](#añadido-de-preguntas-a-una-plantilla-de-cuestionario).

#### Añadido de preguntas a una plantilla de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-adding-questions-questionnaire-template)

Las preguntas especifican la información que desea que proporcionen los encuestados.

##### Antes de empezar

Añadir secciones y subsecciones a la plantilla de cuestionario. Para obtener más información, consulte [Adición de secciones y subsecciones a una plantilla de cuestionario](#añadido-de-secciones-y-subsecciones-a-una-plantilla-de-cuestionario).

##### Acerca de esta tarea

Utilice esta tarea para añadir, editar y suprimir preguntas de una plantilla de cuestionario.

Para empezar a editar una plantilla de cuestionario, debe estar en la pestaña **Editor** de la página **Plantilla de cuestionario**. Si todavía no está en la página **Plantilla de cuestionario** , realice los pasos siguientes:

1. Abra el **Menú principal** y seleccione **Evaluaciones** > **Plantillas de cuestionario**.
2. Pulse el nombre de la plantilla de cuestionario que desea editar.
3. Pulse la pestaña **Editor**.

##### Procedimiento

1. En el panel de navegación, pulse la sección y, a continuación, la subsección a la que desea añadir una pregunta.

   Sólo puede añadir preguntas a una subsección, no a una sección.
2. En el panel derecho, desplácese hasta el final de la subsección y pulse **Nueva pregunta**.

   Aparece el recuadro de diálogo **Configurar pregunta**.
3. Seleccione el **Tipo** de respuesta.

   - **Opción única**

     El encuestado puede elegir sólo una respuesta de una lista que proporcione. Puede hacer que otras preguntas dependan de la respuesta elegida.
   - **Varias opciones**

     El encuestado puede elegir una o más respuestas de una lista que proporcione. Puede hacer que otras preguntas dependan de las respuestas elegidas.
   - **Texto corto**

     El encuestado puede especificar hasta 252 caracteres de texto. Las preguntas de texto breve no tienen puntuación de respuesta y se excluyen de la puntuación.
   - **Texto largo**

     El encuestado puede especificar hasta 2048 caracteres de texto. Las preguntas de texto largo no tienen puntuación de respuesta y se excluyen de la puntuación.
   - **Respuesta de la tabla**

     El encuestado puede añadir hasta 30 filas a la tabla y escribir hasta 50 caracteres por celda. Las preguntas de las respuestas de la tabla no tienen puntuación de respuesta y se excluyen de la puntuación.
4. Seleccione **Obligatorio** si el encuestado debe responder a la pregunta.
5. Si **Peso y puntuación** está habilitado en **Valores de formato**, puede especificar un valor **0** - **9999** en **Peso**. Especifique **0** para excluir una pregunta de la puntuación. No se mostrará en la evaluación de cuestionario.
6. Si **Títulos** está habilitado en **Valores de formato**, puede especificar un **Título**. Este valor se mostrará en la evaluación de cuestionario.
7. Especifique la **Pregunta** que el encuestado necesita responder, hasta un límite de 2048 caracteres. Este valor se mostrará en la evaluación de cuestionario.
8. Si elige **Opción única** o **Selección múltiple** como **Tipo** de respuesta, especifique las respuestas que los encuestados pueden elegir en la lista **Respuestas** . Pulse **Nueva respuesta** para añadir más respuestas.

   Para una pregunta de opción múltiple, puede establecer una o más de las respuestas como **Exclusiva**, lo que significa que el encuestado no puede seleccionar ninguna otra respuesta para la pregunta después de seleccionar una de las respuestas exclusivas.

   Por ejemplo, una pregunta tiene las respuestas siguientes: "A", "B" y "Ninguno de los anteriores". Si establece la respuesta "Ninguna de las anteriores" en **Exclusiva**, el encuestado puede elegir, o ambas, "A" y "B". Sin embargo, si el encuestado elige "Ninguna de las anteriores", no puede elegir ninguna otra respuesta.

   Si **Ponderación y puntuación** está habilitado en los **valores de Formato**, puede especificar una puntuación para cada respuesta. Especifique una **Puntuación** de entre **-1** y **9999**. Introduzca **-1** para las respuestas que desee excluir de la puntuación.

   Por ejemplo, una respuesta de "Ninguno de los anteriores" se puede puntuar **-1**. Utilice una puntuación de respuesta más alta para obtener mejores respuestas. Por ejemplo, utilice **10** para obtener la mejor respuesta. Utilice un rango coherente y manténgalo lo más pequeño posible, como por ejemplo **1** - **10**. Utilice un rango más grande sólo si una pregunta tiene muchas respuestas. Cuando se calcula la puntuación, las puntuaciones de preguntas se normalizan **1** - **10**.
9. Si elige **Tabla** en **Tipo**, especifique el texto de cabecera de columna en **Columna**. Pulse **Nueva columna** para añadir más columnas. Una respuesta de tabla puede tener hasta 15 columnas. Si la pregunta es obligatoria, el encuestado debe especificar una fila de información. Las preguntas de respuesta de tabla pueden ser preguntas dependientes, pero no pueden estar controlando las preguntas. Para fines de elaboración de informes, las respuestas de tabla se conservan en formato CSV con la barra vertical como delimitador.
10. Opcional: Si eligió **Opción única**,**Opción múltiple**, **Texto corto** o **Texto largo** como **Tipo** de respuesta, puede rellenar las respuestas a la pregunta con los valores de un campo cuando se ejecuta una evaluación.

    Por ejemplo, para una pregunta de una sola opción, puede rellenar las respuestas con los valores del campo Departamento del tipo de objeto Empleado.

    Para obtener más información sobre cómo rellenar las respuestas a una pregunta con los valores de un campo, consulte [Asociar respuestas a un campo](#asociar-respuestas-a-un-campo).
11. Opcional: puede configurar dependencias para la pregunta. El hecho de que una pregunta dependiente se oculte o se muestre en una evaluación depende de las respuestas del encuestado a otras preguntas o de los valores de los campos. Para obtener más información sobre la configuración de dependencias, consulte [Creación de dependencias de preguntas](#creación-de-dependencias-de-preguntas).
12. Opcional: Expanda la sección **Contexto adicional** y realice los pasos siguientes:

    - Introduzca una **Justificación** para la pregunta. Puede introducir hasta 4000 caracteres. Este valor no se mostrará en la evaluación de cuestionario.
    - En **Referencia**, introduzca una URL para el material de referencia relacionado. Este valor no se mostrará en la evaluación de cuestionario.
    - Seleccione **Mostrar comentarios** para habilitar los comentarios. Todos los tipos de pregunta pueden tener comentarios. Si está habilitado, el encuestado puede proporcionar varios comentarios. **Mostrar comentarios** está seleccionado de forma predeterminada.

      Si el encuestado debe proporcionar al menos un comentario, seleccione **Comentario necesario**. Si se requiere un comentario, la respuesta se marca como incompleta hasta que el encuestado añade un comentario.
    - Seleccione **Mostrar archivos adjuntos** para habilitar los archivos adjuntos. Todos los tipos de pregunta pueden tener archivos adjuntos. Si está habilitado, el encuestado puede proporcionar varios archivos adjuntos. **Mostrar archivos adjuntos** está seleccionado de forma predeterminada.

      Si el encuestado debe proporcionar al menos un archivo adjunto, seleccione **Archivo adjunto necesario**. Si se requiere un archivo adjunto, la respuesta se marca como incompleta y no se anota hasta que el encuestado añade un archivo adjunto.
13. Opcional: Expanda la sección **Asociaciones** . Para añadir asociaciones, pulse el tipo de objeto que desea asociar a la pregunta y, a continuación, pulse **Añadir**. Seleccione los objetos que desea asociar a la pregunta y pulse **Terminado**.
14. Pulse fuera de la pregunta para guardar los cambios.

##### Qué hacer a continuación

Continúe realizando cambios hasta que finalice la plantilla de cuestionario.

- Para editar una pregunta, pulse la pregunta e introduzca los cambios.
- Para duplicar una pregunta, pulse el icono de menú en la pregunta que desea duplicar y pulse **Duplicado**.
- Para suprimir una pregunta, pulse el icono de menú en la pregunta y pulse **Suprimir**.

  Si suprime una pregunta de control, se elimina la lógica de las preguntas dependientes.
- Para eliminar una dependencia de una pregunta de control o un valor de campo, consulte [Eliminar dependencias de preguntas](#supresión-de-dependencias-de-pregunta).
- Para mover preguntas, subsecciones y secciones, pulse **Mover y reordenar elementos** en el panel de navegación, arrastre el elemento que desea mover a su nueva ubicación y pulse **Guardar**. Las preguntas de control y las preguntas que dependen de ellas deben existir en la misma subsección. Cuando intenta mover una pregunta dependiente o de control a otra sección o subsección, aparece un icono de signo de exclamación amarillo con cada nombre de elemento en la relación dependiente. El icono del signo de exclamación indica que la dependencia se elimina si hace clic en **Guardar**.

Revise las preguntas:

- Verifique la finalización de las preguntas y compruebe los errores.
- Verifique las respuestas y compruebe los errores.
- Verifique que los comentarios y archivos adjuntos están marcados correctamente como obligatorios.
- Compruebe si hay preguntas duplicadas.
- Si **Ponderación y puntuación** está habilitado en los **valores de Formato**, compruebe que las ponderaciones de preguntas y la puntuación de respuesta sean correctas y coherentes.
- Revisar dependencias. Para obtener más información, consulte [Creación de relaciones de preguntas](#creación-de-dependencias-de-preguntas).

##### Creación de dependencias de preguntas

`Guía del usuario › Cuestionarios › Plantillas de cuestionario › Añadido de preguntas a una plantilla de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=template-creating-question-dependencies)

Una pregunta dependiente se oculta o se muestra en una evaluación basada en una o más condiciones. Una condición puede basarse en la respuesta del encuestado a otra pregunta, denominada pregunta de control, o en el valor de campo para un tipo de objeto especificado.

> **Importante** : Una pregunta dependiente que se oculta o muestra en función del valor de campo para un tipo de objeto específico no se ve afectada por un cambio en el valor del campo cuando la evaluación del cuestionario está cerrada o es de solo lectura.

###### Acerca de esta tarea

Si define varias condiciones, se deben cumplir todas las condiciones para que se visualice la pregunta. Para alterar temporalmente esta regla, defina la lógica avanzada para combinar las condiciones de forma diferente.

###### Procedimiento

1. Expanda la sección **Mostrar lógica** .
2. Pulse **Generador de condiciones**.
3. Pulse **Nueva condición basada en preguntas** o **Nueva condición basada en atributos**.
4. Si está creando una nueva condición basada en preguntas, realice los pasos siguientes:

   1. Pulse **Seleccionar una pregunta**.

      Seleccione una pregunta de control en la lista. Puede elegir entre preguntas simples o de opción múltiple en cualquier sección o subsección.

      Las preguntas que tienen más de tres niveles de dependencias no se pueden seleccionar como preguntas de control.

      No puede seleccionar una pregunta de control si provoca una dependencia circular. Por ejemplo, si la pregunta A ya depende de la pregunta B, no puede hacer que la pregunta B dependa de la pregunta A.
   2. Seleccione **Valores** y elija uno o más valores para la condición.

      El operador ya está establecido en **en**. Este operador hace que la respuesta se compare con la lista de valores que seleccione en **Valores**. Si la respuesta coincide con uno de los valores seleccionados, la condición se evalúa como verdadera.
5. Si está creando una nueva condición basada en atributos, realice los pasos siguientes:

   1. Seleccione un tipo de objeto.
   2. Seleccione un campo para el tipo de objeto.
   3. Seleccione uno de los operadores siguientes basándose en el tipo de datos del campo:

      **Tabla 1. Selección de operadores para el tipo de datos del campo**

      | Tipo de datos de campo | Operadores |
      | --- | --- |
      | Moneda, Fecha, Decimal, Entero | **empty**, **equal**, **mayor que**, **mayor o igual que**, **menor que**, **menor o igual que**,**not empty**, **not equal** |
      | serie enumerada | **no coincide con ningún**, **vacío**, **igual**, **en**, **coincide con cualquier**, **no vacío**, **no igual**, **no está en** |
      | serie simple | **que contiene**, **vacío**, **termina con**, **igual a**, **expresión regular coincidente**, **no contiene**, **no está vacío**, **no es igual a**,**no coincide con expresión regular,** **empieza con** |
      | Usuario o grupo | **empty**, **equal**, **en**, **en el grupo**, **not empty**, **not equal**, **not in**, **not in group** |
   4. Si ha seleccionado un operador que no sea **vacío** o **no vacío**, especifique un valor para el campo.

   Cuando un encuestado responde a preguntas en una evaluación de cuestionario, las condiciones que especifican tipos de objeto que no están relacionados con la evaluación se resuelven en falso. Por ejemplo, si especifica condiciones para campos en los tipos de objeto Empleado, Proveedor y Proceso, y el encuestado responde a una evaluación que está relacionada solo con el tipo de objeto Proveedor, todas las condiciones Empleado y tipos de objeto Proceso se resuelven en falso.
6. Establezca **Lógica avanzada** en **Activado** para alterar temporalmente la regla predeterminada de que se deben cumplir todas las condiciones.

   Para escribir una expresión, utilice los números de condición junto con los operadores `AND`, `OR`, `NOT`y paréntesis. La expresión no distingue entre mayúsculas y minúsculas. Los operadores se procesan en el orden siguiente:

   1. Paréntesis
   2. NO
   3. Y
   4. O

   Por ejemplo:

   - `1 or 2 or 3`
   - `1 and (2 or 3)`
   - `1 not (2 or 3)`
7. Pulse **Guardar**.

   Cuando la pregunta tiene una condición que se basa en una o más preguntas de control, se muestra el icono de pregunta dependiente ![Icono de pregunta dependiente](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/dependent_question_icon.svg) para esa pregunta. Cuando el ratón pasa por encima del icono de pregunta dependiente, se visualiza un mensaje que identifica todas las preguntas de control.

##### Supresión de dependencias de pregunta

`Guía del usuario › Cuestionarios › Plantillas de cuestionario › Añadido de preguntas a una plantilla de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=template-deleting-question-dependencies)

Puede eliminar dependencias entre una pregunta dependiente y una pregunta de control o un valor de campo.

###### Acerca de esta tarea

Elimine las dependencias suprimiendo las condiciones de la pregunta dependiente.

###### Procedimiento

1. Expanda la sección **Mostrar lógica** .
2. Pulse **Generador de condiciones**.
3. Pulse ![icono de signo menos](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/minus_icon.png) para cada condición que se base en una pregunta de control o un valor de campo.
4. Si **Lógica avanzada** se establece en **Activado**, asegúrese de modificar la expresión para eliminar las condiciones suprimidas o establezca **Lógica avanzada** en **Desactivado**.
5. Pulse **Guardar**.

   Después de guardar los cambios en la pregunta, si la pregunta dependía de una o más preguntas de control y eliminaba todas esas dependencias de la pregunta, el icono de pregunta dependiente ![Icono de pregunta dependiente](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/dependent_question_icon.svg) ya no se visualiza.

##### Asociar respuestas a un campo

`Guía del usuario › Cuestionarios › Plantillas de cuestionario › Añadido de preguntas a una plantilla de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=template-associating-answers-field)

Para rellenar las respuestas a una pregunta con los valores de un campo, asocie las respuestas a un campo que contenga los valores que desea.

> **Importante:** Cuando una pregunta tiene respuestas asociadas a un campo, el hecho de que la pregunta se muestre en una evaluación de cuestionario depende del tipo de objeto de ese campo. Si el tipo de objeto no es el padre primario de la evaluación del cuestionario, la pregunta no se muestra. Por ejemplo, si el padre primario de la evaluación del cuestionario es el tipo de objeto Proveedor, la pregunta no se muestra si sus respuestas están asociadas al campo Departamento del tipo de objeto Empleado.

###### Acerca de esta tarea

Puede definir una de las siguientes asociaciones:

- Pregunta de opción única asociada a un campo de valor de selección única.
- Pregunta de opción múltiple asociada a un campo de valor de selección múltiple.
- Pregunta de texto breve asociada a un campo de texto.
- Pregunta de texto largo asociada a un campo o área de texto.

###### Procedimiento

1. Haga clic en **Asociar respuesta a un campo**.
2. Seleccione el **tipo de objeto relacionado** y el **campo de objeto relacionado** a partir del cual se rellenarán las respuestas.
3. Pulse **Guardar**.

   Las opciones de valor de campo se muestran si el usuario está creando una pregunta de selección única o de selección múltiple.
4. Opcional: Establezca una puntuación para cada respuesta.
5. Pulse fuera de la pregunta para guardar los cambios.

   Para mostrar que la pregunta tiene respuestas asociadas a un campo, se muestra el icono de respuestas asociadas ' ![Icono de respuestas asociadas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/answer_associated_to_field.png). Cuando el ratón pasa por encima del icono, aparece un mensaje que identifica el campo asociado y el tipo de objeto.

###### Qué hacer a continuación

Para rellenar las respuestas de la evaluación del cuestionario, añada la operación **Establecer respuestas del cuestionario con valor de campo relacionado** a una acción del Flujo de trabajo de evaluación del cuestionario. Para obtener más información, consulte [Definición de una acción de flujo de trabajo que rellena respuestas en una evaluación de cuestionario](3.3-guia-del-administrador.md#definición-de-una-acción-de-flujo-de-trabajo-que-rellena-las-respuestas-en-una-evaluación-de-cuestionario).

#### Establecer los valores de campo de un objeto basándose en las respuestas de un encuestado

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-setting-objects-field-values-based-respondents-answers)

Cree una acción de respuesta que establezca los valores de campo de un objeto basándose en las respuestas proporcionadas por un encuestado.

##### Antes de empezar

Para empezar a editar una plantilla de cuestionario, debe estar en la pestaña **Editor** de la página **Plantilla de cuestionario**. Si todavía no está en la página **Plantilla de cuestionario** , realice los pasos siguientes:

1. Abra el **Menú principal** y seleccione **Evaluaciones** > **Plantillas de cuestionario**.
2. Pulse el nombre de la plantilla de cuestionario que desea editar.
3. Pulse la pestaña **Editor**.

##### Acerca de esta tarea

En esta tarea, está configurando una acción de respuesta que establece el valor de los campos en los objetos.

Una acción de respuesta es un conjunto de operaciones que se definen para una plantilla de cuestionario. Para ejecutar acciones de respuesta, debe configurar una operación **Acción de respuesta de cuestionario** en una acción del **Flujo de trabajo de evaluación de cuestionario**. Cuando una evaluación de cuestionario ejecuta la acción de flujo de trabajo, procesa todas las acciones de respuesta definidas para la plantilla de cuestionario asociada a la evaluación de cuestionario.

##### Procedimiento

1. Pulse **Acciones de respuesta** en el panel izquierdo.
2. Pulse **Nueva acción de respuesta**.
3. Especifique un **Nombre** para la acción.
4. Opcional: Especifique una **Descripción** para la acción.
5. Opcional: En la sección **Aplicabilidad de la acción** , defina las condiciones que hacen que se produzca la acción:

   1. Pulse **Seleccionar una pregunta**.

      Seleccione una pregunta de la lista. Puede elegir entre preguntas simples o de opción múltiple en cualquier sección o subsección.

      Desplácese hacia abajo y pulse **Seleccionar**.
   2. Seleccione **Responder** y elija uno o más valores para la condición.

      El operador ya está establecido en **en**. Este operador hace que la respuesta se compare con la lista de valores que seleccione en **Respuesta**. Si la respuesta coincide con uno de los valores seleccionados, la condición se evalúa como verdadera.
   3. Opcional: Si desea aplicar más condiciones, pulse **Nueva condición** y repita los pasos 5a y 5b.
   4. Opcional: Establezca **Lógica avanzada** en **Activado** para alterar temporalmente la regla predeterminada de que se deben cumplir todas las condiciones.

      Para escribir una expresión, utilice los números de condición junto con los operadores `AND`, `OR`, `NOT`y paréntesis. La expresión no distingue entre mayúsculas y minúsculas. Los operadores se procesan en el orden siguiente:

      1. Paréntesis
      2. NO
      3. Y
      4. O

      Los ejemplos siguientes muestran cómo construir una expresión.

      - `1 or 2 or 3`
      - `1 and (2 or 3)`
      - `1 not (2 or 3)`
6. En la sección **Operaciones** , seleccione **Establecer campos**.
7. Especifique los valores que desea aplicar a los campos de objeto cuando se cumplan las condiciones:

   1. Para **Tipo de operación**, seleccione **Establecer campo**, **Establecer campo con respuesta**o **Añadir nuevos valores al campo**.

      - Para especificar un valor para el campo en esta operación, seleccione **Especificar campo**.
      - Para establecer el campo en esta operación con la respuesta que el encuestado eligió para la pregunta, elija **Establecer campo con respuesta**. Cuando elija la operación **Establecer campo con respuesta** , puede establecer campos de serie simple y larga en un objeto utilizando las respuestas de cuestionario de texto corto o preguntas de texto largo.
      - Para añadir valores a la lista de valores que ya están definidos para el campo de cadena de enumeración, seleccione **Añadir nuevos valores al campo**. La operación **Añadir nuevos valores al campo** no sustituye los valores como lo hace la operación **Establecer campo** .

        Por ejemplo, un campo de serie de enumeración denominado `Categories` tiene los valores `Color` & `Shape`. Si elige la operación **Establecer campo** y establece **Valor/Pregunta** en `Size`, el campo `Categories` tiene un valor de `Size` después de que se ejecute la acción de respuesta. Sin embargo, si elige **Añadir valores nuevos al campo**, el campo `Categories` tiene valores de `Color`, `Shape`y `Size` después de que se ejecute la acción de respuesta.
   2. Seleccione el **Objeto de destino** de la operación.

      Cuando un encuestado responde preguntas en una evaluación de cuestionario, sólo se procesan las operaciones sobre tipos de objeto relacionados con la evaluación. Por ejemplo, si especifica operaciones para campos en los tipos de objeto Empleado, Proveedor y Proceso, y el encuestado responde a una evaluación que está relacionada con el tipo de objeto Proveedor, sólo se procesan las operaciones que especifican los tipos de objeto Proveedor.
   3. Para **Nombre de campo**, seleccione el campo que desea establecer.
   4. Para **Valor/Pregunta**, realice uno de los pasos siguientes:

      - Si ha seleccionado **Establecer campo** como tipo de operación, especifique o seleccione el valor en el que desea establecer el campo.

        Puede introducir una expresión para el valor. Por ejemplo, puede introducir `[$TODAY$]` para la fecha actual,`[$END_USER$]` para el nombre del usuario registrado, o `[$System Fields:Description$]` para establecer el campo en el valor del campo `Description` del objeto. Esta expresión implica que el campo `Description` procede del objeto activo, o `self`, en lugar de un hijo o padre del objeto activo.

        Si está configurando un campo en un objeto existente y utiliza una expresión para el valor de un campo, `self` se refiere a la evaluación del cuestionario.

        Si está creando un nuevo objeto, o copiando un objeto existente, y está utilizando una expresión para el valor de un campo, `self` se refiere al padre de la evaluación del cuestionario.

        Para obtener más información sobre el uso de expresiones, consulte [Reglas sintácticas para expresiones](3.3-guia-del-administrador.md#reglas-de-sintaxis-para-expresiones) y [Uso de variables, funciones y campos](3.3-guia-del-administrador.md#uso-de-variables-funciones-y-campos).
      - Si ha seleccionado **Establecer campo con respuesta** como tipo de operación, seleccione la pregunta que tiene la respuesta que desea utilizar para establecer el campo.
      - Si ha seleccionado **Añadir nuevos valores al campo** como tipo de operación, seleccione los valores que desea añadir al campo de serie enumerada.
   5. Opcional: Si desea aplicar otra operación, pulse **Nueva operación** y repita los pasos para definir la operación.
8. Revise la acción de respuesta y edítela según sea necesario. Cuando termine de revisar, pulse **Guardar**.

##### Qué hacer a continuación

Para ejecutar la acción de respuesta, añada una operación en una acción en el flujo de trabajo de evaluación de cuestionario. Para obtener más información, consulte [Ejecución de una acción basada en respuestas en una evaluación de cuestionario](3.3-guia-del-administrador.md#ejecución-de-una-acción-basada-en-respuestas-en-una-evaluación-de-cuestionario).

#### Creación de un objeto basado en las respuestas de un encuestado

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-creating-object-based-respondents-answers)

Crea una acción de respuesta que cree un objeto. El nuevo objeto, hijo del padre de la evaluación del cuestionario, se crea a partir de las respuestas que proporciona un encuestado.

##### Antes de empezar

Para empezar a editar una plantilla de cuestionario, debe estar en la pestaña **Editor** de la página **Plantilla de cuestionario**. Si todavía no está en la página **Plantilla de cuestionario** , realice los pasos siguientes:

1. Abra el **Menú principal** y seleccione **Evaluaciones** > **Plantillas de cuestionario**.
2. Pulse el nombre de la plantilla de cuestionario que desea editar.
3. Pulse la pestaña **Editor**.

##### Acerca de esta tarea

En esta tarea, está configurando una acción de respuesta que crea un nuevo objeto hijo.

Una acción de respuesta es un conjunto de operaciones que se definen para una plantilla de cuestionario. Para ejecutar acciones de respuesta, debe configurar una operación **Acción de respuesta de cuestionario** en una acción del **Flujo de trabajo de evaluación de cuestionario**. Cuando una evaluación de cuestionario ejecuta la acción de flujo de trabajo, procesa todas las acciones de respuesta definidas para la plantilla de cuestionario asociada a la evaluación de cuestionario.

##### Procedimiento

1. Pulse **Acciones de respuesta** en el panel izquierdo.
2. Pulse **Nueva acción de respuesta**.
3. Especifique un **Nombre** para la acción.
4. Opcional: Especifique una **Descripción** para la acción.
5. Opcional: En la sección **Aplicabilidad de la acción** , defina las condiciones que hacen que se produzca la acción:

   1. Pulse **Seleccionar una pregunta**.

      Seleccione una pregunta de la lista. Puede elegir entre preguntas simples o de opción múltiple en cualquier sección o subsección.

      Desplácese hacia abajo y pulse **Seleccionar**.
   2. Seleccione **Responder** y elija uno o más valores para la condición.

      El operador ya está establecido en **en**. Este operador hace que la respuesta se compare con la lista de valores que seleccione en **Respuesta**. Si la respuesta coincide con uno de los valores seleccionados, la condición se evalúa como verdadera.
   3. Opcional: Si desea aplicar más condiciones, pulse **Nueva condición** y repita los pasos 5a y 5b.
   4. Opcional: Establezca **Lógica avanzada** en **Activado** para alterar temporalmente la regla predeterminada de que se deben cumplir todas las condiciones.

      Para escribir una expresión, utilice los números de condición junto con los operadores `AND`, `OR`, `NOT`y paréntesis. La expresión no distingue entre mayúsculas y minúsculas. Los operadores se procesan en el orden siguiente:

      1. Paréntesis
      2. NO
      3. Y
      4. O

      Los ejemplos siguientes muestran cómo construir una expresión.

      - `1 or 2 or 3`
      - `1 and (2 or 3)`
      - `1 not (2 or 3)`
6. En la sección **Operaciones** , seleccione **Crear objeto**.
7. En **Tipo de objeto hijo**, seleccione el tipo de objeto que desea crear.
8. **Nuevo nombre del objeto** is disabled if the object is auto-named. Si la opción **Nuevo nombre de objeto** no está desactivada, introduzca el nombre del objeto que desea crear
9. El hecho de introducir un **Nombre de objeto nuevo** depende de si el tipo de objeto tiene nombre automático y de si el administrador ha habilitado la edición. Su administrador establece **Aplicaciones** > **GRCM** > **Asignación automática de nombres** > **`<tipo_objeto>`** > **Se puede editar** en **verdadero** o **falso** para determinar si se puede editar el nombre generado para un tipo de objeto.

   - **Nuevo nombre de objeto** está desactivado si el objeto tiene nombre automático y su administrador no ha activado la edición del nombre.
   - Si el objeto tiene nombre automático y su administrador ha habilitado la edición, puede elegir si desea introducir un nombre para anular el nombre automático. Si no introduce un nombre, el objeto se nombra automáticamente.
   - Si el objeto no tiene nombre automático, introduzca un **Nombre nuevo del objeto**.
10. Seleccione **Omitir si existe** si no desea que la acción de respuesta intente volver a crear un nuevo objeto si ya existe un objeto con el mismo nombre.

    Por ejemplo, una acción de respuesta que crea un objeto se ejecuta cuando un encuestado envía una evaluación de cuestionario para su revisión. El revisor rechaza la evaluación del cuestionario, y el encuestado la corrige y vuelve a enviarla al revisor. El reenvío hace que la acción de respuesta se ejecute de nuevo e intente crear el objeto. Cuando se especifica un nombre para el objeto creado por la acción de respuesta, el objeto no se puede crear porque ya existe. Se muestra un mensaje de error al encuestado y éste no puede enviar la evaluación del cuestionario al revisor.

    Si se selecciona **Omitir si existe**, cuando el encuestado vuelve a enviar la evaluación del cuestionario, la acción de respuesta no intenta volver a crear el objeto y se permite que la evaluación del cuestionario continúe para su revisión.
11. Establezca los valores de los campos para el nuevo objeto. Especifica al menos una operación, como **Configurar campo**, **Configurar campo con respuesta**, o **Añadir nuevos valores al campo**.

    Pulse **Establecer valor de campo** para cada campo que desee establecer.
12. Especifique los valores que desea aplicar a los campos de objeto cuando se cumplan las condiciones:

    1. Para **Tipo de operación**, seleccione **Establecer campo**, **Establecer campo con respuesta**o **Añadir nuevos valores al campo**.

       - Para especificar un valor para el campo en esta operación, seleccione **Especificar campo**.
       - Para establecer el campo en esta operación con la respuesta que el encuestado eligió para la pregunta, elija **Establecer campo con respuesta**. Cuando elija la operación **Establecer campo con respuesta** , puede establecer campos de serie simple y larga en un objeto utilizando las respuestas de cuestionario de texto corto o preguntas de texto largo.
       - Para añadir valores a la lista de valores que ya están definidos para el campo de cadena de enumeración, seleccione **Añadir nuevos valores al campo**. La operación **Añadir nuevos valores al campo** no sustituye los valores como lo hace la operación **Establecer campo** .

         Por ejemplo, un campo de serie de enumeración denominado `Categories` tiene los valores `Color` & `Shape`. Si elige la operación **Establecer campo** y establece **Valor/Pregunta** en `Size`, el campo `Categories` tiene un valor de `Size` después de que se ejecute la acción de respuesta. Sin embargo, si elige **Añadir valores nuevos al campo**, el campo `Categories` tiene valores de `Color`, `Shape`y `Size` después de que se ejecute la acción de respuesta.
    2. Seleccione el **Objeto de destino** de la operación.

       Cuando un encuestado responde preguntas en una evaluación de cuestionario, sólo se procesan las operaciones sobre tipos de objeto relacionados con la evaluación. Por ejemplo, si especifica operaciones para campos en los tipos de objeto Empleado, Proveedor y Proceso, y el encuestado responde a una evaluación que está relacionada con el tipo de objeto Proveedor, sólo se procesan las operaciones que especifican los tipos de objeto Proveedor.
    3. Para **Nombre de campo**, seleccione el campo que desea establecer.
    4. Para **Valor/Pregunta**, realice uno de los pasos siguientes:

       - Si ha seleccionado **Establecer campo** como tipo de operación, especifique o seleccione el valor en el que desea establecer el campo.

         Puede introducir una expresión para el valor. Por ejemplo, puede introducir `[$TODAY$]` para la fecha actual,`[$END_USER$]` para el nombre del usuario registrado, o `[$System Fields:Description$]` para establecer el campo en el valor del campo `Description` del objeto. Esta expresión implica que el campo `Description` procede del objeto activo, o `self`, en lugar de un hijo o padre del objeto activo.

         Si está configurando un campo en un objeto existente y utiliza una expresión para el valor de un campo, `self` se refiere a la evaluación del cuestionario.

         Si está creando un nuevo objeto, o copiando un objeto existente, y está utilizando una expresión para el valor de un campo, `self` se refiere al padre de la evaluación del cuestionario.

         Para obtener más información sobre el uso de expresiones, consulte [Reglas sintácticas para expresiones](3.3-guia-del-administrador.md#reglas-de-sintaxis-para-expresiones) y [Uso de variables, funciones y campos](3.3-guia-del-administrador.md#uso-de-variables-funciones-y-campos).
       - Si ha seleccionado **Establecer campo con respuesta** como tipo de operación, seleccione la pregunta que tiene la respuesta que desea utilizar para establecer el campo.
       - Si ha seleccionado **Añadir nuevos valores al campo** como tipo de operación, seleccione los valores que desea añadir al campo de serie enumerada.
    5. Opcional: Si desea establecer otro valor de campo, pulse **Establecer valor de campo** y repita los pasos para especificar un valor de campo.
13. Revise la acción de respuesta y edítela según sea necesario. Cuando termine de revisar, pulse **Guardar**.

##### Qué hacer a continuación

Para ejecutar la acción de respuesta, añada una operación en una acción en el flujo de trabajo de evaluación de cuestionario. Para obtener más información, consulte [Ejecución de una acción basada en respuestas en una evaluación de cuestionario](3.3-guia-del-administrador.md#ejecución-de-una-acción-basada-en-respuestas-en-una-evaluación-de-cuestionario).

#### Copia de un objeto basado en las respuestas de un encuestado

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-copying-object-based-respondents-answers)

Crea una acción de respuesta que copie un objeto existente. El nuevo objeto, hijo del padre de la evaluación del cuestionario, se crea a partir de las respuestas que proporciona un encuestado.

##### Antes de empezar

Para empezar a editar una plantilla de cuestionario, debe estar en la pestaña **Editor** de la página **Plantilla de cuestionario**. Si todavía no está en la página **Plantilla de cuestionario** , realice los pasos siguientes:

1. Abra el **Menú principal** y seleccione **Evaluaciones** > **Plantillas de cuestionario**.
2. Pulse el nombre de la plantilla de cuestionario que desea editar.
3. Pulse la pestaña **Editor**.

##### Acerca de esta tarea

En esta tarea, está configurando una acción de respuesta que copia un objeto.

Una acción de respuesta es un conjunto de operaciones que se definen para una plantilla de cuestionario. Para ejecutar acciones de respuesta, debe configurar una operación **Acción de respuesta de cuestionario** en una acción del **Flujo de trabajo de evaluación de cuestionario**. Cuando una evaluación de cuestionario ejecuta la acción de flujo de trabajo, procesa todas las acciones de respuesta definidas para la plantilla de cuestionario asociada a la evaluación de cuestionario.

##### Procedimiento

1. Pulse **Acciones de respuesta** en el panel izquierdo.
2. Pulse **Nueva acción de respuesta**.
3. Especifique un **Nombre** para la acción.
4. Opcional: Especifique una **Descripción** para la acción.
5. Opcional: En la sección **Aplicabilidad de la acción** , defina las condiciones que hacen que se produzca la acción:

   1. Pulse **Seleccionar una pregunta**.

      Seleccione una pregunta de la lista. Puede elegir entre preguntas simples o de opción múltiple en cualquier sección o subsección.

      Desplácese hacia abajo y pulse **Seleccionar**.
   2. Seleccione **Responder** y elija uno o más valores para la condición.

      El operador ya está establecido en **en**. Este operador hace que la respuesta se compare con la lista de valores que seleccione en **Respuesta**. Si la respuesta coincide con uno de los valores seleccionados, la condición se evalúa como verdadera.
   3. Opcional: Si desea aplicar más condiciones, pulse **Nueva condición** y repita los pasos 5a y 5b.
   4. Opcional: Establezca **Lógica avanzada** en **Activado** para alterar temporalmente la regla predeterminada de que se deben cumplir todas las condiciones.

      Para escribir una expresión, utilice los números de condición junto con los operadores `AND`, `OR`, `NOT`y paréntesis. La expresión no distingue entre mayúsculas y minúsculas. Los operadores se procesan en el orden siguiente:

      1. Paréntesis
      2. NO
      3. Y
      4. O

      Los ejemplos siguientes muestran cómo construir una expresión.

      - `1 or 2 or 3`
      - `1 and (2 or 3)`
      - `1 not (2 or 3)`
6. En la sección **Operaciones** , seleccione **Copiar objeto**.
7. En **Tipo de objeto hijo**, seleccione el tipo de objeto que desea copiar.
8. En **Objeto a copiar**, pulse **Seleccionar objeto**.
9. En el recuadro de diálogo **Copiar** `< tipo_objeto>`, donde `< tipo_objeto>` es el tipo de objeto hijo que ha elegido copiar, seleccione el objeto que desea copiar y pulse **Terminado**.
10. Opcional: En **Mantener relaciones**, si desea que la copia del objeto conserve las asociaciones padre que tiene el objeto de origen, seleccione los tipos de objeto para los que desea conservar las relaciones.

    Por ejemplo, si copia un control y selecciona **Requisito**, el nuevo objeto se asocia a los mismos objetos de requisito padre que el objeto de control de origen.
11. Opcional: Si desea establecer los valores de los campos para el nuevo objeto, pulse **Establecer valor de campo** para cada campo que desee establecer.

    De lo contrario, omita el paso siguiente.
12. Especifique los valores que desea aplicar a los campos de objeto cuando se cumplan las condiciones:

    1. Para **Tipo de operación**, seleccione **Establecer campo**, **Establecer campo con respuesta**o **Añadir nuevos valores al campo**.

       - Para especificar un valor para el campo en esta operación, seleccione **Especificar campo**.
       - Para establecer el campo en esta operación con la respuesta que el encuestado eligió para la pregunta, elija **Establecer campo con respuesta**. Cuando elija la operación **Establecer campo con respuesta** , puede establecer campos de serie simple y larga en un objeto utilizando las respuestas de cuestionario de texto corto o preguntas de texto largo.
       - Para añadir valores a la lista de valores que ya están definidos para el campo de cadena de enumeración, seleccione **Añadir nuevos valores al campo**. La operación **Añadir nuevos valores al campo** no sustituye los valores como lo hace la operación **Establecer campo** .

         Por ejemplo, un campo de serie de enumeración denominado `Categories` tiene los valores `Color` & `Shape`. Si elige la operación **Establecer campo** y establece **Valor/Pregunta** en `Size`, el campo `Categories` tiene un valor de `Size` después de que se ejecute la acción de respuesta. Sin embargo, si elige **Añadir valores nuevos al campo**, el campo `Categories` tiene valores de `Color`, `Shape`y `Size` después de que se ejecute la acción de respuesta.
    2. Para **Nombre de campo**, seleccione el campo que desea establecer.
    3. Para **Valor/Pregunta**, realice uno de los pasos siguientes:

       - Si ha seleccionado **Establecer campo** como tipo de operación, especifique o seleccione el valor en el que desea establecer el campo.

         Puede introducir una expresión para el valor. Por ejemplo, puede introducir `[$TODAY$]` para la fecha actual,`[$END_USER$]` para el nombre del usuario registrado, o `[$System Fields:Description$]` para establecer el campo en el valor del campo `Description` del objeto. Esta expresión implica que el campo `Description` procede del objeto activo, o `self`, en lugar de un hijo o padre del objeto activo.

         Si está configurando un campo en un objeto existente y utiliza una expresión para el valor de un campo, `self` se refiere a la evaluación del cuestionario.

         Si está creando un nuevo objeto, o copiando un objeto existente, y está utilizando una expresión para el valor de un campo, `self` se refiere al padre de la evaluación del cuestionario.

         Para obtener más información sobre el uso de expresiones, consulte [Reglas sintácticas para expresiones](3.3-guia-del-administrador.md#reglas-de-sintaxis-para-expresiones) y [Uso de variables, funciones y campos](3.3-guia-del-administrador.md#uso-de-variables-funciones-y-campos).
       - Si ha seleccionado **Establecer campo con respuesta** como tipo de operación, seleccione la pregunta que tiene la respuesta que desea utilizar para establecer el campo.
       - Si ha seleccionado **Añadir nuevos valores al campo** como tipo de operación, seleccione los valores que desea añadir al campo de serie enumerada.
    4. Opcional: Si desea establecer otro valor de campo, pulse **Establecer valor de campo** y repita los pasos para especificar un valor de campo.
13. Revise la acción de respuesta y edítela según sea necesario. Cuando termine de revisar, pulse **Guardar**.

##### Qué hacer a continuación

Para ejecutar la acción de respuesta, añada una operación en una acción en el flujo de trabajo de evaluación de cuestionario. Para obtener más información, consulte [Ejecución de una acción basada en respuestas en una evaluación de cuestionario](3.3-guia-del-administrador.md#ejecución-de-una-acción-basada-en-respuestas-en-una-evaluación-de-cuestionario).

#### Adición de variables de objeto a una plantilla de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-adding-object-variables-questionnaire-template)

Las variables de objeto en una plantilla de cuestionario se representan en valoraciones de cuestionario como valores de los objetos asociados con la evaluación de cuestionario que responde el encuestado. Puede utilizar variables de objeto en una plantilla de cuestionario.

También puede añadir enlaces a las plantillas de cuestionario. Para obtener información, consulte [Adición de enlaces a una plantilla de cuestionario](#adición-de-enlaces-a-una-plantilla-de-cuestionario).

Puede añadir variables de objeto en las ubicaciones siguientes:

- Descripciones de sección
- Descripciones de subsección
- Para una pregunta, el texto **Pregunta** y el texto **Rationale** en la sección **Contexto adicional**

Las variables pueden insertar la información siguiente:

- El identificador, nombre o descripción del activo subyacente en el que se basa la evaluación de cuestionario.
- El identificador, nombre o descripción del programa a partir del que se ha iniciado la evaluación de cuestionario.
- El identificador, nombre o descripción de la evaluación de cuestionario que responde el encuestado.
- El identificador, nombre o descripción de la plantilla de cuestionario a partir de la que se ha creado la evaluación de cuestionario.

Por ejemplo, el texto siguiente en una descripción de sección inserta el identificador de la evaluación de cuestionario, el nombre del activo subyacente con el que está relacionado y el nombre del programa que lo ha generado.

```
This questionnaire assessment, ${questionnaireassessment.id}, is related 
to the following asset: ${asset.name}. 
It is part of the ${program.name} program. 
```

Se muestra como una evaluación de cuestionario de la siguiente manera:

**Esta evaluación de cuestionario, 2018-Assessment-7362810, está relacionada con el activo: ResourceA. Es parte del programa 2018 Annual Risk Assessment Questionnaire.**

Donde **2018-Assessment-7362810** es el identificador de la evaluación de cuestionario, **ResourceA** es el nombre del activo subyacente y **2018 Annual Risk Assessment Questionnaire** es el nombre del programa.

Puede crear un programa de prueba e iniciar una evaluación de cuestionario para asegurarse de que las variables se insertan correctamente.

##### Utilización de la característica de asistencia de contenido para elegir variables de objeto

Puede utilizar la característica de asistencia de contenido para elegir entre una lista de variables de objeto. En el cuadro de texto, escriba **/?** para mostrar todas las variables disponibles o escriba **${** seguido del nombre de la variable para filtrar las opciones.

![Una descripción de sección que muestra la lista de variables de objeto disponibles](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/questionnaire_vars_list.png)

##### Lista de variables de objeto

Consulte la tabla siguiente para obtener una lista de variables. Las variables no distinguen entre mayúsculas y minúsculas.

**Tabla 1. Variables de objeto permitidas en plantillas de cuestionario**

| Variable de objeto | Descripción |
| --- | --- |
| ${asset.id} | Inserta el identificador del activo subyacente |
| ${asset.name} | Inserta el nombre de activo del activo subyacente |
| ${asset.description} | Inserta la descripción del activo subyacente |
| ${program.id} | Inserta el identificador de programa |
| ${program.name} | Inserta el nombre del programa |
| ${program.description} | Inserta la descripción del programa |
| ${questionnaireassessment.id} | Inserta el identificador de evaluación de cuestionario |
| ${questionnaireassessment.name} | Inserta el nombre de evaluación de cuestionario |
| ${questionnaireassessment.description} | Inserta la descripción de evaluación de cuestionario |
| ${questionnairetemplate.id} | Inserta el identificador de plantilla de cuestionario |
| ${questionnairetemplate.name} | Inserta el nombre de la plantilla de cuestionario |
| ${questionnairetemplate.description} | Inserta la descripción de la plantilla de cuestionario |

#### Adición de enlaces a una plantilla de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-adding-links-questionnaire-template)

Los enlaces de una plantilla de cuestionario se muestran en las evaluaciones de cuestionario como hipervínculos en los que un encuestado puede hacer clic para acceder a una URL, un objeto de OpenPages®, por ejemplo, el activo subyacente en el que se basa una evaluación de cuestionario, o un informe de IBM® Cognos® Analytics. Puede utilizar enlaces en una plantilla de cuestionario.

Puede añadir enlaces en las ubicaciones siguientes:

- Descripciones de sección
- Descripciones de subsección
- Para una pregunta, el texto **Pregunta** y el texto **Rationale** en la sección **Contexto adicional**

Puede tener los siguientes tipos de enlaces:

- Un enlace fijo a una URL
- Un enlace dinámico a la vista de tarea de un objeto
- Un enlace a un informe de Cognos

Por ejemplo, el siguiente texto en la descripción de una sección incluye un enlace dinámico a la vista de tareas de un objeto y un enlace fijo a una URL :

```
This questionnaire is related to the asset: ${asset.link}.
For more information about assets, see [Assets](https://www.ibm.com/docs/en/opw/9.0.0?topic=links-resources).
```

Se muestra como una evaluación de cuestionario de la siguiente manera:

**Este cuestionario está relacionado con el activo: AssetA. Para obtener más información sobre assetts, consulte Activos.**

**AssetA** es un enlace a la vista de tarea del activo subyacente y **Activos** es un enlace al tema de ayuda IBM Documentation sobre objetos de activo.

Puede crear un programa de prueba e iniciar una evaluación de cuestionario para asegurarse de que los enlaces se insertan correctamente.

También puede añadir variables de objetos a las plantillas de cuestionario. Para obtener información, consulte [Adición de variables de objeto a una plantilla de cuestionario](#adición-de-variables-de-objeto-a-una-plantilla-de-cuestionario).

##### Enlaces fijos en las plantillas de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario › Adición de enlaces a una plantilla de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=template-fixed-links-in-questionnaire-templates)

Los enlaces fijos se representan como hiperenlaces en plantillas de cuestionario y evaluaciones. Cuando un encuestado hace clic en el hipervínculo, la URL se abre en una nueva pestaña o ventana.

- **Sintaxis**

  ```
  [link_text](url)
  ```

- **Ejemplo**

  ```
  [Controls](https://www.ibm.com/docs/en/opw/9.0.0?topic=objects-controls)
  ```

  Se representa como un hiperenlace con el texto de enlace **Controles** y abre IBM Documentation en el tema de ayuda sobre Controles.

- **Reglas**

  El protocolo puede ser http, https o ftp. No use únicamente www.

##### Enlaces dinámicos en plantillas de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario › Adición de enlaces a una plantilla de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=template-dynamic-links-in-questionnaire-templates)

Un enlace dinámico se representa en una evaluación de cuestionario como un enlace a un objeto asociado con la evaluación de cuestionario a la que responde un encuestado.

Un enlace dinámico contiene una variable que inserta un enlace a los objetos siguientes:

- El activo subyacente en el que se basa la evaluación de cuestionario.
- El programa a partir del que se inicia la evaluación de cuestionario.
- La plantilla de cuestionario a partir de la que se crea la evaluación de cuestionario.
- La evaluación de cuestionario que responde el encuestado.

- **Sintaxis**

  ```
  ${variable}
  ```

- **Ejemplo**

  ```
  This questionnaire is based on the asset: ${asset.link}
  ```

  Se representa como el texto siguiente, donde **ResourceA** es un enlace a la vista de tarea del activo subyacente.

  **Este cuestionario se basa en el activo: ResourceA**

- **Reglas**

  Consulte la Tabla 1 para obtener una lista de variables.

  Las variables no distinguen entre mayúsculas y minúsculas.

**Tabla 1. Variables de enlace permitidas en plantillas de cuestionario**

| Variable de enlace | Descripción |
| --- | --- |
| ${asset.link} | Inserta un enlace al activo subyacente. El nombre de activo se visualiza como texto de enlace. |
| ${program.link} | Inserta un enlace al programa. El nombre del programa se visualiza como el texto del enlace. |
| ${questionnaireassessment.link} | Inserta un enlace a la evaluación de cuestionario. El nombre de evaluación de cuestionario se muestra como texto de enlace. |
| ${questionnairetemplate.link} | Inserta un enlace a la plantilla de cuestionario. El nombre de plantilla de cuestionario se visualiza como texto de enlace. |

##### Enlaces a informes de IBM Cognos Analytics en plantillas de cuestionario

`Guía del usuario › Cuestionarios › Plantillas de cuestionario › Adición de enlaces a una plantilla de cuestionario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=template-links-cognos-analytics-reports-in-questionnaire-templates)

Un enlace a un informe de Cognos® se representa como un hiperenlace en una evaluación de cuestionario. Cuando un encuestado pulsa el hiperenlace, el informe de Cognos se abre en una nueva pestaña o ventana. Opcionalmente, los parámetros se pueden pasar de la evaluación de cuestionario al informe.

- **Sintaxis**

  ```
  [link_text](report://folderName=folder name&reportName=report name&parameter1=${variable}&parameter2=value)
  ```

- **Ejemplo 1: sin parámetros**

  ```
  [KRI Dashboard](report://folderName=OpenPages Solutions Reports/Indicator Reports/KRI Dashboard&reportName=KRI Dashboard)
  ```

  Se representa como un hiperenlace con el texto de enlace **Panel de instrumentos KRI** y abre el informe Panel de instrumentos KRI.

- **Ejemplo 2: parámetros de valor fijo y parámetros de variable**

  ```
  [Program Report w/params](report://folderName=OpenPages Platform Reports/Questionnaire Reports&reportName=Program Report&P_ReportType=Risk&P_Program Type=254&P_Program=${Program.id}&P_Assessment=${QuestionnaireAssessment.id})
  ```

  Se representa como un hiperenlace con el texto de enlace **Informe de programa con parámetros**, pasa parámetros de valor fijo (tipo de informe y tipo de programa) al informe, pasa parámetros variables (el ID de evaluación de cuestionario y el ID de programa) al informe y abre el informe. El valor de `P_Program Type` difiere entre los despliegues de OpenPages .

- **Reglas**

  Tanto `folderName` (nombre de carpeta) y `reportName` (nombre de informe) son obligatorios.

  Si no conoce `folderName` y `reportName`, puede buscar los valores. Haga clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Páginas y plantillas** y seleccione el informe. La **Carpeta de informes** muestra `folderName/reportName`

  Si pasa parámetros de la evaluación de cuestionario al informe, los nombres de parámetro los determina el informe de Cognos . Los parámetros pueden contener parámetros de valor fijo, por ejemplo, el tipo de informe o el tipo de programa. Los parámetros también pueden ser variables que pasan la información siguiente:

  - El identificador, nombre o descripción del activo subyacente en el que se basa la evaluación de cuestionario.
  - El identificador, nombre o descripción del programa a partir del que se ha iniciado la evaluación de cuestionario.
  - El identificador, nombre o descripción de la evaluación de cuestionario que responde el encuestado.
  - El identificador, nombre o descripción de la plantilla de cuestionario a partir de la que se ha creado la evaluación de cuestionario.

  Consulte la [Tabla 1](#adición-de-variables-de-objeto-a-una-plantilla-de-cuestionario) para obtener una lista de variables.

  Separe los parámetros por el signo `&`.

### evaluaciones de cuestionarios

`Guía del usuario › Cuestionarios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=questionnaires-questionnaire-assessments)

Las evaluaciones de cuestionario son medios de recopilar información de los usuarios empresariales de la organización. Los encuestados completan las preguntas y envían la evaluación de cuestionario finalizada.

Antes de utilizar las evaluaciones de cuestionario, consulte [Visión general del cuestionario](#resumen-del-cuestionario).

Las evaluaciones de cuestionario se crean cuando se inicia un programa. Para obtener más información, consulte [Inicio de un programa](#lanzamiento-de-un-programa).

#### Completar una evaluación de cuestionario

`Guía del usuario › Cuestionarios › evaluaciones de cuestionarios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=assessments-completing-questionnaire-assessment)

Como encuestado, puede completar una evaluación de cuestionario que el equipo de riesgo empresarial le ha enviado.

Puede elegir copiar respuestas, comentarios y archivos adjuntos de una evaluación de cuestionario existente para ahorrar tiempo. Por ejemplo, es posible que desee copiar respuestas si recibe un cuestionario anual y algunas de sus respuestas del año pasado siguen siendo las mismas. OpenPages® utiliza un ID interno para hacer coincidir las preguntas de la evaluación del año pasado con las preguntas del cuestionario que está completando. Al hacer coincidir los ID, OpenPages garantiza que las respuestas, los comentarios y los archivos adjuntos se copien en las mismas preguntas o en preguntas similares.

Puede copiar respuestas en una evaluación de cuestionario tantas veces como desee. Cada vez que copie las respuestas, puede elegir copiar de la misma evaluación de cuestionario o de una diferente.

##### Acerca de esta tarea

Las preguntas pueden presentar los formatos siguientes:

- **Opción única**

  Sólo puede elegir una respuesta de una lista que proporcione. Puede hacer que otras preguntas dependan de la respuesta elegida.
- **Varias opciones**

  Puede elegir una o más respuestas de una lista que proporcione. Puede hacer que otras preguntas dependan de las respuestas elegidas.
- **Texto corto**

  Puede especificar hasta 252 caracteres de texto. Las preguntas de texto breve no tienen puntuación de respuesta y se excluyen de la puntuación.
- **Texto largo**

  Puede especificar hasta 2048 caracteres de texto. Las preguntas de texto largo no tienen puntuación de respuesta y se excluyen de la puntuación.
- **Tabla**

  Puede añadir hasta 30 filas a la tabla y escribir hasta 50 caracteres por celda. Las preguntas de las respuestas de la tabla no tienen puntuación de respuesta y se excluyen de la puntuación.

Si una pregunta es dependiente, se muestra u oculta en función de su respuesta a una pregunta de control anterior. Por ejemplo, si responde a una pregunta de control con la respuesta **Sí**, el cuestionario muestra tres preguntas más dependientes sobre ese tema. Pero si responde **No**, el sistema oculta las preguntas dependientes.

El porcentaje de progreso, **Puntuación de conformidad** y **Puntuación de riesgo** se visualizan en la vista Cuadrícula de evaluación del cuestionario. Estos valores se actualizan de manera continua a medida que se trabaja en la evaluación de cuestionario. La puntuación de conformidad es el resultado de la puntuación normalizada de todas las preguntas que ha respondido hasta el momento. Una puntuación de conformidad de **0** indica la no conformidad y **100** significa conformidad completa. La puntuación de riesgo es el resultado de la puntuación. La puntuación de riesgo no se normaliza. La puntuación de riesgo está definida por el usuario y puede ser, por ejemplo, **0** - **100**, donde **0** significa que no hay riesgo y **100** significa alto riesgo, o **0** - **500**, donde **0** significa que no hay riesgo y **500** significa alto riesgo. También el revisor puede ver esta información.

Cualquiera que pueda acceder a la evaluación de cuestionario también puede trabajar en ella. En una evaluación de cuestionario puede trabajar más de un encuestado.

##### Procedimiento

1. Puede abrir una evaluación de cuestionario de una de las maneras siguientes:

   - Abra el correo electrónico y pulse la URL. El sistema abre la evaluación del cuestionario en una nueva ventana. Pulse **Abrir cuestionario**.
   - Si el correo electrónico no está configurado, pulse **Evaluaciones** > **Evaluaciones de cuestionario**. El sistema mostrará una lista de evaluaciones de cuestionario. Pulse la evaluación de cuestionario que desea completar y pulse la pestaña **Cuestionario**.
2. Opcional: Si desea copiar respuestas de otra evaluación de cuestionario, pulse **Copiar respuestas** en el panel izquierdo.

   1. Opcional: Si desea copiar archivos adjuntos o comentarios, pulse **Seleccionar opciones de copia**. Seleccione las opciones que desee.
   2. Opcional: Si desea sobrescribir las respuestas existentes con las respuestas copiadas, seleccione **Sustituir respuestas existentes**.
   3. Seleccione una evaluación de cuestionario de la que copiar respuestas.
   4. Pulse **Terminado**.

   Cada vez que se copian respuestas de otra evaluación de cuestionario, se añade un comentario a cada pregunta con una respuesta copiada. El comentario muestra cuándo se ha copiado una respuesta y el nombre de la evaluación de cuestionario de la que se ha copiado.
3. Empiece a responder las preguntas:

   - Puede empezar en cualquier sección o subsección.
   - Trabaje secuencialmente entre las preguntas de una subsección. Las preguntas se pueden mostrar u ocultar en función de sus respuestas.
   - Puede cambiar sus respuestas tanto como quiera hasta que envíe el cuestionario.
   - Puede pulsar **Guardar borrador** o dejar que la evaluación se guarde automáticamente.
   - Puede pararse y volver a empezar siempre que lo necesite.
   - Es posible que pueda dejar las preguntas sin responder en función de cómo se haya definido la plantilla de cuestionario.
   - En una pregunta de opción múltiple, una o más de las respuestas pueden ser respuestas exclusivas, lo que significa que no puede seleccionar ninguna otra respuesta para la pregunta después de seleccionar una respuesta exclusiva. Por ejemplo, una pregunta tiene las respuestas siguientes: "A", "B" y "Ninguno de los anteriores". Si la persona que ha creado el cuestionario ha establecido la respuesta "Ninguna de las anteriores" en exclusiva, puede elegir entre "A" y "B", o ambas. Sin embargo, si elige "Ninguno de los anteriores", no puede elegir ninguna otra respuesta.
   - Puede utilizar el filtro de preguntas en el panel de navegación para controlar las preguntas que se muestran. Puede elegir **Ver todas las preguntas**, **Ver preguntas completadas**, **Ver preguntas incompletas**, **Ver preguntas marcadas**o **Ver preguntas necesarias**. Una pregunta se completa si tiene una respuesta y todos los comentarios y archivos adjuntos necesarios.
   - Pulse **Borrar** para descartar una respuesta o texto que ha especificado y volver a establecer la pregunta en su estado inicial.
   - Pulse **Actividad** para ver quién ha respondido por última vez a una pregunta y cuándo.
4. Si una pregunta ya tiene una respuesta, se ha copiado desde la misma pregunta de una evaluación de cuestionario previa en relación con el activo. Puede conservar la respuesta o cambiarla. Pulse **Comentario** para visualizar comentarios o **Archivos adjuntos** para visualizar archivos adjuntos. Puede retener, suprimir o modificarlos. También se puede visualizar el nombre de la evaluación de cuestionario de origen. En función de los valores definidos durante el inicio del programa, se mostrarán comentarios, archivos adjuntos o información de origen.
5. Si los comentarios están habilitados para una pregunta, pulse **Comentario** para añadir información adicional a una respuesta.

   Todas las preguntas pueden tener comentarios y cada pregunta puede tener varios comentarios. Un comentario puede ser parte opcional u obligatoria de una respuesta. Si es obligatorio, la respuesta se marcará como incompleta hasta que se añada un comentario.

   La longitud máxima de un comentario es de 1000 caracteres.

   Puede copiar y pegar texto en un comentario. Si copia el texto desde otra fuente, debe estar en una línea sin saltos de párrafo.

   Los comentarios no pueden suprimirse.

   Para editar un comentario que haya creado, haga clic en **Editar** ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_icon.jpg). Los comentarios generados que indican que una respuesta se ha copiado de otra evaluación de cuestionario no se pueden editar.

   Para eliminar un comentario que haya creado, haga clic en **Eliminar** ![Icono Suprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/trash_icon.png). Los siguientes tipos de comentarios no se pueden suprimir:

   - Comentarios generados que indican que se ha copiado una respuesta de otra evaluación de cuestionario
   - Comenta el revisor creado para explicar por qué se ha marcado una pregunta
   - Comentarios que el revisor ha aceptado después de que la pregunta se haya marcado durante el proceso de revisión
6. Si los archivos adjuntos están habilitados para una pregunta, pulse **Archivo adjunto** para añadir documentación de soporte a la respuesta. Todas las preguntas pueden tener archivos adjuntos. Un archivo adjunto puede ser parte opcional u obligatoria de una respuesta. Si es obligatorio, la respuesta se marcará como incompleta y no se puntuará hasta que se añada un archivo adjunto. También se puede añadir una descripción a un archivo adjunto, con una longitud máxima de 100 caracteres. Los archivos adjuntos pueden suprimirse.
7. Cuando haya terminado de responder preguntas, compruebe que ha finalizado todas las preguntas y que están completas. Puede cambiar sus respuestas. Asegúrese de haber añadido los comentarios y archivos adjuntos a las preguntas que los necesiten. Puede suprimir archivos adjuntos y añadir otros nuevos. Si el indicador de progreso de **Preguntas completadas** muestra que hay algunas preguntas que no ha respondido, seleccione **Ver preguntas incompletas** en el filtro de preguntas para mostrar las preguntas sin respuesta. También puede seleccionar **Ver preguntas necesarias** en el filtro de preguntas para visualizar las preguntas necesarias.
8. Cuando la evaluación del cuestionario esté completa, los pasos siguientes dependerán de la interfaz que esté utilizando.

   - Si está respondiendo al cuestionario tras pulsar un enlace en un correo electrónico que ha recibido, pulse **Enviar para revisión** o **Enviar y cerrar**. El flujo de trabajo determina qué icono se visualiza.

     Cuando se le solicite que confirme la acción, pulse **Enviar**.
   - Si está respondiendo al cuestionario en la pestaña **Cuestionario**, pulse **Acción**. Seleccione la acción **Enviar y cerrar** para una evaluación de cuestionario de 1 fase o **Enviar para revisión** para una evaluación de cuestionario de 2 o 3 fases. Cuando se le solicite que confirme la acción, pulse **Enviar**.

   El sistema cambia el estado a cerrado para un ciclo de vida de dos fases o para revisar un ciclo de vida de tres o cuatro fases. Aún puede acceder a él pero ya no puede editarlo.

##### Resultados

Tras enviar una evaluación de preguntas, lo que sucede a continuación viene determinado por su flujo de trabajo. La evaluación de la pregunta se puede cerrar o moverse a través de un proceso de revisión. Si se mueve a través de un proceso de revisión, un revisor recibe un correo electrónico (si se ha configurado) y lo revisa. Si lo rechazan, se lo devuelven y usted recibirá un correo electrónico. Mire en la lista de sección para mensajes sobre respuestas rechazadas. Abra la sección y busque las preguntas rechazadas. El revisor habrá añadido comentarios o motivos por los que se ha rechazado la respuesta. Realice las correcciones y vuelva a enviarlo.

#### Revisión de una evaluación de cuestionario

`Guía del usuario › Cuestionarios › evaluaciones de cuestionarios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=assessments-reviewing-questionnaire-assessment)

Después de que un usuario complete una evaluación de cuestionario, puede revisarla si está en la etapa de flujo de trabajo de revisión.

##### Acerca de esta tarea

De forma predeterminada, cuando una evaluación de cuestionario está en la etapa de revisión, cualquier persona con derecho a editar la evaluación de cuestionario puede abrirla y revisar las respuestas. Para restringir el acceso, establezca la propiedad **Control de acceso** en la etapa Revisión en **Estricto (los no participantes no pueden ver una tarea en esta etapa)** o **Leer (los no participantes pueden ver pero no editar una tarea en esta etapa)**. Para obtener más información sobre cómo establecer la propiedad **Control de acceso** , consulte [Definición de una etapa estándar](3.3-guia-del-administrador.md#definición-de-una-etapa-estándar).

##### Procedimiento

1. Puede abrir una evaluación de cuestionario para su revisión de una de las maneras siguientes:

   - Abra el correo electrónico y pulse la URL. La página de destino para la evaluación de cuestionario se abre en el navegador web. Pulse **Abrir cuestionario**.
   - Si el correo electrónico no está configurado, pulse **Evaluaciones** > **Evaluaciones de cuestionario**. El sistema mostrará una lista de evaluaciones de cuestionario. Pulse la evaluación de cuestionario que desea revisar. Se muestra la pestaña **Cuestionario**.

     Si desea empezar desde la página de destino de la evaluación de cuestionario, pulse ![Iniciar evaluación de cuestionario](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/questionnaire_landing_page_icon.png). La página de destino para la evaluación de cuestionario abre una nueva pestaña en el navegador web. Pulse **Abrir cuestionario**.
2. Revise las respuestas.

   De forma predeterminada, se muestran todas las preguntas. Para ver sólo las preguntas completadas, necesarias, marcadas o de puntuación baja, puede filtrarlas seleccionando una de las siguientes opciones en el menú desplegable del panel izquierdo: **Ver todas las preguntas**, **Ver preguntas completadas**, **Ver preguntas incompletas**, **Ver preguntas marcadas**, **Ver preguntas necesarias**o **Ver preguntas con puntuaciones bajas**.

   Una pregunta se completa si tiene una respuesta y todos los comentarios y archivos adjuntos necesarios.

   Una pregunta de opción única o múltiple se considera una pregunta de puntuación baja si tiene una puntuación de 0, 1, 2, 3 o 4. Una pregunta con una puntuación de -1 no se tiene en cuenta para la puntuación.

   Sólo para preguntas de opción múltiple, la puntuación final de una pregunta es igual a la suma de las puntuaciones de todas las respuestas seleccionadas por el encuestado. Si alguna de las respuestas seleccionadas tiene una puntuación de -1, entonces la puntuación global de la pregunta se ignora independientemente de las puntuaciones de otras respuestas seleccionadas, y la pregunta no se considera de puntuación baja.
3. Opcional: Si una respuesta requiere más información del encuestado, pulse el icono de distintivo ![Icono de distintivo](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/answer_flag_icon.png), especifique la razón para marcar la respuesta y pulse **Distintivo**.
4. Opcional: Si desea realizar un comentario sobre una respuesta, pulse el icono de comentario ![Icono de comentario](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/answer_comment_icon.png), especifique el comentario y pulse la flecha para enviar el comentario tal como se muestra en la imagen siguiente.

   ![La imagen muestra una pregunta. Una barra de herramientas muestra iconos, incluido el icono Comentario. Cuando se pulsa el icono Comentario, se abre el recuadro de texto. La imagen muestra cómo puede escribir en el cuadro de texto y, a continuación, enviar el comentario.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/submitting_a_comment_icon.png)

   La longitud máxima de un comentario es de 1000 caracteres.

   Para editar un comentario que ha creado, pulse **Editar** ![Icono Editar](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/tfui_edit_icon.jpg). Los comentarios generados que indican que una respuesta se ha copiado de otra evaluación de cuestionario no se pueden editar.

   Para suprimir un comentario que ha creado, pulse **Suprimir** ![Icono Suprimir](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/trash_icon.png). Los siguientes tipos de comentarios no se pueden suprimir:

   - Comentarios generados que indican que se ha copiado una respuesta de otra evaluación de cuestionario
   - Comenta el revisor creado para explicar por qué se ha marcado una pregunta
   - Comentarios que el revisor ha aceptado después de que la pregunta se haya marcado durante el proceso de revisión
5. Cuando haya terminado de revisar todas las respuestas, realice uno de los pasos siguientes.

   - Si todas las respuestas están completas y no necesitan ninguna acción adicional, pulse **Acción** > **Aprobar y cerrar** (ciclo de vida de tres etapas) o **Acción** > **Enviar para aprobación** (ciclo de vida de cuatro etapas). Los nombres de opción pueden ser diferentes en función del GRC Workflow que está dirigiendo el proceso de revisión.
   - Si hay respuestas que ha marcado o comentarios que desea que el encuestado dirija, pulse **Acción** > **Rechazar** en la barra de título.

     La evaluación de cuestionario regresará a la fase de recopilación de información. Se reenviará al encuestado. El encuestado recibe un correo electrónico e inicia la evaluación, responde a las preguntas marcadas y lo reenvía. Cuando regrese a usted, al recibir un correo electrónico, la volverá a abrir y seguirá el mismo proceso para revisarla. Puede aprobarla o volver a rechazarla. En la segunda y posteriores revisiones, puede incluir un comentario en las respuestas aceptadas que anteriormente había rechazado.

##### Resultados

Después de aprobar una evaluación de cuestionario, el tipo de flujo de trabajo determina lo que sucede a continuación.

Si está asignada a un ciclo de vida de tres fases, el sistema la cierra. Tanto el encuestado como el revisor pueden verla, pero ninguno de ellos puede editarla.

Si se asigna a un ciclo de vida de cuatro fases, un aprobador recibe un correo electrónico y lo revisa, siguiendo el mismo proceso que el revisor. El aprobador puede marcar o comentar respuestas y enviarle de nuevo la evaluación. Revise las respuestas y los comentarios marcados y vuelva a enviarla o rechazarla. Si la rechaza, vuelve al encuestado. Cuando el aprobador pulsa **Acción** > **Aprobar**, el sistema cierra la evaluación de cuestionario. En ese momento puede verla pero ya no editarla.

Si el asignado sigue siendo el mismo, los correos electrónicos no se envían. De forma predeterminada, no se envían correos electrónicos cuando las evaluaciones están cerradas.

#### Creación de una evaluación de cuestionario ad hoc

`Guía del usuario › Cuestionarios › evaluaciones de cuestionarios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=assessments-creating-ad-hoc-questionnaire-assessment)

Utilice una evaluación de cuestionario ad hoc para crear una única evaluación de cuestionario independiente de un programa.

##### Acerca de esta tarea

La evaluación de cuestionario se puede asignar a otro usuario, no solo al usuario que la ha creado.

##### Procedimiento

1. Haga clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Activos** y seleccione el activo para el que desea crear una evaluación de cuestionario. Por ejemplo, haga clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Activos** > **Recursos** y haga clic en un recurso.
2. En la pestaña **Tarea** , expanda la sección **Evaluación, problemas y vulnerabilidades** .
3. Pulse **Nuevo**.

   Se abre una vista en la que puede crear una nueva evaluación de cuestionario. El activo donde se ha iniciado se asigna a la evaluación de cuestionario.
4. Asigne un ciclo de vida a la evaluación de cuestionario.
5. Añada información opcional.
6. Pulse **Guardar**.

   Se abre otra pestaña **Tarea** donde puede trabajar con la evaluación del cuestionario.
7. Pulse **Seleccionar plantilla de cuestionario** y asigne una plantilla a la evaluación de cuestionario.
8. Haga clic en la ficha **Cuestionario** para abrir la evaluación de cuestionario y responder a las preguntas.

   Se inicia el flujo de trabajo que se ha asignado a la evaluación de cuestionario.
9. Responda a las preguntas. Puede pulsar **Guardar borrador** para guardar o dejar que la evaluación se guarde automáticamente.

   Cuando haya terminado de responder a todas las preguntas, pulse **Acción**. Seleccione la acción **Enviar y cerrar** para una evaluación de cuestionario de 1 fase o **Enviar para revisión** para una evaluación de cuestionario de 2 o 3 fases. Cuando se le solicite que confirme la acción, pulse **Enviar**.

### Programas

`Guía del usuario › Cuestionarios` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=questionnaires-programs)

Utilice programas para definir e iniciar evaluaciones de cuestionario.

Antes de utilizar programas, consulte [Visión general del cuestionario](#resumen-del-cuestionario).

Un programa define las personas que participan en una evaluación, incluido el gestor responsable, los revisores y los aprobadores. También define la plantilla de cuestionario que utiliza el programa. Un programa se basa en un activo subyacente que se desea evaluar. Estos activos pueden ser procesos, subprocesos, recursos, empleados, proveedores o compromisos.

Los programas basados en empleados crean evaluaciones de cuestionario que se envían a los empleados. Los programas basados en recursos, procesos, subprocesos, proveedores o compromisos se basan en objetos seleccionados y se envían al propietario principal de los objetos. Si un empleado no tiene una cuenta de empleado o un activo no tiene propietario primario, no hay ningún encuestado para la evaluación del cuestionario.

En primer lugar, cree un objeto de programa y asígnele la plantilla de cuestionario y los activos. Cuando se inicia, la etapa de evaluación del cuestionario se establece en la recopilación de información. Un flujo de trabajo se inicia porque los flujos de trabajo se utilizan para impulsar el proceso de revisión. Una evaluación de cuestionario pasa de una fase a la siguiente cuando un usuario la envía, la rechaza o la confirma. El propietario de la fase puede proceder del activo subyacente o ser el propietario del programa, si tiene la última fase.

Puede actualizar los activos que se asignan a un programa y volver a lanzaros si se han añadido nuevos activos después del lanzamiento inicial.

Los usuarios que inician programas deben tener permisos de lectura para la evaluación de cuestionario y los objetos de la plantilla del cuestionario. Configure los permisos de forma que solo los propietarios de los programas puedan suprimir las evaluaciones de cuestionario.

#### Iniciar un programa y copiar respuestas

Al iniciar un programa, puede incluir respuestas de un programa anterior en la evaluación del cuestionario. Por ejemplo, este año puede enviar evaluaciones de cuestionario que sean iguales o similares a las que envió el año pasado, y puede incluir las respuestas del año pasado. El destinatario recibe evaluaciones de cuestionario en las que algunas o todas las preguntas incluyen respuestas que el destinatario puede conservar o cambiar.

Puede utilizar la plantilla de cuestionario del programa anterior o guardarla como una plantilla nueva y realizar cambios. Los dos programas no tienen que utilizar la misma plantilla de cuestionario. Para copiar respuestas, las preguntas deben conservar sus identificadores internos de una plantilla de cuestionario a otra. Puede realizar ligeros cambios en las preguntas de la nueva plantilla de cuestionario si la pregunta permanece fundamentalmente igual. Puede añadir preguntas nuevas y suprimir otras. No vuelva a escribir una pregunta existente porque las respuestas que ya no se aplican se pueden copiar en ella.

#### Creación y configuración de un programa

`Guía del usuario › Cuestionarios › Programas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=programs-creating-configuring-program)

Cree, configure e inicie un programa para crear evaluaciones de cuestionario.

##### Acerca de esta tarea

En el recuadro desplegable **Ciclo de vida** , puede seleccionar un ciclo de vida de **2 Etapa**, **3 Etapa**o **4 Etapa** . No hay revisión ni aprobación en un ciclo de vida de **2 etapas** . El encuestado rellena el cuestionario y se envía. Un ciclo de vida de programa de **2 etapas** tiene las etapas siguientes:

1. Recopilación de información
2. Cerrado

Un ciclo de vida de programa **3 Etapa (con revisión)** añade un paso de revisión al ciclo de vida. Después de que un encuestado rellene una evaluación de cuestionario, la evaluación de cuestionario se asigna a un revisor para comprobarlo. El revisor puede elegir aceptar o rechazar el cuestionario. Si se rechaza, el cuestionario se devuelve al encuestado, con comentarios si es necesario, y el programa vuelve a la etapa de recopilación de información. Si se acepta, la evaluación de cuestionario pasa a la etapa Cerrado. Un ciclo de vida de programa de **3 etapas** tiene las etapas siguientes:

1. Recopilación de información
2. En revisión
3. Cerrado

Un ciclo de vida de programa **4 Etapa (con revisión y aprobación)** añade una etapa En aprobación en la que las evaluaciones de cuestionario pueden existir sin estar cerradas. Un ciclo de vida de programa de **4 etapas** tiene las etapas siguientes:

1. Recopilación de información
2. En revisión
3. En aprobación
4. Cerrado

##### Procedimiento

1. Abra el **Menú primario** y seleccione **Evaluaciones** > **Programas**.
2. Pulse **Nuevo**.
3. Complete la siguiente información en el formulario para crear el nuevo objeto de programa:

   1. En el recuadro **Nombre** , especifique el nombre del programa.
   2. En el cuadro **Tipo** , seleccione **Cuestionario de clasificación** o **Cuestionario de evaluación**.
   3. En el recuadro desplegable **Propietario primario** , seleccione un usuario de la lista de nombres **Utilizados recientemente** o especifique un nombre y seleccione en la lista de usuarios que se muestra. Asimismo, puede especificar un **Revisor**, **Aprobador** y **Propietarios adicionales**.
   4. Pulse **Seleccionar entidad de negocios primaria**, seleccione una entidad de negocios y pulse **Terminado**.
   5. En el recuadro desplegable **Ciclo de vida** , seleccione el número de etapas que desea para el flujo de trabajo.
   6. Opcional: Puede especificar una **Fecha de vencimiento de evaluación** especificando una fecha o seleccionando una fecha del calendario.
4. Cuando haya terminado de completar el formulario, pulse **Guardar**.

   La página del programa se abre en la pestaña **Tarea**.
5. Complete la información siguiente en la pestaña **Tarea** .

   1. Pulse **Seleccionar cuestionario de la biblioteca**, seleccione un cuestionario y pulse **Terminado**.
   2. En el cuadro **Activos en programa** , seleccione un tipo de activo: **Activos de TI**, **Procesos**, **Subprocesos**, **Proveedores**, **Compromisos**o **Empleados**.

      Pulse **Añadir** y seleccione los recursos. Cuando haya seleccionado los recursos que desea, pulse **Terminado**.

      Repita este paso para todos los tipos de activos que desee elegir.

   El programa ya está listo para su inicio. Antes de lanzar un programa, asegúrese de que los activos que elija tengan cuentas de empleados o propietarios primarios.

##### Qué hacer a continuación

Inicie el programa. Para obtener más información, consulte [Inicio de un programa](#lanzamiento-de-un-programa).

#### Lanzamiento de un programa

`Guía del usuario › Cuestionarios › Programas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=programs-launching-program)

Es posible lanzar un programa para crear instancias de evaluación de cuestionario.

##### Antes de empezar

- Cree y configure un objeto de programa. Para obtener más información, consulte [Creación y configuración de un programa](#creación-y-configuración-de-un-programa).
- Verifique que los activos cuentan con nombres de empleado o propietarios primarios.

##### Acerca de esta tarea

Cuando se inicia un programa por primera vez, el sistema crea instancias de la evaluación de cuestionario. Puede volver a iniciarla si ha añadido nuevos activos a la misma. Cuando se inicia un programa por segunda vez, el sistema crea solo evaluaciones de cuestionario para los nuevos activos. Las evaluaciones de cuestionario existentes y sin cambiar no se ven afectadas.

##### Procedimiento

1. Para empezar a iniciar un programa, elija uno de los pasos siguientes:

   1. Si ya está en la pestaña **Tarea** de la página del programa, pulse **Iniciar** en el recuadro **Gestión de evaluaciones** .
   2. De lo contrario, abra el **Menú primario** y seleccione **Evaluaciones** > **Programas**. El sistema mostrará una lista de programas.

      Elija el programa que desea iniciar y pulse **Iniciar** en la columna **Iniciar programa** . El sistema muestra un mensaje con el número de nuevas instancias de evaluación de cuestionario que se crearán. Si ya se ha creado una evaluación de cuestionario para el activo especificado, dicha evaluación no se incluye en el número de nuevas evaluaciones del mensaje.
2. Si se visualiza **Programa para copiar respuestas de** , puede seleccionar un programa de origen del que desee copiar respuestas.

   Para obtener más información sobre cómo copiar respuestas de otro programa, consulte [Inicio de un programa y copia de respuestas](#programas).
3. Pulse **Iniciar**.

##### Resultados

El sistema:

- Crea un objeto de evaluación de cuestionario por empleado, recurso, proceso, subproceso, proveedor o compromiso del programa. Hace esto en un proceso en segundo plano.
- Inicia el flujo de trabajo para las evaluaciones de cuestionario.
- Envía correos electrónicos a los encuestados.
- Bloquea la plantilla de cuestionario.

##### Qué hacer a continuación

1. Revise el estado del lanzamiento del programa.

   1. Si ya está en la pestaña **Tarea** de la página del programa, vaya al paso 1b. De lo contrario, abra el **Menú primario** y seleccione **Evaluaciones** > **Programas**. Pulse el programa para el que desea ver el estado.
   2. En la pestaña **Tarea**, pulse **Vista** en el recuadro **Gestión de evaluación**. La ventana **Historial de procesos** muestra el estado de todos los procesos.
2. Revise las plantillas de cuestionario que el programa ha creado. Verifique que los activos son correctos. Haga las correcciones necesarias y reinicie el programa.

   Para suprimir evaluaciones de cuestionario que se hayan creado por error, es necesario disociar la evaluación de cuestionario del activo.

## Aplicación de firmas y bloqueos

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-applying-signatures-locks)

Puede añadir una firma para iniciar la sesión en un objeto para indicar que el objeto cumple su aprobación. No tiene facultades de ejecución y no impide que el elemento se modifique después de la aprobación. Sin embargo, las modificaciones en el objeto se impiden si los valores del sistema se configuran para aplicar automáticamente un bloqueo en el objeto firmado. Se puede establecer otro valor del sistema para bloquear los hijos del objeto de un tipo de objeto determinado cuando el padre está bloqueado.

Puede tener un bloqueo sobre un objeto con o sin una firma.

### Firmas

Para añadir o revocar una firma, debe ser miembro de un grupo con privilegios de firma.

Si el valor **Applications** > **GRCM** > **Firma** > **Cascada** > **< tipo_objeto_padre>** se establece en un tipo de objeto hijo, una firma añadida al padre también se coloca en sus hijos del tipo de objeto especificado.

Si el valor **Applications** > **GRCM** > **Firma** > **Modalidad** se establece en **Autolock** en el sistema, cuando añade una firma en un objeto, el objeto se bloquea y no se puede modificar hasta que revoca la firma o un administrador desbloquea el objeto.

Para obtener más información sobre cómo añadir firmas, consulte [Adición de una firma](#añadir-una-firma).

Para obtener más información sobre la revocación de firmas, consulte [Revocación de firmas](#revocación-de-firmas).

### Bloqueos

Un bloqueo en un objeto se comporta de la misma manera si bloquea un objeto manualmente o si el bloqueo se aplica a un objeto como resultado de una firma añadida.

Un icono de bloqueo cerrado ![Desbloquear recurso](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-padlock.jpg) que aparece junto al nombre del objeto en una vista de cuadrícula o en la página del objeto indica un objeto bloqueado. Dado que se puede replicar un bloqueo en la jerarquía de objetos, un objeto puede heredar varios bloqueos. No se puede modificar un objeto con varios bloqueos hasta que se eliminen todos los bloqueos.

Si el valor **Aplicaciones** > **GRCM** > **Objetos bloqueados** > **Bloquear tipos hijo** > **< tipo_objeto_padre>** se establece en un tipo de objeto hijo, cuando el padre está bloqueado, todos sus objetos hijo del tipo especificado están bloqueados.

Sólo se puede colocar un bloqueo activo en un objeto. Se pueden heredar varios bloqueos de objetos padres cuando esos objetos están bloqueados.

Para bloquear o desbloquear un objeto, debe tener los permisos necesarios establecidos en su cuenta. Para obtener más información, consulte al administrador del sistema para obtener más detalles.

No puede realizar las siguientes acciones en un objeto bloqueado:

- Mueva el objeto a una nueva ubicación.
- Edite las propiedades.
- Cambiar el nombre del objeto.
- Suprima el objeto.
- Asocie otros objetos con el objeto.

Puede realizar las siguientes acciones en un objeto bloqueado:

- Ver los detalles del objeto.
- Copiar el objeto en una nueva ubicación. La copia recién creada se desbloquea.

### Añadir una firma

`Guía del usuario › Aplicación de firmas y bloqueos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=locks-adding-signature)

Si el grupo de usuarios tiene permisos para añadir una firma para el tipo de objeto, puede añadir una firma para iniciar la sesión en un objeto.

#### Acerca de esta tarea

Si el valor **Aplicaciones** > **GRCM** > **Firma** > **Modalidad** se establece en **Autolock** en el sistema, cuando añade una Firma en un objeto, el objeto se bloquea y no se puede modificar hasta que revoque la firma o un administrador desbloquee el objeto.

Cuando un objeto padre tiene un bloqueo de firma aplicado, sólo se puede colocar un bloqueo activo en dicho objeto. Se pueden heredar varios bloqueos de objetos padre.

#### Procedimiento

1. Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)**.
2. Expanda las categorías para ver los tipos de objeto.
3. Seleccione el tipo de objeto con el que desea trabajar.

   Se abre una vista de cuadrícula.
4. Pulse el nombre del objeto con el que desea trabajar.
5. Pulse la pestaña **Admin** .

   Si la pestaña **Administrador** no está disponible, la plantilla de rol asociada a la cuenta de usuario no tiene el permiso necesario para ver la pestaña.
6. En la sección **Hijos** , pulse la pestaña **Firmas** .
7. Pulse **Nuevo**.
8. En la pestaña **Nueva firma** , puede especificar una **Descripción** y **Comentarios**.
9. Haga clic en **Guardar** para crear la nueva firma.

### Revocación de firmas

`Guía del usuario › Aplicación de firmas y bloqueos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=locks-revoking-signatures)

Puede revocar una firma o iniciar la sesión en una firma que ha añadido manualmente. Con el flujo de trabajo predefinido, Revocación de firma, sólo puede revocar una firma que haya creado.

#### Acerca de esta tarea

Para desbloquear un objeto con un bloqueo de firma y conservar la firma, el grupo debe añadirse al valor de **Applications** > **GRCM** > **Signature** > **Permission** > `<object_type>` donde `<object_type>` es el tipo de objeto del objeto con la firma.

Todos losbloqueos de firma (incluidos los bloqueos heredados) se debeneliminar del objeto antes de que se pueda editar. Para eliminar un bloqueo heredado, utilice el flujo de trabajo de **Revocación de firma** para habilitar la acción para revocar la firma del objeto padre.

#### Procedimiento

1. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_menu_icon_task_focused_ui.jpg)** > **Solución. Configuración** > **Flujos de trabajo** > **Revocar firma**.
2. Seleccione la acción entre las etapas **Inicio** y **Fin** .

   Se visualiza el panel **Propiedades de acción**.
3. Expanda la sección **Validaciones y operaciones** .
4. Pulse **Desbloquear proceso padre-Bloquear o desbloquear objetos**.
5. En el panel **Operaciones** , pulse **Editar** para **Objetos de destino**.
6. En el campo **Tipo de objeto relacionado** , seleccione el tipo de objeto para el que desea revocar la firma. Pulse **Publicar**.
7. Abra el objeto bloqueado. En la sección de la pestaña Admin donde se listan los hijos del objeto, la firma se muestra como un hijo del objeto bloqueado. Pulse el nombre de la firma que desea revocar.
8. Pulse **Acciones** > **Iniciar revocación de firma**.
9. Cuando se le solicite que confirme la acción, pulse **Continuar y cerrar pestaña**.

   El campo **Estado** para la firma muestra que está **Revocado**.

### Visualización de firmas

`Guía del usuario › Aplicación de firmas y bloqueos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=locks-viewing-signatures)

Puede ver una firma asociada con un objeto.

#### Procedimiento

1. Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)**.
2. Expanda las categorías para ver los tipos de objeto.
3. Seleccione el tipo de objeto con el que desea trabajar.

   Se abre una vista de cuadrícula.
4. Pulse el nombre del objeto con el que desea trabajar.
5. Pulse la pestaña **Admin** .

   Si la pestaña **Administrador** no está disponible, la plantilla de rol asociada a la cuenta de usuario no tiene el permiso necesario para ver la pestaña.
6. En la sección **Hijos** , pulse la pestaña **Firmas** .

   Las firmas para el objeto se listan en una vista de cuadrícula. Para ver si hay una firma en vigor, pulse la firma y compruebe el campo **Estado**.

### Bloqueo y desbloqueo de objetos

`Guía del usuario › Aplicación de firmas y bloqueos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=locks-locking-unlocking-objects)

Los tipos de objetos que puede bloquear o desbloquear están determinados por un valor del sistema y sus permisos de acceso. Sólo puede bloquear objetos de primer nivel.

En una vista de cuadrícula, las opciones **Bloquear** y **Bloquear** se visualizan cuando selecciona el recuadro de selección de un objeto que puede bloquear o desbloquear.

En otras vistas, se visualiza un icono ![Bloquear recurso](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-padlock-unlock.jpg) o ![Desbloquear recurso](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-padlock.jpg) junto al nombre de un objeto. Cuando un objeto está bloqueado, se visualiza el icono de bloqueo cerrado ![Desbloquear](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-padlock.jpg) . Un icono de bloqueo cerrado gris indica que el objeto ha heredado el bloqueo. Para eliminar un bloqueo heredado, debe desbloquear el objeto padre.

#### Acerca de esta tarea

Cuando se bloquea un objeto padre y se especifica el valor de aplicación para bloquear objetos hijo, sus objetos hijo del tipo especificado en el valor también se bloquean.

Al desbloquear un objeto, el icono de bloqueo cerrado se sustituye por un icono de bloqueo abierto en el objeto y se eliminan los bloqueos heredados de cualquier objeto hijo asociado. Cuando desbloquea un objeto con firmas, las firmas siguen en vigor y no se revocan.

#### Procedimiento

1. Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)**.
2. Expanda las categorías para ver los tipos de objeto.
3. Seleccione el tipo de objeto con el que desea trabajar.

   Se abre una vista de cuadrícula.
4. Lleve a cabo una de las siguientes acciones:

   - Para desbloquear uno o más objetos, marque el recuadro de selección de cada objeto que desee desbloquear. Pulse **Desbloquear** ![Desbloquear](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-padlock-unlock.jpg).
   - Para bloquear uno o más objetos, marque el recuadro de selección de cada objeto que desee bloquear. Pulse **Bloquear** ![Bloquear](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/icon-padlock.jpg).

   Las opciones **Desbloquear** y **Bloquear** sólo están disponibles para los tipos de objeto que soportan el bloqueo y sólo cuando los permisos de acceso permiten el bloqueo y el desbloqueo.

## Utilización de objetos de OpenPages Platform

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-openpages-platform-objects)

Los objetos de plataforma son los objetos fundamentales que componen el núcleo de OpenPages®. Forman parte de cada sistema OpenPages , independientemente de las soluciones configuradas.

### Entidades empresariales

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-business-entities)

Las entidades empresariales son representaciones abstractas de la estructura empresarial. Una entidad de negocio puede contener subentidades (como departamentos, unidades de negocio o ubicaciones geográficas). La estructura de la entidad que crea depende de las necesidades empresariales. Por ejemplo, puede crear una entidad padre para las oficinas centrales de la empresa y una subentidad para cada ubicación o departamento. Es posible que también desee representar una estructura de entidad legal y una estructura de entidad de negocios.

Las entidades de negocios también se utilizan para organizar datos de biblioteca, como las bibliotecas de control o riesgo, o contenido regulador (por ejemplo, leyes, normativas y estándares).

Cuando configure la jerarquía de entidades empresariales, trabaje con su asesor de IBM® OpenPages® . La estructura de la entidad de negocios afecta al tipo y calidad de la información que se puede extraer de la aplicación.

En IBM OpenPages Internal Audit Management , las entidades empresariales también modelan la estructura organizativa de auditoría interna, lo que facilita la creación de informes y la seguridad para el equipo de auditoría interna. La estructura organizativa de la auditoría interna es una entidad de nivel superior para minimizar la posibilidad de otorgar de manera accidental a un usuario empresarial acceso a información de la auditoría interna. Los elementos del universo de la auditoría interna que posee el equipo de auditoría interna están asociados a la entidad de negocios del equipo. Se puede crear otra estructura de entidad de negocios de nivel superior para organizar auditorías confidenciales, proporcionando una seguridad especial a esas auditorías. La entidad de negocios también se puede utilizar para organizar una biblioteca de plantillas de contenido de auditoría.

### Evaluaciones de riesgos

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-risk-assessments)

Las evaluaciones de riesgos le ofrecen la posibilidad de evaluar y notificar pasivos potenciales para un conjunto de entidades o procesos empresariales. Un objeto Evaluación de riesgo contiene los nombres del asesor y revisor, los marcos de tiempo de la evaluación y el estado de la evaluación. Utilice una evaluación de riesgo para gestionar el riesgo de un proceso de autoevaluación. Asocie los objetos Riesgo a una evaluación de riesgo para crear un enlace entre la entidad de negocios y los riesgos. Por ejemplo, cree una evaluación de riesgo para evaluar riesgos operativos, como un fraude o robo externo, un fraude internos, daños físicos a la propiedad o interrupción de negocio.

### Evaluaciones de evaluación de riesgos

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-risk-assessment-evals)

Los objetos Evaluación de evaluación de riesgo son similares a los objetos Evaluación de riesgo, excepto que se instancian como hijos de las evaluaciones de riesgo. Almacenan los datos de evaluación de riesgo.

### Objetivos de control

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-control-objectives)

Un objetivo de control es un objeto de evaluación que define las categorías de riesgo para un proceso o subproceso.

Los objetivos de control definen las categorías de conformidad COSO que intentan mitigar los controles. Los objetivos de control se pueden clasificar en categorías como Conformidad, Creación de informes financieros, Estrategia, Operaciones o Desconocido.

Una vez se ha identificado un objetivo de control, se pueden definir los riesgos que pertenecen a ese objetivo de control. En la mayoría de los casos, cada objetivo de control tiene un riesgo asociado. Sin embargo, puede tener asociado más de un riesgo. Por ejemplo, una compañía de servicios financieros emplea vendedores que conocen los estándares éticos necesarios. El departamento de RRHH configura un objetivo de control denominado 'Personal'. Un riesgo asociado con el objetivo de control es: «“Los empleados hacen operaciones comerciales que entran en conflicto con los objetivos de la empresa en cuanto a la ética comercial y el comercio justo”».

De forma predeterminada, un objetivo de control de OpenPages® Internal Audit Management está inhabilitado. Este objeto no se utiliza a menudo, excepto para alinearlo con otras soluciones que pueden utilizarlo.

### Procesos

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-processes)

Los procesos representan las principales actividades empresariales globales dentro de una entidad empresarial que están sujetas a riesgo. Los procesos residen en áreas como la creación de informes financieros, la conformidad y la seguridad de la información. Por ejemplo, los procesos del departamento de cuentas por cobrar, como el proceso desde el pedido hasta el cobro se pueden mejorar con controles para protegerse contra los riesgos de creación de informes financieros, por ejemplo, contra un comportamiento fraudulento o contra imprecisiones de la creación de informes financieros.

En OpenPages® Internal Audit Management, los procesos también se utilizan en las auditorías de ámbito. Las auditorías pueden copiar procesos creados por la entidad de negocios o crear sus propios procesos.

### Evaluaciones de proceso

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-process-evals)

Los objetos de evaluación de proceso son hijos de los objetos de proceso y se utilizan para capturar valores de medida de proceso para fines de tendencia.

Cuando los periodos de creación de informes no están alineado con los ciclos de evaluación, puede utilizar objetos Evaluación de proceso para capturar varios ciclos de evaluación dentro de un único periodo de creación de informes.

### Subprocesos

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-sub-processes)

Un subproceso es un componente de un proceso. Se utiliza para dividir procesos en unidades más pequeñas con fines de evaluación. Por ejemplo, un proceso financiero desde el pedido hasta el cobro puede componerse de varios subprocesos como acreedores, compras y contabilidad general. Cualquiera de estos subprocesos podría exponer a la entidad de negocios a un riesgo, lo cual es posible mejorar utilizando controles.

### Controles

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-controls)

Los controles son políticas y procedimientos que garantizan que se realizan respuestas de mitigación de riesgos.

Una vez identificados los riesgos que llevan consigo sus prácticas, establezca controles, como aprobaciones, autorizaciones y verificaciones. Estos controles eliminan, limitan o transfieren estos riesgos.

Los controles proporcionan prevención o detección de riesgos. Los controles están asociados con pruebas que garantizan que un control el eficaz. Por ejemplo, el departamento de recursos humanos identifica un riesgo en el nuevo proceso de contratación. El proceso no cumple con las normas y directrices para la diversidad y discriminación. Defina los controles para mitigar este riesgo, como establecer políticas y procedimientos de contratación, y lleve a cabo una formación obligatoria para los gestores de contratación.

En IBM OpenPages® Internal Audit Management utilice Controles para crear un modelo detallado de los controles que existen o que desea aplicar en las actividades que se auditan. Si se comparten con Negocio, los controles se pueden clasificar por separado por Auditoría interna y por Negocio.

### Planes de conformidad y Temas de conformidad

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-compliance-plans-compliance-themes)

Los objetos Plan de conformidad y Tema de conformidad se utilizan con IBM OpenPages® Regulatory Compliance Management.

Los objetos Planes de conformidad permiten la creación de un plan general para aplicar los requisitos normativos en un valor estructurado, o para estructurar un conjunto de tareas reguladoras. Por ejemplo, se puede crear un Plan de conformidad para hacer un seguimiento de las tareas reguladoras, o para llevar a cabo evaluaciones de conformidad en varios requisitos reguladores. Se pueden agrupar uno o varios temas de conformidad en un plan de conformidad general para la organización.

Los Temas de conformidad permiten organizar requisitos normativos en temas a efectos de evaluación. Este enfoque permite evaluar los requisitos de conformidad más allá del típico enfoque de entidad de negocios, agrupando los requisitos normativos en temas que afectan a toda la organización. Los temas de muestra pueden incluir privacidad de datos, gobierno y responsabilidad, etc. Esto permite evaluar el impacto de las normativas no sólo dentro de las entidades de negocios, sino entre temas que tocan varias áreas de la organización.

Puede desplegar un Tema de conformidad en varias entidades de negocio. O bien puede desplegar varios temas en una única entidad de negocios. RCM Theme Deployer crea la estructura de forma automática, incluidos el plan de conformidad, el tema de conformidad y los registros de evaluación de requisitos relevantes debajo del tema, y los enlaza con los objetos de control relevantes.

Por ejemplo, supongamos que desea desplegar el tema de conformidad de privacidad de datos en la entidad de negocios Servicios de agencia. El tema de conformidad de privacidad de datos tiene 35 requisitos relacionados. Algunos de estos requisitos tienen controles asociados. Al desplegar el tema de privacidad de datos, se crea un objeto Evaluación de requisitos para la entidad de negocios para cada uno de los 35 requisitos del tema. Ahora tiene los objetos de evaluación de requisitos que necesita para evaluar el grado de conformidad con los requisitos de la entidad de negocios.

Puede elegir cómo o si se van a crear o enlazar objetos de control. Puede crear o enlazar controles, o bien puede elegir no gestionar objetos de control al desplegar un tema.

Por ejemplo, imagine que despliega el tema de conformidad de privacidad de datos y elige crear o enlazar controles. Las asociaciones entre controles y objetos de evaluación de requisitos se configuran automáticamente en función de los pasos siguientes:

- ¿La entidad Servicios de agencia ya tiene un control asociado relevante para el requisito? Si es así, se crea un enlace entre el control y la evaluación del requisito.
- Si la entidad Servicios de agencia no tiene ningún control asociado que sea relevante, ¿existe un control en la biblioteca RCM que sea relevante? Si es así, se crea un enlace entre el control de la biblioteca y la evaluación del requisito.
- Si la entidad Servicios de agencia no tiene un control asociado que sea relevante y tampoco hay objetos de control relevantes en la biblioteca, se crea un nuevo objeto de control y se enlaza con la evaluación de requisitos.

En este ejemplo, el requisito de privacidad de datos 1 se enlaza con un control denominado Control de privacidad de datos 1 (Data Privacy Control 1). Servicios de agencia todavía no tiene este control. Por lo tanto, la evaluación del requisito de privacidad de datos 1 (Data Privacy Requirement Evaluation 1) se enlaza con el control en la biblioteca de controles (Controls Library).

![Diagrama de flujo que muestra el tema Data Privacy que se despliega en los servicios de agencia.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/op_depl_theme_eg1.jpg)

#### Despliegue de varios temas de conformidad en una entidad de negocios

`Guía del usuario › Uso de objetos de OpenPages Platform › Planes de conformidad y Temas de conformidad` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=themes-deploying-multiple-compliance-business-entity)

Puede desplegar varios temas de conformidad a una entidad de negocios.

##### Procedimiento

1. Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Cumplimiento de la normativa** > **Planes de cumplimiento**.

   Utilice filtros para buscar el plan que desea utilizar.
2. Pulse el plan de conformidad que contenga los temas de conformidad que desea desplegar.
3. Pulse **Iniciar** en **Administración de plan de conformidad**.

   Se muestra la ventana **Desplegar temas de conformidad en entidad**.
4. Seleccione los temas de conformidad que desee desplegar. Pulse **Siguiente**.
5. Seleccione cómo desplegar los objetos de control relacionados.
6. Pulse **Siguiente**.
7. Revise la información de la pestaña **Vista previa** .
8. Pulse **Enviar**.

   Se inicia el proceso de despliegue. La página **Historial de proceso** muestra el progreso. Pulse **Renovar** para actualizar la página.
9. Cierre la ventana **Historial de procesos** .

   > **Nota:** Para ver una lista de todos los procesos que está ejecutando, haga clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_menu_icon_task_focused_ui.jpg)** > **Otros** > **Procesos de fondo**.

#### Despliegue de un tema de conformidad en varias entidades de negocio

`Guía del usuario › Uso de objetos de OpenPages Platform › Planes de conformidad y Temas de conformidad` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=themes-deploying-compliance-theme-multiple-business-entities)

Puede desplegar un tema de conformidad en varias entidades de negocio.

##### Acerca de esta tarea

Cuando se despliega un tema de conformidad en una o varias entidades de negocio, los objetos y asociaciones que necesita para las evaluaciones de requisitos se crean de forma automática. También puede optar por crear o enlazar a los controles asociados con los requisitos asociados con el tema. También puede elegir no crear controles o enlaces a estos.

##### Procedimiento

1. Haz clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Cumplimiento de la normativa** > **Temas de cumplimiento**.

   Utilice filtros para buscar el tema que desea desplegar.
2. Pulse el Tema de conformidad que desea desplegar.
3. Pulse **Iniciar** en **Administración de temas de conformidad**.

   Se muestra la ventana **Desplegar temas de conformidad en entidades seleccionadas**.
4. Seleccione las entidades de negocio en las que desea desplegar el tema de conformidad. Pulse **Siguiente**.

   > **Nota:** Los campos de texto enriquecido se muestran en texto sin formato en RCM Theme Deployer.
5. Seleccione cómo desplegar los objetos de control relacionados.

   - **Crear/Enlazar**: Si todavía no se ha asociado el control de biblioteca con la entidad de negocio y si no hubiera un objeto Control debajo de la entidad de negocio en el que correlacionar los objetos de Evaluación de requisitos, RCM Theme Deployer crea un nuevo objeto Control.
   - **Enlazar**: Si la entidad de negocio tiene un objeto Control relevante, RCM Theme Deployer crea un enlace entre el objeto de Evaluación de requisitos y el Control perteneciente al ámbito de la entidad de negocio.
   - **Ninguno**: No ser realiza ninguna acción. RCM Theme Deployer no crea ni enlaza objetos Control.
6. Pulse **Siguiente**.
7. Revise la información de la pestaña **Vista previa** .
8. Pulse **Enviar**.

   Se inicia el proceso de despliegue. La página **Historial de proceso** muestra el progreso. Pulse **Renovar** para actualizar la página.
9. Cierre la ventana **Historial de procesos** .

   > **Nota:** Para ver una lista de todos los procesos que está ejecutando, haga clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/settings_menu_icon_task_focused_ui.jpg)** > **Otros** > **Procesos de fondo**.

### Evaluaciones de control

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-control-evals)

Los objetos de evaluación de riesgo son similares a los objetos de evaluación de riesgo, excepto que se crean como hijos de controles. Almacenan datos de gestión de control. Cuando los ciclos de evaluación de control y periodos de informes no están alineados, utilice objetos Evaluación de control para capturar varios ciclos de evaluación de gestión dentro de un único periodo de creación de informes.

### Riesgos

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-risks)

Los riesgos son pasivos potenciales. Los riesgos pueden estar asociados a procesos empresariales, entidades de negocios o en conformidad con un mandato. Cada riesgo tiene controles que proporcionan protección contra el riesgo. Los controles ayudan a reducir las consecuencias que son resultado del riesgo. Utilice el objeto Riesgo para categorizar riesgos; capturar la frecuencia, la puntuación y la gravedad de los datos de riesgo observados y calculados; y para ver informes para identificar los elementos de riesgo principales. Por ejemplo, la cuenta En metálico tiene un proceso denominado Nómina. Un riesgo potencial que se puede producir en la nómina es un desembolso de nómina duplicado o la creación de desembolsos de nómina ficticios. La identificación de riesgos en curso es un componente principal del desarrollo de un proyecto de documentación de controles financieros.

En OpenPages® Internal Audit Management, un riesgo que se comparte entre una auditoría interna y la empresa se puede clasificar por separado.

### Evaluaciones de riesgos

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-risk-evals)

Los objetos Evaluación de riesgo son hijos de los objetos Riesgo y se utilizan para capturar valores de medida de riesgo a efectos de tendencia. Cuando los periodos de creación de informes no están alineado con los ciclos de evaluación de riesgo, puede utilizar objetos Evaluación de riesgo para capturar varios ciclos de evaluación dentro de un único periodo de creación de informes..

### Planes de pruebas

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-test-plans)

Un plan de prueba es un contenedor para pruebas y se puede asociar con objetos de control padre y objetos hijo, como por ejemplo Resultados de prueba y Problemas. Determine la efectividad operativa de un control realizando pruebas detalladas y documentando los resultados. Los planes de prueba describen los mecanismos que determinan si un control es efectivo. Por ejemplo, un control de prueba sería: «“Recursos Humanos autoriza cambios en el estado del empleado”». Una prueba de este control sería: «“Verificar el sello de autorización de RRHH en los registros de empleados nuevos”». La prueba verifica que el nuevo control está implementado y en uso.  Un resultado de la prueba es la información que se obtiene tras la ejecución de un plan de prueba.

#### Planes de pruebas

`Guía del usuario › Uso de objetos de OpenPages Platform › Planes de pruebas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=plans-test)

Un plan de prueba es un contenedor para pruebas y se puede asociar con objetos de control padre y objetos hijo, como por ejemplo Resultados de prueba y Problemas. Determine la efectividad operativa de un control realizando pruebas detalladas y documentando los resultados. Los planes de prueba describen los mecanismos que determinan si un control es efectivo. Por ejemplo, un control de prueba sería: «“Recursos Humanos autoriza cambios en el estado del empleado”». Una prueba de este control sería: «“Verificar el sello de autorización de RRHH en los registros de empleados nuevos”». La prueba verifica que el nuevo control está implementado y en uso.

La configuración predeterminada de OpenPages® Internal Audit Management utiliza el objeto Informe en lugar del plan de prueba y el resultado de la prueba. El objeto Auditoría necesita acceder a estos elementos porque se utilizan a menudo para documentar pruebas empresariales.

#### Resultados de prueba

`Guía del usuario › Uso de objetos de OpenPages Platform › Planes de pruebas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=plans-test-results)

Un resultado de prueba es la información que se obtiene de la ejecución de un plan de prueba.

La configuración predeterminada de OpenPages® Internal Audit Management utiliza el objeto Informe en lugar del plan de prueba y el resultado de la prueba. El objeto Auditoría necesita acceder a estos elementos porque se utilizan a menudo para documentar pruebas empresariales.

### Problemas y elementos de acción

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-issue-action-items)

Aunque los problemas se generan en áreas donde los controles internos no se implementan correctamente, utilice el objeto Problema para documentar un problema asociado a cualquier tipo de objeto. Por ejemplo, una prueba se ha asociado con un control, pero la prueba ha fallado la última vez que se ha completado. Este problema potencial puede resaltarse capturándolo en un objeto Problema.

Un problema se resuelve a través de Elementos de acción. Puede utilizar un elemento de acción o una serie de elementos de acción relacionados para formar un Plan de acción. Cada elemento de acción se asigna a un usuario para su resolución y hace seguimiento del progreso. Una vez que todos los elementos de acción para un problema se completan (cuando el responsable establece el valor en el 100%), cierre el problema.

En OpenPages® Internal Audit Management, se pueden utilizar problemas y elementos de acción en lugar de, o con, resultados.

#### Adición de comentarios a un elemento de acción

`Guía del usuario › Uso de objetos de OpenPages Platform › Problemas y elementos de acción` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=items-adding-comments-action-item)

Puede añadir comentarios a un elemento de acción desde una vista de tarea. Después de guardar un comentario, no se puede editar o suprimir.

##### Procedimiento

1. Abra la vista de tarea para el objeto padre en el que está interesado. Puede acceder a la vista de tarea desde un enlace de un correo electrónico, un asistente, un panel de control o una vista de cuadrícula.
2. En **Contenido relacionado**, pulse **Problemas**.
3. Pulse el nombre del problema.
4. En **Corrección**, pulse el elemento de acción.
5. Para añadir un comentario, pulse el campo **Comentario** . Escriba su comentario y pulse fuera del campo.
6. Pulse **Guardar**.

#### Completar elementos de acción

`Guía del usuario › Uso de objetos de OpenPages Platform › Problemas y elementos de acción` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=items-completing-action)

Puede seleccionar un porcentaje en el campo Porcentaje completado de un objeto de elemento de acción para identificar el progreso o la finalización del elemento de acción asignado. Para mostrar que ha completado un elemento de acción, establezca el porcentaje de compleción en 100%.

##### Procedimiento

1. En el menú principal, pulse **Corrección** > **Elementos de acción**.
2. Pulse el elemento de acción en el que está interesado.
3. En el campo **Porcentaje completado** , escriba un valor como, por ejemplo, 100.
4. Para añadir un comentario, pulse el campo **Comentario** .
5. Pulse **Guardar**.
6. Si el elemento de acción se ha completado, pulse **Acción** > **Enviar para aprobación**.

### Preferencias y Grupos de preferencias

`Guía del usuario › Uso de objetos de OpenPages Platform` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-preferences-preferences-groups)

El objeto Preferencia es hijo de una entidad de negocios o un grupo de preferencias e incluye valores variables que pueden dirigir informes, flujos de trabajo y campos calculados. Tiene valores de variable específicos de la entidad que permiten un comportamiento diferente para los mismos flujos de trabajo. Por ejemplo, defina valores de variable para determinar el comportamiento para flujos de trabajo de revisión y aprobación como, por ejemplo, los usuarios adecuados para cada nivel de revisión y aprobación, y los umbrales para determinar cuántos niveles de revisión y aprobación se necesitan.

El Grupo de preferencia se utiliza para agrupar objetos Preferencia. Sin este objeto de agrupación, los objetos Preferencia deben asociarse por separado con cada entidad de negocios relevante. El grupo de preferencia ayuda a minimizar el mantenimiento asociado.

En la configuración predeterminada de IBM OpenPages® Internal Audit Management , estos objetos se utilizan para mantener ponderaciones para los factores de riesgo utilizados en la clasificación de riesgos de evaluación anual. Puesto que los pesos y factores pueden ser diferentes para cada tipo de auditoría, como financiera, operativa o estratégica, cree una instancia de Preferencia individual para cada tipo de auditoría. Como hijo de la entidad de negocios, este enfoque proporciona la capacidad de tener valores de variable específicos de la entidad.

## Utilización de OpenPages Internal Audit Management (IAM)

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-openpages-internal-audit-management-iam)

IBM® OpenPages® Internal Audit Management (IAM) proporciona a los auditores internos una vista configurada de forma exclusiva del gobierno, riesgo y conformidad de la organización (GRC), lo que permite a la auditoría complementar y coexistir con actividades de gestión de riesgos y conformidad más amplias.

Al igual que con todas las soluciones, IBM OpenPages Internal Audit Management está completamente integrado con la gestión de controles financieros, el gobierno de TI, los esfuerzos de gestión de políticas y los programas de gestión de riesgos operativos. El equipo de auditoría interna tiene la capacidad de trabajar como un socio completamente integrado con los actores clave, de forma totalmente independiente o en una posición intermedia, en función de las necesidades concretas del departamento de auditorías o de lo que determine la auditoría en particular que se está realizando.

Sus principales características son:

- La capacidad de clasificar los riesgos del universo de auditoría, configurado en función de su metodología de auditoría

  - Fuerte soporte para la metodología de gestión de riesgo
  - Creación de informes completo en todo el universo de la auditoría
- La capacidad para definir, planear, ejecutar e informar sobre auditorías en toda la empresa

  - Hacer seguimiento y gestionar auditorías, secciones de auditoría, informes y asignaciones y requisitos de recurso de auditoría
  - Automatizar operaciones a través de un creación de informes completamente configurables

- Capacidad de proporcionar una garantía independiente a la empresa o funcionar como una parte integral de los esfuerzos de GRC

  - Opinar sobre los esfuerzos GRC de la gestión de forma independiente
  - Controlar el acceso a auditorías, campos y vistas de sólo auditoría confidenciales

### Objetos de OpenPages Internal Audit Management

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=iam-openpages-internal-audit-management-objects)

Este tema proporciona información sobre los objetos de OpenPages® Internal Audit Management .

#### Planes de auditoría de resumen

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-summary-audit-plans)

El tipo de objeto Plan de auditoría de resumen permite a una oficina del programa planificar auditorías de entidades auditables para un periodo de tiempo predeterminado (anual, medio año o trimestre) por ámbito, perfil de riesgo, horas de previsión de auditorías, etc.

El objeto Plan de auditoría de resumen es un hijo de Entidad de negocios. Los hijos del plan de auditoría de resumen incluyen: Auditoría y Entidad auditable.

#### Auditorías

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-audits)

Una auditoría representa cada ejecución de una auditoría en una entidad auditable. Por ejemplo, si se audita una entidad auditable cada dos años, se debe crear una instancia de auditoría hijo independiente para cada periodo de dos años, como 2022 y 2024. Una organización puede auditar varios procesos. Por ejemplo, puede auditar una entidad, un requisito regulador específico o una seguridad física de centro de datos.

El objeto Auditoría se configura como un tipo de objeto autocontenido y se crea una carpeta automáticamente para cada instancia Auditoría. Esta configuración le permite copiar auditorías de plantilla y componentes de auditoría desde una biblioteca a una jerarquía de auditoría sin conflictos de denominación de objetos.

La planificación y programación de recursos de Auditoría se realiza a nivel de auditoría.

Se puede realizar seguimiento a un proceso de auditoría de alto nivel supervisando los valores Estado y Fecha en la auditoría. Se puede hacer seguimiento de los hitos de auditoría claves añadiendo campos que representan fechas de finalización para cada uno de los hitos claves a los que se va a realizar seguimiento.

Utilice el objeto Auditoría para gestionar el proceso de auditoría en su empresa. La Auditoría identifica un punto de retención para capturar información como ámbito, objetivos, información de temporización, revisión, ejecución y funciones de aprobación. Puede realizar seguimiento a un subconjunto de auditorías que está emprendiendo en un horizonte de planificación determinado o a todas las auditorías en el universo de la auditoría.

#### Entidades auditables

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-auditable-entities)

Un objeto Entidad auditable es un hijo de una Entidad de negocios y un Plan de auditoría de resumen. Se establece una jerarquía de entidad de negocios de auditoría y se crean todas las Entidades auditables como hijo del objeto Entidad de negocios de auditoría interna. Las entidades auditables alineadas con elementos de la jerarquía organizativa de la entidad de negocios también están asociadas a las entidades de negocios.

Una Entidad auditable representa un único elemento de Universo de la auditoría; una colección de elementos de la empresa que se pueden auditar. La mayoría de las entidades auditables representan entidades de negocios o legales, pero también pueden representar procesos, proyectos de larga ejecución o iniciativas, programas de conformidad o servicios de TI compartidos.

Las Entidades auditables se clasifican como riesgo anualmente para determinar la prioridad de realizar una auditoría cada año. Se calcula una Puntuación de riesgo calculada pero el alcance se puede alterar.

#### Secciones de auditoría

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-audit-sections)

Las secciones de auditoría se pueden utilizar para representar las fases de la auditoría, los programas de trabajo dentro de la auditoría u otros componentes de la auditoría en el nivel de granularidad que desee.

Las organizaciones pueden tener varios componentes estándar para cada auditoría. Las auditorías de plantilla que incluyen secciones para cada componente estándar se pueden crear en una biblioteca. Las fechas de inicio y finalización planificadas y reales para estas secciones se utilizan para informar del progreso en hitos clave de las auditorías.

Se puede hacer seguimiento del progreso de auditoría detallada incluyendo una sección de auditoría para cada hito. También, algunas organizaciones pueden añadir campos a la auditoría que representan fechas de finalización para cada uno de los hitos claves a los que desea hacer seguimiento.

Aunque las secciones de auditoría se pueden utilizar para planificar y programar recursos de auditoría, la mayoría de organizaciones encuentran que este método es demasiado detallado.

#### Planes

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-plans)

Un tipo de objeto Plan facilita la planificación y asignación de recursos de auditoría en cualquier nivel. Por ejemplo, puede crear un único objeto de planificación para una auditoría completa o puede crear un objeto de planificación por tarea para cada auditor implicado en la auditoría. Los objetos Plan se utilizan para determinar la disponibilidad, habilidades y experiencia necesarias del recurso deseado. Las vistas de auditoría de OpenPages® , informes, etc., están alineadas con la planificación a nivel de auditoría. Los planes se pueden asociar a secciones de auditoría, en cuyo caso, estos componentes tendrán que modificarse.

Los objetos Plan también gestionan el seguimiento horario - se hace seguimiento de todas las horas en Planes. Se utiliza un tipo de objeto de hoja de registro horario para registrar las horas y gastos semanales reales empleados en relación con el objeto de planificación de una auditoría. Puesto que los objetos Hoja de registro horario están asociados a los planes, es fácil hacer seguimiento de las desviaciones entre los gastos y horas reales y planeados.

Normalmente, puede crear o modificar un objeto Plan utilizando el ayudante Añadir o modificar planes, al que los propietarios de auditoría pueden acceder desde un enlace en la vista de tareas Auditoría. También puede editar planes (pero no crearlos) accediendo al elemento de menú **Gestión de auditoría** > **Planes** .

#### Informes

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-workpapers)

Un informe de trabajo es cualquier artefacto o entregable del que desee realizar un seguimiento en el ámbito de una auditoría. Puede representar una carta de compromiso, una matriz de prueba, las notas de una entrevista o cualquier otro cosa que resulte apropiada para la auditoría en cuestión. El propio informe puede ser atributos que se almacenan en el objeto de informe, o puede ser un archivo de Microsoft Word, Microsoft Excel u otro tipo de archivo que se adjunta a un objeto de informe. Cuando el informe se utiliza como evidencia de prueba, documenta la planificación de la prueba y los resultados de la prueba.

Cree un objeto Documento de trabajo desde la vista de tareas de una sección de auditoría. Los objetos de informe de trabajo también se pueden copiar desde una biblioteca, donde representan plantillas de diferentes tipos de informes de trabajo generadas por un departamento de auditorías internas.

#### Conclusiones

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-findings)

Las conclusiones se pueden utilizar para representar observaciones notificables a la empresa, al Comité de auditoría o a ambos. Además, las conclusiones se pueden utilizar para representar observaciones objetivas individuales, mientras que los problemas se utilizan para representar temas consolidados o problemas sistémicos de los que se informa a la empresa, al comité de auditoría o a ambos.

Una conclusión representa algo que se ha descubierto en el curso de una auditoría que necesita una explicación y una investigación por parte del equipo directivo. Puede utilizar una conclusión para hacer seguimiento del progreso de la gestión a la hora de tratar el problema subyacente identificado. Se puede utilizar el objeto Problema en lugar de, o junto con el objeto Conclusión.

#### Auditores

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-auditors)

La planificación y asignación de recursos requiere información clave sobre cada persona que pueda realizar el trabajo de auditoría. El objeto Auditor se utiliza para crear una agrupación de auditores que se pueden asignar a la auditorías.

Cada usuario asignado al trabajo de auditoría se representa como una instancia Auditor. Los auditores están disponibles ahora para la asignación de recursos. El objeto Auditor incluye atributos que se pueden utilizar para evaluar y seleccionar auditores para los contratos de auditoría, como especialidades, idiomas y certificaciones. Los objetos Auditor están asociados al componente relevante de la jerarquía organizativa de la auditoría interna. Como recomendación, haya coincidir el nombre del objeto Auditor con el nombre de usuario.

#### Comentarios de revisión de auditoría

`Guía del usuario › Utilización de OpenPages Internal Audit Management (IAM) › Objetos de OpenPages Internal Audit Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-audit-review-comments)

El tipo de objeto Comentario de revisión de auditoría se utiliza para proporcionar comentarios durante el proceso de revisión para una auditoría y sus componentes. Está asociado como hijo a la instancia de Auditoría, Sección, Informe o Conclusión para la que se está proporcionando feedback.

## Utilización de OpenPages IT Governance (ITG)

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-openpages-it-governance-itg)

IBM OpenPages® IT Governance (ITG) es una solución de gobierno de TI empresarial que alinea los servicios de TI, los riesgos y las políticas con las iniciativas empresariales corporativas, la estrategia y los estándares operativos.

IBM® OpenPages IT Governance le permite gestionar el control interno de TI y el riesgo de acuerdo con los procesos de negocio a los que dan soporte. Además, IBM OpenPages IT Governance une varios silos de riesgo y conformidad de TI para ofrecer una mejor visibilidad, un mejor soporte a las decisiones y, en última instancia, un mejor rendimiento corporativo.

Sus principales características son:

- Cumplimiento regulatorio y de las políticas por parte de los departamentos de TI
- Evaluaciones de riesgo y control
- Pruebas de control y solución de problemas
- Gestión de recursos de TI
- Seguimiento de incidentes
- Seguimiento y puntuación de vulnerabilidades
- Indicadores clave de rendimiento y de riesgo
- Creación de informes, supervisión y analítica

### Términos de OpenPages IT Governance que debe conocer

`Guía del usuario › Utilización de OpenPages IT Governance (ITG)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=itg-openpages-it-governance-terms-you-should-know)

Este tema proporciona términos para utilizar en IBM OpenPages® IT Governance.

- **Aplicación**

  Un objeto que define un programa de software que se utiliza para dar soporte a un servicio de TI.

- **Activo**

  Personal, infraestructura o aplicación que se utiliza para dar soporte a un servicio de TI.

- **Incidente**

  Un objeto que registra un incidente de TI que tiene un efecto real o potencialmente adverso en la empresa.

- **Infraestructura**

  Un objeto que define el equipo físico o ubicación física que se utiliza para dar soporte a un servicio de TI.

- **Biblioteca**

  Un área de retención para mandatos relevantes para la empresa.

- **Mandato**

  (1) Obligación que debe cumplir una empresa. Un mandato puede ser una normativa gubernamental (local, federal o internacional), un estándar de práctica recomendada establecido por una organización de estándares o una política de la compañía interna. (2) Un objeto utilizado para establecer el proceso de gestión de conformidad de la empresa para una normativa o política específica, como PCI.

- **Personal**

  Un objeto que identifica el tipo de recurso humano (DBA, administrador del sistema, equipo empresarial, etc.) que se requiere para dar soporte a un servicio de TI.

- **Submandato**

  Objeto utilizado para establecer el proceso de gestión de conformidad para una subsección de una normativa o política. Normalmente, un hijo del objeto Mandato.

### Objetos de gobierno de TI interno de OpenPages

`Guía del usuario › Utilización de OpenPages IT Governance (ITG)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=itg-openpages-internal-it-governance-objects)

Este tema proporciona información sobre los objetos OpenPages® Internal IT Governance.

#### Activos y enlaces de activos

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-assets-asset-links)

El tipo de objeto Activo se utiliza para representar categorías de personal, aplicaciones, infraestructura, procesos, instalaciones y funciones. Los objetos de activo del mismo tipo a menudo deben estar relacionados entre sí. Puede utilizar un tipo de objeto Enlace de activo para enlazar dos objetos Activo.

##### Activos

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages › Activos y enlaces de activos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-assets)

El tipo de objeto Activo se utiliza para representar categorías de personal, aplicaciones, infraestructura, procesos, recursos y funciones.

> **Nota:** Los tipos de objeto y las acciones disponibles en una página dependen de su configuración y permisos concretos.

Aunque los objetos de activos pueden representar un activo de TI individual (por ejemplo, un servidor de aplicaciones determinado), con más frecuencia representan un grupo de activos, como una agrupación de servidores de aplicaciones utilizados para una aplicación específica.

Normalmente, los objetos de activo los crea la entidad empresarial de TI propietaria o responsable y, a continuación, se asocian con el objeto al que dan soporte como, por ejemplo, Entidades empresariales, Procesos y Líneas base.

Para acceder a los objetos Activos, haga clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Activos** > **Activos**.

##### Enlaces de activos

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages › Activos y enlaces de activos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=links-asset)

A menudo, los objetos de activo del mismo tipo deben estar relacionados entre sí. Puede utilizar un tipo de objeto Enlace de activo para enlazar dos objetos Activo.

Para enlazar un activo con otro activo, vaya a la vista de tarea de un objeto de activo, pulse la pestaña **Admin** y, a continuación, pulse **Crear enlace de activo**. Los usuarios con permisos de administración pueden acceder a la pestaña **Administrador** en las vistas de tareas.

Además, puede añadir el campo Enlace de activo a las vistas de tarea o cuadrícula del objeto Activo para permitir a los usuarios crear enlaces de activo a partir de estas vistas.

Varias opciones de filtrado en la pestaña **Admin** le permiten seleccionar el activo que desea enlazar. El enlace de activo que se crea es un objeto hijo de los dos activos enlazados y se rellena con los atributos de los objetos padre.

Tenga en cuenta que si los nombres o atributos de cualquiera de los objetos de activo padre se cambian después de crear el enlace de activo, el nombre de enlace de activo y sus atributos ya no se correlacionarán correctamente con sus activos padre.

#### Líneas base

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-baselines)

Un tipo de objeto de línea base representa una plantilla de requisitos de biblioteca. Es autónomo, lo que significa que las carpetas se crean para cada línea base. Las líneas base de la biblioteca representan elementos del entorno operativo de TI. Están enlazados a los requisitos para ese tipo de elemento. El objeto Línea base se copia de la biblioteca a la jerarquía empresarial, se realiza una asociación a un requisito en la biblioteca, y los tipos de objeto Riesgo, Control y Prueba se crean como objetos hijo. Los objetos Riesgo, Control y Prueba se llenan con datos del requisito cuando se utiliza el ayudante de copia de línea base.

Por ejemplo, un objeto Línea base puede representar una colección de objetos Requisito para un centro de datos con Información personalmente identificable (PII) y una clasificación de datos confidenciales. Para cada uno de los objetos Requisito, establezca una práctica recomendad para definir qué controlar (objeto Riesgo) y cómo controlarlo (objeto Control). También puede establecer una práctica para verificar la eficacia del Control (objeto Prueba).

Generalmente, los objetos Línea base se crean en la biblioteca como punto de partida. El contenido del objeto Línea base se modificará más tarde para que cumpla con un entorno operativo específico, y se realizarán evaluaciones en el entorno operativo real para este contenido.

Puede añadir un objeto de línea base a través del enlace **Añadir una línea base** en la vista de tareas de un objeto del sistema. El objeto Línea base se copia de la biblioteca a la jerarquía empresarial, se realiza una asociación a un requisito en la biblioteca, y los tipos de objeto Riesgo, Control y Prueba se crean como objetos hijo del objeto Línea base. Los objetos Riesgo, Control y Prueba se llena con datos adecuados del Requisito.

En la vista de tareas de un objeto Línea base, puede asociar objetos padre, adjuntar archivos o enlaces y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

#### Incidencias

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-incidents)

Una incidencia es una aparición que tiene un efecto potencialmente adverso en la empresa. Cree un objeto Incidente para registrar información, como la persona responsable de la investigación del incidente y otros datos relacionados. El objeto Incidencia lo utiliza un flujo de trabajo para facilitar el análisis de incidencias. Las categorías que se aplican a los incidentes incluyen la Conformidad con la normativa, Conformidad legal, Seguridad de la información y TI. Las incidencias se almacenan en la entidad de negocios o activo donde se ha producido el suceso y se asocian de forma secundaria a un mandato o política afectados.

#### KRI y valores de KRI

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-kris-kri-values)

Los KRI (Key Risk Indicators) son componentes del proceso de supervisión de riesgos y se utilizan para proporcionar indicadores iniciales o de retraso para condiciones de riesgo potenciales. Cada instancia de KRI dentro de la organización puede tener límites de umbral y destino exclusivos. Los valores KRI se utilizan para registrar el valor real de un indicador en un punto específico en el tiempo.

Puede crear y asociar un KRI (Indicador clave de riesgo) desde la vista de tarea de un tipo de objeto principal (por ejemplo, Riesgo, Control, Entidad de negocios). Desde la vista de tarea de un objeto de KRI, puede asociar una o varias entidades de negocios padre, riesgos o controles, y crear, ver o editar uno o más valores de KRI.

> **Nota:** Puede asociar KRI con controles. Algunos KRI pueden funcionar como indicadores de control señalando que un control no está funcionando correctamente. Por ejemplo, puede configurar varios controles de perímetro de seguridad con un KRI asociado. Si su empresa experimenta varias brechas de seguridad importantes, el KRI asociado puede indicar que los controles del perímetro de seguridad no son efectivos.

Los valores KRI se utilizan para registrar el valor real de un indicador en un punto específico en el tiempo.

Puede acceder a los elementos de menú **KRIs** y **Valores KRI** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Indicadores**.

#### KPI y valores de KPI

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-kpis-kpi-values)

Los ICR (Key Performance Indicators) son componentes del proceso de supervisión de riesgos y se utilizan para proporcionar indicadores iniciales o de retraso para condiciones de riesgo potenciales. Cada instancia de KPI dentro de la organización puede tener límites de umbral y destino exclusivos. El tipo de objeto Valor de KPI registra el valor de un objeto de KPI en un punto específico. Cree un objeto de KPI y, a continuación, periódicamente (diariamente, semanalmente, mensualmente) cree un objeto Valor de KPI para poder detectar tendencias.

Un objeto KPI se puede asociar con uno o más tipos de objeto padre (como, Entidad de negocios, Control, Sistema, Proceso, Subproceso). Por lo general, crea y asocia un KPI desde la vista de tarea de un tipo de objeto principal.

Puede acceder a los elementos de menú **KPIs** y **Valores de KPI** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Indicadores**.

#### Mandatos

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-mandates)

Los mandatos representan elementos externos con los que las organizaciones deben cumplir, como leyes, normativas y estándares. El contenido se puede extraer de proveedores de terceros como, por ejemplo, UCF, Ascent Reg Techo Wolters Kluwer. Los mandatos se representan en una estructura de entidades de negocios por biblioteca y no se replican para todo el sistema.

#### Políticas

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-policies)

Las políticas representan directrices internas adoptadas por el Consejo de Administración o el cuerpo de gobierno sénior dentro de una organización. El texto de una política puede almacenarse en los campos estandarizados en el objeto o como un archivo adjunto al objeto. Normalmente, las políticas tienen un ciclo de vida definido que va de Borrador a Publicado a Caducado, así como un proceso de revisión y aprobación. Normalmente, las políticas Borrador residen en la Jerarquía empresarial organizativa, mientras que las políticas Publicado y Caducado residen en las entidades de biblioteca de referencia. Las políticas también se correlacionan con mandatos aplicables de la biblioteca con la que están relacionadas.

#### Procedimientos

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-procedures)

Los procedimientos representan el qué, dónde, cuándo y cómo de cómo se implementan las políticas en una organización. El texto de los procedimientos se almacenan normalmente en los campos en el objeto. Normalmente, los procedimientos se representan como hijos de una política y residen en la misma estructura de entidad que su política padre.

#### Requisitos

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-requirements)

El objeto Requisito detalla requisitos específicos, que se encuentran en el objeto Mandato o Submandato relacionado, que la organización necesita cumplir para estar en conformidad.

Por ejemplo:

- Los tipos de objeto y las acciones que están disponibles en una vista dependen de la configuración y de los permisos específicos.
- Para acceder a la opción **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Conformidad** > **Requisitos**, debes tener configurados los permisos necesarios en tu cuenta.

Normalmente, se crean requisitos como objetos autónomos desde la vista de cuadrícula Requisitos y posteriormente se asocia el requisito a otros objetos. De forma alternativa, también puede crear un objeto Requisito desde la vista de tarea de un objeto padre (por ejemplo, objetivos de control, controles, mandatos o submandatos).

En la vista de tareas de un objeto Requisito, puede crear, asociar o desasociar objetos hijo (por ejemplo problemas, firmas, archivos o enlaces), asociar objetos padre y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

Puede acceder a la opción de menú **Requisitos** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Conformidad**.

#### Submandatos

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-sub-mandates)

Los submandatos representan subelementos externos (o internos) que la organización necesita cumplir. El contenido se puede extraer de proveedores de terceros, incluyendo UCF, Ascent Reg Tech, Thomson Reutersy Wolters Kluwer. Generalmente, los Submandatos están representados en una estructura de Entidad de negocios de biblioteca y no se replican en todo el sistema. El submandato es recursivo, pero el contenido de Deloitte, UCF, Ascent Reg Tech, Thomson Reutersy Wolters Kluwer utiliza exactamente un nivel de submandato. Los submandatos también soportan contenido para conformidad con la normativa. Los submandatos se pueden utilizar para representar párrafos derivados de informes reguladores.

#### Sistemas

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-systems)

El sistema es un tipo de objeto autocontenido, lo que significa que se crean carpetas para cada objeto del sistema. El objeto Sistema agrupa varias líneas base para representar elementos en el entorno operativo que se pueden evaluar para el riesgo. Actúa como contenedor para una colección de objetos de activos y los riesgos, controles y requisitos relacionados que realizan conjuntamente una función o forman parte de un servicio de TI. Por ejemplo, un objeto del sistema puede representar los servidores, sistemas operativos, aplicaciones, bases de datos, personal de soporte y recursos que proporcionan el correo electrónico corporativo.

En la vista de tarea de un objeto del sistema, puede asociar objetos padre, adjuntar archivos o enlaces y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

#### Amenazas

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-threats)

Una amenaza es cualquier circunstancia o suceso con el potencial de afectar negativamente a las operaciones y activos de la organización. Se puede crear una biblioteca de amenazas bajo el objeto Entidad de negocios y asociarse o copiarse en un objeto Proceso, Sistema o Activo padre. Las amenazas también pueden asociarse a Vulnerabilidades para identificar y evaluar la probabilidad y el impacto de la explotación de una Vulnerabilidad por parte de una Amenaza, lo que daría como resultado un riesgo para un Activo, Sistema o Proceso.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

#### Vulnerabilidades

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-vulnerabilities)

Las vulnerabilidades le ofrecen la posibilidad de realizar un seguimiento y evaluar las debilidades de seguridad. Asigne puntuaciones a Vulnerabilidades mediante Vulnerabilities Common Vulnerability Scoring System (CVSS v2). El objeto padre de una vulnerabilidad puede ser un sistema, una incidencia, un activo o un riesgo. Por norma, las vulnerabilidades se importan de una solución de seguridad de TI.

En la vista de tareas de un objeto Vulnerabilidad, puede crear, asociar o desasociar objetos hijo (por ejemplo, problemas, firmas, archivos o enlaces), asociar objetos padre y editar campos de un objeto de vulnerabilidad.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

#### Renuncias

`Guía del usuario › Utilización de OpenPages IT Governance (ITG) › Objetos de gobierno de TI interno de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-waivers)

Los vencidos le ofrecen la posibilidad de documentar, procesar y gestionar el ciclo de vida de excepciones a políticas, requisitos o controles. Las exenciones se pueden asociar a entidades empresariales, políticas, procedimientos, requisitos, riesgos, controles, líneas base y activos.

Algunos ejemplos de negocio de excepciones para las que se pueden solicitar renuncias incluyen lo siguiente:

- Desviación de política (como corporativa, seguridad de la información y políticas de TI)
- Aceptación de riesgo
- Autoridad para operar (ATO)
- ATO provisional - permite a un proceso avanzar antes de recibir la certificación (parte de la directriz NIST 800-37)

En la vista de tareas de un objeto Renuncia, puede asociar objetos padre, adjuntar archivos o enlaces y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

## Uso de objetos de OpenPages Operational Risk Management

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-openpages-operational-risk-management-objects)

IBM OpenPages® Operational Risk Management combina la gestión de documentos y procesos con un sistema de supervisión y soporte de decisiones que permite a las organizaciones analizar, gestionar y mitigar los riesgos de forma sencilla y eficiente.

IBM OpenPages Operational Risk Management ayuda a automatizar el proceso de medición y supervisión del riesgo operativo. Combina todos los datos de riesgo, incluidas las evaluaciones de riesgos y autocontrol, los eventos de pérdida, los análisis de escenarios, las pérdidas externas y los indicadores claves de riesgo (KRI) en un única solución integrada.

IBM OpenPages Operational Risk Management incluye las siguientes características clave:

- Eventos de pérdida, que incluye las siguientes actividades:

  - El seguimiento, evaluación y gestión de eventos internos y externos puede causar pérdida operativa.
  - Gestión de varios sucesos y recuperaciones de impacto asociados a pérdidas operativas.
- Autoevaluaciones de control y riesgo (RCSA), que incluyen las siguientes actividades:

  - Identificación, medida y mitigación de riesgos.
  - Prueba y documentación de controles internos.
- Indicadores claves de riesgo (KRI) e indicadores clave de rendimiento (KPI), que pueden realizar un seguimiento de las mediciones de rendimiento para mostrar potencialmente la presencia o el estado de una condición de riesgo o una tendencia.
- Análisis de escenarios, que es una técnica de evaluación que se utiliza para identificar y medir determinadas clases de riesgos, en particular, los eventos muy graves y de baja frecuencia.
- Los Eventos de pérdida externa proporcionan la capacidad de importar datos de pérdida de IBM® FIRST Risk Case Studies, ORX y bases de datos de pérdida ORIC a OpenPages Operational Risk Management para análisis de escenarios, benchmarking y generación de informes. También puede exportar datos de pérdida a herramientas analíticas o aplicaciones de asignación de capital.
- Gestión de problemas y solución (IMR), que incluye las siguientes actividades:

  - Creación y asignación de problemas
  - Creación y asignación de acciones
  - Rendimiento de la solución
  - Cierre del problema
  - Creación de informes
- Informes, supervisión y análisis.

### Objetos de OpenPages Operational Risk Management

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-openpages-operational-risk-management)

Este tema proporciona información sobre los objetos OpenPages® Operational Risk Management .

#### KRI y valores de KRI

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=oormo-kris-kri-values)

Los KRI (Key Risk Indicators) son componentes del proceso de supervisión de riesgos y se utilizan para proporcionar indicadores iniciales o de retraso para condiciones de riesgo potenciales. Cada instancia de KRI dentro de la organización puede tener límites de umbral y destino exclusivos. Los valores KRI se utilizan para registrar el valor real de un indicador en un punto específico en el tiempo.

Puede crear y asociar un KRI (Indicador clave de riesgo) desde la vista de tarea de un tipo de objeto principal (por ejemplo, Riesgo, Control, Entidad de negocios). Desde la vista de tarea de un objeto de KRI, puede asociar una o varias entidades de negocios padre, riesgos o controles, y crear, ver o editar uno o más valores de KRI.

> **Nota:** Puede asociar KRI con controles. Algunos KRI pueden funcionar como indicadores de control señalando que un control no está funcionando correctamente. Por ejemplo, puede configurar varios controles de perímetro de seguridad con un KRI asociado. Si su empresa experimenta varias brechas de seguridad importantes, el KRI asociado puede indicar que los controles del perímetro de seguridad no son efectivos.

Los valores KRI se utilizan para registrar el valor real de un indicador en un punto específico en el tiempo.

Puede acceder a los elementos de menú **KRIs** y **Valores KRI** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Indicadores**.

#### KPI y valores de KPI

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=oormo-kpis-kpi-values)

Los ICR (Key Performance Indicators) son componentes del proceso de supervisión de riesgos y se utilizan para proporcionar indicadores iniciales o de retraso para condiciones de riesgo potenciales. Cada instancia de KPI dentro de la organización puede tener límites de umbral y destino exclusivos. El tipo de objeto Valor de KPI registra el valor de un objeto de KPI en un punto específico. Cree un objeto de KPI y, a continuación, periódicamente (diariamente, semanalmente, mensualmente) cree un objeto Valor de KPI para poder detectar tendencias.

Un objeto KPI se puede asociar con uno o más tipos de objeto padre (como, Entidad de negocios, Control, Sistema, Proceso, Subproceso). Por lo general, crea y asocia un KPI desde la vista de tarea de un tipo de objeto principal.

Puede acceder a los elementos de menú **KPIs** y **Valores de KPI** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Indicadores**.

#### Eventos de pérdida

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-loss-events)

Los eventos de pérdida se utilizan para realizar un seguimiento de las pérdidas operativas que se producen en cualquier parte de una organización. Los Eventos de pérdida se almacenan generalmente bajo la Entidad de negocios donde se ha producido la pérdida. Los objetos Evento de pérdida se utilizan para hacer seguimiento, evaluar y gestionar los datos de pérdida internos relacionados. Puede añadir varios impactos y recuperaciones a cada evento de pérdida utilizando los objetos Impacto de pérdida y Recuperación de pérdida. Los objetos Evento de pérdida, Impacto de pérdida y Recuperación de pérdida también se pueden crear en IBM® OpenPages® Loss Event Entry.

Su organización puede llamar a los eventos de pérdida «“eventos operativos”», «“eventos de riesgo”» o «“incidentes”».

#### Impactos de pérdida

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-loss-impacts)

Un impacto de pérdida es una consecuencia financiera y no financiera que resulta de un evento de pérdida. Los impactos de pérdida realizan un seguimiento de los impactos iniciados por un evento de pérdida, como la responsabilidad legal, pérdida o daños en los activos o una interrupción de la actividad del negocio. Puede haber varios impactos de pérdida asociados con cada evento de pérdida.

#### Recuperaciones de pérdidas

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-loss-recoveries)

Los objetos de recuperación de pérdida se utilizan para realizar un seguimiento de los procesos asociados con la recuperación de daños que resultan de los eventos de pérdida.

#### Análisis de escenario

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-scenario-analysis)

Análisis de escenario (SA) es una técnica de evaluación que se utiliza para identificar y medir la aparición potencial de sucesos de riesgo operativo o para evaluar la resiliencia operativa. A diferencia de las evaluaciones de riesgos operativos tradicionales, es un análisis de futuro «“what if”» .

El análisis de escenarios está diseñado para derivar evaluaciones razonadas de la probabilidad e impacto de pérdidas operativas plausibles o para analizar la resiliencia operativa. Puede utilizar el proceso de análisis de escenario en OpenPages® para construir análisis de escenario y recopilar datos cualitativos y cuantitativos de soporte. Con un Análisis de escenario, puede registrar un intervalo de estimaciones de frecuencia y gravedad en «“grupos”» junto con la información de soporte de la evaluación.

#### Resultados del caso de ejemplo

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-scenario-results)

Los objetos Resultado del escenario son hijos de los objetos Análisis del escenario y se utilizan para capturar los resultados de los talleres de Análisis del escenario con fines de comparación y tendencias.

#### Pérdidas FIRST

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-first-losses)

Los objetos de pérdida FIRST se pueden importar desde la base de datos de pérdida externa FIRST, para utilizarlos con análisis de escenario, benchmarking y generación de informes, y para exportar datos de pérdida a herramientas analíticas o aplicaciones de asignación de capital. Los objetos Pérdida FIRST a menudo se organizan por categorías de pérdida, como líneas de producto o tipos de evento. Por ejemplo, utilice una entidad de negocios para crear una jerarquía para los datos de la pérdida FIRST. Denomine al objeto raíz «“FIRST-data”» y cree carpetas de categoría bajo la raíz. Enlace pérdidas externas a ese objeto.

Generalmente, crea un objeto Pérdida FIRST a partir de una Entidad de negocios principal que reside en una estructura de biblioteca. El objeto Pérdida FIRST es hijo de la Entidad de negocios de biblioteca y puede asociarse al Análisis de escenario y a otros tipos de objetos de la Entidad de negocios.

En la vista de tareas de un objeto Pérdida FIRST, puede asociar objetos padre, adjuntar archivos o enlaces y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

#### Pérdidas ORIC

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-oric-losses)

Los objetos Pérdida ORIC se pueden importar desde la base de datos de pérdida externa ORIC, para utilizarlos con análisis de escenario, benchmarking y generación de informes, y para exportar datos de pérdida a herramientas analíticas o aplicaciones de asignación de capital.

Los objetos Pérdida ORIC se organizan generalmente por categorías de pérdida (como por ejemplo líneas de producto o tipos de suceso) en una estructura de biblioteca no empresarial. Por ejemplo, puede ver un tipo de objeto Entidad de negocios para crear una jerarquía para datos de pérdida ORIC, nombrar datos ORIC del objeto raíz y crear carpetas de categoría bajo las pérdidas externas de enlace y raíz.

Generalmente, crea un objeto Pérdida ORIC a partir de una Entidad de negocios padre que reside en una estructura de biblioteca. El objeto Pérdida ORIC es hijo de la Entidad de negocios de biblioteca y puede asociarse al Análisis de escenario y a otros tipos de objetos de la Entidad de negocios.

En la vista de tareas de un objeto Pérdida ORIC, puede asociar objetos padre, adjuntar archivos o enlaces y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

Puede acceder a la opción de menú **Pérdidas ORIC** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Eventos**.

#### Pérdidas ORX

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-orx-losses)

Los objetos Pérdida ORX se pueden importar desde la base de datos de pérdida externa ORX, para utilizarlos con análisis de escenario, benchmarking y generación de informes, y para exportar datos de pérdida a herramientas analíticas o aplicaciones de asignación de capital. Puede importar datos de pérdida ORX externos a OpenPages® Operational Risk Management para utilizarlos con el análisis de escenario.

Los objetos Pérdida ORX se organizan generalmente por categorías de pérdida (como por ejemplo líneas de producto o tipos de suceso) en una estructura de biblioteca no empresarial. Por ejemplo, puede ver un tipo de objeto Entidad de negocios para crear una jerarquía para datos de pérdida ORX, nombrar datos ORX del objeto raíz y crear carpetas de categoría bajo las pérdidas externas de enlace y raíz.

Generalmente, crea un objeto Pérdida ORX a partir de una Entidad de negocios padre que reside en una estructura de biblioteca. El objeto Pérdida ORX es hijo de la Entidad de negocios de biblioteca y puede asociarse al Análisis de escenario y a otros tipos de objetos de la Entidad de negocios.

En la vista de tareas de un objeto Pérdida ORX, puede asociar objetos padre e hijo, adjuntar archivos o enlaces y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

Puede acceder a la opción de menú **Pérdidas de ORX** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Eventos**.

#### Centros de costes

`Guía del usuario › Uso de objetos de OpenPages Operational Risk Management › Objetos de OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-cost-centers)

Los objetos del Centro de costes de  se utilizan para agrupar eventos de pérdida bajo una entidad empresarial. En muchos casos, las firmas desean hacer seguimiento donde se producen los eventos de pérdida con el más mínimo detalle, como a nivel de centro de costes, pero no desean representar todas las capas organizativas como entidades de negocios.

Normalmente, se crea un objeto de Centro de costes desde la vista de tarea de una entidad de negocios padre. Puede asociar objetos Evento de pérdida hijo a un objeto Centro de costes padre.

En la vista de tareas de un objeto de Centro de costes, puede crear, asociar o desasociar objetos, adjuntar archivos o enlaces y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

Puede acceder a la opción de menú **Centros de costes** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Organización**.

## Utilización de OpenPages Policy Management

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-openpages-policy-management)

IBM OpenPages® Policy Management (PCM) es una solución de software de gestión de conformidad empresarial que reduce el coste, la complejidad y la naturaleza engorrosa de la conformidad con varios mandatos normativos y políticas corporativas.

IBM OpenPages Gestión de políticas permite a las empresas gestionar y supervisar las actividades de conformidad a través de un conjunto completo de funciones integradas que incluyen:

- Bibliotecas regulatorias y Gestión de cambios
- Evaluaciones de riesgo y control
- Gestión de políticas, incluidas la creación, revisión y aprobación de políticas y el conocimiento de políticas
- Pruebas de control y solución de problemas
- Gestión de interacciones con el regulador
- Seguimiento de incidentes
- Indicadores clave de rendimiento
- Informes, supervisión y análisis

El PCM apoya tres enfoques para cargar inicialmente los datos de políticas y establecer cómo se organizan y se ven en los objetos de políticas:

- **Centrado en datos**

  Los atributos de las políticas se almacenan como metadatos en el objeto Política. El contenido de las políticas y procedimientos se crea, almacena, modifica y revisa en los visores de las políticas. No se admite el control de cambios marcados con una raya roja dentro de las iteraciones del borrador.

- **Centrado en documento**

  Los atributos de las políticas se almacenan como metadatos en el objeto Política. El contenido de política y procedimiento se crea fuera de OpenPages y todo el documento se adjunta al objeto de política. El contenido de política y procedimiento nunca se importa ni se almacena en OpenPages.

- **Híbrido**

  Los atributos de las políticas se almacenan como metadatos en el objeto Política. El contenido de políticas y procedimientos se crea y edita en documentos de Microsoft Word y, a continuación, se importa y se almacena en OpenPages. La funcionalidad Seguimiento de cambios disponible en Microsoft Word se utiliza para realizar un seguimiento de los cambios de línea roja dentro de las iteraciones de borrador.

Una vez cargados los datos de la política, un flujo de trabajo preconstruido permite a las organizaciones hacer avanzar un objeto de la política a través de un proceso de revisión y un proceso de aprobación. La política avanza en cada etapa sobre la base de los valores del estado de aprobación y publicación.

Para obtener más información, consulte [OpenPages](https://www.ibm.com/docs/es/SSFUEU_9.0.0/pdf/OpenPages_PCM_Solution_v9.pdf).

### Términos de IBM OpenPages Policy Management que debe conocer

`Guía del usuario › Utilización de OpenPages Policy Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=management-openpages-policy-terms-you-should-know)

Este tema proporciona términos que debe conocer para utilizar IBM OpenPages® Policy Management.

- **Submandato**

  Objeto utilizado para establecer el proceso de gestión de conformidad para una subsección de una normativa o política. Normalmente, un hijo del objeto Mandato.

- **Biblioteca**

  Una Entidad de negocios que contiene el texto de las normativas relevantes para la empresa. Dentro de la entidad de negocios, cada normativa está representada por un mandato.

- **Mandato**

  (1) Obligación que debe cumplir una empresa. Un mandato puede ser una normativa gubernamental (local, federal o internacional), un estándar de práctica recomendada establecido por una organización de estándares o una política de la compañía interna. (2) Un objeto utilizado para establecer el proceso de gestión de conformidad de la empresa para una normativa o política específica, como HIPAA o GLBA.

### Objetos de gestión de políticas de OpenPages

`Guía del usuario › Utilización de OpenPages Policy Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=management-openpages-policy-objects)

Este tema proporciona información sobre los objetos IBM OpenPages® Policy Management .

#### Aplicabilidades del reglamento

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-regulation-applicabilities)

El objeto Aplicabilidad de la normativa reside en la jerarquía empresarial de la organización. Evalúa y hace seguimiento del impacto regulador de un mandato de la biblioteca en una entidad de negocios.

#### Mandatos

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=opmo-mandates)

Los mandatos representan elementos externos con los que las organizaciones deben cumplir, como leyes, normativas y estándares. El contenido se puede extraer de proveedores de terceros como, por ejemplo, UCF, Ascent Reg Techo Wolters Kluwer. Los mandatos se representan en una estructura de entidades de negocios por biblioteca y no se replican para todo el sistema.

#### Submandato

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-sub-mandate)

Los Submandatos representan subelementos internos o externos que debe cumplir la organización.

La configuración preestablecida soporta directamente el contenido proporcionado por Deloitte y UCF, y la configuración se puede adaptar para dar soporte a contenido de otros proveedores. Generalmente, los Submandatos están representados en una estructura de Entidad de negocios de biblioteca y no se replican en todo el sistema. El Submandato es recursivo, pero el contenido de Deloitte y de UCF utiliza exactamente un nivel de Submandato.

#### Requisito

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-requirement)

El objeto Requisito detalla requisitos específicos, que se encuentran en el objeto Mandato o Submandato relacionado, que la organización necesita cumplir para estar en conformidad.

El contenido se puede extraer de UCF, Ascent Reg Techu otros proveedores de terceros. Por lo general, los mandatos se representan en una estructura de entidades de negocios por biblioteca y no se replican para todo el sistema.

Para Ascent Reg Tech, se crea un requisito para cada tarea entrante.

#### KRI y valores de KRI

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=opmo-kris-kri-values)

Los KRI (Key Risk Indicators) son componentes del proceso de supervisión de riesgos y se utilizan para proporcionar indicadores iniciales o de retraso para condiciones de riesgo potenciales. Cada instancia de KRI dentro de la organización puede tener límites de umbral y destino exclusivos. Los valores KRI se utilizan para registrar el valor real de un indicador en un punto específico en el tiempo.

Puede crear y asociar un KRI (Indicador clave de riesgo) desde la vista de tarea de un tipo de objeto principal (por ejemplo, Riesgo, Control, Entidad de negocios). Desde la vista de tarea de un objeto de KRI, puede asociar una o varias entidades de negocios padre, riesgos o controles, y crear, ver o editar uno o más valores de KRI.

> **Nota:** Puede asociar KRI con controles. Algunos KRI pueden funcionar como indicadores de control señalando que un control no está funcionando correctamente. Por ejemplo, puede configurar varios controles de perímetro de seguridad con un KRI asociado. Si su empresa experimenta varias brechas de seguridad importantes, el KRI asociado puede indicar que los controles del perímetro de seguridad no son efectivos.

Los valores KRI se utilizan para registrar el valor real de un indicador en un punto específico en el tiempo.

Puede acceder a los elementos de menú **KRIs** y **Valores KRI** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Indicadores**.

#### Incidencias

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=opmo-incidents)

Una incidencia es una aparición que tiene un efecto potencialmente adverso en la empresa. Cree un objeto Incidente para registrar información, como la persona responsable de la investigación del incidente y otros datos relacionados. El objeto Incidencia lo utiliza un flujo de trabajo para facilitar el análisis de incidencias. Las categorías que se aplican a los incidentes incluyen la Conformidad con la normativa, Conformidad legal, Seguridad de la información y TI. Las incidencias se almacenan en la entidad de negocios o activo donde se ha producido el suceso y se asocian de forma secundaria a un mandato o política afectados.

#### Renuncias

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=opmo-waivers)

Los vencidos le ofrecen la posibilidad de documentar, procesar y gestionar el ciclo de vida de excepciones a políticas, requisitos o controles. Las exenciones se pueden asociar a entidades empresariales, políticas, procedimientos, requisitos, riesgos, controles, líneas base y activos.

Algunos ejemplos de negocio de excepciones para las que se pueden solicitar renuncias incluyen lo siguiente:

- Desviación de política (como corporativa, seguridad de la información y políticas de TI)
- Aceptación de riesgo
- Autoridad para operar (ATO)
- ATO provisional - permite a un proceso avanzar antes de recibir la certificación (parte de la directriz NIST 800-37)

En la vista de tareas de un objeto Renuncia, puede asociar objetos padre, adjuntar archivos o enlaces y editar campos.

Para ver un historial de cambios, vaya a la pestaña **Actividad** del objeto.

#### KPI y valores de KPI

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=opmo-kpis-kpi-values)

Los ICR (Key Performance Indicators) son componentes del proceso de supervisión de riesgos y se utilizan para proporcionar indicadores iniciales o de retraso para condiciones de riesgo potenciales. Cada instancia de KPI dentro de la organización puede tener límites de umbral y destino exclusivos. El tipo de objeto Valor de KPI registra el valor de un objeto de KPI en un punto específico. Cree un objeto de KPI y, a continuación, periódicamente (diariamente, semanalmente, mensualmente) cree un objeto Valor de KPI para poder detectar tendencias.

Un objeto KPI se puede asociar con uno o más tipos de objeto padre (como, Entidad de negocios, Control, Sistema, Proceso, Subproceso). Por lo general, crea y asocia un KPI desde la vista de tarea de un tipo de objeto principal.

Puede acceder a los elementos de menú **KPIs** y **Valores de KPI** haciendo clic en **Menú principal ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_user/primary_menu_icon_task_focused_ui.png)** > **Indicadores**.

#### Políticas

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=opmo-policies)

Las políticas representan directrices internas adoptadas por el Consejo de Administración o el cuerpo de gobierno sénior dentro de una organización. El texto de una política puede almacenarse en los campos estandarizados en el objeto o como un archivo adjunto al objeto. Normalmente, las políticas tienen un ciclo de vida definido que va de Borrador a Publicado a Caducado, así como un proceso de revisión y aprobación. Normalmente, las políticas Borrador residen en la Jerarquía empresarial organizativa, mientras que las políticas Publicado y Caducado residen en las entidades de biblioteca de referencia. Las políticas también se correlacionan con mandatos aplicables de la biblioteca con la que están relacionadas.

#### Comentario de revisión de política

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-policy-review-comment)

Los comentarios de revisión de políticas dan soporte y facilitan el proceso de revisión y aprobación de políticas y procedimientos por parte de expertos en la materia y personal de conformidad.

#### Procedimientos

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=opmo-procedures)

Los procedimientos representan el qué, dónde, cuándo y cómo de cómo se implementan las políticas en una organización. El texto de los procedimientos se almacenan normalmente en los campos en el objeto. Normalmente, los procedimientos se representan como hijos de una política y residen en la misma estructura de entidad que su política padre.

#### Campañas

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-campaigns)

El objeto Campaña forma parte de la prestación Conocimiento de política y se utiliza para gestionar los aspectos de gestión de proyectos de una campaña de reconocimiento. También se utiliza para definir los requisitos y criterios que identifica qué empleados necesitan leer y autenticar cada política. Las campañas se crean generalmente en la jerarquía de políticas publicadas.

#### Empleados

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-employees)

El objeto Employee forma parte de la prestación Policy Awareness Ability. Se utiliza para capturar información sobre empleados individuales, como el nombre, el cargo, el correo electrónico, la región, el departamento, el estado, etc. La información del perfil del empleado se coteja después con los requisitos de atestación definidos en una campaña para determinar qué empleados necesitan testificar sobre cada política. Los datos de empleado provienen generalmente de la exportación del sistema de RRHH, cargado a través de Online FastMap, y residen en la entidad de negocios de empleado de referencia. Se recomienda que el campo Nombre de empleado coincida con el nombre de usuario del usuario.

#### Atestaciones

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-attestations)

El objeto de testificación, que forma parte de la función de reconocimiento de políticas, se utiliza para capturar la afirmación de un empleado de que ha leído y comprendido una política. Un padre principal de la Atestación es el registro de empleados y el padre secundario es la campaña asociada.

#### Autoridades reguladoras

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-regulators)

El objeto Regulador forma parte de la prestación Gestión de interacciones con la autoridad reguladora y proporciona a las organizaciones la capacidad de crear un único inventario de todos los reguladores con los que interactúan. Las actividades reguladoras normalmente se crean en una entidad de negocios de biblioteca. El objeto es un hijo de la entidad de negocios y se puede asociar a mandatos e interacciones con la actividad reguladora.

#### Interacciones de las autoridades reguladoras, categorías de RI y solicitudes de RI

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-regulator-interactions-ri-categories-ri-requests)

El objeto Interacción con la autoridad reguladora forma parte de la prestación Gestión de interacciones con la autoridad reguladora. El objeto Interacción con la autoridad reguladora permite gestionar las interacciones, las comunicaciones, los trabajos internos, las revisiones y las aprobaciones asociadas con las autoridades reguladoras externas, como las consultas, los envíos, los archivados, los exámenes y las reuniones. Para las interacciones complejas, como por ejemplo los exámenes, puede utilizar los objetos Componente RI y Subcomponente RI para partir la interacción en componentes más pequeños o para rastrear las consultas de seguimiento procedentes de la entidad reguladora. La Interacción con la autoridad reguladora se puede correlacionar a los siguientes objetos padre: Autoridad reguladora, Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones padre permiten a un usuario enlazar objetos que puedan estar dando problemas en la Interacción con la autoridad reguladora, e identificar a los usuarios que son relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Se podrían asignar tareas individuales relacionadas con la gestión y respuesta a la interacción con la autoridad reguladora a usuarios a través de objetos hijo de tareas reguladoras.

##### Categorías de RI

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages › Interacciones de las autoridades reguladoras, categorías de RI y solicitudes de RI` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=requests-ri-categories)

El objeto Componente RI (anteriormente etiquetado como Categoría RI) forma parte de la prestación Gestión de interacciones con la autoridad reguladora y se utiliza como nivel medio del modelo de objeto de tres niveles (Interacción con la autoridad reguladora, Componente RI y Subcomponente RI). El objeto se utiliza para dividir una Interacción con la autoridad reguladora compleja en registros más pequeños, más manejables o para enlazar una consulta de seguimiento de una autoridad reguladora con el objeto padre de la Interacción con la autoridad reguladora. Además, el Componente RI se puede correlacionar con los siguientes objetos padre: Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones permiten a un usuario enlazar objetos que puedan estar dando problemas e identificar a los usuarios relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Las tareas individuales relacionadas con la gestión y respuesta a la interacción reguladora se pueden asignar a usuarios a través de un objeto hijo de tarea reguladora.

##### Solicitudes de RI

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages › Interacciones de las autoridades reguladoras, categorías de RI y solicitudes de RI` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=requests-ri)

El objeto Subcomponente RI (anteriormente denominado Solicitud RI) forma parte de la prestación Gestión de interacciones con la autoridad reguladora y se utiliza como último nivel del modelo de objeto de tres niveles (Interacción con la autoridad reguladora, Componente RI y Subcomponente RI). El objeto se utiliza para dividir una Interacción con la autoridad reguladora y el componente RI en registros más pequeños y manejables. Además, el Subcomponente RI se puede correlacionar con los siguientes objetos padre: Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones permiten a un usuario enlazar objetos que puedan estar dando problemas e identificar a los usuarios relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Las tareas individuales relacionadas con la gestión y respuesta a la interacción reguladora se pueden asignar a usuarios a través de objetos hijo de tareas reguladoras.

#### Cambios reguladores y tareas reguladoras

`Guía del usuario › Utilización de OpenPages Policy Management › Objetos de gestión de políticas de OpenPages` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-regulatory-changes-regulatory-tasks)

El objeto Cambio regulador forma parte de la capacidad de Gestión de cambios reguladores. Ofrece la capacidad de realizar un seguimiento de los cambios reguladores, evalúa el impacto de una modificación en la organización, comunica el cambio a nivel interno a las personas que correspondan y gestiona los procesos internos de respuesta al cambio.

El objeto Tarea reguladora se utiliza para asignar tareas a usuarios de OpenPages® cuando la tarea está relacionada con uno de los siguientes objetos padre: Proyecto, Política, Cambio regulador, Interacción con la autoridad reguladora, Componente RI o Subcomponente RI. Una Tarea reguladora también se puede asociar a una entidad de negocios.

## Utilización de IBM OpenPages Financial Controls Management

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-openpages-financial-controls-management)

IBM® OpenPages® Financial Controls Management reduce el tiempo y los costes de recursos asociados con la conformidad continua de las normativas de informes financieros.

IBM OpenPages Financial Controls Management combina una potente gestión de documentos y procesos con completas prestaciones de creación de informes interactivos en un entorno flexible y adaptable, fácil de utilizar, que permite a los CEO, CFO, gestores, auditores independientes y comités de auditoría realizar todas las actividades necesarias para cumplir con las normativas de creación de informes financieros de forma sencilla y eficiente.

IBM OpenPages Financial Controls Management permite a los usuarios ver fácilmente el estado de su proyecto de documentación de controles financieros y proporciona un repositorio seguro para el almacenamiento de su documentación de controles internos.

Sus principales características son:

- Repositorio de gestión de controles financieros, que presentan de manera lógica procesos, riesgos y controles en relaciones compartidas muchos a muchos en varios niveles, y habilita la prestación de adjunto a archivo y planes de acción para procesos, riesgos, controles y pruebas a todos los niveles.
- Automatización flexible, que proporciona notificación y finalización de actividades de gestión de controles financieros, como la revisión de diseño, la revisión operativa y la certificación.
- Creación de informes, supervisión y analítica

### Objetos OpenPages Financial Controls Management

`Guía del usuario › Utilización de IBM OpenPages Financial Controls Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=management-openpages-financial-controls-objects)

Este tema proporciona información sobre los objetos OpenPages® Financial Controls Management .

#### Subcuentas

`Guía del usuario › Utilización de IBM OpenPages Financial Controls Management › Objetos OpenPages Financial Controls Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-sub-accounts)

Una subcuenta representa un elemento de línea más pequeño y más específico que forma parte de una cuenta padre más grande (o de otra subcuenta). Cada objeto Subcuenta puede estar asociado a objetos Subcuenta o Cuenta padre.

#### Declaraciones

`Guía del usuario › Utilización de IBM OpenPages Financial Controls Management › Objetos OpenPages Financial Controls Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-assertions)

El objeto Declaraciones se utiliza para enlazar un control directamente con la cuenta (o subcuenta) a la que afecta y para documentar qué declaraciones cubre para una cuenta o subcuenta concreta.

Una práctica común es almacenar el tipo de declaración que está cubriendo el control como, por ejemplo, un campo de datos en el Objeto Declaración. Cree un objeto Assertion desde la vista de tarea de un tipo de objeto de cuenta, subcuenta o control principal.

Los tipos de objeto y acciones disponibles en una página depende de la configuración y los permisos.

#### Cuentas

`Guía del usuario › Utilización de IBM OpenPages Financial Controls Management › Objetos OpenPages Financial Controls Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-accounts)

Las cuentas corresponden a una o varias líneas de detalle de un informe financiero. Cada cuenta está afectada por Procesos recurrentes. Estos procesos pueden introducir riesgos que deben documentarse durante el proyecto de documentación de controles financieros. Una cuenta se identifica como cuenta significativa en base a factores como el tamaño, la complejidad de los procesos que operan en la cuenta o si la cuenta está asociada con una nueva línea de producto dentro de la empresa. Los riesgos que podrían materializarse y que producen un efecto material sobre la cuenta se identifican mediante la consideración de los procesos que operan en la cuenta.

## Utilización de OpenPages Regulatory Compliance Management

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-regulatory-compliance-management-overview)

IBM OpenPages® Regulatory Compliance Management (RCM) da soporte a las organizaciones para desglosar las normativas en un catálogo de requisitos, evaluar su impacto en la empresa y crear tareas accionables.

Como solución, permite a las empresas:

- Mantener un repositorio de regulaciones y requisitos que deben cumplir
- Identificar y crear un catálogo de requisitos que satisfacen las regulaciones
- Correlacionar requisitos reguladores con un marco de trabajo de control interno
- Crear agrupaciones de requisitos en Temas de conformidad
- Realizar evaluaciones de requisitos normativos bajo Planes de conformidad
- Ingerir, apuntar y responder a eventos reguladores suministrados por proveedores de datos de terceros
- Registrar, organizar y responder a las interacciones reguladoras, incluyendo las consultas y exploraciones reguladoras

Puede utilizar RCM Theme Deployer para crear la estructura de temas de las entidades de negocio. Para obtener más información, consulte [Planes de conformidad y temas de conformidad](#planes-de-conformidad-y-temas-de-conformidad).

### Objetos de OpenPages Regulatory Compliance Management

`Guía del usuario › Visión general de Regulatory Compliance Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=overview-regulatory-compliance-management-object-types)

Este tema proporciona información sobre los objetos IBM OpenPages® Regulatory Compliance Management para la gestión de conformidad con la normativa.

- **Ascent Información de soporte**

  El objeto Información de soporte de Ascent almacena información de soporte que se importa desde Ascent. La información de soporte es un texto normativo que no tiene un nivel de requisito legal, sino que proporciona orientación adicional, detalles, etc. para ayudar a las entidades a comprender los requisitos y el impacto de la normativa. El tipo de objeto Ascent Información de soporte tiene un padre, Requisito.

- **Plan de conformidad**

  Los objetos Planes de conformidad permiten la creación de un plan general para aplicar los requisitos normativos en un valor estructurado, o para estructurar un conjunto de tareas reguladoras. Por ejemplo, se puede crear un Plan de conformidad para hacer un seguimiento de las tareas reguladoras, o para llevar a cabo evaluaciones de conformidad en varios requisitos reguladores. Se pueden agrupar uno o varios Temas de conformidad en un Plan de conformidad general para la organización.

- **Evaluación del plan de conformidad**

  Los objetos Evaluación del plan de conformidad son hijos del objeto Plan de conformidad. Los objetos Evaluación del plan de conformidad se utilizan para capturar valores que se proporcionan como parte de la evaluación de conformidad que se captura en el plan de conformidad. Se crea un registro de evaluación del plan de conformidad y se rellena como último paso en los flujos de trabajo de evaluación de BE del plan de conformidad y evaluación de la biblioteca de planes de conformidad.

- **Tema de conformidad**

  Los Temas de conformidad permiten a los usuarios organizar requisitos normativos en temas a efectos de evaluación. Esto permite evaluar los requisitos de conformidad más allá del típico enfoque de entidad de negocios, agrupando los requisitos normativos en temas que afectan a toda la organización. Los temas de ejemplo pueden incluir privacidad de datos, gobierno, responsabilidad, etc. Esto permite a los usuarios evaluar el impacto de la normativa no sólo dentro de las entidades empresariales, sino a través de temas que afectan a múltiples áreas de la organización.

- **Evaluación de temas de conformidad**

  Los objetos Evaluación de temas de conformidad son hijos de objetos Tema de conformidad. Los objetos Evaluación de temas de conformidad se utilizan para capturar valores que se proporcionan como parte de la evaluación de conformidad que se captura en el tema de conformidad. Se crea un registro de evaluación de temas de conformidad y se rellena como el último paso en los flujos de trabajo Evaluación de BE de temas de conformidad y Evaluación de la biblioteca de temas de conformidad.

- **Mandato**

  Los mandatos representan elementos externos con los que las organizaciones deben cumplir, como leyes, normativas y estándares. El contenido se puede extraer de proveedores de terceros como, por ejemplo, UCF, Ascent Reg Techo Wolters Kluwer. Los mandatos se representan en una estructura de entidades de negocios por biblioteca y no se replican para todo el sistema.

  Por ejemplo, una compañía de seguros tiene un objeto Mandato para HIPAA y otro objeto Mandato para GLBA. Puede asociar el mismo mandato a grupos diferentes dentro de la organización. Los mandatos de privacidad, por ejemplo, pueden aplicarse a los departamentos de nóminas, servicios de seguros, legal y al departamento de TI.

- **Obligación**

  El tipo de objeto Obligación representa «“las cosas que hay que hacer”» normalizadas y armonizadas para cumplir con todos los objetos Mandato, Submandato y Requisito asociados de la obligación.

  Los objetos Obligación cumplen dos objetivos principales: traducen la jerga legal, a menudo difícil y farragosa, de los mandatos/submandatos/requisitos a un inglés sencillo, y utilizan los elementos comunes a varios mandatos/submandatos/requisitos. Por ejemplo, es posible que tenga muchos submandatos y requisitos en numerosos mandatos que requieren el uso de contraseñas fuertes. Un solo objeto Obligación puede documentar los detalles para contraseñas fuertes. Cumpliendo esta única obligación, la tecnología de la información puede satisfacer muchos mandatos, submandatos y requisitos.

- **Evaluación de la obligación**

  Una vez que los usuarios han correlacionado los controles internos con las obligaciones, los usuarios pueden realizar una evaluación de lo bien que están operando en relación con la obligación identificada. Los usuarios pueden evaluar la efectividad operativa y la efectividad de diseño de los controles dentro del ámbito de un tema de conformidad.

- **Proyecto**

  Un Proyecto se diseña para organizar tareas de normativas en un proyecto de conformidad general. Por ejemplo, puede haber cambios de normativa que se deben abordar en el marco de trabajo de conformidad; los usuarios pueden crear un proyecto para identificar y asignar tareas.

- **Reg-Track Evento normativo**

  El objeto de evento regulador Reg-Track habilita la ingestión directa de canales de información de eventos reguladores de Reg-Track en IBM OpenPages Regulatory Compliance Management.

- **Reg-Track Serie de eventos reguladores**

  El objeto Serie de eventos reguladores Reg-Track es una colección de eventos reguladores Reg-Track a los que se les ha asignado el mismo ID de serie Reg-Track dentro del canal de información de Reg-Track . La agrupación de eventos reguladores de Reg-Track dentro de la serie de eventos reguladores de Reg-Track permite realizar un seguimiento de los cambios desde la etapa propuesta hasta la etapa final en la evolución del cambio regulador.

- **Autoridad reguladora**

  El objeto Regulador forma parte de la capacidad de gestión de interacción del regulador y proporciona la posibilidad de que las organizaciones creen un inventario único de todos los reguladores con los que interactúan. Las actividades reguladoras normalmente se crean en una entidad de negocios de biblioteca. El objeto es un hijo de la entidad de negocios y se puede asociar a mandatos e interacciones con la actividad reguladora.

- **Interacción con la autoridad reguladora**

  El objeto Interacción de regulador forma parte de la capacidad de gestión de interacción del regulador. El objeto Interacción con la autoridad reguladora permite gestionar las interacciones, las comunicaciones, los trabajos internos, las revisiones y las aprobaciones asociadas con las autoridades reguladoras externas, como las consultas, los envíos, los archivados, los exámenes y las reuniones. Para las interacciones complejas, como por ejemplo los exámenes, puede utilizar los objetos Componente RI y Subcomponente RI para partir la interacción en componentes más pequeños o para rastrear las consultas de seguimiento procedentes de la entidad reguladora. La Interacción con la autoridad reguladora se puede correlacionar a los siguientes objetos padre: Autoridad reguladora, Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones padre permiten a un usuario enlazar objetos que puedan estar dando problemas en la Interacción con la autoridad reguladora, e identificar a los usuarios que son relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Se podrían asignar tareas individuales relacionadas con la gestión y respuesta a la interacción con la autoridad reguladora a usuarios a través de objetos hijo de tareas reguladoras.

- **Cambio regulador**

  El objeto Cambio regulador forma parte de la capacidad de Gestión de cambios reguladores. Ofrece la capacidad de realizar un seguimiento de los cambios reguladores, evalúa el impacto de una modificación en la organización, comunica el cambio a nivel interno a las personas que correspondan y gestiona los procesos internos de respuesta al cambio.

- **Evento normativo**

  El objeto Evento regulador se utiliza con IBM OpenPages Regulatory Compliance Management (RCM). El tipo de objeto Evento regulador permite la ingestión directa de canales de información de eventos reguladores utilizando la API REST o IBM® AppConnect en RCM. Junto con el **Motor de reglas**, el tipo de objeto Evento regulador da soporte a la generación automatizada de flujos de trabajo que asignan sucesos reguladores entrantes a los usuarios en función de los puntos de datos proporcionados. También se da soporte a los documentos que se ven afectados por el cambio normativo. Estas prestaciones ayudan a asignar tareas de forma eficiente a los usuarios para responder a los cambios normativos y prepararse para ellos de forma eficiente. Un evento regulador puede ser un hijo de una entidad empresarial, control, mandato, submandato, requisito, política o procedimiento. Los usuarios pueden crear objetos de cambio regulador como hijos de eventos reguladores.

- **Iniciativa reguladora**

  El objeto Iniciativa reguladora es hijo del objeto Entidad de negocios y captura información descriptiva sobre normativas que afectan a la organización. Las iniciativas reguladoras representan una agrupación más amplia de normativas. Por ejemplo, Antiblanqueo de dinero puede ser una iniciativa reguladoras que incluya varias normativas de blanqueo de dinero diferentes con las que las organizaciones deben cumplir.

- **Tarea reguladora**

  El objeto Tarea reguladora se utiliza para asignar tareas a usuarios de OpenPages cuando la tarea está relacionada con uno de los siguientes objetos padre: Proyecto, Política, Cambio regulador, Interacción con la autoridad reguladora, Componente RI o Subcomponente RI. Una Tarea reguladora también se puede asociar a una entidad de negocios.

- **Requisito**

  El objeto Requisito detalla los requisitos específicos, que se encuentran en el objeto Mandato o Submandato relacionado, que la organización debe cumplir para estar en conformidad.

- **Evaluación de requisitos**

  Después de que los usuarios correlacionan controles internos para los requisitos derivados de normativas, los usuarios pueden realizar una evaluación de lo bien que están funcionando en relación al requisito identificado. Los usuarios pueden evaluar la eficacia operativa y la eficacia del diseño de controles dentro del ámbito de un Tema de conformidad.

- **Valor de evaluación de requisito**

  Los Valores de evaluación de requisitos se utilizan para registrar el valor real de un requisito en un punto específico en el tiempo dentro del ámbito de una Evaluación de requisito.

- **Componente RI**

  El objeto Componente RI (anteriormente denominado Categoría RI) forma parte de la capacidad de Gestión de interacción de reguladores y se utiliza como el nivel medio del modelo de objeto de tres niveles (Interacción de regulador, Componente RI y Subcomponente RI). El objeto se utiliza para dividir una Interacción con la autoridad reguladora compleja en registros más pequeños, más manejables o para enlazar una consulta de seguimiento de una autoridad reguladora con el objeto padre de la Interacción con la autoridad reguladora. Además, el Componente RI se puede correlacionar con los siguientes objetos padre: Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones permiten a un usuario enlazar objetos que puedan estar dando problemas e identificar a los usuarios relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Las tareas individuales relacionadas con la gestión y respuesta a la interacción reguladora se pueden asignar a usuarios a través de un objeto hijo de tarea reguladora.

- **Subcomponente RI**

  El objeto Subcomponente RI (anteriormente denominado Solicitud RI) forma parte de la capacidad de gestión de interacción del regulador y se utiliza como último nivel del modelo de objeto de tres niveles (Interacción de regulador, Componente RI y Subcomponente RI). El objeto se utiliza para dividir una Interacción con la autoridad reguladora y el componente RI en registros más pequeños y manejables. Además, el Subcomponente RI se puede correlacionar con los siguientes objetos padre: Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones permiten a un usuario enlazar objetos que puedan estar dando problemas e identificar a los usuarios relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Las tareas individuales relacionadas con la gestión y respuesta a la interacción reguladora se pueden asignar a usuarios a través de objetos hijo de tareas reguladoras.

- **Submandato**

  Los submandatos representan subpartidas externas (o internas) con los que la organización debe cumplir. El contenido se puede extraer de proveedores de terceros, incluyendo UCF, Ascent Reg Tech, Thomson Reutersy Wolters Kluwer. Generalmente, los Submandatos están representados en una estructura de Entidad de negocios de biblioteca y no se replican en todo el sistema. El submandato es recursivo, pero el contenido de Deloitte, UCF, Ascent Reg Tech, Thomson Reutersy Wolters Kluwer utiliza exactamente un nivel de submandato. Los submandatos también soportan contenido para conformidad con la normativa. Los submandatos se pueden utilizar para representar párrafos derivados de informes reguladores.

- **Evento regulador TRRI**

  El objeto Evento regulador TRRI habilita la ingestión directa de canales de información de eventos reguladores de Thomson Reuters en IBM OpenPages Regulatory Compliance Management.

- **Serie de eventos reguladores TRRI**

  El objeto Serie de eventos reguladores de TRRI es una recopilación de eventos reguladores de TRRI a los que se ha asignado el mismo ID de serie dentro del canal de información TRRI. La agrupación de eventos reguladores TRRI dentro de la serie de eventos reguladores TRRI permite realizar el seguimiento de los cambios desde la etapa propuesta hasta la última en la evolución de los cambios reguladores.

- **Evento regulador WK**

  El objeto Evento regulador WK habilita la ingestión directa de canales de información de eventos reguladores de Wolters Kluwer en IBM OpenPages Regulatory Compliance Management.

## objetos de OpenPages Model Risk Governance

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-openpages-model-risk-governance-objects)

Este tema proporciona información sobre los objetos OpenPages® Model Risk Governance .

### OpenPages Model Risk Governance

`Guía del usuario › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-openpages-model-risk-governance)

IBM OpenPages® Model Risk Governance (MRG) da soporte a las organizaciones para organizar y centralizar su inventario de modelos.

Como solución, IBM OpenPages Model Risk Governance proporciona una plataforma configurable y personalizable, que permite a las empresas:

- Organizar, documentar y mantener un inventario de modelos de toda la empresa y sus usos
- Documentar y hacer seguimiento de problemas asociados con modelos en una ubicación central
- Registrar actividades de gobierno de la gestión de cambios de modelo.
- Planificar, hacer seguimiento y gestionar Revisiones y validaciones de modelo
- Realizar atestaciones de modelo y evaluaciones de riesgos de modelo periódicas
- Asignar funciones y responsabilidades apropiadas para la gestión de riesgos de modelo y propiedad de modelo
- Supervisar el rendimiento y el estado de su programa de gestión de riesgos de modelo
- Ver las relaciones entre su Inventario de modelos y los aspectos relevantes de sus obligaciones de política y conformidad

#### IBM Watson OpenScale Integración

IBM OpenPages Model Risk Governance (MRG) incluye una integración lista para usar con IBM Watson® OpenScale.

IBM Watson OpenScale es una herramienta que supervisa y mide los resultados de los modelos de IA en todo su ciclo de vida y realiza validaciones continuas de los modelos de IA. Las organizaciones pueden incluir modelos de inteligencia artificial en su inventario de modelos y enviar los resultados de la supervisión de rendimiento directamente a OpenPages.

#### Tutorial

Este vídeo proporciona una visión general de cómo se integra OpenPages con IBM Watson OpenScale:

[Este vídeo proporciona una descripción general de la integración entre MRG y OpenScale.](https://video.ibm.com/embed/channel/25817967/video/op-integrate-model-risk)

#### Campos

Los campos siguientes se utilizan en la integración con IBM Watson OpenScale:

- Grupo de campos MRG-Model

  - Modelo de aprendizaje automático
  - Supervisado con Watson Studio
- Grupo de campos MRG-Metric-Shared

  - Tipo de métrica
  - Categoría de Watson Studio
  - Descripción de Watson Studio
  - Métrica de Watson Studio
  - Valor de métrica de Watson Studio
  - Nombre de suscripción de Watson Studio
  - Tipo de suscripción de Watson Studio
  - Subcategoría de Watson Studio

#### Ejemplo de cálculo

El cálculo de actualización de valor de métrica se utiliza en la integración con IBM Watson OpenScale.

#### Filtro público

IBM Watson OpenScale utiliza un filtro público para el objeto Modelo para localizar modelos en OpenPages que tienen el campo Supervisado con Watson Studio establecido en Sí.

#### Perfiles de usuario

Los perfiles MRG incluyen los campos que dan soporte a la integración.

### objetos de OpenPages Model Risk Governance

`Guía del usuario › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=omrgo-openpages-model-risk-governance-objects)

Este tema proporciona información sobre los objetos IBM OpenPages® Model Risk Governance .

#### Solicitud de cambio

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-change-request)

El objeto Solicitud de cambio es hijo de los objetos Modelo y Despliegue de modelo y permite la creación y el seguimiento de actividades de gobierno relacionadas con los cambios en los modelos y sus despliegues. El objeto captura datos como Tipo de cambio, Descripción de cambio y Estado. Está soportado por un flujo de trabajo.

#### Comité

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-committee)

El objeto Comité es hijo de la entidad empresarial y permite a una organización representar grupos/comités de gobierno. Éstos pueden alinearse a continuación con los modelos y también puede ser el padre del objeto Empleado. Puede almacenar información como los Términos de referencia para un comité, la frecuencia de reuniones y el detalle del Moderador.

#### Métrica

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-metric)

El objeto Métrica registra la definición de una medida de rendimiento que la organización elige rastrear. Un usuario establece el Tipo de métrica, los Umbrales amarillo y rojo y otra información de la recopilación. Una Métrica es un hijo de los objetos Despliegue de modelo y Modelo.

#### Valor de métrica

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-metric-value)

El objeto Valor de métrica registra el resultado de la medida de rendimiento de métrica. Está diseñado para permitir a la organización almacenar los resultados de medida de las series temporales.

#### Modelo

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-model)

El objeto Modelo proporciona representación de los modelos dentro de una organización. A nivel teórico, un modelo como método cuantitativo, sistema o enfoque que se aplica a teorías, técnicas y asunciones estadísticas, económicas, financieras o matemáticas para procesar datos de entrada en estimaciones cuantitativas. Dentro del objeto Modelo, se puede representar información clave del modelo, incluyendo: descripción del modelo, propiedad del modelo, estado del modelo, fechas de ciclo de vida de desarrollo, tipo de modelo y categoría, y datos de evaluación de riesgos del modelo. Un objeto Modelo es hijo de una Entidad de negocios y padre de objetos Despliegue del modelo.

#### Atestación de modelo

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-model-attestation)

La testificación de modelo permite a una organización solicitar una validación regular o *testificación* de un modelo. El administrador de MRG crea periódicamente un conjunto de atestaciones de modelo en blanco, que se asignan a los respectivos propietarios de modelo. Cada propietario de modelo responde a un conjunto de preguntas acerca del modelo y envía su atestación de modelo.

#### Entrada de modelo

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-model-input)

Si una organización desea adoptar un enfoque más granular para la documentación del modelo, el objeto Entrada de modelo proporciona la posibilidad de registrar las entradas. Los campos incluyen Propietario de entrada, Tipo, Estado y Descripción. Un objeto de Entrada de modelo también puede ser el hijo de un objeto de Salida de modelo, lo que permite crear cadenas de modelos a un nivel de detalle si el enfoque de enlace de modelo no es suficientemente granular.

#### Enlace de modelo

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-model-link)

Si una organización desea adoptar un enfoque menos granular para la documentación del modelo, utilice el enlace de modelo, que es una asociación de tipo amplio que no proporciona detalles explícitos del canal de información de un modelo a otro. Actúa como hijo de varios modelos para permitir la generación de cadenas de modelos.

#### Salida del modelo

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-model-output)

Si una organización desea adoptar un enfoque más granular en la documentación del modelo, el objeto Resultado del modelo proporciona la posibilidad de registrar las salidas del modelo. La finalidad prevista es registrar la descripción y visión general de la salida desde un punto de vista de gobierno.

#### Tarjeta de puntuación de riesgo modelo

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-model-risk-scorecard)

Las evaluaciones de riesgo de modelo se realizan durante la fase de desarrollo y documentación de un modelo. También se realizan de forma periódica una vez que un modelo se encuentra en producción. El objeto Modelo de tarjeta de puntuación de riesgo se utiliza para realizar esta evaluación de riesgo. El usuario responde a una serie de preguntas sobre el modelo. Los desencadenantes de Tabla de puntuación de riesgo de modelo calculan una puntuación de riesgo y determinan el nivel de modelo.

#### Caso de uso de modelo

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-model-use-case)

El objeto Caso de uso de modelo o Caso de uso es un hijo de Entity y un padre del objeto Modelo. El uso del objeto Caso de uso de modelo es opcional. Su finalidad principal es actuar como biblioteca de los modelos durante el desarrollo.

#### Revisar

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-review)

El objeto de revisión se utiliza para registrar la planificación y los resultados de cualquier actividad de revisión de modelo. Es hijo de los objetos de despliegue de modelo y modelo. El objeto está pensado para capturar los resultados de revisiones realizadas preimplementación, postimplementación y realizadas por una segunda o tercera línea de defensa.

#### Despliegue de modelos

`Guía del usuario › objetos de OpenPages Model Risk Governance › objetos de OpenPages Model Risk Governance` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=objects-model-deployment)

El objeto Despliegue del modelo es hijo del modelo. Se utiliza como elemento clave para registrar el despliegue de uno o más modelos.

## Utilización de OpenPages Third Party Risk Management

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-third-party-risk-management-overview)

IBM OpenPages® Third Party Risk Management da soporte a las organizaciones en la organización y centralización de la información sobre sus proveedores.

Como solución, proporciona una plataforma configurable y personalizable, permitiendo firmas para:

- Crear, mantener y documentar todos los proveedores y compromisos
- Clasificar o "nivelar" proveedores como de baja, media o alta gravedad
- Utilizar evaluaciones de riesgo estándar para identificar y mitigar riesgos de manera específica para proveedores individuales
- Optimizar la prestación de evaluación del cuestionario para efectuar la organización en niveles de proveedores o compromisos utilizando información recopilada mediante evaluaciones y cuestionarios de riesgos y conformidad

En releases anteriores, IBM OpenPages Third Party Risk Management se denominaba Vendor Risk Management. El nombre original y el acrónimo, VRM, aún existen en los nombres internos de perfiles y plantillas de funciones.

### OpenPages Objetos de gestión de riesgos de terceros

`Guía del usuario › Visión general de la gestión de riesgos de terceros` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=overview-third-party-risk-management-object-types)

Este tema proporciona información sobre los objetos IBM OpenPages® Third Party Risk Management .

- **Contrato**

  Los objetos de contrato son objetos hijo de objetos Proveedor o Compromiso. Un Contrato representa un acuerdo legal o comercial entre una entidad de negocios y un Proveedor o un Compromiso. Un Contrato contiene información adicional de soporte, como, por ejemplo, el periodo de tiempo del contrato o información pecuniaria. Los Contratos son opcionales.

- **Compromiso**

  Los objetos de compromiso son objetos hijo de objetos de proveedor. Un Compromiso representa un servicio único proporcionado por un proveedor. Se utiliza para diferenciar los diversos servicios y acuerdos que tiene con un proveedor. Los compromisos son opcionales. Pueden estar sujetos a evaluaciones de cuestionario, evaluaciones de riesgo u organización en niveles. Puede resumir y analizar los riesgos asociados a distintos Compromisos. Puede añadir una asociación padre con el proceso o el subproceso que admite un Compromiso.

- **Ubicación**

  El tipo de objeto Ubicación se utiliza para capturar detalles de geografía y ubicación que son necesarios en el proceso de planificación de contingencia. La información de ubicación puede incluir, por ejemplo, el número de empleados que trabajan en una ubicación, los bienes (como el equipo de sistemas) y otros detalles de ubicación.

- **RapidRatings Calificaciones**

  RapidRatings Los objetos de clasificación se utilizan con el conector RapidRatings en IBM OpenPages Gestión de riesgos de terceros. Los objetos RapidRatings Ratings almacenan evaluaciones financieras y son hijos de los objetos Vendor.

- **RiskRecon Calificaciones**

  RiskRecon Los objetos de clasificación se utilizan con el conector RiskRecon en IBM OpenPages Gestión de riesgos de terceros. Los objetos de RiskRecon Ratings almacenan valoraciones y puntuaciones de proveedor en los niveles de categoría y subcategoría. Los objetos RiskRecon Ratings se crean bajo `/BusinessEntity/Library/VRM/VRMLibrary/RiskRecon` y son hijos de objetos Vendor.

- **Subcontratista**

  Los objetos Subcontratista son objetos hijo de objetos Proveedor. Un subcontratista representa una parte de un servicio proporcionado por un proveedor. Subcontratista es un tipo de objeto opcional. Los subcontratistas pueden estar sujetos a evaluaciones de cuestionarios, evaluaciones de riesgos o niveles. Puede resumir y analizar el riesgo asociado a distintos subcontratistas. Puede añadir una asociación padre al proceso o subproceso al que da soporte un subcontratista.

- **Supply Wisdom**

  El objeto Supply Wisdom almacena evaluaciones de riesgo de proveedores que se importan de Supply Wisdom. El tipo de objeto Supply Wisdom tiene un padre, Vendor.

- **Alerta padre de Supply Wisdom**

  El objeto Alerta padre Supply Wisdom almacena datos de alerta que se importan de Supply Wisdom. La importación crea objetos de suceso de continuidad de negocio para los datos de alerta entrantes y asocia las alertas a los objetos de proveedor y ubicación correspondientes en OpenPages.

- **Proveedor**

  Un proveedor es una empresa externa a la que una empresa adquiere bienes o servicios. Los proveedores pueden tener cuatro tipos de objetos hijo: Vendedor Filial, SubContractors, Encargos y Contratos. Los proveedores pueden estar sujetos a evaluaciones de cuestionario, evaluaciones de riesgo u organización en niveles. Puede resumir y analizar los riesgos asociados a los distintos Proveedores. Puede añadir una asociación padre al proceso o al subproceso al que da soporte el Proveedor.

- **Filial del proveedor**

  Una filial de proveedor representa una filial de un proveedor de la que una empresa adquiere bienes o servicios. Subsidiaria de proveedor es un tipo de objeto opcional. Subsidiaria de proveedor es un hijo de Proveedor. La Filial Proveedor puede tener tres tipos de objetos hijo: SubContractor, Encargos y Contratos. La filial del proveedor puede estar sujeta a evaluaciones de cuestionarios, evaluaciones de riesgos o niveles. Puede resumir y analizar el riesgo asociado con diferentes filiales de proveedor. Puede añadir una asociación padre al proceso o subproceso al que da soporte una filial de proveedor.

## Utilización de OpenPages Business Continuity Management

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-using-openpages-business-continuity-management)

IBM OpenPages® Business Continuity Management (BCM) es utilizado por una organización, o grupo, para mantener o reanudar un nivel predeterminado de operaciones durante o después de un suceso disruptivo. Se identifican todos los riesgos que pueden afectar potencialmente al negocio durante o después de un suceso.

Mediante BCM, las organizaciones pueden crear una infraestructura para identificar activos y procesos críticos y elaborar planes de continuidad de negocio de nivel empresarial.

BCM ayuda a las organizaciones a:

- Centralizar los datos de la continuidad de negocio
- Establecer, supervisar y probar umbrales de tolerancia de impacto para servicios empresariales importantes identificados
- Realizar análisis del impacto empresarial para determinar el grado de importancia de personas, procesos y activos
- Desarrollar planes de continuidad de negocio, incluyendo, pero sin limitarse a, el nivel de preparación para la recuperación tras desastre, planes de comunicación, listas de comprobación de equipos, preparación para emergencias, logística de empleados y listas de comprobación de proveedores
- Probar la eficacia del plan de continuidad de negocio e identificar y mitigar los riesgos clave
- Ejecutar flujos de trabajo de forma programada para garantizar que las revisiones de los servicios empresariales, los análisis de impacto empresarial, las asignaciones de dependencia y las pruebas se realicen a intervalos regulares
- Visualice las actividades de gestión de claves y supervise los indicadores clave de rendimiento y riesgo con un panel de control fácil de usar

El BCM tiene cálculos incorporados para ayudar a las organizaciones a determinar la importancia de los procesos para su negocio y garantizar la alineación de los objetivos de tiempo y puntos de recuperación entre los activos y los proveedores que soportan los procesos empresariales críticos. Los flujos de trabajo incorporados previamente permiten a las organizaciones redactar borradores, revisar, aprobar y publicar planes con desencadenantes para la caducidad y el archivado. Estos planes se pueden correlacionar con los análisis de impacto empresarial, políticas, procedimientos, procesos, ubicaciones, sucesos, problemas y pruebas del cliente.

### Tutorial: descripción general de BCM

Para obtener una descripción general de BCM, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general de BCM.](https://video.ibm.com/embed/channel/25817967/video/op-overview-bus-continuity)

### Tutorial: panel de control de BCM

Para obtener una descripción general del panel que está disponible para los usuarios asignados al perfil de Gestión de continuidad del negocio, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general del panel de control que está disponible para los usuarios que tienen el asignado el perfil de gestión de continuidad de negocio.](https://video.ibm.com/embed/channel/25817967/video/op-dashboard-business-continuity)

### Tutorial: objeto del plan de continuidad de negocio

Para obtener una descripción general del objeto Plan de continuidad del negocio y cómo se utiliza en BCM, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general del objeto del plan de continuidad de negocio y de cómo se utiliza en BCM.](https://video.ibm.com/embed/channel/25817967/video/op-plan-object-bus-continuity)

### Tutorial: objeto del análisis del impacto empresarial

Para obtener una descripción general del objeto Análisis de impacto empresarial y cómo se utiliza en BCM, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general del objeto del análisis del impacto empresarial y de cómo se utiliza en BCM.](https://video.ibm.com/embed/channel/25817967/video/op-business-impact-analysis)

### Tutorial: objeto del plan de pruebas de la continuidad de negocio

Para obtener una descripción general del objeto Plan de prueba de continuidad del negocio y cómo se utiliza en BCM, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general del objeto del plan de prueba de la continuidad de negocio y de cómo se utiliza en BCM.](https://video.ibm.com/embed/channel/25817967/video/op-test-plan-bus-continuity)

## Avisos

`Guía del usuario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ug-notices)

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

El siguiente párrafo no se aplica al Reino Unido ni a ningún otro país donde dichas disposiciones sean incompatibles con la legislación local: INTERNATIONAL BUSINESS MACHINES CORPORATION PROPORCIONA ESTA PUBLICACIÓN Y TODAS LAS MUESTRAS DE CÓDIGO "TAL CUAL" SIN GARANTÍA DE NINGÚN TIPO, YA SEA EXPRESA O IMPLÍCITA, INCLUYENDO, PERO NO LIMITADO A, LAS GARANTÍAS IMPLÍCITAS DE NO INFRACCIÓN, COMERCIABILIDAD O IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Algunos estados no permiten la declaración de limitación de responsabilidad de las garantías explícitas o implícitas en determinadas transacciones, por lo tanto, es posible que esta sentencia no sea aplicable en su caso.

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

Este manual contiene ejemplos de datos e informes que se utilizan en operaciones comerciales diarias. Para ilustrarlas de la forma más completa posible, los ejemplos incluyen los nombres de personas, empresas, marcas y productos. Todos estos nombres son ficticios y cualquier similitud a los nombres y direcciones que haya utilizado una empresa real es pura coincidencia.

Si ha optado por visualizar la copia software de esta información, puede que no aparezcan las fotografías y las ilustraciones a color.

Esta oferta de software no utiliza cookies ni otro tipo de tecnología para recopilar información de identificación personal.
