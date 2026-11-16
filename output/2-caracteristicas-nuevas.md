---
product: IBM OpenPages 9.1.3
product_key: SSFUEU_9.1
file: 2
guide: Características nuevas
covers: Características nuevas — Avisos
chapters: 15
topics: 47
words: 34252
tasks: 0
concepts: 47
references: 0
tables: 8
code_blocks: 2
figures: 186
applies_to: En cloud
updated: 2026-02-11
lang: es
source: https://www.ibm.com/docs/es/openpages/9.1.x?topic=new-features
extracted: 2026-11-16
---

# 2 · Características nuevas

> **Qué hay en este archivo.** «Características nuevas» de IBM OpenPages 9.1.3, completa: 15 capítulos. 47 temas, 8 tablas, 2 bloques de código, 186 figuras y 34.252 palabras.
>
> **Capítulos:** Características nuevas · Nuevas características de la versión 9.1.3 · Novedades de la versión 9.1.2 · Novedades de la versión 9.1.1 · Nuevas características en la versión 9.1.0 · Novedades de la versión 9.0.0.5 · Novedades de la versión 9.0.0.4 · Características nuevas de la versión 9.0.0.3 · Características nuevas de la versión 9.0.0.2 · Características nuevas de la versión 9.0.0.1 · Características nuevas de la versión 9.0.0 · Características nuevas de la versión 8.3.0.2 · y 3 más.
>
> **Se aplica a:** En cloud.
>
> **Si lo que buscas no está acá.** El índice de los 2.417 temas del producto, con su archivo y su ancla, está en `index.md`.

**Términos propios de este archivo:** risklens, supply, wisdom, cuadrícula, conformidad, sysview, anualizado, etapa, maestro, ámbito, mejorado, comentarios, respuestas, rapidratings.

## Índice de este archivo

- [Características nuevas](#características-nuevas)
- [Nuevas características de la versión 9.1.3](#nuevas-características-de-la-versión-913)
- [Novedades de la versión 9.1.2](#novedades-de-la-versión-912)
- [Novedades de la versión 9.1.1](#novedades-de-la-versión-911)
- [Nuevas características en la versión 9.1.0](#nuevas-características-en-la-versión-910)
- [Novedades de la versión 9.0.0.5](#novedades-de-la-versión-9005)
- [Novedades de la versión 9.0.0.4](#novedades-de-la-versión-9004)
- [Características nuevas de la versión 9.0.0.3](#características-nuevas-de-la-versión-9003)
- [Características nuevas de la versión 9.0.0.2](#características-nuevas-de-la-versión-9002)
- [Características nuevas de la versión 9.0.0.1](#características-nuevas-de-la-versión-9001)
- [Características nuevas de la versión 9.0.0](#características-nuevas-de-la-versión-900)
  - [Mejoras de la interfaz de usuario en 9.0.0](#mejoras-de-la-interfaz-de-usuario-en-900)
  - [Mejoras del flujo de trabajo en 9.0.0](#mejoras-del-flujo-de-trabajo-en-900)
  - [Mejora del etiquetado en 9.0.0](#mejora-del-etiquetado-en-900)
  - [Mejoras del cuestionario en 9.0.0](#mejoras-del-cuestionario-en-900)
  - [Integración del modelo de aprendizaje automático personalizado en 9.0.0](#integración-del-modelo-de-aprendizaje-automático-personalizado-en-900)
  - [Mejoras de filtrado en 9.0.0](#mejoras-de-filtrado-en-900)
  - [Mejoras de soluciones en 9.0.0](#mejoras-de-soluciones-en-900)
  - [Mejoras de administración y capacidad de servicio](#mejoras-de-administración-y-capacidad-de-servicio)
  - [Mejoras de la API en 9.0.0](#mejoras-de-la-api-en-900)
  - [Nueva guía del desarrollador en 9.0.0](#nueva-guía-del-desarrollador-en-900)
  - [Software soportado en 9.0.0](#software-soportado-en-900)
- [Características nuevas de la versión 8.3.0.2](#características-nuevas-de-la-versión-8302)
  - [Notificaciones de etapa de flujo de trabajo personalizado en 8.3.0.2](#notificaciones-de-etapa-de-flujo-de-trabajo-personalizado-en-8302)
  - [IBM OpenPages Gestión de riesgos para ESG](#ibm-openpages-gestión-de-riesgos-para-esg)
  - [Mejoras en la integración de modelos de IA en 8.3.0.2](#mejoras-en-la-integración-de-modelos-de-ia-en-8302)
  - [Mejoras en IBM OpenPages Regulatory Compliance Management en 8.3.0.2](#mejoras-en-ibm-openpages-regulatory-compliance-management-en-8302)
- [Características nuevas de la versión 8.3.0.1](#características-nuevas-de-la-versión-8301)
  - [Integración de modelos de IA](#integración-de-modelos-de-ia)
  - [Mejoras en IBM OpenPages Regulatory Compliance Management](#mejoras-en-ibm-openpages-regulatory-compliance-management)
  - [Mejoras de la gestión de riesgos de terceros en 8.3.0.1](#mejoras-de-la-gestión-de-riesgos-de-terceros-en-8301)
  - [Cuestionarios](#cuestionarios)
  - [Etiquetas](#etiquetas)
  - [Gráficos de tendencias basados en el historial de cambios de los valores de campo](#gráficos-de-tendencias-basados-en-el-historial-de-cambios-de-los-valores-de-campo)
- [Nuevas características en la versión 8.3.0](#nuevas-características-en-la-versión-830)
  - [Mejoras de la plataforma en 8.3.0](#mejoras-de-la-plataforma-en-830)
  - [Mejoras de soluciones en 8.3.0](#mejoras-de-soluciones-en-830)
    - [Mejoras en la gestión de continuidad de negocio en 8.3.0](#mejoras-en-la-gestión-de-continuidad-de-negocio-en-830)
    - [Mejoras de la Gestión de privacidad de datos en 8.3.0](#mejoras-de-la-gestión-de-privacidad-de-datos-en-830)
    - [Mejoras de Gobierno de TI en 8.3.0](#mejoras-de-gobierno-de-ti-en-830)
    - [Mejoras en el gobierno de riesgos de modelo en 8.3.0](#mejoras-en-el-gobierno-de-riesgos-de-modelo-en-830)
    - [Mejoras en la gestión de riesgos operativos en 8.3.0](#mejoras-en-la-gestión-de-riesgos-operativos-en-830)
    - [Mejoras en la gestión de políticas en 8.3.0](#mejoras-en-la-gestión-de-políticas-en-830)
    - [Mejoras en la gestión de conformidad reguladora en 8.3.0](#mejoras-en-la-gestión-de-conformidad-reguladora-en-830)
    - [Mejoras en la gestión de riesgos de terceros en 8.3.0](#mejoras-en-la-gestión-de-riesgos-de-terceros-en-830)
  - [Software soportado en 8.3](#software-soportado-en-83)
- [Avisos](#avisos)


# Características nuevas

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=new-features)

La *Guía de nuevas funciones deIBM OpenPages* está destinada a los usuarios que deseen conocer las nuevas funciones de la última versión de ' IBM OpenPages®. Para obtener más información sobre las características nuevas y cambiadas, consulte los documentos específicos del producto, por ejemplo guías de instalación y guías de usuario.

Los temas de la publicación *IBM OpenPages Guía de características nuevas* cubren los releases y fixpacks principales que incluyen características nuevas. Los arreglos provisionales y los fixpacks que no incluían características nuevas no están cubiertos.

Para obtener una lista de los arreglos de cada release, consulte la Lista de arreglos para dicho release. Puede acceder a las listas de correcciones desde el [portal de soporte de IBM](https://www.ibm.com/mysupport).

Además, puede ver una lista completa de solicitudes de mejoras (RFE) entregadas en cada release. Para obtener más información, consulte [Solicitudes de mejoras (RFE) entregadas por release](https://www.ibm.com/support/pages/node/1073770).

## IBM OpenPages documentación

IBM® mantiene un conjunto de servicios de documentación IBM OpenPages, IBM OpenPages for IBM Cloud Pak for Datay IBM OpenPages on Cloud despliegues. La documentación de IBM OpenPages describe determinadas características y funciones que pueden no estar disponibles en la nube.

Si tiene alguna pregunta sobre la funcionalidad disponible en la versión del producto que está utilizando, póngase en contacto con el soporte deIBM a través del [portal de soporte de IBM](https://www.ibm.com/mysupport).

## Funciones de accesibilidad

Las características de accesibilidad ayudan a los usuarios que tienen alguna discapacidad física, por ejemplo movilidad restringida o visión limitada, a utilizar productos de tecnología de la información. La documentación de OpenPages tiene características de accesibilidad. Los documentos PDF son complementarios y no incluyen características de accesibilidad.

## Características y mejoras

Puede revisar las características y mejoras del release actual y de los releases anteriores.

## Nuevas características de la versión 9.1.3

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-913)

La OpenPages®9.1.3 versión incluye GRC Canvas, una nueva experiencia visual dentro de OpenPages, nuevas y mejoradas funciones en IA, experiencia general de tareas del usuario y administración.

Consulte las siguientes categorías para obtener más información sobre las nuevas funciones:

- Lienzo GRC
- Mejoras en IA
- Mejoras en la interfaz de usuario centradas en las tareas
- Controles y configuraciones de administración

### Lienzo GRC

- **GRC Canvas: una nueva experiencia visual dentro de OpenPages**

  GRC Canvas proporciona una interfaz visual dentro de IBM OpenPages para mapear las relaciones entre riesgos, controles, procesos o cualquier otro objeto. Permite a los usuarios crear y configurar lienzos para los tipos de objetos compatibles basándose en los datos que ya se encuentran en OpenPages. Los usuarios pueden añadir OpenPages objetos o nodos personalizados y añadir anotaciones con nodos de texto. Dentro del lienzo, los usuarios podrán crear y agrupar nodos, aplicar colores, gestionar los campos mostrados y acceder a sus datos directamente desde el lienzo. El control de versiones se admite a través de los estados de borrador y publicado, con detección de conflictos y gestión de cambios para mantener los diagramas alineados con los datos subyacentes. Los permisos y el acceso a los objetos se transfieren al lienzo. Para obtener más información, consulte [Visualización del riesgo y el cumplimiento mediante Canvas](4-guia-del-usuario.md#visualización-del-riesgo-y-el-cumplimiento-mediante-canvas).

  *Figura 1. Ejemplo de un lienzo de evaluación de riesgos*

  ![Diseño en lienzo de un objeto de evaluación de riesgos con nodos principales y nodos secundarios agrupados.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/canvas_nfg.png)

### Mejoras en IA

- **Servidor MCP local para operaciones de IA en objetos**

  El servidor MCP solo se implementa localmente y proporciona una interfaz estandarizada que permite a los agentes de IA realizar operaciones sobre OpenPages objetos, como incidencias y controles.

  > **Nota:**

  > Esta es una función beta de la versión 9.1.3 de OpenPages. El servidor MCP se puede implementar localmente dentro de un sistema de agentes, como watsonx Orchestrate. El servidor MCP local solo se puede utilizar en desarrollo para explorar casos de uso de agentes. Para implementar el servidor MCP en su entorno local, utilice el [repositorio de código abierto IBM OpenPages del servidor MCP local](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2FIBM%2Fibm-openpages-local-mcp-server).

- **Gestionar entradas y salidas de enumeraciones multivalor en modelos**

  Se ha añadido compatibilidad con campos enumerados multivalor en las entradas y salidas de los modelos, lo que reduce los errores y mejora la integración de los modelos.

- **Compatibilidad avanzada con JSON y entrada de expresiones**

  La interfaz de usuario de configuración del aprendizaje automático (ML) ahora admite conmutadores de entrada JSON avanzados y la introducción de expresiones, lo que agiliza la configuración del modelo y mejora la usabilidad.

  *Figura 2. Configuración del aprendizaje automático con expresión JSON*

  ![Ventana de expresión para entrada JSON](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/json_expression_ml.png)

- **Ampliaciones de API**

  - **Conectividad flexible de modelos de IA a través de extensiones API**

    Habilite OpenPages para conectarse con cualquier modelo de IA a través de API, como OpenAIChatGPT, Mistral AI, otros LLM o terminales de ML. Al permitir a los administradores crear nuevos complementos de integración, OpenPages las implementaciones pueden conectarse virtualmente con cualquier solución externa que exponga una API. Esto permite enviar y recibir datos sin problemas, aprovechando el marco existente Bring Your Own Model (BYOM) para analizar y procesar la información.

    *Figura 3. Configuración de la extensión para OpenAI el modelo*

    ![Editar ventana de configuración de la extensión con OpenAI especificaciones.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/connect_ai_model_api_ext.png)

  - **Gestionar extensiones API en la interfaz de usuario de modelos de aprendizaje automático personalizados**

    Se ha introducido una nueva interfaz de usuario para gestionar las extensiones API en modelos ML personalizados, lo que hace que la configuración sea más intuitiva y accesible.

    *Figura 4. Configuración personalizada del modelo de aprendizaje automático para gestionar las extensiones de la API*

    ![Ventana de configuración personalizada del modelo de aprendizaje automático con una conexión correcta a la extensión Mistral.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/custom_ml_api_connection_ui.png)

  - **Mejora las extensiones API con registro y trazabilidad**

    Se han añadido capacidades de registro y seguimiento a las extensiones de la API, lo que mejora la facilidad de mantenimiento y la depuración de los complementos de integración.

    *Figura 5. Registro y trazabilidad para extensiones API*

    ![Las extensiones en el panel de opciones de tracción del sistema están activadas.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/log_trace_api_ext.png)

  - **Habilitar la migración de configuraciones de extensiones API**

    Migrar las configuraciones de la extensión API, garantizando transiciones más fluidas entre entornos y simplificando los procesos de actualización.

    *Figura 6. Extensiones de la API de exportación*

    ![Elemento de extensión Mistral para exportar](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/export_api_ext.png)

### Mejoras en la interfaz de usuario centradas en las tareas

- **Permitir la vista de tareas y las modificaciones de sección para campos ocultos**

  Ahora los usuarios pueden anular la configuración de visibilidad en las vistas de tareas y secciones, ocultando o mostrando los campos según sea necesario. Esta flexibilidad mejora la personalización y el control sobre las interfaces de usuario.

- **Añadir campos de recuento a diseños compactos y de tabla**

  Ahora se pueden incluir campos de texto y recuento personalizados en diseños compactos y tabulares, lo que mejora la visibilidad de los datos y permite obtener resúmenes más informativos.

  *Figura 7. Diseño compacto de tabla para presupuesto y calendario con campos de texto y recuento personalizados*

  ![Diseño de tabla compacto para el presupuesto y el calendario con la fecha de inicio y finalización, las horas y los campos de texto personalizado y recuento de T&E.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/count_fields_table_layout.png)

- **Cambiar entre períodos de informe**

  Al cambiar los períodos de informe, las pestañas abiertas ahora permanecen abiertas. La interfaz de usuario se adapta al período seleccionado, mejorando la navegación y la claridad.

### Controles y configuraciones de administración

- **Ocultar el botón Mover en las vistas de cuadrícula**

  Los administradores ahora pueden configurar la interfaz de usuario para ocultar el botón **Mover** en las vistas de cuadrícula para tipos de objetos específicos, lo que ayuda a aplicar un control más estricto sobre la gestión de objetos.

- **Capacidad del administrador para mover objetos que no son entidades**

  Los administradores ahora pueden mover uno o más objetos de cualquier tipo que no sea entidad a un objeto de destino, lo que incluye la detección de todos los elementos secundarios del objeto seleccionado. Se trataría de un movimiento jerárquico, lo que significa que, para el objeto que se está moviendo, los elementos secundarios que se encuentran debajo de él también se moverían (primarios y no primarios). Para el objeto que se está moviendo, la ruta de la carpeta principal de sus hijos cambiará. En el caso del objeto que se mueve, los hijos no primarios también se moverían, pero su ruta solo cambiaría si el padre de los hijos no primarios es un hijo primario del objeto que se está moviendo.

- **Admite reglas entre objetos para cálculos en tiempo de ejecución**

  Ahora se admiten reglas entre objetos en los cálculos en tiempo de ejecución, lo que permite la agregación de datos entre objetos relacionados sin consultas persistentes.

### Soporte para 12.1.1Cognos AnalyticsIBM y Db2 12.1.3

OpenPages Ahora es compatible con 12.1.1Cognos® AnalyticsIBM® y Db2® 12.1.3, lo que garantiza la compatibilidad con las últimas versiones para mejorar el rendimiento y la integración.

## Novedades de la versión 9.1.2

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-912)

La versión OpenPages® 9.1.2 incluye funciones nuevas y mejoradas en IA, experiencia general de la tarea del usuario, administración y flujos de trabajo.

### Crear objeto hijo a partir de la salida de la IA generativa

Ahora los usuarios pueden generar objetos hijos, como elementos de acción o controles, basándose en los resultados de la IA generativa. Esta función agiliza la creación de contenidos y ayuda a los usuarios a actuar de forma más eficiente a partir de la información generada por la IA. ![Crear objetos hijo a partir de sugerencias de salida de IA](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/child_obj_genai.png)

### Mostrar objetos no relacionados en las vistas de tareas para contextualizar

Las vistas de tareas ahora pueden incluir objetos no relacionados/contextuales, filtrados por reglas o etiquetas. Esto proporciona a los usuarios el contexto pertinente, como siniestros similares o controles aplicables, lo que mejora la toma de decisiones y la calidad de los datos de IA.

Esto permite enviar información extra que proporciona un contexto adicional para que el agente de IA proporcione la información adecuada. Esto desbloquea un nuevo conjunto de un caso de uso como el siguiente:

- Similitudes de asuntos - donde el Agente de IA puede recibir asuntos relevantes con los que comparar (asuntos en el negocio, abiertos en los últimos años).
- Sugerencias de controles - donde la solución puede enviar la lista actual de controles de la biblioteca.

![Control en el diseñador de vistas con el tipo de relación contextual seleccionado](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ctrl_task_relation_type.png)

A continuación se muestra un ejemplo de similitud de asuntos:

![Emitir panel de percepciones de similitud en la vista de tareas](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/issue_similarity_example.png)

### Permitir que el administrador obtenga la objectJson para la entrada de vista

Ahora los administradores pueden exportar fácilmente la dirección objectJson exacta enviada a los modelos de IA cuando se utiliza una **vista** como entrada. Esta mejora simplifica la configuración de los avisos.

![Exportar objeto Json para entrada AI en una Vista](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/objJson_ai_input_views.png)

### Añadir más campos a las rejillas para la IA y las vistas de usuario

Se ha aumentado de 6 a 10 el número máximo de campos por objeto en las rejillas. Esto permite mostrar datos más completos y utilizarlos en vistas basadas en IA.

### Soporte de Markdown para agilizar la presentación visual de los resultados de la IA

El soporte de Markdown permite que la salida de AI tenga un formato organizado, incluyendo encabezados, viñetas y enlaces que permiten enlazar dentro de las pestañas de OpenPages , por lo que el prompt es mucho más fácil de construir.

![Ejemplo Markdown de salida AI](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/markdown_example_aioutput.png)

### Visualizar los datos relativos a la hora en las zonas horarias locales de los usuarios

Los usuarios de las implantaciones globales de OpenPages ahora pueden ver la información relacionada con la hora -como las fechas de los objetos, los registros de actividad y las horas de inicio de sesión- en su zona horaria local. Esta mejora aumenta la claridad y reduce la confusión a la hora de colaborar entre regiones.

![Visualización de datos horarios para usuarios en implantaciones globales](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/users_time_data.png)

### Posibilidad de añadir una etiqueta a un campo de enlace - Mejora de Markdown

Los usuarios tienen ahora la posibilidad de añadir una etiqueta a un campo que sea un enlace. El campo URL utiliza ahora el altLabel definido en la configuración del campo. En lugar de mostrar el texto en bruto URL, la interfaz de usuario muestra el texto altLabel. Cuando el usuario hace clic en este texto, se le redirige a la página URL. Esto puede verse siempre que se muestre un campo de tipo enlace en la interfaz de usuario.

![Etiqueta para un campo de texto de enlace con la palabra clave de configuración altLabel](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/altlabel_link.png)

### Personalice las vistas de las tareas con diseños de tabla compactos y editables

Una nueva opción de diseño compacto permite a los usuarios organizar los campos en formato de tabla dentro de las vistas de tareas. Esto facilita la lectura y la interacción con la información relacionada, especialmente cuando se trata de varios campos. Los usuarios pueden definir los encabezados de las columnas y filas, y los campos siguen siendo editables en función de los controles de acceso.

![Diseño compacto de tablas en la vista de tareas](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/compact_table_layout.png)

### Bloquear el panel de comentarios cuando se bloquea un objeto

Para evitar comentarios no autorizados o involuntarios, ahora el panel de comentarios se bloquea cuando se bloquea el objeto asociado. Esto garantiza que no se puedan añadir o modificar comentarios sin el conocimiento del propietario del objeto.

### Ver los datos de la cuadrícula como tarjetas para una mejor legibilidad

Ahora los usuarios pueden cambiar entre los diseños de cuadrícula y tarjeta para la presentación de los datos. La disposición en tarjetas es especialmente útil en pantallas pequeñas y mejora la legibilidad de los datos más consumibles. Los administradores pueden configurar los diseños predeterminados y permitidos.

![Disposición de las tarjetas en la vista en cuadrícula](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/card_layout_grids.png)

### Exportar las respuestas del cuestionario de evaluación al formato xlsx en la fase de recogida de información

Ahora los usuarios pueden exportar las respuestas de la Evaluación de cuestionarios en la etapa de recopilación de información junto con las demás etapas del ciclo de vida de un cuestionario.

### Copiar objetos hijo al duplicar una respuesta de cuestionario

Al copiar una respuesta de un cuestionario, los usuarios ahora pueden elegir copiar las relaciones hijo. Esto agiliza el proceso de duplicación y garantiza la conservación de los datos relacionados. Los usuarios podrán ver una nueva opción llamada **Copiar hijo relacionado** bajo la operación **Copiar objeto** en las acciones de respuesta del modelo de cuestionario.

### Fusionar ediciones concurrentes no conflictivas

OpenPages ahora permite fusionar ediciones simultáneas cuando se realizan cambios en campos diferentes. Esto reduce el riesgo de perder trabajo por errores de concurrencia y mejora la experiencia de edición en entornos colaborativos.

### Posibilidad de tener varios periodos de información

Los administradores ahora tienen la capacidad de crear múltiples periodos de informes, permitiendo a los usuarios cambiar entre periodos de informes en el Registro de Actividad. De este modo, se puede pasar de un periodo a otro sin problemas, lo que permite un seguimiento y un análisis más precisos de los datos históricos.

Además, los objetos que existan en el período de informe actual seguirán reflejados y no se actualizarán.

![Seleccionar un período de informe para una acción en el registro de actividades](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/switch_periods_activity_log.png)

### Exportar las respuestas al cuestionario y los datos de evaluación

Ahora los administradores pueden exportar las respuestas de la Evaluación del cuestionario a archivos CSV utilizando la función de Exportación de datos. Esta función permite mejorar el análisis de datos y la elaboración de informes para tipos de objetos no estándar.

### Ejecutar cálculos sobre los objetos seleccionados desde la vista en cuadrícula

Ahora los administradores pueden seleccionar objetos específicos de una vista en cuadrícula y realizar cálculos sobre ellos. Este enfoque selectivo ahorra tiempo y recursos en comparación con la ejecución de cálculos en todos los objetos aplicables.

![Seleccione el cálculo de ejecución para los elementos de la vista en cuadrícula de Activos](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/obj_run_calc.png)

### Integración de Webhooks

Ahora puede integrarse con Webhooks para permitir la comunicación en tiempo real basada en eventos entre OpenPages y sistemas externos. Esta nueva función permite a los usuarios configurar Webhooks salientes que activan automáticamente las devoluciones de llamada de HTTP cuando se producen eventos específicos en la plataforma, como la creación, actualización, eliminación, asociación y disociación de registros. Esta función permite a desarrolladores y administradores crear soluciones con mayor capacidad de respuesta e interconectadas utilizando OpenPages.

### Ejecute varios flujos de trabajo en paralelo

Los flujos de trabajo que no requieren la interacción del usuario ahora pueden ejecutarse simultáneamente con otros flujos de trabajo. Esto permite automatizar acciones específicas sin interrumpir los procesos en curso, lo que mejora la eficacia y la flexibilidad.

A continuación se muestra un ejemplo de flujo de trabajo automatizado que puede utilizarse para realizar automáticamente las siguientes tareas:

- Crear objetos
- Cálculo de la ejecución
- Ejecutar un agente de IA

![Ejemplo de flujo de trabajo automatizado que ejecuta múltiples tareas automáticamente](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/automated_workflow.png)

### Hacer editables los campos de sólo lectura en las anulaciones de la vista de tareas

Ahora los administradores pueden anular las vistas de tareas para que los campos de sólo lectura sean editables. Esto proporciona una mayor flexibilidad a la hora de personalizar los flujos de trabajo sin alterar la configuración de seguridad subyacente.

### Configurar relaciones múltiples en flujos de trabajo de creación de objetos

Las operaciones de flujo de trabajo para crear objetos ahora admiten la configuración de relaciones múltiples. Esta mejora simplifica los complejos escenarios de creación de objetos y mejora la vinculación de datos.

![Añadir relaciones múltiples en operaciones de flujo de trabajo](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/multiple_relationships_workflows.png)

## Novedades de la versión 9.1.1

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-911)

OpenPages® 9.1.1 ofrece un amplio conjunto de mejoras en cinco áreas clave:

- IA y automatización: Integración ampliada con watsonx, configuración más inteligente del modelo de IA y automatización activada por el flujo de trabajo.
- Interfaz de usuario y usabilidad: Navegación mejorada, filtrado dinámico, compatibilidad con markdown e interacciones de usuario mejoradas.
- Administración y Data Management : Gestión de entidades más sencilla, exportaciones de datos enriquecidos y procesos de actualización agilizados.
- Datos y visualización: Gráficos más potentes para una mejor comprensión de los datos.
- Integración y feeds: Campos personalizados en RCM Feed.

### Filtro de la carpeta principal de la cuadrícula de asociación

Permite al administrador definir un filtro dinámico en una carpeta. El filtro dinámico se basa en la carpeta del objeto actual; se trata de una mejora del filtro de carpetas actual.

![Vista de diseño de Entidad de Negocio con panel lateral de filtro de carpetas](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/dynamic_filter.png)

Ventaja: Proporciona a los usuarios finales sólo una lista de objetos o actividades que son relevantes para ellos en este momento. En lugar de ver miles de controles, el usuario final sólo vería los controles de la misma entidad empresarial/organización.

### Un filtro público para identificar fácilmente los objetos bloqueados

Ahora puede filtrar objetos bloqueados en las vistas utilizando filtros privados y públicos.

![Nuevo panel de condiciones para Controles con Bloqueo seleccionado](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/locked_object_filtering.png)

### Asociación de hijos en las vistas de creación

Los usuarios pueden asociar elementos existentes como hijos durante el proceso de creación.

![Ver diseñador para la opción Programa con hijos de tipo Relación](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/child_association_creation_view.png)

Utilidad: Los usuarios pueden ahorrar tiempo y asignar hijos en las vistas de creación.

### Grupo de inicio de selector de usuario basado en objetos relacionados

Puede definir el grupo inicial para los campos de selector de usuario basándose en otros campos de usuario de objetos relacionados en el diseñador de la vista de tareas.

![Diseñador de vistas con panel Campo de grupo inicial](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/starting_group_user_selector.png)

### Exportación de cuadrículas anidadas en formato Excel sencillo

El botón de exportación permite ahora exportar la información de una rejilla (con rejilla anidada) en un sencillo formato Excel.

![Panel de exportación de evaluaciones de riesgos con la vista de cuadrícula seleccionada](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/export_simple_excel.png)

Ventajas: Proporciona al usuario la flexibilidad de exportar datos a una hoja de cálculo Excel.

### Plantilla de cuestionario Autorización

Se ha añadido un nuevo permiso para controlar quién puede ser el autor de las Plantillas de cuestionario (es decir, `All/SOX/User Interfaces/Questionnaire Template Authoring`). Sin este permiso de aplicación, los usuarios no pueden ver la pestaña **Editor** de la plantilla de cuestionario.

### Exportar las respuestas de evaluación del cuestionario a xlsx

Los usuarios podrán ahora exportar las respuestas de la evaluación del cuestionario haciendo clic en el botón **Exportar** en las etapas de revisión, aprobación y cierre de una evaluación del cuestionario.

![Evaluación de cuestionario](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/export_questionnaire_response.png)

### Mejoras en el análisis de referencias sobre el terreno

Si se hace referencia a un campo en varios tipos de objeto, ahora se agrupa por tipo de objeto. Ahora se incluyen en el informe los campos que se utilizan en la entrada de eventos de pérdida y en Machine Learning personalizada. Por último, ahora los administradores pueden descargar el análisis mediante un archivo.xlsx.

![Cuadro de diálogo de análisis de referencia de campo](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/field_reference_analysis_box.png)

Utilidad: Proporciona al usuario información sobre dónde se utiliza actualmente el campo, dónde se eliminará y las posibles repercusiones de su eliminación.

### Eliminación de campos para tipos de datos seleccionados

Esta función permite a los usuarios gestionar las configuraciones de campos de forma más eficaz, ya que permite eliminar campos de los grupos de campos definidos. Los usuarios pueden eliminar los campos obsoletos o que ya no son relevantes.

> **Nota:** Los campos de moneda y multiactor no pueden eliminarse mediante esta función.

![Campos de la cuenta con opción de supresión](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/field_delete.png)

Utilidad: Esta funcionalidad ayuda a los usuarios a mantener los datos más limpios, mejorar el rendimiento del sistema y garantizar que sólo se conserva la información relevante para la elaboración de informes y análisis.

### Formato Markdown

Ahora puede utilizar Markdown como tipo de visualización para tipos de datos de cadenas simples y largas. El tipo de visualización le permite tanto editar como previsualizar su Markdown antes de guardarlo, lo que facilita la integración de IA, ya que este es el formato principal para la salida de modelos de IA.

![Tipo de visualización de campo seleccionado a Markdown](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/display_type_markdown.png)

Utilidad: Markdown es ahora compatible como nuevo tipo de visualización para campos de texto, y en una salida personalizada de aprendizaje automático.

### Campos de referencia de etiquetas en los comentarios

Los usuarios pueden hacer referencia a campos en los comentarios utilizando el signo #, lo que permite a los destinatarios navegar directamente al campo de referencia dentro de la vista de la tarea.

![Panel lateral de comentarios con la opción del signo # en el desplegable](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ref_fields_comments.png)

Utilidad: Esta función agiliza la colaboración y reduce el tiempo dedicado a buscar información relevante.

### Mejoras en las cuadrículas anidadas

Los tipos de objetos anidados ahora admiten filtros y órdenes de clasificación.

![Configurar el panel lateral de enlaces de activos anidados con opciones de filtrado y clasificación](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nested_object_filters_sort_orders.png)

### Cabeceras adhesivas en las rejillas

Las cabeceras de las cuadrículas permanecen visibles al desplazarse, lo que mejora su uso en grandes conjuntos de datos.

### Edición de etiquetas Enum en páginas de objetos

Ahora los administradores pueden editar las etiquetas Enum directamente desde la interfaz de usuario de la página de objetos.

![Etiqueta Enum en el panel lateral para editar](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/enum_label_edit.png)

### Soporte de configuración regional

Ahora puede crear locales para ruso y esloveno.

### Migración de entornos para modelos personalizados de aprendizaje automático

Migración de entornos para modelos de IA personalizados.

![Cuadro de diálogo de exportación de modelos personalizados de aprendizaje automático](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/export_custom_ai_models.png)

Ventaja: Soporte de infraestructura para migrar integraciones de IA entre entornos

### Compatibilidad con cuadrículas anidadas en modelos de IA basados en vistas

Ahora puede utilizar cuadrículas anidadas como entrada para modelos de aprendizaje automático personalizados basados en vistas.

Utilidad: Envíe fácilmente los datos correctos al modelo incluyendo todos los objetos relacionados relevantes -hasta 6 campos por objeto, 3 niveles de profundidad. Esta mejora ofrece una mayor flexibilidad a la hora de estructurar los datos, lo que permite realizar predicciones de IA más precisas.

### Activación automática de modelos de IA mediante flujos de trabajo

Los modelos de aprendizaje automático personalizados **Set Fields** y **Set Tags** configurados con acciones automáticas ahora se pueden utilizar como acciones dentro de los flujos de trabajo.

![Panel lateral de operaciones para un flujo de trabajo con la opción Ejecutar un modelo AI como operación.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/workflow_action_run_ai.png)

Ventajas: La ejecución de un modelo de IA ahora se puede activar directamente desde las acciones del flujo de trabajo, lo que agiliza la automatización para las capacidades de campos establecidos y etiquetas establecidas (ejemplo: categorizar automáticamente las incidencias).

### Establezca relaciones automáticamente aprovechando los modelos de IA

Los modelos de aprendizaje automático personalizados para establecer relaciones pueden configurarse ahora para que se ejecuten automáticamente en función de los cambios de entrada y establezcan automáticamente las relaciones en la cuadrícula sin intervención del usuario.

![Edite el cuadro de diálogo de su modelo con la opción Automático seleccionada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/automatic_run_ai_model.png)

Utilidad: Establecer automáticamente relaciones basadas en los resultados del modelo de IA, permitiendo después al usuario simplemente revisar y actualizar los objetos o actividades asociados.

### Watsonx assistant y watsonx orquestan la integración

Ahora se admiten acciones en el asistente watsonx en lugar de la integración basada en diálogos.

![Watsonx asistente de la interfaz de usuario de acciones con el botón Crear acción](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/watsonx_assistant_actions.png)

Utilidad: La perfecta integración con watsonx Assistant y Orchestrate permite capacidades de IA conversacional en OpenPages, aprovechando las variables de acción en lugar del diálogo. Esta es una nueva forma de adjuntar información contextual de una tarea a watsonx Assistant o al Asistente en Orchestrate (por ejemplo: el Asistente puede entender dónde está el usuario, qué perfil tiene, qué objeto está mirando en OpenPages, y como resultado informar al usuario qué tipo de acción o servicio está disponible).

### RCM - Campos personalizados para el feed de Wolters Kluwer

Wolters Kluwer ahora tiene la capacidad de proporcionar campos personalizados para el contenido normativo.

Para habilitar esta función:

- Añadir campos personalizados a Wolters Kluwer
- Añada los campos personalizados a un Grupo de campos en OpenPages. Utilice los mismos nombres de campo que en Wolters Kluwer
- Cuando se ingieren datos de Wolters Kluwer, el proceso comprueba si hay campos personalizados en el XML. En caso afirmativo, el proceso comprueba si existe un campo con el mismo nombre en OpenPages. Si lo hace, el proceso actualiza el campo. Si no, se salta el campo.

Utilidad: La incorporación de la compatibilidad con campos personalizados en el feed RCM de Wolters Kluwer mejora la gestión del contenido normativo.

### Soporte para Cognos 12.1

OpenPages incluye ahora compatibilidad con IBM Cognos Analytics 12.1, además de su compatibilidad con Cognos 12.0.1 y las versiones posteriores 12.0.x.

### Soporte para Db2 12.1

OpenPages incluye ahora compatibilidad con las bases de datos IBM Db2 12.1, además de su compatibilidad con Db2 11.5.5 y las versiones posteriores 11.5.x.

### Soporte del instalador para actualizaciones automáticas de bases de datos

El instalador de OpenPages ahora puede actualizar la base de datos de OpenPages automáticamente como parte del resto de la actualización de OpenPages para las versiones principales y de mods, además de la compatibilidad existente en las versiones de paquetes de correcciones y correcciones provisionales. Los usuarios pueden elegir entre actualizar su base de datos manualmente antes de la actualización de OpenPages, o permitir que el instalador realice la actualización.

### Mover / Renombrar Entidad

Esta versión incluye una nueva función de administración que permite mover y renombrar entidades empresariales por lotes a través de la interfaz de usuario. Esta nueva interfaz de usuario proporciona las mismas capacidades que la [utilidad de línea de comandos Mover/Cambiar nombre de entidad](3.4-guia-del-administrador.md#programa-de-utilidad-movercambiar-nombre-de-entidad) existente.

En el menú de administración, haga clic en **Otros** > **Mover / Renombrar**.

![Operaciones de traslado y cambio de nombre de entidades empresariales.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/move_rename_business_entitities.png)

Utilidad: Ahora los administradores pueden renombrar o mover entidades directamente a través de la interfaz de usuario.

### Lógica de interfaz de usuario simplificada para la validación de acciones de flujo de trabajo

Se ha simplificado la compleja lógica de la interfaz de usuario para mejorar su comprensión.

![Creación de elementos de acción con la pestaña Lógica expandida.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ui_logic.png)

### La exportación de datos ahora incluye etiquetas

La exportación incluye ahora etiquetas para los tipos de objetos seleccionados.

### Mejoras en los gráficos

Ahora los gráficos admiten campos de selección múltiple. Mejora de la visualización de gráficos con más de 10 elementos utilizando un cubo "Otros".

![Gráfico de barras con campos de selección múltiple](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/chart_multi_select.png)

## Nuevas características en la versión 9.1.0

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-910)

La versión 9.1.0 de OpenPages® incluye mejoras en los modelos personalizados de aprendizaje automático, comentarios de objetos, cuestionarios, compatibilidad nativa con OAuth 2.0, exportación de datos y mucho más.

### Uso de vistas para enviar campos de entrada a modelos personalizados

En versiones anteriores de OpenPages, un administrador podía especificar campos de objeto para utilizarlos como entrada en un modelo personalizado. Los administradores ahora pueden configurar una vista de tareas o informes que contenga los campos de datos de entrada ( OpenPages ) que desean que procese el modelo. Excepto los campos de relación de gráfico, todos los campos de objeto y de relación de la vista se envían como entrada al modelo.

Para obtener más información sobre cómo crear un modelo que utilice una vista como entrada, consulte el tema [Configuración de entradas de modelo](3.5-guia-del-administrador.md#configuración-de-entradas-de-modelo) en *la Guía del administrador de IBM OpenPages.*

Dado que los usuarios necesitan una forma de acceder a la información de un modelo, el administrador añade **un botón Ver información de IA** a una vista en View Designer. La vista puede ser una vista de creación, vista de tareas, vista de administración (utilizada por los administradores) o vista de informe. Cuando el administrador configura el botón, especifica el modelo que se ejecutará y la vista que se utilizará como entrada. Después de que el administrador publique la vista, el usuario puede hacer clic **en Ver perspectivas** ![Botón Ver perspectivas](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ai-launch.png) para mostrar las perspectivas del modelo.

Para obtener más información sobre la adición de un botón **View AI insights** a una vista en View Designer, consulte *Adición de un botón para ver insights* en el tema [Adición de elementos generales a una vista](3.2-guia-del-administrador.md#adición-de-elementos-generales-a-una-vista) de la *Guía del administrador de IBM OpenPages*.

### Exportación de datos

Puede exportar datos desde OpenPages. Los datos exportados pueden utilizarse en aplicaciones de cuadros de mando y elaboración de informes, para la Generación Mejorada por Recuperación (RAG) y para otros modelos basados en IA.

Debe tener el permiso de administrador ( `All Permissions/SOX/Administration/Data Export` ) para ejecutar exportaciones de datos.

Para obtener más información, consulte [el tema Exportación de datos de OpenPages para que los utilicen otras aplicaciones](3.5-guia-del-administrador.md#exportar-datos-de-openpages-s-para-que-los-utilicen-otras-aplicaciones) en *la Guía del administrador de IBM OpenPages*.

### Uso de @menciones en comentarios de objetos

En un comentario sobre un objeto, los usuarios ahora pueden usar @menciones para etiquetar a otros usuarios. Cuando escriben @ seguido de unos caracteres del nombre, apellido o nombre de usuario, se muestra una lista de usuarios. El usuario puede entonces elegir un nombre de la lista.

Para obtener más información, consulte el tema [Añadir comentarios a los objetos](4-guia-del-usuario.md#añadir-comentarios-a-los-objetos) en *la Guía del usuario de OpenPages ( IBM* ).

### Añadir un comentario Panel de actividad al panel de control

Los usuarios pueden añadir un panel en el panel de control para ver los comentarios que han hecho y los comentarios en los que se les menciona.

Para obtener más información, consulte el tema [Agregar un panel de actividad de comentario](4-guia-del-usuario.md#añadir-un-comentario-panel-de-actividad) en la *Guía del usuario IBM OpenPages*.

### Personalización de plantillas de correo electrónico para notificaciones de comentarios

Los administradores pueden personalizar la plantilla de los correos electrónicos que reciben los usuarios cuando se les menciona en un comentario.

Para obtener más información, consulte el tema [Configuración de comentarios de objetos](3.2-guia-del-administrador.md#configurar-el-comentario-de-objetos) en *la Guía del administrador de IBM OpenPages*.

### Reordenar las respuestas en las plantillas de los cuestionarios

Los autores de plantillas de cuestionarios ahora pueden reordenar las respuestas a una pregunta.

Para obtener más información, consulte el tema [Añadir preguntas a una plantilla de cuestionario](4-guia-del-usuario.md#añadido-de-preguntas-a-una-plantilla-de-cuestionario) en *la Guía del usuario de IBM OpenPages.*

### Cambiar la bandera de las preguntas en las evaluaciones del cuestionario

Cuando un revisor marca una pregunta en un cuestionario y la envía de vuelta al usuario para que realice cambios, aunque el revisor acepte la nueva respuesta, el revisor puede volver a marcar la misma pregunta más adelante.

Para obtener más información, consulte el tema [Revisar una evaluación del cuestionario](4-guia-del-usuario.md#revisión-de-una-evaluación-de-cuestionario) en *la Guía del usuario de IBM OpenPages.*

### Utilizar acciones de respuesta en plantillas de cuestionarios para establecer una respuesta a un campo enumerado

Un autor de cuestionarios ahora puede utilizar campos enumerados para establecer un campo en las acciones de respuesta de una plantilla de cuestionario.

Para obtener más información sobre la configuración de campos mediante acciones de respuesta, consulte el tema [Configuración de los valores de campo de un objeto en función de las respuestas de un encuestado](4-guia-del-usuario.md#establecer-los-valores-de-campo-de-un-objeto-basándose-en-las-respuestas-de-un-encuestado) en la *Guía del usuario de IBM OpenPages*.

### Soporte nativo para autenticación OAuth 2.0 para OpenPages API REST V1 y V2

Ahora puede configurar la autenticación nativa de OAuth2.0 para OpenPages IBM OpenPages REST API V1 y V2 en IBM OpenPages en las instalaciones o IBM OpenPages en la nube.

En esta configuración, OpenPages desempeña la función de servidor de autorización de OAuth 2.0. Puede utilizar un proveedor de OIDC ( OpenID Connect) como proveedor de identidad ( IdP ).

Para obtener más información sobre la configuración de la autenticación nativa OAuth 2.0, consulte el tema [Configuración de la autenticación nativa OAuth 2.0](3.1-guia-del-administrador.md#configuración-de-la-autenticación-nativa-oauth-20) en *la Guía del administrador de IBM OpenPages*.

### Cuadrículas anidadas

Un administrador puede configurar una cuadrícula anidada para una Vista de cuadrícula o como un campo de relación en una Vista de tareas o de administración. Una cuadrícula anidada muestra los hijos de un tipo de objeto específico y los descendientes de tipos de objetos específicos para cada hijo. Cada nivel de objetos está sangrado para proporcionar una representación visual de las relaciones entre los objetos.

La siguiente figura muestra una vista de cuadrícula anidada con la estructura de una entidad comercial, sus procesos secundarios y sus riesgos secundarios.

*Figura 1. Una vista de cuadrícula anidada*

![Una vista de cuadrícula anidada que muestra las entidades empresariales, sus procesos secundarios y sus descendientes.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nested_grid_view.png)

Para obtener más información sobre cómo configurar una vista de cuadrícula anidada, consulte el tema [Definir una vista de cuadrícula](3.6-guia-del-administrador.md#definición-de-una-vista-de-cuadrícula) en *la Guía del administrador de IBM OpenPages.*

Para obtener más información sobre el uso de una vista de cuadrícula anidada, consulte el tema [Uso de vistas de cuadrícula para buscar, abrir y trabajar con objetos](4-guia-del-usuario.md#utilización-de-las-vistas-de-cuadrícula-para-buscar-abrir-y-trabajar-con-objetos) en la *Guía del usuario de IBM OpenPages*.

La siguiente figura muestra una vista de tareas con una cuadrícula de relaciones. La cuadrícula anidada muestra la estructura de los Procesos, sus Riesgos secundarios y sus Controles terciarios.

*Figura 2. Una cuadrícula anidada*

![Una cuadrícula anidada en el campo de relación de una vista de tareas que muestra los procesos secundarios y sus descendientes.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nested_grid1.png)

Para obtener más información sobre cómo configurar una cuadrícula anidada para un campo de relación en una vista de tareas, consulte el tema [Añadir un diseño de cuadrícula](3.6-guia-del-administrador.md#adición-de-un-diseño-de-cuadrícula) en *la Guía del administrador de IBM OpenPages.*

Para obtener más información sobre el uso de una cuadrícula anidada para un campo de relación en una vista de tareas, consulte el tema [Asociaciones entre objetos](4-guia-del-usuario.md#asociaciones-entre-objetos) en *la Guía del usuario de OpenPages IBM.*

### Acciones del flujo de trabajo de pedidos

Los administradores ahora pueden establecer el orden de las acciones que un usuario ve cuando hace clic en **Acción** en una Vista de tareas. Por ejemplo, un administrador puede editar las propiedades de una etapa para mostrar las acciones en el orden de las más utilizadas a las menos utilizadas.

Para obtener más información sobre cómo cambiar el orden de las acciones, consulte el tema [Definir una etapa estándar](3.3-guia-del-administrador.md#definición-de-una-etapa-estándar) en *la Guía del administrador de IBM OpenPages.*

### Determinar dónde se hace referencia a los campos

Los administradores ahora pueden determinar si las referencias a un campo siguen siendo necesarias ejecutando un informe de análisis de referencia de campo. El informe comprueba si hay referencias al campo en vistas, flujos de trabajo, perfiles, cálculos, reglas de seguridad, filtros, vistas de panel, dependencias de campo y reglas de eventos normativos.

Para obtener más información, consulte el tema [Determinar dónde se hace referencia a los campos](3.1-guia-del-administrador.md#determinar-dónde-se-hace-referencia-a-los-campos) en *la Guía del administrador de IBM OpenPages*.

### Migración del sistema: exportación de dependencias

Puede exportar un artículo sin exportar otros artículos de los que depende. Por ejemplo, puede exportar una vista sin sus definiciones de campo y objeto dependientes.

Para obtener más información, consulte [el tema Exportar elementos de configuración desde el entorno de origen](3.4-guia-del-administrador.md#exportación-de-elementos-de-configuración-desde-el-entorno-de-origen) en *la Guía del administrador de IBM OpenPages*.

Además, el contenido no relacionado ya no se incluye en la exportación. Por ejemplo, cuando exportaba un perfil en versiones anteriores, se exportaban todos los tipos de objeto incluidos en el perfil, incluyendo todos los campos de esos tipos de objeto. En la versión 9.1.0 de OpenPages, solo se incluyen en la exportación los artículos a los que hace referencia el artículo exportado.

### Flujos de trabajo del sistema

Solo un trabajo de programador u otro flujo de trabajo puede iniciar un flujo de trabajo del sistema. Cuando utiliza un flujo de trabajo del sistema, se asegura de que el flujo de trabajo se ejecute de forma coherente y en el momento adecuado, minimizando el riesgo de variaciones o errores.

### Nuevos puntos finales disponibles en la API REST de GRC V2

Ahora puede recuperar plantillas de cuestionarios y evaluaciones por ID utilizando los nuevos puntos finales `GET /questionnaire/{id}` y `GET /assessment/{id}`.

También puede crear o actualizar una lista de objetos utilizando el nuevo punto final `POST /contents/bulk`.

Para obtener más información sobre las actualizaciones de la API V2, consulte [Novedades de la versión 9.1.0](9-guia-del-desarrollador.md#novedades-de-la-versión-910) en la *Guía del desarrollador IBM OpenPages*.

### Están disponibles las configuraciones regionales árabe (Arabia Saudí) y árabe (Emiratos Árabes Unidos)

Los administradores ahora pueden agregar árabe (Arabia Saudí) y árabe (Emiratos Árabes Unidos) como nuevos idiomas. Sin embargo, todos los datos numéricos, como la moneda, los decimales y la hora, utilizan números arábigos occidentales, independientemente de la preferencia regional.

Para obtener más información sobre cómo agregar configuraciones regionales, consulte el tema [Agregar configuraciones regionales](3.3-guia-del-administrador.md#adición-de-entornos-locales) en *la Guía del administrador de IBM OpenPages*.

### Cambios en los formatos de moneda y fecha

Los formatos de visualización de monedas y fechas han cambiado para las siguientes configuraciones regionales:

**Tabla 1. Cambios en el formato de las divisas**

| Idioma o localidad | Nuevo formato | Formato anterior |
| --- | --- | --- |
| Griego | • Separador decimal: `,`<br>• Grupo (miles) separador: `.`<br>Por ejemplo: `12.345,00` | `12,345.00`. |
| Rumano | • Separador decimal: `,`<br>• Grupo (miles) separador: `.`<br>Por ejemplo: `12.345,00` | `12 345.00` |
| Serbio Latino | • Separador decimal: `,`<br>• Grupo (miles) separador: `.`<br>Por ejemplo: `12.345,00` | `12,345.00` |
| Sueco | • Separador decimal: `,`<br>• Grupo (miles) separador:  (espacio)<br>Por ejemplo: `123 456,00` | `1 234,56` |

**Tabla 2. Cambios en el formato de las fechas**

| Idioma o localidad | Nuevo formato | Formato anterior |
| --- | --- | --- |
| Danés | `tt-mm-jjjj` | `tt.mm.jjjj`. |
| Coreano | `yyyy. mm. dd` | `yyyy. mm. dd.` |
| Letón | `yyyy.dd.mm` | `dd.mm.yyyy` |

Los cambios se deben a la actualización de IBM® Semeru Runtimes.

### Otros cambios

- Ahora puede controlar cómo se muestra `displayname` aplicando la configuración **Aplicaciones** > **GRCM** > **Anexar nombre de usuario con nombre para mostrar**.

  Para obtener más información, consulte el tema [Añadir nombre de usuario con `displayname`](3.3-guia-del-administrador.md#añadir-nombre-de-usuario-con-nombre-de-visualización) en la *Guía del administrador de IBM OpenPages*.
- Ahora puede mantener valores de API válidos para que el usuario los añada al campo **Contenido referenciado** de una vista de tarea aplicando la configuración **Aplicaciones** > **Común** > **Contenido referenciado** > **Lista de API permitidas**.

  Para obtener más información, consulte el tema de [configuración API allowlist](3.3-guia-del-administrador.md#configuración-de-la-lista-de-permisos-de-la-api) en la *Guía del administrador de IBM OpenPages*.
- El botón **Abrir vista rápida** ![Abrir el botón de vista rápida](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/tfui_quick_view_icon.jpg) que solía aparecer en la columna situada más a la derecha en una vista de cuadrícula se muestra ahora en la segunda columna desde la izquierda cuando se pasa el puntero del ratón sobre una fila.
- Cuando utilice la barra de desplazamiento situada en la parte inferior de la página para ver todas las columnas de una vista de cuadrícula, la columna situada más a la izquierda permanecerá en su sitio para que siempre esté visible.
- El algoritmo de cifrado 3DES no es compatible con IBM Semeru Runtimes. Si utiliza un almacén de claves personalizado, utilice AES.

  Antes de actualizar o migrar, consulte el tema [Prepare el almacén de claves personalizado para la actualización o migración](5.1-guia-de-instalacion-y-despliegue-solo-local.md#preparar-el-almacén-de-claves-personalizado-para-la-actualización-o-migración) en la *Guía de instalación y despliegue de IBM OpenPages*.
- Los algoritmos de encriptación OP-CUSTOM y 3DES ya no son compatibles con la encriptación de contraseñas. Cambia el algoritmo a AES.

  Para obtener más información, consulte el tema [Actualización del algoritmo de cifrado de contraseñas de OpenPages](5.1-guia-de-instalacion-y-despliegue-solo-local.md#actualización-del-algoritmo-de-cifrado-de-contraseñas-de-openpages) en la *Guía de instalación e implantación de IBM OpenPages*.
- Ahora se admiten los nuevos códigos de moneda XCG y ZWG. Para obtener información sobre cómo activar una divisa y cargar los tipos de cambio, consulte [Modificación de los tipos de cambio de divisas](3.1-guia-del-administrador.md#modificación-de-los-tipos-de-cambio-de-moneda).
- Las siguientes integraciones ya no están disponibles:

  - RiskLens
  - Supply Wisdom

## Novedades de la versión 9.0.0.5

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-9005)

La versión 9.0.0.5 de OpenPages® incluye mejoras en las vistas de tareas, cuestionarios y mucho más.

### Comentario de objetos

Los usuarios pueden añadir sus comentarios a los objetos si el administrador les da permiso. Por ejemplo, un usuario puede añadir un comentario a un asunto para hacer una pregunta, una observación o dejar constancia de sus pensamientos sobre el asunto.

Para obtener más información, consulte el tema [Comentario de objetos](4-guia-del-usuario.md#añadir-comentarios-a-los-objetos) en la *Guía del usuario de IBM OpenPages*.

Los administradores pueden eliminar todos los comentarios de un objeto con una operación en una acción de flujo de trabajo.

Para obtener más información, consulte el tema [Definición de una acción de flujo de trabajo que elimina todos los comentarios de objetos](3.3-guia-del-administrador.md#definir-una-acción-de-flujo-de-trabajo-que-elimine-todos-los-comentarios-de-objetos) en la *Guía del administrador deIBM OpenPages*.

### Respuestas pobladas para las evaluaciones del cuestionario

Para rellenar las respuestas a una pregunta con los valores de un campo, los autores de la plantilla del cuestionario asocian la pregunta a ese campo.

Para obtener más información, consulte el tema [Asociar respuestas a un campo](4-guia-del-usuario.md#asociar-respuestas-a-un-campo) en la *Guía del usuario de IBM OpenPages*.

Para rellenar las respuestas de la evaluación del cuestionario, los administradores añaden la operación **Establecer respuestas del cuestionario con valor de campo relacionado** a una acción del Flujo de trabajo de evaluación del cuestionario.

Para obtener más información, consulte el tema [Definición de una acción de flujo de trabajo que rellena respuestas en una evaluación de cuestionario](3.3-guia-del-administrador.md#definición-de-una-acción-de-flujo-de-trabajo-que-rellena-las-respuestas-en-una-evaluación-de-cuestionario) en la *Guía del administrador deIBM OpenPages*.

### Autenticación OAuth 2.0 0 compatible con la API REST ' OpenPages V1 y V2

Ahora puede configurar la autenticación OAuth2.0 para ' OpenPages ' IBM OpenPages REST API V1 y V2 en ' IBM OpenPages on premises o ' IBM OpenPages ' on Cloud.

Para obtener más información sobre la configuración de OAuth 2.00, consulte la sección *Seguridad y autenticación* del tema [IBM OpenPages GRC REST API V2](9-guia-del-desarrollador.md#ibm-openpages-api-rest-grc-v2) en *IBM OpenPages Developer Guide*.

### Eliminar objetos mediante un flujo de trabajo

Los administradores pueden definir flujos de trabajo para eliminar objetos de las siguientes maneras:

- En una etapa final, especifique una operación para eliminar el objeto que el flujo de trabajo está procesando.

  Para obtener más información, consulte el tema [Eliminación de objetos en una etapa final](3.3-guia-del-administrador.md#eliminación-de-objetos-en-una-etapa-final) en la *Guía del administrador deIBM OpenPages*.
- En una acción, especifique una operación para eliminar los hijos o descendientes del objeto que el flujo de trabajo está procesando.

  Para obtener más información, consulte el tema [Definición de una acción de flujo de trabajo que elimina objetos](3.3-guia-del-administrador.md#definición-de-una-acción-de-flujo-de-trabajo-que-elimina-objetos) en la *Guía del administrador deIBM OpenPages*.

### Integración de la traducción con watsonx.ai

Cuando los administradores utilizan el servicio de traducción de idiomas watsonx.ai, pueden definir el mensaje y el contexto de la traducción. Con esta función, el gran modelo lingüístico (LLM) puede proporcionar una traducción que utilice el lenguaje específico del sector del dominio de Gobernanza, Riesgo y Cumplimiento para ofrecer traducciones más adecuadas al contexto.

Para configurar el servicio de traducción de idiomas de watsonx.ai™, haga clic en **Abrir menú de administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/settings_menu_icon_task_focused_ui.jpg)** > **Integraciones** > **Servicios de traducción de OpenPages** y seleccione **watsonx.ai** como **Tipo de traductor**.

### La información contextual puede compartirse con IBM watsonx Assistant

A través de la integración con IBM watsonx Assistant, OpenPages puede compartir información contextual sobre la sesión de usuario de OpenPages . Con esta información, IBM watsonx Assistant conoce el tipo de usuario que ha iniciado sesión y en qué parte de la interfaz de usuario ' OpenPages ' se encuentra. IBM watsonx Assistant puede entonces utilizar la API ' OpenPages ' para obtener más información o realizar acciones en nombre del usuario. Por ejemplo, IBM watsonx Assistant puede utilizar IA generativa para crear un elemento de acción para un problema en " OpenPages.

La siguiente información contextual se envía al inicio de una nueva sesión de usuario:

- Nombre e ID del perfil de usuario
- entorno local del usuario
- URL de la instancia OpenPages

La siguiente información contextual se envía durante la sesión del usuario:

- Tipo de vista, como cuadrícula, creación, tarea o vista de administrador
- Tipo de objeto
- ID del objeto, que permite a la API recuperar información relacionada con el objeto
- Acciones de flujo de trabajo disponibles si el objeto está en un flujo de trabajo

### Seguimiento de la actividad del correo electrónico

Los administradores pueden utilizar una nueva opción de rastreo del sistema, **Notificación de correo electrónico**, para capturar información sobre la actividad del correo electrónico que incluye si los mensajes de correo electrónico se envían correctamente.

Para obtener más información, consulte el tema [Recopilación de registros con la interfaz de usuario LogCollector](3.4-guia-del-administrador.md#recopilación-de-registros-con-la-interfaz-de-usuario-de-logcollector) en la *Guía del administrador deIBM OpenPages*.

### Buscar tipos de objetos en el menú principal

Ahora puede hacer clic en **el menú Principal** ![Icono de menú principal](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/primary_menu_icon_task_focused_ui.png) e e introducir un tipo de objeto en el cuadro Buscar tipo de objeto para encontrar un tipo de objeto.

Para obtener más información sobre el menú Principal, consulte el tema [Uso del menú Principal](4-guia-del-usuario.md#uso-del-menú-principal) en la *Guía del usuario de IBM OpenPages*.

### Disponible en español mexicano

Ahora los administradores pueden añadir el español de México como nueva configuración regional.

Para obtener más información sobre la adición de configuraciones regionales, consulte el tema [Adición de configuraciones regionales](3.3-guia-del-administrador.md#adición-de-entornos-locales) en la *Guía del administrador deIBM OpenPages*.

## Novedades de la versión 9.0.0.4

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-9004)

La versión 9.0.0.4 de OpenPages® incluye mejoras en el panel de control, los gráficos, el registro, los cuestionarios y mucho más.

### Si olvida su contraseña, puede restablecerla

**Se aplica a:** [En cloud](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue) [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Los usuarios pueden hacer clic en **¿Ha olvidado la contraseña?** en la pantalla de acceso si olvidan su contraseña. En la página **Olvidaste la contraseña**, pueden introducir su nombre de usuario para recibir un mensaje de correo electrónico en el que se les explica cómo restablecer su contraseña.

Si el acceso de un usuario a OpenPages se controla utilizando el inicio de sesión único (SSO) como método de autenticación, o si el acceso del usuario está controlado por un servidor de autenticación LDAP (Lightweight Directory Access Protocol), el usuario recibe un mensaje de correo electrónico en el que se le explica que no puede restablecer su contraseña.

Si un administrador desactiva esta función estableciendo `/Platform/Security/Password/Reset/Enabled` en **false**, aparecerá el mensaje **¿Ha olvidado la contraseña?** no aparece en la pantalla de inicio de sesión.

### Gráficos de barras apiladas

Ahora puede configurar un gráfico de barras apiladas en el cuadro de mandos y en el Diseñador de vistas de tareas.

Para obtener más información, consulte el tema [Ejemplos de diagramas](3.6-guia-del-administrador.md#ejemplos-de-diagrama-de-gráfico) en la *IBM OpenPages*.

### Múltiples pestañas en el salpicadero

Puedes añadir informes y pestañas personalizadas a tu panel de control. El cuadro de mandos puede contener hasta tres pestañas para informes Cognos® y OpenPages y hasta tres pestañas personalizadas.

> **Importante:** Las fichas de informe no son compatibles con OpenPages as a Service.

Es posible que desee crear pestañas personalizadas en lugar de añadir a la ficha Inicio para mantenerlo ordenado y mantener el rendimiento. Además, es posible que desee utilizar pestañas personalizadas para agrupar paneles y widgets relacionados en lugares separados.

Es posible que tu administrador haya creado informes y fichas personalizadas para el perfil al que perteneces. Si este es el caso, puedes conservar las pestañas o eliminarlas y añadir las tuyas propias, como pestañas para los informes a los que accedes con más frecuencia.

Para obtener más información, consulte el tema [Añadir un informe o una ficha personalizada](4-guia-del-usuario.md#añadir-un-informe-o-una-ficha-personalizada) de la *IBM OpenPages*.

### Eliminar una configuración regional añadida

Ahora puede eliminar una configuración regional añadida anteriormente si ya no la necesita.

Para obtener más información, consulte el tema [Eliminación de locales](3.3-guia-del-administrador.md#eliminar-locales) en la *IBM OpenPages*.

### **Omitir si existe** opción en las acciones de respuesta al cuestionario

Si no desea que una acción de respuesta intente volver a crear un nuevo objeto si ya existe un objeto con el mismo nombre, seleccione **Omitir si existe**.

Para obtener más información, consulte el tema [Creación de un objeto basado en las respuestas de un encuestado](4-guia-del-usuario.md#creación-de-un-objeto-basado-en-las-respuestas-de-un-encuestado) en la *IBM OpenPages*.

### Expresiones en operaciones de campo fijo en cuestionarios

Ahora puede introducir una expresión para el valor de un campo. Por ejemplo, puede introducir `[$TODAY$]` para la fecha actual, `[$END_USER$]` ` para el nombre del usuario registrado, o `[$System Fields:Description$]` para establecer el campo en el valor del campo Descripción del objeto.

Para obtener más información, consulte el tema [Establecimiento de los valores de campo de un objeto en función de las respuestas de un encuestado](4-guia-del-usuario.md#establecer-los-valores-de-campo-de-un-objeto-basándose-en-las-respuestas-de-un-encuestado) en la *IBM OpenPages*.

### Seguimiento de la sesión

Un administrador puede configurar **/Applications/Common/Administration/Session Tracing** para habilitar el seguimiento de las acciones de un usuario.

### datos de diagnóstico

Puede utilizar una nueva opción de rastreo del sistema para capturar datos de diagnóstico relacionados con el rendimiento de la base de datos.

Para obtener más información, consulte el tema [Recopilación de registros con la interfaz de usuario de LogCollector](3.4-guia-del-administrador.md#recopilación-de-registros-con-la-interfaz-de-usuario-de-logcollector) en la *IBM OpenPages*.

## Características nuevas de la versión 9.0.0.3

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-9003)

La versión 9.0.0.3 de OpenPages® incluye mejoras en entornos locales, seguridad, edición de campos de texto, cuestionarios, etc.

### Añadir nuevos entornos locales

Ahora los administradores pueden añadir nuevos entornos locales para proporcionar soporte de traducción para idiomas distintos de los que OpenPages soporta de forma predeterminada.

*Figura 1. Adición de un nuevo entorno local*

![La pestaña Entornos locales se muestra con una lista de entornos locales nuevos que se pueden seleccionar.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/9003_nf_locales.png)

Puede seleccionar nuevos entornos locales para añadirlos en la lista siguiente:

- Croata
- Checo
- Danés
- Holandés
- Estonio
- Finés
- Griego
- Indonesio
- Coreano
- Letón
- Malayo latino
- Nuevo Noruego
- Polaco
- Rumano
- Serbio latino
- Sueco
- Tailandés
- Turco

También puede habilitar e inhabilitar entornos locales. Cuando inhabilita un entorno local, los usuarios con ese entorno local ven el entorno local predeterminado después de renovar su navegador o después de cerrar la sesión y volver a iniciarla.

Para obtener más información sobre cómo añadir entornos locales, consulte el tema [Añadir entornos locales](3.3-guia-del-administrador.md#adición-de-entornos-locales) en la publicación *IBM OpenPages Guía del administrador*.

### Nuevas herramientas para campos de texto enriquecido

Para los campos de serie que tienen un tipo de visualización de texto enriquecido, los usuarios tienen una barra de herramientas y mandatos para el formato de texto y el procesamiento de texto. Esta barra de herramientas ahora contiene las siguientes herramientas:

- Utilizar el**Subir imagen desde la computadora**![Cargar imagen desde el ícono de la computadora](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ckeditor_image_icon.png) herramienta para agregar una imagen. En el cuadro de diálogo, seleccione la imagen que desee.

  La imagen se almacena en la aplicación cuando guarda el objeto.
- Utilizar el**Pantalla completa**![Icono de pantalla completa](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ckeditor_full_screen_icon.png) herramienta para maximizar el campo a pantalla completa.
- Utilizar el**Fuente**![Icono de fuente](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ckeditor_source_icon.png) herramienta para editar el código HTML directamente.

Por ejemplo, la figura siguiente muestra el campo Propósito de una nueva política. El campo contiene una imagen. Las nuevas herramientas de la barra de herramientas aparecen en un círculo.

*Figura 2. Una imagen utilizada en el propósito de una política*

![Se muestra un objeto de política. El campo de propósito de la política contiene una imagen.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/9003_nf_rich_txt_image.png)

> **Importante:** FastMap no exporta ni importa imágenes. Cuando un objeto se exporta utilizandoFastMap, cualquier imagen agregada a campos de texto enriquecido no se exporta con ese objeto.

### Exportar e importar paneles de instrumentos utilizando la interfaz de usuario de migración de entorno

Antes de 9.0.0.3, los paneles de instrumentos solo se podían exportar como parte de un perfil. Ahora puede exportar paneles de control directamente utilizando la interfaz de usuario de migración de entorno.

Para obtener más información sobre la exportación e importación de paneles de instrumentos, consulte los temas [Exportación de elementos de configuración desde el entorno de origen](3.4-guia-del-administrador.md#exportación-de-elementos-de-configuración-desde-el-entorno-de-origen) y [Importación de elementos de configuración al entorno de destino](3.4-guia-del-administrador.md#importación-de-un-archivo-de-migración) en la publicación *IBM OpenPages Guía del administrador*.

### Editar y suprimir comentarios en cuestionarios

Tanto los encuestados como los revisores ahora pueden editar o suprimir comentarios en un cuestionario.

Puede editar o suprimir un comentario que ha creado. Hay algunas restricciones en los comentarios que puede suprimir.

*Figura 3. Una evaluación de cuestionario que muestra un comentario con los botones Editar y Suprimir en círculo*

![La ficha Cuestionario de una evaluación de cuestionario se muestra junto con una pregunta. Los botones Editar y Suprimir del comentario aparecen en un círculo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/9003_nf_edit_delete_comment.png)

Para obtener más información sobre cómo editar o suprimir comentarios mientras responde a un cuestionario, consulte el tema [Completar una evaluación de cuestionario](4-guia-del-usuario.md#completar-una-evaluación-de-cuestionario) en la publicación *IBM OpenPages Guía del usuario*.

Para obtener más información sobre cómo editar o suprimir comentarios mientras está revisando un cuestionario, consulte el tema [Revisión de una evaluación de cuestionario](4-guia-del-usuario.md#revisión-de-una-evaluación-de-cuestionario) en la publicación *IBM OpenPages Guía del usuario*.

### Hacer que una respuesta sea exclusiva para una pregunta de opción múltiple

Al editar una plantilla de cuestionario, un usuario puede hacer que una respuesta sea exclusiva para una pregunta de varias opciones. Cuando un encuestado elige una respuesta exclusiva, no puede seleccionar otra respuesta para la pregunta. Un ejemplo de una respuesta exclusiva es "Ninguno de los anteriores".

*Figura 4. Una plantilla de cuestionario con el recuadro de selección de respuesta exclusivo en círculo*

![La pestaña Editor de una plantilla de cuestionario se muestra con una respuesta seleccionada como respuesta exclusiva. El recuadro de selección seleccionado aparece en un círculo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/9003_nf_exclusive_question.png)

Para obtener más información sobre cómo hacer que una respuesta sea exclusiva en un cuestionario, consulte el tema [Adición de preguntas a una plantilla de cuestionario](4-guia-del-usuario.md#añadido-de-preguntas-a-una-plantilla-de-cuestionario) en la publicación *IBM OpenPages Guía del usuario*.

### Soporte para mensajes implementados con variables dewatsonx.ai

La costumbreMachine Learning La función de integración de modelos ahora admite mensajes implementados con variables dewatsonx.ai .

Cuando esté configurando su modelo, configure las entradas para las variables de solicitud y la salida para analizar el JSON producido a partir del modelo. Cuando esté configurando JSONata para la salida, comience la ruta de ubicación de JSONata con el objeto`results` .

Por ejemplo, si espera el siguiente resultado:

```json
{
	"generated_text": " \"person\": \"Fred\", \"organization\": \"IBM\", \"location\": \"USA\" ",
	"generated_token_count": 30,
	"input_token_count": 85,
	"stop_reason": "eos_token"
}
```

La salida devuelta está contenida dentro de un objeto JSON llamado`results` , como se muestra en el siguiente ejemplo:

```json
{
    "created_at": "2023-06-21T17:44:50.554Z",
    "model_id": "google/flan-ul2",
    "results": [
	"generated_text": " \"person\": \"Ghada\", \"organization\": \"IBM\", \"location\": \"USA\" ",
	"generated_token_count": 30,
	"input_token_count": 85,
	"stop_reason": "eos_token"
      }
    ]
}
```

La ruta de ubicación de JSONata para el resultado del ejemplo anterior comienza con`results.generated_text` .

Para más información sobre la AduanaMachine Learning Función de integración de modelos, consulte la[CostumbreMachine Learning Modelos](3.5-guia-del-administrador.md#modelos-de-aprendizaje-automático-personalizados) tema en el*IBMOpenPages Guía del administrador* .

### Nuevos puntos finales disponibles en la API REST de GRC V2

Hay nuevos puntos finales para automatizar la importación y validación de FastMap , los procesos de LogCollector , la recuperación de entornos locales soportados y la actualización de los valores de configuración.

Para obtener más información sobre las actualizaciones de la API V2 , consulte [Novedades de la versión 9.0.0.3](9-guia-del-desarrollador.md#novedades-de-la-versión-9003) en la publicación *IBM OpenPages Developer Guide*.

### Seguridad adicional para la aplicación

Se ha mejorado la política de seguridad de contenido (CSP) de OpenPages predeterminada para proporcionar seguridad adicional para la aplicación. CSP es una cabecera de respuesta HTTP que los navegadores utilizan para mejorar la seguridad del documento o página web. El encabezado CSP permite restringir qué recursos, como JavaScript, CSS e imágenes, pueden cargarse, y las URL desde las que pueden cargarse.

Las mejoras en la seguridad cambian la forma en que funciona OpenPages :

- No tiene determinadas características en el editor de texto enriquecido que utilizan estilos en línea, como el color y la familia de fuentes, y el redimensionamiento y la alineación de imágenes y tablas.
- La pestaña JSON no se muestra en el Diseñador de vistas.
- Es posible que los asistentes personalizados y los informes JSP no funcionen correctamente. Para obtener más información, consulte la nota técnica.[Muchos asistentes personalizados dejan de funcionar correctamente después de actualizar a9.0.0.3](https://www.ibm.com/support/pages/node/7158837) .
- Es posible que el informe de importación de FastMap y el informe de estado de importación de FastMap tengan problemas de representación y no funcionen correctamente.
- Los ayudantes e informes heredados, como los programas de utilidad KRI y Creación de valores KPI, pueden tener problemas de representación y puede que no funcionen correctamente.

Para obtener más información sobre CSP y sobre cómo restaurar o sustituir la funcionalidad de estas características, consulte el tema [Valores de registro CSP (Content-Security-Policy)](3.3-guia-del-administrador.md#valores-de-registro-csp-content-security-policy) en la publicación *IBM OpenPages Guía del administrador*.

## Características nuevas de la versión 9.0.0.2

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-9002)

La versión 9.0.0.2 de OpenPages® incluye mejoras en flujos de trabajo, informes, cuestionarios, etc.

### Varios informes en una única vista de informe

Ahora los administradores pueden definir varias vistas de informe para tipos de objeto, lo que proporciona a los usuarios más opciones para ver y compartir información.

Una *vista de informe* es una vista de sólo lectura de información clave. Las vistas de informes están diseñadas para ser fáciles de imprimir y compartir. Anteriormente, se daba soporte a una única vista de informe por tipo de objeto.

Ahora, los administradores pueden crear varias vistas de informe y especificar la prioridad de estas vistas. Las vistas de informe están disponibles para los usuarios desde un menú desplegable en la pestaña **Informe** . La prioridad de vista determina el orden de las vistas de informe en el menú.

*Figura 1. Selección de una vista de informe*

![Se muestra un objeto de plan de continuidad de negocio. La pestaña de informe muestra tres informes. Se selecciona el informe Resumen ejecutivo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9002_report-view.png)

Para obtener más información, consulte [Definición de una vista de informe](3.6-guia-del-administrador.md#definición-de-una-vista-de-informe).

### Nueva operación para asociar objetos en una acción de flujo de trabajo

En un flujo de trabajo, ahora puede añadir una nueva operación **Asociar objetos** en una acción. Esta operación crea una relación entre el objeto actual y otros objetos basándose en las condiciones que especifique. Por ejemplo, en el Flujo de trabajo de evaluación de cuestionario, puede asociar automáticamente una plantilla de cuestionario con el objeto de evaluación de cuestionario actual.

*Figura 2. Adición de una operación para asociar objetos*

![Se muestra la página Operaciones. El tipo de operación se establece en Asociar objetos. La opción Objetos a asociar se ha establecido en Plantilla de cuestionario hijo directo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9002_wf-op-assoc.png)

Además, si está asociando un objeto como hijo del objeto actual, puede hacer que el objeto actual sea el padre principal del objeto hijo. Por ejemplo, si está asociando automáticamente una plantilla de cuestionario con una evaluación de cuestionario, puede hacer que la evaluación de cuestionario sea el padre principal de la plantilla de cuestionario.

Para obtener más información, consulte [Definición de una acción de flujo de trabajo que asocia objetos con el objeto actual](3.3-guia-del-administrador.md#definición-de-una-acción-de-flujo-de-trabajo-que-asocia-objetos-con-el-objeto-actual).

### Creación de objetos basada en respuestas de cuestionario

En una plantilla de cuestionario, ahora un autor de cuestionario puede crear acciones de respuesta para crear o copiar automáticamente un objeto y establecer valores de campo en el objeto.

- Crear automáticamente un objeto basado en la respuesta a una pregunta. Por ejemplo, en un cuestionario de evaluación de riesgos, es posible que desee crear problemas basándose en las respuestas a las preguntas.
- Copiar automáticamente un objeto de la biblioteca basándose en la respuesta a una pregunta. Por ejemplo, en un cuestionario de identificación de riesgos, es posible que desee identificar los riesgos relacionados de la biblioteca de riesgos global basándose en una respuesta a la pregunta.

En la pestaña **Editor** de una plantilla de cuestionario, seleccione **Acciones de respuesta**.

*Figura 3. Adición de una acción de respuesta*

![La página Acciones de respuesta se muestra con el botón Nueva acción de respuesta. Hay dos acciones de respuesta listadas.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_response_actions1.png)

Al configurar la acción de respuesta, puede elegir crear un objeto basándose en la respuesta.

*Figura 4. Creación de un objeto basado en una respuesta*

![Se muestra el cuadro de diálogo Acción de respuesta. La operación Crear objeto está seleccionada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_response_actions2.png)

De forma alternativa, puede elegir copiar un objeto basándose en la respuesta.

*Figura 5. Copia de un objeto basándose en una respuesta*

![Se muestra el cuadro de diálogo Acción de respuesta. La operación Copiar objeto está seleccionada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_response_actions3.png)

Cree una operación de acción de respuesta de cuestionario en una acción del flujo de trabajo de evaluación de cuestionario para aplicar la acción de respuesta.

*Figura 6. Configuración de una acción de respuesta de cuestionario en un flujo de trabajo*

![Se muestra el flujo de trabajo de evaluación de cuestionario. El panel Operaciones está abierto con una operación de acción de respuesta de cuestionario especificada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_response_actions4.png)

Para obtener más información sobre la creación de objetos, consulte  [Creación de un objeto basándose en las respuestas de un encuestado](4-guia-del-usuario.md#creación-de-un-objeto-basado-en-las-respuestas-de-un-encuestado).

Para obtener más información sobre la copia de objetos, consulte  [Copia de un objeto basándose en las respuestas de un encuestado](4-guia-del-usuario.md#copia-de-un-objeto-basado-en-las-respuestas-de-un-encuestado).

### Configurar un modelo para sugerir relaciones para crear o copiar

Ahora los administradores pueden configurar un modelo para sugerir relaciones entre objetos para el usuario. Una relación puede ser nueva o copiarse de una relación existente.

*Figura 7. Elección del tipo de conocimiento Establecer relación*

![La página Editar el modelo se muestra con el paso de acceso Modelo seleccionado. El tipo de Insight es Establecer relación.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ai_set_relationship.png)

Por ejemplo, puede configurar el modelo para realizar las sugerencias siguientes:

- Cuando un usuario está creando un riesgo, el modelo puede sugerir un conjunto de controles que se copiarán de la biblioteca.
- Cuando un usuario está creando un problema, el modelo puede sugerir un conjunto de elementos de acciones predefinidos de la biblioteca y un conjunto de controles en el entorno.

*Figura 8. Selección de controles para copiar desde la biblioteca*

![Se muestra la vista Copiar de cuadrícula. Las sugerencias de IA sólo están habilitadas. La cuadrícula lista los controles sugeridos.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/ai_set_relationship-copy.png)

### Exportar plantillas de cuestionarios mediante el proceso de migración de entornos

Utilice el proceso de migración de entornos para exportar plantillas de cuestionarios. Cuando se exporta una plantilla de cuestionario utilizando la migración de entorno, todos los componentes y datos de la plantilla de cuestionario se exportan con ella. Por ejemplo, se exporta una plantilla de cuestionario con dependencias de preguntas y acciones de respuesta.

> **Advertencia:** Si utiliza FastMap para exportar una plantilla de cuestionario, no obtendrá todos los componentes y datos asociados a la plantilla.

En versiones de OpenPages anteriores a 9.0.0.2, se utilizaba FastMap para exportar plantillas de cuestionarios a un libro de Microsoft Excel. Sin embargo, en la versión 9.0.0.2, los datos asociados a las plantillas de cuestionarios pasaron a ser demasiado grandes para exportarlos a un libro de trabajo. En lugar de crear un libro de trabajo, la exportación de migración de entorno crea un archivo JAR.

> **Nota:** Puede seguir utilizando FastMap para importar plantillas de cuestionarios que haya exportado desde una versión de OpenPages anterior a 9.0.0.2.

Para obtener más información sobre el uso de la migración de entorno, consulte el tema *Migración de OpenPages entornos* en la sección [Migración de OpenPages entornos](3.4-guia-del-administrador.md#migración-de-entornos-de-openpages).

### Ver cuestionarios de puntuación baja en Evaluaciones de cuestionario

Ahora un revisor de cuestionario puede ver las preguntas con puntuaciones bajas utilizando el nuevo filtro **Ver preguntas con puntuaciones bajas** .

*Figura 9. Selección del filtro **Ver preguntas con puntuaciones bajas** en una evaluación de cuestionario*

![Se muestra una evaluación de cuestionario con el filtro Ver preguntas con puntuación baja aplicado.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/low_score_questions.png)

### Servicios de traducción

OpenPages ahora da soporte a NeuralSeek. Los administradores pueden aprovisionar rápida y fácilmente un servicio NeuralSeek en [IBM Cloud®](https://cloud.ibm.com/docs/language-translator?topic=language-translator-about) e integrarlo después con OpenPages.

*Figura 10. Configuración de un servicio de traducción*

![En OpenPages, se muestra la página de configuración de los servicios de traducción.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9002_tr_serv.png)

Para obtener más información, consulte [Servicios de traducción](3.5-guia-del-administrador.md#servicios-de-traducción).

### Software soportado en 9.0.0.2

OpenPages ahora da soporte a las siguientes versiones de software:

**Tabla 1. Cambios en las versiones de software soportadas**

| Software | Cambios de conformidad |
| --- | --- |
| Servidor Red Hat Enterprise Linux® (RHEL) | Ahora se da soporte a 9.x . |
| IBM® Db2® | Ahora se da soporte a 11.5.9 . |

Para más información, consulte la página web [Entornos compatibles](https://www.ibm.com/support/pages/node/713069).

## Características nuevas de la versión 9.0.0.1

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-9001)

Las nuevas características de OpenPages® 9.0.0.1 dan soporte al objetivo continuado de IBM®de implicar a los usuarios, desplegar casos de uso a través de herramientas y ayudar a los equipos a aprender con el uso compartido de información simplificado.

Este release introduce la creación de informes en aplicación que utiliza un nuevo tipo de vista denominado *Vista de informe*. Las vistas de informe se crean utilizando el Diseñador de vistas y se visualizan como una pestaña en el objeto. Las últimas mejoras también permiten a los usuarios imprimir fácilmente en PDF o exportar a Excel, agilizando el proceso de creación de informes y mejorando los esfuerzos de colaboración.

Las mejoras del cuestionario incluyen la capacidad de enriquecer o modificar campos en el activo relacionados con el cuestionario, basándose en las respuestas a las preguntas del cuestionario.

Además, seguimos mejorando la página de inicio del usuario, los flujos de trabajo, el diseñador de vistas, el filtrado y las visualizaciones de gráficos.

### Personalizar el mensaje de bienvenida de la página de inicio

Ahora los administradores pueden personalizar el mensaje de bienvenida en la página **Inicio** editando el texto de la aplicación `app.dashboard.home.title.greet` . Para obtener más información, consulte [Modificación del mensaje de bienvenida de la página de inicio](3.3-guia-del-administrador.md#modificar-el-mensaje-de-bienvenida-en-el-salpicadero).

*Figura 1. Personalizar el mensaje de bienvenida de la página de inicio*

![penPages Configuración de solución > Pantalla Tipos de objeto que muestra app.dashboard.home.title.greet. ¡panel con Bienvenido a OpenPages, %NM;! tecleado en U.S. Inglés, seguido de una imagen de la página de inicio de OpenPages mostrando un nuevo mensaje de bienvenida que dice: ¡Bienvenido a OpenPages, Jane!](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_welcome_message.png)

### Filtrar por etiquetas

Los usuarios y administradores ahora pueden crear y guardar filtros públicos y personalizados basados en etiquetas. Para obtener más información, consulte [Adición de filtros a tipos de objeto](3.2-guia-del-administrador.md#adición-de-filtros-a-tipos-de-objeto).

*Figura 2. Filtrado con etiquetas*

![Pestaña OpenPages Tipo de objeto de riesgo, con el botón Filtro resaltado, seguido de una imagen de la ventana Exportar riesgos, con el botón de selección Vista de cuadrícula seleccionado](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_filter_by_tags.png)

### Aplicar automáticamente los cambios de los flujos de trabajo recién publicados

Ahora los cambios se pueden aplicar automáticamente a los flujos de trabajo en curso sin necesidad de terminarlos y reiniciarlos. Para obtener más información, consulte [Definiciones de flujo de trabajo e instancias de flujo de trabajo](3.3-guia-del-administrador.md#definiciones-e-instancias-de-flujo-de-trabajo).

### Establecer valores de campo basados en respuestas de cuestionario

Actualizar automáticamente los campos basándose en las respuestas a los cuestionarios. Una acción de respuesta establece el valor de los campos en los objetos basándose en las respuestas que proporciona un encuestado en una evaluación de cuestionario. Como resultado, se puede utilizar una interfaz de usuario de cuestionario simple para clasificar a los proveedores, clasificar los activos como altos, medios o bajos, y enriquecer la información de inventario en función de las respuestas proporcionadas por el usuario. Para obtener más información, consulte  [Establecimiento de los valores de campo de un objeto basándose en las respuestas de un encuestado](4-guia-del-usuario.md#establecer-los-valores-de-campo-de-un-objeto-basándose-en-las-respuestas-de-un-encuestado).

*Figura 3. Configuración de una acción de respuesta*

![Abra la pantalla de acción Respuesta de página.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_questionnaire_response_action.png)

### Crear y acceder a una vista de informe

Cree una vista de informe que muestre información específica que los usuarios necesitan. Las vistas de informe se crean utilizando el Diseñador de vistas. Se muestran como una pestaña en el objeto, además de la vista Tarea, la vista Actividad y la vista Admin (donde sea aplicable). Estas vistas son de sólo lectura y se pueden imprimir en PDF para simplificar el gobierno y el uso compartido de actividades de conformidad con la normativa (GRC). Para obtener más información, consulte [Definición de una vista de informe](3.6-guia-del-administrador.md#definición-de-una-vista-de-informe).

*Figura 4. Creación de una vista de informe*

![Pestaña OpenPages Vistas con el panel Nueva vista expandido y resaltado. El menú Tipo de vista se ha expandido con Admin seleccionado. La pantalla siguiente muestra una nueva pestaña de vista que muestra la etiqueta, Mi nueva vista de administrador.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_create_access_report_view.png)

### Añadir etiquetas a vistas

Se ha añadido un nuevo campo **Etiqueta** a la configuración de vista. A diferencia de la vista **Nombre**, puede editar la **Etiqueta** después de crear una vista. La etiqueta se muestra en la cuadrícula Ver y aparece como el nombre de la pestaña en la vista Informe.

*Figura 5. Adición de una etiqueta a una vista*

![Pestaña OpenPages Vistas con el panel Nueva vista expandido. El campo Etiqueta se resalta y dice, Nueva etiqueta de vista. La pantalla siguiente muestra una nueva pestaña de vista con el título Nueva etiqueta de vista resaltada](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_add_labels_to_views.png)

### Copiar vistas existentes

Al crear una vista nueva, ahora puede pulsar **Copiar vista** para replicar la vista actual o copiar una existente. A continuación, puede editar la copia para satisfacer sus necesidades. La copia de una vista se puede realizar al crear una vista o al utilizar el Diseñador de vistas. La copia se puede realizar tanto en vistas personalizadas como en vistas de sistema de sólo lectura para que pueda utilizar vistas de sistema listas para usar para vistas personalizadas sin tener que volver a crearlas desde cero. Para obtener más información, consulte [Copia de una vista](3.6-guia-del-administrador.md#copia-de-una-vista).

*Figura 6. Crear una vista copiando de una vista existente*

![OpenPages Pantalla Vista de tarea con el botón Copiar vista resaltado, seguida de una pantalla Vista de tarea con el panel Nueva vista visualizada. La pantalla final muestra el menú Tipo en el panel Nueva vista expandida y Tarea seleccionada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_copy_existing_views.png)

### Imprimir y exportar vistas

Exporte las vistas como informes limpios y fáciles de leer en unos pocos clics. El tipo de exportación depende de la vista. Imprima en PDF pulsando **Imprimir** ![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/print_button.png) para las vistas siguientes:

- tarea
- Administrador
- Informe

Exporte a Excel pulsando **Exportar** ![botón Exportar](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/tfui_export_icon.JPG) para las vistas siguientes:

- Cuadrícula
- Actividad

Al seleccionar **Imprimir**![Botón Imprimir](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/print_button.png) en una vista, puede imprimir una vista detallada en PDF. El archivo puede imprimirse o guardarse y compartirse como PDF. Los usuarios pueden definir un título de impresión, que se muestra en la cabecera del informe y en el nombre de archivo, cuando se exporta. Es fácil de leer y excluye los controles del navegador y los elementos de navegación, como botones, campos de búsqueda, menús, barras de desplazamiento, recuadros de selección y URL. El archivo exportado incluye texto enriquecido, estado de flujo de trabajo, etiquetas, enlaces a objetos y toda la información de cuadrícula tabular. El informe también captura la fecha y hora de la exportación para su auditabilidad. Para obtener más información, consulte  [Impresión de una vista en PDF](4-guia-del-usuario.md#imprimir-una-vista-en-pdf).

*Figura 7. Impresión de una vista de tarea*

![OpenPages 2021 La vista Pagos AML-Carta de notificación se ha abierto con el botón de impresión resaltado, seguido de la misma pantalla con la ventana Imprimir abierta. La pantalla final muestra una vista impresa de la vista Pagos AML-Carta de notificación de 2021.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_print_and_export_views_pdf.png)

Para compartir datos desde la vista de cuadrícula o actividad, pulse **Exportar** ![botón Exportar](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/tfui_export_icon.JPG) para descargar un archivo de Microsoft Excel.

*Figura 8. Exportación de datos desde una vista de cuadrícula*

![OpenPages Pantalla de la vista Riesgos con el botón Exportar resaltado, seguido de la pantalla de la vista Riesgos con la ventana Exportar riesgos abierta y el botón de selección Vista de cuadrícula seleccionado.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_print_export_view_grid.png)

### Filtrar datos en la vista Actividad

Ahora hay nuevas opciones de filtro disponibles en la vista Actividad. Puede refinar la búsqueda según fechas, horas y usuarios específicos. Para ver cómo funciona, lea  [Visualización del historial de cambios en la pestaña Actividad](4-guia-del-usuario.md#visualización-del-historial-de-cambios-en-la-pestaña-actividad) .

*Figura 9. Filtrado de la vista Actividad*

![La pantalla OpenPages que muestra la vista Tema de biblioteca-Actividad de supervisión de gobierno de datos. El panel Filtro se expande, mostrando los campos Fecha de inicio, Hora de inicio, Fecha de finalización y Hora de finalización.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_filter_data_in_activity_view.png)

### Personalizar gráficos con ordenación de datos mejorada

Personalice y ordene los datos del gráfico para obtener una visualización y un análisis más precisos. Ordene los valores de gráfico según la definición de campo, o en orden ascendente o descendente. Por ejemplo, un gráfico que muestra la gravedad siempre presenta *Alta*, *Media*, *Baja* en el mismo orden en lugar de basarse en la cantidad agregada. Para obtener más información, consulte [Adición de un diagrama de gráfico](3.6-guia-del-administrador.md#adición-de-un-diagrama-de-gráfico).

*Figura 10. Ordenación de datos en un gráfico*

![OpenPages Pantalla de la página de inicio con el panel Diseño visualizado. Se expande el menú Ordenar dirección y se selecciona el orden de definición de campo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/new_feature_9001_customize_charts_enhanced_data_sorting%20.png)

### Software soportado en 9.0.0.1

OpenPages ahora da soporte a Cognos® 12.0.1. También se admiten los releases continuos 12.0.x posteriores. Para obtener más información, consulte [Software de requisito previo para servidores de informes](5.1-guia-de-instalacion-y-despliegue-solo-local.md#software-de-requisito-previo-para-servidores-de-informes).

## Características nuevas de la versión 9.0.0

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-900)

Las nuevas características de IBM OpenPages® 9.0.0.0 incluyen las mejoras siguientes.

### Mejoras de la interfaz de usuario en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-ui-enhancements-in)

En versiones anteriores de IBM OpenPages®, cuando cambiaba la paleta de colores para un campo enumerado, tenía que cambiarla en el Diseñador de vistas para cambiar el color del campo en todas las vistas.

En IBM OpenPages 9.0.0, en lugar de utilizar el Diseñador de vistas, ahora especifique la paleta de colores para un campo enumerado cuando especifique la definición del campo para un tipo de objeto. Para obtener más información, consulte [Definición de campos de serie enumerada](3.1-guia-del-administrador.md#definición-de-campos-de-serie-enumerados).

### Mejoras del flujo de trabajo en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-workflow-enhancements-in)

Se han realizado varias mejoras para ayudarle a administrar, mantener y dar soporte IBM OpenPages®.

#### Mensajes de error personalizados

Ahora los administradores pueden crear mensajes personalizados que se mostrarán a los usuarios cuando se desencadene una validación dentro de un flujo de trabajo. En lugar de basarse en mensajes generados automáticamente, los administradores ahora pueden proporcionar orientación específica (hasta 196 caracteres) al usuario final en relación con las acciones que deben llevarse a cabo para avanzar en el flujo de trabajo y evitar desencadenar la validación. Esta es una característica opcional, y el mensaje de validación generado automáticamente existente se mostrará en las instancias en las que no se haya definido un mensaje personalizado en el Diseñador de flujos de trabajo.

*Figura 1. La nueva opción **Mensaje de error personalizado** en el Diseñador de flujos de trabajo al crear una validación*

![Se muestra el panel Validaciones. Incluye un campo denominado Mensaje de error personalizado.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-wf_customerr1.png)

La imagen de la izquierda muestra una vista del sistema 8.3.0.2 . En esta vista, se ha desencadenado una validación que utiliza lógica avanzada desde un flujo de trabajo listo para usar. La imagen de la derecha muestra un sistema 9.0 . En esta vista, se ha desencadenado la misma validación, pero esta vez se ha creado un mensaje de error personalizado para la validación. El mensaje de error personalizado indica al usuario que rellene un campo de texto porque dos valores de campo no coinciden cuando se esperaba que coincidiesen.

*Figura 2. La opción de mensaje de error personalizado para flujos de trabajo*

![Se muestran dos imágenes. La primera imagen muestra una vista de tarea en la versión 8.3.0.2. Se muestra un mensaje de aviso. Muestra siete avisos. La segunda imagen muestra la misma vista de tarea en 9.0.0. Se muestra un mensaje de aviso. Contiene un aviso. Un indicador en el panel lateral muestra que dos campos tienen valores no coincidentes. El panel lateral proporciona orientación sobre cómo solucionar el problema.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-wf_customerr2.png)

#### Avance automático de la etapa de flujo de trabajo

La característica de avance automático de la etapa de flujo de trabajo permite a los administradores habilitar un valor en el Diseñador de flujo de trabajo para avanzar una etapa de flujo de trabajo automáticamente basándose en una condición en el objeto de flujo de trabajo. Los administradores pueden utilizar el motor de cálculo, una acción de flujo de trabajo o requerir una selección manual por parte del usuario para establecer el valor de campo en el objeto de flujo de trabajo para satisfacer la condición establecida en el flujo de trabajo para avanzar automáticamente en la etapa.

Para utilizar esta característica, seleccione una acción en un flujo de trabajo y seleccione la opción **Etapa de avance automático** .

*Figura 3. La nueva opción **Etapa de avance automático** en el Diseñador de flujos de trabajo al crear una acción*

![Se muestra el panel Propiedades de acción. Incluye un nuevo conmutador que se llama Auto-Advance Stage. En este ejemplo, la etapa de avance automático está habilitada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-wf_stage1.png)

En la misma acción, establezca una condición en el objeto que es el sujeto del flujo de trabajo.

En el ejemplo siguiente, cuando el campo Comentario de ciclo de vida tiene un valor de **Elementos de acción completados**, la etapa de flujo de trabajo avanza automáticamente.

*Figura 4. Definición de la condición*

![Se muestra el panel Propiedades de acción. En este ejemplo, se establece una condición para la acción: Comentario de ciclo de vida de emisión = Elementos de acción completados.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-wf_stage2.png)

Un flujo de trabajo de ejemplo con el valor **Etapa de avance automático** habilitado está disponible en el flujo de trabajo Revisión de problema. Este flujo de trabajo está disponible en instalaciones nuevas de 9.0. En el flujo de trabajo de ejemplo, la etapa **En espera de finalización** avanza automáticamente cuando el campo Comentario de ciclo de vida es igual a **Elementos de acción completados**. El valor **Elementos de acción completados** para el campo Comentario de ciclo de vida se establece mediante el cálculo de ejemplo **Emitir avance automático de etapa de flujo de trabajo** . Este cálculo cuenta cada elemento de acción hijo bajo el problema. Cuando todos los elementos de acción hijo están en estado Cerrado, el campo Comentario de ciclo de vida se establece con el valor que hace avanzar la etapa de flujo de trabajo.

*Figura 5. El flujo de trabajo de revisión de problemas con el valor **Etapa de avance automático** configurado para la etapa **En espera de finalización***

![El flujo de trabajo de revisión de problemas se muestra en el Diseñador de flujos de trabajo. Se selecciona la acción entre la etapa En espera de finalización y la etapa Aprobación FInal. Se muestra el panel lateral Propiedades de acción. La opción Etapa de avance automático está habilitada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-wf_stage3.png)

### Mejora del etiquetado en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-tagging-enhancement-in)

En IBM OpenPages® 9.0.0, se han realizado las siguientes mejoras en el etiquetado.

- Las etiquetas ahora se pueden crear y asignar ejecutando un modelo de IA utilizando la funcionalidad de modelo de aprendizaje automático personalizado. Para obtener más información, consulte [Integración de modelo de aprendizaje automático personalizado en 9.0.0](#integración-del-modelo-de-aprendizaje-automático-personalizado-en-900).
- Ahora los administradores pueden especificar qué tipos de objeto pueden tener etiquetas.

Como administrador, puede limitar la aplicación de etiquetas a tipos de objeto específicos.

Por ejemplo, puede tener uno de los siguientes casos de uso:

- Desea limitar las etiquetas de identificación sólo a Controles.
- Desea no permitir etiquetas para tipos de valor o valor porque no es necesario etiquetarlas cuando se etiqueta su padre.

Si desea impedir la aplicación de etiquetas a tipos de objeto específicos, realice los pasos siguientes.

1. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Etiquetas**.
2. En el panel **Valores del sistema** , pulse el recuadro **Habilitar etiquetado para estos tipos de objeto** .
3. Deseleccione los tipos de objeto para los que no desea permitir etiquetas.

   Por ejemplo, la Figura 1 muestra el panel **Valores del sistema** donde el tipo de objeto Cuenta está deseleccionado para que los usuarios no puedan aplicar etiquetas a Cuentas.

   *Figura 1. El panel **Valores del sistema** con el tipo de objeto Cuenta deseleccionado.*

   ![Se muestra el panel Valores del sistema. Muestra que las etiquetas no están permitidas para los tipos de objeto de cuenta.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-tags_system_settings.png)

### Mejoras del cuestionario en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-questionnaire-enhancements-in)

En IBM OpenPages® 9.0.0, puede responder a un cuestionario en modalidad autónoma y definir lógica compleja para dependencias en plantillas de cuestionario.

#### Respuesta al cuestionario

Ahora puede abrir una evaluación de cuestionario en modo autónomo pulsando ![Iniciar el cuestionario en el icono de modo en curso](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/qr_launch_stand-alone.png) en la pestaña **Cuestionario** .

*Figura 1. Una evaluación de cuestionario que muestra el icono utilizado para abrir la evaluación en modo autónomo*

![Una evaluación de cuestionario que muestra el icono utilizado para abrir la evaluación en modo autónomo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-questionnaire_stand-alone.png)

Responder a los cuestionarios es ahora más fácil con el nuevo formato para preguntas de una sola opción y de varias. Las preguntas de opción única o múltiple con nueve o más opciones muestran las opciones en un campo desplegable o de selección múltiple.

*Figura 2. Una única pregunta de elección con nueve o más opciones.*

![Una evaluación de cuestionario que muestra una pregunta de opción única con nueve o más opciones.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-questionnaire_single_morethan8.png)

*Figura 3. Una pregunta de opción múltiple con nueve o más opciones.*

![Una evaluación de cuestionario que muestra una pregunta de varias opciones con nueve o más opciones.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-questionnaire_multi_morethan8.png)

#### Dependencias de la pregunta

Ahora puede utilizar una plantilla de cuestionario para especificar lógica compleja para que las dependencias oculten o muestren preguntas. Se da soporte a la lógica siguiente:

- Preguntas que tienen hasta tres niveles de dependencia para preguntas que dependen de las respuestas a otras preguntas.
- Preguntas que dependen de otras preguntas en otra sección o subsección.
- Preguntas que dependen de los valores de los campos de objeto.
- Preguntas que dependen de varias condiciones y lógica avanzada para combinar varias condiciones. La lógica avanzada utiliza una expresión que consta de los números de condición combinados con los operadores `AND`, `OR`, `NOT`y paréntesis. La expresión no distingue entre mayúsculas y minúsculas.

*Figura 4. El generador de condiciones donde se especifican las condiciones para las preguntas dependientes*

![El generador de condiciones donde se especifican las condiciones para las preguntas dependientes.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-questionnaire_condition_builder.png)

### Integración del modelo de aprendizaje automático personalizado en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-custom-machine-learning-model-integration-in)

En IBM OpenPages® 9.0.0, la integración del modelo de aprendizaje automático personalizado ahora da soporte a la conexión con los servicios siguientes.

- IBM Watson® Machine Learning en IBM Cloud
- IBM Watson Machine Learning en Cloud Pak for Data
- IBM® Natural Language Understanding on Cloud para características como clasificación, extracción de entidades y resumen de texto

La integración mejorada da soporte a los siguientes casos de uso:

- **Insight** que muestra información para modelos como, por ejemplo, controles cognitivos y PII.
- **Establecer campos** que utiliza modelos de clasificación que establecen campos.

  Antes de intentar este caso de uso, consulte [OpenPages Lista de problemas conocidos](https://www.ibm.com/support/pages/node/6998093).
- **Conjunto de etiquetas** que utiliza modelos para sugerir etiquetas para establecer en el objeto.

La integración del modelo de aprendizaje automático personalizado incluye las siguientes características nuevas:

- Los usuarios pueden ejecutar modelos, establecer etiquetas o establecer campos de forma manual o automática.
- Los administradores pueden establecer umbrales de confianza de modelo para su visualización y personalizar la visualización de las notificaciones de modelo y el estilo para el usuario.
- La nueva interfaz incluye interacciones de usuario y visualizaciones mejoradas.

*Figura 1. La página **Orientación** donde el administrador establece las notificaciones y el estilo de salida para el usuario*

![La página Orientación donde el administrador establece las notificaciones y el estilo de salida para el usuario.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-ml_config_user_guidance.png)

### Mejoras de filtrado en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-filtering-enhancements-in)

IBM OpenPages® 9.0.0 presenta varias mejoras en el filtrado.

#### Filtrado de objetos ancestros y descendientes

Anteriormente, los usuarios solo podían filtrar objetos padre e hijo. Sin embargo, con OpenPages 9.0.0, los usuarios ahora pueden crear filtros ad hoc y privados para objetos ancestros y descendientes en paneles de control y vistas de cuadrícula.

Para obtener más información sobre el filtrado de objetos relacionados en filtros ad hoc y privados, consulte  [Definición de filtros privados](4-guia-del-usuario.md#definición-de-filtros-privados)  .

#### Restricciones en las acciones de asociación y copia para usuarios

Al definir las acciones **Añadir**, **Copiar recurrente**o **Establecer padre primario** en una vista de tarea, los administradores ahora pueden prohibir que los usuarios eliminen los filtros establecidos para estas acciones.

Para obtener más información sobre cómo prohibir que los usuarios eliminen filtros, consulte  [Adición de una acción Añadir](3.6-guia-del-administrador.md#adición-de-una-acción-añadir), [Adición de una acción Establecer padre primario](3.6-guia-del-administrador.md#adición-de-una-acción-establecer-padre-primario)y [Adición de una acción Copiar recurrente](3.6-guia-del-administrador.md#adición-de-una-acción-copia-recurrente)  .

#### Nuevas operaciones de filtro

Hay nuevos operadores disponibles para filtros ad hoc, privados y públicos.

La tabla siguiente lista los nuevos operadores disponibles para cada tipo de datos de campo:

**Tabla 1. Nuevos operadores para filtros**

| Tipo de datos | Nuevos operadores |
| --- | --- |
| Serie simple | Está vacío, No está vacío, No es igual a, No contiene |
| Cadena larga | Está vacío, No está vacío, No contiene |
| Cadena enumerada | Está vacío, No está vacío |
| Entero o decimal | Está vacío, No está vacío, No es igual a |
| Moneda | Está vacío, No está vacío, No es igual a |
| Fecha | Está vacío, No está vacío, No en una fecha específica |
| Usuario o grupo | Está vacío, No está vacío |
| Booleano | Está vacío, No está vacío |
| Selector de entidad de negocios | Está vacío, No está vacío, No es igual a, No contiene |

Para obtener más información sobre los operadores disponibles para filtros, consulte  [Adición de filtros a tipos de objeto](3.2-guia-del-administrador.md#adición-de-filtros-a-tipos-de-objeto) y [Definición de filtros privados](4-guia-del-usuario.md#definición-de-filtros-privados)  .

#### Nuevo filtro de relaciones compartidas

Con un filtro de relaciones compartidas, los administradores pueden limitar las opciones de los usuarios para asociaciones o copiar acciones recursivas. Un administrador puede optar por permitir a los usuarios seleccionar sólo objetos con un ancestro compartido o descendiente del objeto actual.

Para obtener más información sobre los filtros de relaciones compartidas, consulte  [Creación de un filtro de relaciones compartidas](3.6-guia-del-administrador.md#creación-de-un-filtro-de-relaciones-compartidas)  .

### Mejoras de soluciones en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-solutions-enhancements-in)

Las soluciones de IBM OpenPages® se han mejorado para hacerlas más completas y fáciles de utilizar.

- Metodología de ámbito basado en cuenta en IBM OpenPages Financial Controls Management
- Mejoras en IBM OpenPages Data Privacy Management
- Mejoras en IBM OpenPages Internal Audit Management
- Mejoras en IBM OpenPages IT Governance
- Mejoras en IBM OpenPages Model Risk Governance
- Mejoras en IBM OpenPages Policy Management
- Mejoras en IBM OpenPages Regulatory Compliance Management
- Mejoras en OpenPages Gestión de riesgos de terceros

#### Metodología de ámbito basado en cuenta en IBM OpenPages Financial Controls Management

Se dispone de una metodología de ámbito de referencia para ayudar al usuario a estimar la materialidad de la cuenta utilizando un umbral de cálculo del 5% para los valores de clasificación de cuenta. Este porcentaje se puede ajustar en función del proceso interno de la organización.

Por ejemplo, cuando el usuario especifica un importe en el campo Valor anualizado, el cálculo calcula el porcentaje de valor anualizado del registro basándose en la suma de todos los objetos Cuenta con la misma clasificación y entidad empresarial padre. Si el porcentaje de valor anualizado es del 5% o superior, el valor del campo Cuenta en ámbito se establece en **Sí**. Si el porcentaje de valor anualizado está por debajo del 5%, el campo Cuenta en ámbito se establece en **No**.

*Figura 1. La vista de cuadrícula Cuentas con los nuevos campos de clasificación*

![Se muestra una vista de cuadrícula para cuentas. Las columnas incluyen Tipo de cuenta, Clasificación, Valor anualizado y Porcentaje de valor anualizado.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-fcm_account_gridview.png)

Se han añadido campos de clasificación al objeto Entidad de negocios. Se ha añadido una nueva sección, Totales de clasificación de cuenta, a las vistas de objeto Entidad de negocios relacionadas. Un cálculo establece los campos de esta sección.

*Figura 2. Una vista de tarea de entidad empresarial con una nueva sección para la clasificación de cuentas*

![Se muestra una vista de tarea para una entidad empresarial. Una sección denominada Totales de clasificación de cuenta muestra los valores calculados y un gráfico de barras verticales colorido.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-fcm_be_taskview.png)

Se han añadido nuevos cálculos, informes, campos y vistas de Cuenta y Entidad de negocios actualizadas para dar soporte a este proceso.

**Nuevos cálculos**

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

**Informes nuevos**

- **Ámbito de cuenta por entidad y clasificación**

  Este informe muestra los objetos Cuentas por entidad de negocios y clasificación. El informe incluye los valores de los campos Tipo de cuenta, Saldo, Porcentaje anual y En ámbito.

  *Figura 3. Informe de ámbito de cuenta por entidad y clasificación*

  ![Se muestra un informe tabular. Las cuentas se agrupan por clasificación: Activos, Acciones y Gastos. Las columnas son Clasificación de cuenta, Cuenta, Tipo, Balance de cuenta, Porcentaje anualizado y En ámbito. Para cada clasificación, una fila Total muestra el saldo total de la cuenta para la clasificación.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-fcm_account_report.png)

- **Correlación de cuentas y procesos de FCM**

  Los usuarios pueden elegir la correlación de relaciones de proceso y/o cuenta para visualizarla en el informe.

  Por ejemplo, los usuarios pueden ver cuentas que están en el ámbito y no están asociadas a procesos junto con procesos que están en el ámbito y no están asociados a cuentas.

  *Figura 4. Correlación de procesos y cuentas-selección de opciones*

  ![Se muestra un informe. Un conjunto de recuadros de selección permite a los usuarios realizar selecciones para el informe.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-fcm_process_report1.png)

  *Figura 5. Correlación de proceso y cuenta-informe*

  ![Se muestra un informe tabular. Muestra cuentas y procesos que están en el ámbito.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-fcm_process_report2.png)

**Un panel de control actualizado**

El panel de control actualizado incluye los nuevos informes de ámbito de FCM (en el mosaico Informes) y un mosaico de datos de clasificación.

*Figura 6. Panel FCM*

![Se muestra el panel de control con tareas FCM, informes y otros datos. Un gráfico de barras muestra las cuentas en el ámbito por clasificación. Una serie de gráficos circulares muestra cuentas, procesos y controles clave que están en el ámbito de SOX.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-fcm_dashboard.png)

#### Mejoras en IBM OpenPages Data Privacy Management

Las mejoras en DPM incluyen:

**Campos de nuevo activo**

Se han añadido varios campos nuevos al tipo de objeto Activo (Recurso) para habilitar la captura de actividades de proceso y volver a identificar el riesgo.

**Panel de control maestro actualizado**

El panel de control de DPM listo para usar se ha actualizado para incluir información más rica sobre activos de datos, actividades de proceso, evaluaciones de privacidad y riesgo.

*Figura 7. Panel de control maestro de DPM*

![Se muestra un panel de control con tareas de DPM, enlaces y otros datos. Los gráficos coloridos muestran información sobre activos de datos.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-dpm_master_dashboard.png)

**Nuevos perfiles y paneles de instrumentos**

- **Responsable de privacidad de DPM**

  Este perfil está pensado para roles relacionados con la conformidad y el riesgo de privacidad. El panel de control Oficial de privacidad de DPM resalta la información que sería relevante para los usuarios en este rol.

  *Figura 8. Panel de control Oficial de privacidad de DPM*

  ![Se muestra un panel de control con tareas de DPM, enlaces y otros datos. Los gráficos coloridos muestran información sobre el cumplimiento de la privacidad de los datos y las evaluaciones de privacidad.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-dpm_dpo_dashboard.png)

- **Encargado de datos de DPM**

  Este perfil está pensado para roles técnicos relacionados con la privacidad de datos, como representantes de datos e ingenieros de datos. El panel de control del encargado de datos resalta la información que sería relevante para los usuarios de este rol.

  *Figura 9. Panel de control encargado de datos de DPM*

  ![Se muestra un panel de control con tareas de DPM, enlaces y otros datos. Los gráficos coloridos muestran información sobre las evaluaciones de privacidad y los activos de datos.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-dpm_ds_dashboard.png)

#### Mejoras en IBM OpenPages Internal Audit Management

Las mejoras en IAM incluyen:

**Nuevo tipo de objeto: Plan de auditoría de resumen**

El tipo de objeto Plan de auditoría de resumen permite a una oficina del programa planificar auditorías de entidades auditables durante un periodo de tiempo predeterminado (anual, medio año, o trimestre) por ámbito, perfil de riesgo, horas de previsión de auditorías, etc.

El objeto Plan de auditoría de resumen es un hijo de Entidad de negocios. Los hijos del plan de auditoría de resumen incluyen: Auditoría y Entidad auditable.

Se han añadido nuevas vistas para dar soporte al objeto Plan de auditoría de resumen.

**Nuevo cálculo: Resumen de presupuesto y planes de plan de auditoría**

Calcula los campos siguientes para la vista de objeto Plan de auditoría de resumen: Bajo Más de horas, Horas de auditoría asignadas, Horas completadas y Horas restantes. Los valores de estos campos se suman a partir de los objetos Entidad auditable y Auditoría relacionados.

**Un panel de control actualizado**

*Figura 10. Panel de control de IAM*

![Se muestra el panel de control con tareas de IAM, informes y otros datos. Un gráfico de barras muestra la auditoría por tipo. Otro muestra los resultados por prioridad. Un diagrama de Gantt muestra la planificación de auditoría.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-iam_dashboard.png)

#### Mejoras en IBM OpenPages IT Governance

Las mejoras en ITG incluyen:

**Tipo de objeto nuevo: Amenaza**

Una amenaza es cualquier circunstancia o suceso con el potencial de afectar negativamente a las operaciones y activos de la organización. Se puede crear una biblioteca de amenazas bajo el objeto Entidad de negocios y asociarse o copiarse en un objeto Proceso, Sistema o Activo padre. Las amenazas también se pueden asociar a vulnerabilidades para identificar y evaluar la probabilidad y el impacto de la explotación de una vulnerabilidad por parte de una amenaza, lo que podría dar lugar a un riesgo para un activo, un sistema o un proceso.

**Panel de control actualizado**

*Figura 11. Panel de instrumentos maestro de ITG*

![Se muestra un panel de instrumentos con tareas y datos de ITG. Los gráficos de anillo coloridos muestran el estado de los sistemas, las evaluaciones de riesgos, los problemas y las incidencias.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-itg_dashboard.png)

**Cálculos nuevos**:

- Activo-Calificación de vulnerabilidad
- Sistema-Calificación de vulnerabilidad
- Vulnerabilidad-Evaluación de amenazas

**Nuevos flujos de trabajo**:

- **Revisión de vulnerabilidad**

  Este flujo de trabajo automático realiza un seguimiento del progreso de la evaluación de la gravedad de una vulnerabilidad identificada y proporciona una opción para que el usuario inicie el flujo de trabajo Evaluación de amenazas.

- **Evaluación de amenazas**

  Este flujo de trabajo manual se puede iniciar desde el flujo de trabajo Revisión de vulnerabilidad.

  El flujo de trabajo Evaluación de amenazas realiza un seguimiento del progreso de la identificación de cualquier amenaza que pueda explotar una vulnerabilidad y la evaluación de la probabilidad y el impacto de la explotación de la vulnerabilidad por parte de las amenazas identificadas.

- **Exención de TI**

  Este flujo de trabajo automático realiza un seguimiento de la solicitud y respuesta para obtener una renuncia siempre que la renuncia se clasifique como InfoSec Política, política de TI, requisito de TI o control de TI en el campo Tipo. Si la solicitud se aprueba, el responsable debe proporcionar una fecha de caducidad para la cancelación. De lo contrario, se asigna una fecha de caducidad de un año a partir de la fecha de aprobación.

- **Revisión de caducidad de exención de TI**

  Este flujo de trabajo automático se inicia en una planificación para cualquier Waiver aprobado desde el flujo de trabajo IT Waiver cuando la fecha de caducidad es inferior a 30 días a partir de la fecha en que se ejecuta la planificación. El usuario que ha solicitado la aprobación en el flujo de trabajo de Waiver de TI determinará si es necesaria una extensión de Waiver. Si se necesita una extensión, la cancelación avanzará a la etapa de revisión de extensión de cancelación, donde se aprobará y se otorgará una nueva fecha de vencimiento o se rechazará.

#### Mejoras en IBM OpenPages Model Risk Governance

Las mejoras en MRG incluyen:

**Nuevos campos y grupos de campos**

Se han añadido muchos campos a Model Use Case (Register), Model y Model Deployment (Usage) para dar soporte a la integración con AI Factsheets, y para habilitar las mejoras realizadas en la metodología predefinida mediante una colaboración con los laboratorios expertos de IBM para producir las mejores prácticas para el gobierno de IA. El uso del objeto Caso de uso de modelo (Registro) ahora es más prominente en la solución para realizar un seguimiento de los casos de uso para los que se están creando los modelos.

**Vistas actualizadas**

La mayoría de las vistas del sistema para objetos MRG que incluyen Caso de uso de modelo (Registro), Modelo, Despliegue de modelo (Uso), Métrica, Valor de métrica, Revisión, Desafío, Tabla de puntuación de riesgo de modelo, Testificación de modelo y Solicitud de cambio se han renovado y actualizado con una mejor orientación e información más útil.

Varias vistas para los objetos Modelo y Revisión se han consolidado en una única vista para cada objeto. Los flujos de trabajo que hacen referencia a las vistas antiguas se han actualizado para que apunten a una única vista.

*Figura 12. Parte de la vista de tarea Modelo actualizada*

![Se muestra la vista de tarea para el objeto Modelo. Una cuadrícula muestra casos de uso padre para el modelo. Otra cuadrícula muestra revisiones de modelo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-mrg_taskview.png)

**Paneles de instrumentos nuevos**

Los paneles de control MRG listos para usar se han actualizado para incluir información más rica sobre los modelos, el riesgo, el rendimiento y los datos que son relevantes para los perfiles de usuario respectivos.

*Figura 13. Panel de control maestro de MRG*

![Se muestra un panel de control con tareas y datos de MRG. Un gráfico de barras muestra los modelos por departamento. Otro muestra el estado de conformidad de los modelos. Varios gráficos de anillo muestran modelos por agrupaciones o categorías.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-mrg_dashboard1.png)

*Figura 14. Panel de control para el perfil de validación de modelo MRG*

![Se muestra un panel de control con tareas y datos de MRG. Los gráficos de anillo muestran modelos por riesgo de modelo, estado de validación y rendimiento.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-mrg_dashboard2.png)

*Figura 15. Panel de control para el perfil de propietario de modelo MRG*

![Se muestra un panel de control con tareas y datos de MRG. Los gráficos de anillo muestran el inventario del modelo. Un gráfico de barras muestra los modelos por departamento.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-mrg_dashboard3.png)

**Flujo de trabajo nuevo: Ciclo de vida de modelo**

El flujo de trabajo Ciclo de vida de modelo sustituye al flujo de trabajo Desarrollo de modelo (que ahora está inhabilitado de forma predeterminada) para los modelos de IA. Incluye algunas etapas adicionales para el aprovisionamiento y verificación de datos, y para la verificación de modelos desarrollados.

*Figura 16. Flujo de trabajo de ciclo de vida*

![Se muestra el flujo de trabajo. Tiene varias etapas y puntos finales.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-mrg_wf-model_lifecycle.png)

**Flujo de trabajo nuevo: solicitud de caso de uso de modelo**

El flujo de trabajo Solicitud de caso de uso de modelo se utiliza para evaluar el riesgo y obtener la aprobación empresarial para un caso de uso de modelo. Una vez que se ha aprobado un caso de uso de modelo, puede empezar el desarrollo del modelo.

*Figura 17. Flujo de trabajo de solicitud de caso de uso de modelo*

![Se muestra el flujo de trabajo. Tiene las etapas siguientes: Inicio, Propuesto, En espera de aprobación, Rechazado y Aprobado.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-mrg_wf-use_case_request.png)

**Flujo de trabajo nuevo: Despliegue del modelo**

El flujo de trabajo Despliegue del modelo se utiliza para controlar el proceso de despliegue del modelo una vez que se ha completado el desarrollo. Si el modelo se está desplegando en producción, hay un paso adicional para producir el modelo antes de que se complete el despliegue.

*Figura 18. Flujo de trabajo de solicitud de caso de uso de modelo*

![Se muestra el flujo de trabajo. Tiene las etapas siguientes: Iniciar, Desplegar Modelo, Verificar Despliegue, Desplegado y Productionizar modelo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-mrg_wf-model_deployment.png)

#### Mejoras en IBM OpenPages Policy Management

Las mejoras en PCM incluyen:

**Flujo de trabajo nuevo: Retirar flujo de trabajo de política**

Este flujo de trabajo se desencadena cuando el estado de publicación = Listo para retirar.

El flujo de trabajo lleva al usuario a través de un proceso de revisión y aprobación para retirar la política. En cada una de estas etapas, se genera un objeto Comentario de revisión de políticas (PRC) para documentar la etapa de aprobación de SME y la etapa de aprobación ejecutiva.

El ayudante de publicación debe desencadenarse al final del proceso para completar la retirada de la política. El ayudante de publicación suprimirá la política de borrador y moverá la versión publicada de la política a la carpeta de biblioteca de políticas caducada.

**Nueva documentación de**

El nuevo [Documento de solución de gestión de políticas deOpenPages](https://www.ibm.com/docs/es/SSFUEU_9.1/pdf/OpenPages_PCM_Solution_v91.pdf) proporciona detalles sobre la solución, incluida una visión general del ciclo de vida de la política, un inventario de lo que incluye la solución y una plantilla de importación de políticas de ejemplo.

#### Mejoras en IBM OpenPages Regulatory Compliance Management

Las mejoras en RCM incluyen:

**Nuevo tipo de objeto: evento regulador**:

El objeto Evento regulador se utiliza con IBM OpenPages Regulatory Compliance Management (RCM).

El tipo de objeto Evento regulador permite la ingestión directa de canales de información de eventos reguladores utilizando la API REST o IBM AppConnect en RCM. Junto con el motor de reglas, el tipo de objeto Evento regulador da soporte a la generación automatizada de flujos de trabajo que asignan sucesos reguladores entrantes a los usuarios en función de los puntos de datos proporcionados. También se da soporte a los documentos que se ven afectados por el cambio normativo. Estas prestaciones ayudan a asignar tareas de forma eficiente a los usuarios para responder a los cambios normativos y prepararse para ellos de forma eficiente. Un evento regulador puede ser un hijo de una entidad empresarial, control, mandato, submandato, requisito, política o procedimiento. Los usuarios pueden crear objetos de cambio regulador como hijos de eventos reguladores.

**Nuevos flujos de trabajo: Activar cambio-Regulador**

Este flujo de trabajo crea un registro de cambios regulatorios y asocia el registro a un evento regulatorio cuando se cumplen las condiciones de una regla del Motor de reglas que indican que el evento regulatorio aborda un cambio regulatorio como, por ejemplo, como una proposición de regla o regla final publicada en el registro federal. El flujo de trabajo también llena determinados campos en el registro de cambio regulador creado, incluida la categorización del registro de cambio regulador como cambio regulador. Este flujo de trabajo permite la asociación de varios registros de cambios regulatorios a un evento regulatorio, de forma que varios usuarios pueden analizar el impacto del suceso regulatorio sobre sus áreas concretas de responsabilidad dentro de la organización.

#### Mejoras en OpenPages Gestión de riesgos de terceros

Las mejoras en TPRM incluyen:

**Nuevos tipos de objeto:**

- **Subcontratista**: los objetos Subcontratista son objetos hijo de objetos Proveedor. Un subcontratista representa una parte de un servicio proporcionado por un proveedor. Subcontratista es un tipo de objeto opcional. Los subcontratistas pueden estar sujetos a evaluaciones de cuestionarios, evaluaciones de riesgos o niveles. Puede resumir y analizar el riesgo asociado a distintos subcontratistas. Puede añadir una asociación padre al proceso o subproceso al que da soporte un subcontratista.
- **Subsidiaria de proveedor**: una subsidiaria de proveedor representa una subsidiaria de un proveedor del que una empresa adquiere bienes o servicios. Subsidiaria de proveedor es un tipo de objeto opcional. Subsidiaria de proveedor es un hijo de Proveedor. La Filial Proveedor puede tener tres tipos de objetos hijo: SubContractor, Encargos y Contratos. La filial del proveedor puede estar sujeta a evaluaciones de cuestionarios, evaluaciones de riesgos o niveles. Puede resumir y analizar el riesgo asociado con diferentes filiales de proveedor. Puede añadir una asociación padre al proceso o subproceso al que da soporte una filial de proveedor.

### Mejoras de administración y capacidad de servicio

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-administration-serviceability-enhancements)

Se han realizado varias mejoras para ayudarle a administrar, mantener y dar soporte IBM OpenPages®.

#### Nuevo campo Título del sistema

La nueva característica Campo de título del sistema proporciona opciones adicionales que los administradores pueden utilizar para hacer referencia a un registro. Antes de 9.0, se proporcionaba a los administradores sólo una opción para hacer referencia a un registro dentro de OpenPages: el campo Nombre (`System Fields:Name`).

El campo Nombre se muestra en muchas ubicaciones prominentes dentro de OpenPages que no se pueden configurar para mostrar un campo diferente (incluyendo el banner en la parte superior de las vistas de tarea, diagramas de árbol de relaciones y paneles y pestañas en los paneles de control). El campo Nombre debe ser exclusivo dentro de una carpeta, lo que, a su vez, hace que el campo funcione más como un campo de ID que como la forma típica de hacer referencia a un registro por nombre. Como solución temporal a este problema, muchos clientes utilizan otro campo como Título del registro, lo que da como resultado una falta de estandarización dentro y entre entornos de cliente.

Para equilibrar la prevención de interrupciones para los clientes existentes y una mejor experiencia para los nuevos clientes, hemos creado una configuración totalmente opcional que está disponible para cada tipo de objeto, **Habilitar componente de título**. Esta opción controla cómo se visualiza la referencia a un objeto. Si la opción **Habilitar componente de título** se establece en **False** (que es el valor predeterminado para los clientes que actualizan a 9.0), no experimentará ningún cambio en el comportamiento relacionado con el campo Nombre del sistema.

Un administrador puede acceder a esta función haciendo clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Tipos de objetos**. Después de seleccionar un objeto, pulse el botón **Editar** para abrir un panel lateral que muestra la nueva opción **Habilitar componente de título** . Cuando establece la opción en **True**, se le proporcionan tres opciones para visualizar el campo Nombre: Sólo título, Título (ID) e ID (Título). Esta selección dicta cómo se hace referencia al objeto en todo el sistema y proporciona el componente Título al usuario final para que lo llene en los registros de este tipo de objeto. No es necesario que el componente Título sea exclusivo dentro de una carpeta y tiene un límite de 4.000 caracteres. En el mismo panel lateral, también puede hacer que el título sea un campo obligatorio, lo que impide que los usuarios guarden un registro a menos que se llene el campo Título.

*Figura 1. Ejemplo: Habilitación del componente Título para el tipo de objeto KRI*

![Se muestra la página de configuración para el tipo de objeto KRI. En otra imagen, se muestra el panel lateral. La nueva opción Habilitar componente de título está resaltada. La opción está activada y desactivada utilizando un botón de conmutación. Se muestran tres botones de selección: Título solamente, Título (ID) e ID (Título). También se muestra otro conmutador, Título. En este ejemplo, Habilitar componente de título se establece en True, Sólo título se selecciona y Título es necesario se establece en False.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_panel2.png)

Cuando **Habilitar componente de título** se establece en **True**, el campo Nombre muestra dos componentes: ID y Título. El campo ID se rellena con los valores existentes que se proporcionaron en el campo Nombre del sistema anterior a 9.0. Cuando **Habilitar componente de título** se establece en **False**, el campo de ID se llena con los valores rellenados en el campo Nombre.

El componente ID tiene las mismas reglas que se aplican al campo Nombre del sistema (un campo necesario y exclusivo dentro de una carpeta) y los valores de denominación automática se aplicarán al componente ID.

Cuando se rellena el componente Título, el campo Nombre se muestra en todo OpenPages de acuerdo con el valor **Visualización de nombre** establecido en la página Tipo de objeto. El valor de configuración también hace que el componente Título esté disponible en el diseñador de flujos de trabajo, los cálculos y en los filtros relacionados con ese objeto. Si el componente Título no se llena en un registro, se visualiza el valor que se proporciona en el componente ID.

El ejemplo siguiente muestra el Diseñador de vistas con los componentes ID y Título del campo Nombre. Puede establecer los valores de **Sólo lectura** y **Obligatorio** del componente Título en la vista.

*Figura 2. Ejemplo: Visualización de los componentes ID y Título del campo Nombre en el Diseñador de vistas*

![Se muestra el Diseñador de vistas. Se visualiza la vista de creación para el tipo de objeto KRI. El campo Nombre está seleccionado. En el panel lateral, se muestran los componentes ID y Título. Para Título, hay dos conmutadores disponibles: Sólo lectura y Obligatorio. En este ejemplo, ambos conmutadores se establecen en False.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_view_designer.png)

Este ejemplo muestra una vista de creación en la que el componente Título está habilitado y la denominación automática está en su lugar para el componente ID.

*Figura 3. Ejemplo: una vista de creación con título habilitado y denominación automática para el ID*

![Se visualiza la vista de creación para el tipo de objeto KRI. La sección General muestra el campo Nombre con dos componentes: ID y Título. El ID es _KRI_001. El campo Título está vacío. El panel lateral muestra que Name :ID es obligatorio y se ha completado mientras que Name: Title es opcional y todavía no se ha rellenado.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_view.png)

Basándose en el valor que se ha configurado en el objeto KRI, el componente Título se muestra en ubicaciones prominentes dentro de la vista de tarea. En el ejemplo siguiente, al pulsar el campo Nombre se muestran los componentes ID y Título cuando al menos un componente es editable; de lo contrario, el valor **Visualización de nombre** dicta la visualización del campo Nombre. En este ejemplo, el valor **Visualización de nombre** en el objeto KRI se establece en **Sólo título**y, por lo tanto, el componente Título se visualiza en la cabecera de la vista de tarea y en el diagrama de árbol de relaciones.

*Figura 4. Ejemplo: una vista de tarea con título habilitado*

![Se visualiza la vista de tarea del tipo de objeto KRI. La cabecera de la vista muestra el campo Título. La vista contiene un diagrama de árbol. Dentro del árbol, se muestra el título del KRI.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_view2.png)

El ejemplo siguiente muestra la vista de cuadrícula para KRI con Título habilitado. El componente Título se muestra en la columna Nombre en las vistas de cuadrícula, basándose en el valor del tipo de objeto KRI. Al pasar el cursor por encima de la entrada se muestra el ID y el título del objeto. Con el componente Título rellenado en este objeto, el ID, el título y la descripción están todos disponibles para la búsqueda y el filtrado en las vistas de cuadrícula.

*Figura 5. Ejemplo: una vista de cuadrícula con el título habilitado*

![Se visualiza la vista de cuadrícula del tipo de objeto KRI. El panel Filtro está abierto. La cuadrícula se filtra para mostrar los KRI donde Name.Title empieza por Reclamaciones de cliente. En la cuadrícula, la columna Nombre muestra el título de los KRI. El puntero del ratón está en el nombre de un KRI. Una ayuda contextual muestra el ID y el título del KRI.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_view3.png)

Los ejemplos siguientes muestran un panel de instrumentos con el valor **Visualización de nombre** que indica la visualización del campo Nombre para objetos KRI.

*Figura 6. Ejemplo: un panel de control con el título habilitado*

![Se muestra un panel de control. Un panel muestra los cinco KRI principales por fecha de vencimiento. La lista muestra los títulos de los KRI. El ratón pasa por encima de Reclamaciones de cliente. La ayuda contextual muestra el ID y el título del KRI.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_dashboard.png)

*Figura 7. Ejemplo: la pestaña del panel de control Mis tareas con Título habilitado*

![Se muestra la pestaña Mis tareas. En una cuadrícula, se listan los KRI. La columna Nombre muestra el título de los KRI.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_dashboard2.png)

El valor **Visualización de nombre** proporciona los componentes ID y Título dentro del flujo de trabajo y los motores de cálculo. Si el valor **Habilitar componente de título** se establece en **False**, sólo se mostrará el campo Nombre (y no los dos componentes ID y Título) (el comportamiento pre-9.0 ).

El ejemplo siguiente muestra el diseñador de flujos de trabajo con el valor **Visualización de nombre** que indica la visualización del campo Nombre.

*Figura 8. Ejemplo: un flujo de trabajo en el diseñador con el componente Título habilitado para el tipo de objeto*

![Se muestra el diseñador de flujos de trabajo. Se muestra el flujo de trabajo Creación de valor KRI. El panel lateral muestra las condiciones de flujo de trabajo. La lista Campo de objeto muestra Name.ID y Name.Title.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_wf1.png)

El ejemplo siguiente muestra un cálculo con el valor **Visualización de nombre** que indica la visualización del campo Nombre.

*Figura 9. Ejemplo: un cálculo con el componente Título habilitado para el tipo de objeto*

![Se muestra un cálculo. En el panel lateral, la lista Campo de objeto muestra Name.ID y Name.Title.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_calc.png)

El ejemplo siguiente muestra un correo electrónico generado por un flujo de trabajo que utiliza el componente Título del KRI, tal como lo establece el valor **Visualización de nombre** en el objeto KRI.

*Figura 10. Ejemplo: un correo electrónico de notificación que muestra el título de un objeto*

![Se muestra un correo electrónico. El mensaje muestra el título de un KRI, Reclamaciones de cliente.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-systitle_email.png)

#### Migración de usuarios, grupos y roles

Ahora puede exportar los elementos siguientes utilizando **Exportar configuración**:

- Grupos y usuarios
- Plantillas de funciones
- Asignación de funciones

El ejemplo siguiente muestra cómo puede exportar grupos. Al exportar un grupo, la exportación incluye la jerarquía de grupos bajo el grupo, incluidos los subgrupos, los usuarios, las asociaciones de perfiles de usuarios y grupos y los administradores del grupo.

*Figura 11. Selección de grupos para exportar*

![Se muestra la página Seleccionar elementos para exportar. Los elementos disponibles para exportar ahora incluyen Grupos/Usuarios, Asignaciones de roles y Plantillas de roles. En este ejemplo, se seleccionan Grupos/Usuarios y se seleccionan dos grupos para la exportación.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-export_groups.png)

#### Actualizaciones de la interfaz de usuario y temas personalizados (Carbon)

La interfaz de usuario ahora utiliza Carbon 11. Los nombres de los valores de color para temas personalizados ahora son más fáciles de entender.

*Figura 12. Selección de colores para un tema personalizado*

![Se muestra el panel lateral Añadir tema. Se listan los colores disponibles. Los valores de color incluyen button-primary-active y link-primary. En versiones anteriores, los nombres eran menos intuitivos.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg9000-carbon11.png)

La tabla siguiente muestra ejemplos de los cambios de nombre:

| Nombre anterior | Nombre nuevo |
| --- | --- |
| `interactive-01` | `background-brand` |
| `interactive-03` | `button-tertiary` |
| `interactive-04` | Dividir en dos valores: `border-interactive` y `interactive` |
| `text-04` | `text-on-color` |
| `link-01` | `link-primary` |
| `focus` | `focus` |
| `hover-primary` | `button-primary-hover` |
| `active-primary` | `button-primary-active` |
| `hover-primary-text` | `link-primary-hover` |
| `hover-tertiary` | `button-tertiary-hover` |
| `active-tertiary` | `button-tertiary-active` |

Si está actualizando o migrando, no es necesario que actualice los temas personalizados para utilizar estos nuevos valores de color.

Para más información sobre los ajustes de color, consulte [https://carbondesignsystem.com/elements/color/usage/](https://www.ibm.com/links?url=https%3A%2F%2Fcarbondesignsystem.com%2Felements%2Fcolor%2Fusage%2F)

Para obtener más información sobre Carbon, consulte [https://carbondesignsystem.com/all-about-carbon/what-is-carbon/](https://www.ibm.com/links?url=https%3A%2F%2Fcarbondesignsystem.com%2Fall-about-carbon%2Fwhat-is-carbon%2F).

Para obtener información sobre la creación de temas personalizados, consulte [Definición de temas personalizados](3.2-guia-del-administrador.md#definición-de-temas-personalizados).

### Mejoras de la API en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-api-enhancements-in)

IBM OpenPages® 9.0.0 presenta una nueva versión de la API REST de GRC.

La nueva API REST deIBM OpenPages GRC V2 ofrece las siguientes ventajas:

- Se ajusta a las directrices de la API de IBM Cloud . Esto hace que la API sea coherente con otros productos de IBM Cloud .
- Compatible con SCIM.
- Mayor facilidad de uso.

Utilice la versión IBM OpenPages GRC REST API V2 de la API OpenPages para nuevas implementaciones. Para obtener más información sobre la API V2 , consulte [IBM OpenPages GRC V2](9-guia-del-desarrollador.md#ibm-openpages-api-rest-grc-v2)  .

Utilice la versión IBM OpenPages API REST GRC V1 de la API OpenPages para las versiones OpenPages anteriores a 9.0.0. Para obtener más información sobre la API V1 , consulte [IBM OpenPages GRC](9-guia-del-desarrollador.md#ibm-openpages-api-rest-grc-v1)  .

### Nueva guía del desarrollador en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-new-developer-guide-in)

IBM OpenPages® 9.0.0 presenta una nueva Guía del desarrollador.

La  [Guía del desarrollador](9-guia-del-desarrollador.md#guía-del-desarrollador)  reúne toda la documentación y los ejemplos que los desarrolladores necesitan para interactuar mediante programación con IBM OpenPages. La Guía del desarrollador incluye información detallada sobre los temas siguientes:

- Las versiones V1 y V2 de la API REST deIBM OpenPages GRC
- API deIBM OpenPages GRC Java™
- Ejemplos de API
- Activadores

### Software soportado en 9.0.0

`Características nuevas › Características nuevas de la versión 9.0.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=900-supported-software-in)

IBM OpenPages® 9.0.0 incluye cambios en los requisitos de software:

#### Requisitos previos de software

**Tabla 1. Cambios en las versiones de software soportadas**

| Software | Cambios de conformidad |
| --- | --- |
| Servidor Red Hat Enterprise Linux® (RHEL) | 7.x ya no está soportado. |
| Microsoft Windows Server | Ahora se da soporte a Standard Edition 2022. |

Para obtener más información, consulte la página web [Supported Environments](https://www.ibm.com/support/pages/node/713069) .

#### Requisitos de formato de archivo de FastMap

En la versión 9.0, FastMap sólo da soporte a archivos `.xlsx` . El tipo de archivo `.xls` ya no está soportado.

- La plantilla de exportación predeterminada está ahora en formato `.xlsx` . El archivo `.xls` existente no se elimina pero ya no se utiliza.

  Si ha personalizado `DefaultTemplate.xls`, descárguelo, vuelva a guardarlo como un archivo `.xlsx` utilizando Microsoft Excel y, a continuación, cargue el archivo `DefaultTemplate.xlsx` .

  > **Nota:** El nombre de archivo debe ser `DefaultTemplate.xlsx`.
- Si utiliza plantillas de exportación específicas de objeto, actualícelas al formato `.xlsx` . (Descárguelos, vuelva a guardarlos como archivos `.xlsx` utilizando Microsoft Excel y, a continuación, cárguelos.)

  Si una plantilla específica de objeto está en formato `.xls` , se utiliza `DefaultTemplate.xlsx` .
- Los archivos de importación de FastMap deben estar en formato `.xlsx` . Si necesita importar un archivo de un entorno más antiguo, guarde el archivo como `.xlsx`y, a continuación, impórtelo.
- El formato `.xlsx` da soporte a un mayor número de columnas y filas. Para obtener más información, consulte la documentación de Microsoft Excel.

> **Nota:** Se espera que el rendimiento sea más lento con los archivos `.xlsx` debido a las características del tipo de archivo `.xlsx` . Este problema de rendimiento no es específico de OpenPages.

## Características nuevas de la versión 8.3.0.2

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-8302)

Las nuevas características de IBM OpenPages® 8.3.0.2 incluyen las mejoras siguientes.

### Notificaciones de etapa de flujo de trabajo personalizado en 8.3.0.2

`Características nuevas › Características nuevas de la versión 8.3.0.2` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8302-custom-workflow-stage-notifications)

Ahora puede editar y crear plantillas de notificación de correo electrónico en el Diseñador de flujos de trabajo y asignar plantillas a las etapas de flujo de trabajo.

Los usuarios administrativos pueden crear plantillas de notificación de etapa de correo electrónico específicas de una etapa de flujo de trabajo. Ya no está restringido a utilizar una plantilla universal para las notificaciones que se envían a las personas asignadas, a los suscriptores o a los destinatarios de notificaciones de la etapa final.

Para las notificaciones que se envían a los responsables o suscriptores, hay disponible una nueva selección **Personalizar** en el panel **Propiedades de acción** en la sección **Correo electrónico** .

Para las notificaciones enviadas cuando se ha completado un flujo de trabajo, está disponible un nuevo botón **Personalizar plantilla de correo electrónico** en el panel **Propiedades de etapa** en la sección **General** .

*Figura 1. Personalización de notificaciones de correo electrónico para acciones y etapas*

![Se muestran dos imágenes. La primera imagen muestra el panel Propiedades de acción. Las secciones Notificar a los responsables y Notificar a los suscriptores tienen cada una un enlace denominado Personalizar. La segunda imagen muestra el panel de propiedades de etapa. La sección Notificar a otros usuarios tiene un botón denominado Personalizar plantilla de correo electrónico.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-wf_action_props.png)

Cuando pulsa **Personalizar** o el botón **Personalizar plantilla de correo electrónico** , se abre un panel. Inicialmente, muestra las plantillas predeterminadas para las series de texto de aplicación de asunto y cuerpo. Puede seleccionar cualquier plantilla de correo electrónico de asunto en OpenPages en la sección **Asunto** o cualquier plantilla de correo electrónico de cuerpo en OpenPages en la sección **Cuerpo** . Las ediciones que realice en una plantilla en este panel se aplican a todas las etapas de flujo de trabajo asignadas a la plantilla.

*Figura 2. Selección y personalización de plantillas para notificaciones de asignado*

![Se muestra el panel Personalizar notificaciones de asignado. El panel tiene dos secciones: Asunto y Cuerpo. Cada sección tiene dos campos: uno para seleccionar una plantilla y otro para ver o editar el HTML de la plantilla.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-wf_assignee_custn.png)

También puede seleccionar una plantilla y pulsar **Copiar en plantilla nueva**. Con esta opción, especifica un nombre y una descripción para la nueva plantilla, y las series proporcionadas por la plantilla que ha seleccionado se ponen a su disposición para su edición. Se genera automáticamente un nombre para la nueva plantilla. Puede modificarlo según sea necesario.

*Figura 3. Creación de una plantilla copiando de otra plantilla*

![Se muestra el panel Personalizar notificaciones de asignado. Se resalta la plantilla Copiar a nueva. Otra imagen muestra el panel Copiar en plantilla nueva. El ejemplo muestra la copia de la plantilla predeterminada en una nueva plantilla que se utilizará para la etapa Enviar para revisión de un flujo de trabajo de problema.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-wf_template_copy.png)

El texto de la plantilla de correo electrónico se puede previsualizar pulsando **Vista previa**, que muestra cómo se presentará el correo electrónico al destinatario. Si su entorno se integra con Watson Language Translator, también puede traducir las series que se crean o editan en una plantilla. Después de completar las ediciones en la plantilla de correo electrónico y pulsar **Terminado**, la notificación para la acción seleccionada o la notificación de la etapa final se envía al destinatario utilizando la plantilla de correo electrónico seleccionada.

*Figura 4. Vista previa de una notificación*

![El panel Personalizar notificaciones de asignado muestra una vista previa de una notificación de correo electrónico. La vista previa muestra el asunto y el cuerpo del correo electrónico, que incluye enlaces, colores y cadenas de texto de aplicación como [$System Fields: Description$].](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-wf_assignee_custn-2.png)

Cualquier plantilla que se cree o edite dentro del Diseñador de flujos de trabajo se refleja en la pantalla **Texto de aplicación**, a la que se accede desde **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema**. Además, los cambios realizados en una plantilla de correo electrónico desde la pantalla **Texto de aplicación** se reflejan en el Diseñador de flujo de trabajo.

### IBM OpenPages Gestión de riesgos para ESG

`Características nuevas › Características nuevas de la versión 8.3.0.2` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8302-openpages-risk-management-esg)

La nueva solución IBM OpenPages® Risk Management for ESG (ESG) ayuda a las organizaciones a gobernar y gestionar sus programas ESG.

IBM OpenPages Risk Management for ESG da soporte a los siguientes casos de uso:

- Cuestionario para comprender las prioridades de ESG
- Capturar y gobernar objetivos estratégicos
- Enlazar objetivos a procesos, riesgos, controles y proveedores existentes
- Registrar un conjunto de indicadores para ESG
- Almacenar una biblioteca de requisitos normativos y divulgaciones de ESG
- Conformidad de pruebas con requisitos de informes externos
- Exploración de horizonte ESG

#### Perfiles

ESG incluye dos perfiles:

- **Perfil maestro de ESG**

  Contiene los campos y vistas para el uso general de la solución.

- **ESG Mast Profile con Supply Wisdom**

  Contiene los campos y vistas para el uso general de la solución con elementos adicionales para que el usuario pueda ver las clasificaciones ESG en los proveedores tal como proporciona la integración con Supply Wisdom.

  > **Nota:** Para utilizar este perfil, debe tener OpenPages Third Party Risk Management y una suscripción al canal de información de Supply Wisdom .

  La integración de Supply Wisdom se eliminó en 9.1.0.

#### Paneles de control

ESG incluye dos paneles de control:

- **Panel de control maestro de ESG**

  Este panel de control predefinido se alinea con el perfil **OpenPages ESG Master** . El panel de control incluye los paneles siguientes:

  - Mis tareas
  - Favoritos
  - Conformidad con ESG
  - Objetivos estratégicos
  - Informes de ESG
  - Gestión de problemas

  *Figura 1. Panel de control Maestro ESG*

  ![Se muestra el panel de control con tareas ESG, informes y otros datos. El panel de control incluye barras coloridas y gráficos de anillo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_master-dashb.png)

- **Panel de control maestro de ESG Supply Wisdom**

  Este panel de control predefinido se alinea con el perfil **OpenPages ESG Master** . El panel de control incluye los paneles siguientes:

  - Mis tareas
  - Favoritos
  - Conformidad con ESG
  - Objetivos estratégicos
  - Supply Wisdom
  - Informes de ESG
  - Gestión de problemas

  *Figura 2. Panel de control de ESG Supply Wisdom Master*

  ![Este panel es similar al Panel principal de ESG, pero incluye un panel adicional para los datos de Supply Wisdom.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_master-sw-dashb.png)

#### Nuevos tipos de objeto

ESG incluye nuevos tipos de objeto:

- **Objetivo estratégico (objetivo)**

  Este tipo de objeto se utiliza para representar los objetivos ESG de una organización. El tipo de objeto incluye campos para el dominio ESG y los objetivos.

  - Padre: Entidad de negocios
  - Asociaciones hijo: Producto, Evaluación de riesgos, KRI, KPI, Problema, Archivo, Enlace, Firma

- **Producto**

  Este tipo de objeto se utiliza para representar productos.

  - Padre: objetivo estratégico
  - Asociaciones hijo: Evaluación de riesgos, KRI, KPI, Problema, Archivo, Enlace, Firma

- **Declaración de divulgación**

  Este tipo de objeto se utiliza principalmente para registrar comentarios basados en texto en relación con los requisitos de divulgación.

  - Padre: Requisito
  - Asociaciones hijo: Archivo, Problema, Enlace, Firma

#### Plantillas de funciones

ESG incluye dos paneles de control:

- **ESG-Todos los datos-Administración limitada**

  Acceso de lectura, escritura, asociación y supresión para todos los objetos ESG. Los permisos de rol adicionales están limitados a: Archivos, Publicación.

- **ESG-Todos los permisos**

  Acceso de lectura, escritura, asociación y supresión para todos los objetos ESG. Todos los permisos de rol.

#### Flujos de trabajo

ESG incluye flujos de trabajo para los siguientes casos de uso:

- Gestión objetiva
- Aplicabilidad de conformidad ESG
- Evaluación de conformidad de ESG

Los flujos de trabajo para la gestión de objetivos son:

- **Flujo de trabajo de creación de objetivos**

  Cuando se crea un objetivo, este flujo de trabajo permite al usuario rellenar campos clave relacionados con la descripción, la propiedad, la categorización y la priorización del objetivo.

  *Figura 3. Flujo de trabajo de creación de objetivos*

  ![Este flujo de trabajo tiene tres etapas: Inicio, Objetivo de documento y Objetivo final en directo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_obj-cr.png)

- **Flujo de trabajo de actualización de objetivo**

  Este flujo de trabajo se utiliza para actualizar un objetivo o marcarlo como Completo.

  *Figura 4. Flujo de trabajo de actualización de objetivo*

  ![Este flujo de trabajo tiene cuatro etapas: Inicio, Progreso de actualización, Objetivo de finalización completado y Objetivo de finalización en curso.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_obj-upd.png)

Los flujos de trabajo para la aplicabilidad de conformidad son:

- **Aplicabilidad ESG-Flujo de trabajo de mandato**

  Este flujo de trabajo crea evaluaciones de aplicabilidad. No es necesaria ninguna acción de usuario. Este flujo de trabajo inicia el flujo de trabajo «“Aplicabilidad de ESG- SubMandate”» para todos los SubMandatesasociados.

  *Figura 5. Aplicabilidad ESG-Flujo de trabajo de mandato*

  ![Este flujo de trabajo tiene dos etapas: Inicio y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_app-m.png)

- **Aplicabilidad ESG-Flujo de trabajo SubMandate**

  Este flujo de trabajo se inicia desde el mandato padre. El flujo de trabajo solicita al propietario del mandato que evalúe la aplicabilidad de ESG en cada SubMandate. Tras el envío, el flujo de trabajo inicia el flujo de trabajo «“Aplicabilidad ESG-Requisito”» para los requisitos asociados.

  *Figura 6. Aplicabilidad ESG-Flujo de trabajo SubMandate*

  ![Este flujo de trabajo tiene tres etapas: Iniciar, Determinar aplicabilidad y Finalizar.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_app-subm.png)

- **Aplicabilidad ESG-Requisito**

  Este flujo de trabajo permite al propietario del mandato registrar si el requisito es aplicable y notificable para ESG. El usuario también registra el tipo de evaluación para el requisito: medido (uso de KRI) o declaración de divulgación.

  *Figura 7. Aplicabilidad ESG-Flujo de trabajo de requisito*

  ![Este flujo de trabajo tiene tres etapas: Iniciar, Determinar aplicabilidad y Finalizar.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_app-req.png)

Los flujos de trabajo para la evaluación de conformidad son:

- **Evaluación de conformidad de ESG-Iniciar flujo de trabajo**

  Este flujo de trabajo no tiene tareas de usuario. El flujo de trabajo inicia el flujo de trabajo «“Evaluación del cumplimiento de ESG - Requisito”» para todos los requisitos descendientes (Mandato, SubMandate, y Requisito) que estén marcados como Aplicables para ESG.

  *Figura 8. Evaluación de conformidad de ESG-Iniciar flujo de trabajo*

  ![Este flujo de trabajo tiene dos etapas: Inicio y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_ca-launch.png)

- **Evaluación de conformidad de ESG-Flujo de trabajo de requisito**

  Este flujo de trabajo es un flujo de trabajo de evaluación y aprobación de dos etapas para los requisitos que son aplicables para ESG.

  *Figura 9. Evaluación de conformidad de ESG-Flujo de trabajo de requisito*

  ![Este flujo de trabajo tiene cinco etapas: Inicio, Evaluación-Declaración de divulgación, Evaluación-Medida, Revisión de evaluación y Evaluación y Revisión completadas.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_ca-req.png)

- **Flujo de trabajo Declaración de divulgación y revisión**

  Se trata de un flujo de trabajo de evaluación y aprobación de dos etapas para las declaraciones de divulgación.

  *Figura 10. Flujo de trabajo Declaración de divulgación y revisión*

  ![Este flujo de trabajo tiene cinco etapas: Inicio, Declaración de divulgación completa, Revisión de divulgación, Finalización de intención cumplida y Finalización de intención no cumplida.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_wf-ds.png)

#### Cálculos

ESG incluye dos cálculos:

- **Puntuación de prioridad de objetivo**

  Calcula una puntuación de prioridad objetivo.

  Obtiene los valores de los campos `Importance to Firm` y `Importance to Stakeholders` : Muy bajo = «“1”» , Bajo = «“2”», Medio = «“3”», Alto = «“4”», Muy alto = «“5”». A continuación, se añaden los dos valores para obtener la puntuación de prioridad de objetivo, que puede oscilar entre 2 y 10.

- **Progreso objetivo**

  Calcula la diferencia entre el Progreso del objetivo y el Objetivo objetivo. A continuación, el cálculo establece el campo Estado de progreso en **Bajo logro**, **Sobre logro**o **En destino**.

#### Vistas

ESG incluye un conjunto de vistas:

- Vistas para los nuevos tipos de objeto
- Vistas adicionales para Requisito, Evaluación de riesgo y SubMandate
- Actualizadas las vistas del sistema para Entidad de Negocio, Indicador de Riesgo Clave, Mandato, SubMandate, y Requisito

#### Informes

La solución ESG incluye los informes siguientes:

- **Panel de control de objetivos**

  Este informe es un panel de control interactivo de varias pestañas Cognos Analytics que permite a una organización revisar el estado actual de los objetivos, la priorización y el progreso frente al objetivo.

  Este informe incluye enlaces de acceso a detalles al informe de acceso a detalles del panel de control Objetivo.

  *Figura 11. Panel de control de objetivos*

  ![El panel de instrumentos colorido muestra un gráfico de anillo de objetivos por estado, un gráfico de barras de objetivos por dominio y un gráfico de barras de objetivos por estado de progreso.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_obj-dashb.png)

  *Figura 12. Panel de instrumentos Objetivo-Pestaña Priorización*

  ![La pestaña Priorización muestra un diagrama de dispersión de objetivos estratégicos por Importancia a Firma e Importancia a partes interesadas. La pestaña también muestra una tabla de objetivos con detalles y puntuaciones de prioridad.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_obj-dashb-pr.png)

  *Figura 13. Panel de instrumentos Objetivo-Pestaña Progreso frente a Destino*

  ![La pestaña Progreso frente a objetivo muestra un gráfico de barras grande con el porcentaje alcanzado en el eje y y los objetivos en el eje x. Las barras están codificadas por colores por dominio ESG.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_obj-dashb-prog.png)

- **Listado de objetivos**

  Este informe de lista muestra una tabla de objetivos, que se filtran por entidad, estado de objetivo y estado de progreso. Este informe incluye enlaces de seguimiento cruzado a la vista Tarea para cada objetivo.

- **Acceso a los detalles del panel de control de objetivos**

  Este informe de lista muestra una tabla de objetivos. Se accede a este informe como un acceso a los detalles desde el panel **Objetivo por estado** en el **Panel de control Objetivo de ESG**.

  *Figura 14. Panel de instrumentos Objetivo-Informe de acceso a detalles*

  ![El informe muestra una tabla con detalles sobre los objetivos de ESG para una entidad de negocios.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_obj-dashb-dt.png)

- **Panel de control KRI de objetivo**

  Este informe se filtra por objetivo y muestra una descripción y un gráfico de tendencias para todos los indicadores clave de riesgo asociados.

  *Figura 15. Panel de control KRI de objetivo*

  ![El informe muestra los KRI. Para cada KRI, el informe muestra su descripción y un gráfico de tendencias.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_kri-dashb.png)

- **Panel de control de conformidad de ESG**

  Este informe es un panel de control interactivo de varias pestañas Cognos Analytics que permite a una organización ver su estado de conformidad ESG. El informe incluye enlaces de acceso a detalles al informe de acceso a detalles Conformidad por mandato.

  *Figura 16. Panel de control de conformidad de ESG*

  ![El panel de control de colores muestra un gráfico de barras apiladas. Un panel de filtro le permite filtrar el gráfico por un estándar o infraestructura de conformidad.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_comp-dashb.png)

  *Figura 17. Panel de control de conformidad de ESG-Conformidad por SubMandate*

  ![La pestaña del panel de control muestra un mapa de calor de evaluaciones de requisitos por submandato. Un panel de filtro le permite filtrar el gráfico por un mandato.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_comp-dashb-sm.png)

  *Figura 18. Panel de control de conformidad de ESG-Progreso de evaluación*

  ![La pestaña del panel de control muestra dos gráficos de barras apiladas: progreso de evaluación por infraestructura y tipo de evaluación por infraestructura.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_comp-dashb-prog.png)

- **Conformidad por acceso a detalles de mandato**

  A este informe de lista se accede como un informe de acceso a detalles desde el **Panel de control de conformidad de ESG**.

  *Figura 19. Informe de acceso a detalles de conformidad por mandato*

  ![El informe muestra una tabla de declaraciones de divulgación para un mandato.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_comp-mand-dt.png)

- **Detalles de cumplimiento normativo y estándar de ESG**

  Este informe muestra detalles sobre submandatos y requisitos para un mandato seleccionado.

- **Lista de proveedores-Clasificaciones ESG**

  Este informe de lista detallado muestra las valoraciones de ESG para los proveedores seleccionados, filtradas por nombre de proveedor.

  Este informe se basa en los datos que se proporcionan a través de una integración con el canal de información del proveedor de Supply Wisdom .

- **Obtención de detalles de proveedor de ESG**

  Se trata de un informe de acceso a los detalles al que se accede desde el informe Listado de proveedores. El informe muestra datos clave de valoración de Supply Wisdom ESG e incluye enlaces de seguimiento cruzado con el proveedor.

  Este informe se basa en los datos que se proporcionan a través de una integración con el canal de información del proveedor de Supply Wisdom .

- **Comparación de proveedores-ESG**

  Este informe muestra las valoraciones de ESG de Supply Wisdom para dos proveedores. El informe incluye un filtro para seleccionar los proveedores para la comparación.

  Este informe se basa en los datos que se proporcionan a través de una integración con el canal de información del proveedor de Supply Wisdom .

  *Figura 20. Comparación de proveedores-Informe ESG*

  ![El informe muestra dos gráficos de barras, uno para cada proveedor. Cada gráfico de barras muestra la valoración actual en el eje y y el nombre de riesgo de sabiduría de suministro en el eje x.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_vendor-comp.png)

- **Postura de proveedor-Calificaciones de ESG**

  Este informe se filtra por proveedor y muestra los riesgos de Supply Wisdom ESG asociados del proveedor en varios formatos (Radar, Cross Tab y Trend Line chart).

  Este informe se basa en los datos que se proporcionan a través de una integración con el canal de información del proveedor de Supply Wisdom .

  *Figura 21. Postura del proveedor-Informe de valoraciones de ESG*

  ![El informe muestra las calificaciones de riesgo de Sabiduría de suministro en una tabla y en varios gráficos.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-esg_vendor-post.png)

### Mejoras en la integración de modelos de IA en 8.3.0.2

`Características nuevas › Características nuevas de la versión 8.3.0.2` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8302-enhancements-ai-model-integration)

Versión 8.3.0.2 incluye los siguientes cambios y mejoras en la integración de modelos de IA:

- La integración de Watson Machine Learning tiene un nuevo nombre: Integración de modelo de Machine Learning personalizada.
- La integración de modelos de Machine Learning personalizada ahora da soporte a la conexión con Natural Language Understanding en IBM® Cloud para modelos de clasificación personalizados.

### Mejoras en IBM OpenPages Regulatory Compliance Management en 8.3.0.2

`Características nuevas › Características nuevas de la versión 8.3.0.2` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8302-enhancements-rcm)

IBM OpenPages® Regulatory Compliance Management (RCM) incluye mejoras que continúan basándose en la estrategia y la dirección que se introdujo en 8.3.0.1.

#### Mejoras en el conector de Ascent

La integración de Ascent se ha mejorado con la ingestión de versiones de requisitos. El objeto Versión de requisito detalla las versiones anteriores y futuras del texto regulador de requisito. La versión de requisito es un hijo de requisito. El objeto Versión de requisito realizará un seguimiento de los cambios normativos a lo largo del tiempo. Las versiones anteriores pueden ayudarle a revisar un requisito en un momento determinado. Las versiones futuras permiten al usuario prepararse para el futuro cambio de texto normativo y comenzar su análisis de impacto.

*Figura 1. Vista de tarea de requisito RCM con la cuadrícula de relación de versión de requisito*

Se visualiza una vista de tarea para el objeto Requisito. En la versión de requisito de la vista, una cuadrícula muestra las versiones relacionadas del texto regulador.

![Se visualiza una vista de tarea para el objeto Requisito. En la versión de requisito de la vista, una cuadrícula muestra las versiones relacionadas del texto regulador.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8302-rcm_ascent.png)

**Nuevo objeto**

Se ha añadido el siguiente tipo de objeto al modelo de objeto: Versión de requisito.

**Nuevas vistas**

Las vistas siguientes se han editado o añadido para dar soporte a la integración de Ascent :

- SysView-Task-Requirement-Ascent
- SysView-Task-Requirement Version-Ascent
- SysView-Admin-Requirement Version-Ascent

## Características nuevas de la versión 8.3.0.1

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-8301)

Las nuevas características de IBM OpenPages® 8.3.0.1 incluyen las mejoras siguientes.

### Integración de modelos de IA

`Características nuevas › Características nuevas de la versión 8.3.0.1` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8301-integration-ai-models)

Ahora puede crear o incorporar cualquier tipo de modelo de IA y utilizar la información de modelo directamente en vistas y flujos de trabajo de OpenPages® .

Puede utilizar modelos de IA creados con AutoAI en Watson Studio o desarrollados por un equipo de ciencia de datos y, a continuación, desplegados en Watson Machine Learning en IBM® Cloud. A continuación, la integración de OpenPages puede enviar datos a los modelos para captar predicciones en directo.

### Mejoras en IBM OpenPages Regulatory Compliance Management

`Características nuevas › Características nuevas de la versión 8.3.0.1` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8301-enhancements-rcm-in)

IBM OpenPages® Regulatory Compliance Management (RCM) incluye numerosas mejoras que continúan basándose en la estrategia y la dirección que se introdujo en 8.3.0.1.

#### Mejoras en el conector de Ascent

La integración de Ascent se ha mejorado con la ingestión de información de soporte como hijo de requisito. Información de soporte es un texto normativo que no alcanza el nivel de un requisito legal, pero proporciona orientación adicional, detalles, etc. para ayudar a las entidades a comprender los requisitos y el impacto del reglamento.

*Figura 1. Vista de tarea de requisito de RCM con la cuadrícula de relación de información de soporte*

![Se visualiza una vista de tarea para el objeto Requisito. En la sección Información de soporte de la vista, una cuadrícula muestra las citas relacionadas.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8301-rcm_ascent.png)

**Nuevo objeto**

Se ha añadido el siguiente tipo de objeto al modelo de objeto: Ascent Información de soporte.

**Nuevas vistas**

Se han añadido las vistas siguientes para dar soporte a la integración de Ascent :

- SysView-Task-Supporting Information-Ascent
- SysView-Admin-Supporting Information-Ascent
- SysView-Grid-Supporting Information-Ascent

### Mejoras de la gestión de riesgos de terceros en 8.3.0.1

`Características nuevas › Características nuevas de la versión 8.3.0.1` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8301-enhancements-tprm-in)

Versión 8.3.0.1 incluye mejoras para OpenPages® Third Party Risk Management (TPRM).

#### RapidRatings

OpenPages Gestión de riesgos de terceros ahora incluye un conector para RapidRatings.

El conector RapidRatings le permite importar detalles de proveedor y evaluaciones financieras de RapidRatings a objetos de proveedor en OpenPages. A continuación, puede ver las evaluaciones en OpenPages.

Al igual que otras integraciones, se necesita una licencia independiente con RapidRatings para integrarse en su plataforma, y el grupo de campos, el trabajo y las vistas se pueden obtener como un paso posterior a la instalación.

Para obtener información sobre cómo configurar el conector RapidRatings , consulte la publicación  [*IBM OpenPages Guía del administrador*](3.6-guia-del-administrador.md#conector-de-rapidratings-para-ibm-openpages-third-party-risk-management) .

*Figura 1. Panel de control de TPRM con RapidRatings*

![Panel de instrumentos que muestra los nuevos paneles para RapidRatings. Por ejemplo, uno de los paneles muestra un gráfico de anillo colorido que muestra los riesgos por categoría RapidRatings .](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8301-tprm_rapidr_db.png)

*Figura 2. Detalles de proveedor de TPRM con datos de RapidRatings*

![Vista de tareas de un proveedor. La vista incluye datos de RapidRatings.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8301-tprm_rapidr_view.png)

**Trabajo de Planificador**

Los administradores configuran y planifican el canal de información de RapidRatings utilizando el nuevo trabajo administrativo de RapidRatings en el Planificador.

**Nuevo perfil**

Se ha añadido el perfil siguiente: OpenPages RapidRatings Master

**Nuevas plantillas de rol**

Se han añadido las siguientes plantillas de funciones:

- TPRM Rapid Ratings - All Permissions
- TPRM Rapid Ratings - All Data - Limited Admin

**Nuevo tipo de objeto**

Se ha añadido el siguiente tipo de objeto al modelo de objeto: RapidRatings Ratings.

**Nuevos grupos de campos**

Se han añadido los siguientes grupos de campos al objeto Proveedor:

- OPSS-RRCompany
- OPSS-RRRatingDataPoints

*Figura 3. Ejemplo de campos rellenados a partir de datos proporcionados por la integración de RapidRatings*

![Se muestra una vista de tarea. Muestra las calificaciones financieras y otros datos proporcionados por la integración de RapidRatings .](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8301-tprm_rapidr_field.png)

**Nuevas vistas**

Se han añadido las vistas siguientes para dar soporte a la integración de RapidRatings :

- SysView-Task-Vendor-RapidRatings
- SysView-Grid- Vendor-RapidRatings
- SysView-Admin- Vendor-RapidRatings
- SysView-Task-RRRating-RapidRatings
- SysView-Grid-RRRating-RapidRatings
- SysView-Admin-RRRating-RapidRatings

#### RiskRecon

OpenPages Gestión de riesgos de terceros ahora incluye un conector para RiskRecon.

El conector RiskRecon le permite importar detalles de proveedor y valoraciones de RiskRecon a objetos de proveedor en OpenPages. A continuación, puede ver las evaluaciones en OpenPages.

Al igual que otras integraciones, se necesita una licencia independiente con RiskRecon para integrarse en su plataforma, y el grupo de campos, el trabajo y las vistas se pueden obtener como un paso posterior a la instalación.

Para obtener información sobre cómo configurar el conector RiskRecon , consulte la publicación  [*IBM OpenPages Guía del administrador*](3.6-guia-del-administrador.md#conector-de-riskrecon-para-ibm-openpages-third-party-risk-management) .

*Figura 4. Panel de control de TPRM con RiskRecon*

![Panel de instrumentos que muestra los nuevos paneles para RiskRecon](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8301-tprm_riskrecon_db.png)

*Figura 5. Detalles de proveedor de TPRM con datos de RiskRecon*

![Vista de tareas de un proveedor. La vista incluye datos de RiskRecon.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8301-tprm_riskrecon_view.png)

**Trabajo de Planificador**

Los administradores configuran y planifican el canal de información de RiskRecon utilizando el nuevo trabajo administrativo de RiskRecon en el Planificador.

**Nuevo perfil**

Se ha añadido el perfil siguiente: VRM RiskRecon Master.

**Nuevo tipo de objeto**

Se ha añadido el siguiente tipo de objeto al modelo de objeto: RiskRecon Ratings.

**Nuevo grupo de campos**

Se ha añadido el siguiente grupo de campos al objeto Riesgo: OPSS-RiskRecon-Domain-Ratings.

*Figura 6. Ejemplo de campos rellenados a partir de datos proporcionados por la integración de RiskRecon*

![Se muestra una vista de tarea. Muestra las evaluaciones de seguridad de la aplicación proporcionadas por la integración de RiskRecon .](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8301-tprm_riskrecon_field.png)

**Nuevas vistas**

Se han añadido las vistas siguientes para dar soporte a la integración de RiskRecon :

- SysView-Grid- Vendor-RiskRecon
- SysView-Task-Vendor-RiskRecon
- SysView-Admin- Vendor-RiskRecon
- SysView-Grid-RiskRecon
- SysView-Task-RiskRecon
- SysView-Admin-RiskRecon

### Cuestionarios

`Características nuevas › Características nuevas de la versión 8.3.0.1` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8301-questionnaires)

Las mejoras en la funcionalidad de cuestionario se incluyen en esta versión de IBM OpenPages®.

#### Copiar respuestas, comentarios y archivos adjuntos de una evaluación anterior

Los encuestados pueden elegir copiar respuestas, comentarios y archivos adjuntos de una evaluación de cuestionario existente para ahorrar tiempo. Por ejemplo, es posible que un encuestado desee copiar respuestas si recibe un cuestionario anual y algunas de sus respuestas del año pasado siguen siendo las mismas. OpenPages utiliza un ID interno para hacer coincidir las preguntas de la evaluación del año pasado con las preguntas del cuestionario que está completando. Al hacer coincidir los ID, OpenPages garantiza que las respuestas, los comentarios y los archivos adjuntos se copien en las mismas preguntas o en preguntas similares. Cada vez que el encuestado copia las respuestas de otra evaluación de cuestionario, se añade un comentario a cada pregunta con una respuesta copiada. Como se muestra en la Figura 2, el comentario incluye cuando se copió una respuesta y el nombre de la evaluación del cuestionario del que se copió.

Los encuestados pueden sustituir las respuestas existentes. Si el recuadro de selección **Sustituir respuestas existentes** está seleccionado, la funcionalidad de copia de respuesta sustituye las respuestas del cuestionario actual por las respuestas copiadas.

*Figura 1. Recuadro de diálogo **Copiar respuestas***

![El cuadro de diálogo Copiar respuestas donde los encuestados pueden copiar respuestas, comentarios y archivos adjuntos de un cuestionario anterior.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/copy_answers_dialog.png)

*Figura 2. Se ha copiado un **Evaluación de cuestionario** que muestra el comentario que muestra una respuesta*

![Una evaluación de cuestionario que muestra el comentario que muestra una respuesta se ha copiado de otra evaluación.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/copied_answers_assessment.png)

#### Crear un objeto basado en puntuaciones en una evaluación de cuestionario

En IBM OpenPages 8.3, una nueva acción personalizada en el flujo de trabajo de evaluación de cuestionario le permite crear un problema cuando la puntuación de la respuesta a una pregunta no cumple un umbral establecido. Ahora se puede utilizar una nueva propiedad en la acción personalizada para crear cualquier tipo de objeto siempre que el tipo de objeto sea un hijo del tipo de activo.

Por ejemplo, el cuestionario contiene la pregunta **¿Tiene su organización un proceso para restringir el procesamiento de Datos Personales en sus sistemas?**. Desea generar un riesgo cuando el encuestado selecciona **No** como respuesta. A la respuesta **No** se le asigna una puntuación de **1**.

1. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Flujos de trabajo**.
2. Pulse **Flujo de trabajo de evaluación de cuestionario**.
3. Seleccione una acción entre dos etapas. Por ejemplo, para una evaluación de cuestionario de dos etapas, puede seleccionar la acción **Enviar y cerrar** entre la etapa **Recopilación de información** y la etapa **Cerrado**.

   Aparece el panel **Propiedades de acción**.
4. Expanda la sección **Validaciones y operaciones**.
5. Haga clic en **Nueva operación**.
6. En el campo **Operación**, seleccione **Acción personalizada**.
7. Especifique un nombre en **Nombre**.
8. En el campo **Nombre de clase**, escriba **com.ibm.openpages.api.service.local.workflow.actions.QuestionnaireScoreAssessmentAction**.
9. Pulse **Añadir propiedad**.
10. Especifique el **Nombre** de la propiedad, **umbral**, y un **Valor** de **5**.
11. En el panel **Propiedades**, pulse **Hecho**.
12. Pulse **Añadir propiedad**.
13. Introduzca el **Nombre** de la propiedad, **Tipo de objeto**, y un **Valor** de **RiesgoSOX**.

    El valor de esta propiedad debe ser el nombre del sistema y no la etiqueta del tipo de objeto. Por ejemplo, el valor especificado en el ejemplo es **RiesgoSOX** y no **Riesgo**.
14. En el panel **Propiedades**, pulse **Hecho**.

    El panel **Operaciones** muestra ambas propiedades.

    ![Se muestra el panel de operaciones. La sección Propiedades muestra las dos propiedades: umbral y tipo de objeto.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/operations_dialog.png)
15. En el panel **Operaciones** , pulse **Hecho** y pulse **Publicar**.

Con el umbral establecido en **5** y **objectType** establecido en **SOXRisk**, se genera un riesgo cuando una puntuación para cualquier respuesta es menor que 5. El texto de la pregunta, el ID del encuestado y la respuesta a la pregunta aparecen en la descripción del riesgo.

### Etiquetas

`Características nuevas › Características nuevas de la versión 8.3.0.1` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8301-tags)

Ahora los usuarios pueden aplicar etiquetas a objetos en IBM OpenPages® para categorizar los objetos y realizar búsquedas basadas en dichas categorías. Los usuarios pueden buscar etiquetas en cualquier cuadrícula que no sea una cuadrícula de relaciones en una pestaña **Tarea** o **Admin** .

#### Ejemplo

En el ejemplo siguiente, las etiquetas **Modelo** y **Gestión de cambios** se utilizan para categorizar un control, un problema y un objeto de proveedor relacionados con modelos y cambios en dichos modelos.

- Un control tiene las etiquetas **Modelo** y **Gestión de cambios** porque el control hace referencia a las actividades necesarias cuando se actualiza un modelo.
- Un problema tiene las etiquetas **Modelo** y **Gestión de cambios** porque el problema se ha generado debido a la desviación del modelo después de actualizar el modelo. El problema también tiene la etiqueta **Prueba** para indicar que se necesitan pruebas en el modelo.
- Un proveedor tiene las etiquetas **Modelo** y **Gestión de cambios** porque el proveedor es responsable de desarrollar, probar y desplegar modelos en producción. El proveedor también tiene la etiqueta **Desarrollo** para mostrar que está implicado en el desarrollo de modelos.

#### Qué pueden hacer los administradores y los usuarios con las etiquetas

Los administradores con el permiso de administración de etiquetado pueden realizar las tareas siguientes:

- Habilite o inhabilite la característica de etiquetado.
- Cree nuevas etiquetas.
- Actualizar etiquetas existentes.
- Habilitar o inhabilitar etiquetas individuales.

*Figura 1. La pestaña **Etiquetas** donde el administrador trabaja con etiquetas*

![La pestaña Etiquetas donde el administrador trabaja con etiquetas](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/managing_tags.png)

Después de que el administrador habilite el etiquetado, los usuarios pueden realizar las tareas siguientes:

- Asignar y eliminar etiquetas predefinidas en objetos desbloqueados a los que el usuario tiene acceso de escritura.
- Asignar etiquetas de forma masiva desde la página de cuadrícula principal en objetos desbloqueados a los que el usuario tiene acceso de escritura.
- Busque etiquetas en la cuadrícula principal para cada tipo de objeto.
- Buscar etiquetas para buscar objetos para asociar al añadir una relación a un objeto.

*Figura 2. Aplicación de etiquetas a un riesgo*

![Aplicación de etiquetas a un riesgo en la vista de tarea](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/selecting_tags_in_task_view.png)

*Figura 3. Visualización de etiquetas en riesgos en la vista de cuadrícula*

![Visualización de etiquetas en riesgos en la vista de cuadrícula](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/viewing_tags_in_grid.png)

*Figura 4. Búsqueda de etiquetas para asociar objetos relacionados*

![Búsqueda de etiquetas para asociar objetos relacionados](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/assoc_search_on_tags.png)

#### Gestión de etiquetas a través de la API

Ahora hay disponible un nuevo punto final de API REST para añadir y eliminar etiquetas de un objeto.

### Gráficos de tendencias basados en el historial de cambios de los valores de campo

`Características nuevas › Características nuevas de la versión 8.3.0.1` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=8301-trend-charts-based-change-history-field-values)

Ahora puede añadir un gráfico de tendencias con campos a una vista de tarea o de administración para que un objeto muestre los valores históricos de los campos numéricos.

Un gráfico de tendencias puede ser especialmente valioso para los campos que se actualizan automáticamente. La lista siguiente incluye ejemplos de campos que es posible que desee ver en un gráfico de tendencias.

- Campos calculados, como por ejemplo una suma de pérdidas para las vistas de tarea Entidad de negocios.
- Campos actualizados a través de la integración con sistemas de terceros a través de la API

*Figura 1. Un ejemplo de un gráfico de tendencias basado en el historial de cambios de los valores de campo*

![Un ejemplo de un gráfico de tendencias basado en el historial de cambios de los valores de campo](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/trend_chart_for_field_values.png)

## Nuevas características en la versión 8.3.0

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-new-in-version-830)

Las nuevas características de IBM OpenPages® 8.3.0 incluyen las mejoras siguientes.

### Mejoras de la plataforma en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-platform-enhancements-in)

Las mejoras en la funcionalidad se incluyen en esta versión de IBM OpenPages®.

#### Cuestionarios

El nuevo diseño del cuestionario proporciona más funcionalidad y mejora la facilidad de uso.

- Valores de formato de cuestionario

  Los autores de cuestionarios ahora pueden establecer propiedades para mostrar u ocultar las características de la interfaz de usuario cuando crean una plantilla de cuestionario.

  Un autor puede establecer las siguientes propiedades del cuestionario:

  - **Títulos** determina si los títulos aparecen para cada pregunta en el cuestionario.
  - **Numeración automática** determina si las preguntas están numeradas.
  - **Numeración automática** determina si el peso y la puntuación aparecen para preguntas, secciones y subsecciones.

  Estos valores se pueden modificar en el editor de plantillas de cuestionario pulsando **Valores de formato** en el panel de navegación.

  *Figura 1. El cuadro de diálogo **Valores de formato***

  ![El recuadro de diálogo Valores de formato donde los autores pueden establecer las propiedades del cuestionario.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_8.3_qr1.png)
- Página de destino con logotipo

  La nueva página de destino del cuestionario proporciona información introductoria al usuario, como el título, la descripción, la fecha de vencimiento, el progreso, las personas asignadas y la exención de responsabilidad. Un autor puede añadir un logotipo personalizado y un texto de exención de responsabilidad para que aparezcan en todos los cuestionarios.

  *Figura 2. Una página de destino de un cuestionario*

  ![Una página de destino que muestra información introductoria que incluye un logotipo personalizado y una exención de responsabilidad](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_8.3_qr3.svg)
- Los autores del cuestionario pueden designar las preguntas que deseen.

  Los encuestados no podrán presentar el cuestionario si no responden a alguna de las preguntas requeridas.
- Los administradores pueden configurar el flujo de trabajo de la evaluación del cuestionario para crear un problema cuando la puntuación de la respuesta a una pregunta no alcanza un umbral establecido.

  Los administradores pueden añadir una acción personalizada al flujo de trabajo de evaluación del cuestionario utilizando un **Nombre de clase** de **com.ibm.openpages.api.service.local.workflow.actions.QuestionnaireScoreAssessmentAction** para crear un problema para cada pregunta que tenga una puntuación inferior al umbral. El problema está asociado con el padre primario de la evaluación del cuestionario. La propiedad de umbral establece el umbral de puntuación. El valor predeterminado de la propiedad de umbral es **5**.
- Los autores de cuestionario pueden correlacionar objetos padre con preguntas específicas.

  Los autores pueden correlacionar los controles padre o los requisitos con una pregunta. Cuando un autor correlaciona un control o requisito padre con un objeto de pregunta, el padre se muestra con la pregunta en el cuestionario.

#### Mejoras en la interfaz de usuario

La interfaz de usuario incluye numerosas funciones y características nuevas.

- Gráfico de tendencias

  Un nuevo gráfico está disponible para su inclusión en las vistas de tareas para mostrar las tendencias de los valores numéricos de los objetos hijo a lo largo del tiempo. El gráfico siguiente se proporciona en la vista de tareas de KRI y muestra el campo **Valor** de los objetos de valor KRI hijo en azul, los valores del **umbral rojo** y los valores del **umbral amarillo**.

  *Figura 3. Gráfico de tendencias de KRI*

  ![Un ejemplo de gráfico de tendencias](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_8.3_trend_chart.png)
- Vista administrativa

  La gestión administrativa de los registros ahora es más fácil con la creación de la vista administrativa, que muestra todos los campos y asociaciones disponibles en el perfil del usuario independientemente de la vista de tareas determinada que esté habilitada para un registro. Un usuario al que se le ha concedido permiso para acceder a la vista de administración con un nuevo permiso de plantilla de rol puede acceder a la nueva vista desde cualquier vista de tarea.

  *Figura 4. Una pestaña **Tarea** para un objeto de riesgo*

  ![Un ejemplo de una pestaña Tarea](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_8.3_task_tab.png)

  Cuando un usuario pulsa la pestaña Admin, puede ver todos los campos disponibles para el objeto que están disponibles en el perfil del usuario.

  *Figura 5. Una pestaña Admin para un objeto de riesgo*

  ![Un ejemplo de una pestaña Admin](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_8.3_admin_tab.png)

  La pestaña Admin puede mostrar todos los padres e hijos del registro.

  *Figura 6. Una pestaña Admin que muestra los padres y los hijos de un objeto de riesgo*

  ![Un ejemplo de una pestaña Admin que muestra padres e hijos](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg_8.3_parents_and_children.png)

  Las vistas administrativas se crean utilizando el Diseñador de vistas. El orden de los campos que se asigna en el Diseñador de vistas establece el orden de los campos para la importación de FastMap. Una selección de solo lectura para un campo en la vista administrativa impide una importación de FastMap de dicho campo. Los clientes de actualización pueden importar las vistas de detalles de su versión anterior de OpenPages como vistas administrativas.
- Migración de características anteriormente disponibles solo dentro de la interfaz de usuario estándar

  La versión 8.3 es la primera versión local y SaaS que presenta la interfaz de usuario centrada en las tareas sin la opción de cambiar a la interfaz de usuario estándar existente anteriormente. Como parte de este esfuerzo, las siguientes características disponibles anteriormente solo dentro de la interfaz de usuario estándar, ahora están disponibles en la interfaz de usuario centrada en la tarea:

  - Publicación de informes de Cognos en OpenPages desde la pantalla **Páginas y plantillas**
  - Pantalla de configuración de búsqueda global
  - Nivel de objeto recursivo y selección de exclusión de campo en tipos de objeto
  - Visualización de procesos de fondo
  - Restringir el número de asociaciones padre a una única selección padre para objetos hijo en la pantalla **Tipos de objeto** utilizando el valor **Máx. monoparental**

#### Integración de WalkMe

Ahora puede realizar la integración con una herramienta de terceros denominada WalkMe para desplegar contenido personalizado y experiencias de "iniciación" con IBM OpenPages. A través de visitas guiadas, descripciones de las características y recursos incluidos, WalkMe ayuda a los usuarios a sacar el máximo partido a su implementación de OpenPages. Los valores de registro ahora están incluidos para que pueda habilitar WalkMe y conectarse a sus propios fragmentos de código de JavaScript WalkMe.

Para las implementaciones personalizadas, debe tener una licencia separada para WalkMe.

Para ver los valores del registro para Walkme, realice los pasos siguientes:

1. Haga clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Ajustes** y establezca **Aplicaciones** > **Común** > **Configuración** > **Mostrar ajustes ocultos** en **verdadero** para mostrar la configuración oculta.
2. Vaya a **Aplicaciones** > **Walkme**.

*Figura 7. Los valores de la aplicación Walwalme*

![Valores de aplicación de Walme](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/walkme_settings.png)

- **Walkme habilitado**

  Para habilitar Walkme, establezca **Aplicaciones** > **Walkme** > **Walkme habilitado** en **verdadero**.
- **Origen de Walkme**

  De forma predeterminada, **Origen de Walkme** se establece en el URL del almacenamiento en la nube de IBM. Si desea utilizar su propia implementación de WalkMe, actualice este URL al fragmento de código JS.
- **URL de Walkme**

  De forma predeterminada, el valor **URL de Walkme** apunta a una ubicación donde se almacenan las plantillas de Carbon UI y el contenido de OpenPages WalkMe .

  El valor del valor **URL de Walkme** lista los dominios para permitir la seguridad de contenido. Se deben configurar los cortafuegos para permitir estos dominios.

  Si desea utilizar su propia implementación de WalkMe, actualice los URL para que coincidan con su implementación.

### Mejoras de soluciones en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-solutions-enhancements-in)

Las soluciones de IBM OpenPages® se han mejorado para hacerlas más completas y fáciles de utilizar.

#### Mejoras en la gestión de continuidad de negocio en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0 › Mejoras de soluciones en 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-business-continuity-management-enhancements-in)

Versión 8.3 incluye varias mejoras en IBM OpenPages® Business Continuity Management (BCM).

Con la nueva versión de BCM, puede evaluar y supervisar los servicios empresariales para la resiliencia operativa. La solución también proporciona nuevos cálculos para establecer objetivos de tiempo de recuperación (RTO) y objetivos de punto de recuperación (RPO) para procesos empresariales utilizando un enfoque basado en el tiempo y compara los RTO de proceso y los RPO con las dependencias correlacionadas.

Otros cambios incluyen:

- Un nuevo panel de control
- Nuevos flujos de trabajo para ayudar a los usuarios a utilizar la solución BCM de forma inmediata
- Uso de los objetos KPI y KRI para supervisar el rendimiento de BCM.

**Nuevo panel de control**

El panel de control maestro de BCM incorpora ahora objetos KRI y KPI y muestra más métricas para supervisar el rendimiento de la gestión de la continuidad del negocio.

*Figura 1. Panel de control maestro de BCM*

![Se muestra un panel de control en OpenPages. El panel de instrumentos tiene los paneles siguientes: Mis tareas, Análisis de impacto empresarial, Métricas de servicios empresariales y Mis tareas. Los paneles muestran coloridos gráficos de barras y gráficos de anillo. La parte inferior del panel de control se corta para mostrar que el panel de control incluye más paneles.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-bcm_dashboard.png)

**Nuevos tipos de objeto**

BCM incluye los siguientes tipos de objeto nuevos:

- Servicio empresarial

  Un servicio empresarial es un servicio proporcionado por la organización, como la retirada de efectivo de un cajero automático o la capacidad de comprobar un saldo en línea, que puede desglosarse en procesos de soporte. Los servicios empresariales pueden clasificarse además como servicios empresariales importantes, que son servicios prestados a usuarios finales externos en los que una interrupción causaría un daño intolerable a los consumidores o a los participantes en el mercado, a la integridad del mercado, a la protección de los asegurados, a la seguridad y a la solidez, o a la estabilidad financiera.

  Un objeto de servicio empresarial puede ser un hijo de un objeto de Entidad empresarial o Ubicación.
- Evaluación de servicios empresariales

  Los objetos de Evaluación de servicios empresariales son hijos de objetos de servicios empresariales y se utilizan para capturar valores que se proporcionan como parte de la evaluación del servicio empresarial con el fin de establecer tendencias. El servicio Evaluación de servicios empresariales se crea y se rellena como parte del último paso de un flujo de trabajo de evaluación de servicios empresariales.

Los tipos de objeto siguientes están ahora disponibles en BCM:

- KPI, Valor de KPI: se utiliza para medir el rendimiento de los procesos que se correlacionan con los análisis del impacto empresarial. Puede utilizar los objetos de KPI y de valor de KPI para realizar un seguimiento de la gravedad de los procesos a lo largo del tiempo para determinar si son necesarios cambios en la interrupción máxima aceptable, el objetivo de tiempo de recuperación y el objetivo de punto de recuperación.
- KRI, Valor de KRI: se utiliza para supervisar el riesgo relacionado con una infracción de una tolerancia de impacto establecida en servicios empresariales y dependencias relacionadas
- Análisis de escenario: se utiliza para identificar y medir escenarios severos pero plausibles que podrían interrumpir servicios empresariales importantes para probar la probabilidad de que el servicio empresarial pueda recuperarse dentro de las tolerancias de impacto establecidas.
- Resultado del escenario: se utiliza para capturar los valores de los análisis de escenario completados. La creación del objeto y la población de campos se realiza durante la última etapa del flujo de trabajo Análisis de escenario.

**Nuevas asociaciones**

En el release 8.3 se han añadido las siguientes asociaciones de objetos:

- La ubicación ahora tiene las siguientes asociaciones hijo: Proveedor, Recurso, Riesgo, Equipo, KPI y KRI
- El análisis de impacto empresarial ahora tiene las siguientes asociaciones hijo: KRI, KPI, Equipo, Empleado
- Ahora el recurso se puede correlacionar con un objeto de empleado hijo
- El proveedor ahora se puede correlacionar con un suceso de continuidad de negocio hijo

**Nuevos cálculos**

La versión 8.3 incluye actualizaciones de los cálculos así como nuevos cálculos. Los cálculos se pueden agrupar en tres categorías principales:

- Cálculos para análisis de impacto empresarial

  El objeto de Análisis del impacto empresarial se utiliza para ayudar a los usuarios a identificar los procesos más críticos dentro de su organización. Se han añadido cálculos y campos al análisis de impacto empresarial para permitir la evaluación de los impactos a lo largo del tiempo.

  El cálculo, el flujo de trabajo y la vista del release anterior siguen estando disponibles en 8.3, pero están inhabilitados de forma predeterminada.
- Cálculos para impulsar y comparar métricas de BIA

  Los nuevos cálculos y campos permiten la comparación de RTO y RPO de procesos con los recursos y proveedores dependientes para garantizar una alineación adecuada. Por ejemplo, un recurso dependiente de un proceso nunca debe tener un RTO mayor que su proceso padre. Los cálculos y flujos de trabajo en 8.3 empujan las métricas establecidas en un BIA a su proceso padre. A continuación, el RTO del proceso se envía a cada recurso hijo y proveedor. En las instancias cuando el RTO de proceso es inferior al RTO del recurso o cuando el Tiempo de recuperación del recurso excede el RTO de proceso o el RTO de recurso, se establece un distintivo de aviso en el registro de recurso.

  *Figura 2. La sección Continuidad de negocio de la vista Tarea de recurso muestra las métricas RPO y RTO*

  ![La sección Continuidad de negocio de una vista de tarea se muestra en OpenPages. La sección contiene campos como, por ejemplo, objetivo de tiempo de recuperación de procesos, objetivo de tiempo de recuperación de recursos, objetivo de punto de recuperación de procesos, etc. Un campo denominado Aviso de alineación de RTO muestra un icono de aviso rojo.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-bcm_bc_calc.png)

  Los usuarios pueden ver las métricas en el panel de control maestro de BCM.

  *Figura 3. Panel de control maestro de BCM*

  ![Se muestra un panel de control en OpenPages. Se muestran dos paneles: Alertas de objetivo de punto de recuperación y Alertas de objetivo de tiempo de recuperación. Cada panel muestra gráficos de texto y barras. En el panel Alertas de RTO, por ejemplo, un gráfico de barras muestra que dos proveedores y un recurso tienen puntuaciones de gravedad alta.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-bcm_dashbrd-rpo.png)
- Cálculos para la resiliencia operativa

  Los nuevos cálculos en 8.3 identifican los Servicios empresariales y las dependencias relacionadas (Ubicaciones, Procesos, Recursos y Proveedores) con los KRI que están en o cerca de la infracción de una tolerancia de impacto establecida.
- Cálculos para KRI y KPI

  Los nuevos cálculos de 8.3 para KRI y los KPI sustituyen los desencadenantes existentes. Consulte la sección sobre Gestión de riesgos operativos para obtener información adicional.

**Nuevos flujos de trabajo**

La versión 8.3 incluye las siguientes mejoras en los flujos de trabajo:

- Nuevos flujos de trabajo para identificar los servicios empresariales importantes, así como para establecer y probar las tolerancias de impacto.
- Nuevos flujos de trabajo para las evaluaciones de impacto empresarial de los procesos empresariales para tener en cuenta los nuevos cálculos introducidos en 8.3.
- Nuevo flujo de trabajo para garantizar que las correlaciones de dependencias de procesos empresariales se mantienen actualizadas.
- Nuevos flujos de trabajo para establecer y ejecutar planes de prueba de continuidad de negocio. El flujo de trabajo existente de Business Impact Analysis está ahora inhabilitado de forma predeterminada.
- El flujo de trabajo de los informes de los resultados de las pruebas de BC se denomina ahora Documentación de los resultados de las pruebas de BC y se ha actualizado.

Por ejemplo, un nuevo flujo de trabajo denominado Evaluación inicial del servicio empresarial guía a los usuarios a través de la creación de un registro de servicios empresariales, la clasificación de un servicio empresarial como un servicio empresarial importante, la correlación de los servicios empresariales importantes con las dependencias y el establecimiento de su tolerancia al impacto. El flujo de trabajo utiliza los nuevos campos y vistas que se proporcionan en la versión 8.3.

*Figura 4. El nuevo flujo de trabajo de evaluación inicial del servicio empresarial*

![Se muestra un flujo de trabajo en el Diseñador de flujos de trabajo. El flujo de trabajo tiene nueve etapas.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-bcm_workflow.png)

**Integración con Supply Wisdom**

> **Nota** : Esta integración se eliminó en 9.1.0.

La versión 8.3 incluye una integración con Supply Wisdom que incluye lo siguiente para los suscriptores de Supply Wisdom :

- Alertas en el objeto de suceso de continuidad de negocio que se correlacionan con ubicaciones y proveedores
- Datos de riesgo dentro del objeto de ubicación
- Datos de riesgo dentro del objeto de proveedor
- Un nuevo perfil, BCM Supply Wisdom Master

*Figura 5. La vista de tareas de ubicación*

![Se visualiza la nueva sección Clasificaciones de sabiduría de suministro de la vista de tarea Ubicación. La sección contiene dos gráficos de anillos (un gráfico muestra las tendencias de riesgo, el otro muestra la gravedad) y una vista de cuadrícula de los riesgos.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-bcm_view_sw.png)

#### Mejoras de la Gestión de privacidad de datos en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0 › Mejoras de soluciones en 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-data-privacy-management-enhancements-in)

Versión 8.3 incluye varias mejoras en IBM OpenPages® Data Privacy Management (DPM).

**Nuevo panel de control**

IBM OpenPages Data Privacy Management incluye un nuevo panel de control.

*Figura 1. Panel de control de DPM*

![Se muestra un panel de control en OpenPages. El panel de control incluye un panel denominado Mis tareas con una barra codificada por colores que muestra el estado de las tareas. Otro panel muestra un gráfico circular colorido de Recursos por ubicación física.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-dpm_dashboard.png)

**Nuevo flujo de trabajo**

DPM incluye dos flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

- **Evaluación de impacto de privacidad**

  Este flujo de trabajo ayuda a las organizaciones a gestionar el proceso de evaluación de impacto de privacidad Cuando se importa un nuevo activo de datos (recurso) en Watson Knowledge Catalog, el flujo de trabajo de Evaluación de impacto de privacidad se inicia automáticamente y guía a los responsables de privacidad a través del proceso de evaluación.

  *Figura 2. Evaluación de impacto de privacidad*

  ![Se visualiza un flujo de trabajo en el diseñador de flujos de trabajo. El flujo de trabajo empieza con una etapa Revisión de activo de datos y finaliza con una etapa Evaluación de privacidad no necesaria o una etapa Evaluación de privacidad completada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-dpm_pia_workflow.png)

- **Evaluación del impacto de la protección de datos**

  Este flujo de trabajo ayuda a las organizaciones a gestionar el proceso de evaluación del impacto de la protección de datos (DPIA). El flujo de trabajo utiliza evaluaciones de cuestionario para ayudar a los responsables de privacidad y a los administradores de datos a completar las evaluaciones de DPIA.

  *Figura 3. Flujo de trabajo de evaluación del impacto de protección de datos*

  ![Se visualiza un flujo de trabajo en el diseñador de flujos de trabajo. El flujo de trabajo empieza con una etapa DPIA iniciada y termina con una etapa DPIA no necesaria o una etapa DPIA completada.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-dpm_dpia_workflow.png)

**Nuevas plantillas de rol**

Las plantillas de funciones para la gestión de Data Privacy ahora se incluyen con OpenPages.

#### Mejoras de Gobierno de TI en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0 › Mejoras de soluciones en 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-it-governance-enhancements-in)

La versión 8.3 incluye una integración con la plataforma de análisis de cuantificación de riesgos cibernéticos RiskLens.

> **Nota** : Esta función se eliminó en la versión 9.1.

Dentro de la plataforma RiskLens, los usuarios registran los activos y las amenazas incluidas dentro de los escenarios y llenan estos objetos de acuerdo con el método FAIR utilizando ayudantes de datos proporcionados en RiskLens. La integración con OpenPages® permite a un usuario de OpenPages enviar un registro para su inclusión dentro de una evaluación de riesgo en RiskLens. El objeto se puede asociar a uno o más escenarios dentro de las simulaciones de RiskLens y Monte Carlo. Después de completar la simulación y de acuerdo con el trabajo planificado en OpenPages, las métricas de exposición a pérdidas generadas por las simulaciones de Monte Carlo se extraen en OpenPages para su uso en toda la aplicación. El trabajo planificado en OpenPages extrae datos actualizados de RiskLens cuando se modifican las evaluaciones de riesgo.

De forma similar a otras integraciones, se requiere una licencia separada con RiskLens para integrar a su plataforma y el grupo de campo, el trabajo y las vistas se pueden obtener como un paso posterior a la instalación.

**Nuevo grupo de campos**

El siguiente grupo de campos se ha añadido al objeto de riesgo: **OPS-RiskLens**.

*Figura 1. Ejemplo de campos rellenados a partir de datos proporcionados por la integración de RiskLens*

![Se visualiza una vista de tarea en OpenPages. La vista tiene una sección de Integración de RiskLens, que incluye un enlace a RiskLens, métricas, estado de la solicitud y la fecha de la última ejecución.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-itg_fieldgrp.png)

**Nuevo trabajo en el planificador**

El nuevo trabajo RiskLens está configurado para enviar datos y extraer datos de RiskLens. El trabajo está preconfigurado para empujar y extraer datos en el tipo de objeto de riesgo; sin embargo, al añadir el grupo de campos OPSS-RiskLens a un objeto diferente y añadir ese objeto al campo Tipos de objeto del trabajo, cualquier objeto puede ser enviado a la plataforma RiskLens como un registro de evaluación de riesgo. Dentro del trabajo, los campos URL de API, URL de autenticación, ID de cliente y Secreto de cliente deben rellenarse para conectarse a la plataforma RiskLens.

**Nuevas vistas**

Se han añadido las siguientes vistas para dar soporte a la integración de RiskLens:

- SysView-Task-SOXRisk-RiskLens
- SysView-Task-SOXRisk-RiskLens-2
- SysView-Task-SOXRisk-RiskLens-3
- SysView-Admin-SOXRisk-RiskLens

#### Mejoras en el gobierno de riesgos de modelo en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0 › Mejoras de soluciones en 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-model-risk-governance-enhancements-in)

Versión 8.3 incluye varias mejoras en IBM OpenPages® Model Risk Governance (MRG).

En 8.3 hemos realizado algunas mejoras en el modelo de objeto para dar soporte a varios despliegues (usos) de un modelo y a la posibilidad de publicar métricas de OpenScale en despliegues de modelo en lugar del modelo padre. Hemos añadido un objeto nuevo denominado Versión de modelo como un objeto opcional para un nivel de detalle adicional entre un modelo y un despliegue de modelo.

**Nuevos tipos de objeto**

MRG incluye los siguientes tipos de objeto nuevos:

- **Versión del modelo**

  El objeto Versión de modelo es un hijo del objeto Modelo y padre del Despliegue de modelo. El objeto Versión del modelo es opcional. Si se necesitan más detalles cuando se compilan varias versiones de un modelo, el objeto Versión del modelo puede utilizarse como objeto intermedio.
- **Obligación**

  El tipo de objeto Obligación representa las "cosas que hay que hacer" normalizadas y armonizadas para cumplir con todos los objetos Mandato, Submandato y Requisito asociados a la obligación. Esto podría aplicarse a los reglamentos relacionados con el modelo.

  Los objetos Obligación cumplen dos objetivos principales: traducen la jerga legal, a menudo difícil y farragosa, de los mandatos/submandatos/requisitos a un inglés sencillo, y utilizan los elementos comunes a varios mandatos/submandatos/requisitos. Por ejemplo, es posible que tenga muchos submandatos y requisitos en numerosos mandatos que requieren un proceso de validación de modelos sólido. Un único objeto Obligación puede documentar los detalles para la validación del modelo. Al cumplir con esta única obligación, la gestión del riesgos del modelo puede satisfacer muchos mandatos, submandatos y requisitos.
- **Evaluación de la obligación y valor de evaluación de la obligación**

  Una vez que los usuarios han correlacionado los controles internos con las obligaciones, los usuarios pueden realizar una evaluación de lo bien que están operando en relación con la obligación identificada. Los usuarios pueden evaluar la efectividad operativa y la efectividad de diseño delos controles dentro del ámbito de un tema de conformidad.

  Los valores de evaluación de la obligación se utilizan para registrar el valor real de una obligación en un momento determinado dentro del ámbito de una evaluación de obligación.

**Nuevos cálculos**

Los nuevos cálculos de métrica ayudan en el proceso de recopilación de métricas y mantienen las métricas en sincronización con el último valor de la métrica. El cálculo de la tarjeta de puntuación es más fácil de personalizar y actualizar que el desencadenante al que sustituye.

- El nuevo cálculo, Actualización del valor de la métrica, sustituye al flujo de trabajo de Información del último valor de la métrica de actualización de OpenScale
- El nuevo cálculo, Tarjeta de puntuación de riesgo, sustituye al desencadenante de la tarjeta de puntuación de riesgo de modelo
- Dos cálculos adicionales: Siguiente fecha de recopilación de métricas y Valor de métrica - Actualización de la métrica padre

**Nuevo flujo de trabajo**

La versión 8.3 incluye un nuevo flujo de trabajo, Creación de valor de métrica. Cuando vence la próxima fecha de recogida de una métrica activa, este flujo de trabajo crea automáticamente un nuevo valor de métrica y lo rellena con la información del propietario, el captador y el umbral de la métrica principal. A continuación, el recopilador puede llenar la información de valor de métrica y enviarla para su revisión.

#### Mejoras en la gestión de riesgos operativos en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0 › Mejoras de soluciones en 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-operational-risk-management-enhancements-in)

Versión 8.3 incluye varias mejoras en IBM OpenPages® Operational Risk Management (ORM).

Las actualizaciones incluyen:

- Un nuevo panel de control
- Flujos de trabajo, cálculos, vistas y modificaciones de campos nuevos y actualizados para ayudar a los usuarios a utilizar la solución ORM de forma inmediata
- Sustitución del programa de utilidad de desencadenante KRI y KPI con el uso de cálculos, flujos de trabajo y el planificador.

**Nuevo panel de control**

El panel de control maestro de ORM proporciona una visión general de alto nivel de las diversas actividades de ORM que puede utilizar un propietario, gestor o analista de riesgos operativos. Este panel de control visualiza o enlaza con datos relevantes como, por ejemplo, entidades y procesos empresariales de la organización, KRI, sucesos de pérdida, riesgos, controles, problemas y acciones. También permite crear fácilmente nuevos objetos directamente desde el panel de control.

*Figura 1. Panel control maestro de ORM*

![Se muestra un panel de control en OpenPages. El panel de control incluye un panel denominado Mis tareas con una barra codificada por colores que muestra el estado de las tareas. Varios otros paneles muestran coloridos gráficos circulares. Por ejemplo, un panel tiene un gráfico de anillos que muestra el estado de ruptura de los indicadores clave de riesgo (KRI).](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-orm_dashbrd.png)

**Cálculos nuevos y actualizados**

La versión 8.3 incluye actualizaciones de los cálculos así como nuevos cálculos.

- **Cálculos para KRI y KPI**

  Se han creado nuevos cálculos para sustituir los desencadenantes de ciclo de vida de KRI/KPI existentes.

  - KRIValue - Aumento y KRIValue - Disminución

    Estos cálculos automáticos se aplican a los valores de KRI con un KRI padre en un estado Activo, con cálculos separados aplicados en función de si el campo Información de dirección del KRI padre se establece como «“Aumento significa mayor riesgo”» o «“Disminución significa mayor riesgo.”» El cálculo identifica el umbral amarillo, el umbral rojo y la información de dirección del KRI padre y establece estos campos en el valor de KRI. El cálculo establece el estado de la infracción en el valor de KRI basado en la entrada del campo Valor en el registro de valor de KRI comparado con los umbrales amarillo y rojo.
  - Aumento de KRI y disminución de KRI

    Estos cálculos automáticos se aplican a KRI en un estado Activo, con cálculos separados aplicados en función de si el campo Información de dirección se establece en «“Aumento significa mayor riesgo”» o «“Disminución significa mayor riesgo.”» El cálculo trae los campos Valor de los valores de KRI en un estado de recopilación de «“Recopilado”» que están relacionados con el KRI. El cálculo clasifica los valores en orden descendente por valor de fecha y compara los dos últimos valores. A continuación, el cálculo establece el campo Tendencia de indicador en el KRI comparando los dos valores que son más recientes en el tiempo. A continuación, establece el campo Valor en el KRI basándose en el valor del KRI con la última fecha de valor en el tiempo y utiliza esta misma entrada para determinar el estado de incumplimiento del KRI comparando el valor con los umbrales amarillo y rojo en el KRI.
  - Siguiente fecha de recopilación de KRI

    Este cálculo automático se aplica a los KRI en un estado Activo. El cálculo establece la Siguiente fecha de recopilación añadiendo días a la Siguiente fecha de recopilación de KRI basada en el campo Frecuencia en el KRI y la Fecha de recopilación prevista en los valores de KRI relacionados.
  - Indicador clave de riesgo

    Este cálculo automático establece la última fecha de valor de un valor KRI en el KRI principal. El cálculo también establece el estado de recopilación de KRI en función del estado de recopilación del valor de KRI con la fecha de valor más reciente.

  La vista de tareas de KRI muestra la fecha de la próxima recopilación calculada basada en la frecuencia y la fecha de inicio de la recopilación de KRI; la tendencia de indicador y estado de indicador calculado basándose en los umbrales definidos y la información de dirección; y la información de último valor de KRI calculada basada en el valor de KRI más reciente en el estado recopilado.

  *Figura 2. La vista de tareas de KRI*

  ![Se visualiza una vista de tarea de Indicador clave de riesgo (KRI) en OpenPages. La vista muestra la información de medición de KRI, el valor más reciente del KRI, un gráfico de colores que muestra el estado de la colección del KRI, y una vista de cuadrícula de los valores de KRI que son hijos del KRI. La vista de cuadrícula incluye información sobre el estado de recopilación y el estado de infracción de cada valor KRI.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-orm_view.png)

- **Cálculos de KPI**

  Los cálculos siguientes están relacionados con los objetos de KPI y del valor de KPI y son similares a los cálculos del valor de KRI y KRI:

  - KPI
  - KPI - Disminuir
  - KPI – Aumentar
  - Siguiente fecha de recopilación de KPI
  - KPIValue - Disminución
  - KPIValue - Aumento

- **Cálculos para pruebas de control**

  Se han creado nuevos cálculos para determinar la próxima fecha de vencimiento de las pruebas si una prueba de control se produce de forma planificada y llevar la información más reciente del resultado de la prueba al objeto principal del plan de pruebas.

  - Plan de pruebas

    Este cálculo automático establece la última fecha de realización de un resultado de prueba al plan de pruebas padre. El cálculo también establece el estado del plan de pruebas basado en el estado de resultado de prueba hijo con la fecha de realización más reciente. El cálculo clasifica los valores de Resultado de prueba en orden descendente por Fecha de realización y compara los dos últimos resultados. A continuación, el cálculo establece el campo Tendencia en el plan de pruebas comparando los dos resultados que son más recientes en el tiempo.
  - Fecha de vencimiento de pruebas

    Descripción: este cálculo automático establece la fecha de vencimiento del plan de pruebas añadiendo días a la última fecha de vencimiento del resultado de la prueba basada en el campo Frecuencia del plan de pruebas (diaria, semanal, mensual o anual) y la fecha de inicio prevista del plan de pruebas.

- **Actualización de cálculo para la evaluación de riesgos cualitativos**

  El cálculo actualizado en 8.3 incluye ahora un valor de campo predeterminado de «“No determinado”» para la calificación de riesgo inherente y residual.

**Nuevos flujos de trabajo**

DPM incluye dos flujos de trabajo de ejemplo. Puede utilizarlos tal cual o modificarlos para que se ajusten a sus necesidades. Los flujos de trabajo de ejemplo también se pueden utilizar como plantillas y herramientas de aprendizaje para sus propios flujos de trabajo.

- **Nuevos flujos de trabajo para KRI / KPI y KRI / Valores de KPI**

  Se han creado los siguientes flujos de trabajo relacionados con los objetos KRI y KRIValue y KPI y KPIValue:

  - Creación de valor de KRI
  - Entrada de valor de KRI
  - Creación de valor de KPI
  - Entrada de valor de KPI

  Los flujos de trabajo de creación de valor de KRI y creación de valor de KPI crean automáticamente valores KRI/KPI basados en la planificación/frecuencia definidas en el KRI/KPI padre. Cuando la próxima fecha de recopilación se debe a un valor de KRI/KPI activo, este flujo de trabajo crea automáticamente un nuevo valor de KRI/KPI y lo llena con información de propietario, capturador y umbral del KRI/KPI padre. Con los flujos de trabajo Entrada de valor de KRI y Entrada de valor de KPI, el recopilador puede entonces llenar la información de valor de KRI/KPI y enviarla para su revisión o aprobación.

  Estos flujos de trabajo, en combinación con los cálculos introducidos en 8.3 para KRI/KPI, sustituyen a los desencadenantes de KRI/KPI y a los ayudantes (desencadenante de ciclo de vida, programa de utilidad de creación de valor y notificaciones vencidas). Las notificaciones de correo electrónico se desencadenan con el flujo de trabajo cuando el valor de KRI/KPI cambia el estado de infracción.

- **Nuevos flujos de trabajo para pruebas de control**

  Se han creado los siguientes flujos de trabajo relacionados con los objetos Plan de pruebas y Resultado de prueba:

  - Crear resultado de prueba
  - Realizar prueba de control
  - Actualizar y revisar plan de prueba

  El flujo de trabajo Crear resultado de prueba crea automáticamente un resultado de prueba basado en la planificación o frecuencia definida en el plan de prueba padre. Cuando llega la próxima fecha de vencimiento de un plan de pruebas activo, este flujo de trabajo crea automáticamente un nuevo resultado de prueba, y lo rellena con la información del ejecutor de la prueba y la fecha de vencimiento de la prueba del plan de pruebas principal. Con el flujo de trabajo Realizar prueba de control, la prueba pasa por su realización, revisión, solicitud de documentación (si es necesaria), e incluso se crea automáticamente una incidencia si el resultado de la prueba ha fallado.

- **Otros nuevos flujos de trabajo y mejoras del flujo**

  - Nuevos flujos de trabajo para la Autoevaluación de riesgos y control (RCSA) y para la Evaluación de control para establecer y ejecutar una evaluación cualitativa del riesgo y una evaluación de control.
  - Un flujo de trabajo mejorado para revisiones de sucesos de pérdida.
  - Se ha creado un nuevo grupo de campos para Comentarios de flujo de trabajo bajo el objeto Riesgo. El grupo de campos se utiliza para almacenar comentarios de flujo de trabajo en varias etapas de flujo de trabajo.

#### Mejoras en la gestión de políticas en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0 › Mejoras de soluciones en 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-policy-management-enhancements-in)

Versión 8.3 incluye varias mejoras en IBM OpenPages® Policy Management (PCM).

**Nuevo panel de control**

PCM incluye un nuevo panel de control, el panel de control del propietario de PCM.

El panel de control Propietario de PCM de OpenPages proporciona una visión general de alto nivel de las diversas actividades de política que puede utilizar un propietario de política o un gestor de políticas. Un propietario o gestor de políticas puede utilizar el panel de control para visualizar o enlazar con datos relevantes como las tareas de las políticas, el estado de las políticas que posee, las campañas de las políticas que posee o las actividades de planificación de las políticas.

*Figura 1. Panel de control de propietario de políticas de PCM*

![Se muestra un panel de control en OpenPages. El panel de control tiene los paneles siguientes: Mis tareas de política, Buscar, Mis políticas, Informes, Estado de PRC y Mis favoritos.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-pcm_dashboard.png)

**Nuevo flujo de trabajo**

PCM incluye un nuevo flujo de trabajo, Revisión y aprobación de políticas. Este flujo de trabajo permite a las organizaciones gestionar la revisión de políticas y el proceso de aprobación mediante la automatización.

El flujo de trabajo Revisión y aprobación de políticas aborda los siguientes casos de uso:

- Nuevo proceso de creación de políticas
- Proceso de revisión de políticas anual
- Procesos de revisión ad hoc o fuera de ciclo

*Figura 2. Flujo de trabajo Revisión y aprobación de políticas*

![El flujo de trabajo se muestra en el Diseñador de flujos de trabajo. Es un flujo de trabajo complejo con varias ramas: nuevas políticas, políticas con cambios importantes, políticas con cambios menores y políticas sin cambios.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-pcm_review_workflow.png)

Las etapas y los usuarios de ejemplo del flujo de trabajo incluyen:

| Etapas | Usuarios de ejemplo |
| --- | --- |
| Revisión y selección | Propietario de política, Gestor de políticas |
| Nueva política, Cambio importante, Cambio menor, Sin cambios | Propietario de política, Autor, Editor |
| Revisor y aprobación de experto en la materia, Aprobación ejecutiva | Experto en la materia, Supervisores, Cumplimiento, Gestión, Ejecutivo |

> **Sugerencia:** Puede añadir etapas al flujo de trabajo para aprobadores adicionales.

La capacidad de aprovechar la capacidad de «“solo lectura”» a nivel de campo en el flujo de trabajo o en la vista de tareas de la política proporciona una alternativa práctica al bloqueo de todos los campos del objeto. Anteriormente, PCM utilizaba ayudantes y ajustes.

**Nuevo cálculo**

PCM incluye un nuevo cálculo, Comentario de revisión de política.

El cálculo rellena la descripción de objeto de comentario de revisión de política (PRC) con el nombre de política. Esto proporciona contexto a los usuarios cuando están viendo el objeto PRC en una vista de lista o de cuadrícula.

*Figura 3. Comentario de revisión de política en una vista de cuadrícula*

![Una vista de cuadrícula contiene un comentario de revisión de política. La columna Descripción muestra el nombre de la política relacionada del comentario de revisión.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-pcm_view.png)

Puede inhabilitar este cálculo, si es necesario.

#### Mejoras en la gestión de conformidad reguladora en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0 › Mejoras de soluciones en 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-regulatory-compliance-management-enhancements-in)

Versión 8.3 incluye varias mejoras en IBM OpenPages® Regulatory Compliance Management (RCM).

Las actualizaciones incluyen nuevos tipos de objetos, flujos de trabajo, cálculos y modificaciones de campos para facilitar a los usuarios la realización de evaluaciones de conformidad desde el primer momento.

El ayudante de tema de conformidad - el proceso de enviar o extraer los temas de conformidad de una carpeta de entidad empresaria - no ha cambiado, aunque se han mejorado las vistas, los flujos de trabajo y los cálculos que se utilizan para las evaluaciones de conformidad.

**Nuevos tipos de objeto**

RCM incluye varios tipos de objeto nuevos:

- **Evaluación de temas de conformidad**

  Los objetos Evaluación de temas de conformidad son hijos de objetos Tema de conformidad. Los objetos Evaluación de temas de conformidad se utilizan para capturar valores que se proporcionan como parte de la evaluación de conformidad que se captura en el tema de conformidad. Se crea un registro de evaluación de temas de conformidad y se rellena como el último paso en los flujos de trabajo Evaluación de BE de temas de conformidad y Evaluación de la biblioteca de temas de conformidad.
- **Evaluación del plan de conformidad**

  Los objetos Evaluación del plan de conformidad son hijos del objeto Plan de conformidad. Los objetos Evaluación del plan de conformidad se utilizan para capturar valores que se proporcionan como parte de la evaluación de conformidad que se captura en el plan de conformidad. Se crea un registro de Evaluación del plan de conformidad y se rellena como último paso en los flujos de trabajo Evaluación de BE del plan de conformidad y Evaluación de la biblioteca del plan de conformidad.
- **Obligación**

  El tipo de objeto Obligación representa las "cosas que hay que hacer" normalizadas y armonizadas para cumplir con todos los objetos Mandato, Submandato y Requisito asociados a la obligación.

  El objeto Obligación cumple dos objetivos principales: traduce la jerga legal, a menudo difícil y farragosa, de los mandatos/submandatos/requisitos a un inglés sencillo, y utilizan los elementos comunes a varios mandatos/submandatos/requisitos. Por ejemplo, es posible que tenga muchos submandatos y requisitos en numerosos mandatos que requieren el uso de contraseñas fuertes. Un solo objeto Obligación puede documentar los detalles para contraseñas fuertes. Cumpliendo esta única obligación, la tecnología de la información pueden satisfacer muchos mandatos, submandatos y requisitos.
- **Evaluación de la obligación y valor de evaluación de la obligación**

  Una vez que los usuarios han correlacionado los controles internos con las obligaciones, los usuarios pueden realizar una evaluación de lo bien que están operando en relación con la obligación identificada. Los usuarios pueden evaluar la efectividad operativa y la efectividad de diseño delos controles dentro del ámbito de un tema de conformidad.

  Los valores de evaluación de la obligación se utilizan para registrar el valor real de una obligación en un momento determinado dentro del ámbito de una evaluación de obligación.

  La versión 8.3 también añade soporte para una nueva asociación de tipo de objeto: los tipos de objeto de política y procedimiento ahora pueden tener un objeto de evaluación de requisitos como padre.

**Nuevos cálculos**

La versión 8.3 incluye varios cálculos nuevos para agregar los datos de los controles a las evaluaciones de requisitos, de las evaluaciones de requisitos a los temas de conformidad y de los temas de conformidad a los planes de conformidad. Estas métricas calculadas se pueden utilizar para ayudar al usuario en la realización de su evaluación y también se incluyen dentro de los registros de valor de evaluación de requisitos, evaluación de temas de conformidad y evaluación del plan de conformidad para el análisis de tendencias.

**Flujos de trabajo nuevos y actualizados**

Los nuevos flujos de trabajo para la evaluación de conformidad se pueden categorizar como flujos de trabajo de biblioteca de temas, flujos de trabajo de evaluación y flujos de trabajo de restablecimiento.

Los flujos de trabajo de la biblioteca de temas ayudan a los usuarios a construir un tema de conformidad, que luego se puede desplegar en las entidades empresariales utilizando el desplegador de temas de conformidad. Por ejemplo, el flujo de trabajo de creación de la biblioteca de temas de conformidad ayuda a los usuarios a la construcción de los temas de conformidad de bibliotecas que se pueden desplegar en las entidades empresariales para su evaluación. El flujo de trabajo se inicia automáticamente cuando los usuarios crean un nuevo objeto de biblioteca de tema des conformidad.

*Figura 1. Flujo de trabajo Creación de biblioteca de temas de conformidad*

![El Editor de flujos de trabajo muestra las etapas en el flujo de trabajo: Inicio, Correlación de requisitos, Aprobación, Iniciar desplegador de temas y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-rcm_lib_workflow.png)

Los flujos de trabajo de evaluación están ahora disponibles para los objetos Evaluación de requisitos, Requisito, Tema de conformidad y Plan de conformidad. Por ejemplo, el flujo de trabajo Evaluación de requisitos ayuda a los usuarios a evaluar la eficacia de los controles para gestionar el riesgo de conformidad de los requisitos correlacionados. Con este flujo de trabajo, los usuarios revisan todos los controles que son hijos de la evaluación de requisitos y, a continuación, proporcionan evaluaciones para la eficacia del diseño del control, la eficacia operativa y una valoración general sobre lo bien que los controles abordan el requisito subyacente bajo revisión.

*Figura 2. Flujo de trabajo de evaluación de requisitos*

![El Editor de flujos de trabajo muestra las etapas del flujo de trabajo: Inicio, Evaluación de requisitos, Aprobación de evaluación y Fin.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_new_features/nfg8300-rcm_assess_workflow.png)

Los flujos de trabajo de restablecimiento funcionan conjuntamente para renovar los datos de evaluación que se especifican en los registros de evaluación de requisitos, tema de conformidad y plan de conformidad cuando se implementa un nuevo ciclo de evaluación.

**Nuevos perfiles para los proveedores de canales de información:**

- RCM Ascent Master
- RCM Reg-Track Master
- RCM TRRI Master
- RCM WK Master

#### Mejoras en la gestión de riesgos de terceros en 8.3.0

`Características nuevas › Nuevas características en la versión 8.3.0 › Mejoras de soluciones en 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-third-party-risk-management-enhancements-in)

Versión 8.3 incluye mejoras para OpenPages® Third Party Risk Management (TPRM).

Las actualizaciones incluyen mejoras en el cuestionario, que se utilizan al realizar una evaluación de proveedor.

La integración de Supply Wisdom se ha mejorado con la ingestión de supervisión de sucesos de proveedores junto con las ubicaciones en las que operan dichos proveedores. Se han añadido factores de riesgo de ubicación para ayudar a identificar los riesgos geopolíticos y medioambientales que podrían afectar a la prestación de servicios de un proveedor

> **Nota** : La integración de Supply Wisdom se eliminó en 9.1.0.

Ahora están disponibles nuevos flujos de trabajo listos para usar para la gestión del ciclo de vida del proveedor (Selección a través de la terminación). Estos flujos de trabajo están diseñados para ser complementados por los procesos internos del usuario:

- **Selección de proveedor**

  Este flujo de trabajo se utiliza al seleccionar proveedores. Este flujo de trabajo puede ser utilizado por el aprovisionamiento o una entidad empresarial en su proceso. El primer paso es identificar las responsabilidades del proveedor que se deben añadir como parte del proceso RFI del cliente. Una vez determinado, se creará la RFI y se determinará una lista de proveedores para participar. A continuación, el cliente utiliza su propio proceso de RFI y realiza un seguimiento de los resultados. A continuación, el usuario utilizará el flujo de trabajo Debida diligencia antes de la selección final. Al finalizar el flujo de trabajo de selección de proveedor, el usuario puede iniciar el flujo de trabajo de incorporación de proveedores.

- **Diligencia debida de proveedor**

  Este flujo de trabajo es para llevar a cabo la diligencia debida sobre un tercero potencial. Se puede añadir un cuestionario o lista de comprobación (basada en procesos internos) para documentar el proceso de diligencia debida. El flujo de trabajo empieza con la identificación del proveedor y, a continuación, asigna un usuario a la tarea de diligencia debida. Una vez completada la recopilación de hechos, el flujo de trabajo documenta los pasos de aprobación para aceptar o rechazar un proveedor.

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

### Software soportado en 8.3

`Características nuevas › Nuevas características en la versión 8.3.0` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=830-supported-software-in-83)

IBM OpenPages® 8.3.0 requiere nuevas versiones de algún software:

**Tabla 1. Cambios en las versiones de software soportadas**

| Software | Cambios de conformidad |
| --- | --- |
| Oracle Database | Oracle 12c y 18c ya no están soportados.<br>La versión 19.3 es la versión mínima soportada. |
| Base de datos de IBM® Db2® | Enterprise Server Edition 11.1.x ya no está soportado.<br>Advanced Edition 11.5.5 es la versión mínima soportada. |
| IBM Cognos® Analytics | 11.1.x ya no está soportado.<br>La versión 11.2.1 es la versión mínima soportada. También se da soporte a los releases continuos de 11.2.x. |
| Soporte de navegador Web | Microsoft Internet Explorer 11 ya no está soportado. |

Para obtener más información, consulte [Entornos soportados](https://www.ibm.com/support/pages/node/713069).

## Avisos

`Características nuevas` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=features-notices)

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

La información relacionada con productos que no son de IBM se ha obtenido de los proveedores de dichos productos, de sus anuncios publicados o de otras fuentes de disponibilidad pública. IBM no ha probado estos productos y no puede confirmar la precisión de su rendimiento, su compatibilidad o cualquier otra reclamación relacionada con productos que no sean de IBM. Las preguntas relacionadas con las prestaciones de los productos que no son de IBM deberán dirigirse a los proveedores de estos productos.

Todas las declaraciones relacionadas con futuras directrices o intenciones de IBM están sujetas a cambios o a su retirada sin previo aviso y sólo representan objetivos.

Este manual contiene ejemplos de datos e informes que se utilizan en operaciones comerciales diarias. Para ilustrarlas de la forma más completa posible, los ejemplos incluyen los nombres de personas, empresas, marcas y productos. Todos estos nombres son ficticios y cualquier similitud a los nombres y direcciones que haya utilizado una empresa real es pura coincidencia.

Si ha optado por visualizar la copia software de esta información, puede que no aparezcan las fotografías y las ilustraciones a color.

Esta oferta de software no utiliza cookies ni otro tipo de tecnología para recopilar información de identificación personal.
