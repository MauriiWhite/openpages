---
product: IBM OpenPages 9.0.0
product_key: SSFUEU_9.0.0
file: 8
guide: Guía de soluciones
covers: Guía de soluciones — Avisos
chapters: 14
topics: 116
words: 66366
tasks: 0
concepts: 116
references: 0
tables: 48
code_blocks: 0
figures: 44
applies_to: sin declarar
updated: 2025-02-13
lang: es
source: https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-guide
extracted: 2026-09-11
---

# 8 · Guía de soluciones

> **Qué hay en este archivo.** «Guía de soluciones» de IBM OpenPages 9.0.0, completa: 14 capítulos. 116 temas, 48 tablas, 44 figuras y 66.366 palabras.
>
> **Capítulos:** Guía de soluciones · IBM OpenPages GRC Solutions · Novedades · Tipos de objeto · Asistentes · Notificaciones · Informes · Activadores · Perfiles · Plantillas de funciones · Cálculos de GRC · GRC Workflow · y 2 más.
>
> **Si lo que buscas no está acá.** El índice de los 2.511 temas del producto, con su archivo y su ancla, está en `index.md`.

**Términos propios de este archivo:** vulneración, regulador, continuidad, tolerancia, conformidad, ciclo, rcsa, master, reguladora, métrica, maestro, activador, first, cerrado.

## Índice de este archivo

- [Guía de soluciones](#guía-de-soluciones)
- [IBM OpenPages GRC Solutions](#ibm-openpages-grc-solutions)
  - [OpenPages Financial Controls Management](#openpages-financial-controls-management)
  - [OpenPages Model Risk Governance](#openpages-model-risk-governance)
  - [OpenPages Operational Risk Management](#openpages-operational-risk-management)
    - [IBM FIRST Risk Case Studies](#ibm-first-risk-case-studies)
  - [OpenPages Policy Management](#openpages-policy-management)
  - [OpenPages IT Governance](#openpages-it-governance)
  - [OpenPages Internal Audit Management](#openpages-internal-audit-management)
  - [Gestión de problemas y corrección](#gestión-de-problemas-y-corrección)
  - [Indicadores clave de riesgo e Indicadores clave de rendimiento (KRI y KPI)](#indicadores-clave-de-riesgo-e-indicadores-clave-de-rendimiento-kri-y-kpi)
  - [OpenPages Gestión de riesgos de terceros](#openpages-gestión-de-riesgos-de-terceros)
  - [OpenPages Regulatory Compliance Management](#openpages-regulatory-compliance-management)
  - [Utilización de OpenPages Business Continuity Management](#utilización-de-openpages-business-continuity-management)
  - [OpenPages Data Privacy Management](#openpages-data-privacy-management)
  - [OpenPages Gestión de riesgos para ESG](#openpages-gestión-de-riesgos-para-esg)
- [Novedades](#novedades)
  - [Características nuevas de la versión 9.0.0.0](#características-nuevas-de-la-versión-9000)
  - [Características nuevas de la versión 8.3.0.2](#características-nuevas-de-la-versión-8302)
  - [Características nuevas de la versión 8.3.0.1](#características-nuevas-de-la-versión-8301)
  - [Nuevas características en la versión 8.3.0](#nuevas-características-en-la-versión-830)
  - [Nuevas características en la versión 8.2.0.3](#nuevas-características-en-la-versión-8203)
  - [Nuevas características en la versión 8.2.0.2](#nuevas-características-en-la-versión-8202)
  - [Nuevas características en la versión 8.2.0.1](#nuevas-características-en-la-versión-8201)
  - [Características nuevas de la versión 8.2.0](#características-nuevas-de-la-versión-820)
- [Tipos de objeto](#tipos-de-objeto)
  - [Correlación de nombres de objeto](#correlación-de-nombres-de-objeto)
  - [Descripciones de tipo de objeto](#descripciones-de-tipo-de-objeto)
  - [Subcomponentes](#subcomponentes)
- [Asistentes](#asistentes)
  - [Asistente de relleno de RCSA](#asistente-de-relleno-de-rcsa)
  - [Asistente de alineación de procesos RCSA](#asistente-de-alineación-de-procesos-rcsa)
  - [Asistente del programa de utilidad de inicio de RCSA](#asistente-del-programa-de-utilidad-de-inicio-de-rcsa)
  - [Asistente de sincronización de sitios de RCSA](#asistente-de-sincronización-de-sitios-de-rcsa)
  - [Configuración de asistentes de RCSA](#configuración-de-asistentes-de-rcsa)
  - [Visores de políticas](#visores-de-políticas)
  - [Asistente Vista de comparación de políticas](#asistente-vista-de-comparación-de-políticas)
  - [Asistente Desbloquear política](#asistente-desbloquear-política)
  - [Asistente Publicar notificación por lotes](#asistente-publicar-notificación-por-lotes)
  - [Asistente Vista de conocimiento de política](#asistente-vista-de-conocimiento-de-política)
  - [Asistente Informe de creación de atestación](#asistente-informe-de-creación-de-atestación)
  - [Asistente Obtener líneas base](#asistente-obtener-líneas-base)
  - [Asistente Crear enlaces de recursos](#asistente-crear-enlaces-de-recursos)
  - [Asistente Cerrar auditoría](#asistente-cerrar-auditoría)
  - [Asistente para añadir o modificar planificaciones](#asistente-para-añadir-o-modificar-planificaciones)
  - [Asistentes de hoja de registro horario](#asistentes-de-hoja-de-registro-horario)
    - [Asistente de entrada de hoja de registro horario](#asistente-de-entrada-de-hoja-de-registro-horario)
    - [Asistente de aprobación de hoja de registro horario](#asistente-de-aprobación-de-hoja-de-registro-horario)
- [Notificaciones](#notificaciones)
  - [Notificación a través del boletín de problemas y acciones](#notificación-a-través-del-boletín-de-problemas-y-acciones)
  - [Notificación de incidente](#notificación-de-incidente)
  - [Notificación de evaluación de cuestionario](#notificación-de-evaluación-de-cuestionario)
  - [Notificación de error de ingesta de Reg-Track](#notificación-de-error-de-ingesta-de-reg-track)
  - [Notificación de Error de ingesta TRRI](#notificación-de-error-de-ingesta-trri)
  - [Notificación de Error de ingesta WK](#notificación-de-error-de-ingesta-wk)
  - [Notificación de objetos de biblioteca reguladora nuevos/corregidos](#notificación-de-objetos-de-biblioteca-reguladora-nuevoscorregidos)
- [Informes](#informes)
  - [Informes de evaluación de riesgos](#informes-de-evaluación-de-riesgos)
  - [Informes de riesgos](#informes-de-riesgos)
  - [Informes de control](#informes-de-control)
  - [Informes de prueba](#informes-de-prueba)
  - [Informes de indicador](#informes-de-indicador)
  - [Informes de eventos de pérdida](#informes-de-eventos-de-pérdida)
  - [Informes de gestión de problemas y corrección](#informes-de-gestión-de-problemas-y-corrección)
  - [Informes de análisis de escenarios](#informes-de-análisis-de-escenarios)
  - [Informes de conformidad reguladora](#informes-de-conformidad-reguladora)
  - [Informes de activos de TI](#informes-de-activos-de-ti)
  - [Informes de conformidad de TI](#informes-de-conformidad-de-ti)
  - [Informes de administración de auditoría](#informes-de-administración-de-auditoría)
  - [Informes de cuestionario](#informes-de-cuestionario)
  - [Informes de gestión de controles financieros](#informes-de-gestión-de-controles-financieros)
  - [Informes de gestión de riesgos para ESG](#informes-de-gestión-de-riesgos-para-esg)
- [Activadores](#activadores)
  - [Tipos de objeto que contienen activadores](#tipos-de-objeto-que-contienen-activadores)
  - [Autoevaluaciones de riesgo y control (desencadenantes y cálculos)](#autoevaluaciones-de-riesgo-y-control-desencadenantes-y-cálculos)
  - [Activadores de ciclo de vida de control](#activadores-de-ciclo-de-vida-de-control)
  - [Activador de importación de políticas](#activador-de-importación-de-políticas)
  - [Activador de bloqueo de políticas](#activador-de-bloqueo-de-políticas)
  - [Activador de cálculos de clasificación de riesgos de la auditoría](#activador-de-cálculos-de-clasificación-de-riesgos-de-la-auditoría)
  - [Activador de automatización de cierre de auditoría](#activador-de-automatización-de-cierre-de-auditoría)
  - [Desencadenante de tarjeta de puntuación de riesgo de modelo](#desencadenante-de-tarjeta-de-puntuación-de-riesgo-de-modelo)
  - [Activador Tipo de cambio](#activador-tipo-de-cambio)
- [Perfiles](#perfiles)
- [Plantillas de funciones](#plantillas-de-funciones)
  - [Lista de plantillas de funciones](#lista-de-plantillas-de-funciones)
  - [Permisos de plantillas de funciones](#permisos-de-plantillas-de-funciones)
  - [Permisos de tipo de objeto asignados por plantilla de funciones](#permisos-de-tipo-de-objeto-asignados-por-plantilla-de-funciones)
- [Cálculos de GRC](#cálculos-de-grc)
  - [Cálculos de ejemplo](#cálculos-de-ejemplo)
- [GRC Workflow](#grc-workflow)
  - [Flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo)
  - [Flujos de trabajo de IBM OpenPages Business Continuity Management (BCM)](#flujos-de-trabajo-de-ibm-openpages-business-continuity-management-bcm)
  - [Flujos de trabajo de IBM OpenPages Data Privacy Management (DPM)](#flujos-de-trabajo-de-ibm-openpages-data-privacy-management-dpm)
  - [IBM OpenPages Financial Controls Management (FCM)](#ibm-openpages-financial-controls-management-fcm)
  - [Flujos de trabajo de IBM OpenPages IT Governance (ITG)](#flujos-de-trabajo-de-ibm-openpages-it-governance-itg)
  - [Flujos de trabajo de IBM OpenPages Model Risk Governance (MRG)](#flujos-de-trabajo-de-ibm-openpages-model-risk-governance-mrg)
  - [IBM OpenPages Policy Management (PCM)](#ibm-openpages-policy-management-pcm)
  - [IBM OpenPages Regulatory Compliance Management (RCM)](#ibm-openpages-regulatory-compliance-management-rcm)
  - [Flujos de trabajo de IBM OpenPages Risk Management for ESG](#flujos-de-trabajo-de-ibm-openpages-risk-management-for-esg)
  - [Flujos de trabajo de IBM OpenPages Third Party Risk Management (TPRM)](#flujos-de-trabajo-de-ibm-openpages-third-party-risk-management-tprm)
- [Características heredadas](#características-heredadas)
  - [Visualizaciones de procesos empresariales (existentes)](#visualizaciones-de-procesos-empresariales-existentes)
  - [Campos calculados](#campos-calculados)
  - [Activadores heredados](#activadores-heredados)
    - [Desencadenantes de ciclo de vida de eventos de pérdida (versión 7.2.0.1 y posterior) (existentes)](#desencadenantes-de-ciclo-de-vida-de-eventos-de-pérdida-versión-7201-y-posterior-existentes)
    - [Desencadenantes del ciclo de vida de eventos de pérdida (existentes)](#desencadenantes-del-ciclo-de-vida-de-eventos-de-pérdida-existentes)
    - [Desencadenantes de ciclo de vida de evaluación de cuestionario (existentes)](#desencadenantes-de-ciclo-de-vida-de-evaluación-de-cuestionario-existentes)
    - [Desencadenantes de ciclo de vida de incidencias (existentes)](#desencadenantes-de-ciclo-de-vida-de-incidencias-existentes)
    - [Desencadenantes de ciclo de vida añadidos en la versión 7.2.0.1 (existentes)](#desencadenantes-de-ciclo-de-vida-añadidos-en-la-versión-7201-existentes)
    - [Configuración del ciclo de vida (existente)](#configuración-del-ciclo-de-vida-existente)
    - [Desencadenantes de RCSA cuantitativas y RCSA cualitativas (existente)](#desencadenantes-de-rcsa-cuantitativas-y-rcsa-cualitativas-existente)
    - [Desencadenantes de ciclo de vida de KRI y KPI (existentes)](#desencadenantes-de-ciclo-de-vida-de-kri-y-kpi-existentes)
  - [Tipos de objetos existentes](#tipos-de-objetos-existentes)
  - [Informes y ayudantes ya existentes](#informes-y-ayudantes-ya-existentes)
  - [Flujos de trabajo y cálculos existentes](#flujos-de-trabajo-y-cálculos-existentes)
- [Avisos](#avisos)


# Guía de soluciones

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-guide)

La publicación *IBM OpenPages Guía de soluciones* está pensada para los usuarios que necesitan utilizar las soluciones que se proporcionan con OpenPages®. El contenido describe los tipos de objeto para cada solución. Identifica también los subcomponentes, campos calculados, asistentes, notificaciones, informes, activadores, perfiles, plantillas de funciones, vistas y flujos de trabajo compatibles con cada solución.

## IBM OpenPages documentación

IBM® mantiene un conjunto de servicios de documentación IBM OpenPages, IBM OpenPages for IBM Cloud Pak for Datay IBM OpenPages on Cloud despliegues. La documentación de IBM OpenPages describe determinadas características y funciones que pueden no estar disponibles en la nube.

Si tiene alguna pregunta sobre la funcionalidad disponible en la versión del producto que está utilizando, póngase en contacto con el soporte deIBM utilizando el [portal de soporte de IBM](https://www.ibm.com/mysupport).

## Funciones de accesibilidad

Las características de accesibilidad ayudan a los usuarios que tienen alguna discapacidad física, por ejemplo movilidad restringida o visión limitada, a utilizar productos de tecnología de la información. La documentación de OpenPages tiene características de accesibilidad. Los documentos PDF son complementarios y no incluyen características de accesibilidad.

## Licencias de tipos de objeto

Tiene licencia para utilizar los tipos de objeto para cada solución de IBM OpenPages que haya adquirido.

Para obtener una lista completa de los tipos de objeto proporcionados con cada solución, consulte [Tipos de objeto](#tipos-de-objeto). El uso de cualquier otro tipo de objeto está prohibido sin la aprobación previa por escrito de IBM.

## Acrónimos de soluciones

En esta guía se utilizan los siguientes acrónimos de soluciones:

- BCM = IBM OpenPages Business Continuity Management
- DPM = IBM OpenPages Data Privacy privacidad de datos
- ESG = IBM OpenPages Risk Management for ESG
- FCM = IBM OpenPages Financial Controls Management
- ITG = IBM OpenPages IT Governance
- IAM = IBM OpenPages Internal Audit Management
- MRG = IBM OpenPages Model Risk Governance
- ORM = IBM OpenPages Operational Risk Management
- PCM = IBM OpenPages Gestión de políticas
- RCM = IBM OpenPages Regulatory Compliance Management
- TPRM = IBM OpenPages Gestión de riesgos de terceros

## IBM OpenPages GRC Solutions

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-openpages-grc-solutions)

IBM OpenPages® contiene las soluciones siguientes.

### OpenPages Financial Controls Management

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-financial-controls-management)

IBM OpenPages® Financial Controls Management (FCM) reduce el tiempo y los costes de recursos asociados con la conformidad continua de las normativas de informes financieros.

IBM OpenPages Financial Controls Management combina una potente gestión de documentos y procesos con amplias prestaciones de creación de informes interactivos en un entorno fácil de utilizar flexible y adaptable. Esta característica proporciona a los CEO, CFO, gestores, auditores independientes y comités de auditoría la capacidad de realizar todas las actividades necesarias para cumplir las regulaciones sobre informes financieros de una forma sencilla y eficaz.

Permite a los usuarios ver fácilmente el estado de sus proyectos de documentación sobre controles financieros y proporciona un repositorio seguro para el almacenamiento de la documentación de sus controles internos.

Sus principales características son:

- Un repositorio de gestión de controles financieros, que presenta los procesos,los riesgos y controles de modo lógico en relaciones de varios a varios y compartidas en diferentes niveles y permite adjuntar archivos y planes de acción a los procesos, riesgos, controles y pruebas a todos los niveles.
- Automatización flexible que proporciona notificación y finalización de las actividades de gestión de los controles financieros, como revisión de diseño, revisión de funcionamiento y certificación.
- Informes, supervisión y análisis.
- Los flujos de trabajo preconstruidos crean un enfoque automatizado, coherente y repetible para reducir la complejidad del proceso de subcertificación interna de una organización.
- Mayor visibilidad para la función de supervisión en la salud de los marcos de proceso y control interno de la organización.
- Los informes accionables y a la carta permiten a los usuarios identificar, remediar y notificar los riesgos con mayor rapidez.

#### Mostrar cómo: Visión general de FCM

Este vídeo proporciona una descripción general de FCM:

[Este vídeo proporciona una visión general de FCM.](https://video.ibm.com/embed/channel/25817967/video/op-overview-financial-controls)

### OpenPages Model Risk Governance

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-model-risk-governance)

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

### OpenPages Operational Risk Management

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-operational-risk-management)

IBM OpenPages® Operational Risk Management (ORM) combina la gestión de documentos y procesos con un sistema de supervisión y soporte de decisiones. IBM OpenPages Operational Risk Management permite a las organizaciones analizar, gestionar y mitigar el riesgo de una forma sencilla y eficiente.

IBM OpenPages Operational Risk Management ayuda a automatizar el proceso de medición y supervisión del riesgo operativo. Combina todos los datos de riesgo, incluidas las evaluaciones de riesgos y autocontrol, los eventos de pérdida, los análisis de escenarios, las pérdidas externas y los indicadores claves de riesgo (KRI) en un única solución integrada.

IBM OpenPages Operational Risk Management incluye las siguientes características clave:

- Eventos de pérdida para monitorizar, evaluar y gestionar eventos internos y externos que podrían originar pérdidas operativas.
- Evaluaciones de autocontrol y riesgos (RCSA) para identificar, medir y reducir el riesgo.
- Indicadores claves de riesgo (KRI) e indicadores clave de rendimiento (KPI), que pueden realizar un seguimiento de las mediciones de rendimiento para mostrar potencialmente la presencia o el estado de una condición de riesgo o una tendencia.
- Análisis de escenarios, que es una técnica de evaluación que se utiliza para identificar y medir determinadas clases de riesgos, en particular, los eventos muy graves y de baja frecuencia.
- Eventos de pérdida externa para importar datos de pérdida de IBM® FIRST Risk Case Studies, ORX y bases de datos de pérdida ORIC
- Gestión de problemas y corrección (IMR)
- Informes, supervisión y análisis

#### IBM FIRST Risk Case Studies

`Guía de soluciones › IBM OpenPages GRC Solutions › OpenPages Operational Risk Management` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=management-first-risk-case-studies)

La base de datos IBM FIRST Risk Case Studies es una colección de eventos de pérdida de riesgo operativo públicos externos en forma de estudios de caso de riesgo.

Los sucesos de IBM FIRST Risk Case Studies están dirigidos al sector financiero y contienen más de 20 años de sucesos, que se han indexado en 13 jerarquías de palabras clave, incluidas la categoría de Basilea y la línea de negocio. Otras jerarquías incluyen el factor de control, el activador de eventos, el tipo de unidad de negocio y el tipo de entidad. Los casos de IBM FIRST Risk Case Studies incluyen descripciones detalladas que desglosan el suceso para analizar la causa raíz, identificar los desgloses de control, las lecciones aprendidas, la respuesta de gestión y las secuelas del suceso. Los eventos también pueden incluir secciones con detalles de respaldo que proporcionan una línea temporal al evento, información relevante sobre la institución en la que sucedió y otros detalles sobre el impacto de las pérdidas.

La mayoría de los sucesos de IBM FIRST Risk Case Studies capturan información cuantitativa, así como un análisis cualitativo detallado. Esta información cuantitativa toma la forma de importes de pérdida que se capturan en el momento del evento.

IBM FIRST Risk Case Studies ofrece una suscripción a un complemento de datos renovado diariamente con la base de datos IBM FIRST Risk Case Studies en un formato compatible con la característica FastMap .Los clientes de IBM OpenPages® pueden utilizar el complemento de datos IBM FIRST Risk Case Studies FastMap para proporcionar a los usuarios finales acceso a los estudios de caso de IBM FIRST Risk Case Studies dentro de la aplicación OpenPages . Una vez cargados los datos en OpenPages, los usuarios finales pueden examinar y asociar los estudios de caso de IBM FIRST Risk Case Studies a objetos como Análisis de escenario, Riesgos y Eventos de pérdida. Póngase en contacto con el representante de la cuenta de IBM para obtener detalles sobre cómo obtener el complemento de datos IBM FIRST Risk Case Studies para OpenPages.

Si se suscribe al servicio de base de datos IBM FIRST Risk Case Studies , IBM FIRST Risk Case Studies proporciona un archivo FastMap compatible para una carga sin fisuras de datos de IBM FIRST Risk Case Studies a IBM OpenPages Operational Risk Management.

De forma predeterminada, IBM OpenPages Operational Risk Management incluye el perfil OpenPages FIRST Loss. Los usuarios con este perfil pueden cargar datos de FIRST Loss a través de la característica IBM OpenPages FastMap . Para obtener más información sobre este perfil, consulte [Perfiles](#perfiles).

### OpenPages Policy Management

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-policy-management)

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

### OpenPages IT Governance

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-it-governance)

IBM OpenPages® IT Governance (ITG) alinea los servicios de TI, los riesgos y las políticas con las iniciativas empresariales corporativas, la estrategia y los estándares operativos.

IBM OpenPages IT Governance le permite gestionar el control interno de TI y el riesgo de acuerdo con los procesos de negocio a los que dan soporte. Asimismo, unifica varios silos de riesgos y conformidad de los departamentos de TI para proporcionar una mejor visibilidad, servir de base a la toma de decisiones y, en última instancia, mejorar el rendimiento de la empresa.

Sus principales características son:

- Cumplimiento regulatorio y de las políticas por parte de los departamentos de TI
- Evaluaciones de riesgo y control
- Pruebas de control y solución de problemas
- Gestión de recursos de TI
- Seguimiento de incidentes
- Seguimiento y puntuación de vulnerabilidades
- Indicadores clave de rendimiento y de riesgo
- Informes, supervisión y análisis

#### RiskLens Conector

IBM OpenPages IT Governance incluye una integración con la plataforma de análisis de cuantificación de riesgos cibernéticos RiskLens.

En la plataforma RiskLens , los usuarios registran los activos y amenazas incluidos en los escenarios y rellenan estos objetos de acuerdo con el método FAIR utilizando los ayudantes de datos proporcionados en RiskLens para obtener orientación. La integración con OpenPages permite a un usuario de OpenPages enviar un registro para su inclusión en una evaluación de riesgo en RiskLens. El objeto se puede asociar a uno o más escenarios dentro de RiskLens y se realizan simulaciones de Monte Carlo. Después de completar la simulación, y de acuerdo con el trabajo planificado en OpenPages, las métricas de exposición a pérdidas generadas por las simulaciones de Monte Carlo se incorporan a OpenPages para su uso en toda la aplicación. El trabajo planificado en OpenPages también extrae datos actualizados de RiskLens cuando se modifican las evaluaciones de riesgos.

Para obtener información sobre cómo configurar el conector RiskLens , consulte la publicación  [*IBM OpenPages Guía del administrador*](3.5-guia-del-administrador.md#ibm-openpages-it-governance-con-risklens) .

### OpenPages Internal Audit Management

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-internal-audit-management)

IBM OpenPages® Internal Audit Management (IAM) proporciona a los auditores internos una vista configurada de forma exclusiva del gobierno organizativo, el riesgo y la conformidad (GRC), lo que permite a la auditoría complementar y coexistir con actividades más amplias de gestión del riesgo y la conformidad.

IBM OpenPages Internal Audit Management está completamente integrado con la gestión de controles financieros, el gobierno de TI, los esfuerzos de gestión de políticas y los programas de gestión de riesgos operativos. El equipo de auditoría interna tiene la capacidad de trabajar como un socio completamente integrado con los actores clave, de forma totalmente independiente o en una posición intermedia, en función de las necesidades concretas del departamento de auditorías o de lo que determine la auditoría en particular que se está realizando.

Sus principales características son:

- La capacidad de clasificar los riesgos del universo de auditoría, configurado en función de su metodología de auditoría

  - Amplia compatibilidad con su metodología de evaluación de riesgos
  - Informes completos en la totalidad del universo de la auditoría
- Capacidad para definir, planificar, ejecutar e informar sobre las auditorías en toda la empresa

  - Seguimiento y gestión de auditorías, secciones de auditoría, informes de trabajo y requisitos y asignaciones de recursos de auditoría
  - Automatizar operaciones a través de un creación de informes completamente configurables
- Capacidad de proporcionar una garantía independiente a la empresa o funcionar como una parte integral de los esfuerzos de GRC

  - Opinión independiente sobre los esfuerzos de GRC del equipo de gestión
  - Control del acceso a auditorías, campos y vistas de solo auditoría confidenciales

### Gestión de problemas y corrección

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-issue-management-remediation)

El proceso de Gestión de problemas y corrección (IMR) es un componente esencial de cualquier programa de gestión de riesgos. Una infraestructura IMR sólida ofrece reconocimiento, validación y transparencia al programa de gestión de riesgos al que da soporte.

Cuando se implementa de forma correcta, proporciona un alto valor con una sobrecarga mínima y sirve como estímulo subyacente para la continua mejora de un programa de gestión de riesgos. Una infraestructura IMR efectiva documenta, supervisa, corrige y audita los problemas identificados.

Los problemas son eventos que afectan de forma negativa a la gestión y notificación de los riesgos de forma precisa. Estos eventos se identifican en relación con la infraestructura IMR documentada. Los problemas se pueden asociar con objetos dentro de la infraestructura y tienen, por lo general, atributos como la propiedad, la programación y el estado de corrección que identifican el área de concentración. Un problema puede estar asociado con varios elementos principales. Por ejemplo, si se descubre un problema a través de un evento de pérdida, el problema se puede asociar con el evento de pérdida, el riesgo que se ha producido y cualquier control con error que se haya documentado.

El proceso IMR funciona en las siguientes actividades clave:

1. Creación y asignación de problemas
2. Creación y asignación de acciones
3. Rendimiento de la solución
4. Cierre del problema
5. Creación de informes

#### Creación y asignación de problemas

Los problemas surgen como resultado de diferentes actividades de gestión de riesgos, como un evento de pérdida, una ruptura del umbral o la identificación de una debilidad del control. A lo largo de estas actividades, los usuarios pueden crear un problema en IBM OpenPages.

Cuando se crea un problema, el flujo de trabajo de revisión de problemas se inicia automáticamente. Para obtener más información, consulte [Emitir flujo de trabajo de revisión](#flujos-de-trabajo-de-ejemplo).

#### Creación y asignación de acciones

Es responsabilidad del propietario del problema establecer y registrar las acciones adecuadas para resolver el problema identificado.

Cuando se crea una acción, el flujo de trabajo Elemento de acción se inicia automáticamente. Para obtener más información, consulte [Flujo de trabajo Aprobación de elemento de acción](#flujos-de-trabajo-de-ejemplo).

Se capturan los siguientes datos sobre un elemento de acción: descripción, responsable, fecha de inicio, fecha de vencimiento, fecha de cierre real, estado (solo lectura) y comentarios.

Los responsables de la acción reciben una notificación de que deben realizar una acción.

#### Rendimiento de la solución

Después de recibir la notificación, el responsable realiza la acción asignada. Algunas acciones pueden tardar algún tiempo en completarse, por lo que el responsable añade comentarios para realizar un seguimiento del progreso.

Cuando se completa la acción, el asignado selecciona **Acciones** > **Enviar para aprobación**.

#### Cierre del problema

El propietario del problema accede a una lista de acciones para aprobar el cierre.

Si la acción se rechaza y se guarda, el estado cambia a pendiente y la acción vuelve a la persona que tiene asignada la acción. Si la acción se acepta para su cierre y se guarda, el estado de la acción cambiará a cerrado y el campo **Fecha de cierre** se rellenará con la fecha actual.

Una vez finalizadas las acciones, el propietario del problema revisa el problema y actualiza el estado a **Cerrado**.

#### Creación de informes

Existen varios informes de problemas y de acciones a disposición de todos los usuarios. Asimismo, todas las notificaciones por correo electrónico se incluyen en un único boletín de problemas y acciones para los usuarios, incluida la siguiente información:

- Problemas asignados al destinatario en los X últimos días.
- Acciones asignadas al destinatario en los X últimos días.
- Problemas previstos para cerrar en los próximos X días.
- Acciones previstas para cerrar en los próximos X días.
- Problemas vencidos.
- Acciones vencidas.
- Acciones a la espera de aprobación de cierre.

### Indicadores clave de riesgo e Indicadores clave de rendimiento (KRI y KPI)

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ogs-key-risk-indicators-key-performance-indicators-kris-kpis)

Los indicadores clave de riesgo (KRI) y los indicadores clave de rendimiento (KPis) están disponibles para las soluciones siguientes: IBM OpenPages Operational Risk Management, IBM OpenPages IT Governancey IBM OpenPages Business Continuity Management.

Las principales fases dentro del ciclo de vida de los indicadores clave son la definición, la creación de valor, la captura de valor y la elaboración de informes. Se proporciona la automatización siguiente en estas etapas para KRI y KPI para ofrecer soporte a un programa de gestión de métricas:

- **Definición de indicador**

  Los indicadores se pueden crear desde cero o basándose en indicadores estándares de una biblioteca de indicadores.

- **Creación de valor**

  Los objetos KRI y valor KPI se crean automáticamente mediante el flujo de trabajo de creación de valor de KRI, que se ejecuta de forma planificada. El flujo de trabajo también puede ser ejecutado por un administrador.

- **Captura de valor**

  El flujo de trabajo de entrada de valor de KRI asigna valores de KRI a los usuarios y proporciona un proceso para la aprobación de valor de KRI. Las notificaciones de que un valor debe especificarse se envían automáticamente al valor Recopilador de indicadores activos que están cerca de su fecha de recopilación. Cuando el valor se ha entrado y guardado, los cálculos calculan automáticamente la infracción y otros valores de estado, y los mantienen en el valor y en el indicador. Es posible que tenga que pulsar otra pestaña y volver a la vista para ver los últimos valores de KRI o KPI. Si el Estado de vulneración de indicador clave de riesgo es rojo, se crea un problema hijo.

- **Informes de indicadores**

  Los paneles de control de KRI y KPI muestran información de indicador de resumen para la entidad empresarial seleccionada y sus descendientes, con la capacidad de profundizar en la información de detalles y tendencias para los valores de indicadores.

### OpenPages Gestión de riesgos de terceros

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-third-party-risk-management)

IBM OpenPages® Third Party Risk Management (TPRM) da soporte a las empresas en la evaluación y el análisis de riesgos asociados a los proveedores con los que hacen negocios.

IBM OpenPages Gestión de riesgos de terceros aporta transparencia a las actividades operativas y de seguridad para los proveedores y los subcontratistas que contratan. Ofrece un modo escalable de gestionar el cumplimiento de terceros y los riesgos. Las empresas pueden utilizarlo para comprender con mayor claridad cómo los proveedores individuales o los compromisos se relacionan con los procesos de negocio.

IBM OpenPages Gestión de riesgos de terceros permite a las empresas realizar las tareas siguientes:

- Crear, mantener y documentar todos los proveedores y compromisos
- Clasificar o «“nivelar”» proveedores como de baja, media o alta gravedad
- Gestionar contratos con proveedores de terceros
- Comprender cómo soportan su negocio los compromisos de terceros
- Utilizar evaluaciones de riesgo estándar para identificar y mitigar riesgos de manera específica para proveedores individuales
- Aprovechar las prestaciones de evaluación de cuestionarios para clasificar proveedores o compromisos utilizando información recopilada mediante evaluaciones de cuestionarios de cumplimiento o riesgos.
- Recopilar y almacenar evidencias en una ubicación central
- Importar detalles y valoraciones de proveedores de datos de terceros
- Remediar y mitigar riesgos tras identificarlos
- Crear indicadores de riesgos y rendimiento claves
- Supervisar e informar sobre riesgos de manera continuada

En releases anteriores, IBM OpenPages Third Party Risk Management se denominaba Vendor Risk Management. El nombre original y el acrónimo, VRM, aún existen en los nombres internos de perfiles y plantillas de funciones.

#### RapidRatings Conector

OpenPages Third Party Risk Management incluye un conector para RapidRatings.

El conector RapidRatings le permite importar detalles de proveedor y evaluaciones financieras de RapidRatings a objetos de proveedor en OpenPages. A continuación, puede ver las evaluaciones en OpenPages.

Para obtener información sobre cómo configurar el conector Supply Wisdom , consulte la publicación  [*IBM OpenPages Guía del administrador*](3.6-guia-del-administrador.md#conector-de-rapidratings-para-ibm-openpages-third-party-risk-management) .

#### RiskRecon Conector

OpenPages Third Party Risk Management incluye un conector para RiskRecon.

El conector RiskRecon le permite importar detalles de proveedor y valoraciones de RiskRecon a objetos de proveedor en OpenPages. A continuación, puede ver las evaluaciones en OpenPages.

Para obtener información sobre cómo configurar el conector RiskRecon , consulte la publicación  [*IBM OpenPages Guía del administrador*](3.6-guia-del-administrador.md#conector-de-riskrecon-para-ibm-openpages-third-party-risk-management) .

#### SecurityScorecard Conector

OpenPages Third Party Risk Management incluye un conector para SecurityScorecard.

El conector SecurityScorecard le permite importar valoraciones de seguridad de SecurityScorecard a objetos de proveedor en OpenPages. A continuación, puede ver las evaluaciones en OpenPages.

Para obtener información sobre cómo configurar el conector SecurityScorecard , consulte la publicación  [*IBM OpenPages Guía del administrador*](3.6-guia-del-administrador.md#conector-de-securityscorecard-para-ibm-openpages-third-party-risk-management) .

#### Supply Wisdom Conector

OpenPages Third Party Risk Management incluye un conector para Supply Wisdom.

El conector Supply Wisdom le permite importar detalles de proveedor, evaluaciones, alertas y ubicaciones de Supply Wisdom en objetos Proveedor en OpenPages. A continuación, puede ver las evaluaciones en OpenPages.

Para obtener información sobre cómo configurar el conector Supply Wisdom , consulte la publicación  [*IBM OpenPages Guía del administrador*](3.6-guia-del-administrador.md#supply-wisdom-conector) .

### OpenPages Regulatory Compliance Management

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-regulatory-compliance-management)

IBM OpenPages® Regulatory Compliance Management (RCM) da soporte a las organizaciones para desglosar las normativas en un catálogo de requisitos, evaluar su impacto en la empresa y crear tareas accionables.

Como solución, permite a las empresas:

- Mantener un repositorio de regulaciones y requisitos que deben cumplir
- Identificar y crear un catálogo de requisitos que satisfacen las regulaciones
- Correlacionar requisitos reguladores con un marco de trabajo de control interno
- Crear agrupaciones de requisitos en Temas de conformidad
- Realizar evaluaciones de requisitos normativos bajo Planes de conformidad
- Ingerir, apuntar y responder a eventos reguladores suministrados por proveedores de datos de terceros
- Registrar, organizar y responder a las interacciones reguladoras, incluyendo las consultas y exploraciones reguladoras

#### Ascent Conector

IBM OpenPages Regulatory Compliance Management incluye un conector para Ascent Reg Tech.

El conector Ascent permite la ingestión directa de canales de información normativos desde Ascent Reg Tech en RCM.

IBM OpenPages habilita la ingestión directa de nuevas reglas, cambios de reglas y obligaciones de Ascent Reg Tech en los objetos Mandato, Submandato y Requisito en OpenPages. Para los requisitos, están disponibles las versiones pasadas y futuras del texto regulador.

Para obtener información sobre cómo configurar el conector Ascent , consulte la publicación *IBM OpenPages Guía del administrador*.

#### Reg-Track Conector

IBM OpenPages Regulatory Compliance Management incluye un conector para Reg-Track.

El objeto de evento regulador de Reg-Track permite la ingesta directa de canales de información de eventos reguladores de Reg-Track en RCM y la generación automatizada de flujos de trabajo asignados a los usuarios basándose en los puntos de datos proporcionados. Esta automatización ayuda a asignar tareas a los usuarios de forma eficiente, lo que les permite responder de forma eficaz y prepararse para el cambio regulador.

- **Correlación de taxonomías**

  Los usuarios pueden asociar su propia taxonomía a la taxonomía Reg-Track que se utiliza para eventos reguladores.

  Los usuarios pueden rellenar campos en un registro de evento regulador que sean más coherentes con otros valores que se utilizan en IBM OpenPages. Los puntos de datos convertidos están disponibles para su uso de la misma forma que los puntos de datos existentes en el registro de evento regulador como, por ejemplo, para establecer condiciones dentro del motor de reglas o en un flujo de trabajo.

- **Reg-Track Motor de reglas**

  El motor de reglas de IBM OpenPages ayuda a los usuarios a manejar la afluencia diaria de sucesos normativos, a direccionarlos automáticamente a los usuarios adecuados de su organización e iniciar los flujos de trabajo necesarios.

  Los datos de los canales de información de Reg-Track se cargan en OpenPagesy, a continuación, pasan a través del motor de reglas. Un evento regulador puede activar varias reglas si se cumple más de una de las condiciones de una regla.

  Los usuarios pueden acceder al motor de reglas a través de un enlace en la página **Eventos reguladores Reg-Track**.

- **Flujos de trabajo de ejemplo**

  IBM OpenPages incluye flujos de trabajo de ejemplo para procesar eventos reguladores Reg-Track. Para obtener más información, consulte [Flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo).

- **Reglas listas para usar para el proceso de eventos reguladores de Reg-Track**

  IBM OpenPages incluye reglas de ejemplo para los eventos reguladores de Reg-Track entrantes. Estas reglas se pueden modificar para que coincidan con la metodología de una organización para procesar las alertas publicadas por agencias reguladoras.

Para obtener información sobre cómo configurar el conector Reg-Track , consulte la publicación *IBM OpenPages Guía del administrador*.

#### Thomson Reuters Conector

IBM OpenPages Regulatory Compliance Management incluye un conector para Thomson Reuters Regulatory Intelligence (TRRI).

El objeto Evento regulador TRRI permite la ingestión directa de canales de información de eventos reguladores de Thomson Reuters en RCM, y la generación automatizada de flujos de trabajo asignados a los usuarios en función de los puntos de datos proporcionados, así como de los documentos afectados por el cambio regulador. Esto ayuda a asignar de forma eficiente tareas a los usuarios para que respondan eficazmente a los cambios reguladores y se preparen para ello.

- **Correlación de taxonomías**

  Los usuarios pueden asociar su propia taxonomía a la taxonomía de Thomson Reuters que se utiliza para los eventos reguladores.

  Los usuarios pueden rellenar campos en un registro de evento regulador que sean más coherentes con otros valores que se utilizan en IBM OpenPages. Los puntos de datos convertidos están disponibles para su uso de la misma forma que los puntos de datos existentes en el registro de evento regulador como, por ejemplo, para establecer condiciones dentro del motor de reglas o en un flujo de trabajo.

- **Motor de reglas TRRI**

  El motor de reglas de IBM OpenPages ayuda a los usuarios a manejar la afluencia diaria de sucesos normativos, a direccionarlos automáticamente a los usuarios adecuados de su organización e iniciar los flujos de trabajo necesarios.

  Los datos del canal de información de Thomson Reuters Regulatory Intelligence (TRRI) se cargan en OpenPagesy, a continuación, pasan a través del motor de reglas. Un evento regulador puede activar varias reglas si se cumple más de una de las condiciones de una regla.

  Los usuarios pueden acceder al motor de reglas a través de un enlace en la página **Eventos reguladores TRRI**.

- **Flujos de trabajo de ejemplo**

  IBM OpenPages incluye flujos de trabajo de ejemplo para procesar eventos reguladores TRRI. Para obtener más información, consulte [Flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo).

- **Reglas predefinidas para el proceso de eventos reguladores TRRI**

  IBM OpenPages incluye reglas de ejemplo para los eventos reguladores TRRI entrantes. Estas reglas se pueden modificar para que coincidan con la metodología de una organización para procesar las alertas publicadas por agencias reguladoras.

- **Biblioteca regulatoria**

  IBM OpenPages habilita la ingestión directa de un canal de información de biblioteca reguladora desde Thomson Reuters en el objeto Submandato de RCM. En los casos en los que Thomson Reuters identifica las normativas afectadas por un evento regulador, el submandato afectado se asocia automáticamente tras la ingestión.

Para obtener información sobre cómo configurar el conector Thomson Reuters , consulte la publicación *IBM OpenPages Guía del administrador*.

#### Wolters Kluwer Conector

IBM OpenPages Regulatory Compliance Management incluye un conector para Wolters Kluwer (WK).

El objeto de evento regulador WK permite la ingestión directa de canales de información de eventos reguladores de Wolters Kluwer en RCM, y la generación automatizada de flujos de trabajo asignados a los usuarios en función de los puntos de datos proporcionados, así como los documentos afectados por el cambio regulador. Esto ayuda a asignar de forma eficiente tareas a los usuarios para que respondan eficazmente a los cambios reguladores y se preparen para ello.

- **Correlación de taxonomías**

  Los usuarios pueden asociar su propia taxonomía a la taxonomía Wolters Kluwer que se utiliza para eventos reguladores.

  Los usuarios pueden rellenar campos en un registro de evento regulador que sean más coherentes con otros valores que se utilizan en IBM OpenPages. Los puntos de datos convertidos están disponibles para su uso de la misma forma que los puntos de datos existentes en el registro de evento regulador como, por ejemplo, para establecer condiciones dentro del motor de reglas o en un flujo de trabajo.

- **Motor de reglas WK**

  El motor de reglas ayuda a los usuarios a manejar el flujo diario de eventos reguladores, direccionarlos automáticamente a los usuarios correctos en su organización e iniciar los flujos de trabajo necesarios.

  Los datos de Wolters Kluwer se cargan en OpenPagesy, a continuación, pasan a través del motor de reglas. Un evento regulador puede activar varias reglas si se cumple más de una de las condiciones de una regla.

  Los usuarios pueden acceder al motor de reglas a través de un enlace en la página **Eventos reguladores WK**.

- **Flujos de trabajo de ejemplo**

  IBM OpenPages incluye flujos de trabajo de ejemplo para procesar eventos reguladores de WK. Para obtener más información, consulte la publicación *IBM OpenPages Guía de soluciones*.

- **Reglas predefinidas para el proceso de eventos reguladores WK**

  IBM OpenPages incluye reglas de ejemplo para los eventos reguladores WK entrantes. Estas reglas se pueden modificar para que coincidan con la metodología de una organización para procesar las alertas publicadas por agencias reguladoras.

- **Biblioteca regulatoria**

  IBM OpenPages habilita la ingestión directa de un canal de información de biblioteca reguladora desde Wolters Kluwer en los objetos Mandato y Submandato de RCM. En los casos en los que Wolters Kluwer identifica las normativas afectadas por un evento regulador, los mandatos y submandatos afectados se asocian automáticamente tras la ingestión.

Para obtener información sobre cómo configurar el conector Wolters Kluwer , consulte la publicación *IBM OpenPages Guía del administrador*.

### Utilización de OpenPages Business Continuity Management

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-using-openpages-business-continuity-management)

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

#### Tutorial: descripción general de BCM

Para obtener una descripción general de BCM, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general de BCM.](https://video.ibm.com/embed/channel/25817967/video/op-overview-bus-continuity)

#### Tutorial: panel de control de BCM

Para obtener una descripción general del panel que está disponible para los usuarios asignados al perfil de Gestión de continuidad del negocio, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general del panel de control que está disponible para los usuarios que tienen el asignado el perfil de gestión de continuidad de negocio.](https://video.ibm.com/embed/channel/25817967/video/op-dashboard-business-continuity)

#### Tutorial: objeto del plan de continuidad de negocio

Para obtener una descripción general del objeto Plan de continuidad del negocio y cómo se utiliza en BCM, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general del objeto del plan de continuidad de negocio y de cómo se utiliza en BCM.](https://video.ibm.com/embed/channel/25817967/video/op-plan-object-bus-continuity)

#### Tutorial: objeto del análisis del impacto empresarial

Para obtener una descripción general del objeto Análisis de impacto empresarial y cómo se utiliza en BCM, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general del objeto del análisis del impacto empresarial y de cómo se utiliza en BCM.](https://video.ibm.com/embed/channel/25817967/video/op-business-impact-analysis)

#### Tutorial: objeto del plan de pruebas de la continuidad de negocio

Para obtener una descripción general del objeto Plan de prueba de continuidad del negocio y cómo se utiliza en BCM, vea el siguiente vídeo:

[Este vídeo proporciona una descripción general del objeto del plan de prueba de la continuidad de negocio y de cómo se utiliza en BCM.](https://video.ibm.com/embed/channel/25817967/video/op-test-plan-bus-continuity)

### OpenPages Data Privacy Management

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-data-privacy-management)

La solución IBM OpenPages® Data Privacy Management (DPM) es utilizada por una organización para ayudar a cumplir con las normativas de privacidad de datos.

Utilizando DPM, las organizaciones pueden tener una visibilidad clara de todos sus datos privados o sensibles y asegurarse de que los datos se manejan correctamente. DPM ayuda a los CPO, CDO, CCO y otros profesionales de la privacidad y el cumplimiento proporcionando visibilidad y permitiéndoles demostrar el cumplimiento.

DPM ayuda a las organizaciones a:

- Soportar el cumplimiento con la normativa de privacidad de datos
- Mantener un inventario de todos los datos privados en la organización de OpenPages utilizando una integración con Watson Knowledge Catalog
- Tener una visión holística de todos los datos privados en toda su organización
- Demostrar el cumplimiento de la privacidad mediante evaluaciones de cuestionarios e informes
- Iniciar automáticamente las evaluaciones de privacidad para los activos de datos recién cargados

#### Perfil maestro de DPM

DPM incluye el perfil maestro de DPM.

El perfil incluye:

- Panel de control
- Vistas dependientes y listas de selección dependientes
- Vistas de cuadrícula y vistas de tareas

#### Panel de control

DPM incluye el panel de control de maestro de DPM.

El panel de control de maestro de DPM proporciona a los profesionales de privacidad una visión general de alto nivel de los diferentes activos de datos de su organización, las tareas que se les han asignado y el estado de las evaluaciones de privacidad que se están realizando en la organización.

*Figura 1. Panel de control de DPM*

![Se visualiza un panel de control. El panel de control incluye un panel denominado Mis tareas con una barra codificada por colores que muestra el estado de las tareas. Otro panel muestra un gráfico circular colorido de Recursos por ubicación física y Recursos por jurisdicción.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/dpm_dashboard.png)

#### Flujos de trabajo de ejemplo

DPM incluye dos flujos de trabajo de ejemplo: Evaluación de impacto de privacidad y Evaluación de impacto de protección de datos. Para obtener más información, consulte [IBM OpenPages Data Privacy Management (DPM)](#flujos-de-trabajo-de-ibm-openpages-data-privacy-management-dpm).

### OpenPages Gestión de riesgos para ESG

`Guía de soluciones › IBM OpenPages GRC Solutions` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=solutions-openpages-risk-management-esg)

IBM OpenPages® Risk Management for ESG ayuda a las organizaciones a gobernar y gestionar sus programas ESG (medioambientales, sociales y de gobierno corporativo).

IBM OpenPages Risk Management for ESG da soporte a los siguientes casos de uso:

- Cuestionario para comprender las prioridades de ESG
- Capturar y gobernar objetivos estratégicos
- Enlazar objetivos a procesos, riesgos, controles y proveedores existentes
- Registrar un conjunto de indicadores para ESG
- Almacenar una biblioteca de requisitos normativos y divulgaciones de ESG
- Conformidad de pruebas con los requisitos de informes externos
- Exploración de horizonte de ESG
- Puntuaciones de ESG de superficie en proveedores (Supply Wisdom)

#### OpenPages Third Party Risk Management y el conector Supply Wisdom

Puede utilizar OpenPages Third Party Risk Management y Supply Wisdom junto con IBM OpenPages Risk Management for ESG.

El conector Supply Wisdom le permite importar detalles de proveedor, evaluaciones, alertas y ubicaciones de Supply Wisdom en objetos Proveedor en OpenPages. A continuación, puede ver las valoraciones de ESG de sus proveedores en OpenPages.

Para utilizar estas prestaciones, necesita los componentes siguientes:

- IBM OpenPages Gestión de riesgos para ESG
- OpenPages Gestión de riesgos de terceros
- El conector de Supply Wisdom

Para obtener información sobre cómo configurar el conector Supply Wisdom , consulte la publicación  [*IBM OpenPages Guía del administrador*](3.6-guia-del-administrador.md#supply-wisdom-conector).

## Novedades

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=sg-whats-new)

Hay nuevas características disponibles para este release de soluciones de IBM OpenPages® .

Para obtener información sobre todas las características nuevas de este release, consulte la publicación *IBM OpenPages New Features Guide*.

### Características nuevas de la versión 9.0.0.0

`Guía de soluciones › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wn-version-9000)

Las nuevas características de IBM OpenPages® versión 9.0.0.0 se describen en las secciones siguientes.

#### Mejoras en las soluciones

**Tabla 1. Mejoras en las soluciones**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Las mejoras en IBM OpenPages Policy Management incluyen:<br>• Un nuevo flujo de trabajo: Retirar flujo de trabajo de política<br>• Una nueva guía sobre la solución | [IBM OpenPages Flujos de trabajo de gestión de políticas (PCM)](#ibm-openpages-policy-management-pcm) [OpenPages Documento de solución de gestión de políticas](https://www.ibm.com/docs/es/SSFUEU_9.0.0/pdf/OpenPages_PCM_Solution_v9.pdf) |
| Las mejoras de IBM OpenPages Data Privacy Management incluyen:<br>• Nuevos perfiles: **encargado de datos de DPM** y **responsable de privacidad de DPM**<br>• Nuevos paneles de control y actualizaciones en el panel de control maestro<br>• Campos nuevos en el tipo de objeto Activo | [Perfiles](#perfiles) |
| Las mejoras en IBM OpenPages Financial Controls Management incluyen:<br>• Nuevos cálculos<br>• Informes nuevos<br>• Un panel de control actualizado | [Cálculos de ejemplo](#cálculos-de-ejemplo) [Informes de Gestión de controles financieros](#informes-de-gestión-de-controles-financieros) |
| Las mejoras en IBM OpenPages IT Governance incluyen:<br>Un nuevo tipo de objeto: amenaza<br>Nuevos cálculos:<br>• Activo-Calificación de vulnerabilidad<br>• Sistema-Calificación de vulnerabilidad<br>• Vulnerabilidad-Evaluación de amenazas<br>Nuevos flujos de trabajo:<br>• Revisión de vulnerabilidad<br>• Evaluación de amenazas<br>• Exención de TI<br>• Revisión de caducidad de exención de TI | [Tipos de objeto](#tipos-de-objeto) [Cálculos de ejemplo](#cálculos-de-ejemplo) [IBM OpenPages IT Governance (ITG)](#flujos-de-trabajo-de-ibm-openpages-it-governance-itg) |
| Las mejoras de IBM OpenPages Internal Audit Management incluyen:<br>• El nuevo tipo de objeto: **SummaryAuditPlan**<br>• El nuevo cálculo: Resumen de presupuesto y planes de plan de auditoría<br>• Un panel de control actualizado | [Descripciones de tipos de objeto](#descripciones-de-tipo-de-objeto) [Cálculos de ejemplo](#cálculos-de-ejemplo) |
| Las mejoras de IBM OpenPages Regulatory Compliance Management incluyen:<br>• El nuevo tipo de objeto: **RegulatoryEvent**<br>• El nuevo flujo de trabajo: **Activar cambio-Regulador** | [Descripciones de tipos de objeto](#descripciones-de-tipo-de-objeto) [IBM OpenPages Regulatory Compliance Management (RCM)](#ibm-openpages-regulatory-compliance-management-rcm) |
| Las mejoras en IBM OpenPages Model Risk Governance incluyen:<br>• Nuevos campos y grupos de campos en los tipos de objeto Caso de uso de modelo (Registro), Modelo y Despliegue de modelo (Uso)<br>• Nuevos flujos de trabajo: **Despliegue de modelo**,**Solicitud de caso de uso de modelo**y **Ciclo de vida de modelo**<br>• Vistas actualizadas<br>• Paneles de instrumentos actualizados | [Flujos de trabajo deIBM OpenPages Model Risk Governance (MRG)](#flujos-de-trabajo-de-ibm-openpages-model-risk-governance-mrg) |
| Los nuevos tipos de objeto **Subcontractor** y **VendorSubsidiary**, que pueden utilizarse con OpenPages Third Party Risk Management | [Descripciones de tipo de objeto](#descripciones-de-tipo-de-objeto) |
| Las etiquetas de los objetos siguientes han cambiado:<br>• `Register` -la etiqueta es ahora Caso de uso de modelo<br>• `RiskEntity` -la etiqueta es ahora Sistema<br>• `Resource` -la etiqueta es ahora Activo<br>• `ResourceLink` -la etiqueta es ahora Enlace de activo<br>Los nombres de objeto no han cambiado. | [Correlación de nombres de objeto](#correlación-de-nombres-de-objeto) |
| El superadministrador (`OpenPagesAdministrator`) tiene acceso a los perfiles maestros de soluciones de forma predeterminada. | [Perfiles](#perfiles) |
| Los siguientes tipos de objeto ya no se incluyen en instalaciones nuevas:<br>• Modelo de capital<br>• Resultado del modelo de capital | [Tipos de objetos existentes](#tipos-de-objetos-existentes) |
| Los siguientes campos computados son ahora campos URL :<br>• OPSS-RA:RCSA Completion Helper<br>• OPSS-RA:RCSA Process Alignment Helper |  |
| Cuando realiza una instalación nueva de soluciones, los usuarios de ejemplo para las soluciones ya no se crean. |  |

### Características nuevas de la versión 8.3.0.2

`Guía de soluciones › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wn-version-8302)

Las características nuevas de IBM OpenPages® versión 8.3.0.2 se describen en las secciones siguientes.

#### Mejoras en las soluciones

**Tabla 1. Mejoras en las soluciones**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Se ha introducido la nueva solución, IBM OpenPages Risk Management for ESG.<br>Se han añadido los elementos siguientes:<br>• Tipos de objeto: Disclosure Statement, Product, Strategic Objective<br>• Vistas<br>• Informes<br>• Paneles de control<br>• Perfiles<br>• Plantillas de funciones<br>• Cálculos<br>• Flujos de trabajo | [Descripciones de tipo de objeto](#descripciones-de-tipo-de-objeto)<br>[Gestión de riesgos para informes ESG](#informes-de-gestión-de-riesgos-para-esg)<br>[Perfiles](#perfiles)<br>[Lista de plantillas de funciones](#lista-de-plantillas-de-funciones)<br>[Cálculos de ejemplo](#cálculos-de-ejemplo)<br>[IBM OpenPages Gestión de riesgos para flujos de trabajo ESG](#flujos-de-trabajo-de-ibm-openpages-risk-management-for-esg) |
| El nuevo tipo de objeto, **Versión de requisito**, que se puede utilizar con IBM OpenPages Regulatory Compliance Management | [Descripciones de tipo de objeto](#descripciones-de-tipo-de-objeto) |

### Características nuevas de la versión 8.3.0.1

`Guía de soluciones › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wn-version-8301)

Las características nuevas de IBM OpenPages® versión 8.3.0.1 se describen en las secciones siguientes.

#### Mejoras en las soluciones

**Tabla 1. Mejoras en las soluciones**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Los cambios en IBM OpenPages Regulatory Compliance Management incluyen:<br>• El nuevo tipo de objeto: Ascent Información de soporte | [Tipos de objeto](#tipos-de-objeto) |
| Los cambios en OpenPages Third Party Risk Management incluyen:<br>• Integración con RiskRecon para importar proveedores, puntuaciones y valoraciones<br>• Integración con RapidRatings para importar proveedores, puntuaciones y valoraciones<br>• Los nuevos tipos de objeto: RiskRecon Ratings y RapidRatings Ratings<br>• Nuevos paneles de instrumentos que incluyen paneles para RapidRatings y RiskRecon<br>• Nuevos perfiles: VRM RiskRecon Master y OpenPages RapidRatings  Master<br>• Nuevas plantillas de funciones: TPRM RapidRatings -Todos los permisos y TPRM RapidRatings -Todos los datos-Administración limitada | [OpenPages Gestión de riesgos de terceros](#openpages-gestión-de-riesgos-de-terceros) [Tipos de objeto](#tipos-de-objeto) [Perfiles](#perfiles) [Plantillas de roles](#plantillas-de-funciones) |

### Nuevas características en la versión 8.3.0

`Guía de soluciones › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wn-version-8300)

Las nuevas características de IBM OpenPages® versión 8.3.0 se describen en las secciones siguientes.

#### Mejoras en las soluciones

**Tabla 1. Mejoras en las soluciones**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Los cambios en IBM OpenPages Regulatory Compliance Management incluyen:<br>• Los nuevos tipos de objeto: Evaluación de temas de conformidad, Evaluación del plan de conformidad, Obligación, Evaluación de la obligación y Valor de evaluación de la obligación<br>• Nuevos cálculos<br>• Nuevos flujos de trabajo<br>• Soporte para una nueva asociación de tipo de objeto: los tipos de objeto de política y procedimiento ahora pueden tener un objeto de evaluación de requisitos como padre.<br>• Soporte para la integración con RiskLens, incluyendo un nuevo perfil y un nuevo trabajo en el Programador | [Tipos de objeto](#tipos-de-objeto) [Cálculos de GRC](#cálculos-de-grc) [IBM OpenPages Regulatory Compliance Management (RCM)](#ibm-openpages-regulatory-compliance-management-rcm) [Perfiles](#perfiles) |
| Los cambios en IBM OpenPages Model Risk Governance incluyen:<br>• Los nuevos tipos de objeto: Versión de modelo, Obligación<br>• Cambios en las etiquetas de objeto: la tarjeta de puntuación de modelo es ahora la tarjeta de puntuación de riesgo de modelo, el registro es ahora la entrada de modelo y el uso es ahora el despliegue del modelo<br>• El nuevo cálculo, Actualización del valor de la métrica, sustituye al flujo de trabajo de Información del último valor de la métrica de actualización de OpenScale<br>• El nuevo cálculo, Tarjeta de puntuación de riesgo, sustituye al desencadenante de la tarjeta de puntuación de riesgo de modelo<br>• Dos cálculos adicionales: Siguiente fecha de recopilación de métricas y Valor de métrica - Actualización de la métrica padre<br>• Nuevos flujos de trabajo<br>• Las etiquetas de los campos, grupos de campos y filtros utilizan ahora el nuevo nombre de OpenScale,, que es IBM Watson® OpenScale | [Tipos de objeto](#tipos-de-objeto) [Cálculos de GRC](#cálculos-de-grc) [IBM OpenPages Model Risk Governance (MRG)](#flujos-de-trabajo-de-ibm-openpages-model-risk-governance-mrg) |
| Los cambios en IBM OpenPages Business Continuity Management incluyen:<br>• Los nuevos tipos de objeto: Servicio empresarial y Evaluación de servicios empresariales<br>• Tipos de objeto adicionales que ahora están disponibles para la solución: KPI, Valor de KPI, KRI, Valor de KRI, Análisis de escenario, Resultado de escenario<br>• Soporte para nuevas asociaciones de tipo de objeto<br>• Nuevos cálculos<br>• Nuevos flujos de trabajo<br>• Panel de control nuevo<br>• Integración con Supply Wisdom para proporcionar alertas en el objeto Suceso de continuidad de negocio y datos de riesgo dentro del objeto Ubicación<br>• Un nuevo perfil, BCM Supply Wisdom Master | [Tipos de objeto](#tipos-de-objeto) [Cálculos de ejemplo](#cálculos-de-ejemplo) [IBM OpenPages Flujos de trabajo de Business Continuity Management (BCM)](#flujos-de-trabajo-de-ibm-openpages-business-continuity-management-bcm) [Perfiles](#perfiles) |
| Los cambios en IBM OpenPages Gestión de riesgos de terceros incluyen:<br>• El nuevo tipo de objeto, Supply Wisdom Alerta padre<br>• Nuevos flujos de trabajo<br>• Un nuevo perfil, VRM Supply Wisdom Master | [Tipos de objeto](#tipos-de-objeto) [IBM OpenPages Flujos de trabajo de gestión de riesgos de terceros (TPRM)](#flujos-de-trabajo-de-ibm-openpages-third-party-risk-management-tprm) [Perfiles](#perfiles) |
| Los cambios en IBM OpenPages Policy Management incluyen:<br>• El nuevo tipo de objeto: Obligación<br>• El nuevo flujo de trabajo Revisión y aprobación de políticas<br>• El nuevo cálculo de comentario de revisión de política<br>• El nuevo panel de control del propietario de PCM<br>• Los valores predeterminados de algunos valores en `Solutions/PCM` se han actualizado para dar soporte al nuevo flujo de trabajo Revisión y aprobación de políticas | [Tipos de objeto](#tipos-de-objeto) [IBM OpenPages Policy Management (PCM)](#ibm-openpages-policy-management-pcm) [Cálculos de ejemplo](#cálculos-de-ejemplo) |
| Los cambios en IBM OpenPages IT Governance incluyen:<br>• El nuevo tipo de objeto: Obligación<br>• Integración con RiskLens<br>• El nuevo perfil ITG RiskLens Master | [Tipos de objeto](#tipos-de-objeto) [Perfiles](#perfiles) |
| Los cambios en IBM OpenPages Data Privacy Management incluyen:<br>• Nuevo panel de control<br>• Nuevos flujos de trabajo<br>• Las nuevas plantillas de rol | [IBM OpenPages Data Privacy Management (DPM)](#flujos-de-trabajo-de-ibm-openpages-data-privacy-management-dpm) [Lista de plantillas de funciones](#lista-de-plantillas-de-funciones) |
| Los cambios en IBM OpenPages Operational Risk Management incluyen:<br>• Nuevo panel de control<br>• Flujos de trabajo, cálculos, vistas y modificaciones de campos nuevos y actualizados para ayudar a los usuarios a utilizar la solución ORM de forma inmediata<br>• Sustitución del programa de utilidad de desencadenante KRI y KPI con el uso de cálculos, flujos de trabajo y el planificador. | [Flujo de trabajo de GRC](#grc-workflow) [Cálculos de GRC](#cálculos-de-grc) |
| El nombre de la carpeta en IBM® Cognos® Analytics donde se almacenan los informes de solución ha cambiado. Los informes y las páginas de informe se encuentran en **Contenido de equipo** > **OpenPages Informes de soluciones**.<br>Si ha actualizado o migrado, los informes existentes siguen estando disponibles en **Team Content** > **OpenPages Solutions Reports V6**. |  |
| Los informes de solución se han actualizado:<br>• Los informes ahora utilizan los nuevos modelos de infraestructura de la modalidad de consulta dinámica (DQM).<br>• Los informes ahora utilizan una hoja de estilo nueva para alinearse más estrechamente con la interfaz de usuario de OpenPages .<br>• Los informes utilizan JavaScript actualizado para enlaces CrossTrack . | [Informes](#informes)Consulte también la publicación *IBM OpenPages Report Author's Guide* |
| Ahora se dispone de nuevos informes en instalaciones nuevas:<br>• Pruebas de rendimiento y resultados<br>• Detalles de prueba<br>• Panel de control de eventos de pérdida consolidados<br>• Detalles del panel de control de eventos de pérdida - Entidad<br>• Panel de control de eventos de pérdida - Categoría | [Informes de prueba](#informes-de-prueba) [Informes de eventos de pérdida](#informes-de-eventos-de-pérdida) |
| Los siguientes tipos de objeto ya no se incluyen en instalaciones nuevas:<br>• Objetivo (SOXMilestone)<br>• Elemento de acción de objetivo (ProjectActionItem)<br>• Cuestionario (cuestionario)<br>• Sección (QSection)<br>• Pregunta (Quest) | [Tipos de objetos existentes](#tipos-de-objetos-existentes) |
| En instalaciones nuevas, los campos siguientes ya no son campos calculados:<br>• `Audit: OPSS-Aud: Close Audit` -Convertir en un campo de enlace<br>• `Audit: OPSS-Aud: Plans` -Convertir en un campo de enlace<br>• `Audit: OPSS-AudEnt:Weighted Risk Score` -Convertido en un campo de texto que muestra el resultado de un cálculo<br>• `Control Plan: OPSS-RiskEnt: Baselines` -Convertir en un campo de enlace<br>• `Resource: OPSS-Res: Resource Links` -Convertir en un campo de enlace<br>• `Plan: OPSS-Plan:Actual Hours` -Convertido en un campo de texto que muestra el resultado de un cálculo<br>• `Plan: OPSS-Plan:Actual TE` -Convertido en un campo de texto que muestra el resultado de un cálculo<br>• `Audit: OPSS-Aud:Actual Hours` -Convertido en un campo de texto que muestra el resultado de un cálculo<br>• `Audit: OPSS-Aud:Actual TE` -Convertido en un campo de texto que muestra el resultado de un cálculo | [Campos calculados](#campos-calculados) [Cálculos de GRC](#cálculos-de-grc) |
| El ayudante de finalización de escenario ya no se incluye en instalaciones nuevas. |  |
| Para los ayudantes del informe de creación de certificación, `/OpenPages/Solutions/PCM/Attestation/Email Sender Name` se ha sustituido por `/Applications/Common/Email/Mail From Address` y `/OpenPages/Solutions/PCM/Attestation/Email Sender Address` se ha sustituido por `/Applications/Common/Email/Mail From Name`. |  |
| Para los desencadenantes que utilizan el atributo `from.address`, si `from.address` está vacío o tiene un valor de `donotreply@openpages.com`, el valor se sustituye por el valor del valor de registro `/Applications/Common/Email/Mail From Address`. |  |
| Los desencadenantes de ciclo de vida de KRI y KPI y las notificaciones ya no se incluyen en instalaciones nuevas. Estos desencadenantes se han sustituido por flujos de trabajo y cálculos. | [flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo) |

### Nuevas características en la versión 8.2.0.3

`Guía de soluciones › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wn-version-8203)

Las nuevas características de IBM OpenPages® versión 8.2.0.3 se describen en las secciones siguientes.

#### Mejoras en las soluciones

**Tabla 1. Mejoras en las soluciones**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| La posibilidad de importar datos de Supply Wisdom a IBM OpenPages Third Party Risk Management. Los cambios incluyen:<br>• Se ha añadido un nuevo tipo de objeto, Supply Wisdom, como hijo del tipo de objeto Proveedor<br>• Se ha actualizado el tipo de objeto Ubicación para que sea un padre del tipo de objeto Proveedor<br>• Se han añadido nuevos campos al tipo de objeto Proveedor<br>• Se han añadido nuevos paneles de control<br>• Se han añadido nuevas vistas del sistema para el tipo de objeto Proveedor<br>• Se ha añadido un nuevo trabajo al Planificador<br>• Se ha añadido un nuevo cálculo<br>• Se ha añadido un nuevo permiso de aplicación<br>• Se han actualizado los perfiles VRM Master y VRM Vendor Manager | [OpenPages Gestión de riesgos de terceros](#openpages-gestión-de-riesgos-de-terceros) |
| Los siguientes perfiles de IBM OpenPages Financial Controls Management ahora incluyen el tipo de objeto Elemento de acción:<br>• FCM Master V2<br>• Certificación FCM V2 | [OpenPages Financial Controls Management](#openpages-financial-controls-management) |

### Nuevas características en la versión 8.2.0.2

`Guía de soluciones › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wn-version-8202)

Las características nuevas de IBM OpenPages® versión 8.2.0.2 se describen en las secciones siguientes.

#### Mejoras en las soluciones

**Tabla 1. Mejoras en las soluciones**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Se ha introducido la nueva solución, IBM OpenPages Data Privacy Management.<br>Se ha añadido el siguiente perfil:<br>• Perfil maestro de DPM<br>Se añade el flujo de trabajo siguiente:<br>• Evaluación de privacidad de datos<br>Se ha añadido el panel siguiente:<br>• Panel de control maestro de DPM | [OpenPages Data Privacy Gestión](#openpages-data-privacy-management)<br>[Perfiles](#perfiles)<br>[flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo) |
| Los cambios en IBM OpenPages Financial Controls Management incluyen nuevos:<br>• Perfiles de usuario<br>• Plantilla de funciones<br>• Grupo de campos<br>• Filtros<br>• Paneles de control<br>• Flujos de trabajo de ejemplo<br>• Cálculos de ejemplo<br>• Informes | [OpenPages Financial Controls Management](#openpages-financial-controls-management)<br>[Lista de plantillas de funciones](#lista-de-plantillas-de-funciones)<br>[flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo)<br>[Cálculos de ejemplo](#cálculos-de-ejemplo)<br>[Informes de gestión de controles financieros](#informes-de-gestión-de-controles-financieros) |

### Nuevas características en la versión 8.2.0.1

`Guía de soluciones › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wn-version-8201)

Las nuevas características de IBM OpenPages® versión 8.2.0.1 se describen en las secciones siguientes.

#### Mejoras en las soluciones

**Tabla 1. Mejoras en las soluciones**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Los cambios en IBM OpenPages Regulatory Compliance Management incluyen:<br>• Ingesta de eventos reguladores de los canales de información de Reg-Track<br>• Tipos de objeto añadidos, Reg-Track Evento regulador y Reg-Track Serie de eventos reguladores, para Reg-Track<br>• Se han añadido flujos de trabajo de ejemplo para Reg-Track<br>• Se han añadido reglas listas para usar para Reg-Track<br>• Notificaciones añadidas para Reg-Track | [OpenPages Regulatory Compliance Management](#openpages-regulatory-compliance-management), [Descripciones de tipo de objeto](#descripciones-de-tipo-de-objeto)y [Subcomponentes](#subcomponentes) |
| La posibilidad de importar datos de SecurityScorecard a IBM OpenPages Third Party Risk Management. Los cambios incluyen:<br>• Se han añadido nuevos campos al tipo de objeto Proveedor<br>• Se ha añadido un nuevo panel de control, Proveedor de TPRM con SecurityScorecard<br>• Se ha añadido una nueva vista de cuadrícula y una nueva vista de tareas<br>• Se ha añadido un nuevo trabajo al Planificador<br>• Se ha añadido un nuevo permiso de aplicación<br>• Se han actualizado los perfiles VRM Master y VRM Vendor Manager | [OpenPages Gestión de riesgos de terceros](#openpages-gestión-de-riesgos-de-terceros) |
| Se han actualizado los informes JSP para IBM OpenPages Operational Risk Management . |  |
| Se ha actualizado la JSP de informe de política de publicación para IBM OpenPages Gestión de políticas . |  |

### Características nuevas de la versión 8.2.0

`Guía de soluciones › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=wn-version-8200)

Las nuevas características de IBM OpenPages® versión 8.2.0 se describen en las secciones siguientes.

#### Mejoras en las soluciones

**Tabla 1. Mejoras en las soluciones**

| Para obtener información sobre... | Consulte el tema... |
| --- | --- |
| Los cálculos de ejemplo se incluyen con la nueva característica GRC Calculations . | [Cálculos de ejemplo](#cálculos-de-ejemplo) |
| Se ha introducido la nueva solución, IBM OpenPages Business Continuity Management.<br>Se han añadido los siguientes tipos de objetos:<br>• BCBusinessImpactAnalysis<br>• BCEvent<br>• BCPlan<br>• BCTest<br>• BCTestResult<br>• Ubicación<br>• Equipo<br>Se han añadido los siguientes perfiles:<br>• Perfil de OpenPages BCM Master<br>• BCM End User<br>Se han añadido los paneles de instrumentos siguientes a la IU centrada en tareas:<br>• Panel de control OpenPages BCM Master<br>• Panel de control Usuario final de BCM OpenPages<br>Se han añadido las siguientes plantillas de funciones:<br>• Assignee<br>• BC End User<br>• BC Manager<br>• BC Owner<br>• BCP Approver<br>• BCP Author<br>• BCP Focal<br>• BCP Reviewer<br>Se han añadido los siguientes flujos de trabajo:<br>• Flujo de trabajo 1: Proceso de revisión y aprobación del plan de continuidad de negocio<br>• Flujo de trabajo 2: Análisis del impacto empresarial para determinar procesos críticos<br>• Flujo de trabajo 3: Elaboración de informes de resultados de pruebas BC<br>Se ha añadido un informe de Cognos® en el objeto Planes de continuidad de negocio. El enlace al mismo se denomina `Print BC Plan Details`. El enlace genera un informe de Cognos con los detalles del objeto Plan de continuidad de negocio en formato PDF. | [Utilización de OpenPages Business Continuity Management](#utilización-de-openpages-business-continuity-management)<br>[Descripciones de tipo de objeto](#descripciones-de-tipo-de-objeto)<br>[Perfiles](#perfiles)<br>[Lista de plantillas de funciones](#lista-de-plantillas-de-funciones)<br>[flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo) |
| IBM OpenPages Model Risk Governance (MRG) incluye una integración lista para usar con IBM Watson® OpenScale. | [OpenPages Model Risk Governance](#openpages-model-risk-governance)<br>[flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo) |
| Se han realizado las mejoras siguientes en IBM OpenPages Gestión de políticas:<br>Se ha añadido el siguiente perfil:<br>• PCM End User<br>Se han añadido los paneles de instrumentos siguientes a la IU centrada en tareas:<br>• Panel de control de OpenPages PCM Master<br>• Panel de control de OpenPages Usuario final de PCM<br>Se ha añadido el flujo de trabajo Revisión de política.<br>RegTask tiene los siguientes padres nuevos: Interacción reguladora, Componente RI y Subcomponente RI. | [OpenPages Policy Management](#openpages-policy-management)<br>[Perfiles](#perfiles)<br>[flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo) |
| Los cambios en IBM OpenPages Regulatory Compliance Management incluyen:<br>• Ingestión de obligaciones de canales de información Ascent Reg Tech<br>• Un nuevo objeto Comentario de revisión de conformidad, que tiene los padres siguientes: Interacción con la autoridad reguladora, Componente RI, Subcomponente RI, RegTask y RegChange<br>• Categoría de RI tiene una nueva etiqueta: Componente RI<br>• Solicitud de RI tiene una etiqueta nueva: Subcomponente RI<br>• RegTask tiene los padres nuevos siguientes: Interacción con la autoridad reguladora, Componente RI y Subcomponente RI.<br>• Interacción con la autoridad reguladora, Componente RI y subcomponente RI tiene cada uno los nuevos padres siguientes: Mandato, Submandato, Requisito, Política, Procedimiento y Control | [Descripciones de tipos de objeto](#descripciones-de-tipo-de-objeto) y [Subcomponentes](#subcomponentes) |
| IBM OpenPages Vendor Risk Management se ha renombrado como IBM OpenPages Third Party Risk Management. | [OpenPages Gestión de riesgos de terceros](#openpages-gestión-de-riesgos-de-terceros) |
| Los asistentes de entrada de hoja de registro horario ahora están disponibles en un panel de informes en el panel de control en la IU centrada en tareas. La información de hoja de registro horario se puede ver con el nuevo elemento de menú, **Gestión de auditoría** > **Hoja de registro horario**. | [Asistentes de hoja de registro horario](#asistentes-de-hoja-de-registro-horario) |
| IBM OpenPages Internal Audit Management incluye un nuevo panel de control maestro. |  |
| Se han añadido flujos de trabajo de ejemplo para:<br>• Incidencias<br>• Evaluaciones de cuestionario | [flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo) |
| Los cálculos de ejemplo se incluyen con la nueva característica GRC Calculations . | [Cálculos de ejemplo](#cálculos-de-ejemplo) |
| Varios activadores ya no están habilitados en las instalaciones nuevas. | [Activadores heredados](#activadores-heredados) |
| Ya no se da soporte a las visualizaciones que representaron procesos de negocio en un formato gráfico. | [Visualizaciones de procesos empresariales (existentes)](#visualizaciones-de-procesos-empresariales-existentes) |

## Tipos de objeto

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=sg-object-types)

Las soluciones de IBM OpenPages® constan de varios tipos de objeto.

El documento *OpenPages Detalles de modelo de objeto* proporciona información sobre las relaciones entre tipos de objeto para cada solución.

### Correlación de nombres de objeto

`Guía de soluciones › Tipos de objeto` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=types-object-name-mapping)

Se correlacionan las etiquetas de tipo de objeto predeterminadas con nombres de objeto.

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

### Descripciones de tipo de objeto

`Guía de soluciones › Tipos de objeto` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=types-object-type-descriptions)

Las soluciones de IBM OpenPages® constan de varios tipos de objeto.

- **Cuenta**

  Las cuentas corresponden a una o más líneas de detalle de un informe financiero. Cada cuenta está afectada por Procesos recurrentes. Estos procesos pueden introducir riesgos que deben documentarse durante el proyecto de documentación de controles financieros. Una cuenta se identifica como cuenta significativa en base a factores como el tamaño, la complejidad de los procesos que operan en la cuenta o si la cuenta está asociada con una nueva línea de producto dentro de la empresa. Los riesgos que podrían materializarse y que producen un efecto material sobre la cuenta se identifican mediante la consideración de los procesos que operan en la cuenta.

- **Ascent Información de soporte**

  El objeto Información de soporte de Ascent almacena información de soporte que se importa desde Ascent. La información de soporte es un texto normativo que no tiene un nivel de requisito legal, sino que proporciona orientación adicional, detalles, etc. para ayudar a las entidades a comprender los requisitos y el impacto de la normativa. El tipo de objeto Ascent Información de soporte tiene un padre, Requisito.

- **Declaración**

  El objeto Declaración se utiliza para enlazar objetos de control a objetos de cuenta (o subcuenta). Una práctica común es almacenar el tipo de declaración que está cubriendo el Control como, por ejemplo, un campo de datos en el objeto Declaración.

- **Atestación**

  El objeto Certificación, parte de la capacidad de reconocimiento de políticas, se utiliza para capturar una afirmación de empleado que ha leído y comprendido una política. Un padre principal de la Atestación es el registro de empleados y el padre secundario es la campaña asociada.

- **Activo**

  COBIT sugiere que hay cuatro tipos de activos de TI, mientras que los profesionales también suelen incluir más tipos. El objeto Activo se subescribe utilizando campos dependientes para representar cualquiera de estos tipos de activos de TI. Los activos se crean normalmente como una agrupación asociada a la entidad empresarial de TI propietaria o responsable, a continuación, se asocian a los elementos operativos relevantes (líneas base, procesos, etc.) en el entorno operativo de TI, y se asocian potencialmente también a entidades empresariales relevantes para la empresa. Aunque los activos pueden representar activos de TI individuales (por ejemplo, un servidor Microsoft Windows determinado), con más frecuencia representan un grupo de activos (por ejemplo, una agrupación de servidores de aplicaciones Windows que se utilizan para una aplicación determinada).

- **Enlace de activo**

  COBIT sugiere que los activos de TI tienen relaciones complicadas. Indican que los activos de tipo Personas, Proceso, Infraestructura e Información pueden ser principales y cada uno puede ser un elemento secundario del otro. Además, los activos del mismo tipo a menudo deben estar relacionados entre sí. Se puede utilizar un enlace de activo para enlazar activos de una forma de muchos a muchos, pero la práctica (soportada por el asistente Crear enlaces de recursos) es enlazar exactamente dos activos. Si se cambian los nombres o atributos de cualquiera de los activos padre, el nombre y los atributos del enlace de activo no estarán sincronizados con sus activos padre.

- **Auditoría**

  Una auditoría representa cada ejecución de una auditoría en una entidad auditable. Por ejemplo, si se audita una entidad auditable cada dos años, se debe crear una instancia de auditoría hijo independiente para cada periodo de dos años, como 2022 y 2024. Una organización puede auditar varios procesos. Por ejemplo, puede auditar una entidad, un requisito regulador específico o una seguridad física de centro de datos.

  El objeto Auditoría se configura como un tipo de objeto autocontenido y se crea una carpeta automáticamente para cada instancia Auditoría. Esta configuración le permite copiar auditorías de plantilla y componentes de auditoría desde una biblioteca a una jerarquía de auditoría sin conflictos de denominación de objetos.

  La planificación y programación de recursos de Auditoría se realiza a nivel de auditoría.

  Se puede realizar seguimiento a un proceso de auditoría de alto nivel supervisando los valores Estado y Fecha en la auditoría. Se puede hacer seguimiento de los hitos de auditoría claves añadiendo campos que representan fechas de finalización para cada uno de los hitos claves a los que se va a realizar seguimiento.

  Utilice el objeto Auditoría para gestionar el proceso de auditoría en su empresa. La Auditoría identifica un punto de retención para capturar información como ámbito, objetivos, información de temporización, revisión, ejecución y funciones de aprobación. Puede realizar seguimiento a un subconjunto de auditorías que está emprendiendo en un horizonte de planificación determinado o a todas las auditorías en el universo de la auditoría.

- **Comentario de revisión de auditoría**

  El tipo de objeto Comentario de revisión de auditoría se utiliza para proporcionar comentarios durante el proceso de revisión de una auditoría y sus componentes. Está asociado como hijo a la instancia de Auditoría, Sección, Informe o Conclusión para la que se está proporcionando feedback.

- **Sección de auditoría**

  Las Secciones de auditoría se pueden utilizar para representar las fases de la auditoría, los programas de trabajo dentro de la auditoría u otros componentes de la auditoría en el nivel de granularidad deseado.

  Las organizaciones pueden tener varios componentes estándar para cada auditoría. Las auditorías de plantilla que incluyen secciones para cada componente estándar se pueden crear en una biblioteca. Las fechas de inicio y finalización planificadas y reales para estas secciones se utilizan para informar del progreso en hitos clave de las auditorías.

  Se puede hacer seguimiento del progreso de auditoría detallada incluyendo una sección de auditoría para cada hito. También, algunas organizaciones pueden añadir campos a la auditoría que representan fechas de finalización para cada uno de los hitos claves a los que desea hacer seguimiento.

  Aunque las secciones de auditoría se pueden utilizar para planificar y programar recursos de auditoría, la mayoría de organizaciones encuentran que este método es demasiado detallado.

- **Entidad auditable**

  Un objeto Entidad auditable es un hijo de una Entidad de negocios y un Plan de auditoría de resumen. Se establece una jerarquía de entidad de negocios de auditoría y se crean todas las Entidades auditables como hijo del objeto Entidad de negocios de auditoría interna. Las entidades auditables alineadas con elementos de la jerarquía organizativa de la entidad de negocios también están asociadas a las entidades de negocios.

  Una Entidad auditable representa un único elemento de Universo de la auditoría; una colección de elementos de la empresa que se pueden auditar. La mayoría de las entidades auditables representan entidades de negocios o legales, pero también pueden representar procesos, proyectos de larga ejecución o iniciativas, programas de conformidad o servicios de TI compartidos.

  Las Entidades auditables se clasifican como riesgo anualmente para determinar la prioridad de realizar una auditoría cada año. Se calcula una Puntuación de riesgo calculada pero el alcance se puede alterar.

- **Auditor**

  La planificación y asignación de recursos requiere información clave sobre cada persona que puede realizar trabajo de auditoría. El objeto Auditor se utiliza para crear una agrupación de auditores que se pueden asignar a la auditorías.

  Cada usuario asignado al trabajo de auditoría se representa como una instancia Auditor. Los auditores están disponibles ahora para la asignación de recursos. El objeto Auditor incluye atributos que se pueden utilizar para evaluar y seleccionar auditores para los contratos de auditoría, como especialidades, idiomas y certificaciones. Los objetos Auditor están asociados al componente relevante de la jerarquía organizativa de la auditoría interna. Como recomendación, haya coincidir el nombre del objeto Auditor con el nombre de usuario.

- **Línea base**

  Un tipo de objeto Linea base representa una plantilla de requisitos de biblioteca. Es autónomo, lo que significa que las carpetas se crean para cada línea base. Las líneas base de la biblioteca representan elementos del entorno operativo de TI. Están enlazados a los requisitos para ese tipo de elemento. El objeto Línea base se copia de la biblioteca a la jerarquía empresarial, se realiza una asociación a un requisito en la biblioteca, y los tipos de objeto Riesgo, Control y Prueba se crean como objetos hijo. Los objetos Riesgo, Control y Prueba se llenan con datos del requisito cuando se utiliza el ayudante de copia de línea base.

  Por ejemplo, un objeto Línea base puede representar una colección de objetos Requisito para un centro de datos con Información personalmente identificable (PII) y una clasificación de datos confidenciales. Para cada uno de los objetos Requisito, establezca una práctica recomendad para definir qué controlar (objeto Riesgo) y cómo controlarlo (objeto Control). También puede establecer una práctica para verificar la eficacia del Control (objeto Prueba).

- **Suceso de continuidad de negocio**

  El objeto Suceso de continuidad de negocio se utiliza para identificar un incidente que afecte negativamente a la operación empresarial, por ejemplo, una pandemia, un huracán, un tornado o una infracción de ciberseguridad. El tipo de objeto Suceso de continuidad de negocio contiene información, como por ejemplo la ubicación y el tipo. Un objeto Suceso de continuidad de negocio se puede asociar con un objeto Plan de continuidad de negocio para proporcionar una forma fácil de relacionar incidencias específicas con los correspondientes planes.

- **Plan de continuidad de negocio**

  Un Plan de continuidad de negocio es una estrategia proactiva, que incluye políticas y procedimientos que describen la forma en que una organización y sus funciones críticas responderán durante e inmediatamente después de una interrupción o un desastre. El Plan de continuidad de negocio se ocupa de los recursos humanos, los procesos de negocio, los activos y los servicios de soporte externalizados. El objeto Plan de continuidad de negocio puede asociarse con otros objetos de continuidad de negocio principales tales como el Análisis de impacto empresarial, Planes de prueba de continuidad de negocio, Evaluaciones de riesgos, Ubicaciones y Equipos.

- **Plan de prueba de continuidad de negocio**

  La realización de pruebas en un plan de continuidad de las actividades es un proceso valioso que se utiliza para calibrar la eficacia del plan y ayudar a identificar los puntos débiles o las lagunas. Las pruebas pueden realizarse utilizando diversos enfoques, como la simulación teórica y la simulación completa, y pueden contribuir a la formación y al conocimiento de los participantes en el plan. El objeto Plan de prueba de continuidad de negocio se puede utilizar para documentar los detalles de la prueba y se puede asociar con el objeto Plan de continuidad de negocio padre y los objetos hijo tales como Problema y Resultado del Plan de prueba de continuidad de negocio.

- **Resultado de prueba de continuidad de negocio**

  Los objetos Resultado de prueba de continuidad de negocio son objetos hijo de un Plan de prueba de continuidad de negocio. Se utilizan para capturar los resultados del plan de pruebas de continuidad de negocio ejecutado. Un resultado de prueba de continuidad de negocio se puede asociar a un plan de prueba de continuidad de negocio relacionado y a cualquier problema que lo acompañe.

- **Entidad empresarial**

  Las entidades empresariales son representaciones abstractas de la estructura empresarial. Una entidad de negocio puede contener subentidades (como departamentos, unidades de negocio o ubicaciones geográficas). La estructura de la entidad que crea depende de las necesidades empresariales. Por ejemplo, puede crear una entidad padre para las oficinas centrales de la empresa y una subentidad para cada ubicación o departamento. Es posible que también desee representar una estructura de entidad legal y una estructura de entidad de negocios.

  Las entidades de negocios también se utilizan para organizar datos de biblioteca, como las bibliotecas de control o riesgo, o contenido regulador (por ejemplo, leyes, normativas y estándares).

  Cuando configure la jerarquía de entidades empresariales, trabaje con su asesor de IBM® OpenPages . La estructura de la entidad de negocios afecta al tipo y calidad de la información que se puede extraer de la aplicación.

  En IBM OpenPages Internal Audit Management , las entidades empresariales también modelan la estructura organizativa de auditoría interna, lo que facilita la creación de informes y la seguridad para el equipo de auditoría interna. La estructura organizativa de la auditoría interna es una entidad de nivel superior para minimizar la posibilidad de otorgar de manera accidental a un usuario empresarial acceso a información de la auditoría interna. Los elementos del universo de la auditoría interna que posee el equipo de auditoría interna están asociados a la entidad de negocios del equipo. Se puede crear otra estructura de entidad de negocios de nivel superior para organizar auditorías confidenciales, proporcionando una seguridad especial a esas auditorías. La entidad de negocios también se puede utilizar para organizar una biblioteca de plantillas de contenido de auditoría.

- **Análisis de impacto empresarial**

  Un análisis de impacto empresarial (BIA) se utiliza para evaluar la gravedad de los procesos predeterminados, sus dependencias y el efecto en el negocio en caso de una interrupción. Se utiliza para medir el impacto que sucesos como los desastres naturales, las pandemias y el terrorismo pueden tener en los procesos de negocio críticos, basándose en la gravedad de las pérdidas.

  El tipo de objeto Análisis del impacto empresarial se ha diseñado para ayudarle a priorizar el impacto crítico en la empresa clasificando categorías predeterminadas utilizando una puntuación numérica. Se pueden aprovechar las clasificaciones de impacto numérico para campos de datos clave como el Objetivo de tiempo de recuperación (RTO) y el Objetivo de punto de recuperación (RPO). También puede utilizar la característica de cálculo en OpenPages para convertir los datos de impacto en información medible como, por ejemplo, las puntuaciones de impacto, los niveles de impacto y las interrupciones máximas aceptables (MAO).

- **Servicio empresarial**

  Un servicio empresarial es un servicio proporcionado por la organización, como la retirada de efectivo de un cajero automático o la posibilidad de consultar un saldo en línea, que puede desglosarse en procesos de soporte. Los servicios empresariales pueden clasificarse además como servicios empresariales importantes, que son servicios prestados a usuarios finales externos en los que una interrupción causaría un daño intolerable a los consumidores o a los participantes en el mercado, a la integridad del mercado, a la protección de los asegurados, a la seguridad y a la solidez, o a la estabilidad financiera.

  Un objeto de servicio empresarial puede ser un hijo de un objeto de Entidad empresarial o Ubicación.

- **Evaluación de servicios empresariales**

  Los objetos de Evaluación de servicios empresariales son hijos de objetos de servicios empresariales y se utilizan para capturar valores que se proporcionan como parte de la evaluación del servicio empresarial con el fin de establecer tendencias. El servicio Evaluación de servicios empresariales se crea y se rellena como parte del último paso de un flujo de trabajo de evaluación de servicios empresariales.

- **Campaña**

  El objeto Campaña forma parte de la capacidad de reconocimiento de políticas y se utiliza para gestionar los aspectos de gestión de proyectos de una campaña de concienciación. También se utiliza para definir los requisitos y criterios que identifica qué empleados necesitan leer y autenticar cada política. Las campañas se crean generalmente en la jerarquía de políticas publicadas.

- **Reto**

  El objeto >Reto se puede utilizar para almacenar y demostrar la presencia de un Reto en cualquier parte del inventario del modelo. Surge un Reto y la respuesta se registra. El objeto Desafío es hijo de los objetos Modelo y Despliegue de modelo.

- **Solicitud de cambio**

  El objeto Solicitud de cambio es hijo de los objetos Modelo y Despliegue de modelo y permite la creación y el seguimiento de actividades de gobierno relacionadas con los cambios en los Modelos y sus despliegues. El objeto captura datos como Tipo de cambio, Descripción de cambio y Estado. Está soportado por un flujo de trabajo.

- **Comité**

  El objeto Comité es hijo de Entidad de negocios y permite a una organización representar comités y grupos de gobierno. Éstos pueden alinearse a continuación con los modelos y también puede ser el padre del objeto Empleado. Puede almacenar información como los Términos de referencia para un comité, la frecuencia de reuniones y el detalle del Moderador.

- **Plan de conformidad**

  Los objetos Planes de conformidad permiten la creación de un plan general para aplicar los requisitos normativos en un valor estructurado, o para estructurar un conjunto de tareas reguladoras. Por ejemplo, se puede crear un Plan de conformidad para hacer un seguimiento de las tareas reguladoras, o para llevar a cabo evaluaciones de conformidad en varios requisitos reguladores. Se pueden agrupar uno o varios Temas de conformidad en un Plan de conformidad general para la organización.

- **Evaluación del plan de conformidad**

  Los objetos Evaluación del plan de conformidad son hijos del objeto Plan de conformidad. Los objetos Evaluación del plan de conformidad se utilizan para capturar valores que se proporcionan como parte de la evaluación de conformidad que se captura en el plan de conformidad. Se crea un registro de evaluación del plan de conformidad y se rellena como último paso en los flujos de trabajo de evaluación de BE del plan de conformidad y evaluación de la biblioteca de planes de conformidad.

- **Comentario de revisión de conformidad**

  El tipo de objeto Comentario de revisión de conformidad permite a un usuario añadir y publicar comentarios en los objetos Cambio regulador, Tarea reguladora, Componente RI, Subcomponente de RI y Interacción reguladora. Un comentario de revisión de conformidad se puede dirigir a una persona o grupo de usuarios para su respuesta, y los archivos se pueden cargar en el objeto para mejorar la colaboración entre los usuarios de IBM OpenPages .

- **Tema de conformidad**

  Los Temas de conformidad permiten a los usuarios organizar requisitos normativos en temas a efectos de evaluación. Esto permite evaluar los requisitos de conformidad más allá del típico enfoque de entidad de negocios, agrupando los requisitos normativos en temas que afectan a toda la organización. Los temas de ejemplo pueden incluir privacidad de datos, gobierno, responsabilidad, etc. Esto permite a los usuarios evaluar el impacto de la normativa no sólo dentro de las entidades empresariales, sino a través de temas que afectan a múltiples áreas de la organización.

- **Evaluación de temas de conformidad**

  Los objetos Evaluación de temas de conformidad son hijos de objetos Tema de conformidad. Los objetos Evaluación de temas de conformidad se utilizan para capturar valores que se proporcionan como parte de la evaluación de conformidad que se captura en el tema de conformidad. Se crea un registro de evaluación de temas de conformidad y se rellena como el último paso en los flujos de trabajo Evaluación de BE de temas de conformidad y Evaluación de la biblioteca de temas de conformidad.

- **Contrato**

  Los objetos de contrato son objetos hijo de objetos Proveedor o Compromiso. Un Contrato representa un acuerdo legal o comercial entre una entidad de negocios y un Proveedor o un Compromiso. Un Contrato contiene información adicional de soporte, como, por ejemplo, el periodo de tiempo del contrato o información pecuniaria. Los Contratos son opcionales.

- **Control**

  Los controles son políticas y procedimientos que garantizan la ejecución de respuestas para mitigar el riesgo.

  Una vez identificados los riesgos que llevan consigo sus prácticas, establezca controles, como aprobaciones, autorizaciones y verificaciones. Estos controles eliminan, limitan o transfieren estos riesgos.

  Los controles proporcionan prevención o detección de riesgos. Los controles están asociados con pruebas que garantizan que un control el eficaz. Por ejemplo, el departamento de recursos humanos identifica un riesgo en el nuevo proceso de contratación. El proceso no cumple con las normas y directrices para la diversidad y discriminación. Defina los controles para mitigar este riesgo, como establecer políticas y procedimientos de contratación, y lleve a cabo una formación obligatoria para los gestores de contratación.

  En IBM OpenPages Internal Audit Management utilice Controles para crear un modelo detallado de los Controles que existen o que desea imponer en las actividades que se auditan. Si se comparten con Negocio, los controles se pueden clasificar por separado por Auditoría interna y por Negocio.

- **Evaluación de control**

  Los objetos de evaluación de control son similares a los objetos de evaluación de riesgo, excepto que se crean como hijos de controles. Almacenan datos de gestión de control. Cuando los ciclos de evaluación de control y periodos de informes no están alineados, utilice objetos Evaluación de control para capturar varios ciclos de evaluación de gestión dentro de un único periodo de creación de informes.

- **Objetivo de control**

  Un objetivo de control es un objeto de evaluación que define las categorías de riesgo para un proceso o subproceso.

  Los objetivos de control definen las categorías de conformidad COSO que intentan mitigar los controles. Los objetivos de control se pueden clasificar en categorías como Conformidad, Creación de informes financieros, Estrategia, Operaciones o Desconocido.

  Una vez se ha identificado un objetivo de control, se pueden definir los riesgos que pertenecen a ese objetivo de control. En la mayoría de los casos, cada objetivo de control tiene un riesgo asociado. Sin embargo, puede tener asociado más de un riesgo. Por ejemplo, una compañía de servicios financieros emplea vendedores que conocen los estándares éticos necesarios. El departamento de RRHH configura un objetivo de control denominado 'Personal'. Un riesgo asociado con el objetivo de control es: «“Los empleados hacen operaciones comerciales que entran en conflicto con los objetivos de la empresa en cuanto a la ética comercial y el comercio justo”».

  De forma predeterminada, un objetivo de control de OpenPages Internal Audit Management está inhabilitado. Este objeto no se utiliza a menudo, excepto para alinearlo con otras soluciones que pueden utilizarlo.

- **Centro de costes**

  Los objetos de Centro de costes se utilizan para agrupar eventos de pérdida bajo una entidad empresarial. En muchos casos, las firmas desean hacer seguimiento donde se producen los eventos de pérdida con el más mínimo detalle, como a nivel de centro de costes, pero no desean representar todas las capas organizativas como entidades de negocios.

- **Declaración de divulgación**

  Este tipo de objeto se utiliza principalmente para registrar comentarios basados en texto en relación con los requisitos de divulgación. Las declaraciones de divulgación son hijos de los requisitos.

- **Empleado**

  El objeto Empleado forma parte de la capacidad de reconocimiento de políticas. Se utiliza para capturar información sobre empleados individuales, como el nombre, el cargo, el correo electrónico, la región, el departamento, el estado, etc. La información del perfil del empleado se coteja después con los requisitos de atestación definidos en una campaña para determinar qué empleados necesitan testificar sobre cada política. Los datos de empleado provienen generalmente de la exportación del sistema de RRHH, cargado a través de Online FastMap, y residen en la entidad de negocios de empleado de referencia. Se recomienda que el campo Nombre de empleado coincida con el nombre de usuario del usuario.

- **Compromiso**

  Los objetos de compromiso son objetos hijo de objetos de proveedor. Un Compromiso representa un servicio único proporcionado por un proveedor. Se utiliza para diferenciar los diversos servicios y acuerdos que tiene con un proveedor. Los compromisos son opcionales. Pueden estar sujetos a evaluaciones de cuestionario, evaluaciones de riesgo u organización en niveles. Puede resumir y analizar los riesgos asociados a distintos Compromisos. Puede añadir una asociación padre con el proceso o el subproceso que admite un Compromiso.

- **Archivo**

  El tipo de objeto Archivo se utiliza para incluir una referencia a un archivo (como un documento, un diagrama de flujo o una hoja de cálculo) en el sistema IBM OpenPages y asociarlo a uno o varios objetos relevantes.

- **Conclusión**

  Los resultados se pueden utilizar para representar observaciones que se notifican a la empresa, al Comité de auditoría o a ambos. Además, las conclusiones se pueden utilizar para representar observaciones objetivas individuales, mientras que los problemas se utilizan para representar temas consolidados o problemas sistémicos de los que se informa a la empresa, al comité de auditoría o a ambos.

  Una conclusión representa algo que se ha descubierto en el curso de una auditoría que necesita una explicación y una investigación por parte del equipo directivo. Puede utilizar una conclusión para hacer seguimiento del progreso de la gestión a la hora de tratar el problema subyacente identificado. Se puede utilizar el objeto Problema en lugar de, o junto con el objeto Conclusión.

- **Pérdida FIRST**

  Los objetos de pérdida FIRST se pueden importar de la base de datos de pérdida externa FIRST, para utilizarlos con el análisis de escenarios, la evaluación comparativa y la generación de informes, y para exportar datos de pérdidas a herramientas analíticas o aplicaciones de asignación de capital. Los objetos Pérdida FIRST a menudo se organizan por categorías de pérdida, como líneas de producto o tipos de evento. Por ejemplo, utilice una entidad de negocios para crear una jerarquía para los datos de la pérdida FIRST. Denomine al objeto raíz «“FIRST-data”» y cree carpetas de categoría bajo la raíz. Enlace pérdidas externas a ese objeto.

- **Incidente**

  Un incidente es un suceso que tiene un efecto potencialmente adverso en la empresa. Cree un objeto Incidente para registrar información, como la persona responsable de la investigación del incidente y otros datos relacionados. El objeto Incidencia lo utiliza un flujo de trabajo para facilitar el análisis de incidencias. Las categorías que se aplican a los incidentes incluyen la Conformidad con la normativa, Conformidad legal, Seguridad de la información y TI. Las incidencias se almacenan bajo la entidad de negocios o activo donde se ha producido el suceso y se asocian de forma secundaria a un mandato o política afectados.

- **Problema, Elemento de acción**

  Aunque se generan problemas en áreas en las que los controles internos no se implementan correctamente, utilice el objeto Problema para documentar una preocupación asociada a cualquier tipo de objeto. Por ejemplo, una prueba se ha asociado con un control, pero la prueba ha fallado la última vez que se ha completado. Este problema potencial puede resaltarse capturándolo en un objeto Problema.

  Un problema se resuelve a través de Elementos de acción. Puede utilizar un elemento de acción o una serie de elementos de acción relacionados para formar un Plan de acción. Cada elemento de acción se asigna a un usuario para su resolución y hace seguimiento del progreso. Una vez que todos los elementos de acción para un problema se completan (cuando el responsable establece el valor en el 100%), cierre el problema.

  En OpenPages Internal Audit Management, se pueden utilizar Problemas y Elementos de acción en lugar de, o con, Resultados.

- **KPI, Valor de KPI**

  Los KPI (indicadores clave de rendimiento) son componentes del proceso de supervisión del riesgo y se utilizan para proporcionar indicadores adelantados o atrasados de posibles condiciones de riesgo. Cada instancia de KPI dentro de la organización puede tener límites de umbral y destino exclusivos. El tipo de objeto Valor de KPI registra el valor de un objeto de KPI en un punto específico. Cree un objeto de KPI y, a continuación, periódicamente (diariamente, semanalmente, mensualmente) cree un objeto Valor de KPI para poder detectar tendencias.

- **KRI, Valor de KRI**

  Los KRI (indicadores clave de riesgo) son componentes del proceso de supervisión del riesgo y se utilizan para proporcionar indicadores adelantados o atrasados de posibles condiciones de riesgo. Cada instancia de KRI dentro de la organización puede tener límites de umbral y destino exclusivos. Los valores KRI se utilizan para registrar el valor real de un indicador en un punto específico en el tiempo.

- **Vínculo**

  El tipo de objeto Enlace se utiliza para incluir una referencia a un URL en el sistema OpenPages y asociarlo a uno o varios objetos relevantes.

- **Ubicación**

  El tipo de objeto Ubicación se utiliza para capturar detalles de geografía y ubicación que son necesarios en el proceso de planificación de contingencia. La información de ubicación puede incluir, por ejemplo, el número de empleados que trabajan en una ubicación, los bienes (como el equipo de sistemas) y otros detalles de ubicación.

- **Evento de pérdida**

  Los sucesos de pérdida se utilizan para realizar un seguimiento de las pérdidas operativas que se producen en cualquier parte de una organización. Los Eventos de pérdida se almacenan generalmente bajo la Entidad de negocios donde se ha producido la pérdida. Los objetos Evento de pérdida se utilizan para hacer seguimiento, evaluar y gestionar los datos de pérdida internos relacionados. Puede añadir varios impactos y recuperaciones a cada evento de pérdida utilizando los objetos Impacto de pérdida y Recuperación de pérdida. Los objetos Evento de pérdida, Impacto de pérdida y Recuperación de pérdida también se pueden crear en IBM OpenPages Loss Event Entry.

- **Impacto de pérdida**

  Un impacto de pérdida es una consecuencia financiera y no financiera que resulta de un evento de pérdida. Los impactos de pérdida realizan un seguimiento de los impactos iniciados por un evento de pérdida, como la responsabilidad legal, pérdida o daños en los activos o una interrupción de la actividad del negocio. Puede haber varios impactos de pérdida asociados con cada evento de pérdida.

- **Recuperación de pérdidas**

  Los objetos de recuperación de pérdidas se utilizan para realizar un seguimiento de los procesos asociados con la recuperación de los daños que son consecuencia de eventos de pérdida.

- **Mandato**

  Los mandatos representan elementos externos con los que las organizaciones deben cumplir, como leyes, normativas y estándares. El contenido se puede extraer de proveedores de terceros como, por ejemplo, UCF, Ascent Reg Techo Wolters Kluwer. Los mandatos se representan en una estructura de entidades de negocios por biblioteca y no se replican para todo el sistema.

  Por ejemplo, una compañía de seguros tiene un objeto Mandato para HIPAA y otro objeto Mandato para GLBA. Puede asociar el mismo mandato a grupos diferentes dentro de la organización. Los mandatos de privacidad, por ejemplo, pueden aplicarse a los departamentos de nóminas, servicios de seguros, legal y al departamento de TI.

  El objeto Mandato también admite contenido para la conformidad con la normativa.

- **Métrica, Valor de métrica**

  El objeto Métrica registra la definición de una medida de rendimiento que la organización decide rastrear. Un usuario establece el Tipo de métrica, los Umbrales amarillo y rojo y otra información de la recopilación. Una métrica es hijo de objetos de modelo y de despliegue de modelo.

  El objeto Valor de métrica registra el resultado de la medida de rendimiento de la métrica. Está diseñado para permitir a la organización almacenar los resultados de medida de las series temporales.

- **Modelo**

  El objeto Modelo proporciona representación de los modelos dentro de una organización. A nivel teórico, un modelo como método cuantitativo, sistema o enfoque que se aplica a teorías, técnicas y asunciones estadísticas, económicas, financieras o matemáticas para procesar datos de entrada en estimaciones cuantitativas. Dentro del objeto Modelo, se puede representar información clave del modelo, incluyendo: descripción del modelo, propiedad del modelo, estado del modelo, fechas de ciclo de vida de desarrollo, tipo de modelo y categoría, y datos de evaluación de riesgos del modelo. Un objeto de modelo es hijo de una entidad empresarial y padre de objetos de despliegue de modelo.

- **Atestación de modelo**

  La atestación del modelo permite a una organización solicitar una validación normal o *atestación* de un modelo. El administrador de MRG crea periódicamente un conjunto de atestaciones de modelo en blanco, que se asignan a los respectivos propietarios de modelo. Cada propietario de modelo responde a un conjunto de preguntas acerca del modelo y envía su atestación de modelo.

- **Despliegue de modelos**

  El objeto de despliegue de modelo es hijo del Modelo. Se utiliza como elemento clave para registrar el despliegue de uno o más modelos.

- **[Modelo] Caso de uso**

  El objeto Caso de uso de modelo o Caso de uso es un hijo de Entity y un padre del objeto Modelo. El uso del objeto Caso de uso de modelo es opcional. Su finalidad principal es actuar como biblioteca de los modelos durante el desarrollo.

- **Entrada de modelo**

  Si una organización desea adoptar un enfoque más granular a la documentación del modelo, el objeto Entrada de modelo proporciona la capacidad de registrar las entradas. Los campos incluyen Propietario de entrada, Tipo, Estado y Descripción. Un objeto de Entrada de modelo también puede ser el hijo de un objeto de Salida de modelo, lo que permite crear cadenas de modelos a un nivel de detalle si el enfoque de enlace de modelo no es suficientemente granular.

- **Enlace de modelo**

  Si una organización desea adoptar un enfoque menos granular para la documentación del modelo, utilice el enlace de modelo, que es una asociación de tipo amplio que no proporciona detalles explícitos del canal de información de un modelo a otro. Actúa como hijo de varios modelos para permitir la generación de cadenas de modelos.

- **Salida del modelo**

  Si una organización quiere adoptar un enfoque más granular para la documentación del Modelo, el objeto Salida del Modelo proporciona la capacidad de registrar las Salidas del modelo. La finalidad prevista es registrar la descripción y visión general de la salida desde un punto de vista de gobierno.

- **Tarjeta de puntuación de riesgo modelo**

  Las evaluaciones de riesgo del modelo se realizan durante la fase de desarrollo y documentación de un modelo. También se realizan de forma periódica una vez que un modelo se encuentra en producción. El objeto Modelo de tarjeta de puntuación de riesgo se utiliza para realizar esta evaluación de riesgo. El usuario responde a una serie de preguntas sobre el modelo. Los desencadenantes de la tarjeta de puntuación de riesgo de modelo calculan una puntuación de riesgo y determinan el nivel de modelo.

- **Versión del modelo**

  El objeto Versión de modelo es hijo del objeto Modelo y padre del despliegue de modelo. El objeto Versión del modelo es opcional. Si se necesitan más detalles al crear varias versiones de un modelo, el objeto Versión de modelo se puede utilizar como un objeto intermediario.

- **Obligación**

  El tipo de objeto Obligación representa «“las cosas que hay que hacer”» normalizadas y armonizadas para cumplir con todos los objetos Mandato, Submandato y Requisito asociados de la obligación.

  Los objetos Obligación cumplen dos objetivos principales: traducen la jerga legal, a menudo difícil y farragosa, de los mandatos/submandatos/requisitos a un inglés sencillo, y utilizan los elementos comunes a varios mandatos/submandatos/requisitos. Por ejemplo, es posible que tenga muchos submandatos y requisitos en numerosos mandatos que requieren el uso de contraseñas fuertes. Un solo objeto Obligación puede documentar los detalles para contraseñas fuertes. Cumpliendo esta única obligación, la tecnología de la información puede satisfacer muchos mandatos, submandatos y requisitos.

  Normalmente, los objetos de obligación se representan en una estructura de entidad empresarial de biblioteca y no se replican en todo el sistema.

- **Evaluación de la obligación**

  Una vez que los usuarios han correlacionado los controles internos con las obligaciones, los usuarios pueden realizar una evaluación de lo bien que están operando en relación con la obligación identificada. Los usuarios pueden evaluar la efectividad operativa y la efectividad de diseño de los controles dentro del ámbito de un tema de conformidad.

- **Valor de evaluación de la obligación**

  Los valores de evaluación de la obligación se utilizan para registrar el valor real de una obligación en un momento determinado dentro del ámbito de una evaluación de obligación.

- **Pérdida ORIC**

  Los objetos Pérdida ORIC se puede importar de la base de datos de pérdida externa ORIC, para utilizarlos con el análisis de escenario, benchmarking y la generación de informes, y para exportar datos de la pérdida a herramientas analíticas o aplicaciones de asignación de capital.

- **Pérdida ORX**

  Los objetos de pérdida ORX se pueden importar de la base de datos de pérdida externa ORX, para utilizarlos con el análisis de escenarios, la evaluación comparativa y la generación de informes, y para exportar datos de pérdidas a herramientas analíticas o aplicaciones de asignación de capital. Puede importar datos de pérdida ORX externos a OpenPages Operational Risk Management para utilizarlos con el análisis de escenarios.

- **Plan, Hoja de registro horario**

  Un tipo de objeto Plan facilita la planificación y asignación de recursos de auditoría en cualquier nivel. Por ejemplo, puede crear un único objeto de planificación para una auditoría completa o puede crear un objeto de planificación por tarea para cada auditor implicado en la auditoría. Los objetos Plan se utilizan para determinar la disponibilidad, habilidades y experiencia necesarias del recurso deseado. Las vistas de auditoría de OpenPages , informes, etc., están alineadas con la planificación a nivel de auditoría. Los planes se pueden asociar a secciones de auditoría, en cuyo caso, estos componentes tendrán que modificarse.

  Los objetos Plan también gestionan el seguimiento horario - se hace seguimiento de todas las horas en Planes. Se utiliza un tipo de objeto de hoja de registro horario para registrar las horas y gastos semanales reales empleados en relación con el objeto de planificación de una auditoría. Puesto que los objetos Hoja de registro horario están asociados a los planes, es fácil hacer seguimiento de las desviaciones entre los gastos y horas reales y planeados.

  Normalmente, puede crear o modificar un objeto Plan utilizando el ayudante Añadir o modificar planes, al que los propietarios de auditoría pueden acceder desde un enlace en la vista de tareas Auditoría. También puede editar planes (pero no crearlos) accediendo al elemento de menú **Gestión de auditoría** > **Planes** .

  Siempre debe utilizar los ayudantes de la hoja de registro horario para entrar, modificar y aprobar datos de tiempo y gastos. La información de la hoja de registro horario se puede visualizar accediendo al elemento de menú **Gestión de auditoría** > **Hoja de registro horario** . También puede añadir los ayudantes de la hoja de registro horario a una pestaña Informes en el panel de control.

- **Política**

  Las políticas representan directrices internas que son adoptadas por el Consejo de Administración o el órgano de gobierno superior dentro de una organización. El texto de una política puede almacenarse en los campos estandarizados en el objeto o como un archivo adjunto al objeto. Normalmente, las políticas tienen un ciclo de vida definido que va de Borrador a Publicado a Caducado, así como un proceso de revisión y aprobación. Normalmente, las políticas Borrador residen en la Jerarquía empresarial organizativa, mientras que las políticas Publicado y Caducado residen en las entidades de biblioteca de referencia. Las políticas también se correlacionan con mandatos aplicables de la biblioteca con la que están relacionadas.

- **Comentario de revisión de política**

  Los Comentarios de revisión de política soportan y facilitan el proceso de revisión y aprobación de políticas y procedimientos por parte de los expertos en la materia y el personal de conformidad.

- **Preferencia, Grupo de preferencia**

  El objeto Preferencia es hijo de una entidad empresarial o grupo de preferencia e incluye valores variables que pueden generar informes, flujos de trabajo y campos calculados. Tiene valores de variable específicos de la entidad que permiten un comportamiento diferente para los mismos flujos de trabajo. Por ejemplo, defina valores de variable para determinar el comportamiento para flujos de trabajo de revisión y aprobación como, por ejemplo, los usuarios adecuados para cada nivel de revisión y aprobación, y los umbrales para determinar cuántos niveles de revisión y aprobación se necesitan.

  El Grupo de preferencia se utiliza para agrupar objetos Preferencia. Sin este objeto de agrupación, los objetos Preferencia deben asociarse por separado con cada entidad de negocios relevante. El grupo de preferencia ayuda a minimizar el mantenimiento asociado.

  En la configuración predeterminada de IBM OpenPages Internal Audit Management , estos objetos se utilizan para mantener ponderaciones para factores de riesgo utilizados en la Clasificación de riesgos de evaluación anual. Puesto que los pesos y factores pueden ser diferentes para cada tipo de auditoría, como financiera, operativa o estratégica, cree una instancia de Preferencia individual para cada tipo de auditoría. Como hijo de la entidad de negocios, este enfoque proporciona la capacidad de tener valores de variable específicos de la entidad.

  En la configuración predeterminada de IBM OpenPages Model Risk Governance , estos objetos se utilizan para identificar participantes en varios flujos de trabajo MRG y para configurar parámetros en la configuración de la tarjeta de puntuación de riesgo de modelo.

- **Procedimiento**

  Los procedimientos representan el qué, el dónde, el cuándo y el cómo se implementan las políticas en una organización. El texto de los procedimientos se almacenan normalmente en los campos en el objeto. Normalmente, los procedimientos se representan como hijos de una política y residen en la misma estructura de entidad que su política padre.

- **Proceso**

  Los procesos representan las principales actividades empresariales de extremo a extremo dentro de una entidad empresarial que están sujetas a riesgo. Los procesos residen en áreas como la creación de informes financieros, la conformidad y la seguridad de la información. Por ejemplo, los procesos del departamento de cuentas por cobrar, como el proceso desde el pedido hasta el cobro se pueden mejorar con controles para protegerse contra los riesgos de creación de informes financieros, por ejemplo, contra un comportamiento fraudulento o contra imprecisiones de la creación de informes financieros.

  En OpenPages Internal Audit Management, los procesos también se utilizan en las auditorías de ámbito. Las auditorías pueden copiar procesos creados por la entidad de negocios o crear sus propios procesos.

- **Evaluación de proceso**

  Los objetos Evaluación de proceso son hijos de los objetos Proceso y se utilizan para capturar valores de medición de procesos para fines de tendencia.

  Cuando los periodos de creación de informes no están alineado con los ciclos de evaluación, puede utilizar objetos Evaluación de proceso para capturar varios ciclos de evaluación dentro de un único periodo de creación de informes.

- **Producto**

  Este tipo de objeto es un hijo del tipo de objeto Objetivo estratégico y se utiliza para representar Productos.

- **Program**

  Los objetos Programa se utilizan con Plantillas de cuestionario para implementar las Evaluaciones de cuestionario. Cuando un administrador empresarial inicia un programa, se crean las evaluaciones de cuestionario. Un programa se asocia a activos subyacentes, las evaluaciones de cuestionario que ha creado y la Plantilla de cuestionario en la que se basa. El Programa proporciona entrada para el flujo de trabajo.

- **Proyecto**

  Un Proyecto se diseña para organizar tareas de normativas en un proyecto de conformidad general. Por ejemplo, puede haber cambios de normativa que se deben abordar en el marco de trabajo de conformidad; los usuarios pueden crear un proyecto para identificar y asignar tareas.

- **Evaluación de cuestionario**

  Los objetos Evaluación de cuestionario son un medio de recopilar información de usuarios empresariales en la organización. Las evaluaciones de cuestionario se crean cuando se inicia un programa. Las evaluaciones de cuestionario se asocian con activos subyacentes, el programa que lo ha lanzado y la Plantilla de cuestionario en la que se basa. Las evaluaciones de cuestionario son utilizadas por un flujo de trabajo para facilitar un proceso de revisión.

  Las evaluaciones de cuestionarios no están relacionadas con cuestionarios. La información que describen las evaluaciones de cuestionario, las plantillas de cuestionario y los programas no se aplican a los cuestionarios. Consulte [Tipos de objeto heredados](#tipos-de-objetos-existentes).

- **Plantilla de cuestionario, Plantilla de sección, Plantilla de subsección y Plantilla de preguntas**

  Los objetos Plantilla de cuestionario, Plantilla de sección, Plantilla de subsección y Plantilla de pregunta se utilizan junto con Programas para implementar las Evaluaciones de cuestionario. Los objetos Plantilla de cuestionario son objetos padre y organizan los objetos Plantilla de sección. Los objetos Plantilla de sección son hijos de objetos Plantilla de cuestionario y organizan los objetos Plantilla de subsección. Los objetos Plantilla de subsección son hijos de objetos Plantilla de sección y organizan los objetos Plantilla de preguntas. Los objetos Plantilla de preguntas contienen preguntas y opciones de respuesta.

- **RapidRatings Calificaciones**

  RapidRatings Los objetos de clasificación se utilizan con el conector RapidRatings en IBM OpenPages Gestión de riesgos de terceros. Los objetos RapidRatings Ratings almacenan evaluaciones financieras y son hijos de los objetos Vendor.

- **Reg-Track Evento normativo**

  El objeto de evento regulador Reg-Track habilita la ingestión directa de canales de información de eventos reguladores de Reg-Track en IBM OpenPages Regulatory Compliance Management.

- **Reg-Track Serie de eventos reguladores**

  El objeto Serie de eventos reguladores Reg-Track es una colección de eventos reguladores Reg-Track a los que se les ha asignado el mismo ID de serie Reg-Track dentro del canal de información de Reg-Track . La agrupación de eventos reguladores de Reg-Track dentro de la serie de eventos reguladores de Reg-Track permite realizar un seguimiento de los cambios desde la etapa propuesta hasta la etapa final en la evolución del cambio regulador.

- **Aplicabilidad de la normativa**

  El objeto Aplicabilidad de regulación reside en la jerarquía empresarial de la organización. Evalúa y hace seguimiento del impacto regulador de un mandato de la biblioteca en una entidad de negocios.

- **Autoridad reguladora**

  El objeto Regulador forma parte de la capacidad de gestión de interacción del regulador y proporciona la posibilidad de que las organizaciones creen un inventario único de todos los reguladores con los que interactúan. Las actividades reguladoras normalmente se crean en una entidad de negocios de biblioteca. El objeto es un hijo de la entidad de negocios y se puede asociar a mandatos e interacciones con la actividad reguladora.

- **Interacción con la autoridad reguladora**

  El objeto Interacción de regulador forma parte de la capacidad de gestión de interacción del regulador. El objeto Interacción con la autoridad reguladora permite gestionar las interacciones, las comunicaciones, los trabajos internos, las revisiones y las aprobaciones asociadas con las autoridades reguladoras externas, como las consultas, los envíos, los archivados, los exámenes y las reuniones. Para las interacciones complejas, como por ejemplo los exámenes, puede utilizar los objetos Componente RI y Subcomponente RI para partir la interacción en componentes más pequeños o para rastrear las consultas de seguimiento procedentes de la entidad reguladora. La Interacción con la autoridad reguladora se puede correlacionar a los siguientes objetos padre: Autoridad reguladora, Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones padre permiten a un usuario enlazar objetos que puedan estar dando problemas en la Interacción con la autoridad reguladora, e identificar a los usuarios que son relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Se podrían asignar tareas individuales relacionadas con la gestión y respuesta a la interacción con la autoridad reguladora a usuarios a través de objetos hijo de tareas reguladoras.

- **Cambio regulador**

  El objeto Cambio regulador forma parte de la capacidad de Gestión de cambios reguladores. Ofrece la capacidad de realizar un seguimiento de los cambios reguladores, evalúa el impacto de una modificación en la organización, comunica el cambio a nivel interno a las personas que correspondan y gestiona los procesos internos de respuesta al cambio.

  Los cambios normativos suelen residir en la entidad empresarial de la biblioteca y se pueden asociar directamente al evento regulador, mandato, submandato o requisito que ha cambiado. El triaje del cambio regulador se realiza a través de la asignación de objetos de Tarea reguladora hijos.

  Para las organizaciones que reciben un canal de información de Reg-Track, Thomson Reuterso Wolters Kluwer de eventos reguladores, los usuarios pueden crear varios objetos de cambio regulador e iniciar flujos de trabajo a partir de la ingestión de un evento regulador basado en reglas que se crean dentro del **Motor de reglas**.

- **Evento normativo**

  El objeto Evento regulador se utiliza con IBM OpenPages Regulatory Compliance Management (RCM). El tipo de objeto Evento regulador permite la ingestión directa de canales de información de eventos reguladores utilizando la API REST o IBM AppConnect en RCM. Junto con el **Motor de reglas**, el tipo de objeto Evento regulador da soporte a la generación automatizada de flujos de trabajo que asignan sucesos reguladores entrantes a los usuarios en función de los puntos de datos proporcionados. También se da soporte a los documentos que se ven afectados por el cambio normativo. Estas prestaciones ayudan a asignar tareas de forma eficiente a los usuarios para responder a los cambios normativos y prepararse para ellos de forma eficiente. Un evento regulador puede ser un hijo de una entidad empresarial, control, mandato, submandato, requisito, política o procedimiento. Los usuarios pueden crear objetos de cambio regulador como hijos de eventos reguladores.

  > **Nota:** Si está utilizando un proveedor de datos como, por ejemplo, Reg-Track, Thomson Reuterso Wolters Kluwer, consulte el tipo de objeto de evento regulador para dicho canal de información, como por ejemplo el tipo de objeto de evento regulador Reg-Track .

- **Iniciativa reguladora**

  El objeto Iniciativa reguladora es hijo del objeto Entidad de negocios y captura información descriptiva sobre normativas que afectan a la organización. Las iniciativas reguladoras representan una agrupación más amplia de normativas. Por ejemplo, Antiblanqueo de dinero puede ser una iniciativa reguladoras que incluya varias normativas de blanqueo de dinero diferentes con las que las organizaciones deben cumplir.

- **Tarea reguladora**

  El objeto Tarea reguladora se utiliza para asignar tareas a usuarios de OpenPages cuando la tarea está relacionada con uno de los siguientes objetos padre: Proyecto, Política, Cambio regulador, Interacción con la autoridad reguladora, Componente RI o Subcomponente RI. Una Tarea reguladora también se puede asociar a una entidad de negocios.

- **Requisito**

  El objeto Requisito detalla los requisitos específicos, que se encuentran en el objeto Mandato o Submandato relacionado, que la organización debe cumplir para estar en conformidad.

  El contenido se puede extraer de UCF, Ascent Reg Techu otros proveedores de terceros. Por lo general, los mandatos se representan en una estructura de entidades de negocios por biblioteca y no se replican para todo el sistema.

  Para Ascent Reg Tech, se crea un requisito para cada tarea entrante.

- **Evaluación de requisitos**

  Después de que los usuarios correlacionan controles internos para los requisitos derivados de normativas, los usuarios pueden realizar una evaluación de lo bien que están funcionando en relación al requisito identificado. Los usuarios pueden evaluar la eficacia operativa y la eficacia del diseño de controles dentro del ámbito de un Tema de conformidad.

- **Valor de evaluación de requisito**

  Los Valores de evaluación de requisitos se utilizan para registrar el valor real de un requisito en un punto específico en el tiempo dentro del ámbito de una Evaluación de requisito.

- **Versión de requisito**

  El objeto Versión de requisito detalla las versiones anteriores y futuras del texto regulador de requisito. El objeto Versión de requisito es un hijo de Requisito. El objeto Versión de requisito realiza un seguimiento de los cambios normativos a lo largo del tiempo. Las versiones anteriores pueden ayudarle a revisar un requisito en un momento determinado. Las versiones futuras permiten al usuario prepararse para el futuro cambio de texto normativo y comenzar su análisis de impacto.

- **Revisar**

  El objeto Revisión se utiliza para registrar la planificación y los resultados de cualquier actividad de Revisión del modelo. Es hijo de los objetos de despliegue de modelo y modelo. El objeto está pensado para capturar los resultados de revisiones realizadas preimplementación, postimplementación y realizadas por una segunda o tercera línea de defensa.

- **Componente RI**

  El objeto Componente RI (anteriormente denominado Categoría RI) forma parte de la capacidad de Gestión de interacción de reguladores y se utiliza como el nivel medio del modelo de objeto de tres niveles (Interacción de regulador, Componente RI y Subcomponente RI). El objeto se utiliza para dividir una Interacción con la autoridad reguladora compleja en registros más pequeños, más manejables o para enlazar una consulta de seguimiento de una autoridad reguladora con el objeto padre de la Interacción con la autoridad reguladora. Además, el Componente RI se puede correlacionar con los siguientes objetos padre: Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones permiten a un usuario enlazar objetos que puedan estar dando problemas e identificar a los usuarios relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Las tareas individuales relacionadas con la gestión y respuesta a la interacción reguladora se pueden asignar a usuarios a través de un objeto hijo de tarea reguladora.

- **Subcomponente RI**

  El objeto Subcomponente RI (anteriormente denominado Solicitud RI) forma parte de la capacidad de gestión de interacción del regulador y se utiliza como último nivel del modelo de objeto de tres niveles (Interacción de regulador, Componente RI y Subcomponente RI). El objeto se utiliza para dividir una Interacción con la autoridad reguladora y el componente RI en registros más pequeños y manejables. Además, el Subcomponente RI se puede correlacionar con los siguientes objetos padre: Mandato, Submandato, Requisito, Política, Procedimiento y Control. Estas asociaciones permiten a un usuario enlazar objetos que puedan estar dando problemas e identificar a los usuarios relevantes para esos objetos y a los que quizás se tenga que consultar para responder a la autoridad reguladora. Las tareas individuales relacionadas con la gestión y respuesta a la interacción reguladora se pueden asignar a usuarios a través de objetos hijo de tareas reguladoras.

- **Riesgo**

  Los riesgos son pasivos potenciales. Los riesgos pueden estar asociados a procesos empresariales, entidades de negocios o en conformidad con un mandato. Cada riesgo tiene controles que proporcionan protección contra el riesgo. Los controles ayudan a reducir las consecuencias que son resultado del riesgo. Utilice el objeto Riesgo para categorizar riesgos; capturar la frecuencia, la puntuación y la gravedad de los datos de riesgo observados y calculados; y para ver informes para identificar los elementos de riesgo principales. Por ejemplo, la cuenta En metálico tiene un proceso denominado Nómina. Un riesgo potencial que se puede producir en la nómina es un desembolso de nómina duplicado o la creación de desembolsos de nómina ficticios. La identificación de riesgos en curso es un componente principal del desarrollo de un proyecto de documentación de controles financieros.

  En OpenPages Internal Audit Management, un riesgo que se comparte entre una auditoría interna y la empresa se puede clasificar por separado.

- **Evaluación de riesgo**

  Las evaluaciones de riesgo le proporcionan la capacidad de evaluar y notificar responsabilidades potenciales para un conjunto de entidades o procesos empresariales. Un objeto Evaluación de riesgo contiene los nombres del asesor y revisor, los marcos de tiempo de la evaluación y el estado de la evaluación. Utilice una evaluación de riesgo para gestionar el riesgo de un proceso de autoevaluación. Asocie los objetos Riesgo a una evaluación de riesgo para crear un enlace entre la entidad de negocios y los riesgos. Por ejemplo, cree una evaluación de riesgo para evaluar riesgos operativos, como un fraude o robo externo, un fraude internos, daños físicos a la propiedad o interrupción de negocio.

- **Evaluación de evaluación de riesgos**

  Los objetos de evaluación de evaluación de riesgos son similares a los objetos de evaluación de riesgos, excepto que se instancian como hijos de las evaluaciones de riesgos. Almacenan los datos de evaluación de riesgo.

- **Evaluación de riesgos**

  Los objetos de evaluación de riesgo son hijos de objetos de riesgo y se utilizan para capturar valores de medición del riesgo con fines de tendencia. Cuando los periodos de creación de informes no están alineado con los ciclos de evaluación de riesgo, puede utilizar objetos Evaluación de riesgo para capturar varios ciclos de evaluación dentro de un único periodo de creación de informes..

- **RiskRecon Calificaciones**

  RiskRecon Los objetos de clasificación se utilizan con el conector RiskRecon en IBM OpenPages Gestión de riesgos de terceros. Los objetos de RiskRecon Ratings almacenan valoraciones y puntuaciones de proveedor en los niveles de categoría y subcategoría. Los objetos RiskRecon Ratings se crean bajo `/BusinessEntity/Library/VRM/VRMLibrary/RiskRecon` y son hijos de objetos Vendor.

- **Análisis de escenario**

  El Análisis de escenarios (SA) es una técnica de evaluación que se utiliza para identificar y medir la aparición potencial de sucesos de riesgo operativo o para evaluar la resiliencia operativa. A diferencia de las evaluaciones de riesgos operacionales tradicionales, es un análisis «“hipotético”».

  El análisis de escenarios está diseñado para derivar evaluaciones razonadas de la probabilidad e impacto de pérdidas operativas plausibles o para analizar la resiliencia operativa. Puede utilizar el proceso Análisis de escenario en OpenPages para construir Análisis de escenario y recopilar datos cualitativos y cuantitativos de soporte. Con un Análisis de escenario, puede registrar un intervalo de estimaciones de frecuencia y gravedad en «“grupos”» junto con la información de soporte de la evaluación.

  En IBM OpenPages Operational Risk Management (ORM), el análisis de escenarios se utiliza a menudo para identificar y medir sucesos con baja frecuencia pero con pérdidas de gravedad alta, por ejemplo, desastres naturales, terrorismo o comerciantes deshonestos. Junto con sus elementos cualitativos, el análisis de escenarios se utiliza a menudo como una aportación directa a la estimación de capital de riesgo operativo de una empresa. El Análisis de escenario a menudo se crea para entidades de negocios y reciben la asignación de una categoría de riesgo. También puede asociar datos ORM de soporte, por ejemplo, evaluaciones de riesgo, eventos de pérdidas relevantes, pérdidas ORIC, pérdidas ORX y riesgos.

  En IBM OpenPages Business Continuity Management (BCM), el análisis de escenario se utiliza para identificar y medir escenarios graves, pero plausibles, que podrían interrumpir los servicios empresariales importantes para probar la probabilidad de que el servicio empresarial pueda recuperarse dentro de las tolerancias de impacto establecidas. Los objetos de análisis de escenarios se crean como objetos hijo de objetos de servicio empresarial. Los resultados de un análisis de escenario se almacenan en un objeto de resultado de escenario.

- **Resultado del caso de ejemplo**

  Los objetos Resultado de escenario son hijos de los objetos Análisis de escenario y se utilizan para capturar los resultados de los talleres del análisis de escenario para fines de tendencia y comparación.

  En IBM OpenPages Business Continuity Management, se crea un objeto Resultados de escenario como parte de la última acción del flujo de trabajo Análisis de escenario.

- **Firma**

  La firma generalmente indica que el objeto reúne las condiciones necesarias para su aprobación. No tiene facultades de ejecución y no impide que el elemento se modifique después de la aprobación.

  Las firmas (con o sin bloqueos asociados) se aplican a un objeto desde la vista de tareas de un objeto.

  Si se han configurado bloqueos de firma en el sistema, cuando valida un objeto, el objeto y sus objetos hijo asociados se bloquean y no se pueden modificar hasta que revoque la firma o hasta que un administrador desbloquee el objeto.

- **Objetivo estratégico**

  Este tipo de objeto se utiliza para representar los objetivos ESG de una organización. El tipo de objeto incluye campos para el dominio ESG y los objetivos. El tipo de objeto Objetivo estratégico tiene un padre: Entidad de negocios.

- **Subcuenta**

  Una subcuenta representa un elemento de línea más pequeño y más objetivo que forma parte de una cuenta principal más grande (o de otra subcuenta). Cada objeto Subcuenta puede estar asociado a objetos Subcuenta o Cuenta padre.

- **Submandato**

  Los submandatos representan subpartidas externas (o internas) con los que la organización debe cumplir. El contenido se puede extraer de proveedores de terceros, incluyendo UCF, Ascent Reg Tech, Thomson Reutersy Wolters Kluwer. Generalmente, los Submandatos están representados en una estructura de Entidad de negocios de biblioteca y no se replican en todo el sistema. El submandato es recursivo, pero el contenido de Deloitte, UCF, Ascent Reg Tech, Thomson Reutersy Wolters Kluwer utiliza exactamente un nivel de submandato. Los submandatos también soportan contenido para conformidad con la normativa. Los submandatos se pueden utilizar para representar párrafos derivados de informes reguladores.

- **Subproceso**

  Un subproceso es un componente de un proceso. Se utiliza para dividir procesos en unidades más pequeñas con fines de evaluación. Por ejemplo, un proceso financiero desde el pedido hasta el cobro puede componerse de varios subprocesos como acreedores, compras y contabilidad general. Cualquiera de estos subprocesos podría exponer a la entidad de negocios a un riesgo, lo cual es posible mejorar utilizando controles.

  En OpenPages Internal Audit Management, este objeto no se utiliza en el ámbito de auditoría, pero se puede utilizar en la documentación de detalles de proceso.

- **Subcontratista**

  Los objetos Subcontratista son objetos hijo de objetos Proveedor. Un subcontratista representa una parte de un servicio proporcionado por un proveedor. Subcontratista es un tipo de objeto opcional. Los subcontratistas pueden estar sujetos a evaluaciones de cuestionarios, evaluaciones de riesgos o niveles. Puede resumir y analizar el riesgo asociado a distintos subcontratistas. Puede añadir una asociación padre al proceso o subproceso al que da soporte un subcontratista.

- **Plan de auditoría de resumen**

  El tipo de objeto Plan de auditoría de resumen permite a una oficina del programa planificar auditorías de entidades auditables durante un periodo de tiempo predeterminado (anual, medio año, o trimestre) por ámbito, perfil de riesgo, horas de previsión de auditorías, etc.

  El objeto Plan de auditoría de resumen es un hijo de Entidad de negocios. Los hijos del plan de auditoría de resumen incluyen: Auditoría y Entidad auditable.

- **Supply Wisdom**

  El objeto Supply Wisdom almacena evaluaciones de riesgo de proveedores que se importan de Supply Wisdom. El tipo de objeto Supply Wisdom tiene un padre, Vendor.

- **Alerta padre de Supply Wisdom**

  El objeto Alerta padre Supply Wisdom almacena datos de alerta que se importan de Supply Wisdom. La importación crea objetos de suceso de continuidad de negocio para los datos de alerta entrantes y asocia las alertas a los objetos de proveedor y ubicación correspondientes en OpenPages.

- **Sistema**

  El sistema es un tipo de objeto autocontenido, lo que significa que se crean carpetas para cada objeto del sistema. El objeto Sistema agrupa varias líneas base para representar elementos en el entorno operativo que se pueden evaluar para el riesgo. Actúa como contenedor para una colección de objetos de activos y los riesgos, controles y requisitos relacionados que realizan conjuntamente una función o forman parte de un servicio de TI. Por ejemplo, un objeto del sistema puede representar los servidores, sistemas operativos, aplicaciones, bases de datos, personal de soporte y recursos que proporcionan el correo electrónico corporativo.

- **Equipo**

  El tipo de objeto Equipo permite a la organización clasificar los grupos que dan soporte al proceso de continuidad de negocio o que se ven afectados en la planificación de la continuidad de negocio. El objeto Equipo se puede utilizar para identificar miembros clave del equipo, la línea de negocio y la ubicación que se puede asociar con el objeto Empleado o el objeto Plan de continuidad de negocio.

- **Plan de pruebas**

  Un plan de prueba es un contenedor para pruebas y puede asociarse con objetos de control padre y objetos hijo, como por ejemplo resultados de prueba y problemas. Determine la efectividad operativa de un control realizando pruebas detalladas y documentando los resultados. Los planes de prueba describen los mecanismos que determinan si un control es efectivo. Por ejemplo, un control de prueba sería: «“Recursos Humanos autoriza cambios en el estado del empleado”». Una prueba de este control sería: «“Verificar el sello de autorización de RRHH en los registros de empleados nuevos”». La prueba verifica que el nuevo control está implementado y en uso.

  La configuración predeterminada de OpenPages Internal Audit Management utiliza el objeto Informe en lugar del Plan de prueba y el Resultado de prueba. El objeto Auditoría necesita acceder a estos elementos porque se utilizan a menudo para documentar pruebas empresariales.

- **Resultado de prueba**

  Un resultado de la prueba es la información que se obtiene tras la ejecución de un plan de prueba.

  La configuración predeterminada de OpenPages Internal Audit Management utiliza el objeto Informe en lugar del Plan de prueba y el Resultado de prueba. El objeto Auditoría necesita acceder a estos elementos porque se utilizan a menudo para documentar pruebas empresariales.

- **Amenaza**

  Una amenaza es cualquier circunstancia o suceso con el potencial de afectar negativamente a las operaciones y activos de la organización. Se puede crear una biblioteca de amenazas bajo el objeto Entidad de negocios y asociarse o copiarse en un objeto Proceso, Sistema o Activo padre. Las amenazas también se pueden asociar a vulnerabilidades para identificar y evaluar la probabilidad y el impacto de la explotación de una vulnerabilidad por parte de una amenaza, lo que podría dar lugar a un riesgo para un activo, un sistema o un proceso.

- **Evento regulador TRRI**

  El objeto de evento regulador TRRI permite la ingestión directa de canales de información de eventos reguladores de Thomson Reuters en IBM OpenPages Regulatory Compliance Management.

- **Serie de eventos reguladores TRRI**

  El objeto Serie de eventos reguladores de TRRI es una recopilación de eventos reguladores de TRRI a los que se ha asignado el mismo ID de serie dentro del canal de información TRRI. La agrupación de eventos reguladores TRRI dentro de la serie de eventos reguladores TRRI permite realizar el seguimiento de los cambios desde la etapa propuesta hasta la última en la evolución de los cambios reguladores.

- **Proveedor**

  Un proveedor es una empresa externa a la que una empresa adquiere bienes o servicios. Los proveedores pueden tener cuatro tipos de objetos hijo: Vendedor Filial, SubContractors, Encargos y Contratos. Los proveedores pueden estar sujetos a evaluaciones de cuestionario, evaluaciones de riesgo u organización en niveles. Puede resumir y analizar los riesgos asociados a los distintos Proveedores. Puede añadir una asociación padre al proceso o al subproceso al que da soporte el Proveedor.

  Si utiliza Supply Wisdom, el objeto Proveedor también tiene el objeto Supply Wisdom como objeto hijo.

  Las calificaciones de proveedor se pueden importar de SecurityScorecard o Supply Wisdom utilizando conectores.

- **Filial del proveedor**

  Una filial de proveedor representa una filial de un proveedor de la que una empresa adquiere bienes o servicios. Subsidiaria de proveedor es un tipo de objeto opcional. Subsidiaria de proveedor es un hijo de Proveedor. La Filial Proveedor puede tener tres tipos de objetos hijo: SubContractor, Encargos y Contratos. La filial del proveedor puede estar sujeta a evaluaciones de cuestionarios, evaluaciones de riesgos o niveles. Puede resumir y analizar el riesgo asociado con diferentes filiales de proveedor. Puede añadir una asociación padre al proceso o subproceso al que da soporte una filial de proveedor.

- **Vulnerabilidad**

  Las vulnerabilidades le permiten rastrear y evaluar los puntos débiles de la seguridad. Asigne puntuaciones a Vulnerabilidades mediante Vulnerabilities Common Vulnerability Scoring System (CVSS v2). El objeto padre de una vulnerabilidad puede ser un sistema, una incidencia, un activo o un riesgo. Por norma, las vulnerabilidades se importan de una solución de seguridad de TI.

- **Renuncia**

  Las exenciones le ofrecen la posibilidad de documentar, procesar y gestionar el ciclo de vida de las excepciones a políticas, requisitos o controles. Las exenciones se pueden asociar a entidades empresariales, políticas, procedimientos, requisitos, riesgos, controles, líneas base y activos.

- **Evento regulador WK**

  El objeto Evento regulador WK habilita la ingestión directa de canales de información de eventos reguladores de Wolters Kluwer en IBM OpenPages Regulatory Compliance Management.

- **Documento de trabajo**

  Un documento de trabajo es cualquier artefacto o entregable que desee rastrear en el ámbito de una auditoría. Puede representar una carta de compromiso, una matriz de prueba, las notas de una entrevista o cualquier otro cosa que resulte apropiada para la auditoría en cuestión. El propio informe puede ser atributos que se almacenan en el objeto de informe, o puede ser un archivo de Microsoft Word, Microsoft Excel u otro tipo de archivo que se adjunta a un objeto de informe. Cuando el informe se utiliza como evidencia de prueba, documenta la planificación de la prueba y los resultados de la prueba.

  Cree un objeto Documento de trabajo desde la vista de tareas de una sección de auditoría. Los objetos de informe de trabajo también se pueden copiar desde una biblioteca, donde representan plantillas de diferentes tipos de informes de trabajo generadas por un departamento de auditorías internas.

### Subcomponentes

`Guía de soluciones › Tipos de objeto` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=types-subcomponents)

Las soluciones de IBM OpenPages® constan de varios subcomponentes.

Un subcomponente es un grupo de tipos de objeto que admite una función lógica en la solución.

En la tabla siguiente se listan los subcomponentes que se incluyen de forma predeterminada.

**Tabla 1. Subcomponentes en OpenPages**

| Subcomponente | Etiqueta de tipo de objeto | ESG | DPM | BCM | TPRM | RCM | MRG | FCM | ORM | PCM | ITG | IAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Organización | Entidad empresarial | X | X | X | X | X | X | X | X | X | X | X |
| Preferencia | Grupo de preferencias, Preferencia | X |  | X | X | X | X | X | X | X | X | X |
| Evaluación de riesgo | Evaluación de riesgos, Análisis de evaluación de riesgos | X |  | X | X | X | X | X | X | X | X | X |
| Proceso | Proceso, Evaluación de proceso, Subproceso, Objetivo de control | X |  | X | X | X | X | X | X | X | X | X |
| Riesgo | Riesgo, Evaluación de riesgos | X |  | X | X | X | X | X | X | X | X | X |
| Control | Control, Evaluación de control | X | X | X | X | X | X | X | X | X | X | X |
| Prueba | Plan de pruebas, Resultado de las pruebas |  |  |  | X | X | X | X | X | X | X | X |
| Problema | Problema, Elemento de acción | X | X | X | X | X | X | X | X | X | X | X |
| Evaluación de cuestionario | Evaluación de cuestionario, Plantilla de cuestionario, Plantilla de sección, Plantilla de subsección, Plantilla de preguntas | X | X | X | X | X | X | X | X | X | X | X |
| Programa de evaluación | Program | X | X | X | X | X | X | X | X | X | X | X |
| Empleado | Empleado |  |  | X | X | X | X | X | X | X | X | X |
| Cuenta | Cuenta, Subcuenta, Declaración |  |  |  |  |  |  | X |  |  |  |  |
| Análisis de escenario | Análisis de escenario, Resultado del escenario | X |  | X |  |  |  |  | X |  |  |  |
| Pérdida externa | Pérdida de ORX, Pérdida de ORIC, Pérdida de FIRST |  |  |  |  |  |  |  | X |  |  |  |
| Evento de pérdida | Evento de pérdida, Impacto de pérdida, Recuperación de pérdidas, Centro de costes |  |  | X |  |  |  |  | X |  |  |  |
| Indicador clave de riesgo | KRI, Valor de KRI | X |  | X | X |  |  |  | X | X | X |  |
| KPI | KPI, Valor de KPI | X |  | X |  |  |  |  | X | X | X |  |
| Biblioteca regulatoria | Mandato, Submandato, Requisito, Obligación<br>Ascent Información de soporte (solo RCM)<br>Versión de requisito (sólo RCM)<br>Declaración de divulgación (solo ESG) | X |  |  |  | X | X |  |  | X | X |  |
| Evento normativo | Evento normativo<br>Evento regulador TRRI, Serie de eventos reguladores TRRI<br>Evento regulador WK<br>Reg-Track Evento regulador, Reg-Track Serie de eventos reguladores |  |  |  |  | X |  |  |  |  |  |  |
| Incidente | Incidente |  | X | X | X |  |  |  |  | X | X |  |
| Renuncia | Renuncia |  |  |  | X |  |  |  |  | X | X |  |
| Política | Política, Procedimiento, Comentario de revisión de política |  |  | X |  | X | X |  |  | X |  |  |
| Atestación de política | Política, Procedimiento, Atestación |  |  |  |  |  |  |  |  | X |  |  |
| Campaña | Campaña, Empleado, Atestación |  |  |  |  |  |  |  |  | X |  |  |
| Interacción con la autoridad reguladora | Interacción con la autoridad reguladora, Autoridad reguladora, Componente RI, Subcomponente RI, Comentario de revisión de conformidad, Tarea reguladora |  |  |  |  | X |  |  |  | X |  |  |
| Cambio regulador | Cambio regulador, Aplicabilidad del reglamento, Tarea reguladora, Comentario de revisión de conformidad | X | X |  |  | X |  |  |  | X |  |  |
| Política de ITG | Política, Procedimiento |  |  |  |  |  |  |  |  |  | X |  |
| Sistema | Sistema, Línea base |  | X |  |  |  |  |  |  |  | X |  |
| Activo | Activo, Enlace de activo |  | X | X |  |  |  |  |  |  | X |  |
| Plan anual | Plan de auditoría de resumen, Entidad auditable, Auditoría |  |  |  |  |  |  |  |  |  |  | X |
| Planificación de compromiso | Planificación, Hoja de registro horario, Auditor |  |  |  |  |  |  |  |  |  |  | X |
| Conclusiones | Conclusión |  |  |  |  |  |  |  |  |  |  | X |
| Trabajo de campo | Sección de auditoría, Informe de trabajo, Comentario de revisión de auditoría |  |  |  |  |  |  |  |  |  |  | X |
| Proyecto de conformidad | Proyecto, Plan de cumplimiento, Evaluación de plan de cumplimiento, Tema de cumplimiento, Evaluación de tema de cumplimiento, Obligación |  |  |  |  | X |  |  |  |  |  |  |
| Evaluación de requisitos | Evaluación de requisitos, Valor de evaluación de requisitos, Evaluación de obligaciones, Valor de evaluación de obligaciones | X |  |  |  | X |  |  |  |  |  |  |
| Autoridad reguladora | Autoridad reguladora, Iniciativa reguladora | X |  |  |  | X |  |  |  |  |  |  |
| Supervisión de modelo | Métrica, Valor de métrica |  |  |  |  |  | X |  |  |  |  |  |
| Estructura de comité | Comité, Empleado |  |  |  |  |  | X |  |  |  |  |  |
| Desencadenantes de inventario de modelos y MRG | Caso de uso de modelo, Despliegue de modelo, Modelo, Versión de modelo, Solicitud de cambio, Entrada de modelo, Salida de modelo, Enlace de modelo, Atestación de modelo, Tabla de puntuación de riesgo de modelo |  |  |  |  |  | X |  |  |  |  |  |
| Revisión y Desafío de MRG | Revisión, Desafío |  |  |  |  |  | X |  |  |  |  |  |
| Proveedor | Ubicación, Evento de continuidad de negocio, Proveedor, Compromiso, Contrato<br>Supply Wisdom, Supply Wisdom Alerta padre (sólo si se utiliza el canal de información Supply Wisdom .)<br>RiskRecon Ratings (sólo TPRM)<br>RapidRatings (sólo TPRM)<br>Subsidiaria de proveedor (sólo TPRM)<br>Subcontratista (solo TPRM) | X |  | X | X |  |  |  |  |  |  |  |
| Gestión de la continuidad de negocio | Servicio de negocio, Evaluación de servicios de negocio, Análisis de impacto de negocio, Evento de continuidad de negocio, Plan de continuidad de negocio, Plan de prueba de continuidad de negocio, Resultado de prueba de continuidad de negocio, Ubicación, Equipo, Modelo |  |  | X |  |  |  |  |  |  |  |  |
| Objetivo estratégico para ESG | Objetivo estratégico, producto | X |  |  |  |  |  |  |  |  |  |  |
| Vulnerabilidad | Vulnerabilidad, amenaza |  |  |  |  |  |  |  |  |  | X |  |

Además de los subcomponentes incluidos en la tabla, se incluyen los siguientes tipos de objeto en cada solución y cualquier usuario autorizado puede tener acceso a ellos:

- Firma
- Archivo
- Vínculo

## Asistentes

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-helpers)

Las soluciones de IBM OpenPages® incluyen varios ayudantes.

### Cómo solucionar problemas

Si encuentra un problema con un ayudante, puede configurar los valores del registro para crear registros para el ayudante. Utilice los siguientes valores de registro para configurar el registro para todos los ayudantes y desencadenantes:

- `/Solutions/ORM/Log Level/Log Level` controla la cantidad de registro que se va a producir. De forma predeterminada, se establece en el nivel ERROR.
- `/Solutions/ORM/Log Level/Log Folder` define la ubicación de los archivos de registro en el sistema de archivos. De forma predeterminada, se establece en `/aurora/logs/custom/`.

  Los siguientes archivos de registro se crean en esta ubicación: `helpers.log` para el registro de ayudantes y `triggers.log` y `DetectPropertyChangeToValueTrigger.log` para el registro de desencadenantes.
- `/Solutions/ORM/Log Level/Log Pattern` es el patrón de salida que utiliza para cada entrada de registro. Este patrón se ajusta a las reglas de formato de Log4j 2 tal como se describe en [Documentación de Apache](https://www.ibm.com/links?url=https%3A%2F%2Flogging.apache.org%2Flog4j%2F2.x%2Fmanual%2Flayouts.html).

Para habilitar la resolución de problemas, establezca el valor de registro `/Solutions/ORM/Log Level/Log Level` en `TRACE`. Para inhabilitar la resolución de problemas, restablezca el valor del registro en `ERROR`.

Debe reiniciar el servidor si cambia alguno de estos valores de registro.

### Tipos de ayudantes

En la tabla siguiente se muestran los asistentes incluidos para cada solución de forma predeterminada.

**Tabla 1. Ayudantes en IBM OpenPages soluciones**

| Asistente | TPRM | RCM | MRG | FCM | ORM | PCM | ITG | IAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Asistente de relleno de RCSA](#asistente-de-relleno-de-rcsa) |  |  |  |  | X |  |  |  |
| [Asistente de alineación de procesos RCSA](#asistente-de-alineación-de-procesos-rcsa) |  |  |  |  | X |  |  |  |
| [Asistente del programa de utilidad de inicio de RCSA](#asistente-del-programa-de-utilidad-de-inicio-de-rcsa) |  |  |  |  | X |  |  |  |
| [Asistente de sincronización de sitios de RCSA](#asistente-de-sincronización-de-sitios-de-rcsa) |  |  |  |  | X |  |  |  |
| Ver política<br>**Nota:** Este ayudante y la política de revisión son el mismo ayudante. Cada uno tiene una función diferente y dependen de en qué punto del ciclo de vida se encuentre la política. |  |  |  |  |  | X |  |  |
| Revisar política<br>**Nota:** Este ayudante y la política de vista son el mismo ayudante. Cada uno tiene una función diferente y dependen de en qué punto del ciclo de vida se encuentre la política. |  |  |  |  |  | X |  |  |
| [Asistente Vista de comparación de políticas](#asistente-vista-de-comparación-de-políticas) |  |  |  |  |  | X |  |  |
| [Asistente Desbloquear política](#asistente-desbloquear-política) |  |  |  |  |  | X |  |  |
| Publicación de notificaciones por lotes |  |  |  |  |  | X |  |  |
| Vista de conocimiento de política |  |  |  |  |  | X |  |  |
| Informe de creación de certificación |  |  |  |  |  | X |  |  |
| [Asistente Obtener líneas base](#asistente-obtener-líneas-base) |  |  |  |  |  |  | X |  |
| [Asistente Crear enlaces de recursos](#asistente-crear-enlaces-de-recursos) |  |  |  |  |  |  | X |  |
| [Asistente Cerrar auditoría](#asistente-cerrar-auditoría) |  |  |  |  |  |  |  | X |
| [Asistente para añadir o modificar planificaciones](#asistente-para-añadir-o-modificar-planificaciones) |  |  |  |  |  |  |  | X |
| [Asistente de entrada de hoja de registro horario](#asistente-de-entrada-de-hoja-de-registro-horario) |  |  |  |  |  |  |  | X |
| [Asistente de aprobación de hoja de registro horario](#asistente-de-aprobación-de-hoja-de-registro-horario) |  |  |  |  |  |  |  | X |
| Iniciar asistente del programa | X | X | X | X | X | X | X | X |

### Asistente de relleno de RCSA

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-rcsa-completion-helper)

El Asistente de relleno de RCSA permite al coordinador de RCSA finalizar la evaluación de riesgos y crear un árbol de evaluación para las referencias históricas.

El coordinador de RCSA recibe un mensaje que pregunta si se debe continuar. Cuando el coordinador de RCSA confirma el mensaje, el asistente realiza las siguientes acciones:

1. Establece el campo de estado **Evaluación de riesgos** como **Aprobado**.
2. Crea la siguiente estructura vinculada para el registro de evaluación secundario:

   - Análisis de evaluación de riesgos
   - Evaluación de procesos
   - Evaluación del riesgo
   - Evaluación de control
3. Copia los datos clave a los nuevos registros de evaluación y realiza asociaciones secundarias.

   Debe especificar qué campos deben copiarse (menú **Configuración**).

Para utilizar el ayudante, los usuarios necesitan un modelo de rol que incluya acceso de **Escritura** y **Asociado** a los tipos de objeto **Evaluación de riesgos** y **Evaluaciones de control**.

### Asistente de alineación de procesos RCSA

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-rcsa-process-alignment-helper)

El Asistente de alineación de procesos RCSA permite al coordinador de RCSA revisar los procesos, riesgos y controles asociados y crear más asociaciones. El asistente también configura los procesos, riesgos y controles con el estado de **En espera de evaluación**.

Cuando el coordinador de RCSA desea iniciar el ciclo RCSA, el coordinador puede iniciar el ayudante desde un enlace de URL en la vista de tareas Evaluación de riesgos.

El asistente basado en tareas realiza las siguientes acciones cuando se inicia:

1. Añade o elimina procesos, riesgos y controles
2. Revisa la propiedad del proceso, del riesgo y del control
3. Pregunta al coordinador de RCSA si desea iniciar la evaluación

   - Si el coordinador responde **Sí**, el asistente continúa con los siguientes procesos:

     - Establece todos los riesgos y controles como **En espera de evaluación**.
     - Establece el campo **Enviar para aprobación** del objeto Riesgo como **No**.
     - Establece el campo **Aprobar/Rechazar** del objeto Riesgo como un valor en blanco.
     - Establece el campo **Comentarios de rechazo** del objeto Riesgo como un valor en blanco.
   - Si el coordinador no desea comenzar el ciclo de RCSA, guarde y cierre la evaluación.

### Asistente del programa de utilidad de inicio de RCSA

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-rcsa-launch-utility-helper)

El Asistente del programa de utilidad de inicio de RCSA genera objetos de evaluación de riesgos para las entidades dentro del ámbito.

El Asistente del programa de utilidad de inicio de RCSA ayuda al administrador a iniciar el proceso de RCSA del siguiente modo:

1. Crea una evaluación de riesgos bajo la entidad de negocios y asocia todos los procesos que están bajo esa entidad de negocios con la evaluación de riesgos.
2. Solicita los detalles de la evaluación de riesgos.

   El administrador proporciona valores para los campos en todas las evaluaciones de riesgos generadas, como **Fecha de inicio**, **Fecha de finalización** e **Instrucciones / Orientación**.
3. Identifica todas las entidades **Dentro del ámbito**.
4. Genera un objeto de evaluación de riesgos para todas las entidades de negocios **Dentro del ámbito**.
5. Rellena el objeto de evaluación de riesgos con los valores proporcionados en el paso 1.
6. Establece el estado de la evaluación de riesgos como **No iniciado** y el campo **Administrador de RCSA** se rellena con el nombre de usuario correspondiente.
7. Envía un correo electrónico al coordinador de RCSA informándole de que el ciclo de RCSA puede comenzar.

   El administrador puede especificar el contenido del correo electrónico a través de la página **Configuración**. El correo electrónico del coordinador de riesgos utiliza la información del registro de preferencia más próximo que tenga el coordinador de RCSA especificado.

### Asistente de sincronización de sitios de RCSA

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-rcsa-site-sync-helper)

El Asistente de sincronización de sitios de RCSA sincroniza instancias de datos de objetos con valores de una estructura de datos de biblioteca.

Cuando se inicia el asistente, identifica todos los cambios en el objeto maestro/biblioteca. El asistente utiliza un campo **Referencia de biblioteca** como una clave común y sincroniza todas las instancias locales del objeto con el maestro.

El ayudante de sincronización del sitio RCSA está disponible en **Reporting** > **OpenPages Informes de soluciones** > **Programas de utilidad administrativos**.

### Configuración de asistentes de RCSA

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-rcsa-configuration)

Si utiliza el proceso de negocio RCSA, el administrador debe configurar RCSA después de instalar los módulos de IBM OpenPages .

#### Datos

El Asistente de alineación de procesos de RCSA y el Asistente de sincronización de sitios de RCSA necesitan el uso de jerarquías de biblioteca y de transferencia.

- **Jerarquía de biblioteca**

  Para contar con la funcionalidad total del asistente de RCSA, debe crear una jerarquía de bibliotecas.

  El objeto raíz Biblioteca es una entidad de negocios y la estructura contiene los procesos empresariales, riesgos y controles comunes que se van a utilizar en el proceso de RCSA.

  Por ejemplo: Entidad de biblioteca: / Biblioteca RCSA

- **Jerarquía de transferencia**

  Para contar con la funcionalidad total del asistente de RCSA, debe crear una jerarquía intermedia.

  El objeto raíz Transferencia es una entidad de negocios y la estructura incluye un proceso de transferencia y un riesgo. La jerarquía se utiliza para almacenar los procesos, riesgos y controles que se eliminan de la entidad empresarial como parte del proceso RCSA.

  Un ejemplo de entidad de transferencia: /RCSA Staging Hierarchy

  Un ejemplo de proceso de transferencia: /RCSA Staging Hierarchy/Staging Process

  Un ejemplo de riesgo de transferencia: /RCSA Staging Hierarchy/Staging Risk

Los datos de jerarquía de transferencia y biblioteca se cargan cuando se instala IBM OpenPages Operational Risk Management .

#### Valores

Las áreas de biblioteca y de transferencia tienen ajustes correspondientes que deberá configurar para los asistentes de RCSA para registrar las estructuras.

Para configurar estos valores:

1. Inicie sesión como administrador.
2. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Configuración**.
3. Expanda las opciones de las siguientes entradas y configure los valores de la jerarquía de transferencia que ha creado.

   - COMMON
   - RCSA PROCESS ALIGNMENT HELPER
   - RCSA SITESYNC
   - RCSA TRIGGERS

#### Común

- **`/OpenPages/Solutions/ORM/Common/Library Path`**

  Este valor se debe configurar en el objeto de entidad raíz Biblioteca; por ejemplo, /RCSA Library.

  Se utiliza con el Asistente de sincronización de sitios de RCSA y el Asistente de alineación de procesos RCSA.

#### Asistente de alineación de procesos RCSA

Esta tabla identifica los valores utilizados en el Asistente de alineación de procesos RCSA.

| Vía de acceso | Descripción |
| --- | --- |
| `/OpenPages/Solutions/ORM/Helpers/RCSA/Alignment/Removed Control Path` | Lo utiliza el Asistente de alineación de procesos para almacenar los controles eliminados. Este valor debe ser una ruta a un riesgo del sistema; por ejemplo, /RCSA Staging Hierarchy/Staging Risk. |
| `/OpenPages/Solutions/ORM/Helpers/RCSA/Alignment/Removed Process Path` | Lo utiliza el Asistente de alineación de procesos para almacenar los procesos eliminados. Este valor debe ser una ruta a una entidad del sistema; por ejemplo, /RCSA Staging Hierarchy. |
| `/OpenPages/Solutions/ORM/Helpers/RCSA/Alignment/Removed Risk Path` | Lo utiliza el Asistente de alineación de procesos para almacenar los riesgos eliminados. Este valor debe ser una ruta a un proceso del sistema; por ejemplo, /RCSA Staging Hierarchy /Staging Process. |

#### Asistente de sincronización de sitios de RCSA

Esta tabla identifica los valores utilizados en el Asistente de sincronización de sitios de RCSA.

| Vía de acceso | Descripción |
| --- | --- |
| `/OpenPages/Solutions/ORM/Helpers/RCSA/SiteSync/Exclude object` | Lo utiliza el Asistente de sincronización de sitios de RCSA para excluir los objetos que se necesita sincronizar. |
| `/OpenPages/Solutions/ORM/Helpers/RCSA/SiteSync/Standalone offset` | Lo utiliza el Asistente de sincronización de sitios de RCSA para buscar hacia atrás un número de días. Por ejemplo, 1 es ayer. |
| `/OpenPages/Solutions/ORM/Helpers/RCSA/SiteSync/Standalone target entity` | Lo utiliza el Asistente de sincronización de sitios de RCSA como jerarquía organizativa raíz; por ejemplo, /BANK ORG. |

### Visores de políticas

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-policy-viewers)

Una serie de visores de políticas facilitan el proceso de creación, modificación, revisión y aprobación de políticas y procedimientos. Agrega varias secciones de una política y los procedimientos asociados a una única vista narrativa para editar, revisar y aprobar, en tanto que permite a los clientes mantener la estandarización de una plantilla **Política**.

Este asistente ofrece las siguientes vistas:

- **Modificar política** - Abierta desde un objeto **Política**, la vista **Modificar política** es una vista editable que permite al autor y al propietario de la política crear y editar un objeto **Política** y sus **Procedimientos** asociados. El visor **Modificar política** solo se utiliza como parte del enfoque **Centrado en datos** para Gestión de políticas.
- **Ver política** - Abierta desde un objeto **Política**, la vista **Ver política** es una vista de solo lectura que permite a los usuarios ver una política y sus procedimientos en una vista narrativa con formato (enfoque **Centrado en datos** e **Híbrido**) o desde un enlace **Archivo adjunto de política** (enfoque **Centrado en documento**).
- **Revisar política** - Abierta desde un objeto **Comentarios de revisión de política**, la vista **Revisar política** es una vista basada en funciones que hace más sencillos los procesos de revisión y aprobación. Además de mostrar los objetos **Política** y **Procedimiento**, o el enlace **Archivo adjunto de política**, incluye el objeto **Comentarios de revisión de política** que permite a los revisores y aprobadores enviar comentarios editando directamente el objeto **Política** o utilizando el formulario **Comentarios**. Los revisores se presentan con una vista editable o de sólo lectura de la política y sus procedimientos, en función del parámetro establecido en IBM OpenPages® en la página **Valores** . A los aprobadores se les presenta una vista de solo lectura de la política.

Utilice los ajustes y los ajustes de texto de la aplicación para configurar este componente de forma que se comporte según la metodología del cliente.

### Asistente Vista de comparación de políticas

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-compare-policy-view-helper)

El asistente Vista de comparación de políticas permite a los usuarios ver diferencias marcadas en color rojo de una versión de política a otra. Por ejemplo, un usuario puede observar a simple vista las diferencias entre un borrador actual de una política y la política publicada, o de las versiones anteriores ya caducadas.

El componente Vista de comparación de políticas se utiliza con los enfoques **Centrado en datos** e **Híbrido**.

Utilice los ajustes de texto de la aplicación y del registro para configurar este componente de forma que se comporte según la metodología de los clientes.

### Asistente Desbloquear política

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-policy-unlock-helper)

El asistente Desbloquear política se abre desde el objeto Política después de que la política pasa a la fase de revisión y aprobación. El asistente Desbloquear política desbloquea el objeto Política y sus componentes (**Procedimientos**, **Adjuntos**, **Comentarios de revisiones de políticas**) para su revisión.

El asistente Desbloquear política admite tres enfoques de política: centrada en datos, centrada en documentos e híbrida.

El asistente Desbloquear política admite dos casos de uso:

1. La reapertura de un objeto **Política** para los cambios producidos dentro de un ciclo de revisión:

   - Establece el **Estado de aprobación** en **En revisión**.
   - Desbloquea los objetos o adjuntos bloqueados que se necesitan durante el proceso de revisión.
   - Actualiza el número de versión.
2. Apertura de una política para un nuevo ciclo de revisión:

   - Establece **Estado de aprobación** como En revisión.
   - Desbloquea el objeto Política y sus componentes (por ejemplo, **Procedimientos**, Adjuntos).
   - Restablece y borra campos, como **Fecha de publicación**, **Estado de publicación**, **Siguiente fecha de revisión**.
   - Actualiza el número de versión.
   - Elimina o borra objetos de **comentarios de revisión de políticas**.
   - Establece un distintivo en la política publicada correspondiente para indicar que el borrador está **En revisión**.

Puede configurar este componente para que cumpla sus requisitos utilizando valores y valores de texto de aplicación. Sin embargo, no cambie el tipo de visualización del campo Autor de la política a un tipo de visualización de varios valores. El campo Autor de la política debe ser un único campo Selector de usuario.

### Asistente Publicar notificación por lotes

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-publishing-batch-notification-helper)

El asistente Publicar notificación por lotes hace más sencillo el proceso de promocionar una política de borrador aprobada a la biblioteca de publicados y de mover la versión publicada actual a la biblioteca de caducados. También retira una política moviendo la política publicada a la biblioteca de publicados y eliminando el borrador. Puede utilizar el asistente Publicar notificación por lotes con los enfoques de política **Centrado en datos**, **Centrado en documentos**, e **Híbrido**.

El asistente Publicar notificación por lotes se ejecuta de forma programada y realiza las siguientes tareas:

- Actualiza la política en borrador:

  - Configura los campos de la política en borrador como **Estado de aprobación**, **Fecha de publicación** y **Estado de publicación**.
  - Actualiza un número de versión en función de la relevancia de un cambio en la política.
- Promociona un objeto **Política** publicado a la biblioteca de caducados:

  - Renombra el objeto de **política** (añade `Expired – V#`).
  - Establece **Ubicación de política** como **Caducada** y especifica la fecha de caducidad.
  - Mantiene las aprobaciones y las asociaciones con objetos como **Entidades** y **Mandatos**.
  - Elimina los archivos adjuntos de políticas híbridas.
- Promociona un objeto **Política** en borrador a la biblioteca de publicados:

  - Establece **Ubicación de política** en **Publicado**.
  - Mantiene las aprobaciones y las asociaciones con objetos como **Entidades** y **Mandatos**.
  - Mantiene asociaciones de objeto existentes (**Evaluación de riesgos**) en un objeto **Política** publicado.
- Envía correos electrónicos tras la correcta de la publicación.

Utilice los ajustes y los ajustes de texto de la aplicación para configurar este componente de forma que se comporte según la metodología del cliente.

### Asistente Vista de conocimiento de política

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-policy-awareness-view-helper)

El asistente Vista de conocimiento de política es una vista intuitiva que permite a los empleados leer de forma fácil una política y sus procedimientos y sus procedimientos en un formato narrativo. El empleado testifica que ha leído y comprendido la política.

El asistente Vista de conocimiento de política realiza las siguientes tareas:

- Muestra los objetos **Política** y su **Procedimiento** en un formato narrativo simple y de solo lectura con la apariencia de una política corporativa.
- Permite a los empleados testificar respecto a la política con un simple clic y sin ningún tipo de navegación.
- Permite a los empleados solicitar una excepción al requisito de atestación de política.

Utilice los ajustes de texto de la aplicación y del registro para configurar este componente para que se comporte según la metodología del cliente.

### Asistente Informe de creación de atestación

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-attestation-creation-report-helper)

El asistente Informe de creación de atestación es una notificación planificada.

Este informe proporciona soporte a la función de conocimiento de políticas. Está pensado para ejecutarse de forma planificada y realiza las siguientes tareas:

- Encuentra todos los objetos Campaña con el estado **Listo para empezar** asociado a las políticas publicadas.
- Encuentra todos los empleados activos que cumplen los mismos criterios de los requisitos de atestación definidos en el objeto Campaña.
- Crea un registro **Atestación** para cada empleado coincidente con esa campaña de política.
- Muestra el registro de **Certificación** en el panel de control del empleado.
- Envía a cada empleado una notificación por correo electrónico y los avisa de que una atestación ha vencido.

### Asistente Obtener líneas base

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-get-baselines-helper)

Iniciado desde un campo de enlace en el objeto del sistema, este ayudante copia la línea base seleccionada de la biblioteca en el entorno operativo de TI, y copia, o crea y rellena previamente, riesgos, controles y planes de prueba descendientes. El asistente crea asociaciones desde los nuevos elementos a los elementos de biblioteca y graba la información de estado en el campo de descripción adicional de la línea base creada.

### Asistente Crear enlaces de recursos

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-create-resource-links-helper)

Este ayudante crea un enlace de activo como un nivel inferior del activo inicial y como un nivel inferior del activo seleccionado. El ayudante rellena previamente los campos en el objeto Enlace de activo creado.

El ayudante se puede iniciar de las siguientes maneras:

- Pulsando **Crear enlace de recurso** en la pestaña **Admin** de la vista de tarea Activo.
- Añadiendo el campo Enlace de activo a las vistas de tarea o cuadrícula para el objeto Activo. A continuación, puede iniciar el ayudante desde la vista.

### Asistente Cerrar auditoría

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-close-audit-helper)

Lanzado desde un campo de enlace en el objeto de auditoría, el ayudante de cierre de auditoría facilita la automatización del proceso de cierre de auditoría.

El ayudante de cierre de la auditoría proporciona un resumen y, opcionalmente, detalles del estado de preparación para el cierre de la auditoría desde la que se lanzó este ayudante, y de todos sus componentes. Cuando todos los componentes están listos, el ayudante proporciona un botón de Cerrar Auditoría que automatiza las acciones realizadas cuando se cierra una auditoría, como establecer y borrar los valores de los campos, eliminar las instancias de los objetos y bloquear los objetos.

Configure este componente para que se comporte según sea apropiado para su metodología utilizando los valores de texto de registro y aplicación.

### Asistente para añadir o modificar planificaciones

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-add-modify-plans-helper)

El ayudante para añadir o modificar planes, que se ejecuta desde un enlace de campo calculado en el objeto de auditoría y que solo está disponible para el propietario de la auditoría, facilita la creación y edición de planes de auditoría. Localiza auditores y los rellena en los campos para asignarlos a las planificaciones.

El asistente proporciona un resumen de las planificaciones de esta auditoría y la capacidad de modificarlas. Proporciona la posibilidad de añadir un nuevo plan a esta auditoría. También proporciona la capacidad de buscar agrupaciones de auditores o una parte determinada de la agrupación, para localizar auditores que tengan los conocimientos, atributos y requisitos de disponibilidad identificados en la planificación. Permite ver detalles de otras planificaciones para cada auditor localizado y seleccionar y rellenar de forma automática al auditor más idóneo a partir de los resultados de búsqueda.

Utilice los ajustes de texto de la aplicación y del registro para configurar este componente de forma que se comporte según la metodología del cliente.

### Asistentes de hoja de registro horario

`Guía de soluciones › Asistentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-timesheet)

IBM OpenPages® Internal Audit Management incluye asistentes de hoja de registro horario.

#### Asistente de entrada de hoja de registro horario

`Guía de soluciones › Asistentes › Asistentes de hoja de registro horario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-timesheet-entry-helper)

Los auditores utilizan el Asistente de entrada de hoja de registro horario para anotar el tiempo y los gastos.

El Asistente de entrada de hoja de registro horario tiene las prestaciones siguientes:

- El asistente incluye validaciones de entrada de datos y permite a los auditores suprimir las entradas de registro horario existentes por filas individuales.
- Puede configurar el asistente de modo que permita a los miembros de un grupo de usuarios entrar las horas de parte de otro auditor.
- Los auditores pueden ver todos los comentarios de rechazo a la vez, y pueden saltar fácilmente a las hojas de registro horario que necesiten actualizar.
- Los auditores pueden buscar y filtrar a partir de la auditoría y plan que necesiten al añadir una fila nueva de hoja de registro horario. Para ayudar al usuario, puede configurar qué campos de auditoría y plan desea que se muestren.

Pulse **Ayudante de entrada de hoja de registro horario** en el panel Informes del panel de control para abrir el Ayudante de entrada de la hoja de registro horario. También puede ver información de hoja de registro horario utilizando el elemento de menú **Gestión de auditoría** > **Hojas de registro horario** .

Cuando un auditor crea y guarda entradas de hojas de registro horario, se crean los objetos de hoja de registro horario, se rellenan las filas nuevas, y los valores se guardan en las hojas de registro horario existentes. Los gastos y las horas son una única entrada por fila a la semana y no se desglosan en categorías de gastos. El tiempo y los gastos se introducen y se muestran siempre en la moneda base.

Puede configurar el ayudante. Haga clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Ajustes** y, a continuación, utilice la configuración de **Soluciones** > **IAM** > **Registro de horas** > **Ayudante de entrada de horas**.

#### Asistente de aprobación de hoja de registro horario

`Guía de soluciones › Asistentes › Asistentes de hoja de registro horario` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=helpers-timesheet-approval-helper)

Los aprobadores del tiempo de los auditores, como propietarios de auditorías o propietarios de planes, utilizan el Asistente de aprobación de hoja de registro horario para revisar y aprobar o rechazar los registros horarios y de gastos.

El Asistente de aprobación de hoja de registro horario separa la hoja de registro horario de la aprobación de hoja de registro horario. Al configurar el asistente, especifique quién puede aprobar o rechazar las hojas de registro horario.

Los aprobadores pueden gestionar todas las aprobaciones a la vez, en auditorías y auditores. Además, los aprobadores pueden ver la cola de las hojas de registro horario pendientes de aprobación.

Cuando un aprobador rechaza una hoja de registro horario, el auditor recibe una notificación por correo electrónico. Esta característica de notificación es opcional.

Pulse **Ayudante de aprobación de hoja de registro horario** en el panel Informes del panel de control para abrir el Ayudante de aprobación de la hoja de registro horario. También puede ver información de hoja de registro horario utilizando el elemento de menú **Gestión de auditoría** > **Hojas de registro horario** .

Puede configurar el ayudante de aprobación de la hoja de registro horario. Haga clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Ajustes** y, a continuación, utilice la configuración de **Soluciones** > **IAM** > **Registro de horas** > **Ayudante de aprobación de hojas de horas**.

## Notificaciones

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-notifications)

Las notificaciones son correos electrónicos que se envían a los propietarios de un proceso como un recordatorio para actuar. Estas notificaciones se pueden producir en diferentes etapas de un proceso o como el paso final de un activador.

Todas las notificaciones que se envían desde las soluciones de IBM OpenPages® utilizan la siguiente dirección del remitente. Configure la dirección de correo electrónico y los ajustes del servidor utilizando la abreviatura de la solución adecuada:

- `/OpenPages/Solutions/ORM/Email/From Email`: la dirección del remitente que se utiliza para enviar notificaciones.
- `/OpenPages/Solutions/ORM/Email/From Name`: configure este elemento para identificar el nombre del remitente de correo electrónico que utilizan las notificaciones.
- `/OpenPages/Common/Email/Mail Server`: configure este elemento para identificar el servidor de correo electrónico que se utiliza para enviar notificaciones.

  Este elemento es utilizado por ciclos de vida. Para los correos electrónicos generados por desencadenantes de ciclo de vida, la dirección del remitente se especifica en el archivo `trigger.xml`. El valor predeterminado es donotreply@openpages.com.

Para obtener información sobre los valores de correo electrónico, consulte la publicación *IBM OpenPages Guía del administrador*.

Las soluciones de OpenPages constan de varias notificaciones. En la tabla siguiente se muestran las notificaciones incluidas para cada solución de forma predeterminada.

Los flujos de trabajo definidos en GRC Workflow también pueden realizar notificaciones. Puede utilizar tanto las notificaciones como las notificaciones de correo electrónico de flujo de trabajo para el mismo tipo de objeto, pero debe tener en cuenta cómo interactúan y dónde entran en conflicto. Para obtener más información, consulte *Configuración de GRC Workflow* en la publicación *IBM OpenPages Guía del administrador*.

**Tabla 1. Notificaciones en IBM OpenPages soluciones**

| Notificación | BCM | TPRM | RCM | MRG | FCM | ORM | PCM | ITG | IAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Notificación a través del boletín de problemas y acciones](#notificación-a-través-del-boletín-de-problemas-y-acciones) |  | X | X | X | X | X | X | X | X |
| [Notificación de incidente](#notificación-de-incidente) |  |  |  |  |  |  | X | X |  |
| [Notificación de evaluación de cuestionario](#notificación-de-evaluación-de-cuestionario) |  | X | X | X | X | X | X | X | X |
| [Notificación de Reg-Track Ingestion Error](#notificación-de-error-de-ingesta-de-reg-track) |  |  | X |  |  |  |  |  |  |
| [Notificación de Error de ingesta TRRI](#notificación-de-error-de-ingesta-trri) |  |  | X |  |  |  |  |  |  |
| [Notificación de Error de ingesta WK](#notificación-de-error-de-ingesta-wk) |  |  | X |  |  |  |  |  |  |
| [Notificación de objetos de biblioteca reguladora nuevos/corregidos](#notificación-de-objetos-de-biblioteca-reguladora-nuevoscorregidos) |  |  | X |  |  |  |  |  |  |
| Notificación de Entrada de evento de pérdida |  |  |  |  |  | X |  |  |  |
| Notificación de control |  | X | X | X | X | X | X | X | X |
| Notificación de rechazo de hoja de registro horario |  |  |  |  |  |  |  |  | X |

### Notificación a través del boletín de problemas y acciones

`Guía de soluciones › Notificaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=notifications-issue-action-bulletin-notification)

Durante la fase de cierre del proceso de gestión de problemas y solución (IMR), se envía un boletín de problemas y acciones como una notificación de correo electrónico a los usuarios. El boletín resalta áreas importantes, como los problemas vencidos y las acciones que están pendientes de cierre. El administrador puede establecer la frecuencia de esta notificación utilizando el boletín de gestión de problemas y solución (IMR).

Cuando se define el Problema, su estado se establece en abierto. El usuario proporciona la fecha de vencimiento actual. La fecha de vencimiento se copia en un campo de solo lectura que contiene la fecha de vencimiento original. Cuando el usuario crea un Problema, el propietario del problema (que puede que no sea la misma persona que ha creado el problema) recibe una notificación por correo electrónico.

El propietario del problema identifica las acciones necesarias para resolver un problema. Los siguientes datos se capturan en un elemento de acción:

- Descripción
- Assignee
- Fecha de inicio
- Fecha de vencimiento
- Fecha de cierre real
- Estado (solo lectura)
- Un comentario para registrar las últimas actualizaciones

El propietario del problema recibe un correo electrónico que resume las acciones que requieren aprobación antes de que se pueda cerrar el problema. El propietario puede aceptar o rechazar el cierre del problema. Una vez finalizadas las acciones, el propietario del problema revisa el problema y actualiza el estado a cerrado. Si cualquier acción hijo está establecida para abrirse o en espera de aprobación, el propietario del problema no puede cerrarlo.

Los problemas sólo se visualizan si la entidad de negocios de nivel inferior tiene un objeto de preferencia hijo asociado al mismo. Si el problema se genera a partir de la entidad de negocio de nivel inferior o de otro tipo de objeto, no se incluye en este informe. Defina un objeto de preferencia para cada nivel en el que se va a informar. Otras características, como el activador de RCSA, utilizan el padre más cercano con un objeto de preferencia. Estas características heredan la preferencia del objeto padre más cercano.

Los usuarios reciben notificaciones por correo electrónico a través de los boletines de problemas y acciones consolidados. El boletín consolida la información siguiente:

- Problemas que se asignan al destinatario en los últimos números de días
- Acciones que se asignan al destinatario en los últimos números de días
- Problemas previstos para cerrar en los próximos números de días.
- Acciones previstas para cerrar en los próximos números de días.
- Problemas vencidos
- Acciones vencidas
- Acciones a la espera de aprobación de cierre

### Notificación de incidente

`Guía de soluciones › Notificaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=notifications-incident-notification)

La notificación de incidencias envía un correo electrónico a un responsable cuando se crea una incidencia y para cada transición del flujo de trabajo de incidencias.

La notificación de incidencias se inicia mediante el flujo de trabajo de incidencias. La notificación de correo electrónico contiene la etapa, el estado y un enlace al incidente.

### Notificación de evaluación de cuestionario

`Guía de soluciones › Notificaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=notifications-questionnaire-assessment-notification)

La notificación de evaluación de cuestionario envía un correo electrónico a un destinatario cuando se crea una evaluación de cuestionario y para cada transición del flujo de trabajo.

El flujo de trabajo del cuestionario inicia la notificación de evaluación de cuestionario. La notificación de correo electrónico contiene la etapa, el estado y un enlace a la evaluación de cuestionario.

### Notificación de error de ingesta de Reg-Track

`Guía de soluciones › Notificaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=notifications-reg-track-ingestion-error-notification)

La notificación de error de ingesta de Reg-Track envía un correo electrónico a los administradores de Reg-Track si la importación de un canal de información de Reg-Trackfalla. Los administradores de Reg-Track se configuran al configurar el canal de información Reg-Track en IBM OpenPages®.

### Notificación de Error de ingesta TRRI

`Guía de soluciones › Notificaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=notifications-trri-ingestion-error-notification)

La notificación de error de ingestión de TRRI envía un correo electrónico a los administradores de TRRI si falla la importación de un canal de información de Thomson Reuters Regulatory Intelligence (TRRI). Los administradores de TRRI se configuran al configurar el canal de información de TRRI en IBM OpenPages®.

### Notificación de Error de ingesta WK

`Guía de soluciones › Notificaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=notifications-wk-ingestion-error-notification)

La notificación de error de ingestión de WK envía un correo electrónico a los administradores de WK si la importación de un canal de información de Wolters Kluwer falla. Los administradores de WK se configuran al configurar el canal de información WK en IBM OpenPages®.

### Notificación de objetos de biblioteca reguladora nuevos/corregidos

`Guía de soluciones › Notificaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=notifications-newamended-regulatory-library-object-notification)

La notificación Objeto de biblioteca reguladora nuevo/modificado envía un correo electrónico si un mandato, submandato o requisito cambia como resultado de una importación de Ascent Reg Tech, Thomson Reuters Regulatory Intelligence o Wolters Kluwer . El correo electrónico se envía al propietario del objeto.

## Informes

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-reports)

Las soluciones de IBM OpenPages® incluyen varios informes.

Los informes adicionales se instalan con OpenPages y están disponibles para todas las soluciones. Para obtener más información, consulte la publicación *IBM OpenPages Guía del administrador*.

En la tabla siguiente se muestran los informes incluidos para cada solución de forma predeterminada.

**Tabla 1. Informes por IBM OpenPages solución**

| Informe |  | FCM | ORM | PCM | ITG | IAM | ESG |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Informes de evaluación de riesgos |  |  |  |  |  |  |  |
|  | Lista de evaluación de riesgos | X | X | X | X | X |  |
|  | Estado de la evaluación de riesgos | X | X | X | X | X |  |
|  | Resumen de evaluación de riesgos | X | X | X | X | X |  |
|  | Problemas y planes de acción de evaluación de riesgos | X | X | X | X | X |  |
| Informes de riesgos |  |  |  |  |  |  |  |
|  | Análisis de riesgos | X | X | X | X | X |  |
|  | Gráfica de riesgos | X | X | X | X | X |  |
|  | Clasificación de riesgo por entidad | X | X | X | X | X |  |
|  | Clasificación de riesgo por categoría | X | X | X | X | X |  |
|  | Riesgos principales | X | X | X | X | X |  |
| Informes de control |  |  |  |  |  |  |  |
|  | Matriz de riesgo y control | X | X | X | X | X |  |
|  | Gráfica de la eficacia de control | X | X | X | X | X |  |
| Informes de prueba |  |  |  |  |  |  |  |
|  | Pruebas de rendimiento y resultados | X | X | X | X | X |  |
| Informes de indicador |  |  |  |  |  |  |  |
|  | Panel KRI |  | X | X | X |  |  |
|  | Panel KPI |  | X | X | X |  |  |
| Informes de eventos de pérdida |  |  |  |  |  |  |  |
|  | Panel de control de eventos de pérdida consolidados |  | X |  |  |  |  |
|  | Riesgo frente a pérdida |  | X |  |  |  |  |
| Informes de gestión de problemas y corrección |  |  |  |  |  |  |  |
|  | Panel de control de problemas de ORM |  | X |  |  |  |  |
|  | Elementos de acción y problemas de ORM |  | X |  |  |  |  |
| Informes de análisis de escenarios |  |  |  |  |  |  |  |
|  | Resumen del escenario |  | X |  |  |  |  |
| Informes de conformidad reguladora |  |  |  |  |  |  |  |
|  | Eficacia de control de proceso por mandato |  |  | X |  |  |  |
|  | Matriz de aplicabilidad del reglamento |  |  | X |  |  |  |
| Informes de activos de TI |  |  |  |  |  |  |  |
|  | Línea base |  |  |  | X |  |  |
|  | Plan de control |  |  |  | X |  |  |
| Informes de conformidad de TI |  |  |  |  |  |  |  |
|  | Eficacia de control de TI por mandato |  |  |  | X |  |  |
|  | Biblioteca de requisitos |  |  |  | X |  |  |
|  | Biblioteca de requisitos del UCF |  |  |  | X |  |  |
| Informes de administración de auditoría |  |  |  |  |  |  |  |
|  | Universo de auditoría |  |  |  |  | X |  |
|  | Plan de auditoría |  |  |  |  | X |  |
|  | Plan de auditor |  |  |  |  | X |  |
|  | Descripción general de auditoría |  |  |  |  | X |  |
|  | Informe de auditoría interna |  |  |  |  | X |  |
|  | Desviación de auditoría |  |  |  |  | X |  |
|  | Desviación del auditor |  |  |  |  | X |  |
|  | Panel de hojas de registros horarios de auditor |  |  |  |  | X |  |
|  | Panel de utilización de auditor |  |  |  |  | X |  |
|  | Panel de aprobaciones de hoja de registro horario pendientes |  |  |  |  | X |  |
|  | Entrada de hoja de registro horario |  |  |  |  | X |  |
|  | Aprobación de hoja de registro horario<br>Asistente |  |  |  |  | X |  |
| Informes de cuestionario |  |  |  |  |  |  |  |
|  | Informe de programa | X | X | X | X | X | X |
|  | Informe de evaluación único | X | X | X | X | X | X |
| Informes de FCM |  |  |  |  |  |  |  |
|  | Ámbito de cuenta por entidad y clasificación | X |  |  |  |  |  |
|  | Certificación de control - Informe de resumen de proceso | X |  |  |  |  |  |
|  | Informe Resumen de estado de certificación de control | X |  |  |  |  |  |
|  | Informe de problemas y acciones de FCM | X |  |  |  |  |  |
|  | Correlación de cuentas y procesos de FCM | X |  |  |  |  |  |
|  | Informe de resumen de SOX (FCM - Informe de certificación de control de proceso) | X |  |  |  |  |  |
| Informes de ESG |  |  |  |  |  |  |  |
|  | Panel de control de objetivos |  |  |  |  |  | X |
|  | Informe de acceso a detalles de panel de control de objetivos |  |  |  |  |  | X |
|  | Listado de objetivos |  |  |  |  |  | X |
|  | Panel de control KRI de objetivo |  |  |  |  |  | X |
|  | Panel de control de conformidad de ESG |  |  |  |  |  | X |
|  | Conformidad por acceso a detalles de mandato |  |  |  |  |  | X |
|  | Detalles de cumplimiento normativo y estándar de ESG |  |  |  |  |  | X |
|  | Lista de proveedores-Clasificaciones ESG<br>Requiere TPRM y Supply Wisdom |  |  |  |  |  | X |
|  | Obtención de detalles de proveedor de ESG<br>Requiere TPRM y Supply Wisdom |  |  |  |  |  | X |
|  | Comparación de proveedores-ESG<br>Requiere TPRM y Supply Wisdom |  |  |  |  |  | X |
|  | Postura de proveedor-Calificaciones de ESG<br>Requiere TPRM y Supply Wisdom |  |  |  |  |  | X |

### Informes de evaluación de riesgos

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-risk-assessment)

Los informes de evaluación de riesgos proporcionan soporte al equipo directivo para tomar mejores decisiones que conducen a la acción. Estos informes forman parte de la fase de acción del proceso de evaluación de riesgos y autocontrol (RCSA).

En la tabla siguiente se describen los informes de evaluación de riesgo disponibles. Los usuarios pueden profundizar en algunos informes para obtener más detalles.

**Tabla 1. Informes de evaluación de riesgos**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Lista de evaluación de riesgos |  | Muestra detalles de la evaluación de riesgos para una entidad de negocios específica y todos sus descendientes. |
| Estado de la evaluación de riesgos | Detalle del estado de la evaluación de riesgos | Muestra un gráfico de columnas apilado que muestra el estado de las evaluaciones de riesgos para la entidad de negocios especificada y sus descendientes directos. |
| Resumen de evaluación de riesgos | Problemas y planes de acción de evaluación de riesgos | Muestra los detalles de las evaluaciones de riesgos junto con sus riesgos y controles asociados. Un informe de acceso a los detalles muestra los problemas y los elementos de acción relacionados con las evaluaciones de riesgos, los riesgos y los controles. |
| Problemas y planes de acción de evaluación de riesgos |  | Muestra todos los problemas y elementos de acción relacionados con la evaluación de riesgos seleccionada y sus riesgos y controles asociados. El objeto principal solo muestra los elementos principales de la evaluación de riesgos, el riesgo y los controles.<br>El informe solicita dos valores: la entidad de negocios y la evaluación de riesgos. Los datos se filtran según la entidad seleccionada. Los usuarios pueden elegir entre todas las evaluaciones de riesgos que están asociadas, directa o indirectamente, a la entidad de negocios seleccionada. |

### Informes de riesgos

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-risk)

Los informes de riesgo están disponibles en las soluciones de IBM OpenPages® . Los usuarios pueden profundizar en algunos informes para obtener más detalles.

**Tabla 1. Informes de riesgos**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Análisis de riesgos |  | Muestra los riesgos agrupados por proceso para una entidad de negocios especificada. |
| Gráfica de riesgos | Detalle de riesgo | Muestra una tabla que agrega riesgos por impacto residual y la probabilidad para una determinada entidad de negocios. |
| Clasificación de riesgo por entidad | Detalle de clasificación de riesgos por entidad | Muestra información de resumen de clasificación de riesgos residuales para la entidad de negocios seleccionada y sus descendientes. Un informe de acceso a los detalles muestra detalles de los riesgos. |
| Clasificación de riesgo por categoría | Detalle de clasificación de riesgos por categoría | Muestra información de resumen de clasificación de riesgos residuales y de categorías de riesgo para la entidad de negocios seleccionada. Un informe de acceso a los detalles muestra detalles de los riesgos. |
| Riesgos principales |  | Muestra un resumen de los principales riesgos clasificados por exposición de riesgo residual y también muestra la exposición de riesgo inherente.<br>De forma predeterminada, los campos de evaluación cuantitativos no están incluidos en las siguientes soluciones, por lo que es posible que este informe no resulte adecuado para los usuarios de estas soluciones:<br>• IBM OpenPages Gestión de políticas<br>• IBM OpenPages Financial Controls Management<br>• IBM OpenPages IT Governance |

### Informes de control

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-control)

Los informes de control de están disponibles en las soluciones de IBM OpenPages® . Los usuarios pueden profundizar en algunos informes para obtener más detalles.

**Tabla 1. Informes de control**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Matriz de riesgo y control |  | Muestra datos de riesgo y de control para la entidad de negocios y los procesos especificados. |
| Gráfica de la eficacia de control | Detalle de efectividad de control | Muestra recuentos de controles agrupados por procesos y eficacia operativa. Un informe detallado contiene más detalles. |

### Informes de prueba

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-testing)

Los informes de prueba están disponibles en las soluciones de IBM OpenPages® . Los usuarios pueden profundizar en ellos para obtener más detalles.

**Tabla 1. Informes de pruebas**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Pruebas de rendimiento y resultados | Detalles de las pruebas | Este informe de varias pestañas muestra una representación visual de los resultados de la prueba, incluidos los resultados de las pruebas realizadas por el estado de prueba y los resultados de las pruebas realizadas a lo largo del tiempo.<br>Un informe de acceso a detalles muestra los planes de prueba, los resultados y las tendencias. |

### Informes de indicador

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-indicator)

La elaboración de informes es la fase final del ciclo de indicadores clave de riesgo (KRI) o de indicadores clave de rendimiento (KPI). Después de que el propietario define los KRI o los KPI, y captura sus valores, se suministran los informes de indicador estándar para ofrecer información de resumen de las entidades de negocios seleccionadas.

En la tabla siguiente se describen los informes de Indicador disponibles en las soluciones IBM OpenPages® Operational Risk Management, IBM OpenPages Policy Managementy IBM OpenPages IT Governance . Los usuarios pueden profundizar en ellos para obtener más detalles.

**Tabla 1. Informes de indicadores**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Panel KRI | Detalle del panel KRI | Muestra información de resumen del KRI relativa a la entidad de negocios seleccionada y sus descendientes. Un informe de acceso a detalles muestra información detallada. |
| Panel KPI | Detalle del panel KPI | Muestra información de resumen del KPI relativa a la entidad de negocios seleccionada y sus descendientes. Un informe de acceso a detalles muestra información detallada. |

### Informes de eventos de pérdida

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-loss-event)

Los informes de eventos de pérdida garantizan que la información sobre eventos de pérdida se recopilará de forma coherente en la totalidad de la organización.

En la tabla siguiente se describen los informes de eventos de pérdida disponibles en IBM OpenPages® Operational Risk Management. Los usuarios pueden profundizar en algunos informes para obtener más detalles.

**Tabla 1. Informes de eventos de pérdidas**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Panel de control de eventos de pérdida consolidados | Detalles del panel de control de eventos de pérdida - Entidad<br>Detalles del panel de control de eventos de pérdida - Categoría | El panel de control de eventos de pérdida muestra datos de eventos de pérdida Las pestañas incluyen:<br>• Resumen de eventos de pérdida<br>• Eventos de pérdida por entidad<br>• Sucesos de pérdida por categoría<br>• Tendencia de eventos de pérdidas<br>• Análisis causal<br>Los informes de acceso a detalles muestran una lista de eventos o categorías. |
| Riesgo frente a pérdida |  | Muestra la pérdida neta anual de una entidad de negocios para una fecha especificada en comparación con la exposición al riesgo residual actual. |

### Informes de gestión de problemas y corrección

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-issue-management-remediation)

Los problemas son elementos que se identifican en relación con la infraestructura documentada. Se considera que afectan de forma negativa a la gestión y notificación de los riesgos de forma precisa.

En la tabla siguiente se describen los informes de gestión y remediación de problemas disponibles en IBM OpenPages® Operational Risk Management. Los usuarios pueden profundizar en algunos informes para obtener más detalles. Para usuarios de otras soluciones hay dos informes de plataforma: Lista de problemas y Elementos de acción y problemas.

**Tabla 1. Informes de gestión de problemas y corrección**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Panel de control de problemas de ORM | Detalle del panel de problemas | Muestra una representación gráfica del número de problemas por estado. El informe entra en el ámbito del objeto de entidad y del rango de fechas. |
| Elementos de acción y problemas de ORM |  | Variante del informe Detalle del panel de problemas. Muestra información de resumen sobre los elementos de acción asociados. |

### Informes de análisis de escenarios

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-scenario-analysis)

Los escenarios implican la cuantificación de sucesos significativos (impactos y frecuencias de eventos potenciales) que se pueden producir en una organización. El análisis captura los escenarios hipotéticos de pérdidas. Los informes de análisis de escenarios son la base de las revisiones de los escenarios existentes para cada unidad de negocio.

La tabla siguiente describe los informes de análisis de escenario disponibles en IBM OpenPages® Operational Risk Management. Los usuarios pueden profundizar en ellos para obtener más detalles.

**Tabla 1. Informes de análisis de escenarios**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Resumen del escenario | Detalle de resultados de escenario | Muestra todos los escenarios por entidad. Los detalles incluyen el ID, la descripción, el estado y el propietario. |

### Informes de conformidad reguladora

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-regulatory-compliance)

En la tabla siguiente se describen los informes de conformidad normativa disponibles en IBM OpenPages® Policy Management. Los usuarios pueden profundizar en algunos informes para obtener más detalles.

**Tabla 1. Informes de conformidad reguladora**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Eficacia de control de proceso por mandato | Eficacia de control de proceso por submandato | Para una entidad de negocios seleccionada, el informe muestra mandatos asociados con el % de controles efectivos asociados con los procesos. Un informe de acceso a detalles muestra información detallada. |
| Matriz de aplicabilidad del reglamento |  | Muestra una vista de matriz de los mandatos y de las entidades de negocios a los que se aplican. |

### Informes de activos de TI

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-it-asset)

La tabla siguiente describe los informes de activos de TI disponibles en IBM OpenPages® IT Governance.

**Tabla 1. Informes de activos de TI**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Línea base |  | Muestra atributos clave de la línea base seleccionada, junto con los requisitos asociados y las actividades de control y procedimientos de prueba recomendados. |
| Plan de control |  | Muestra los atributos clave del objeto del sistema seleccionado, junto con las líneas base asociadas, sus requisitos y las actividades de control y procedimientos de prueba recomendados e implementados. |

### Informes de conformidad de TI

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-it-compliance)

La tabla siguiente describe los informes de conformidad de TI disponibles en IBM OpenPages® IT Governance. Los usuarios pueden profundizar en algunos informes para obtener más detalles.

**Tabla 1. Informes de conformidad de TI**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Eficacia de control de TI por mandato | Eficacia de control de TI por submandato | Para una entidad de negocios seleccionada, el informe muestra mandatos asociados con el% de controles efectivos asociados a sistemas. Un informe de acceso a detalles muestra información detallada.<br>El informe analiza los controles del entorno operativo de TI que se comparten entre los mandatos y las líneas base en el entorno operativo de TI. Ofrece una vista de la efectiva del control operativo por mandato. Un subinforme accede a los detalles del mandato seleccionado para mostrar la eficacia del control operativo por submandato. El otro subinforme muestra los detalles del mandato seleccionado para mostrar los resultados de la prueba agrupados por activo (tipo=aplicación). Este informe proporciona una vista de la conformidad de cada aplicación. Este informe se ejecuta siempre desde el entorno operativo de TI (filtra la entidad de negocios de biblioteca). |
| Biblioteca de requisitos |  | Para los requisitos seleccionados, el informe muestra todas las leyes y regulaciones aplicables.<br>Informa de la jerarquía desde los requisitos que se ajustan al ámbito de la solicitud hasta los submandatos y mandatos que satisface cada uno de esos requisitos. Esto demuestra que cumplir este único requisito satisface muchas leyes. El informe tiene una sola página por requisito y mandatos asociados. Este informe se ejecuta desde la biblioteca. |
| Biblioteca de requisitos del UCF |  | Para los controles armonizados del UCF, el informe muestra todos los documentos de la autoridad aplicables. |

### Informes de administración de auditoría

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-audit-management)

La tabla siguiente describe los informes de gestión de auditoría disponibles en IBM OpenPages® Internal Audit Management. Los usuarios pueden profundizar en algunos informes para obtener más detalles.

**Tabla 1. Informes de administración de auditoría**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Universo de auditoría |  | Para la organización de auditoría seleccionada, este informe muestra las entidades auditables, además de la clasificación de riesgos y los resultados de auditorías anteriores.<br>El ámbito se define por entidad de negocios y los usuarios pueden elegir el orden de clasificación. Si la entidad de negocios seleccionada se encuentra en la jerarquía empresarial de auditoría interna, el informe muestra la parte del universo de auditoría que es propiedad de ese equipo de auditoría interna. Si la entidad de negocios se encuentra dentro de la jerarquía organizativa, el informe muestra los elementos del universo de auditoría que están asociados con esa entidad de negocios o cualquier entidad de negocios descendiente. Este informe se utiliza en las fases de planificación anual tempranas para determinar qué elementos del universo de auditoría se auditarán este año. |
| Plan de auditoría | Detalle del plan de auditoría | Para la organización de auditoría seleccionada y el rango de fechas, este informe proporciona una vista de gráfica de GANTT de la planificación de la auditoría.<br>Con el ámbito de la entidad empresarial, el estado y el rango de fechas, un usuario puede elegir visualizar información por días, semanas, meses o trimestres. El rango de fechas seleccionado muestra el plan de año actual, un plan de 3 o 5 años o un periodo de tiempo de planificación. Al visualizar el informe, puede pulsar **Mostrar detalles** para ver los detalles de cada auditoría planificada para cada entidad auditable. Pulse **Ocultar detalles** para ver un resumen de las auditorías de cada entidad auditable. Si la fecha de inicio y final programadas de la auditoría y la fecha se solapan con una celda, la celda entera se resaltará. Las celdas de resumen que se muestran en color rojo indican que se ha programado más de una auditoría durante ese tiempo para la entidad auditable. |
| Plan de auditor | Detalle del plan de auditor | Para la organización de auditoría seleccionada, los auditores y el rango de fechas, este informe proporciona una vista de gráfica de GANTT de las planificaciones.<br>El ámbito se define por entidad de negocios, auditor y rango de fechas, se puede mostrar información por días, semanas, meses o trimestres. Los auditores disponibles son aquellos asociados con la entidad de negocios seleccionada o sus descendientes. El rango de fechas seleccionado muestra la planificación anual actual o un intervalo de tiempo de planificación. Al ver el informe, podrá alternar entre la vista detallada (muestra los detalles de cada planificación de cada auditor) y la vista resumida (muestra solo un resumen de las planificaciones de cada auditor). Si un auditor se programa para más de una planificación en una determinada columna, la celda entera se resaltará. Las celdas de resumen que se muestran en color rojo indican que se ha asignado más de una planificación durante ese tiempo al auditor. El informe no utiliza la información de Porcentaje asignado en el plan para determinar si hay un conflicto. |
| Descripción general de auditoría | • Detalle de hallazgos de la auditoría<br>• Detalle de problemas de auditoría<br>• Detalle de comentarios de la revisión de auditoría | Para la auditoría seleccionada, consulte del estado de sus secciones e informes de trabajo y vistas de las conclusiones, problemas y comentarios de revisión de auditoría asociados.<br>Si se define el ámbito por auditoría, el informe incluye las conclusiones, los problemas y los comentarios de revisión que son elementos secundarios directos de la auditoría, las secciones y los informes de trabajo. Al hacer clic en el número de problemas, conclusiones o comentarios de revisión de auditoría, se iniciará un informe detallado, con más detalles y enlaces a los objetos de la aplicación. |
| Informe de auditoría interna |  | Informe completo de la auditoría asociada, incluidos un resumen ejecutivo y conclusiones y problemas asociados.<br>El ámbito se define por entidad auditable y después por auditoría. Incluye conclusiones asociadas con auditorías, secciones de auditoría e informes de trabajo y los problemas asociados con la auditoría. |
| Desviación de auditoría |  | Para la auditoría seleccionada, vista de sus planes y secciones de auditoría, incluida información sobre planificaciones y presupuestos, con las desviaciones significativas resaltadas.<br>Este informe enumera los planes y las secciones de la auditoría seleccionada. Incluye información sobre planificaciones y presupuestos y las desviaciones significativas aparecen resaltadas. Las celdas que se muestran en color amarillo indican que falta información esencial. Las celdas que se muestran en color rojo indican una desviación no favorable de la planificación de más de un 20 %. El ámbito se define por entidad auditable y después por auditoría. Incluye la auditoría seleccionada y los planes y secciones de auditoría asociados directamente con la auditoría. |
| Desviación del auditor |  | Para los auditores seleccionados, vista de sus fechas, horas y gastos reales y previstos.<br>El ámbito se define por entidad de negocios de auditores, auditor y rango de fechas. Los auditores disponibles son aquellos asociados con la entidad de negocios seleccionada o sus descendientes. El rango de fechas seleccionado proporciona la posibilidad de ver un periodo de tiempo determinado. El informe muestra los planes de cada auditor seleccionado, incluidas las fechas iniciales y finales programadas, previstas y reales, así como el número de horas planificadas para cada uno y el número de horas reales en la hoja de registro horario, así como la cantidad de tiempo y gastos planificados y reales registrados para cada plan durante cada período de tiempo. Las celdas que se muestran en color rojo indican que están un 20 % o más por encima de las cantidades planificadas. Incluye todos los planes en los que el auditor ha sido seleccionado; las planificaciones que no tienen asignado un auditor no se incluyen en este informe. El informe incluye una fila de resumen para cada auditor y para todo el informe. Está en formato HTML de forma predeterminada y también se encuentra disponible en formato de Microsoft Excel. |
| Panel de hojas de registros horarios de auditor |  | Para los auditores seleccionados, consulte el estado de sus hojas de registro horario durante un número de semanas anteriores a la fecha seleccionada.<br>El Auditor líder y los Gestores de auditoría pueden utilizar este panel para monitorizar a los auditores que no envían las horas y para saber si las métricas de recursos están actualizadas. Pueden entrar y ver los detalles de una semana sobre un auditor determinado. |
| Panel de utilización de auditor |  | Para los auditores seleccionados y un año seleccionado, puede ver la utilización del auditor.<br>Los Gestores de auditoría pueden utilizar este panel para asegurarse de que están utilizando de forma óptima los recursos de auditor, y también para garantizar que los auditores no estén sobrecargados de trabajo. |
| Panel de aprobaciones de hoja de registro horario pendientes |  | Para los auditores seleccionados, consulte las hojas de registro horario pendientes de aprobación durante un número seleccionado de semanas anteriores a la fecha seleccionada.<br>El Responsable de la aprobación de la hoja de registro horario, el Auditor líder y el Gestor de auditorías pueden utilizar este panel para supervisar las entradas de registro horario pendientes. Pueden acceder a niveles más internos para obtener más información. |
| Asistente de entrada de hoja de registro horario |  | Consulte [Ayudante de entrada de hoja de registro horario](#asistente-de-entrada-de-hoja-de-registro-horario). |
| Asistente de aprobación de hoja de registro horario |  | Consulte [Ayudante de aprobación de hoja de registro horario](#asistente-de-aprobación-de-hoja-de-registro-horario). |

### Informes de cuestionario

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-questionnaire)

En la tabla siguiente se describen los informes de cuestionario.

**Tabla 1. Informes de cuestionario**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Informe de programa |  | Para un programa seleccionado, el informe muestra la puntuación global, el progreso del cuestionario y el resumen de respuestas por sección. |
| Informe de evaluación único |  | Para una evaluación de cuestionario seleccionada, el informe muestra las secciones, preguntas y respuestas. |

### Informes de gestión de controles financieros

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-financial-controls-management)

La tabla siguiente describe los informes de FCM.

**Tabla 1. Informes de FCM**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Ámbito de cuenta por entidad y clasificación |  | Muestra objetos de cuenta por entidad de negocios y clasificación. El informe incluye los valores de los campos Tipo de cuenta, Saldo, Porcentaje anual y En ámbito. |
| Certificación de control - Informe de resumen de proceso |  | Muestra un resumen del estado de certificación de los controles clave que dan soporte al proceso.<br>Enlace encontrado en el campo en la vista Proceso. |
| Informe Resumen de estado de certificación de control | Acceso a detalles de la certificación de control | Muestra el estado de certificación de control de claves filtrado por Entidad empresarial, Año y Trimestre.<br>Se encuentra en el panel de control de certificación de FCM y en el panel de control de maestro de FCM |
| Informe de problemas y acciones de FCM |  | Muestra una lista de problemas y acciones correspondientes y puede filtrarse por Entidad empresarial y Tipo de problema.<br>Se encuentra en el panel de control de certificación de FCM y en el panel de control de maestro de FCM |
| Correlación de cuentas y procesos de FCM |  | Los usuarios pueden elegir la correlación de relaciones de proceso y/o cuenta para visualizarla en el informe.<br>Por ejemplo, los usuarios pueden ver cuentas que están en el ámbito y no están asociadas a procesos junto con procesos que están en el ámbito y no están asociados a cuentas. |
| Informe de resumen de SOX (FCM - Informe de certificación de control de proceso) |  | Muestra un resumen del estado de la certificación de controles y procesos por trimestre, filtrado por entidad empresarial, control de claves (Y/N) y número de certificaciones previas (trimestrales).<br>Se encuentra en el panel de control de certificación de FCM y en el panel de control de maestro de FCM |

### Informes de gestión de riesgos para ESG

`Guía de soluciones › Informes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=reports-risk-management-esg)

La tabla siguiente describe los informes disponibles en IBM OpenPages® Risk Management for ESG. Los usuarios pueden profundizar en algunos informes para obtener más detalles.

**Tabla 1. Gestión de riesgos para informes ESG**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Panel de control de objetivos | Informe de acceso a detalles de panel de control de objetivos | Este informe es un panel de control interactivo de varias pestañas IBM® Cognos® Analytics que permite a una organización revisar el estado actual de los objetivos, la priorización y el progreso frente al objetivo.<br>El informe de acceso a detalles muestra una tabla de objetivos. |
| Listado de objetivos |  | Este informe de lista muestra una tabla de objetivos, que se filtran por entidad, estado de objetivo y estado de progreso. Este informe incluye enlaces de seguimiento cruzado a la vista Tarea para cada objetivo. |
| Panel de control KRI de objetivo |  | Este informe se filtra por objetivo y muestra una descripción y un gráfico de tendencias para todos los indicadores clave de riesgo asociados. |
| Panel de control de conformidad de ESG | Conformidad por acceso a detalles de mandato | Este informe es un panel de control interactivo de varias pestañas IBM Cognos Analytics que permite a una organización ver su estado de conformidad ESG. |
| Detalles de cumplimiento normativo y estándar de ESG |  | Este informe muestra detalles sobre submandatos y requisitos para un mandato seleccionado. |

Si utiliza IBM OpenPages Risk Management for ESG y la integración de Supply Wisdom junto con IBM OpenPages Risk Management for ESG, están disponibles los siguientes informes adicionales:

**Tabla 2. Gestión de riesgos para ESG con Supply Wisdom informes**

| Nombre | Informe de acceso a detalles | Descripción |
| --- | --- | --- |
| Lista de proveedores-Clasificaciones ESG | Obtención de detalles de proveedor de ESG | Este informe de lista detallada muestra las valoraciones de ESG para los proveedores seleccionados, que se filtran por nombre de proveedor.<br>El informe de acceso a detalles muestra datos clave de evaluaciones de Supply Wisdom ESG e incluye enlaces de seguimiento cruzado con el proveedor. |
| Comparación de proveedores-ESG |  | Este informe muestra las valoraciones de ESG de Supply Wisdom para dos proveedores. El informe incluye un filtro para seleccionar los proveedores para la comparación. |
| Postura de proveedor-Calificaciones de ESG |  | Este informe se filtra por proveedor y muestra los riesgos de Supply Wisdom ESG asociados del proveedor en varios formatos (Radar, Cross Tab y Trend Line chart). |

## Activadores

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-triggers)

Las soluciones de IBM OpenPages® incluyen varios desencadenantes.

IBM OpenPages ha introducido las características GRC Workflow y GRC Calculations que permiten a una organización actualizar y sustituir sus implementaciones actuales de desencadenantes.

Los activadores que funcionan actualmente en el entorno siguen funcionando. Sin embargo, su organización debe realizar un plan de transición de desencadenantes a una funcionalidad basada en las características GRC Workflow y GRC Calculations .

Para obtener más información, consulte:

- [Cálculos de ejemplo](#cálculos-de-ejemplo)
- [flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo)
- *Configuración de GRC Calculations* en la publicación *IBM OpenPages Guía del administrador*
- *Configuración de GRC Workflow en la publicación IBM OpenPages Guía del administrador*

Los desencadenantes que se han sustituido por flujos de trabajo y cálculos ya no están habilitados de forma predeterminada en instalaciones nuevas de OpenPages. Para obtener más información sobre estos desencadenantes, consulte [Desencadenantes heredados](#activadores-heredados).

La tabla siguiente lista los activadores incluidos y habilitados con cada solución de forma predeterminada.

**Tabla 1. Desencadenantes en IBM OpenPages soluciones**

| Desencadenante | TPRM | RCM | MRG | FCM | ORM | PCM | ITG | IAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Autoevaluaciones de riesgo y control (desencadenantes y cálculos)](#autoevaluaciones-de-riesgo-y-control-desencadenantes-y-cálculos) | X | X |  | X | X | X | X | X |
| [Activadores de ciclo de vida de control](#activadores-de-ciclo-de-vida-de-control) | X | X |  | X | X | X | X | X |
| [Activador de importación de políticas](#activador-de-importación-de-políticas) |  |  |  |  |  | X |  |  |
| [Activador de bloqueo de políticas](#activador-de-bloqueo-de-políticas) |  |  |  |  |  | X |  |  |
| [Activador de cálculos de clasificación de riesgos de la auditoría](#activador-de-cálculos-de-clasificación-de-riesgos-de-la-auditoría) |  |  |  |  |  |  |  | X |
| [Activador de automatización de cierre de auditoría](#activador-de-automatización-de-cierre-de-auditoría) |  |  |  |  |  |  |  | X |
| [Desencadenante de tarjeta de puntuación de riesgo de modelo](#desencadenante-de-tarjeta-de-puntuación-de-riesgo-de-modelo)<br>**Nota:** Este desencadenante está inhabilitado de forma predeterminada. El cálculo de la tarjeta de puntuación de riesgo del modelo sustituye al desencadenante. |  |  | X |  |  |  |  |  |
| [Activador Tipo de cambio](#activador-tipo-de-cambio) |  |  |  |  | X |  |  |  |

> **Nota:** Estos desencadenantes están diseñados para funcionar con la configuración predeterminada de OpenPages. Cualquier cambio en la configuración, como por ejemplo campos, listas de selección dependientes y dependencias de campo, puede afectar a cómo o si los desencadenantes y ayudantes funcionan tal como se han diseñado.

### Tipos de objeto que contienen activadores

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-object-types-that-contain)

Para poder utilizar la herramienta ObjectManager para cargar los datos de instancias XML, inhabilite los activadores en cualquier tipo de objeto para el que desee cargar datos.

En la tabla siguiente se listan los tipos de objeto para los que se han incluido activadores de forma predeterminada.

**Tabla 1. Tipos de objeto que contienen desencadenantes en IBM OpenPages soluciones**

| Tipo de objeto | TPRM | RCM | MRG | FCM | ORM | PCM | ITG | IAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Riesgo | X | X | X | X | X | X | X | X |
| Control | X | X | X | X | X | X | X | X |
| Archivo (SOXDocument) |  |  |  |  |  | X |  |  |
| Política |  |  |  |  |  | X |  |  |
| Auditoría |  |  |  |  |  |  |  | X |
| Comentario de revisión de auditoría |  |  |  |  |  |  |  | X |
| Sección de auditoría |  |  |  |  |  |  |  | X |
| Conclusión |  |  |  |  |  |  |  | X |
| Plan |  |  |  |  |  |  |  | X |
| Hoja de registro horario |  |  |  |  |  |  |  | X |
| Documento de trabajo |  |  |  |  |  |  |  | X |
| Tarjeta de puntuación de riesgo modelo<br>**Nota:** Este desencadenante está inhabilitado de forma predeterminada en instalaciones nuevas. |  |  | X |  |  |  |  |  |

### Autoevaluaciones de riesgo y control (desencadenantes y cálculos)

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-risk-control-self-assessments-calculations)

El proceso de evaluaciones de riesgos se utiliza para identificar, evaluar y cuantificar el perfil de riesgo de una empresa. Cada riesgo se evalúa sobre una base cuantitativa o cualitativa.

Los cálculos y los desencadenantes proporcionan el flujo de trabajo de proceso para la Autoevaluación de riesgos y control del negocio.

Habilite el método cualitativo o cuantitativo:

- Si desea evaluar los riesgos utilizando el método cualitativo, habilite los cálculos de valoración cualitativa del riesgo de auditoría y de valoración cualitativa del riesgo e inhabilite los cálculos de valoración cuantitativa del riesgo de auditoría y de valoración cuantitativa del riesgo.

  Cuando se guarda un riesgo, el cálculo de valoración cualitativa del riesgo cifra la valoración cualitativa del riesgo inherente y la valoración cualitativa del riesgo residual en función de las claves y valores de registro definidos en los objetos de preferencia.
- Si desea evaluar los riesgos utilizando el método cuantitativo, habilite los cálculos de evaluación cuantitativa del riesgo de auditoría y de valoración cuantitativa del riesgo e inhabilite los cálculos de valoración cualitativa del riesgo de auditoría y de valoración cualitativa del riesgo.

  Cuando se guarda un riesgo, el cálculo de valoración cualitativa del riesgo cifra la valoración cuantitativa del riesgo inherente y la valoración cuantitativa del riesgo residual en función de las claves y valores de registro definidos en los objetos de preferencia.

Los siguientes activadores se utilizan para las evaluaciones de riesgos y autocontrol:

- Evaluación de riesgo Crear
- Evaluación de riesgos Actualizar
- Desencadenante de creación de envío de aprobación de riesgo

  Cuando Enviar para su aprobación se establece en Y en un objeto de riesgo, el desencadenante actualiza el campo Estado del riesgo y todos los controles asociados de Pendiente de evaluación a Pendiente de aprobación, establece el estado del proceso en Pendiente de evaluación y envía un correo electrónico al propietario del proceso.
- Desencadenante de actualización de envío de aprobación de riesgo
- Desencadenante de creación de aprobación de control de riesgo

  Cuando se establece Aprobar/Rechazar para Aprobar un riesgo, el desencadenante comprueba si todos los riesgos de un proceso están aprobados. Si es así, el desencadenante cambia el Estado de proceso a Aprobado y envía un correo electrónico al coordinador de RCSA. Si no, no se cambia el estado del proceso.
- Actualización de la aprobación de control de riesgo

El desencadenante RCSA cuantitativa y el desencadenante RCSA cualitativa ya no están habilitados en instalaciones nuevas. Para obtener más información, consulte [Desencadenantes cuantitativos y cualitativos de RCSA (legado)](#desencadenantes-de-rcsa-cuantitativas-y-rcsa-cualitativas-existente).

### Activadores de ciclo de vida de control

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-control-lifecycle)

Los activadores proporcionan las transiciones que mueven controles durante un ciclo de vida de atestación. Los ciclos de vida definen las fases que puede seguir un objeto. En cada fase, el sistema:

- Identifica un responsable del ciclo de vida
- Define las acciones disponibles para moverse a una fase diferente
- Envía automáticamente un correo electrónico al nuevo responsable de ciclo de vida
- Define otros atributos que están relacionados con la fase actual

El ciclo de vida para controles utiliza las fases siguientes:

- Nuevo
- En curso
- Atestación
- Cerrado

Cuando se crea un control, el sistema establece el ciclo de vida en la nueva fase y envía un correo al primer responsable de ciclo de vida. Cuando el usuario completa la tarea, el activador mueve el objeto a la tarea siguiente y al usuario siguiente. Un usuario puede añadir un comentario con cada transición. Las transiciones tienen lugar cuando los usuarios abren un objeto de control en la vista de tarea y pulsan **Acción > `<transition name>`**. La etapa determina la transición que se visualiza.

La tabla siguiente resume cómo el sistema maneja los controles y establece el asignado de ciclo de vida. La columna Transición contiene el nombre de **Ciclo de vida > `<transition name>`** en la vista de tarea de control que un usuario pulsa para desencadenar la transición a la siguiente etapa.

**Tabla 1. Proceso de ciclo de vida y propietarios de la etapa en los controles**

| Etapa | Responsable de ciclo de vida | Transición | Etapa siguiente | Estado siguiente |
| --- | --- | --- | --- | --- |
| Nuevo | Propietario del control | **Iniciar** | En curso | En curso |
| En curso | Propietario del control | **Enviar para testificación** | Atestación | Testificando |
| Atestación | Control de notario | **Devolver** | En curso | Testificación rechazada |
| Atestación | Control de notario | **Testificación** | Cerrado | Cerrado |
| Cerrado | (sin asignar) | **Reabrir** | En curso | Reabierto |

#### Notificación de control

La notificación de control envía un correo electrónico a un asignado de ciclo de vida cuando se crea un control y para cada transición del ciclo de vida del control. Una transición se produce cuando un usuario pulsa un icono de transición **Acción** > **Iniciar**, **Enviar para testificación**, **Enviar atrás**, **Attest**o **Volver a abrir**) en la vista de tarea de control.

El activador de ciclo de vida de control inicia la notificación de control. La notificación de correo electrónico contiene la etapa, el estado, la fecha de vencimiento, comentarios y un enlace al control.

### Activador de importación de políticas

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-policy-import-trigger)

El desencadenante de importación de políticas importa contenido de políticas y procedimientos de un documento estructurado de Microsoft Word a los campos de políticas y procedimientos de IBM OpenPages® analizando las distintas secciones del documento. Se inicia al comprobar un archivo adjunto del objeto Política.

El activador admite el enfoque híbrido de la gestión de políticas. También admite la actualización del número de versión del enfoque centrado en documentos cuando se incorpora un nuevo documento de política. Como parte del proceso de importación, el activador realiza también una validación pormenorizada para asegurarse de que la estructura del documento Word se ajusta a la plantilla de política definida.

OpenPages o el cliente puede configurar este componente para que se comporte para la metodología de cliente a través de los valores de texto de registro y aplicación.

El desencadenante de importación de políticas IBM OpenPages Gestión de políticas tiene las siguientes limitaciones conocidas:

- Las listas con viñetas solo admiten el formato de viñeta de disco y de círculo.
- Las listas numeradas solo admiten decimales, caracteres alfabéticos en mayúscula, caracteres alfabéticos en minúscula, números romanos en mayúscula y números romanos en minúscula.
- No se admiten fuentes de símbolos. Puede utilizar la opción **Insertar símbolo** y seleccionar un símbolo utilizando una fuente normal (por ejemplo, el símbolo de copyright).
- La fuente Wingding no es compatible.
- No se puede establecer sombreado desde el menú **Shading** (Sombreado). Método alternativo: utilice el resaltado de texto para lograr un efecto similar. (solo .doc)
- No se mostrará el valor de un FORMDROPDOWN. (solo .doc)
- Las listas ordenadas utilizan siempre un punto como separador. Por ejemplo, si un elemento de la lista del documento Word se muestra como «“1)”» se convertirá en «“1.”»
- Para `.doc`, el estilo del marcador de elemento de lista se deducirá del contenido de texto de la lista. La familia de fuentes del marcador y el tamaño de la fuente coincidirán con la primera parte del texto en el elemento de lista. El marcador será negrita, cursiva y/o coloreado si el texto entero del elemento de la lista tiene el mismo estilo.
- Las imágenes, WordArt y los diagramas no son compatibles.
- No admite la importación de una tabla de contenidos.
- Todos los estilos de subrayado se muestran como una línea sólida.
- No son compatibles los superíndices o los subíndices definidos con un estilo (solo .doc). Solución: Aplique los subíndices y los superíndices desde el menú Fuente en lugar de utilizar un estilo.
- El formateo resuelve el conflicto con los estilos personalizados. Por ejemplo, si el estilo personalizado incluye un formato de texto Strong y el usuario le elimina la negrita del texto manualmente dentro del documento, el texto se mostrará en negrita por el estilo Strong. (solo `.doc`)
- Las pestañas tienen 4 espacios como valor predeterminado. Esto no garantiza que se ajuste al espacio del documento porque las pestaña se basan en su posición en el documento. Se recomienda utilizar el sangrado al alinear el contenido.
- No se garantiza que la sangría francesa (es decir las sangrías de primera línea) se alinee perfectamente, debido a la diferente anchura de los marcadores de los elementos de línea.
- Dentro de las listas, mezclar distintas técnicas para crear viñetas, listas y sangrías suele dar como resultado que los elementos no se alineen correctamente y que la numeración de los elementos sea incorrecta.
- Si se introducen varios retornos de carro para crear espacios no se traducirán en espacio extra.
- Características no admitidas:

  - Cambios en la dirección del texto
  - Doble tachado
  - Relieve, grabado y texto sombreado
  - Efectos de texto
  - Marcas de énfasis
  - Espaciado de texto personalizado
  - Bordes sombreados
  - Bordes de celda diagonales ascendentes

### Activador de bloqueo de políticas

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-policy-lock-trigger)

El activador de bloqueo de políticas bloquea la política o la política y sus componentes (procedimientos, archivos adjuntos, comentarios de revisiones de políticas) en distintos puntos del proceso de revisión y aprobación. Este activador admite los tres enfoques de la gestión de política: centrado en datos, híbrido y centrado en documentos.

El activador de bloqueo de políticas admite dos casos de uso:

- Bloqueo de archivos adjuntos de política para respaldar una política que se coloca en el ciclo de revisión y aprobación y garantizar que el contenido de la política no se pueda modificar durante las aprobaciones. (Se puede aplicar a los enfoques híbrido y centrado en documentos.)
- Bloqueo de la jerarquía completa del borrador de la política (política, procedimientos, archivos adjuntos y comentarios de revisiones de políticas) una vez que se ha otorgado la aprobación final a la política y está lista para su publicación. (Se puede aplicar a los tres enfoques de la política.)

El cliente puede configurar este componente para que se comporte según su metodología utilizando los ajustes del registro y de texto de la aplicación.

### Activador de cálculos de clasificación de riesgos de la auditoría

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-audit-risk-rating-computations-trigger)

El activador de cálculos de clasificación de riesgos de la auditoría calcula y mantiene los valores del campo de clasificación de riesgos residuales e inherentes de la auditoría en el objeto de riesgo.

El activador RCSA cuantitativas y RCSA cualitativas se aplican al activador de cálculos de clasificación de riesgos de la auditoría.

### Activador de automatización de cierre de auditoría

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-audit-close-automation-trigger)

El activador de automatización de cierre de auditoría evalúa la preparación para el cierre de cada componente configurado de una auditoría. El activador está configurado, de forma predeterminada, para los siguientes tipos de objeto: Auditoría, Sección de auditoría, Informe de trabajo, Conclusión, Comentario de revisión de auditoría, Planificación y Hoja de registro horario.

Cuando se crea o actualiza una instancia de un tipo de objeto configurado, el activador evalúa todos los criterios que se han configurado para ese tipo de objeto. Si se han cumplido todos los criterios, el activador establece el valor del campo Preparado para cierre en Sí. Este valor de campo se utiliza por el asistente de cierre de auditoría para determinar si todos los componentes de la auditoría están listos para el cierre.

Las categorías de criterios de listo para el cierre configuradas incluyen campos que son necesarios, campos de fecha que se deben establecer en la fecha del día en curso o anterior a él, campos de fecha que deben configurarse con una fecha igual o anterior a otros campos de fecha, y campos de usuario que no se pueden configurar igual que otros campos de usuario.

### Desencadenante de tarjeta de puntuación de riesgo de modelo

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-model-risk-scorecard-trigger)

El desencadenante del objeto de tarjeta de puntuación de riesgo de modelo calcula las puntuaciones que se utilizan para asignar un nivel a un modelo. Las tablas de puntuación de riesgo de modelo forman parte de IBM OpenPages® Model Risk Governance.

> **Nota:** Este desencadenante está inhabilitado de forma predeterminada. El cálculo de la tarjeta de puntuación de riesgo del modelo sustituye al desencadenante

El desencadenante del objeto de tarjeta de puntuación de riesgo de modelo se evalúa si se crea una tarjeta de puntuación de riesgo de modelo o si se actualizan los campos de entrada de puntuación. El desencadenante calcula puntuaciones y puntuaciones ponderadas para cada entrada y calcula una puntuación y una puntuación ponderada para cada categoría de entrada. Finalmente, el desencadenante calcula una puntuación global y asigna un nivel al modelo basado en la puntuación global. El desencadenante se configura en los valores de registro y utiliza ponderaciones y otros valores en los registros de preferencia cuyo Tipo está establecido en MRG.

### Activador Tipo de cambio

`Guía de soluciones › Activadores` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-exchange-rate-trigger)

El activador de tipo de cambio vuelve a calcular el valor de campo de moneda especificado utilizando el tipo de cambio más cercano basado en el campo de fecha configurado, en lugar del último tipo de cambio cargado en el sistema.

En Eventos de pérdida, el valor de Pérdida bruta estimada se actualiza en función del tipo de cambio más próximo a la fecha de descubrimiento.

Para Impactos de pérdidas, los valores de Pérdida estimada y Pérdida real se actualizan en función del tipo de cambio más próximo a la fecha de incidencia.

Para Recuperación de pérdidas, los valores de Importe de recuperación estimado e Importe de recuperación se actualizan en función del tipo de cambio más próximo a la fecha de recepción.

El campo `Trigger Run` sobre impactos de pérdidas y recuperaciones de pérdidas no es tenido en cuenta por el desencadenante de tipo de cambio. Si está establecido en No, el activador Tipo de cambio se sigue ejecutando.

Puede habilitar e inhabilitar el desencadenante de tipo de cambio. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Configuración**, y luego edite el **Soluciones** > **ORM** > **Disparadores** > **Eventos de pérdida** > **Ajustador de tipos de cambio**. El valor predeterminado es true (habilitado).

## Perfiles

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=sg-profiles)

Las soluciones de IBM OpenPages® incluyen uno o más perfiles.

Cada solución tiene un perfil principal, que se denomina perfil *Master*. Algunas soluciones incluyen perfiles adicionales. Cada perfil incluye los siguientes elementos preconfigurados, que pueden ser modificados por un administrador:

- Tipos de objeto
- Campos y grupos de campos
- Vistas
- Panel de control
- Filtros
- Informes (si están disponibles)

Algunas soluciones incluyen más perfiles, que son subconjuntos del perfil maestro.

**Tabla 1. Perfiles**

| Solución | Perfiles |
| --- | --- |
| IBM OpenPages Data Privacy Management | • **OpenPages DPM Master**<br>• **encargado de datos de DPM**: este perfil es para los usuarios técnicos de Data Privacy Management, incluidos los encargados de datos e ingenieros de datos.<br>• **Oficial de privacidad de DPM**: este perfil es para los usuarios de Data Privacy Management en roles relacionados con la conformidad y el riesgo de la privacidad. |
| IBM OpenPages Business Continuity Management | • **OpenPages BCM Master**<br>• **Usuario final de BCM**: este perfil proporciona acceso de sólo lectura a los empleados que necesitan ver los planes de continuidad de negocio dentro de la solución Business Continuity Management.<br>• **BCM Supply Wisdom Master*** |
| IBM OpenPages Third Party Risk Management | • **OpenPages VRM Master**<br>• **VRM Vendor Manager**: este perfil está pensado para usuarios que son responsables de gestionar proveedores.<br>• **Proveedor de VRM**: este perfil está pensado para proveedores. El perfil les da acceso a un conjunto limitado de tipos de objeto como, por ejemplo, Cuestionario.<br>• **OpenPages RapidRatings Maestro***<br>• **VRM RiskRecon Maestro***<br>• **VRM Security Scorecard Master***<br>• **VRM Supply Wisdom Master***<br>Durante el proyecto de implementación se pueden crear más perfiles, por ejemplo, para un propietario de proceso, un comprobador de control y otros usuarios. |
| IBM OpenPages Regulatory Compliance Management | • **OpenPages RCM Master**<br>• **RCM Ascent Master***<br>• **RCM Reg-Track Master***<br>• **RCM TRRI Master***<br>• **RCM WK Master*** |
| IBM OpenPages Model Risk Governance | • **OpenPages MRG Master**<br>• **MRG Model Owner**: este perfil está pensado para desarrolladores de modelos y propietarios de modelos. Los usuarios asignados a este perfil tienen acceso a las vistas de tareas específicas de MRG en los tipos de objeto compartido Entidad empresarial y Preferencia.<br>• **MRG Model Validation**: este perfil está pensado para validadores y revisores de modelos. Los usuarios asignados a este perfil tienen acceso a las vistas de tareas específicas de MRG en los tipos de objeto compartido Entidad empresarial y Preferencia. |
| IBM OpenPages Financial Controls Management | • **OpenPages FCM Master**<br>• **FCM Certification V2**: este perfil está diseñado para usuarios que participan activamente en el proceso de revisión y subcertificación.<br>• **FCM Master V2**: este perfil está diseñado para usuarios que están involucrados en la subcertificación o tienen un rol de supervisión en el proceso de subcertificación. |
| IBM OpenPages Operational Risk Management | • **OpenPages ORM Master**<br>• **ORM Operational Risk Team**: este perfil está pensado para un usuario avanzado que utiliza la mayoría de las funciones de OpenPages pero que no necesita acceso de lectura a los ID de biblioteca y a los campos de estado de objeto.<br>Un usuario de este perfil puede:<br>• Mantener procesos<br>• Gestionar bibliotecas de riesgo y control<br>• Determinar el ámbito de RCSA<br>• Ejecutar y supervisar el proceso de RCSA<br>• Administrar, revisar y supervisar eventos de pérdida<br>• Definir y capturar indicadores de riesgo clave (KRI)<br>• Gestionar el cierre de problemas y acciones<br>• Coordinar análisis de escenarios<br>• **ORM Business User**: este perfil incluye los campos y las configuraciones que un gestor de riesgos necesita para utilizar en las operaciones del negocio. Este usuario es un participante activo en la mayoría de las actividades de gestión de riesgos operativos.<br>Un usuario con este perfil puede:<br>• Registrar un evento de pérdida<br>• Determinar el ámbito de RCSA<br>• Aprobar evaluaciones de riesgos<br>• Capturar KRI<br>• Gestionar el cierre de problemas y acciones<br>• Participar en talleres de escenario<br>• **ORM Simplified User**: este perfil permite a un usuario centrarse en eventos de pérdida, captura de valor de KRI y gestión de problemas.<br>• **OpenPages FIRST Loss**: este perfil está diseñado para facilitar la carga de los datos de pérdida FIRST en OpenPages utilizando FastMap.<br>Los usuarios con este perfil pueden editar todos los campos de los objetos FIRST Loss para que dichos datos se puedan cargar. Asigne este perfil a los usuarios responsables de cargar los datos de pérdida FIRST a través de FastMap. Otorgue a todos los demás usuarios acceso de solo lectura a los objetos de pérdida FIRST.<br>Tenga en cuenta que no es necesario asignar este perfil a un usuario. En su lugar, puede configurar la hoja de cálculo de importación de FastMap para utilizar el perfil de **OpenPages FIRST Loss**. |
| IBM OpenPages Gestión de políticas | • **OpenPages PCM Master**<br>• **PCM End User**: este perfil tiene acceso de solo lectura y está pensado para los empleados que necesitan ver políticas y procedimientos.<br>Se pueden crear más perfiles, por ejemplo para un gestor de programas de conformidad, el responsable de privacidad y otros usuarios durante el proyecto de implementación. |
| IBM OpenPages IT Governance | • **OpenPages ITG Master**<br>Los subconjuntos de este perfil que son adecuados para un administrador de bibliotecas de TI, director de TI y otros usuarios se pueden crear durante el proyecto de implementación.<br>• **ITG RiskLens Maestro*** |
| IBM OpenPages Internal Audit Management | **OpenPages IAM Master**<br>Los subconjuntos de este perfil que son adecuados para un auditor principal, director de auditoría y otros usuarios se pueden crear durante el proyecto de implementación. |
| IBM OpenPages Gestión de riesgos para ESG | • **OpenPages ESG Master**<br>• **OpenPages ESG Supply Wisdom Master*** |

\* Estos perfiles solo están disponibles si el entorno incluye la configuración para el canal de información de datos relacionado.

El superadministrador (`OpenPagesAdministrator`) tiene acceso a los perfiles siguientes de forma predeterminada:

- OpenPages Modules Master (ya incluido)
- OpenPages BCM maestro
- OpenPages DPM Master
- OpenPages ESG maestro
- OpenPages FCM Master V2
- OpenPages IAM Master
- OpenPages ITG maestro
- OpenPages MRG Master
- OpenPages Maestro ORM
- OpenPages Maestro PCM
- OpenPages Maestro RCM
- OpenPages VRM Master

## Plantillas de funciones

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-role-templates)

Una plantilla de rol define los privilegios que se otorga a un usuario. Las soluciones de IBM OpenPages® incluyen varias plantillas de funciones. Las plantillas de roles dan permisos a la aplicación y conceden acceso a características y funciones. También proporcionan ACL de objeto (RWDA).

Cuando se asignan derechos de permiso a una plantilla de rol de solución, dichos derechos también se asignan a la plantilla **Maestro de módulos - Todos los permisos**.

De forma predeterminada, se incluyen dos plantillas de rol con la mayoría de las soluciones. La plantilla denominada «“Todos los permisos”» proporciona permisos y derechos administrativos para todos los tipos de objeto que están disponibles para la solución. La plantilla denominada «“Todos los datos - Administración limitada”» proporciona permisos para todos los tipos de objeto que están disponibles para la solución, pero no proporciona derechos administrativos. Algunas soluciones incluyen plantillas de rol adicionales que incluyen un subconjunto de permisos.

Para obtener más información sobre los permisos proporcionados con plantillas de funciones, consulte [Permisos de plantilla de funciones](#permisos-de-plantillas-de-funciones).

### Lista de plantillas de funciones

`Guía de soluciones › Plantillas de funciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-list-role)

Las soluciones de IBM OpenPages® incluyen varias plantillas de funciones.

Se suministran las siguientes plantillas de funciones con las soluciones:

**Tabla 1. Plantillas de funciones**

| Nombre | Descripción |
| --- | --- |
| Maestro de módulos - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos habilitados de forma predeterminada para todas las soluciones. Derechos de administración completos. |
| Maestro de módulos - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos habilitados de forma predeterminada para todas las soluciones. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| [BCM] - Assignee | Acceso R/W/A a la mayoría de objetos de BCM predeterminados. Participante en Proceso de continuidad de negocio. |
| [BCM] - BC End User | Acceso de lectura (R) a objetos del plan de continuidad de negocio. Empleado que busca acceder a los planes de continuidad de negocio relevantes. |
| [BCM] - BC Manager | Acceso R/W/D/A a todos los objetos BCM predeterminados. Gestor de los estándares de planificación del equipo de continuidad de negocio centralizado y de la agregación de planes de todo el mundo de forma centralizada. |
| [BCM] - BC Owner | Acceso R/W/D/A a la mayoría de los objetos BCM predeterminados. Propietario de negocio del plan de continuidad de negocio y su ejecución. |
| [BCM] - BCP Approver | Acceso R/W/A a la mayoría de objetos de BCM predeterminados. Aprobador de planes de continuidad de negocio. |
| [BCM] - BCP Author | Acceso R/W/A a la mayoría de objetos de BCM predeterminados. Autor del plan de continuidad de negocio relativo. |
| [BCM] - BCP Focal | Acceso R/A a todos los objetos BCM predeterminado. Ejecutivo de nivel de unidad de negocio donde se aplica plan. |
| [BCM] - BCP Reviewer | Acceso R/W/A a la mayoría de objetos de BCM predeterminados. Revisor de planes de continuidad de negocio. |
| DPM - Todos los datos - Administración limitada | Acceso completo de L/G/D/A a todos los objetos DPM predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| DPM - Todos los permisos | Acceso completo de L/G/D/A a todos los objetos DPM predeterminados. Derechos de administración completos. |
| ESG-Todos los datos-Administración limitada | Acceso completo R/W/D/A a todos los objetos ESG predeterminados. Permisos de rol adicionales limitados a: Archivos, Publicación. |
| ESG-Todos los permisos | Acceso completo R/W/D/A a todos los objetos ESG predeterminados. Derechos de administración completos. |
| FCM - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de FCM predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| FCM - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de FCM predeterminados. Derechos de administración completos. |
| FCM - Certificaciones | Utilizado por roles implicados en actividades de certificación, por ejemplo, propietarios de procesos o propietarios de control.<br>Los derechos de acceso de lectura, escritura, asociación y supresión se otorgan a los objetos necesarios para la certificación de FCM SOX, por ejemplo, Control, Evaluación de control, proceso, Evaluación de proceso, Riesgo, Archivo, Problema y algunos objetos FCM.<br>La mayoría de los permisos de aplicación de administración no se otorgan. |
| IAM - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de IAM predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| IAM - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de IAM predeterminados. Derechos de administración completos. |
| ITG - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de ITG predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| ITG - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de ITG predeterminados. Derechos de administración completos. |
| Entrada de evento de pérdida | Plantilla de funciones utilizada por la aplicación Entrada de evento de pérdida. |
| MRG - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de MRG predeterminados. Derechos de administración limitados. |
| MRG - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de MRG predeterminados. Derechos de administración completos. |
| MRG - Propietario/desarrollador de modelo | Utilizada por los propietarios y desarrolladores de modelos.<br>Esta plantilla de funciones es similar a la plantilla de funciones Gestión de riesgos de modelo, excepto que no se otorga acceso de escritura sobre el objeto Revisión.<br>La mayoría de los permisos de aplicación de administración no se otorgan. |
| MRG - Gestión de riesgos de modelo | Utilizada por los gestores de riesgos de modelo (segunda línea de defensa).<br>Se otorgan derechos de acceso de lectura, escritura y asociación sobre los tipos de objeto de MRG. El acceso de escritura se deniega a los dos tipos de objeto compartidos, Preferencia y Entidad de negocios.<br>La mayoría de los permisos de aplicación de administración no se otorgan. No se otorga acceso de supresión a ningún tipo de objeto. |
| MRG - Validación de modelo | Utilizada por los usuarios de validación del modelo.<br>Los derechos de acceso de lectura, escritura y asociación se otorgan a un subconjunto de tipos de objeto MRG que incluyen Modelo, Caso de uso de modelo, Revisión, Solicitud de cambio y Reto. Se deniega el acceso de escritura a otros tipos de objeto de MRG. Se deniega el acceso de escritura a los tipos de objeto compartidos, Preferencia y Entidad de negocios.<br>La mayoría de los permisos de aplicación de administración no se otorgan. No se otorga acceso de supresión a ningún tipo de objeto. |
| MRG- AI Factsheets -Acceso de API | Plantilla de roles limitada para que AI Factsheets acceda a la API de OpenPages . |
| ORM - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de ORM predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| ORM - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de ORM predeterminados. Derechos de administración completos. |
| [ORM] Usuario empresarial | Plantilla de funciones de ORM para usuarios que registran eventos de pérdida, realizan RCSA, aprueban evaluaciones de riesgos, capturan KRI, gestionan el cierre de problemas y acciones y participan en talleres de escenario. |
| [ORM] Equipo de riesgo operativo | Plantilla de funciones de ORM para usuarios que mantienen bibliotecas de proceso, riesgo y control, establecen el ámbito de RCSA, ejecutan y supervisan el proceso de RCSA, llevan a cabo la administración de eventos de pérdida, definen y capturan KRI, gestionan el cierre de problemas y acciones y coordinan talleres de escenario. |
| [ORM] Usuario simplificado | Plantilla de funciones de ORM para los usuarios que necesitan un acceso mínimo para su trabajo en eventos de pérdida, captura de valores de KRI y gestión de problemas. |
| PCM - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de PCM predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| PCM - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de PCM predeterminados. Derechos de administración completos. |
| PCM End User | Acceso de lectura (R). Para los empleados que necesitan ver políticas y procedimientos. |
| RCM - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de RCM predeterminados. Ningún derecho de administración excepto aquellos asociados a flujos de trabajo, archivos y carpetas. |
| RCM - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de RCM predeterminados. Derechos de administración completos. |
| RCM - Suscriptor | Acceso de lectura a todos los objetos de RCM predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| TPRM RapidRatings -Todos los permisos | Acceso R/W/D/A completo a todos los objetos TPRM y objetos RapidRatings Ratings predeterminados. Derechos de administración completos. |
| TPRM RapidRatings -Todos los datos-Administración limitada | Acceso R/W/D/A completo a todos los objetos TPRM y objetos RapidRatings Ratings predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| VRM - Todos los datos - Administración limitada | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de TPRM predeterminados. Sin derechos de administración excepto los asociados con flujos de trabajo, archivos y carpetas. |
| VRM - Todos los permisos | Acceso completo R/W/D/A (lectura/escritura/supresión/asociación) a todos los objetos de TPRM predeterminados. Derechos de administración completos. |

### Permisos de plantillas de funciones

`Guía de soluciones › Plantillas de funciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-role-template-permissions)

Cada plantilla de funciones define permisos de acceso que se habilitan para cada tipo de objeto.

Para cada solución, se proporciona una plantilla de funciones denominada Todos los permisos. Incluye derechos de administrador completos. También proporciona acceso completo de lectura, escritura, supresión y asociación (RWDA) a todos los tipos de objeto que están incluidos en la solución.

Además, cada solución incluye una plantilla de rol denominada Todos los datos - Administración limitada. La plantilla no proporciona ningún derecho de administrador salvo los tipos de objeto asociados con archivos y carpetas. Las plantillas proporcionan acceso completo de lectura, escritura, supresión y asociación a todos los tipos de objeto habilitados de forma predeterminada para la solución. Para obtener más información sobre los permisos de acceso que se otorgan a los tipos de objeto en las plantillas de funciones, consulte [Permisos de tipo de objeto asignados por plantillas de funciones](#permisos-de-tipo-de-objeto-asignados-por-plantilla-de-funciones).

### Permisos de tipo de objeto asignados por plantilla de funciones

`Guía de soluciones › Plantillas de funciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=templates-object-type-permissions-assigned-by-role)

Una plantilla de funciones define el acceso de lectura, escritura, supresión y asociación a los tipos de objeto habilitados en cada solución.

Cuando se asignan derechos de permiso a una plantilla de rol, dichos derechos también se asignan a la plantilla Maestro de módulos.

Los permisos siguientes describen los derechos asignados a los tipos de objeto en las plantillas de funciones:

**Tabla 1. Permisos de tipo de objeto**

| Permiso | Nombre | Descripción |
| --- | --- | --- |
| R | Leer | Se otorga a los grupos o usuarios el derecho a examinar y ver los detalles de los objetos. |
| W | Escribir | Se otorga a los grupos o usuarios el derecho a crear o modificar objetos en la carpeta seleccionada. No pueden eliminar los objetos. |
| D | Suprimir | Se otorga a los grupos o usuarios el derecho a suprimir objetos en la estructura de carpetas. |
| A | Asociar | Se otorga a los grupos o usuarios el derecho a crear asociaciones entre objetos. |

## Cálculos de GRC

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-grc-calculations)

Los cálculos de ejemplo se proporcionan con OpenPages® para empezar a utilizar la característica GRC Calculations .

### Cálculos de ejemplo

`Guía de soluciones › Cálculos de GRC` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=calculations-sample)

Puede utilizar los cálculos de ejemplo como se han proporcionado, o bien modificarlos para que cumplan sus requisitos. También se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios cálculos.

Los cálculos de ejemplo están habilitados en instalaciones nuevas. En función del método de evaluación seleccionado durante el proceso de instalación, se han habilitado los cálculos de clasificación de riesgo cuantitativo y de clasificación de riesgo de auditoría cuantitativa o la clasificación de riesgo cualitativa y la clasificación de riesgo de auditoría cualitativa.

Los cálculos de ejemplo siguientes se incluyen en OpenPages®:

- Evento de pérdida

  Calcula la pérdida neta, el importe de recuperación, la pérdida bruta y la pérdida bruta estimada basándose en la recuperación de pérdida y el impacto de pérdida subyacentes. Si la suma de la pérdida real es 0, utiliza la pérdida en bruta estimada.
- Clasificación de riesgos de la auditoría cualitativa

  Calcula automáticamente la clasificación de riesgo inherente de la auditoría cualitativa y la clasificación de riesgo residual de la auditoría cualitativa en función de los objetos de preferencia y las claves de registro definidas.
- Clasificación de riesgo cualitativa

  Calcula automáticamente la clasificación de riesgo inherente cualitativa y la clasificación de riesgo residual cualitativa en función de los objetos de preferencia y las claves de registro definidas.
- Clasificación de riesgos de la auditoría cuantitativa

  Calcula automáticamente la clasificación de riesgo inherente de la auditoría cuantitativa y la clasificación de riesgo residual de la auditoría cuantitativa en función de los objetos de preferencia y las claves de registro definidas.
- Clasificación de riesgos cuantitativa

  Calcula automáticamente la clasificación de riesgo inherente cuantitativa y la clasificación de riesgo residual cuantitativa en función de los objetos de preferencia y las claves de registro definidas.
- CIA de recursos

  Calcula el nivel de importancia de los recursos basándose en la marca límite superior para CIA.
- Tendencia de TPRM Supply Wisdom

  Calcula la valoración de riesgo global de un proveedor, basándose en las puntuaciones trimestrales de Supply Wisdom. Compara la valoración de riesgo global actual con las calificaciones de trimestres anteriores para determinar la tendencia.

#### Cálculos de KRI y KPI

Estos cálculos de KRI y KPI son utilizados por múltiples soluciones.

- KRIValue - Aumento, KRIValue - Disminución

  Estos cálculos automáticos se aplican a los valores de KRI con un KRI padre en un estado Activo, con cálculos separados aplicados en función de si el campo Información de dirección del KRI padre se establece como «“Aumento significa mayor riesgo”» o «“Disminución significa mayor riesgo.”» El cálculo identifica el umbral amarillo, el umbral rojo y la información de dirección del KRI padre y establece estos campos en el valor de KRI. El cálculo establece el estado de la infracción en el valor de KRI basado en la entrada del campo Valor en el registro de valor de KRI comparado con los umbrales amarillo y rojo.
- Aumento de KRI, disminución de KRI

  Estos cálculos automáticos se aplican a KRI en un estado Activo, con cálculos separados aplicados en función de si el campo Información de dirección se establece en «“Aumento significa mayor riesgo”» o «“Disminución significa mayor riesgo.”» El cálculo trae los campos Valor de los valores de KRI en un estado de recopilación de «“Recopilado”» que están relacionados con el KRI. El cálculo clasifica los valores en orden descendente por valor de fecha y compara los dos últimos valores. A continuación, el cálculo establece el campo Tendencia de indicador en el KRI comparando los dos valores que son más recientes en el tiempo. A continuación, establece el campo Valor en el KRI basándose en el valor del KRI con la última fecha de valor en el tiempo y utiliza esta misma entrada para determinar el estado de incumplimiento del KRI comparando el valor con los umbrales amarillo y rojo en el KRI.
- Siguiente fecha de recopilación de KRI

  Este cálculo automático se aplica a los KRI en un estado Activo. El cálculo establece la Siguiente fecha de recopilación añadiendo días a la Siguiente fecha de recopilación de KRI basada en el campo Frecuencia en el KRI y la Fecha de recopilación prevista en los valores de KRI relacionados.
- Indicador clave de riesgo

  Este cálculo automático establece la última fecha de valor de un valor KRI en el KRI principal. El cálculo también establece el estado de recopilación de KRI en función del estado de recopilación del valor de KRI con la fecha de valor más reciente.
- Cálculos de KPI

  Los cálculos siguientes están relacionados con los objetos de KPI y del valor de KPI y son similares a los cálculos del valor de KRI y KRI:

  - KPI
  - KPI - Disminuir
  - KPI – Aumentar
  - Siguiente fecha de recopilación de KPI
  - KPIValue - Disminución
  - KPIValue - Aumento

#### Cálculos de IBM OpenPages Operational Risk Management (ORM)

Estos cálculos determinan la próxima fecha de vencimiento de prueba si se produce una prueba de control en una base planificada y se lleva la información de resultado de prueba más reciente al objeto Plan de prueba padre.

- Plan de pruebas

  Este cálculo automático establece la última fecha de realización de un resultado de prueba al plan de pruebas padre. El cálculo también establece el estado del plan de pruebas basado en el estado de resultado de prueba hijo con la fecha de realización más reciente. El cálculo clasifica los valores de Resultado de prueba en orden descendente por Fecha de realización y compara los dos últimos resultados. A continuación, el cálculo establece el campo Tendencia en el plan de pruebas comparando los dos resultados que son más recientes en el tiempo.
- Fecha de vencimiento de pruebas

  Descripción: este cálculo automático establece la fecha de vencimiento del plan de pruebas añadiendo días a la última fecha de vencimiento del resultado de la prueba basada en el campo Frecuencia del plan de pruebas (diaria, semanal, mensual o anual) y la fecha de inicio prevista del plan de pruebas.

#### Cálculos de IBM OpenPages Business Continuity Management (BCM)

- **Análisis de impacto empresarial**

  - Impacto basado en el tiempo de BIA

    Este cálculo automático realiza las operaciones siguientes:

    1. Establece un peso para cada evaluación de impacto (financiero, legal/regulador, de reputación y operativo)
    2. Convierte el valor enum en un valor numérico (Devastador = 5; Grave = 4, Significativo = 3, Moderado = 2; Menor = 1) para cada periodo de tiempo evaluado (a las 24 horas, a los 3 días, a los 7 días, después de 7 días)
    3. Establece la puntuación de impacto para cada evaluación de impacto añadiendo los valores enum convertidos y multiplicando por el peso proporcionado
    4. Establece una medida del impacto global añadiendo todas las puntuaciones de evaluación de impacto
    5. Establece el MAO calculado y el nivel de impacto calculado en función de la puntuación de impacto global.
  - Puntuación del trimestre del periodo de máxima actividad de BIA

    Este cálculo automático anota cada selección de enumeración (Alto = 3, Elevado = 2, Normal = 1) y establece el trimestre correspondiente en Alto, Mediano o Bajo basado en la selección para los meses de ese trimestre. Si la puntuación combinada de los tres meses del trimestre es mayor o igual a 8, se selecciona Alto; si la puntuación es entre 7 y 5, se selecciona Elevado; y si se selecciona 3 o 4, se selecciona Normal.
  - Puntuación de BIA de continuidad de negocio

    Determina la puntuación de impacto mediante el uso de requisitos, impactos financieros y de reputación. Utiliza la puntuación del impacto para determinar el nivel de impacto y la interrupción máxima aceptable.

    Este cálculo está inhabilitado de forma predeterminada. El cálculo de impacto basado en el tiempo de BIA sustituye al cálculo de puntuación de BIA de continuidad de negocio.
  - BIA - Estado de vulneración

    Este cálculo automático tiene en cuenta el estado de vulneración de todos los KPI hijo que se correlacionan con el registro de análisis de impacto empresarial. El cálculo cuenta cada uno de estos estados de vulneración de KPI y establece el campo Estado de vulneración de indicador clave de rendimiento en el objeto Análisis de impacto empresarial.

    - Si el cálculo identifica al menos un estado de vulneración de KPI de color rojo, el estado de vulneración de KPI se establece en rojo.
    - Si el cálculo no identifica ningún KPI relacionado con un estado de vulneración rojo y al menos uno amarillo, el estado de vulneración del KPI del BIA se establece en amarillo.
    - Si el cálculo no identifica ningún KPI relacionado con un estado de vulneración de color rojo o amarillo y al menos un KPI con un estado de vulneración de color verde, el estado de vulneración del KPI del BIA se establece en verde.
    - Si el estado de vulneración de un KPI relacionado no es igual a rojo, amarillo o verde, el campo Estado de vulneración del KPI de BIA se establece como «“No aplicable.”»

    Los valores rojos y amarillos del estado de vulneración de los KPI se muestran en el panel de control maestro de BCM para identificar los BIA que podrían requerir una actualización basada en el rendimiento medido por los KPI asignados.

- **Impulsar y comparar métricas de BIA**

  - Proceso-BCM

    Este cálculo es un cálculo automático que establece los campos Nivel de impacto, Medida del impacto, RTO, RPO y MAO en el Proceso basándose en las métricas más críticas establecidas en un BIA hijo.

    El cálculo utiliza los campos que se establecen como parte de la última etapa de los flujos de trabajo de Evaluación de impacto empresarial inicial y Revisión de BIA recurrente para asegurarse de que solo los campos que están completamente aprobados dentro del BIA se utilizan para establecer campos en un proceso relacionado.

    Este cálculo establece el campo Duración de tolerancia al impacto de un servicio empresarial padre que se clasifica como un servicio empresarial importante en el proceso.

    Este cálculo también establece el valor de campo Aviso de alineación de objetivo de tiempo de recuperación y Aviso de alineación de objetivo de punto de recuperación en «“Aviso”» en el objeto Proceso, si se cumplen determinadas condiciones. El valor de campo Aviso de alineación de objetivo de tiempo de recuperación de «“Aviso”» se establece cuando una tolerancia de impacto totalmente aprobada (de un servicio empresarial relacionado) es inferior al objetivo de tiempo de recuperación o al tiempo de recuperación o cuando el tiempo de recuperación excede el objetivo de tiempo de recuperación. El valor del campo Aviso de alineación de objetivo de punto de recuperación de «“Aviso”» se establece cuando el objetivo de punto de recuperación es menor que el punto de recuperación.
  - Recurso-BCM

    Este cálculo automático establece y compara los campos que se derivan de un proceso padre. El cálculo establece los campos Nivel de impacto, Puntuación de impacto, Objetivo de tiempo de recuperación de proceso, Objetivo de punto de recuperación de proceso y MAO del proceso con las métricas más críticas en el objeto Activo (Resource). Este cálculo establece los valores de los campos Aviso de alineación de RTO y Aviso de alineación de RPO en «“Aviso”» en el objeto Activo, si se cumplen determinadas condiciones. El valor del campo Aviso de alineación de objetivo de tiempo de recuperación de «“Aviso”» se establece cuando el objetivo de tiempo de recuperación de procesos es menor que el objetivo de tiempo de recuperación de recursos o el tiempo de recuperación o cuando el tiempo de recuperación excede el objetivo de tiempo de recuperación de recursos. El valor del campo Aviso de alineación de objetivo de punto de recuperación de «“Aviso”» se establece cuando el objetivo de punto de recuperación de procesos es menor que el objetivo de punto de recuperación de recursos o punto de recuperación o cuando el punto de recuperación excede el objetivo de punto de recuperación de recursos.
  - Proveedor-BCM

    Este cálculo automático establece y compara los campos que se derivan de un proceso padre. El cálculo establece los campos Nivel de impacto, Medida del impacto, Objetivo de tiempo de recuperación de procesos, Objetivo de punto de recuperación de procesos y MAO del proceso con las métricas más críticas del objeto de proveedor. Este cálculo establece los valores de campo Aviso de alineación de objetivo de tiempo de recuperación y Aviso de alineación de objetivo de punto de recuperación en «“Aviso”» en el objeto Proveedor, si se cumplen determinadas condiciones. El valor del campo Aviso de alineación de objetivo de tiempo de recuperación de «“Aviso”» se establece cuando el objetivo de tiempo de recuperación de procesos es menor que el objetivo de tiempo de recuperación de proveedor o el tiempo de recuperación o cuando el tiempo de recuperación excede el objetivo de tiempo de recuperación de proveedor. El valor del campo Aviso de alineación de objetivo de punto de recuperación de «“Aviso”» se establece cuando el objetivo de punto de recuperación de procesos es menor que el objetivo de punto de recuperación de proveedor o punto de recuperación o cuando el punto de recuperación excede el objetivo de punto de recuperación de proveedor.

- **Resiliencia operativa**

  - KRI - Métrica de tolerancia al impacto

    Este cálculo automático establece el valor de la medida de tolerancia al impacto en «“Sí”» para cualquier KRI que tenga un servicio empresarial padre que esté clasificado como un servicio empresarial importante.
  - Proceso - Estado de vulneración de tolerancia al impacto

    Este cálculo automático tiene en cuenta el estado de vulneración de todos los KRI relacionados con el proceso en el que la métrica de tolerancia al impacto = «“Sí.”» El cálculo cuenta cada uno de estos estados de vulneración de indicador clave de riesgo y establece el campo Estado de vulneración de tolerancia al impacto en el proceso. Si el cálculo identifica al menos un estado de vulneración de indicador clave de riesgo de color rojo, el estado de vulneración de tolerancia al impacto de procesos se establece en rojo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo y al menos uno amarillo, el estado de vulneración de la tolerancia al impacto de procesos se establece en amarillo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo o amarillo y al menos uno con un estado de vulneración verde, el estado de vulneración de tolerancia al impacto de procesos se establece en verde. Si un estado de vulneración de un indicador clave de riesgo relacionado no es igual a rojo, amarillo o verde, o el indicador clave de riesgo no tiene un valor de Métrica de tolerancia al impacto = «“Sí”», el campo se establece en «“No Aplicable.”»

    Los valores rojo y amarillo para el estado de vulneración de tolerancia al impacto se utilizan en los filtros públicos para identificar las posibles dependencias de servicios empresariales que pueden estar en conflicto dentro de las vistas de asociación en SysView-Task-BusService-5 y en el panel de control maestro de BCM.
  - Ubicación - Estado de vulneración de tolerancia al impacto

    Este cálculo automático tiene en cuenta el estado de vulneración de todos los KRI relacionados con la ubicación en la que la métrica de tolerancia al impacto = «“Sí.”» El cálculo cuenta cada estado de vulneración de KRI y establece el campo Estado de vulneración de tolerancia al impacto en la ubicación. Si el cálculo identifica al menos un estado de vulneración de indicador clave de riesgo de color rojo, el estado de vulneración de tolerancia al impacto de ubicación se establece en rojo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo y al menos uno amarillo, el estado de vulneración de la tolerancia al impacto de ubicación se establece en amarillo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo o amarillo y al menos un KRI con un estado de vulneración verde, el estado de vulneración de la tolerancia al impacto de la ubicación se establece en verde. Si un estado de vulneración de un indicador clave de riesgo relacionado no es igual a rojo, amarillo o verde, o el indicador clave de riesgo no tiene un valor de Métrica de tolerancia al impacto = Sí, el campo se establece en «“No Aplicable”».

    Los valores rojo y amarillo para el estado de vulneración de tolerancia al impacto se utilizan en los filtros públicos para identificar las posibles dependencias de servicios empresariales que pueden estar en conflicto dentro de las vistas de asociación en `SysView-Task-BusService-5` y en el panel de control maestro de BCM.
  - Recurso - Estado de vulneración de tolerancia al impacto

    Este cálculo automático tiene en cuenta el estado de infracción de todos los KRI relacionados con el activo donde Métrica de tolerancia de impacto = «“Sí”». El cálculo cuenta cada estado de infracción de KRI y establece el campo Estado de infracción de tolerancia de impacto en el activo. Si el cálculo identifica al menos un estado de vulneración de indicador clave de riesgo de color rojo, el estado de vulneración de tolerancia al impacto de recursos se establece en rojo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo y al menos uno amarillo, el estado de vulneración de la tolerancia al impacto de recursos se establece en amarillo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo o amarillo y al menos uno con un estado de vulneración verde, el estado de vulneración de tolerancia al impacto de recursos se establece en verde. Si un estado de vulneración de un indicador clave de riesgo relacionado no es igual a rojo, amarillo o verde, o el indicador clave de riesgo no tiene un valor de Métrica de tolerancia al impacto = «“Sí”», el campo se establece en «“No Aplicable.”»

    Los valores rojo y amarillo para el estado de vulneración de tolerancia al impacto se utilizan en los filtros públicos para identificar las posibles dependencias de servicios empresariales que pueden estar en conflicto dentro de las vistas de asociación en SysView-Task-BusService-5 y en el panel de control maestro de BCM.
  - Proveedor - Estado de vulneración de tolerancia al impacto

    Este cálculo automático tiene en cuenta el estado de vulneración de todos los KRI relacionados con el proveedor en el que la métrica de tolerancia al impacto = «“Sí.”» El cálculo cuenta cada uno de estos estados de vulneración de indicador clave de riesgo y establece el campo Estado de vulneración de tolerancia al impacto en el proveedor. Si el cálculo identifica al menos un estado de vulneración de indicador clave de riesgo de color rojo, el estado de vulneración de tolerancia al impacto de proveedor se establece en rojo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo y al menos uno amarillo, el estado de vulneración de la tolerancia al impacto de proveedor se establece en amarillo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo o amarillo y al menos uno con un estado de vulneración verde, el estado de vulneración de tolerancia al impacto de proveedor se establece en verde. Si un estado de vulneración de un indicador clave de riesgo relacionado no es igual a rojo, amarillo o verde, o el indicador clave de riesgo no tiene un valor de Métrica de tolerancia al impacto = «“Sí”», el campo se establece en «“No Aplicable.”»

    Los valores rojo y amarillo para el estado de vulneración de tolerancia al impacto se utilizan en los filtros públicos para identificar las posibles dependencias de servicios empresariales que pueden estar en conflicto dentro de las vistas de asociación en SysView-Task-BusService-5 y en el panel de control maestro de BCM.
  - Servicio empresarial - Estado de vulneración

    Este cálculo automático tiene en cuenta el estado de vulneración de todos los KRI relacionados con el servicio empresarial. El cálculo cuenta cada uno de estos estados de vulneración de indicador clave de riesgo y establece el campo Estado de vulneración de tolerancia al impacto en el servicio empresarial. Si el cálculo identifica al menos un estado de vulneración de indicador clave de riesgo de color rojo, el estado de vulneración de tolerancia al impacto del servicio empresarial se establece en rojo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo y al menos uno amarillo, el estado de vulneración de la tolerancia al impacto del servicio empresarial se establece en amarillo. Si el cálculo no identifica ningún KRI relacionado con un estado de vulneración rojo o amarillo y al menos uno con un estado de vulneración verde, el estado de vulneración de tolerancia al impacto del servicio empresarial se establece en verde. Si el estado de vulneración de un KRI relacionado no es igual a rojo, amarillo o verde, el campo se establece como «“No aplicable.”»

    Los valores rojo y amarillo para el estado de vulneración de tolerancia al impacto se utilizan dentro de una regla de enumeración para `SysView-Task-BusService-5` para visualizar una vista de tarea para un servicio empresarial con una tolerancia al impacto que se aproxima a la vulneración o en vulneración. Los valores también se utilizan en el panel de control maestro de BCM.

#### Cálculos de IBM OpenPages Financial Controls Management

- **Ámbito de cuenta-Activos**

  Cuando el campo Clasificación del objeto Cuenta = Activos, este cálculo:

  - Calcula y establece el campo Porcentaje de valor anualizado del registro de cuenta basándose en la suma de todos los registros de objeto de cuenta con el mismo valor de clasificación y entidad de negocios padre.
  - Establece el campo Cuenta en ámbito basándose en un porcentaje de umbral.

- **Ámbito de cuenta-Equidad**

  Cuando el campo Clasificación del objeto Cuenta = Equidad, este cálculo:

  - Calcula y establece el campo Porcentaje de valor anualizado del registro de cuenta basándose en la suma de todos los registros de objeto de cuenta con el mismo valor de clasificación y entidad de negocios padre.
  - Establece el campo Cuenta en ámbito basándose en un porcentaje de umbral.

- **Ámbito de cuenta-Gastos**

  Cuando el campo Clasificación del objeto Cuenta = Gastos, este cálculo:

  - Calcula y establece el campo Porcentaje de valor anualizado del registro de cuenta basándose en la suma de todos los registros de objeto de cuenta con el mismo valor de clasificación y entidad de negocios padre.
  - Establece el campo Cuenta en ámbito basándose en un porcentaje de umbral.

- **Ámbito de cuenta-Pasivos**

  Cuando el campo Clasificación del objeto Cuenta = Pasivos, este cálculo:

  - Calcula y establece el campo Porcentaje de valor anualizado del registro de cuenta basándose en la suma de todos los registros de objeto de cuenta con el mismo valor de clasificación y entidad de negocios padre.
  - Establece el campo Cuenta en ámbito basándose en un porcentaje de umbral.

- **Ámbito de cuenta-Ingresos**

  Cuando el campo Clasificación del objeto Cuenta = Pasivos, este cálculo:

  - Calcula y establece el campo Porcentaje de valor anualizado del registro de cuenta basándose en la suma de todos los registros de objeto de cuenta con el mismo valor de clasificación y entidad de negocios padre.
  - Establece el campo Cuenta en ámbito basándose en un porcentaje de umbral.

- **Ámbito de cuenta-Desconocido**

  Cuando el campo Clasificación del objeto Cuenta = Desconocido, este cálculo:

  - Calcula y establece el campo Porcentaje de valor anualizado del registro de cuenta basándose en la suma de todos los registros de objeto de cuenta con el mismo valor de clasificación y entidad de negocios padre.
  - Establece el campo Cuenta en ámbito basándose en un porcentaje de umbral.

- **BE-Totales de clasificación de cuenta**

  Calcula campos en el objeto Entidad de negocios:

  - Calcula y establece los totales de los valores de campo Clasificación de objeto de cuenta relacionados para cada uno de los siguientes: Activo, Pasivo, Patrimonio Neto, Ingresos, Gastos y Desconocido.
  - Calcula un total combinado de todos los valores de campo Clasificación de objeto de cuenta.

- **Certificación de evaluación de control**

  Da soporte al proceso de subcertificación en IBM OpenPages Financial Controls Management.

- **Certificación de evaluación de proceso**

  Da soporte al proceso de subcertificación en IBM OpenPages Financial Controls Management.

#### Cálculos de IBM OpenPages Internal Audit Management

- **Presupuesto y planes de plan de auditoría de resumen**

  Calcula los campos siguientes para la vista de objeto Plan de auditoría de resumen: Bajo Más de horas, Horas de auditoría asignadas, Horas completadas y Horas restantes. Los valores de estos campos se suman a partir de los objetos Entidad auditable y Auditoría relacionados.

#### Cálculos deIBM OpenPages IT Governance

- **Activo-Calificación de vulnerabilidad**

  Este cálculo establece la calificación de evaluación de vulnerabilidades en el activo basándose en la vulnerabilidad abierta mejor calificada relacionada con el activo.

- **Sistema-Calificación de vulnerabilidad**

  Este cálculo establece la calificación de evaluación de vulnerabilidades en el sistema basándose en la vulnerabilidad abierta mejor calificada relacionada con el sistema o un activo relacionado.

- **Vulnerabilidad-Evaluación de amenazas**

  Este cálculo establece los campos Probabilidad global y Calificación de riesgo basándose en las entradas proporcionadas para los campos de evaluación de amenazas. La puntuación se basa en NIST SP 800-30 Rev. 1.

#### Cálculos deIBM OpenPages Model Risk Governance (MRG)

- Siguiente fecha de recopilación de métricas

  Establece automáticamente la siguiente fecha de recopilación para las métricas activas, basándose en la frecuencia de la métrica.

  > **Nota:** Este cálculo no es aplicable a las métricas de IBM Watson® OpenScale .
- Valor de métrica - Actualización desde métrica padre

  Establece la información de umbral y de dirección de la métrica padre y calcula el estado de vulneración de un valor de métrica.

  > **Nota:** Este cálculo no es aplicable a las métricas de IBM Watson OpenScale .
- Valor de métrica - Actualización

  Actualiza automáticamente las métricas activas con datos del valor de métrica hijo más reciente. También actualiza la tendencia de indicadores de métrica si hay más de un valor de métrica recopilado.
- Tarjeta de puntuación de riesgo modelo

  Calcula un nivel para un modelo que se puede utilizar para evaluar el nivel de riesgo de modelo. Por lo general, una organización establece un modelo mediante la evaluación de una serie de factores. IBM OpenPages Model Risk Governance utiliza los cuatro factores siguientes: Complejidad, Materialidad, Operativo y Regulador. El resultado es que cada Modelo está asignado al Nivel 1, Nivel 2 o Nivel 3. Este cálculo sustituye a un desencadenante que ha realizado el mismo nivel de niveles en versiones anteriores.

  > **Nota:** Este cálculo no es aplicable a los modelos de IBM Watson OpenScale .

#### Cálculos de IBM OpenPages Policy Management (PCM)

- Comentario de revisión de política

  Rellena la descripción de objeto de comentario de revisión de política (PRC) con el nombre de política. Esta información proporciona contexto a los usuarios cuando ven el objeto PRC en una vista de lista o de cuadrícula.

  Este cálculo es opcional. Puede inhabilitarlo, si es necesario.

#### Cálculos deIBM OpenPages Regulatory Compliance Management (RCM)

Estos cálculos agregan los datos de las evaluaciones de requisitos al tema de conformidad y el tema de conformidad con el plan de conformidad. Estas métricas calculadas pueden ayudar a los usuarios a realizar evaluaciones.

Las salidas de estos cálculos se almacenan dentro de los registros correspondientes de valor de evaluación de requisitos, valor de tema de conformidad y evaluación de plan de conformidad para el análisis de tendencias.

- Tema de conformidad - Evaluación de requisitos

  Este cálculo automático captura y establece campos en el objeto Evaluación de requisitos desde controles hijo. El cálculo cuenta todos los controles que se correlacionan con la evaluación de requisitos, los controles con una selección efectiva para la eficacia del diseño y los controles con una selección efectiva para la efectividad operativa. A continuación, el cálculo establece los campos Recuento de control, Recuento de DE efectivo y Recuento OE efectivo en la evaluación de requisitos. El cálculo también divide el recuento de controles calificados como eficaces para el diseño y la eficacia operativa del recuento de todos los controles y establece los campos Porcentaje de eficacia DE y Porcentaje de eficacia OE en la evaluación de requisitos.
- Tema de conformidad - Entidad empresarial

  El cálculo es aplicable a los temas de conformidad que están dentro de la jerarquía de entidades empresariales. El cálculo es un resumen de las evaluaciones de requisitos para establecer el número y el porcentaje de evaluaciones de requisitos que se calificaron como por encima del objetivo y en el objetivo para la eficacia del diseño y la eficacia operativa. El cálculo también establece la puntuación media para la eficacia del diseño, la eficacia operativa y una clasificación global para todas las evaluaciones de requisitos relacionadas que se calificaron como algo distinto de «“6 - No Aplicable.”» La puntuación media se determina puntuando y sumando cada valor enum de todas las evaluaciones de requisitos asociadas (1 - Por encima del objetivo = 1; 2 - En el objetivo = 2; 3 - Por debajo del objetivo = 3; 4 - Significativamente por debajo del objetivo = 4; y 5 - Ningún control pertinente = 5) y dividiendo esta puntuación total por el número de evaluaciones de requisitos con uno de los cinco valores enum listados. Una puntuación inferior indica un nivel superior de conformidad.
- Tema de conformidad - Biblioteca

  El cálculo es aplicable a los temas de conformidad que están dentro de la jerarquía de la biblioteca. El cálculo es un resumen de las evaluaciones de requisitos para establecer el número y el porcentaje de evaluaciones de requisitos que se calificaron como por encima del objetivo y en el objetivo para la eficacia del diseño y la eficacia operativa. El cálculo también establece la puntuación media para la eficacia del diseño, la eficacia operativa y una clasificación global para todas las evaluaciones de requisitos relacionadas que se calificaron como algo distinto de «“6 - No Aplicable.”» La puntuación media se determina puntuando y sumando cada valor enum de todas las evaluaciones de requisitos asociadas (1 - Por encima del objetivo = 1; 2 - En el objetivo = 2; 3 - Por debajo del objetivo = 3; 4 - Significativamente por debajo del objetivo = 4; y 5 - Ningún control pertinente = 5) y dividiendo esta puntuación total por el número de evaluaciones de requisitos con uno de los cinco valores enum listados. Una puntuación inferior indica un nivel superior de conformidad.

  Además, este cálculo cuenta el número de requisitos dentro del Tema de conformidad bajo evaluación y establece el campo Recuento de requisitos.
- Plan de conformidad

  De forma similar al cálculo de los temas de conformidad, el cálculo del plan de conformidad agrega puntuaciones proporcionadas en los temas de conformidad hijo. El cálculo es un resumen de los temas de conformidad para establecer el número y el porcentaje de los temas de conformidad que se calificaron como por encima del objetivo y en el objetivo para la eficacia del diseño y la eficacia operativa. El cálculo también establece la puntuación media para la eficacia del diseño, la eficacia operativa y una calificación global para todos los temas de conformidad relacionados que se calificaron como algo distinto de «“6 - No Aplicable.”» La puntuación media se determina puntuando y sumando cada valor enum de todos los temas de conformidad asociados (1 - Por encima del objetivo = 1; 2 - En el objetivo = 2; 3 - Por debajo del objetivo = 3; 4 - Significativamente por debajo del objetivo = 4; y 5 - Ningún control pertinente = 5) y dividiendo esta puntuación total por el número de temas de conformidad con uno de los cinco valores enum listados. Una puntuación inferior indica un nivel superior de conformidad. El cálculo también cuenta el número de temas de conformidad que se incluyen en el plan de conformidad.

#### Cálculos de IBM OpenPages Risk Management for ESG

- **Puntuación de prioridad de objetivo**

  Calcula una puntuación de prioridad objetivo.

  Obtiene los valores de los campos `Importance to Firm` y `Importance to Stakeholders` . Los valores son: Muy bajo = «“1”» , Bajo = «“2”», Medio = «“3”», Alto = «“4”», Muy alto = «“5”». A continuación, se añaden los dos valores para obtener la puntuación de prioridad de objetivo, que puede oscilar entre 2 y 10.

- **Progreso objetivo**

  Calcula la diferencia entre el Progreso del objetivo y el Objetivo objetivo. A continuación, el cálculo establece el campo Estado de progreso en **Bajo logro**, **Sobre logro**o **En destino**.

## GRC Workflow

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=guide-grc-workflow)

Se proporcionan flujos de trabajo de ejemplo con OpenPages® para empezar a utilizar la característica GRC Workflow .

### Flujos de trabajo de ejemplo

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-sample-workflows)

Puede utilizar los flujos de trabajo de ejemplo como se han proporcionado, o bien modificarlos para que cumplan sus requisitos. También se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

Los flujos de trabajo de ejemplo están habilitados en instalaciones nuevas.

- Flujo de trabajo Aprobación de elemento de acción
- Flujo de trabajo Conclusión
- Flujo de trabajo de incidente
- Flujo de trabajo Revisión de problema
- Flujos de trabajo de KRI y KPI
- Autoevaluación de riesgos y control (RCSA)
- Flujos de trabajo de pruebas de control
- Flujo de trabajo Revisión de evento de pérdida
- Flujo de trabajo Evaluación de cuestionario
- Flujo de trabajo Informe de trabajo
- [IBM OpenPages Business Continuity Management (BCM)](#flujos-de-trabajo-de-ibm-openpages-business-continuity-management-bcm)
- [IBM OpenPages Data Privacy Management (DPM)](#flujos-de-trabajo-de-ibm-openpages-data-privacy-management-dpm)
- [IBM OpenPages Financial Controls Management (FCM)](#ibm-openpages-financial-controls-management-fcm)
- [Flujos de trabajo deIBM OpenPages Model Risk Governance (MRG)](#flujos-de-trabajo-de-ibm-openpages-model-risk-governance-mrg)
- [IBM OpenPages Policy Management (PCM)](#ibm-openpages-policy-management-pcm)
- [IBM OpenPages Regulatory Compliance Management (RCM)](#ibm-openpages-regulatory-compliance-management-rcm)
- [Flujos de trabajo deIBM OpenPages Third Party Risk Management (TPRM)](#flujos-de-trabajo-de-ibm-openpages-third-party-risk-management-tprm)

#### Flujo de trabajo Aprobación de elemento de acción

Cuando se crea un elemento de acción, el flujo de trabajo Aprobación de elemento de acción se inicia automáticamente. Se envía un correo electrónico al responsable del elemento de acción notificándole que se le ha asignado un elemento de acción. La fecha de vencimiento de la tarea se establece en 7 días antes de la fecha de vencimiento del elemento de acción. Cuando se completa un elemento de acción, la persona asignada selecciona **Acciones** > **Enviar para aprobación**. A continuación, el flujo de trabajo realiza las acciones siguientes:

- Copia el valor del campo Propietario del problema del problema padre en el campo Propietario del problema para aprobación del elemento de acción.
- Establece el campo de estado del elemento de acción en En espera de aprobación.
- Envía un correo electrónico al propietario del problema informándole de que un elemento de acción está a la espera de su aprobación.

El propietario del problema revisa el elemento de acción y, a continuación, aprueba o rechaza el cierre del problema. La fecha de vencimiento de la tarea se establece en la fecha de vencimiento del elemento de acción.

Si el propietario del problema selecciona **Acciones** > **Aprobar**, el flujo de trabajo completa las acciones siguientes:

- Establece el campo de estado en Cerrado.
- Establece el campo Aprobar/Rechazar en Aprobar.
- Establece el campo Fecha de finalización real en la fecha de hoy.

Si el propietario del problema selecciona **Acciones** > **Rechazar**, la tarea se vuelve a asignar al responsable de la acción. El flujo de trabajo realiza las siguientes acciones:

- Establece el campo de estado en Abierto.
- Establece el campo Aprobar/Rechazar en Rechazar.

*Figura 1. El flujo de trabajo de ejemplo Elemento de acción*

![El Editor de flujos de trabajo muestra un diagrama esquemático de las etapas del flujo de trabajo: Inicio, En revisión, En curso y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/action_item_appr_workflow.png)

#### Flujo de trabajo Conclusión

El flujo de trabajo Conclusión utiliza la vista de tarea del sistema de Conclusión y depende del esquema predefinido para Conclusión y los tipos de objeto relacionados.

En este flujo de trabajo, observe los siguientes elementos clave:

- La ruta de cancelación

  Si se rechaza una etapa, el flujo de trabajo vuelve a la etapa Preparación de conclusión. En su propio flujo de trabajo, puede elegir esta ruta o elegir volver a las etapas inmediatamente anteriores. Planifique las rutas a través del flujo de trabajo tanto hacia adelante como hacia atrás.
- Alteraciones temporales de tarea

  Las alteraciones temporales de tarea para cada etapa definen los campos de clave que aparecen en la lista. El texto de la orientación de usuario procede de la propia vista de tarea. Con este método, los campos de clave cambian con cada etapa y son específicos de una etapa.

*Figura 2. Flujo de trabajo Conclusión*

![El Editor de flujos de trabajo muestra un diagrama esquemático de las etapas del flujo de trabajo: Inicio, Búsqueda de preparación, revisiones y etapas de respuesta y, a continuación, una etapa Completa.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/finding_workflow.png)

*Figura 3. La especificación para el flujo de trabajo Conclusión*

![Un diagrama de flujo del flujo de trabajo de búsqueda, desde la preparación de la búsqueda hasta el cierre.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/example_wflow_finding1.jpg)

#### Flujo de trabajo de incidente

El flujo de trabajo de incidente mueve un incidente a través de un proceso de investigación y aprobación.

Cuando se crea un incidente, el flujo de trabajo de incidente se inicia automáticamente. El flujo de trabajo establece un propietario para cada etapa (propietario principal, aprobador y revisor). Establece la fecha de vencimiento basada en la fecha de descubrimiento y la gravedad de incidente.

*Figura 4. Flujo de trabajo de incidente*

![El Editor de flujos de trabajo muestra un diagrama esquemático de las etapas del flujo de trabajo: Inicio, En curso, Revisión, Aprobación y Cerrado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/incident_workflow.png)

#### Flujo de trabajo Revisión de problema

En un entorno de Gestión de problemas y corrección (IMR), puede documentar de forma efectiva, supervisar, solucionar y auditar problemas.

Los problemas son elementos que se identifican en relación con el entorno documentado y afectan de forma negativa a la gestión y notificación de los riesgos de forma precisa. En su ciclo de vida, un problema puede tener dos estados: Abierto o Cerrado.

Cuando se crea un problema, el flujo de trabajo de revisión de problema se inicia automáticamente. El flujo de trabajo establece el estado del problema en Abierto y la fecha de vencimiento original en la fecha de vencimiento original que se ha especificado al crear el problema. Se envía un correo electrónico al propietario del problema, informándole de que se le ha asignado un problema. La fecha de vencimiento de la tarea se establece en 15 días antes de la fecha de vencimiento del problema.

Para resolver el problema, el propietario del problema establece y registra las acciones adecuadas.

*Figura 5. Flujo de trabajo Revisión de problema*

![El Editor de flujos de trabajo muestra un diagrama esquemático de las etapas del flujo de trabajo: Inicio, En curso, Solicitud de ampliación de fecha de vencimiento, En revisión y Cerrado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/issue_rev_workflow.png)

El propietario del problema puede solicitar una ampliación de fecha de vencimiento en cualquier momento durante el ciclo de vida del problema estableciendo la fecha de vencimiento solicitada y seleccionando **Acciones** > **Solicitar cambio de fecha de vencimiento**. El aprobador del problema es informado de esta solicitud a través del correo electrónico. El aprobador puede aprobar o rechazar la solicitud. Si la aprueba, la fecha de vencimiento del problema se establece en la fecha de vencimiento solicitada.

El propietario del problema puede enviar el problema para su revisión seleccionando **Acciones** > **Enviar para revisión**. El flujo de trabajo realiza las validaciones siguientes:

- Todos los elementos de acción del problema están cerrados.
- El campo Conclusión del problema se ha rellenado.
- El campo Tipo de problema se ha rellenado.

Si alguna de las validaciones falla, el flujo de trabajo impide que el propietario del problema envíe el problema para su revisión. Si todas las validaciones son correctas, se notifica la solicitud al aprobador del problema por correo electrónico. La fecha de vencimiento de la tarea se establece en la fecha de vencimiento del problema. Si se rechaza, se notifica el rechazo al propietario del problema por correo electrónico. El propietario del problema puede realizar actualizaciones y, a continuación, volver a enviar el problema para su revisión. Si el problema se aprueba, el estado del mismo se establece en Cerrado.

El problema puede volver a abrirse iniciando el flujo de trabajo Revisión del problema.

#### Flujos de trabajo de KRI y KPI

- **Creación de valor de KRI**

  Este flujo de trabajo crea registros de valor de KRI e inicia flujos de trabajo en el valor KRI para la recopilación.

  Este flujo de trabajo se establece en una planificación que se ejecuta diariamente en los registros de KRI. En instancias cuando el estado de KRI es «“Activo”» y la siguiente fecha de recopilación (consulte el cálculo de la siguiente fecha de recopilación de KRI) es igual al día en que se ejecuta la planificación y la fecha de valor de KRI no es igual al día en que se ejecuta la planificación, se crea un registro de valor de KRI.

  Además de crear el registro de valor de KRI, el registro se llena con valores del KRI padre, incluyendo la fecha de recopilación esperada, el capturador de KRI, el propietario de KRI, el estado de la recopilación, el umbral rojo, el umbral amarillo y la fecha de valor.

  A continuación, el valor KRI que crea este flujo de trabajo entra en el flujo de trabajo de entrada de valor de KRI.

  *Figura 6. Flujo de trabajo de creación de valor de KRI*

  ![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/kri_value_create_workflow.png)

- **Entrada de valor de KRI**

  Este flujo de trabajo asigna valores de KRI a los usuarios y proporciona un proceso para la aprobación de valor de KRI.

  Este flujo de trabajo se inicia automáticamente cuando se crea un registro de valor de KRI y se encuentra en un estado de «“En espera de recopilación.”» Cuando se crea, el valor de KRI se llena con datos de su KRI padre, incluidos el capturador de KRI, el propietario de KRI, el valor KRI de los umbrales rojo y amarillo, la descripción y si es necesaria la aprobación. Después de especificar un valor, es posible que tenga que pulsar otra pestaña y después volver a la vista para ver los valores de KRI o KPI más recientes.

  *Figura 7. Flujo de trabajo de entrada de valor de KRI*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, Especificar valor KRI, Aprobación y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/kri_value_entry_workflow.png)

- **Flujo de trabajo de creación de valor de KPI y flujo de trabajo de entrada de valor de KPI**

  Estos flujos de trabajo son similares a los flujos de trabajo de creación de valor de KRI y entrada de valor de KRI

#### Autoevaluación de riesgos y control (RCSA)

- **Autoevaluación de riesgos y control (RCSA)**

  Este flujo de trabajo se puede utilizar para establecer, ejecutar y progresar a través de una evaluación de riesgo cualitativa. Los pasos incluyen: un propietario de riesgo inicia manualmente el flujo de trabajo de Autoevaluación de riesgo y control (RCSA), realiza una evaluación de riesgo inherente identificando el impacto y la probabilidad inherentes, realiza una evaluación de riesgo residual evaluando el impacto residual y la probabilidad, y somete la RCSA para su finalización.

- **Evaluación de control**

  Es necesario realizar una evaluación de control antes de que se pueda completar el flujo de trabajo de RCSA. Este flujo de trabajo se puede utilizar para progresar a través de la evaluación de control. Los pasos incluyen: un propietario de control inicia manualmente el flujo de trabajo de evaluación de control, realiza la evaluación de control evaluando el diseño de control y la eficacia operativa y lo presenta para su aprobación. El propietario del control/riesgo o el coordinador de la RCSA puede rechazar el control y devolverlo para su revisión, o aprobarlo y cerrarlo, marcando el control en estado «“Aprobado”».

#### Flujos de trabajo de pruebas de control

Se incluyen los siguientes flujos de trabajo relacionados con los objetos Plan de prueba y Resultado de prueba:

- Crear resultado de prueba
- Realizar prueba de control
- Actualizar y revisar plan de prueba

El flujo de trabajo Crear resultado de prueba crea automáticamente un resultado de prueba basado en la planificación o frecuencia definida en el plan de prueba padre. Cuando llega la próxima fecha de vencimiento de un plan de pruebas activo, este flujo de trabajo crea automáticamente un nuevo resultado de prueba, y lo rellena con la información del ejecutor de la prueba y la fecha de vencimiento de la prueba del plan de pruebas principal. Con el flujo de trabajo Realizar prueba de control, la prueba pasa por su realización, revisión, solicitud de documentación (si es necesaria), e incluso se crea automáticamente una incidencia si el resultado de la prueba ha fallado.

#### Flujo de trabajo Revisión de evento de pérdida

El flujo de trabajo Revisión de eventos de pérdida es similar al ciclo de vida configurable para evento de pérdida.

En este flujo de trabajo, tenga en cuenta los siguientes elementos:

- Diferentes rutas basadas en un valor de cantidad

  El flujo de trabajo proporciona distintos niveles de aprobación (nivel de aprobación 1 y nivel de aprobación 2) en función del valor de pérdida bruto del evento de pérdida.
- Uso de objetos de preferencia

  El nivel de aprobación 1 y el nivel de aprobación 2 se recuperan del objeto Preferencia. Existen distintos aprobadores basados en la división donde se ha producido el evento de pérdida. Estudie este ejemplo si desea aprender más sobre cómo implementar un objeto Preferencia en flujos de trabajo.

*Figura 8. Flujo de trabajo Revisión de evento de pérdida*

![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, En curso, En revisión, dos etapas Aprobación y Cerrado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/lossevent_rev_workflow.png)

#### Flujo de trabajo Evaluación de cuestionario

El flujo de trabajo Evaluación de cuestionario traslada una evaluación de cuestionario a través de las etapas de recopilación de información, revisión y aprobación.

![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, Recopilación de información, Revisión, Aprobación y Cerrado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/questionnaire_workflow.png)

#### Flujo de trabajo Informe de trabajo

El flujo de trabajo de Informe utiliza la lista de tarea del sistema de informes y depende del esquema predefinido para el informe y los tipos de objeto relacionados.

Hay varios tipos de Informes de trabajo, por ejemplo, Cartas de notificación y Evidencia de prueba. Sin embargo, el flujo de trabajo de ejemplo es de tipo genérico y no se ha definido para un tipo específico. En el flujo de trabajo de informe de trabajo que se crea, probablemente lo definirá para un tipo específico de informe de trabajo, en cuyo caso, puede optar por tener flujos de trabajo independientes para cada tipo o un flujo de trabajo con ramificaciones separadas con condiciones que especifiquen el tipo.

En este flujo de trabajo, tenga en cuenta los siguientes elementos:

- Quién puede ver el botón **Acciones**

  Las dos últimas acciones de reenvío, Enviar para revisión y Aprobar y Completar, están restringidas a usuarios específicos, el preparador y el revisor, respectivamente. Estas acciones se muestran sólo para ellos. Para los demás usuarios, no hay ninguna acción en el botón **Acciones**. Cuando se encuentra con una situación como ésta, puede añadir una explicación a la orientación del usuario para la etapa que explique por qué no hay ninguna opción en el botón **Acciones**.

*Figura 9. Flujo de trabajo Informe de trabajo*

![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, Planificación de informe de trabajo y Plan de recursos, Preparación de informe de trabajo, Ejecución de informe de trabajo, Revisión de informe de trabajo y Informe de trabajo completado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/workpaper_workflow.png)

*Figura 10. La especificación para el flujo de trabajo de Informe*

![Un diagrama de flujo del flujo de trabajo Informe de trabajo, desde la planificación hasta la finalización del informe de trabajo.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/example_wflow_workpaper1.jpg)

### Flujos de trabajo de IBM OpenPages Business Continuity Management (BCM)

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-business-continuity-management-workflows)

IBM OpenPages® Business Continuity Management incluye flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

Los flujos de trabajo de ejemplo están habilitados en instalaciones nuevas.

- **Proceso de revisión y aprobación del plan de continuidad de negocio**

  Este flujo de trabajo guía a los usuarios a través de la creación de un plan de continuidad de negocio, la revisión continua del plan de continuidad de negocio sobre una base anual, y la automatización para el versionado de un plan de continuidad de negocio para asegurar que una versión publicada del plan de continuidad de negocio está siempre disponible después de la creación.

  Para un nuevo Plan BC, el flujo de trabajo guía el proceso a través del progreso, en etapas de revisión y aprobación. El autor, el revisor y el aprobador son campos necesarios para avanzar en el flujo de trabajo. Una vez finalizado el proceso, el flujo de trabajo establece la siguiente fecha de revisión en 365 días y el estado a publicado.

  Para un Plan BC publicado, el usuario tiene dos opciones:

  - Renovar el plan BC actual sin realizar cambios en la versión publicada

    Si se selecciona esta opción, el revisor necesita un comentario y el flujo de trabajo establece la siguiente fecha de revisión en 365 días. El flujo de trabajo hace que el proceso requiera solo una aprobación.
  - Revisar el plan BC publicado

    Si se selecciona esta opción, el flujo de trabajo "bloquea" el plan BC actual, hace una copia del plan y establece el estado del plan copiado en borrador.

    La versión borrador copiada del plan pasa por el proceso de revisión y aprobación del flujo de trabajo. Tras la finalización, el flujo de trabajo establece el estado del plan en "publicado", incrementa el número de versión y establece la siguiente fecha de revisión en 365 días. El estado del plan publicado anteriormente se establece en archivado.

  > **Nota:** Las siguientes asociaciones hijo que estaban presentes en el plan BC anterior («“bloqueado”») también aparecen en la nueva versión del plan BC: BCTest Plan, Teams y Business Impact Analysis (BIA). Todas las asociaciones padre, con la excepción de Sucesos BC, se conservan para el nuevo plan BC.

  *Figura 1. Flujo de trabajo Proceso de revisión y aprobación del plan de continuidad de negocio*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo. El flujo de trabajo tiene dos ramas: 1) Renovar o reescribir, Aprobación y Fin; o 2) En curso, En revisión, Aprobación y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bc_plan_appr_workflow.png)

- **Evaluación de impacto empresarial inicial**

  Este flujo de trabajo ayuda a los usuarios a crear la evaluación de impacto empresarial.

  Este flujo de trabajo se inicia cuando se crea un nuevo análisis de impacto empresarial (BIA).

  *Figura 2. Flujo de trabajo Evaluación de impacto empresarial inicial*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, Actualizar correlación de dependencias, Evaluación de impacto, Identificación y corrección de deficiencias, Aprobación final, Respuesta de rechazo de aprobación y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_initial_bia_workflow.png)

- **Revisión de BIA recurrente**

  Este flujo de trabajo garantiza que los BIA se revisen al menos anualmente planificando una revisión de BIA recurrente o permitiendo una revisión ad hoc por parte del propietario.

  Este flujo de trabajo manual puede ser iniciado por el Propietario de la BIA o cuando la Siguiente fecha de revisión planificada supera la fecha en que se ejecuta la planificación semanal.

  *Figura 3. Flujo de trabajo Revisión de BIA recurrente*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, Revisión de evaluación, Aprobación y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_recur_bia_workflow.png)

- **Creación del plan de prueba de BC**

  Este flujo de trabajo proporciona a los usuarios un proceso para crear planes de prueba de continuidad de negocio.

  Este flujo de trabajo de inicio automático se inicia cuando se crea un registro de plan de prueba de BC.

  *Figura 4. Creación del plan de prueba de BC*

  ![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio, Creación de escenario de prueba, Aprobación, Respuesta a rechazo de aprobación y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bc_crt_testplan_workflow.png)

- **Ejecución del plan de prueba de BC**

  Este flujo de trabajo proporciona a los usuarios un proceso para ejecutar un plan de prueba de BC y para registrar observaciones de las pruebas del plan de prueba de BC.

  Este flujo de trabajo manual puede ser iniciado manualmente por el propietario o se puede iniciar automáticamente en función de una planificación

  *Figura 5. Ejecución del plan de prueba de BC*

  ![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio, Confirmación de inicio, Prueba y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bc_ex_testplan_workflow.png)

- **Documentación del resultado de pruebas de BC**

  Este flujo de trabajo proporciona a los usuarios un proceso para documentar los resultados de los planes de prueba de BC ejecutados y para solucionar problemas identificados durante las pruebas.

  *Figura 6. Flujo de trabajo Documentación del resultado de pruebas de BC*

  ![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio, Resultados de documento, Aprobación y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bc_test_result_workflow.png)

- **Flujo de trabajo de revisión de dependencias**

  Los requisitos de resiliencia operativa exigen que las correlaciones de dependencia de los servicios empresariales importantes se actualicen al menos anualmente. Este flujo de trabajo recuerda a los propietarios de procesos la necesidad de actualizar las dependencias de proceso en el objeto Proceso.

  Este flujo de trabajo de inicio manual puede ser iniciado por el propietario del proceso cuando el proceso se correlaciona con un servicio empresarial importante, o cuando la fecha de revisión de correlación de dependencias está vacía o han transcurrido más de 365 días a partir de la fecha de ejecución de la planificación.

  *Figura 7. Flujo de trabajo de revisión de dependencias*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, Revisión de correlación de dependencias y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_dependency_rev_workflow.png)

- **Evaluación inicial del servicio empresarial**

  Este flujo de trabajo proporciona a los usuarios una forma de catalogar todos los servicios empresariales y documentar el proceso de toma de decisiones para clasificar los servicios empresariales como servicios empresariales importantes. Para los servicios empresariales importantes, los usuarios correlacionan el servicio empresarial con los procesos y ubicaciones relacionados, se correlacionan con las métricas nuevas o existentes relacionadas con la medición de la interrupción y el rendimiento del servicio empresarial importante, y establecen tolerancias de impacto que identifican el punto en el tiempo en el que se produciría un daño intolerable debido a una interrupción del servicio.

  El flujo de trabajo se inicia cuando se crea un registro de servicio empresarial.

  *Figura 8. Evaluación inicial del servicio empresarial*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo. El flujo de trabajo comienza con una evaluación de servicio empresarial y una revisión de evaluación de servicio empresarial. A continuación, el flujo de trabajo se ramifica a la etapa final o a una serie de etapas para un ejercicio de correlación.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bserv_initial_workflow.png)

- **Evaluación periódica de servicio empresarial**

  Se necesita una revisión de la Clasificación de servicio empresarial importante y el valor de tolerancia de impacto al menos anualmente. Este flujo de trabajo garantiza que se realice una revisión anual.

  El propietario del servicio empresarial puede iniciar este flujo de trabajo para un registro en estado de «“Completo”» o cuando la ejecución de la planificación diaria coincide con el campo Siguiente fecha de revisión planificada. Las ramas de flujo de trabajo se basan en si el servicio empresarial está clasificado como un servicio empresarial importante o como un servicio empresarial regular.

  *Figura 9. Evaluación periódica de servicio empresarial*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo. El flujo de trabajo es complejo. Comienza con dos ramas: una para servicios empresariales importantes y otra para todos los demás servicios empresariales. Cada rama contiene varias etapas.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bserv_per_workflow.png)

- **Correlación de escenarios de servicios empresariales**

  Este flujo de trabajo correlaciona los análisis de escenarios con un servicio empresarial en un estado de «“Completo”».

  El propietario del servicio empresarial puede iniciar manualmente este flujo de trabajo para correlacionar escenarios con el servicio empresarial.

  *Figura 10. Correlación de escenarios de servicios empresariales*

  ![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio, Selección de análisis de escenario y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bserv_scen_workflow.png)

- **Desarrollo y pruebas de escenarios**

  Este flujo de trabajo proporciona un proceso para crear escenarios para probar la tolerancia al impacto del servicio empresarial, realizar las pruebas y registrar los resultados de las pruebas.

  Este flujo de trabajo se inicia para cualquier escenario que no se haya sometido a pruebas y se categoricen como ámbito de escenario = Resiliencia.

  *Figura 11. Desarrollo y pruebas de escenarios*

  ![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio, Desarrollo de escenario, Prueba y resultados de escenario, Aprobación de prueba y corrección y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_scen_dev_workflow.png)

- **Prueba de escenario de servicios empresariales**

  Este flujo de trabajo proporciona un proceso para la realización de pruebas planificadas de escenarios contra las tolerancias de impacto de servicios empresariales.

  Este flujo de trabajo se inicia a partir de una planificación para escenarios que se categorizan con Ámbito de escenario = Resistencia en un estado de análisis completado que tiene una fecha de revisión siguiente mayor o igual a la fecha en que se ejecuta la planificación. De forma alternativa, el propietario del análisis de escenarios puede iniciar manualmente el flujo de trabajo para un escenario categorizado con el ámbito de escenario = Resistencia.

  *Figura 12. Correlación de escenarios de servicios empresariales*

  ![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio, Revisión de escenario, Prueba y resultados de escenario, Aprobación de prueba y corrección y Finalización.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bserv_scen_test_workflow.png)

- **Imp Bus Service - Remediación de infracción**

  Este flujo de trabajo proporciona un proceso para enviar notificaciones y para remediar las infracciones y casi infracciones de las tolerancias de impacto de servicios empresariales.

  Este flujo de trabajo se inicia cuando el estado de vulneración de tolerancia al impacto del servicio empresarial está en un estado Rojo o Amarillo.

  *Figura 13. Imp Bus Service - Remediación de infracción*

  ![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio, Revisión de infracciones y, a continuación, No es necesaria ninguna corrección o Se ha creado un problema.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/bcm_bserv_breach_workflow.png)

### Flujos de trabajo de IBM OpenPages Data Privacy Management (DPM)

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-data-privacy-management-workflows)

IBM OpenPages® Data Privacy Management incluye dos flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como una plantilla y herramientas de aprendizaje para sus propios flujos de trabajo.

Los flujos de trabajo de ejemplo están habilitados en instalaciones nuevas.

- **Evaluación de impacto de privacidad**

  Cuando se importa un nuevo activo de datos (recurso) en IBM® Knowledge Catalog, el flujo de trabajo de la evaluación del impacto sobre la privacidad se inicia automáticamente. La primera etapa es Revisión de activos de datos, donde un responsable de privacidad (propietario del negocio) debe determinar si se necesita o no una evaluación de privacidad. Si el responsable de privacidad necesita más información, el responsable puede solicitar más información al encargado de datos (propietario principal) seleccionando **Acciones** > **Solicitar información adicional**. A continuación, el propietario del activo de datos tendría que proporcionar la información solicitada y seleccionar **Acciones** > **Enviar para revisión de activo de datos**.

  Si el responsable de privacidad determina que no es necesaria una evaluación de privacidad, el responsable selecciona **Acciones** > **Evaluación de privacidad no necesaria**. Esta acción establece el campo Estado de PIA del recurso en No necesario y, a continuación, el flujo de trabajo finaliza.

  Si el responsable de privacidad determina que se necesita una evaluación de privacidad, el responsable selecciona **Acciones** > **Evaluación de privacidad necesaria**. Esta acción establece el campo Estado de PIA del recurso en Necesario y crea una evaluación de cuestionario que se asigna al encargado de los datos (propietario principal) del recurso.

  A continuación, el responsable de privacidad selecciona una plantilla de cuestionario para la evaluación y el encargado de datos completa el cuestionario. Cuando se completa el cuestionario, el encargado de datos selecciona **Acciones** > **Enviar para aprobación**.

  El responsable de privacidad ahora revisa la evaluación de privacidad y puede **Aprobar PIA** o **Rechazar PIA**. Si se rechaza, la evaluación se devuelve al encargado de datos para que la corrija. Si la evaluación se aprueba, el flujo de trabajo finaliza.

  *Figura 1. Flujo de trabajo de evaluación de impacto de privacidad*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, Revisión de activos de datos, Evaluación de privacidad no necesaria, Información adicional necesaria, Evaluación de privacidad en curso, Evaluación de privacidad en espera de aprobación y Evaluación de privacidad completa.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/dpm_pia_workflow.png)

- **Evaluación del impacto de la protección de datos**

  Después de que se haya completado una evaluación de impacto de privacidad (PIA) en un activo de datos o si no es necesario un PIA, el flujo de trabajo de Evaluación de impacto de protección de datos se inicia automáticamente. Cuando se inicia, el flujo de trabajo establece el campo Estado de DPIA del recurso en Necesario y crea una evaluación de cuestionario que se asigna al responsable de privacidad (propietario de la empresa) del recurso.

  En la primera etapa del flujo de trabajo, DPIA Iniciado, un encargado de datos (propietario primario) tiene la opción de alterar temporalmente y cancelar la DPIA, si se determina que la DPIA no es necesaria. En este caso, el encargado de datos selecciona **Acciones** > **Sustituir-DPIA no necesario** .

  Si el encargado de datos no altera temporalmente el DPIA, el encargado de datos completa la evaluación de cuestionario y selecciona **Acciones** > **DPIA completado**.

  En la siguiente etapa del flujo de trabajo, DPIA En espera de aprobación, el responsable de privacidad (propietario empresarial) revisa la evaluación de cuestionario DPIA y tiene la opción de rechazarla seleccionando **Acciones** > **Rechazar PIA**, que la devuelve al encargado de datos para su corrección, o aprobarla seleccionando **Acciones** > **Aprobar PIA**, que finaliza el flujo de trabajo.

  *Figura 2. Flujo de trabajo de evaluación del impacto de protección de datos*

  ![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, DPIA iniciado, DPIA no necesario, DPIA en espera de aprobación y DPIA completado.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/dpm_dpia_workflow.png)

### IBM OpenPages Financial Controls Management (FCM)

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-financial-controls-management-workflows)

IBM OpenPages® Financial Controls Management incluye flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

FCM incluye los siguientes flujos de trabajo de ejemplo:

- Certificación FCM - Nivel de negocio
- Certificación FCM - Evaluación de control
- Certificación FCM - Evaluación de proceso
- Certificación FCM - Control
- Certificación FCM - Proceso

Los flujos de trabajo soportan la infraestructura de subcertificación interna en los niveles de Control y Proceso. Dos vías de flujo de trabajo distintas, la subcertificación de control y la subcertificación de proceso, facilitan esto y se ejecutan simultáneamente a partir del nivel de entidad empresarial.

En función de la infraestructura de subcertificación interna de la organización, puede elegir:

- Habilite solo una de estas vías de flujo de trabajo.

  Por ejemplo, el flujo de trabajo de control puede estar inhabilitado si la subcertificación a nivel de proceso es todo lo que se necesita para cumplir los requisitos de la organización.
- Inhabilite el flujo de trabajo Certificación FCM - Nivel de negocio si la entidad empresarial no está categorizada como en el ámbito de SOX.

  Si el flujo de trabajo Certificación de FCM - Nivel de negocio está inhabilitado, las operaciones realizadas en este flujo de trabajo se deben revisar, por ejemplo, volver a establecer el campo Estado de certificación en "No revisado" para determinar los impactos en el proceso de subcertificación general y los flujos de trabajo restantes.

- **Certificación FCM - Flujo de trabajo de nivel de entidad empresarial**

  - El proceso de subcertificación comienza a nivel de entidad empresarial.
  - El flujo de trabajo se activa para todas las entidades empresariales que están en el ámbito de SOX.
  - El flujo de trabajo de nivel empresarial tiene dos etapas, inicio y final.
  - El flujo de trabajo listo para usar se inicia utilizando el Planificador, que se establece para iniciar cada trimestre natural y se puede ajustar a las necesidades de la organización.
  - Este flujo de trabajo desencadena el inicio de los siguientes flujos de trabajo:

    - Certificación FCM - Control (campo "clasificación" = controles clave, aplicabilidad del flujo de trabajo = controles clave), y
    - Certificación FCM - Proceso (campo "en el ámbito" = SOX, aplicabilidad del flujo de trabajo = en el ámbito de SOX)

- **Vía de acceso de flujo de trabajo a nivel de control**

  Los objetivos del flujo de trabajo de Certificación de FCM - Control son:

  - Inicie automáticamente desde el flujo de trabajo a Nivel de negocio para todos los controles clasificados como "clave".
  - Cree un nuevo objeto de evaluación de control para cada control de claves.
  - Inicie automáticamente el flujo de trabajo Certificación de FCM - Evaluación de control.

  Los objetivos del flujo de trabajo Certificación FCM - Evaluación de control son:

  - Proporcione un mecanismo para que el usuario certifique trimestralmente los datos de control para cada control de claves.
  - Cree un registro de solo lectura de la certificación (el objeto Evaluación de control) con los puntos de datos relevantes correlacionados desde el objeto Control en una fecha específica

  El usuario tiene la opción de completar el flujo de trabajo con la acción siguiente: Certificar o Certificar con excepción.

  El usuario puede realizar las acciones siguientes:

  - Certificar - el campo Descripción de la excepción debe estar en blanco
  - Certificar con excepción - el campo Descripción de excepción debe rellenarse con la descripción de excepción.
  - Una vez finalizada la certificación, el objeto de evaluación de control se bloquea para mantener la integridad de los datos.

  *Figura 1. Certificación FCM - Evaluación de control*

  ![Vía de acceso de flujo de trabajo para la evaluación de control](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/fcm_cert_controleval_workflow.png)

- **Vía de acceso de flujo de trabajo a nivel de proceso**

  Los objetivos del flujo de trabajo Certificación FCM - Proceso son:

  - Se inicia automáticamente desde el flujo de trabajo de nivel de negocio para todos los procesos que están "en el ámbito de SOX".
  - Cree un nuevo objeto de evaluación de proceso para cada proceso en el ámbito de aplicación.
  - Inicie automáticamente el flujo de trabajo Certificación de FCM - Evaluación de proceso.

  Los objetivos del flujo de trabajo Certificación FCM - Evaluación de proceso son:

  - Proporcione un mecanismo para que el usuario certifique trimestralmente los datos de proceso para cada proceso en el "ámbito de la aplicación".
  - Cree un registro de solo lectura de la certificación (el objeto Evaluación de proceso) con los puntos de datos relevantes correlacionados desde el objeto Proceso en una fecha específica

  El usuario tiene la opción de completar el flujo de trabajo con las siguientes acciones: Certificar o Certificar con excepción.

  El usuario puede realizar las acciones siguientes:

  - Certificar - el campo Descripción de la excepción debe estar en blanco
  - Certificar con excepción - el campo Descripción de excepción debe rellenarse con la descripción de excepción.
  - Una vez finalizada la subcertificación, el objeto de evaluación de proceso se bloquea para mantener la integridad de los datos.

  *Figura 2. Certificación FCM - Evaluación de proceso*

  ![Vía de acceso de flujo de trabajo para la evaluación de proceso](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/fcm_cert_processeval_workflow.png)

### Flujos de trabajo de IBM OpenPages IT Governance (ITG)

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-it-governance-workflows)

IBM OpenPages® IT Governance incluye flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como una plantilla y herramientas de aprendizaje para sus propios flujos de trabajo.

Los flujos de trabajo de ejemplo están habilitados en instalaciones nuevas.

- **Revisión de vulnerabilidad**

  Este flujo de trabajo automático realiza un seguimiento del progreso de la evaluación de la gravedad de una vulnerabilidad identificada y proporciona una opción para que el usuario inicie el flujo de trabajo Evaluación de amenazas.

- **Evaluación de amenazas**

  Este flujo de trabajo manual se puede iniciar desde el flujo de trabajo Revisión de vulnerabilidad.

  El flujo de trabajo Evaluación de amenazas realiza un seguimiento del progreso de la identificación de cualquier amenaza que pueda explotar una vulnerabilidad y la evaluación de la probabilidad y el impacto de la explotación de la vulnerabilidad por parte de las amenazas identificadas.

- **Exención de TI**

  Este flujo de trabajo automático realiza un seguimiento de la solicitud y respuesta para obtener una renuncia siempre que la renuncia se clasifique como InfoSec Política, política de TI, requisito de TI o control de TI en el campo Tipo. Si la solicitud se aprueba, el responsable debe proporcionar una fecha de caducidad para la cancelación. De lo contrario, se asigna una fecha de caducidad de un año a partir de la fecha de aprobación.

- **Revisión de caducidad de exención de TI**

  Este flujo de trabajo automático se inicia en una planificación para cualquier Waiver aprobado desde el flujo de trabajo IT Waiver cuando la fecha de caducidad es inferior a 30 días a partir de la fecha en que se ejecuta la planificación. El usuario que ha solicitado la aprobación en el flujo de trabajo de Waiver de TI determinará si es necesaria una extensión de Waiver. Si se necesita una extensión, la cancelación avanzará a la etapa de revisión de extensión de cancelación, donde se aprobará y se otorgará una nueva fecha de vencimiento o se rechazará.

### Flujos de trabajo de IBM OpenPages Model Risk Governance (MRG)

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-model-risk-governance-workflows)

IBM OpenPages® Model Risk Governance incluye flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

Los flujos de trabajo de ejemplo están habilitados en instalaciones nuevas.

- **Flujo de trabajo Candidato modelo**

  Este flujo de trabajo permite a un usuario añadir un objeto de modelo al inventario como candidato. El candidato del modelo se envía para aprobación como Modelo o No modelo. El aprobador puede alterar temporalmente la propuesta candidata. Una vez que un candidato de modelo se confirma como modelo, puede comenzar el proceso de desarrollo y documentación del modelo.

- **Flujo de trabajo Evaluación de riesgos de modelo**

  Este flujo de trabajo realiza una evaluación de riesgos de modelo en el modelo, cuyos resultados se utilizan para asignar un nivel al modelo. El cálculo de la tarjeta de puntuación de riesgo del modelo utiliza entonces los valores de los registros de preferencia para calcular las puntuaciones de riesgo y el nivel. Al final del flujo de trabajo, las puntuaciones y el nivel se copian en el modelo padre.

- **Flujo de trabajo de validación de modelo**

  Este flujo de trabajo se ejecuta al finalizar el flujo de trabajo de desarrollo y documentación del modelo. El equipo de planificación de revisión que se identifica en un objeto de preferencia es responsable de realizar esta revisión. Este flujo de trabajo también se utiliza para realizar revisiones una vez que el modelo está en producción.

- **Flujo de trabajo Atestación de modelo**

  Este flujo de trabajo lo inicia generalmente un administrador de MRG y registra la respuesta de un propietario de modelo a una solicitud de atestación.

- **Flujo de trabajo Retos**

  Este flujo de trabajo se inicia en un modelo, uno de sus despliegues de modelo o una revisión. El resultado no puede ser una acción o cambios en un modelo o un despliegue de modelo.

- **Flujo de trabajo Solicitud de cambio de modelo**

  Este flujo de trabajo proporciona control sobre los cambios en los modelos. Un flujo de trabajo puede basarse en cambios en el negocio o en los datos y otras entradas en un modelo. Los usuarios pueden aceptar, aprobar o rechazar el cambio y decidir si es pertinente.

- **Flujo de trabajo Valor de métrica**

  Este flujo de trabajo automatiza el cálculo de Estado del incumplimiento y facilita la supervisión de rendimiento de los modelos desplegados. Este proceso es crítico para la capacidad de decidir proactivamente cambiar el modelo o sus usos o eliminar un modelo de la producción. Por lo general, un administrador de MRG crea objetos de valor de métrica, un capturador de métrica proporciona los datos más recientes para la métrica y el propietario de la métrica la revisa y aprueba. El flujo de trabajo calcula el estado de incumplimiento de la métrica y copia la información de valor de métrica más reciente en la métrica.

- **Flujo de trabajo Creación de valor de métrica**

  Cuando vence la próxima fecha de recogida de una métrica activa, este flujo de trabajo crea automáticamente un nuevo valor de métrica y lo rellena con la información del propietario, el captador y el umbral de la métrica principal. A continuación, el recopilador puede llenar la información de valor de métrica y enviarla para su revisión.

  > **Nota:** Este flujo de trabajo no es aplicable a las métricas de IBM Watson® OpenScale .

- **Flujo de trabajo Retirada de modelo**

  Este flujo de trabajo se utiliza para eliminar un modelo de la producción y retirarlo.

- **Ciclo de vida de modelo**

  Este flujo de trabajo toma un modelo de IA desde la finalización del proceso candidato hasta la aprobación para el despliegue. Incluye varias etapas y subflujos de trabajo que implican a varias partes interesadas.

- **Solicitud de caso de uso de modelo**

  El flujo de trabajo Solicitud de caso de uso de modelo se utiliza para evaluar el riesgo y obtener la aprobación empresarial para un caso de uso de modelo. Una vez que se ha aprobado un caso de uso de modelo, puede empezar el desarrollo del modelo.

- **Despliegue de modelos**

  El flujo de trabajo Despliegue del modelo se utiliza para controlar el proceso de despliegue del modelo una vez que se ha completado el desarrollo. Si el modelo se está desplegando en producción, hay un paso adicional para producir el modelo antes de que se complete el despliegue.

### IBM OpenPages Policy Management (PCM)

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-policy-management-workflows)

IBM OpenPages® Policy Management incluye un flujo de trabajo de ejemplo. Puede utilizarlo tal cual o modificarlo para que se ajuste a sus necesidades. El flujo de trabajo de ejemplo también se puede utilizar como una plantilla y herramientas de aprendizaje para sus propios flujos de trabajo.

El flujo de trabajo de ejemplo está habilitado en instalaciones nuevas.

- **Flujo de trabajo Revisión y aprobación de políticas**

  El flujo de trabajo Revisión y aprobación de políticas permite a las organizaciones gestionar la revisión de políticas y el proceso de aprobación a través de la automatización. El flujo de trabajo aborda los siguientes casos de uso:

  - Creación de una nueva política
  - Proceso de revisión de políticas anual
  - Revisiones ad hoc o fuera de ciclo

  La tabla siguiente muestra las condiciones de la regla de aplicabilidad que desencadenan el flujo de trabajo para cada caso de uso:

  **Tabla 1. Condiciones de la regla de aplicabilidad que desencadenan el inicio del flujo de trabajo**

  | Caso de uso | Regla de aplicabilidad | Eventos desencadenantes de ejemplo |
  | --- | --- | --- |
  | Política nueva | • El campo de versión está vacío | • Cambio de registro<br>• Sucesos internos |
  | Proceso de revisión anual | • Campo Fecha de revisión siguiente = hoy<br>• Campo de estado = borrador | • Revisión anual |
  | Fuera de ciclo | • Campo Tipo de revisión = Revisión fuera del ciclo | • Cambio de registro<br>• Sucesos internos |

  Los usuarios de ejemplo de este flujo de trabajo incluyen:

  - Etapa Revisión / Triaje: Propietario de política, Gestor de política
  - Editar / Etapa de autor: Autor de política, Editores de políticas
  - Revisor de SME /Aprobador: SME, Gestor
  - Ejecutivos / Aprobadores: Supervisores, Gestores, Conformidad, Ejecutivos

  Las características utilizadas en este flujo de trabajo incluyen:

  - Reglas de aplicabilidad (consulte Cuadro 1)
  - Planificador - un trabajo se establece de forma predeterminada para las revisiones diarias
  - Se proporciona orientación en cada etapa para la actividad y el usuario específicos
  - Las vistas en cada etapa de flujo de trabajo se ajustan al rol del usuario
  - Un objeto de comentario de revisión de política (PRC) se crea en las etapas Revisión y Aprobación (SME / Ejecutivo) para documentar la aprobación, los comentarios y los campos relevantes
  - Un cálculo rellena el campo Nombre de política en el campo de descripción de comentario de revisión de política

  > **Nota:** Puede añadir etapas al flujo de trabajo para aprobadores adicionales.

  *Figura 1. Flujo de trabajo Revisión y aprobación de políticas*

  ![El Editor de flujos de trabajo muestra un diagrama esquemático de las etapas del flujo de trabajo. El flujo de trabajo comienza con una etapa Revisión / Triaje. Si no hay cambios, la política pasa por una etapa de revisión/aprobación y luego una etapa Reenviar política. Si hay cambios, la política pasa por uno o más ciclos de revisión y, a continuación, pasa a la etapa Publicar.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/pcm_review_workflow.png)

- **Retirar flujo de trabajo de política**

  Este flujo de trabajo se desencadena cuando el estado de publicación = Listo para retirar.

  El flujo de trabajo lleva al usuario a través de un proceso de revisión y aprobación para retirar la política. En cada una de estas etapas, se genera un objeto Comentario de revisión de políticas (PRC) para documentar la etapa de aprobación de SME y la etapa de aprobación ejecutiva.

  El ayudante de publicación debe desencadenarse al final del proceso para completar la retirada de la política. El ayudante de publicación suprimirá la política de borrador y moverá la versión publicada de la política a la carpeta de biblioteca de políticas caducada.

  *Figura 2. Retirar flujo de trabajo de política*

  ![El Editor de flujos de trabajo muestra un diagrama esquemático de las etapas del flujo de trabajo. El flujo de trabajo empieza con una etapa Retire Policy. Si la política está lista para ser retirada, pasa por una etapa de aprobación de SME. También se proporciona una etapa de aprobación ejecutiva. Si se aprueba, la política se retira.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg9000-pcm_wf-retire_policy.png)

### IBM OpenPages Regulatory Compliance Management (RCM)

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-regulatory-compliance-management-workflows)

IBM OpenPages® Regulatory Compliance Management incluye flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

Los flujos de trabajo de ejemplo están habilitados en instalaciones nuevas.

OpenPages incluye flujos de trabajo de ejemplo para procesar eventos reguladores. Los flujos de trabajo se pueden modificar sin la necesidad de tener recursos de desarrollo o codificación. Los flujos de trabajo se pueden adaptar para que coincidan con la metodología de su organización para procesar alertas publicadas por agencias reguladoras.

- **Flujo de trabajo de revisión de cambio regulador**

  Cuando se crea un registro de cambio regulador, se inicia este flujo de trabajo. El usuario determina la aplicabilidad del registro Evento regulador y determina el impacto del evento regulador. El usuario también tiene la opción de crear y asignar tareas reguladoras a los usuarios dentro de RCM para las acciones que deben realizarse para responder al evento regulador. Cuando las tareas reguladoras se asignan a los usuarios, este flujo de trabajo no se puede cerrar hasta que se han completado todas las tareas reguladoras relacionadas.

- **Flujo de trabajo de tarea reguladora**

  Cuando se crea un registro de tarea reguladora, se inicia este flujo de trabajo. El flujo de trabajo avisa al propietario de la tarea reguladora de que se ha creado un registro y se le ha asignado. Una vez que el usuario haya completado la asignación que se proporciona en el registro de tarea reguladora y pulse **Tarea completada**, el flujo de trabajo cambiará el campo de estado a **Completada** y rellenará la fecha de finalización de la tarea.

- **Flujo de trabajo de interacción con la autoridad reguladora**

  Este flujo de trabajo guía al usuario a través de la preparación y respuesta a una interacción con la autoridad reguladora, como una solicitud de reunión, una consulta o un examen. Un usuario crea un registro de Interacción con la autoridad reguladora y, a continuación, puede añadir documentos al registro antes de iniciar manualmente el flujo de trabajo. El flujo de trabajo se asigna al usuario listado como contacto interno principal del registro de la entidad reguladora padre principal asociado a la interacción con la entidad reguladora, de lo contrario el campo Propietario debe ser la entrada para que el flujo de trabajo inicie. El usuario entonces procede a través de la identificación de otros usuarios para su colaboración, preparando un plan para responder a la interacción con la autoridad reguladora, ejecutando el plan y esperando el resultado de la interacción antes de cerrar el flujo de trabajo. Los campos proporcionados para cada vista dentro del flujo de trabajo se adaptan para el usuario basándose en el tipo de interacción con la entidad reguladora y la etapa del flujo de trabajo.

- **Flujo de trabajo de componente RI**

  Este flujo de trabajo se inicia automáticamente al crear un registro de componente RI. De forma similar al flujo de trabajo de interacción con la autoridad reguladora, el usuario procede a través de fases para preparar un plan para responder al regulador, ejecutando el plan y esperando el resultado final de la interacción con la entidad reguladora. Los campos que se proporcionan para cada vista dentro del flujo de trabajo se adaptan para el usuario basándose en el tipo de interacción con la entidad reguladora y la etapa del flujo de trabajo.

- **Flujo de trabajo de subcomponente RI**

  Este flujo de trabajo se inicia automáticamente al crear un registro de subcomponente RI. De forma similar al flujo de trabajo de interacción con la autoridad reguladora, el usuario procede a través de fases para preparar un plan para responder al regulador, ejecutando el plan y esperando el resultado final de la interacción con la entidad reguladora. Los campos que se proporcionan para cada vista dentro del flujo de trabajo se adaptan para el usuario basándose en el tipo de interacción con la entidad reguladora y la etapa del flujo de trabajo.

- **Flujo de trabajo de comentario de revisión de conformidad**

  Este flujo de trabajo se inicia automáticamente tras la creación de un registro de Comentario de revisión de conformidad cuando el creador del registro ha identificado un revisor. Se asigna una etapa de flujo de trabajo al Revisor para que revise el comentario proporcionado por el creador del registro. Después de introducir información en el campo Respuesta de comentario, el revisor puede enviar la respuesta para la revisión del creador de registros. El creador del registro entonces puede cerrar el flujo de trabajo o solicitar una revisión de seguimiento del revisor.

- **Creación de biblioteca de temas de conformidad**

  Este flujo de trabajo ayuda a los usuarios en la construcción de los temas de conformidad que pueden desplegarse en las entidades empresariales para su evaluación. El flujo de trabajo se inicia automáticamente cuando los usuarios crean un nuevo objeto de biblioteca de tema des conformidad.

- **Actualización de biblioteca de temas de conformidad**

  Este flujo de trabajo ayuda a los usuarios a actualizar los temas de conformidad, que posteriormente se podrán desplegar en las entidades empresariales para su evaluación. Este flujo de trabajo se inicia manualmente.

- **Evaluación de requisitos**

  Este flujo de trabajo ayuda a los usuarios a evaluar la eficacia de los controles para gestionar el riesgo de cumplimiento de los requisitos correlacionados. Este flujo de trabajo se inicia manualmente.

  Después de iniciar el desplegador de temas de conformidad pero antes de iniciar el flujo de trabajo Evaluación de requisitos, asigne un usuario como propietario de la evaluación de requisitos.

- **Evaluación de BE de temas de conformidad**

  Este flujo de trabajo ayuda a los usuarios a evaluar la eficacia de los controles para gestionar el riesgo de conformidad de los requisitos correlacionados dentro de un tema.

  Este flujo de trabajo está planificado para ejecutarse diariamente. El flujo de trabajo se inicia para un Tema de conformidad cuando todas sus evaluaciones de requisitos hijo están en un estado de revisión de «“Completado.”»

- **Evaluación de BE del plan de conformidad**

  Este flujo de trabajo ayuda a los usuarios a evaluar la eficacia de los controles para gestionar el riesgo de conformidad de todos los requisitos de una unidad de negocio.

  Este flujo de trabajo está planificado para ejecutarse diariamente. El flujo de trabajo se inicia cuando todos los temas de conformidad hijo dentro de una jerarquía de entidad empresarial se encuentran en un estado de revisión de «“Completado.”»

- **Evaluación de requisitos**

  Este flujo de trabajo ayuda a los usuarios a evaluar la eficacia de los controles para gestionar el riesgo de cumplimiento de los requisitos correlacionados. Esta evaluación se realiza a nivel de requisito para una revisión de todas las evaluaciones de requisitos hijo.

  Este flujo de trabajo está planificado para ejecutarse semanalmente. El flujo de trabajo se inicia para un requisito cuando todas las evaluaciones de requisitos hijo están en un estado de revisión de «“Completado.”»

- **Evaluación de la biblioteca de temas de conformidad**

  Este flujo de trabajo ayuda a los usuarios a evaluar la eficacia de los controles para gestionar el riesgo de conformidad de los requisitos correlacionados dentro de una biblioteca de temas.

  Este flujo de trabajo está planificado para ejecutarse diariamente. El flujo de trabajo se inicia cuando todos los requisitos hijo tienen definida una puntuación de requisito general.

- **Evaluación de la biblioteca del plan de conformidad**

  Este flujo de trabajo ayuda a los usuarios a evaluar la eficacia de los controles para gestionar el riesgo de conformidad de todos los requisitos correlacionados dentro de la empresa.

  Este flujo de trabajo está planificado para ejecutarse diariamente. El flujo de trabajo se inicia cuando todos los temas de conformidad hijo dentro de la biblioteca están en un estado de revisión de «“Completado.”»

- **Restablecimiento de evaluación de conformidad**

  El flujo de trabajo se invoca desde el objeto Plan de conformidad. El flujo de trabajo inicia una cascada de otros flujos de trabajo de dos etapas para restablecer los valores cuando es necesario un nuevo ciclo de evaluación de conformidad. Ejecute este flujo de trabajo desde **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Flujos de trabajo** para asegurarse de que se restablecen todos los Planes de Cumplimiento.

- **Tema de conformidad - Restablecimiento de biblioteca**

  Este flujo de trabajo lo inicia el flujo de trabajo Restablecimiento de evaluación de conformidad. El flujo de trabajo Tema de conformidad - Restablecimiento de biblioteca restablece los valores de los temas de conformidad de biblioteca.

- **Tema de conformidad - Restablecimiento de BE**

  Este flujo de trabajo lo inicia el flujo de trabajo Restablecimiento de evaluación de conformidad. El flujo de trabajo Tema de conformidad - Restablecimiento de BE restablece los valores de los temas de conformidad que se encuentran en una jerarquía de entidades empresariales.

- **Restablecimiento de evaluación de requisitos**

  Este flujo de trabajo se inicia mediante el flujo de trabajo Tema de conformidad - Restablecimiento de BE. El flujo de trabajo Restablecimiento de evaluación de requisitos restablece los valores en las evaluaciones de requisitos que se correlacionan con un tema de conformidad.

- **Activar cambio - Regulador**

  Este flujo de trabajo crea un registro de cambio regulador y asocia el registro a un evento regulador cuando se cumplen las condiciones de una regla del **Motor de reglas** que indican que el evento regulador aborda un cambio regulador, como una regla propuesta o final publicada en el registro federal. El flujo de trabajo también llena determinados campos en el registro de cambio regulador creado, incluida la categorización del registro de cambio regulador como **Cambio regulador**. Este flujo de trabajo permite la asociación de varios registros de cambios regulatorios a un evento regulatorio, de forma que varios usuarios pueden analizar el impacto del suceso regulatorio sobre sus áreas concretas de responsabilidad dentro de la organización.

#### Flujos de trabajo para el conector Reg-Track

Los siguientes flujos de trabajo están disponibles con el conector Reg-Track :

- **Activar cambio - Regulador**

  Este flujo de trabajo crea un registro de cambio regulador y asocia el registro a un evento regulador de Reg-Track cuando se cumplen las condiciones de una regla del motor de reglas que indica que el evento regulador de Reg-Track aborda un cambio regulador, como una regla propuesta o final publicada en el registro federal. El flujo de trabajo también llena determinados campos en el registro de cambio regulador creado, incluida la categorización del registro de cambio regulador como **Cambio regulador**. Este flujo de trabajo permite la asociación de varios registros de cambios reguladores a un evento regulador de Reg-Track para que varios usuarios puedan analizar el impacto del evento regulador de Reg-Track en sus áreas particulares de responsabilidad dentro de la organización.

- **Activar cambio - Exploración de horizonte**

  Este flujo de trabajo crea un registro de cambio regulador y asocia el registro a un evento regulador de Reg-Track cuando se cumplen las condiciones de una regla del motor de reglas que indica que el evento regulador de Reg-Track aborda un problema que no es un cambio regulador, como una acción de voz o de imposición publicada por un regulador. El flujo de trabajo también rellena determinados campos del registro de cambio regulador creado, incluida la categorización del registro de cambio regulador como **Exploración de horizonte**. Este flujo de trabajo permite la asociación de varios registros de cambios reguladores a un evento regulador de Reg-Track para que varios usuarios puedan analizar el impacto del evento regulador de Reg-Track en sus áreas particulares de responsabilidad dentro de la organización.

- **Reg-Track Flujo de trabajo de revisión de cambio regulador**

  Cuando se crea un registro de cambio regulador, se inicia este flujo de trabajo. El flujo de trabajo guía al usuario a través del proceso de un evento regulador de Reg-Track. El usuario determina la aplicabilidad del evento regulador de Reg-Track asociado con el registro de cambio regulador y determina el impacto del evento regulador de Reg-Track. El usuario también puede crear y asignar tareas reguladoras a los usuarios dentro de RCM para las acciones que se deben lleva a cabo para responder al evento regulador de Reg-Track. Cuando las tareas reguladoras se asignan a los usuarios, este flujo de trabajo no se puede cerrar hasta que se han completado todas las tareas reguladoras relacionadas.

- **Enviar notificación por correo electrónico**

  Este flujo de trabajo se puede utilizar para enviar notificaciones de correo a los usuarios que se nombran dentro de una regla que se crea en el motor de reglas.

#### Flujos de trabajo para el conector Thomson Reuters

Los siguientes flujos de trabajo están disponibles con el conector Thomson Reuters :

- **Activar cambio - Regulador**

  Este flujo de trabajo crea un registro Cambios regulatorios y asocia el registro a un evento regulatorio TRRI cuando se cumplen las condiciones de una regla del Motor de reglas que indican que el evento regulatorio TRRI aborda un cambio regulador como, por ejemplo, una proposición de regla o regla final publicada en el registro federal. El flujo de trabajo también llena determinados campos en el registro de cambio regulador creado, incluida la categorización del registro de cambio regulador como **Cambio regulador**. Este flujo de trabajo permite la asociación de varios registros de cambios reguladores a un evento regulatorio TRRI, de forma que varios usuarios pueden analizar el impacto del suceso regulatorio TRRI sobre sus áreas concretas de responsabilidad dentro de la organización.

- **Activar cambio - Exploración de horizonte**

  Este flujo de trabajo crea un registro de cambio regulador y asocia el registro a un evento regulador TRRI cuando se cumplen las condiciones de una regla del motor de reglas que indican que el evento regulador TRRI aborda un problema que no es un cambio regulador, como por ejemplo una acción de imposición o expresión publicada por un regulador. El flujo de trabajo también rellena determinados campos del registro de cambio regulador creado, incluida la categorización del registro de cambio regulador como **Exploración de horizonte**. Este flujo de trabajo permite la asociación de varios registros de cambios reguladores a un evento regulatorio TRRI, de forma que varios usuarios pueden analizar el impacto del suceso regulatorio TRRI sobre sus áreas concretas de responsabilidad dentro de la organización.

- **Flujo de trabajo de revisión de cambio regulador de TRRI**

  Cuando se crea un registro de cambio regulador, se inicia este flujo de trabajo. El flujo de trabajo guía al usuario a través del proceso de un evento regulador TRRI. El usuario determina la aplicabilidad del evento regulador que está asociado con el registro de cambio regulador TRRI y determina el impacto del evento regulador TRRI. El usuario también tiene la opción de crear y asignar tareas reguladoras a los usuarios dentro de RCM para las acciones que deben realizarse para responder al evento regulador TRRI. Cuando las tareas reguladoras se asignan a los usuarios, este flujo de trabajo no se puede cerrar hasta que se han completado todas las tareas reguladoras relacionadas.

- **Enviar notificación por correo electrónico**

  Este flujo de trabajo se puede utilizar para enviar notificaciones de correo a los usuarios que se nombran dentro de una regla que se crea en el motor de reglas.

#### Flujos de trabajo para el conector Wolters Kluwer

Los siguientes flujos de trabajo están disponibles con el conector Wolters Kluwer :

- **Activar cambio - Regulador**

  Este flujo de trabajo crea un registro Cambios regulatorios y asocia el registro a un evento regulatorio WK cuando se cumplen las condiciones de una regla del Motor de reglas que indican que el evento regulatorio WK aborda un cambio regulador como, por ejemplo, una proposición de regla o regla final publicada en el registro federal. El flujo de trabajo también llena determinados campos en el registro de cambio regulador creado, incluida la categorización del registro de cambio regulador como **Cambio regulador.** Este flujo de trabajo permite la asociación de varios registros de cambios reguladores a un evento regulatorio WK, de forma que varios usuarios pueden analizar el impacto del suceso regulatorio WK sobre sus áreas concretas de responsabilidad dentro de la organización.

- **Activar cambio - Exploración de horizonte**

  Este flujo de trabajo crea un registro de cambio regulador y asocia el registro a un evento regulador WK cuando se cumplen las condiciones de una regla del motor de reglas que indican que el evento regulador WK aborda un problema que no es un cambio regulador, como por ejemplo una acción de imposición o expresión publicada por un regulador. El flujo de trabajo también rellena determinados campos del registro de cambio regulador creado, incluida la categorización del registro de cambio regulador como **Exploración de horizonte**. Este flujo de trabajo permite la asociación de varios registros de cambios reguladores a un evento regulatorio WK, de forma que varios usuarios pueden analizar el impacto del suceso regulatorio WK sobre sus áreas concretas de responsabilidad dentro de la organización.

- **Flujo de trabajo de revisión de cambio regulador de WK**

  Cuando se crea un registro de cambio regulador a partir de un WK, se inicia este flujo de trabajo. El flujo de trabajo guía al usuario a través del proceso de un evento regulador WK. El usuario determina la aplicabilidad del evento regulador WK que está asociado con el registro de cambio regulador y determina el impacto del evento regulador. El usuario también tiene la opción de crear y asignar tareas reguladoras a los usuarios dentro de RCM para las acciones que deben realizarse para responder al evento regulador. Cuando las tareas reguladoras se asignan a los usuarios, este flujo de trabajo no se puede cerrar hasta que se han completado todas las tareas reguladoras relacionadas.

- **Enviar notificación por correo electrónico**

  Este flujo de trabajo se puede utilizar para enviar notificaciones de correo a los usuarios que se nombran dentro de una regla que se crea en el motor de reglas.

### Flujos de trabajo de IBM OpenPages Risk Management for ESG

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-risk-management-esg-workflows)

IBM OpenPages® Risk Management for ESG incluye flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

ESG incluye flujos de trabajo para los siguientes casos de uso:

- Gestión objetiva
- Aplicabilidad de conformidad ESG
- Evaluación de conformidad de ESG

Los flujos de trabajo para la gestión de objetivos son:

- **Flujo de trabajo de creación de objetivos**

  Cuando se crea un objetivo, este flujo de trabajo permite al usuario rellenar campos clave relacionados con la descripción, la propiedad, la categorización y la priorización del objetivo.

  *Figura 1. Flujo de trabajo de creación de objetivos*

  ![Este flujo de trabajo tiene tres etapas: Inicio, Objetivo de documento y Objetivo final en directo.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg8302-esg_obj-cr.png)

- **Flujo de trabajo de actualización de objetivo**

  Este flujo de trabajo se utiliza para actualizar un objetivo o marcarlo como Completo.

  *Figura 2. Flujo de trabajo de actualización de objetivo*

  ![Este flujo de trabajo tiene cuatro etapas: Inicio, Progreso de actualización, Objetivo de finalización completado y Objetivo de finalización en curso.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg8302-esg_obj-upd.png)

Los flujos de trabajo para la aplicabilidad de conformidad son:

- **Aplicabilidad ESG-Flujo de trabajo de mandato**

  Este flujo de trabajo crea evaluaciones de aplicabilidad. No es necesaria ninguna acción de usuario. Este flujo de trabajo inicia el flujo de trabajo «“Aplicabilidad de ESG- SubMandate”» para todos los SubMandatesasociados.

  *Figura 3. Aplicabilidad ESG-Flujo de trabajo de mandato*

  ![Este flujo de trabajo tiene dos etapas: Inicio y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg8302-esg_app-m.png)

- **Aplicabilidad ESG-Flujo de trabajo SubMandate**

  Este flujo de trabajo se inicia desde el mandato padre. Los flujos de trabajo solicitan al propietario del mandato que evalúe la aplicabilidad de ESG en cada SubMandate. Tras el envío, el flujo de trabajo inicia el flujo de trabajo «“Aplicabilidad ESG-Requisito”» para los requisitos asociados.

  *Figura 4. Aplicabilidad ESG-Flujo de trabajo SubMandate*

  ![Este flujo de trabajo tiene tres etapas: Iniciar, Determinar aplicabilidad y Finalizar.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg8302-esg_app-subm.png)

- **Aplicabilidad ESG-Requisito**

  Este flujo de trabajo permite al propietario del mandato registrar si el requisito es aplicable y notificable para ESG. El usuario también registra el tipo de evaluación para el requisito: medido (uso de KRI) o declaración de divulgación.

  *Figura 5. Aplicabilidad ESG-Flujo de trabajo de requisito*

  ![Este flujo de trabajo tiene tres etapas: Iniciar, Determinar aplicabilidad y Finalizar.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg8302-esg_app-req.png)

Los flujos de trabajo para la evaluación de conformidad son:

- **Evaluación de conformidad de ESG-Iniciar flujo de trabajo**

  Este flujo de trabajo no tiene tareas de usuario. El flujo de trabajo inicia el flujo de trabajo «“Evaluación del cumplimiento de ESG - Requisito”» para todos los requisitos descendientes (Mandato, SubMandate, y Requisito) que estén marcados como Aplicables para ESG.

  *Figura 6. Evaluación de conformidad de ESG-Iniciar flujo de trabajo*

  ![Este flujo de trabajo tiene dos etapas: Inicio y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg8302-esg_ca-launch.png)

- **Evaluación de conformidad de ESG-Flujo de trabajo de requisito**

  Se trata de un flujo de trabajo de evaluación y aprobación de dos etapas para los requisitos que son aplicables para ESG.

  *Figura 7. Evaluación de conformidad de ESG-Flujo de trabajo de requisito*

  ![Este flujo de trabajo tiene cinco etapas: Inicio, Evaluación-Declaración de divulgación, Evaluación-Medida, Revisión de evaluación y Evaluación y Revisión completadas.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg8302-esg_ca-req.png)

- **Flujo de trabajo Declaración de divulgación y revisión**

  Se trata de un flujo de trabajo de evaluación y aprobación de dos etapas para las declaraciones de divulgación.

  *Figura 8. Flujo de trabajo Declaración de divulgación y revisión*

  ![Este flujo de trabajo tiene cinco etapas: Inicio, Declaración de divulgación completa, Revisión de divulgación, Finalización de intención cumplida y Finalización de intención no cumplida.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_solutions/nfg8302-esg_wf-ds.png)

### Flujos de trabajo de IBM OpenPages Third Party Risk Management (TPRM)

`Guía de soluciones › GRC Workflow` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=workflow-third-party-risk-management-workflows)

IBM OpenPages® Third Party Risk Management incluye flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

Los flujos de trabajo de ejemplo están habilitados en instalaciones nuevas.

- **Selección de proveedor**

  Este flujo de trabajo se utiliza al seleccionar proveedores. Este flujo de trabajo puede ser utilizado por el aprovisionamiento o una entidad empresarial en su proceso. El primer paso es identificar las responsabilidades del proveedor que se deben añadir como parte del proceso RFI del cliente. Una vez determinado, se creará la RFI y se determinará una lista de proveedores para participar. A continuación, el cliente utiliza su propio proceso RFI y realiza un seguimiento de los resultados. El usuario final utilizará el flujo de trabajo Diligencia debida antes de la selección final. Al finalizar el flujo de trabajo Selección de proveedor, el usuario puede iniciar el flujo de trabajo Incorporación de proveedor.

- **Diligencia debida de proveedor**

  Este flujo de trabajo es para llevar a cabo la diligencia debida sobre un tercero potencial. Se puede añadir un cuestionario o lista de comprobación (basada en procesos internos) para documentar el proceso de diligencia debida. El flujo de trabajo empieza con la identificación del proveedor, asignando un usuario a la tarea de diligencia debida. Una vez completada la recopilación de hechos, el flujo de trabajo documenta los pasos de aprobación para aceptar o rechazar un proveedor.

- **Incorporación de proveedor**

  Este flujo de trabajo se utiliza para la incorporación de un tercero. Se puede añadir un cuestionario o lista de comprobación (basada en procesos internos) para documentar el proceso de incorporación. El flujo de trabajo comienza después de que un proveedor haya pasado por los flujos de trabajo de diligencia debida y se haya firmado el contrato inicial. Un usuario revisará y especificará información pertinente, asignará la gravedad del proveedor y asignará los controles y los KRI. El paso final será planificar el siguiente periodo de evaluación para el proveedor.

- **Negociaciones de contratos de proveedor**

  Este flujo de trabajo permite a un usuario realizar un seguimiento del progreso de las negociaciones de contrato. El flujo de trabajo comienza con la definición de los términos contractuales por parte de la empresa y su entrega al departamento jurídico para su redacción y edición. Una vez preparado el borrador del contrato, éste se entrega al vendedor con los pasos necesarios para su redacción y aprobación final.

- **Terminación de proveedor**

  Este flujo de trabajo permite a un usuario completar el proceso de terminación de un proveedor. Los pasos incluyen la identificación del proveedor, la búsqueda de un proveedor de sustitución (si es necesario), la finalización de la lista de comprobación de terminación, la notificación de terminación y la confirmación final.

- **Evaluación de proveedores**

  El usuario utilizará este flujo de trabajo al realizar una evaluación de riesgo del proveedor. Los pasos incluyen la identificación del cuestionario, la preparación del cuestionario, la evaluación, revisión, aceptación/rechazo y la creación de problemas.

- **Problema global identificado de proveedor**

  Este flujo de trabajo se puede utilizar cuando se identifica un problema global entre los proveedores. Es probable que se cree un problema global debido a una anomalía en la política, procedimiento y/o control del usuario final que ha adoptado un proveedor. Los pasos incluyen: la identificación de un problema global (en toda la empresa) que se ha descubierto; la identificación de las deficiencias que plantearon el problema; la revisión de las políticas, procedimientos y controles internos; la actualización de la documentación necesaria; y el envío de una notificación a todos los proveedores de las actualizaciones realizadas.

- **Remediación de problemas de proveedor**

  Este flujo de trabajo se puede utilizar cuando se ha identificado un problema con un proveedor para que funcione a través del proceso de remediación. Los pasos incluyen: la identificación de un problema con un proveedor, la identificación de las deficiencias que plantearon el problema, la creación de un plan de acción, la finalización de las tareas de mitigación, la documentación de una excepción y/o la terminación.

## Características heredadas

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=sg-legacy-features)

Las características siguientes han quedado en desuso o se han eliminado de IBM OpenPages®.

### Visualizaciones de procesos empresariales (existentes)

`Guía de soluciones › Características heredadas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=features-business-process-visualizations-legacy)

Las visualizaciones que representaban procesos de negocio en un formato gráfico ya no están soportadas en IBM OpenPages®.

La infraestructura, por ejemplo, los tipos de objeto y desencadenantes, que dan soporte a las visualizaciones de procesos de negocio pueden existir en el sistema si utiliza una versión anterior de OpenPages.

Las visualizaciones de procesos de negocio soportan el proceso de gestión de riesgos y análisis de datos proporcionando vistas gráficas de procesos, subprocesos, actividades, riesgos y controles. Incluyen gráficos de organización de Entidad de negocios y diagramas de proceso.

#### Tipos de objeto

Las visualizaciones incluían los tipos de objeto siguientes:

- Objetos Entrada de datos y Salida de datos

  Los objetos Entrada de datos y Salida de datos son objetos hijo del proceso y pueden tener asociaciones únicamente con riesgos existentes. Representan elementos de un flujo para describir una entrada al flujo de negocio o una salida desde diversas actividades de un proceso, como, por ejemplo, la ejecución de un informe, la actualización de un sistema CRM o la obtención de una fuente de datos de un origen de datos externo.
- Objetos de diagrama del proceso

  Un diagrama del proceso es un objeto hijo del proceso y puede tener muchos diagramas por proceso. Se utiliza para almacenar la secuencia de subprocesos o actividades dentro de un proceso con riesgos y controles asociados junto con cualquier anotación, como los nodos de decisión. Todos los atributos de la visualización de Proceso de negocio se almacenan en el objeto Diagrama de proceso.

#### Campo calculado

Las visualizaciones incluyen un campo calculado, `OPSS-ProcDiag.ProDiaLnk`, en el tipo de objeto Diagrama de proceso.

#### Informe

Las visualizaciones incluían el informe de análisis del proceso y los siguientes informes de acceso a detalles:

- Flujo de proceso de negocio
- Diagrama de jerarquía de entidades de negocios
- Gráfica de riesgos

El informe muestra los riesgos y los controles en el contexto de un diagrama del proceso. Proporciona una vista agregada de Riesgo y Controles con calificación de riesgo y eficacia de control en el nivel Proceso y Entidad de negocios.

#### Activadores

Las visualizaciones incluyen activadores basados en objetos de entrada de datos y salida de datos. Los activadores de visualización evitan que un usuario añada riesgos nuevos como elementos secundarios de los tipos de objeto Entrada de datos y Salida de datos. Los objetos Entrada de datos y Salida de datos son elementos secundarios del proceso y solo pueden tener asociaciones con riesgos existentes. El objeto de entrada de datos representa elementos de un flujo para representar una entrada en el flujo empresarial. El objeto de salida de datos representa una salida de las actividades dentro de un proceso, como la ejecución de un informe o la actualización de un sistema CRM.

#### Tipo de archivo del sistema

Las visualizaciones utilizaban el tipo de archivo del sistema VizConfig para los archivos de configuración de visualización.

#### Tareas en la interfaz de usuario estándar

Los usuarios han accedido a las visualizaciones utilizando las tareas siguientes en la interfaz de usuario estándar:

- **Organización** > **Entidades empresariales** > **Campo Gráfico de entidades empresariales** > **Enlace de diagrama de jerarquía**
- **Organización** > **Procesos** > **Asociaciones** > **Diagramas de proceso**

### Campos calculados

`Guía de soluciones › Características heredadas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=features-computed-fields)

La tabla siguiente lista los campos calculados heredados. Estos campos se sustituyen por campos URL. Un campo calculado es un campo de solo lectura cuyo valor se obtiene de los valores de otros campos. Los campos calculados pueden incluir tipos de datos, como booleano, fecha, decimal, entero y cadenas simples.

**Tabla 1. Campos calculados en OpenPages soluciones**

| Etiqueta de tipo de objeto<br>Grupo de campos<br>Nombre de campo | Descripción | RCM | ORM | PCM | ITG | IAM |
| --- | --- | --- | --- | --- | --- | --- |
| Evaluación de riesgo<br>OPSS-RA<br>Asistente de relleno de RCSA | Crea un enlace que inicia el Asistente de relleno de RCSA. Este asistente permite al coordinador de RCSA finalizar la evaluación de riesgos y crear un árbol de evaluación para las referencias históricas. |  | X |  |  |  |
| Evaluación de riesgo<br>OPSS-RA<br>Asistente de alineación de procesos RCSA | Crea un enlace que inicia el Asistente de alineación de procesos RCSA. Este asistente permite al coordinador de RCSA revisar los procesos, riesgos y controles asociados y crear más asociaciones. El asistente también configura los procesos, riesgos y controles con el estado de En espera de evaluación. |  | X |  |  |  |

### Activadores heredados

`Guía de soluciones › Características heredadas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=features-legacy-triggers)

Las soluciones de IBM OpenPages® incluyen varios desencadenantes que no están habilitados en instalaciones nuevas.

Estos desencadenantes se han sustituido por la funcionalidad que está disponible en las características GRC Workflow y GRC Calculations .

La tabla siguiente lista los activadores que ya no están habilitados.

**Tabla 1. Activadores que no están habilitados en instalaciones nuevas**

| Desencadenante | TPRM | RCM | MRG | FCM | ORM | PCM | ITG | IAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Desencadenantes del ciclo de vida de eventos de pérdida (existentes)](#desencadenantes-del-ciclo-de-vida-de-eventos-de-pérdida-existentes) |  |  |  |  | X |  |  |  |
| [Desencadenantes de ciclo de vida de evaluación de cuestionario (existentes)](#desencadenantes-de-ciclo-de-vida-de-evaluación-de-cuestionario-existentes) | X | X | X | X | X | X | X | X |
| [Desencadenantes de ciclo de vida de incidencias (existentes)](#desencadenantes-de-ciclo-de-vida-de-incidencias-existentes) |  |  |  |  |  | X | X |  |
| [Desencadenantes de ciclo de vida de KRI y KPI (existentes)](#desencadenantes-de-ciclo-de-vida-de-kri-y-kpi-existentes) |  |  |  |  | X | X | X |  |
| [Desencadenante de tarjeta de puntuación de riesgo de modelo](#desencadenante-de-tarjeta-de-puntuación-de-riesgo-de-modelo)<br>**Nota:** Este desencadenante está inhabilitado de forma predeterminada, pero sigue estando disponible en instalaciones nuevas. |  |  | X |  |  |  |  |  |
| [Desencadenantes de RCSA cuantitativas y RCSA cualitativas (existente)](#desencadenantes-de-rcsa-cuantitativas-y-rcsa-cualitativas-existente) |  |  |  |  | X |  |  |  |
| Desencadenantes para el tipo de objeto Análisis de escenario: Actualización de finalización de escenario y Creación de finalización de escenario |  |  |  |  | X |  |  |  |
| Desencadenantes de [Visualizaciones de procesos de negocio (heredadas)](#visualizaciones-de-procesos-empresariales-existentes) (desencadenantes para los tipos de objeto Entrada de datos y Salida de datos). |  |  |  |  |  |  |  |  |

#### Desencadenantes de ciclo de vida de eventos de pérdida (versión 7.2.0.1 y posterior) (existentes)

`Guía de soluciones › Características heredadas › Activadores heredados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=lt-loss-event-lifecycle-triggers-version-7201-later-legacy)

Los activadores proporcionan las transiciones que mueven eventos de pérdida durante un ciclo de vida de investigación. Los ciclos de vida definen las etapas que puede seguir un tipo de objeto

Estos desencadenantes no están habilitados en instalaciones nuevas.

En cada fase, el sistema:

- Identifica un responsable del ciclo de vida
- Define las acciones disponibles para moverse a una fase diferente
- Envía automáticamente un correo electrónico al nuevo responsable de ciclo de vida
- Define otros atributos que están relacionados con la fase actual

El ciclo de vida de los eventos de pérdida utiliza las fases siguientes:

- Nuevo
- Abierto
- Pendiente de aprobación
- Awaiting Approval L1
- Awaiting Approval L2
- Cerrado

Cuando se crea un evento de pérdida, el sistema establece el ciclo de vida en la nueva fase y envía un correo al primer asignado de ciclo de vida. Cuando el usuario completa la tarea, el activador mueve el objeto a la tarea siguiente y al usuario siguiente. Un usuario puede añadir un comentario con cada transición. Las transiciones tienen lugar cuando los usuarios abren un objeto de evento de pérdida en la vista de detalles y pulsan Ciclo de vida > `<transition icon>`. La etapa determina el icono de transición que se visualiza.

> **Atención:** Antes de la versión 7.2.0.1 de OpenPages®, existía un activador para los objetos de evento de pérdida que verificaba los campos de fecha y rellenaba los campos de aprobador en el evento de pérdida en el momento en que el usuario establecía el campo **OPSS-LossEv:Submit** en **Sí**. A partir de OpenPages Versión 7.2.0.1 y posteriores, este desencadenante se activa ahora en la transición del ciclo de vida de Abierto a Enviar, por lo que el desencadenante se activa ahora en el campo **OPLC-Std :LCTransition** con un valor de **Enviar**. El campo **OPSS-LossEv:Submit** del evento de pérdida es ahora redundante.

> Existía además un segundo activador para bloquear el evento de pérdida y sus hijos tras el cierre. Antes de la versión 7.2.0.1 de OpenPages, este disparador se activaba en el campo **OPLC-LossEv:Status** con el valor **Aprobado**. A partir de OpenPages Versión 7.2.0.1 y posteriores, este desencadenante se activa ahora en el campo **OPLC-Std :LCStage** con un valor de **Cerrado**.

La tabla siguiente resume cómo el sistema maneja los eventos de pérdida y establece el asignado de ciclo de vida. La columna de icono Transición contiene el nombre del Ciclo de vida >`<transition icon>` en la vista de detalles del problema que un usuario pulsa para desencadenar la transición a la siguiente etapa.

**Tabla 1. Propietarios de etapas y procesos de ciclo de vida para eventos de pérdida**

| Etapa | Responsable de ciclo de vida | Icono de transición | Etapa siguiente | Estado siguiente |
| --- | --- | --- | --- | --- |
| Nuevo | Propietario (Owner) | **Iniciar** | Abierto | Abierto |
| Abierto | Propietario (Owner) | **Enviar** | Cerrado | Cerrado |
| Abierto | Propietario (Owner) | **Enviar** | Pendiente de aprobación | Pendiente de aprobación |
| Abierto | Propietario (Owner) | **Enviar** | Awaiting Approval L1 | Awaiting Approval L1 |
| Pendiente de aprobación | Aprobador | **Reject Approval** | Abierto | Aprobación rechazada |
| Pendiente de aprobación | Aprobador | **Cierre de fase 1** | Cerrado | Aprobado nivel 1 |
| Awaiting Approval L1 | Aprobador | **Enviar para aprobación L2** | Revisión de escalamiento | Revisión de escalamiento |
| Awaiting Approval L1 | Aprobador | **Rechazar aprobación L1** | Abierto | Aprobación L1 Rechazada |
| Awaiting Approval L2 | Aprobador L2 | **Cierre de fase 2** | Cerrado | Niveles 2 aprobados |
| Awaiting Approval L2 | Aprobador L2 | **Devolver a aprobación L1** | Awaiting Approval L1 | Devolver a L1 |
| Awaiting Approval L2 | Aprobador L2 | **Rechazar aprobación L2** | Abierto | Aprobación L2 Rechazada |

Cuando se realiza una transición **Enviar**, el activador comparar la pérdida bruta con los valores de umbral proporcionados en el registro de preferencias asociado con la entidad de negocios más cercana al evento de pérdida . Para una pérdida bruta inferior al umbral 1, el evento de pérdida realiza las transiciones a la fase Cerrado. (Se trata de un ciclo de vida de evento de pérdida fase 0).

Para eventos de pérdida con una pérdida bruta superior al umbral 1 e inferior al umbral 2, el campo **Aprobador** se copia del registro de preferencias al evento de pérdida. El evento de pérdida realiza la transición al la fase Esperando aprobación. (Se trata de un ciclo de vida de evento de pérdida fase 1). De manera predeterminada, el activador define la fecha de vencimiento 14 días después de la fecha de envío

Para eventos de pérdida con una pérdida bruta superior al umbral 2, el campo **Aprobador** y el campo **Aprobador L2** se copian del registro de preferencias al evento de pérdida. El evento de pérdida realiza la transición a la fase Esperando aprobación L1. (Se trata de un ciclo de vida de evento de pérdida fase 2). De manera predeterminada, el activador define la fecha de vencimiento 14 días después de la fecha de envío

Si el evento de pérdida realiza de nuevo la transición a la fase Abierto, el activador se ejecuta de nuevo en **Enviar** y, si la pérdida bruta ha cambiado, puede alterar el ciclo de vida. Cuando el evento de pérdida realiza la transición a la fase Cerrado, un activador cierra y bloquea todos los impactos hijo y recuperaciones. A continuación el activador bloquea el evento de pérdida.

##### Notificación de evento de pérdida

La notificación del evento de pérdida envía un correo electrónico a un asignado de ciclo de vida cuando se crea un evento de pérdida y para cada transición del ciclo de vida del evento de pérdida. Se produce una transición cuando un usuario pulsa un icono de transición (Ciclo de vida > **Inicio**, **Enviar**, **Rechazar aprobación**, **1 Etapa Cerrar**, **Enviar para aprobación de L2**, **Rechazar aprobación de L1**, **2 Etapa Cerrar**, **Devolver a aprobación de L1** o **Rechazar aprobación de L2**) en la vista de detalles del evento de pérdida.

Un activador de ciclo de vida de evento de pérdida inicia la notificación de evento de pérdida. La notificación de correo electrónico contiene la etapa, el estado, la fecha de vencimiento, comentarios y un enlace al evento de pérdida.

##### Eventos de pérdida y GRC Workflow

Puede utilizar tanto los ciclos de vida configurables como los flujos de trabajo para Eventos de pérdida, pero debe tener en cuenta cómo interactúan y dónde entran en conflicto. Para obtener más información, consulte *Configuración de GRC Workflow* en la publicación *IBM OpenPages Guía del administrador*.

##### Condiciones que controlan el botón Ciclo de vida

Cuando un objeto que utiliza ciclos de vida se abre en una vista de detalle o actividad, el botón **Ciclo de vida** > **< icono de transición >** se muestra u oculta basándose en la información de usuario y ciclo de vida actual del objeto.

Se muestra si se cumplen todas las condiciones siguientes:

- El periodo de elaboración de informes es el periodo de elaboración de informes actual.
- En el tipo de objeto se han definido los campos siguientes: LCStage, LCTransition, LCAssignee, LCComment y LCAppData.
- LCStage tiene un valor no vacío.
- Una o más transiciones se han correlacionado con el valor de LCStage actual con una dependencia de lista de selección.
- El usuario actual se ha establecido en LCAssignee, es miembro de un grupo establecido en LCAssignee o tiene permiso de escritura explícito en el objeto.

El botón se oculta si no se cumple una de las condiciones.

El botón Ciclo de vida se oculta si se realizan cambios que afectan a un proceso de ciclo de vida. Si añade campos a un tipo de objeto después de que existan instancias de objeto, los valores predeterminados no se asignan a los campos nuevos. Los campos como LCStage y LCAssignee probablemente no tengan valores válidos en las instancias existentes. El botón Ciclo de vida se oculta, lo cual garantiza que los nuevos ciclos de vida no interrumpan los ciclos de vida anteriores de las instancias de objetos existentes.

Si un tipo de objeto tiene un flujo de trabajo y un ciclo de vida configurable, el botón **Acciones** del flujo de trabajo en las vistas de tarea de la IU centrada en tareas tiene prioridad sobre el botón **Acciones** del ciclo de vida. Para obtener más información, consulte *Configuración de GRC Workflow* en la publicación *IBM OpenPages Guía del administrador*.

#### Desencadenantes del ciclo de vida de eventos de pérdida (existentes)

`Guía de soluciones › Características heredadas › Activadores heredados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-loss-event-lifecycle-legacy)

Los activadores del ciclo de vida de evento de pérdida calculan y mantienen tres campos en el objeto de evento de pérdida, cuando se crean o modifican los campos relacionados en cualquier objeto descendiente de impacto de pérdida o de recuperación de pérdidas.

Estos desencadenantes no están habilitados en instalaciones nuevas.

Los activadores automatizan el proceso de aprobación y el rendimiento de las correcciones del evento de pérdida como se describe en los activadores de envío para la aprobación de evento de pérdida y de aprobación de eventos de pérdida.

El proceso de ciclo de vida de eventos de pérdida consta de tres desencadenantes.

##### activador de cálculo de eventos de pérdida

El Activador de cálculo de eventos de pérdida calcula valores de resumen en la moneda base del sistema de un evento de pérdida en función del impacto de pérdida y recuperaciones asociados.

##### Activador de envío para aprobación del evento de pérdida

El activador de envío para aprobación del evento de pérdida cambia el evento de pérdida de un evento pendiente a la fase de aprobación de su ciclo de vida. El activador valida los datos.

El activador aparece cuando el usuario realiza la transición del ciclo de vida del evento de pérdida de **Abierto** a **Enviar**.

El activador define la fecha de vencimiento de LC 14 días después de la fecha de envío

##### Activador de aprobación de eventos de pérdida

El activador bloquea el evento de pérdida y todo impacto hijo y recuperaciones.

El activador aparece cuando el usuario realiza la transición del ciclo de vida del evento de pérdida de **Abierto** o **Esperando aprobación** a **Cerrado**.

#### Desencadenantes de ciclo de vida de evaluación de cuestionario (existentes)

`Guía de soluciones › Características heredadas › Activadores heredados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-questionnaire-assessment-lifecycle-legacy)

Estos desencadenantes no están habilitados en instalaciones nuevas.

Las evaluaciones de cuestionario son medios de recopilar información de los usuarios empresariales de la organización. Los activadores proporcionan las transiciones que mueven las evaluaciones de cuestionario durante un ciclo de vida. Los ciclos de vida definen las fases que puede seguir un objeto. En cada fase, el sistema:

- Identifica un responsable del ciclo de vida
- Define las acciones disponibles para moverse a una fase diferente
- Envía automáticamente un correo electrónico al nuevo responsable de ciclo de vida
- Define otros atributos que están relacionados con la fase actual

Se selecciona el ciclo de vida en el programa. Puede ser:

- Dos fases: recopilación de información hasta a cierre
- Tres fases: recopilación de información a revisión y hasta cierre
- Cuatro fases: recopilación de información a revisión, a aprobación y hasta cierre

Cuando se inicia un programa, el sistema crea un objeto de evaluación de cuestionario por empleado, recursos, proceso, subproceso, proveedor o compromiso en el programa. Establece el ciclo de vida en la etapa de recopilación de información y envía un correo electrónico al primer responsable de ciclo de vida. Cuando el usuario completa la tarea, el activador mueve el objeto a la tarea siguiente y al usuario siguiente. Un usuario puede añadir un comentario con cada transición. Las transiciones tienen lugar cuando el usuario trabaja con evaluaciones de cuestionario en la UI de cuestionario. Los correos electrónicos se envían en cada transición si el responsable no cambia. De forma predeterminada, los correos electrónicos no se envían cuando las evaluaciones de cuestionario se mueven a la fase Cerrado.

La tabla siguiente resume los ciclos de vida para las evaluaciones de cuestionario. La columna **icono de transición** contiene el nombre del icono en la interfaz de usuario de cuestionario que un usuario pulsa para activar la transición a la siguiente fase.

**Tabla 1. Proceso de ciclo de vida para las evaluaciones de cuestionarios**

| Ciclo de vida | Etapa | Icono de transición | Etapa siguiente | Estado siguiente |
| --- | --- | --- | --- | --- |
| Dos fases | Recopilación de información | **Enviar y cerrar** | Cerrado | Completado |
| Tres fases | Recopilación de información | **Enviar** | Revisar | En revisión |
|  | Revisar | **Acción** > **Rechazar** | Recopilación de información | Rechazado |
|  |  | **Acción** > **Aprobar y cerrar** | Cerrado | Completado |
| Cuatro fases | Recopilación de información | **Enviar** | Revisar | En revisión |
|  | Revisar | **Acción** > **Rechazar** | Recopilación de información | Rechazado |
|  |  | **Acción** > **Enviar para aprobación** | Aprobación | En aprobación |
|  | Aprobación | **Acción** > **Rechazar** | Revisar | Aprobación rechazada |
|  |  | **Acción** > **Aprobar** | Cerrado | Aprobado |

Para las evaluaciones de cuestionario, los activos subyacentes determinan el modo en que el sistema establece los responsables de ciclo de vida. La tabla siguiente resume cómo se determinan los responsables de ciclo de vida.

**Tabla 2. Responsables de ciclo de vida para las evaluaciones de cuestionarios**

| Ciclo de vida | Etapa | Recurso | Proceso/subproceso | Empleado | Proveedor | Compromiso |
| --- | --- | --- | --- | --- | --- | --- |
| Dos fases | Recopilación de información | Propietario principal | Propietario (Owner) | Cuenta de empleado | Propietario de proveedor | Propietario de compromiso |
|  | Cerrado | - | - | - | - | - |
| Tres fases | Recopilación de información | Propietario principal | Propietario (Owner) | Cuenta de empleado | Propietario de proveedor | Propietario de compromiso |
|  | Revisar | Propietario del programa | Propietario del programa | Gestor de empleados | Proveedor - Propietario de unidad de negocio | Proveedor - Propietario de unidad de negocio |
|  | Cerrado | - | - | - | - | - |
| Cuatro fases | Recopilación de información | Propietario principal | Propietario (Owner) | Cuenta de empleado | Propietario de proveedor | Propietario de compromiso |
|  | Revisar | Propietario de negocio | Propietario de negocio | Gestor de empleados | Proveedor - Propietario de unidad de negocio | Proveedor - Propietario de unidad de negocio |
|  | Aprobación | Propietario del programa | Propietario del programa | Propietario del programa | Propietario del programa | Propietario del programa |
|  | Cerrado | - | - | - | - | - |

#### Desencadenantes de ciclo de vida de incidencias (existentes)

`Guía de soluciones › Características heredadas › Activadores heredados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-incident-lifecycle-legacy)

Estos desencadenantes no están habilitados en instalaciones nuevas.

Los activadores proporcionan las transiciones que mueven incidentes durante un ciclo de vida de investigación. Los ciclos de vida definen las fases que puede seguir un objeto. En cada fase, el sistema:

- Identifica un responsable del ciclo de vida
- Define las acciones disponibles para moverse a una fase diferente
- Envía automáticamente un correo electrónico al nuevo responsable de ciclo de vida
- Define otros atributos que están relacionados con la fase actual

El ciclo de vida para incidentes utiliza las fases siguientes:

- Nuevo
- En curso
- Revisar
- Escalamiento
- Revisión de escalado
- Cerrado

Cuando se crea un incidente, el sistema establece el ciclo de vida en la nueva fase y envía un correo al primer responsable de ciclo de vida. Cuando el usuario completa la tarea, el activador mueve el objeto a la tarea siguiente y al usuario siguiente. Un usuario puede añadir un comentario con cada transición. Las transiciones tienen lugar cuando los usuarios abren un objeto de incidencia en la vista de detalles y pulsan **Ciclo de vida** > **< icono de transición >**. La etapa determina el icono de transición que se visualiza.

La tabla siguiente resume cómo el sistema maneja los incidentes y establece el responsable de ciclo de vida. La columna **Icono Transición** contiene el nombre del icono de transición que se muestra en la vista de detalles de incidente.

**Tabla 1. Proceso de ciclo de vida y propietarios de la etapa en los incidentes**

| Etapa | Responsable de ciclo de vida | Icono de transición | Etapa siguiente | Estado siguiente |
| --- | --- | --- | --- | --- |
| **Nuevo** | Propietario principal | **Iniciar** | En curso | En curso |
| **En curso** | Propietario principal | **Enviar para revisión** | Revisar | En revisión |
|  |  | **Escalar** | Escalamiento | Escalado |
| **Revisar** | Revisor | **Rechazo de revisión** | En curso | Revisión rechazada |
|  |  | **Cierre de revisión** | Cerrado | Cerrado |
| **Escalamiento** | Propietario de negocio | **Enviar para revisión de escalado** | Revisión de escalamiento | Revisión de escalamiento |
|  |  | **Desescalar** | En curso | Desescalado |
| **Revisión de escalamiento** | Revisor | **Cerrar revisión de escalado** | Cerrado | Escalado y cerrado |
|  |  | **Rechazar revisión de escalado** | Escalamiento | Revisión de escalamiento rechazada |
| **Cerrado** | Ninguna | **Volver a abrir** | En curso | Reabierto |

#### Desencadenantes de ciclo de vida añadidos en la versión 7.2.0.1 (existentes)

`Guía de soluciones › Características heredadas › Activadores heredados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-lifecycle-added-in-version-7201-legacy)

Tras la habilitación de la característica de ciclo de vida 7.2 en OpenPages®, cualquier objeto que utilice el nuevo ciclo de vida y tenga un ciclo de vida preexistente debe modificarse para utilizar los nuevos campos y grupos de campos de ciclo de vida.

Estos desencadenantes no están habilitados en instalaciones nuevas.

Los activadores proporcionan las transiciones que mueven problemas durante un ciclo de vida de investigación. Los ciclos de vida definen las fases que puede seguir un objeto.

OpenPages Versión 7.2.0.1 presenta tres nuevos ciclos de vida; controles, problemas y sucesos de pérdida. En 8.1.0 los desencadenantes de problemas han quedado en desuso y la funcionalidad se ha movido a GRC Workflow.

Para obtener más información sobre los desencadenantes de control, consulte [Desencadenantes de ciclo de vida de control](#activadores-de-ciclo-de-vida-de-control).

Los eventos de pérdida contaban con activadores existentes para ayudarle con el ciclo de vida existente de los objetos, y estos activadores se han actualizado para utilizar los nuevos campos de ciclo de vida. Si utiliza estos desencadenantes en versiones anteriores a OpenPages Versión 7.2.0.1, debe modificar los campos adecuados que se han utilizado anteriormente para los desencadenantes de eventos de pérdida en el archivo `openpages-solutions.xml` .

Antes de la versión 7.2.0.1 de OpenPages, existía un activador para los objetos de evento de pérdida que verificaba los campos de fecha y rellenaba los campos de aprobador en el evento de pérdida en el momento en que el usuario establecía el campo **OPSS-LossEv:Submit** en **Sí**. A partir de OpenPages Versión 7.2.0.1 y posteriores, este desencadenante se activa ahora en la transición del ciclo de vida de Abierto a Enviar, por lo que el desencadenante se activa ahora en el campo **OPLC-Std :LCTransition** con un valor de **Enviar**. El campo **OPSS-LossEv:Submit** del evento de pérdida es ahora redundante.

Existía además un segundo activador para bloquear el evento de pérdida y sus hijos tras el cierre. Antes de la versión 7.2.0.1 de OpenPages, este disparador se activaba en el campo **OPLC-LossEv:Status** con el valor **Aprobado**. A partir de OpenPages Versión 7.2.0.1 y posteriores, este desencadenante se activa ahora en el campo **OPLC-Std :LCStage** con un valor de **Cerrado**.

Para obtener más información, consulte [Desencadenantes de ciclo de vida de evento de pérdida (versión 7.2.0.1 y posteriores) (heredado)](#desencadenantes-de-ciclo-de-vida-de-eventos-de-pérdida-versión-7201-y-posterior-existentes).

Las soluciones de cliente personalizadas existentes que cuentan con activadores, dependencias de campo, listas de selección o informes que utilizan campos conectados al ciclo de vida existente de los objetos se deben revisar y actualizar. En caso de ser necesario, los campos que se deben sustituir en el objeto (por ejemplo los campos **Estado** o **Asignado**) se deben actualizar en la configuración de la solución existente.

#### Configuración del ciclo de vida (existente)

`Guía de soluciones › Características heredadas › Activadores heredados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-lifecycle-configuration-legacy)

En IBM OpenPages®, los ciclos de vida se pueden configurar para reducir la necesidad de implementar la lógica empresarial a través de desencadenantes personalizados.

El ciclo de vida puede configurarse para establecer valores de campo durante una transición en campos que no sean campos LC. Estos campos pueden ser de texto breve o largo, de tipos de campo enumerados de forma simple o múltiple, booleanos, enteros, decimales, de fecha, de usuario y de grupo de usuarios. En función del tipo de campo, los valores de campo pueden establecerse de las siguientes maneras:

- como un valor absoluto o relativo
- como una adición a un valor existente en el campo
- rellenarse basándose en un valor de otro campo

Por ejemplo, esto podría utilizarse para copiar el valor del campo Estado de ciclo de vida en el campo de estado "normal", de modo que las vistas existentes, informes y asistentes puedan seguir utilizando ese valor de campo de estado.

El ciclo de vida también puede configurarse con lógica condicional para regular transiciones. Se puede utilizar la lógica booleana utilizando valores de campo en el objeto y en los objetos hijo y padre inmediatos. La lógica puede incluir valores de tipos de campo enumerados de forma simple o múltiple, booleanos, enteros, decimales y de fecha. Por ejemplo, esto se podría utilizar para prohibir el envío de un evento de pérdida para su aprobación si no tiene un valor de Fecha de Reconocimiento. Si no se cumplen las condiciones, el proceso de transición se detendrá y se visualizará un error en la interfaz de usuario y se registrará en el registro.

Para obtener más información sobre cómo configurar ciclos de vida, consulte *Trigger Developer Guide*.

#### Desencadenantes de RCSA cuantitativas y RCSA cualitativas (existente)

`Guía de soluciones › Características heredadas › Activadores heredados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-rcsa-quantitative-rcsa-qualitative-legacy)

El proceso de evaluaciones de riesgos se utiliza para identificar, evaluar y cuantificar el perfil de riesgo de una empresa. Cada riesgo se evalúa sobre una base cuantitativa o cualitativa.

> **Nota:** Los desencadenantes cuantitativos y cualitativos de RCSA no están habilitados en instalaciones nuevas. Se han sustituido por la funcionalidad que está disponible en las características GRC Workflow y GRC Calculations . Consulte [Autoevaluaciones de riesgo y control (desencadenantes y cálculos)](#autoevaluaciones-de-riesgo-y-control-desencadenantes-y-cálculos).

##### Activador de RCSA cuantitativas

El desencadenante de Autoevaluaciones de riesgo y control (RCSA) cuantitativas establece la valoración de riesgo y establece el impacto, la probabilidad y la exposición para los riesgos que se especifican con el método Cuantitativo. El desencadenante se produce solo si se han modificado los valores de los campos **Impacto** o **Probabilidad** para **Riesgo**.

> **Importante:** Determine si desea evaluar los riesgos utilizando un enfoque cuantitativo o cualitativo. Este desencadenante no se aplica si utiliza el enfoque cualitativo. La opción cuantitativa o cualitativa se establece durante la instalación de las soluciones de IBM OpenPages® .

Cuando un objeto de riesgo se actualiza, asocia o desasocia, el desencadenante completa las acciones siguientes:

- Obtiene el objeto de preferencia padre.

  El desencadenante intenta encontrar el objeto de preferencia asociado con la entidad empresarial. El desencadenante recorre la jerarquía de entidades padre hasta que se encuentra un objeto de preferencia asociado a una entidad empresarial. El objeto de preferencia contiene los valores para los parámetros necesarios tal como se describe en la tabla Gravedad.
- Determina los campos de Impacto del objeto de riesgo.

  El impacto se calcula identificando el rango de umbral en el que se encuentra el valor de gravedad. Si cualquier valor de Gravedad es nulo, el valor anterior se gestiona como la Gravedad MAX.

  **Tabla 1. Valor de impacto basado en el valor de gravedad**

  | Valor de la gravedad | Valor de impacto |
  | --- | --- |
  | >= 0 y <= Gravedad 1 | 1 |
  | > Gravedad 1 y < = Gravedad 2 | 2 |
  | > Gravedad 2 y < = Gravedad 3 | 3 |
  | > Gravedad 3 y < = a gravedad 4 | 4 |
  | > Gravedad 4 y < = Gravedad 5 | 5 |
  | > Gravedad 5 y < = Gravedad 6 | 6 |
  | > Gravedad 6 y < = Gravedad 7 | 7 |
  | > Gravedad 7 y < = Gravedad 8 | 8 |
  | > Gravedad 8 y < = Gravedad 9 | 9 |
  | > Gravedad 9 | 10 |
- Determina los campos **Probabilidad** en el objeto Riesgo.

  El campo Probabilidad se calcula identificando el rango de umbral en el que cae el valor de la Frecuencia. Si algún valor de Frecuencia es nulo, el valor anterior se gestiona como la frecuencia MAX.

  **Tabla 2. Valor de probabilidad basado en el valor de frecuencia**

  | Valor de frecuencia | Valor de probabilidad |
  | --- | --- |
  | > = 0 y < = Frecuencia 1 | 1 |
  | > Frecuencia 1 y < = Frecuencia 2 | 2 |
  | > Frecuencia 2 y < = Frecuencia 3 | 3 |
  | > Frecuencia 3 y < = Frecuencia 4 | 4 |
  | > Frecuencia 4 y < = Frecuencia 5 | 5 |
  | > Frecuencia 5 y < = Frecuencia 6 | 6 |
  | > Frecuencia 6 y < = Frecuencia 7 | 7 |
  | > Frecuencia 7 y < = Frecuencia 8 | 8 |
  | > Frecuencia 8 y < = Frecuencia 9 | 9 |
  | > Frecuencia 9 | 10 |
- Calcula la exposición multiplicando la gravedad por la frecuencia
- Donde el valor de impacto es `X` y el valor de probabilidad es `Y`:

  El valor XMAX es el valor máximo para el impacto. El valor de YMAX es el valor máximo para la probabilidad.

  Los valores de XMAX y YMAX están disponibles en `/OpenPages/Application/GRCM/ORM/Triggers/RCSA/XMAX` y `/OpenPages/Application/GRCM/ORM/Triggers/RCSA/YMAX`.

  Los valores de XMAX y YMAX se definen durante la instalación. No cambie estos valores. Si se cambian estos valores, es posible que los desencadenantes de RCSA cualitativas y cuantitativas no calculen correctamente la valoración de riesgo.

  El desencadenante calcula la valoración de riesgo utilizando la fórmula siguiente:

  `((X x X) + (Y x Y)) / ((Xmax x Xmax) + (Ymax x Ymax))`

  El valor de valoración es `0 - 1` y se expresa como un porcentaje.

  **Tabla 3. Valoraciones de riesgos basadas en valores de valoración**

  | Valor de valoración | Valoración de riesgos |
  | --- | --- |
  | 0 - 25 % | BAJO (verde) |
  | 26-50 % | MEDIO (amarillo) |
  | 51-75 % | ALTO (naranja) |
  | 76-100 % | MUY ALTO (rojo) |

##### Activador de RCSA cualitativas

El desencadenante de Autoevaluaciones de riesgo y control (RCSA) cuantitativas establece la valoración de riesgo y establece la gravedad, la frecuencia y la exposición para los riesgos que se especifican con el método Cualitativo.

> **Importante:** Determine el método que se debe utilizar para evaluar los riesgos: cuantitativos o cualitativos. Si elige cuantitativo, este desencadenante no se aplica. La opción cuantitativa o cualitativa se establece durante la instalación de las soluciones de IBM OpenPages .

Añada el campo Método de evaluación a Vistas de tareas para riesgo. El valor de este campo determina si se desencadena el método Cualitativo o Cuantitativo.

Cuando un objeto **Riesgo** se actualiza, asocia o desasocia, el desencadenante lleva a cabo las acciones siguientes:

- Evalúa el registro de preferencia para la entidad o su entidad padre si no existe ningún registro de preferencia.

  El desencadenante intenta encontrar el objeto de preferencia asociado con la entidad empresarial. El desencadenante recorre la jerarquía de entidades padre hasta que se encuentra un objeto de preferencia asociado a una entidad empresarial. El objeto de preferencia contiene los valores para los parámetros necesarios tal como se describe en la tabla Gravedad.
- Evalúa los campos **Gravedad** del objeto de riesgo.

  La gravedad viene determinada por las correlaciones de valor de impacto que se especifican en el objeto de Riesgo. Por ejemplo, si el valor de impacto de objeto de riesgo es 1, el riesgo es 1. Si el valor de impacto es 2, la gravedad es 2, y así sucesivamente. El valor de impacto máximo para un objeto de riesgo es 10, para el que la gravedad es 10.
- En función de la probabilidad, evalúa los campos de frecuencia del objeto de riesgo.

  La frecuencia se determina mediante las correlaciones de valor de probabilidad que se especifican en el objeto de riesgo. Por ejemplo, si el valor de probabilidad de objeto de riesgo es 1, la frecuencia es 1. Si el valor de probabilidad es 2, la frecuencia es 2, y así sucesivamente. El valor de máxima probabilidad para un objeto de riesgo es 10, para el que la frecuencia es 10.
- Calcula la exposición como una gravedad multiplicada por la frecuencia.
- Donde el valor de impacto es `X`, el valor de probabilidad es `Y`:

  El valor XMAX es el valor máximo para el impacto. El valor de YMAX es el valor máximo para la probabilidad.

  Los valores de XMAX y YMAX están disponibles en `/OpenPages/Application/GRCM/ORM/Triggers/RCSA/XMAX` y `/OpenPages/Application/GRCM/ORM/Triggers/RCSA/YMAX`.

  Los valores de XMAX y YMAX se definen durante la instalación. No cambie estos valores. Si se cambian estos valores, es posible que los desencadenantes de RCSA cualitativas y cuantitativas no calculen correctamente la valoración de riesgo.

  El desencadenante calcula la valoración de riesgo utilizando la fórmula siguiente:

  `((X x X) + (Y x Y)) / ((Xmax x Xmax) + (Ymax x Ymax))`

  El valor de valoración es `0 - 1` y se expresa como un porcentaje.

  **Tabla 4. Valoraciones de riesgos basadas en valores de valoración**

  | Valor de valoración | Valoración de riesgos |
  | --- | --- |
  | 0 - 25 % | BAJO (verde) |
  | 26-50 % | MEDIO (amarillo) |
  | 51-75 % | ALTO (naranja) |
  | 76-100 % | MUY ALTO (rojo) |

#### Desencadenantes de ciclo de vida de KRI y KPI (existentes)

`Guía de soluciones › Características heredadas › Activadores heredados` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=triggers-kri-kpi-lifecycle-legacy)

Los activadores del ciclo de vida de KRI y KPI calculan y mantienen valores de campo en los tipos de objeto KRI/KPI y Valor de KRI/KPI.

> **Nota:** Si está utilizando los desencadenantes de ciclo de vida de KRI y KPI, considere la posibilidad de utilizar los flujos de trabajo de KRI y KPI en su lugar. Para obtener más información, consulte [Flujos de trabajo de ejemplo](#flujos-de-trabajo-de-ejemplo).

El desencadenante del ciclo de vida de KRI o KPI solo se ejecuta si el valor **Estado de recopilación** del valor de KRI o KPI se establece en **Recopilado** y los campos **Valor** y **Fecha de valor** no están en blanco.

Cuando un objeto Valor de KRI o KPI se actualiza, se asocia o disocia, el activador realiza las siguientes acciones:

1. Determina si el KRI o KPI se ha establecido para aprobación.

   - Si el estado es **Sí**, el activador actualiza el estado a **En espera de aprobación** y continúa con los pasos 2, 3, 4 y 6.
   - Si el estado es **No**, el activador actualiza el estado de **En espera de recopilación** a **Recopilado** y continúa con los pasos 2, 3, 4 y 5.
2. Copia la información de umbral actual desde el KRI o KPI al valor KRI o KPI secundario.
3. Evalúa el estado de incumplimiento.
4. Copia el estado **Valor**, **Fecha del valor**, **Recopilación** e **Incumplimiento** del KRI o KPI en el KRI o KPI principal.
5. Si el estado del campo **Incumplimiento** del KRI o KPI cambia de **Verde** o **Ámbar** a **Rojo**, el activador envía una notificación por correo electrónico al propietario del riesgo para informarle del incumplimiento.
6. Si el estado se establece en **Pendiente de aprobación**, el valor de KRI o KPI se visualiza en el panel de control del propietario de KRI o KPI. El propietario del KRI o KPI puede aprobar o rechazar el valor:

   - Si el propietario de KRI o KPI guarda el registro con un estado de **Rechazar**, el **Valor** de KRI o KPI, **Fecha de valor** y el campo **Aprobar/rechazar** se cambian por un espacio en blanco y el estado de valor de KRI o KPI se establece en **Pendiente de recopilación**.
   - Si el propietario del KRI o KPI guarda el registro con el estado de **Aprobado**, el estado **Recopilación** cambia a **Recopilado** en el campo **Valor** y en el KRI o KPI.

   > **Nota:** Cuando el propietario del KRI o KPI define el KRI o KPI, el propietario puede especificar los detalles relativos a su aprobación.

### Tipos de objetos existentes

`Guía de soluciones › Características heredadas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=features-legacy-object-types)

Las soluciones de IBM OpenPages® incluyen varios tipos de objeto que no están habilitados en instalaciones nuevas.

- **Modelo de capital**

  El objeto Modelo de capital se utiliza para almacenar resultados de modelos de capital de riesgo operativo derivados utilizando el enfoque de medición avanzado (AMA).

- **Resultado de modelo de capital (ModelResult)**

  El objeto Resultado del modelo de capital es la estimación de capital de riesgo operativo resultante o la distribución de pérdida agregada que resulta de la simulación de las distribuciones de frecuencia y gravedad mejor ajustadas seleccionadas. Cada Resultado del modelo de capital se asocia a un objeto Modelo de capital. Para Modelos únicos (Modelos de escenario, Modelo de pérdidas internas, Modelo de pérdidas FIRST), se visualiza un Valor en riesgo individual (VaR) a diferentes percentiles (el número y valor de los percentiles se puede configurar). Para los Modelos independientes y correlacionados, el capital se muestra para VaR individual, ESF aditivo (Déficit esperado) y VaR aditivo a diferentes percentiles (el número y valor de los percentiles se puede configurar).

- **Cuestionario, Sección, Pregunta**

  Los objetos Cuestionario, Sección y Pregunta se utilizan conjuntamente para implementar cuestionarios. Los cuestionarios se crean como plantillas en una biblioteca y recopilan información de los encuestados. Los objetos Sección, son hijos de objetos Cuestionario padre y organizan conjuntos de preguntas relacionadas. Los objetos Pregunta son hijos de los objetos Sección y capturan datos del encuestado. Los administradores empresariales utilizan la vista de actividad de configuración de cuestionario para configurar plantillas de cuestionarios. Las plantillas de cuestionario se copian después a tipos de objeto Entidad de negocios, Proceso, Subproceso o Empleado.

  Los cuestionarios no están relacionados con las evaluaciones de cuestionario. La información que describen los cuestionarios no se aplica a evaluaciones de cuestionario.

- **Hitos, Elemento de acción de hitos**

  Un hito representa un punto significativo en el desarrollo de su proyecto. Puede relacionar hitos con fechas específicas, o utilizarlos para señalar la terminación de una parte del proyecto. Los hitos pueden contener otros hitos o elementos de acción de hitos. No puede asociar un hito con otros objetos de la jerarquía de objetos.

  Un elemento de acción de hito es un objetivo específico que debe finalizarse para alcanzar un hito. En general, todos los elementos de acción de hito asociados con un hito deben finalizarse para poder alcanzar un hito. Cuando se le asigna un objeto Elemento de acción de hitos, se visualiza (si está configurado) en la sección Elementos de acción de Mi hito de la pestaña Mi trabajo.

### Informes y ayudantes ya existentes

`Guía de soluciones › Características heredadas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=features-legacy-reports-helpers)

Los informes disponibles en las soluciones de IBM OpenPages® han cambiado.

- **Programa de utilidad Creación de valor de KRI**

  Este ayudante se ha sustituido por cálculos y flujos de trabajo. Consulte el flujo de trabajo [Creación de valor KRI](#flujos-de-trabajo-de-ejemplo) .

- **Programa de utilidad Creación de valor de KPI**

  Este ayudante se ha sustituido por cálculos y flujos de trabajo. Consulte [Flujo de trabajo de creación de valor de KPI y flujo de trabajo de entrada de valor de KPI](#flujos-de-trabajo-de-ejemplo).

- **Notificación pendiente de KRI**

  Este ayudante se ha sustituido por cálculos y flujos de trabajo. Véase [entrada de valor KRI](#flujos-de-trabajo-de-ejemplo).

- **Notificación pendiente de KPI**

  Este ayudante se ha sustituido por cálculos y flujos de trabajo. Consulte [Flujo de trabajo de creación de valor de KPI y flujo de trabajo de entrada de valor de KPI](#flujos-de-trabajo-de-ejemplo).

- **Asistente de finalización de escenario**

  Este ayudante se ha sustituido por cálculos y flujos de trabajo. Consulte los flujos de trabajo [Desarrollo y pruebas de escenario](#flujos-de-trabajo-de-ibm-openpages-business-continuity-management-bcm) y [Prueba de escenario de servicio empresarial](#flujos-de-trabajo-de-ibm-openpages-business-continuity-management-bcm) .

  Elimine el campo Asistente de análisis de escenario de las vistas.

- **Informes de prueba**

  - El informe de panel de control de pruebas se ha sustituido por el informe de rendimiento y resultados de pruebas
  - El informe Detalles del panel de instrumentos de prueba se ha sustituido por el informe Detalles de prueba

  Para obtener más información, consulte [Prueba de informes](#informes-de-prueba).

- **Informes de eventos de pérdida**

  Los informes siguientes se han sustituido por el Panel de control de eventos de pérdida consolidado y sus informes de detalle:

  - Panel de evento de pérdida
  - Detalle del panel de evento de pérdida
  - Resumen de sucesos de pérdida
  - Detalle del evento de pérdida
  - Tendencia de eventos de pérdidas
  - Detalle de tendencia del evento de pérdida

  Para obtener más información, consulte [Informes de eventos de pérdida](#informes-de-eventos-de-pérdida).

- **Informes de modelado de capital**

  Se han eliminado los siguientes informes:

  - Aportaciones de capital por entidad empresarial
  - Aportaciones de capital por categoría de riesgo
  - Fragmento de resultados del modelo

### Flujos de trabajo y cálculos existentes

`Guía de soluciones › Características heredadas` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=features-legacy-workflows-calculations)

Las soluciones de IBM OpenPages® incluyen varios flujos de trabajo y cálculos que no están habilitados en instalaciones nuevas.

- **Flujo de trabajo de Información del último valor de la métrica de actualización de OpenScale.**

  El flujo de trabajo Actualizar información de último valor de métrica de OpenScale da soporte a la integración de MRG con IBM Watson® OpenScale. Actualiza los campos Información de último valor de métrica en objetos de métrica para modelos de IBM Watson OpenScale con valores del objeto de valor de métrica más reciente que IBM Watson OpenScale ha enviado a OpenPages. El flujo de trabajo actualiza los cuatro campos siguientes en el objeto de métrica:

  - Estado de vulneración
  - Estado de recopilación
  - Valor
  - Fecha del valor

  Este flujo de trabajo se sustituye por el cálculo de actualización de valor de métrica.

- **Análisis del impacto empresarial para determinar procesos críticos**

  Este flujo de trabajo mueve el análisis del impacto empresarial (BIA) a través de un proceso de revisión y aprobación. Se necesita un cálculo en el objeto BIA para moverlo a la fase de aprobación. Después de la aprobación, dos de los valores resultantes del cálculo, Nivel de impacto e Interrupción máxima aceptable, se guardan en el padre de proceso del objeto BIA.

  Este flujo de trabajo está inhabilitado en instalaciones nuevas. Un conjunto de flujos de trabajo de BIA sustituye al flujo de trabajo Análisis de impacto empresarial para determinar procesos críticos.

- **Flujo de trabajo de revisión de política (PCM)**

  Este flujo de trabajo está diseñado para avanzar en un objeto de política a través de un proceso de revisión y aprobación de políticas. Cada acción crea un objeto Comentario de revisión de política (PRC) antes de las fases de revisión (SME, ejecutiva y final) y se asocia con la política en revisión. El PRC captura los comentarios y las aprobaciones para cada revisor. La revisión ejecutiva es opcional, dependiendo de si los cambios de política son sustanciales.

  Este flujo de trabajo se sustituye por el flujo de trabajo de revisión y aprobación de política.

- **Flujo de trabajo Desarrollo de modelo y documentación**

  Este flujo de trabajo toma un modelo a partir de la finalización del proceso de candidato hasta la aprobación para el despliegue. Se compone de cuatro fases y varios subflujos de trabajo que implican a varias partes interesadas:

  - Definición y planificación (propietario del modelo)
  - Desarrollo y documentación (desarrollador de modelo)
  - Revisión previa a la implementación (validación de modelo)
  - Aprobación (responsable de desarrollo de modelos)

  Este flujo de trabajo se sustituye por el flujo de trabajo Ciclo de vida de modelo.

## Avisos

`Guía de soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=sg-notices)

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
