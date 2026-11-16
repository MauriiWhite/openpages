---
product: IBM OpenPages 9.1.3
product_key: SSFUEU_9.1
file: 9
guide: Guía del desarrollador
covers: Guía del desarrollador — Integración de OpenPages con la seguridad de IBM® WebSphere Liberty
chapters: 12
topics: 18
words: 12655
tasks: 1
concepts: 17
references: 0
tables: 1
code_blocks: 42
figures: 1
applies_to: sin declarar
updated: 2026-02-11
lang: es
source: https://www.ibm.com/docs/es/openpages/9.1.x?topic=developer-guide
extracted: 2026-11-16
---

# 9 · Guía del desarrollador

> **Qué hay en este archivo.** «Guía del desarrollador» de IBM OpenPages 9.1.3, completa: 12 capítulos. 18 temas, 1 de ellos un procedimiento paso a paso, 1 tabla, 42 bloques de código, 1 figura y 12.655 palabras.
>
> **Capítulos:** Guía del desarrollador · Novedades · Tareas de actualización para desarrolladores · Extensiones · Webhooks · API Java deIBM OpenPages GRC · IBM OpenPages API REST GRC V2 · IBM OpenPages API REST GRC V1 · Ejemplos de API · Activadores · Avisos · Integración de OpenPages con la seguridad de IBM® WebSphere Liberty.
>
> **Si lo que buscas no está acá.** El índice de los 2.417 temas del producto, con su archivo y su ancla, está en `index.md`.

**Términos propios de este archivo:** oauth, certificado, curl, regex, regular, openapi, oidc, token, liberty, captura, nativa, openid, coincidente, sujeto.

## Índice de este archivo

- [Guía del desarrollador](#guía-del-desarrollador)
- [Novedades](#novedades)
  - [Novedades de la versión 9.1.0](#novedades-de-la-versión-910)
  - [Novedades de la versión 9.0.0.5](#novedades-de-la-versión-9005)
  - [Novedades de la versión 9.0.0.4](#novedades-de-la-versión-9004)
  - [Novedades de la versión 9.0.0.3](#novedades-de-la-versión-9003)
  - [Novedades de la versión 9.0.0.2](#novedades-de-la-versión-9002)
  - [Novedades de la versión 9.0.0.1](#novedades-de-la-versión-9001)
- [Tareas de actualización para desarrolladores](#tareas-de-actualización-para-desarrolladores)
- [Extensiones](#extensiones)
- [Webhooks](#webhooks)
- [API Java deIBM OpenPages GRC](#api-java-deibm-openpages-grc)
- [IBM OpenPages API REST GRC V2](#ibm-openpages-api-rest-grc-v2)
- [IBM OpenPages API REST GRC V1](#ibm-openpages-api-rest-grc-v1)
- [Ejemplos de API](#ejemplos-de-api)
- [Activadores](#activadores)
- [Avisos](#avisos)
- [Integración de OpenPages con la seguridad de IBM® WebSphere Liberty](#integración-de-openpages-con-la-seguridad-de-ibm-websphere-liberty)


# Guía del desarrollador

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=developer-guide)

Puede utilizar la API REST deIBM OpenPages GRC, IBM OpenPages GRC Java™y desencadenantes para interactuar mediante programación con IBM OpenPages®.

## Novedades

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=guide-whats-new)

Hay características nuevas y modificadas disponibles para IBM OpenPages®.

Para obtener información sobre todas las características nuevas de este release, consulte la publicación *IBM OpenPages New Features Guide*.

### Novedades de la versión 9.1.0

`Guía del desarrollador › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=new-whats-in-version-910)

Las actualizaciones en IBM OpenPages® REST API V2 en la versión 9.1.0 se describen en la siguiente sección.

#### Nuevos límites de puntos finales y parámetros de consulta en la API REST de GRC V2

- El nuevo punto final `get /questionnaire/{id}/template` obtiene una plantilla de cuestionario especificando el ID.
- El nuevo punto final `get /questionnaire/{id}/assessment` obtiene una evaluación del cuestionario al especificar el ID.
- El nuevo punto final `post /contents/bulk` crea una lista de nuevos objetos. Si los objetos ya existen, se actualizan.
- El parámetro de consulta `offset` tiene ahora un valor máximo de `2147483647` y un valor mínimo de `0` y el parámetro de consulta `limit` tiene ahora un valor máximo de `1000` y un valor mínimo de `0` para los siguientes puntos finales:

  - `get /configuration/settings/all/{setting_path}`
  - `get /configuration/currencies/{code}/exchange_rates`
  - `get /configuration/text`
  - `get /contents/{id}/associations`
  - `get /folders/{folder_id}/resources`
  - `get /processes/{process_id}/logs`
- Los parámetros de consulta `offset` y `limit` tienen ahora un valor máximo de `2147483647` y un valor mínimo de `0` para el punto final `get /query` .
- Los parámetros de consulta `start_row` y `end_row` tienen ahora un valor máximo de `2147483647` y un valor mínimo de `0` para el punto final `get /contents/deletedresources` .
- Los ayudantes basados en el modelo `ReactCarbonHelper` ahora admiten la configuración de campos de sólo lectura.

Para más información, consulte la [documentación de IBM® API Hub](https://developer.ibm.com/apis/catalog/openpages--ibm-openpages-with-watson-rest-api-v2).

#### Compatibilidad nativa con la autenticación OAuth 2.0 para OpenPages REST API V1 y V2

Ahora puede configurar la autenticación nativa de OAuth2.0 para OpenPages IBM OpenPages REST API V1 y V2 en IBM OpenPages on premises o IBM OpenPages on Cloud.

En esta configuración, OpenPages desempeña el papel de servidor de autorización OAuth 2.0. Puede utilizar un proveedor de OpenID Connect (OIDC) como proveedor de identidad ( IdP ).

Para obtener más información sobre cómo configurar la autenticación nativa de OAuth 2.0, consulte el tema [Configuración de la autenticación nativa de OAuth 2.0](3.1-guia-del-administrador.md#configuración-de-la-autenticación-nativa-oauth-20) en la *Guía del administrador de IBM OpenPages*.

### Novedades de la versión 9.0.0.5

`Guía del desarrollador › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=new-whats-in-version-9005)

Las actualizaciones de la API REST V2 de ' IBM OpenPages® ' en la versión 9.0.0.5 se describen en la siguiente sección.

#### Puntos finales nuevos y obsoletos en la GRC REST API V2

La documentación de la API REST V2 de ' IBM OpenPages ' para la versión 9.0.0.4 incluía los puntos finales de Log Collector para Iniciar proceso de registro (`POST /v2/logs/collector`) y Obtener detalles del proceso para registros (`GET /v2/logs/collector/{process_id}`).

Dado que las definiciones de estos puntos finales no cumplen el estándar OpenAPI, algunas aplicaciones que utilizan el archivo ' `openapi.json` ' no pueden procesarlo. Para mejorar la conformidad de la API REST V2 OpenPages, los puntos finales se han dejado obsoletos y se han eliminado del archivo ' `openapi.json` ' y de la documentación de la versión 9.0.0.5.

Puede seguir utilizando los puntos finales obsoletos, pero considere la posibilidad de utilizar los nuevos puntos finales alternativos de 9.0.0.5:

- Utilice el punto final " `GET /v2/logs/collect/{process_id}` " en lugar del obsoleto punto final " `GET /v2/logs/collector/{process_id}` " para recuperar los detalles de los subprocesos que realizan el seguimiento de los servidores de aplicaciones en el clúster.
- Utilice el punto final " `POST /v2/logs/collect` " en lugar del obsoleto punto final " `POST /v2/logs/collector` " para iniciar el proceso de recopilación de registros.

Si ya está utilizando los puntos finales obsoletos, consulte [Deprecation of Log collector endpoints in the OpenPages REST API V2](https://www.ibm.com/support/pages/node/7177113).

Para obtener más información sobre ' IBM OpenPages ' REST API V2, consulte [la documentación del IBM® API Hub](https://developer.ibm.com/apis/catalog/openpages--ibm-openpages-with-watson-rest-api-v2).

### Novedades de la versión 9.0.0.4

`Guía del desarrollador › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=new-whats-in-version-9004)

Las actualizaciones en IBM OpenPages® REST API V2 en IBM OpenPages versión 9.0.0.4 se describen en la siguiente sección.

#### Nuevo parámetro de consulta en la API REST de GRC V2

Establezca un nuevo parámetro de consulta, `append_enum_vals`, en `true` para crear un valor de cadena enumerado si no existe. Puede utilizar `append_enum_vals` en los siguientes puntos finales:

- `POST /v2/contents`
- `PUT /v2/contents/{id}`

Para obtener más información, consulte la [IBM®](https://developer.ibm.com/apis/catalog/openpages--ibm-openpages-with-watson-rest-api-v2).

### Novedades de la versión 9.0.0.3

`Guía del desarrollador › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=new-whats-in-version-9003)

Las actualizaciones de la IBM OpenPages® API REST V2 en IBM OpenPages versión 9.0.0.3 se describen en las listas siguientes.

#### Nuevos puntos finales y métodos en la API REST de GRC V2

- Nuevo punto final `/fastmap/validate` para validar el contenido de una plantilla FastMap de XLSX.
- Nuevo punto final `/fastmap/import` para cargar el contenido de una plantilla FastMap de XLSX.
- Nuevo punto final `/logs/collector` con métodos para iniciar el proceso de recopilación de registros, obtener detalles de proceso de registros y recuperar registros como un archivo zip.
- Nuevo punto final `/configuration/locales` para obtener una lista de entornos locales soportados.
- Nuevo método `PUT` disponible para el punto final `/configuration/settings` para actualizar el valor de configuración especificado.

Para obtener más información, consulte la [documentación de IBM® API Hub](https://developer.ibm.com/apis/catalog/openpages--ibm-openpages-with-watson-rest-api-v2).

### Novedades de la versión 9.0.0.2

`Guía del desarrollador › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=new-whats-in-version-9002)

Las actualizaciones en IBM OpenPages® API REST V1 y V2 en IBM OpenPages versión 9.0.0.2 se describen en las listas siguientes.

Para obtener más información, consulte la publicación [*IBM OpenPages Guía de características nuevas*](2-caracteristicas-nuevas.md#características-nuevas).

#### API REST de GRC V2

- Se ha añadido un nuevo punto final `/scim/Bulk` para procesar la solicitud masiva.
- La documentación ahora está disponible para el punto final `/rules/run` .
- Contenido actualizado para ayudarle a identificar qué operaciones de API han desencadenado los sucesos en el servicio Activity Tracker .

Para obtener más información, consulte la [documentación de IBM® API Hub](https://developer.ibm.com/apis/catalog/openpages--ibm-openpages-with-watson-rest-api-v2).

#### API REST de GRC V1

- Ahora hay documentación disponible para el parámetro `fmt` para el punto final `/grc/api/search` .
- Contenido actualizado para el punto final `/grc/api/contents/{id}/document` con más detalles sobre las cabeceras necesarias.

Para obtener más información, consulte la[OpenPages API REST de GRCV1 Guia de referencia](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/GRC_REST_API.pdf) .

### Novedades de la versión 9.0.0.1

`Guía del desarrollador › Novedades` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=new-whats-in-version-9001)

Las actualizaciones en ' IBM OpenPages® REST API V2 en la versión 9.0.0.1 1 se describen en la siguiente lista.

Para obtener más información sobre el uso de REST API V2, consulte [la documentación de IBM® API Hub](https://developer.ibm.com/apis/catalog/openpages--ibm-openpages-with-watson-rest-api-v2).

#### Nuevo parámetro de consulta

- En el punto final " `GET /v2/contents/{id}` ", establezca el parámetro de consulta " `include_workflow` " en " `true` " para devolver la información de flujo de trabajo asociada.

#### Nuevos puntos finales

- Utilice " `GET /v2/workflows/instances/{id}` " para devolver datos de instancia de flujo de trabajo para el ID de instancia de flujo de trabajo especificado.
- Utilice ' `GET /v2/workflows/definitions/{id}` ' para devolver una definición de proceso de flujo de trabajo con el ID especificado.
- Utilice ' `GET /v2/workflows/definitions/version/{id}` ' para devolver una definición de proceso de flujo de trabajo con el ID de versión especificado.
- Utilice ' `GET /v2/workflows/definitions` ' para devolver todas las definiciones de procesos de flujo de trabajo.
- Utilice ' `POST /v2/workflows/instances/{id}/transition/{transition}` ' para realizar la transición de un objeto a un nuevo estado de flujo de trabajo basándose en el ID de instancia y el nombre de transición especificados.
- Utilice ' `GET /v2/workflows/instances/search` ' para devolver instancias de flujo de trabajo utilizando parámetros de búsqueda.
- Utilice ' `POST /v2/workflows/definitions/{id}/start/{grc_object_id}` ' para iniciar el flujo de trabajo. El parámetro ID especifica el flujo de trabajo y el ID del objeto especifica el objeto que pasa por el proceso de flujo de trabajo.

## Tareas de actualización para desarrolladores

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=guide-upgrade-tasks-developers)

OpenPages® 9.1.0 incluye una actualización a IBM® Semeru Runtimes 21. Además, la versión 9.1.0 elimina la dependencia del Cognos® SDK y la sustituye por una nueva envoltura del servicio proxy. Estos cambios requieren actualizaciones de su código personalizado.

La actualización de Java™ aporta ventajas sustanciales, como un mayor rendimiento, nuevas funciones del lenguaje y una mayor seguridad.

> **Nota** : IBM Cognos Analytics sigue funcionando en IBM SDK, Java Technology Edition 8.

### Actualice el código personalizado para utilizar IBM Semeru Runtimes

1. Reconstruya sus JAR personalizados con IBM Semeru Runtimes 21 para determinar si hay errores de tiempo de compilación causados por clases que ya no reciben soporte en IBM Semeru Runtimes 21. Si encuentra errores, actualice las dependencias.
2. Asegúrese de que todos los componentes de software personalizados cumplen las nuevas normas IBM Semeru Runtimes.

   Por ejemplo:

   - `javax.xml.transform.TransformerFactory` cambiado de `com.ibm.xtq.xslt.jaxp.compiler.TransformerFactoryImpl` a `com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl`.
   - `javax.xml.xpath.XPathFactory` cambiado de`org.apache.xpath.jaxp.XPathFactoryImp` a `com.sun.org.apache.xpath.internal.jaxp.XPathFactoryImp`
3. Si sus aplicaciones utilizan `Nashorn` para scripts, añada un motor externo JavaScript como `GraalVM` para manejar estos scripts. `Nashorn` se ha eliminado de IBM Semeru Runtimes 21.
4. Si tiene aplicaciones que dependen de formatos de zona horaria específicos, asegúrese de que utilizan los estándares internacionales compatibles con IBM Semeru Runtimes 21. Es posible que los formatos de zona horaria compatibles con IBM SDK, Java Technology Edition no sean interpretados correctamente por IBM Semeru Runtimes.
5. Si utiliza los siguientes paquetes internos, puede utilizar una opción de `jvm` para abrirlos y permitir el acceso sin restricciones en su entorno de aplicación:

   ```
   java.base/java.lang
   java.base/java.net
   java.base/java.io
   java.base/java.util
   java.base/java.nio
   java.base/java.security
   java.base/java.util.concurrent
   java.base/sun.security.x509
   java.base/sun.security.util
   java.base/sun.misc
   java.logging/java.util.logging
   java.xml/com.sun.org.apache.xerces.internal.parsers
   java.xml/com.sun.org.apache.xalan.internal.xsltc.trax
   java.xml/javax.xml.transform
   ```

### Actualizar el código personalizado para utilizar el nuevo Cognos envoltorio de servicio

En OpenPages 9.1.0, se eliminó la dependencia del Cognos Y los archivos JAR del SDK de Cognos (`cognosClient.jar` y `cognos-axis.jar`) ya no se incluyen en la ruta de la clase. Como resultado, todas las implementaciones personalizadas que anteriormente utilizaban Cognos SDK para migrar a una nueva envoltura de servicio proxy.

Para obtener más información sobre cómo adaptar su código, consulte [Uso de una clase Wrapper para la migración personalizada de código Cognos en OpenPages 9.1.](https://www.ibm.com/support/pages/node/7229267)

### Pasos posteriores a la actualización

Una vez completada la actualización a 9.1.0, puede eliminar IBM SDK, Java Technology Edition de los servidores de aplicaciones y del servidor de búsqueda global, si ninguna otra aplicación lo está utilizando. No elimine Java 8 de los servidores de informes.

## Extensiones

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=guide-extensions)

Mediante el uso de extensiones, puede configurar y gestionar conexiones con sistemas externos, enviar y recibir datos, y utilizar el marco Bring Your Own Model (BYOM). Le permite conectarse IBM OpenPages® a prácticamente cualquier terminal que exponga una API, lo que permite casos de uso avanzados como la ejecución de simulaciones FAIR o Monte Carlo, etc.

### Requisitos

Debe proporcionar una OpenAPI especificación (JSON, YAML o YML) para configurar las extensiones. La especificación de la API puede tener más de un servidor definido, pero debe haber al menos uno.

[Como servicio](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue) Si estás en IBM OpenPages as a Service, los dominios del servidor deben estar en la lista de permitidos aprobada:

> **Nota:** El comodín (*) indica cualquier subdominio.

```
*.azure.com
*.*.services.ai.azure.com
*.*.models.ai.azure.com
*.openai.azure.com
*.lambda-url.*.on.aws
*.googleapis.com
api.openai.com
api.llama.com
api.mistral.ai
```

La primera `GET` operación de una especificación se utiliza para probar la conectividad y la autenticación desde la interfaz de usuario de las extensiones. Asegúrese de que se especifiquen todos los valores predeterminados para los parámetros URL y ruta de la `GET` operación, ya que esos valores se utilizan durante las pruebas.

Sin una operación GET, no se puede probar una extensión, pero aún así se puede habilitar. Si hay algún problema de conectividad, lo sabrás en tiempo de ejecución.

Si se utiliza una extensión para integrar modelos de aprendizaje automático personalizados, la conectividad se puede probar mediante la interfaz de usuario de configuración de aprendizaje automático personalizado. En ese caso, no es necesaria una operación GET.

### Autenticación

Los tipos de autenticación admitidos son los siguientes:

- Autenticación básica
- Señal portadora
- Clave API (Se puede configurar para utilizar encabezados personalizados y prefijos de token)
- OAuth 2.0 (Actualmente restringido a IBM® las claves API de IAM y MCSP de )

### Especificación de muestra

Por ejemplo, aquí hay una especificación OpenAPI de watsonx.ai™ muestra que se puede utilizar con indicaciones o implementaciones en IBM Cloud o AWS Marketplace. Admite tanto la autenticación IAM como MCSP:

```
openapi: 3.0.0
info:
  title: IBM watsonx.ai API
  description: |
    API for IBM watsonx.ai, a generative AI service that enables developers to build enterprise-ready AI applications.
    This API allows you to interact with foundation models for text generation and inferencing.
  version: '2023-05-02'
  contact:
    name: IBM Cloud Support
    url: https://cloud.ibm.com/unifiedsupport/supportcenter
servers:
  - url: https://dev.aws.wxai.ibm.com
    description: watsonx.ai API server in Mumbai region
  - url: https://ap-south-1.aws.wxai.ibm.com
    description: watsonx.ai API server in Mumbai region 
  - url: https://us-east-1.aws.wxai.ibm.com
    description: watsonx.ai API server in us-east-1 (North Virginia)
  - url: https://{cluster_url}
    description: Custom cluster URL
    variables:
      cluster_url:
        default: ap-south-1.aws.wxai.ibm.com
        description: The cluster URL for your watsonx.ai instance

security:
  - IBMCloudAuth: []

paths:
  /ml/v1/deployments/{id_or_name}/text/generation:
    post:
      summary: Generate text using a foundation model 
      description: |
        This endpoint allows you to generate text using a deployed foundation model.
        You provide prompt variables and generation parameters, and the model returns generated text.
      operationId: generateTextStream
      parameters:
        - name: id_or_name
          in: path
          description: The ID or name of the deployed model
          required: true
          schema:
            type: string
            default: '5e3d3ed9-c757-4a41-990c-b5347fc2b7dd'
        - name: version
          in: query
          description: The API version
          required: true
          schema:
            type: string
            default: '2021-05-01'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TextGenerationRequest'
      responses:
        '200':
          description: Successful text generation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TextGenerationResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Model not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
               
  /ml/v1/text/generation:
    post:
      summary: Generate text using a specified model
      description: |
        This endpoint allows you to generate text using a specified model.
        You provide the model ID, input prompt, and generation parameters, and the model returns generated text.
      operationId: generateTextWithModel
      parameters:
        - name: version
          in: query
          description: The API version
          required: true
          schema:
            type: string
            default: '2023-05-02'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TextRequest'
      responses:
        '200':
          description: Successful text generation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TextGenerationResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Model not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
  
 
  /ml/v4/deployments/{deployment_id}:
    get:
      summary: Get deployment details
      description: |
        Retrieve information about a specific deployment by its ID.
        This endpoint returns details about the deployment including its configuration, status, and metadata.
      operationId: getDeployment
      parameters:
        - name: deployment_id
          in: path
          description: The ID of the deployment to retrieve
          required: true
          schema:
            type: string
            default: '76633500-9ad8-49fc-a794-69aab4e35dcc'
          example: "5e3d3ed9-c757-4a41-990c-b5347fc2b7dd"
        - name: space_id
          in: query
          description: The ID of the space containing the deployment
          required: true
          schema:
            type: string
            default: '7b71d5d5-8a86-4415-a0e5-b5e962328be6' 
          example: "7b71d5d5-8a86-4415-a0e5-b5e962328be6"
        - name: version
          in: query
          description: The API version
          required: true
          schema:
            type: string
            default: '2023-05-02'
      responses:
        '200':
          description: Successful retrieval of deployment details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Deployment not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

components:
  schemas:  
    TextGenerationRequest:
      type: object
      properties:
        parameters:
          type: object
          description: Parameters for text generation with prompt variables
          properties:
            prompt_variables:
              type: object
              description: Variables to be used in the prompt template
              additionalProperties:
                type: string
              example:
                Test: ""
            max_new_tokens:
              type: integer
              description: The maximum number of tokens to generate
              default: 100
              minimum: 1
              maximum: 2048
            time_limit:
              type: integer
              description: The time limit for generation in milliseconds
              default: 1000
              minimum: 100
            decoding_method:
              type: string
              description: The decoding method to use
              enum: [greedy, sample]
              default: greedy
            temperature:
              type: number
              description: Controls randomness in generation (higher = more random)
              minimum: 0
              maximum: 2
              default: 1.0
            top_p:
              type: number
              description: Nucleus sampling parameter
              minimum: 0
              maximum: 1
              default: 1.0
            top_k:
              type: integer
              description: Top-k sampling parameter
              minimum: 1
              default: 50
            repetition_penalty:
              type: number
              description: Penalty for repeating tokens
              minimum: 1.0
              default: 1.0
            stop_sequences:
              type: array
              description: Sequences that will stop generation when produced
              items:
                type: string
              example: ["\\n", "###"]
     
    TextGenerationResponse:
      type: object
      properties:
        model_id:
          type: string
          description: The ID of the model used for generation
        created_at:
          type: string
          format: date-time
          description: The timestamp when the response was created
        results:
          type: array
          description: The generated text results
          items:
            type: object
            properties:
              generated_text:
                type: string
                description: The generated text
              generated_token_count:
                type: integer
                description: The number of tokens generated
              input_token_count:
                type: integer
                description: The number of tokens in the input
              stop_reason:
                type: string
                description: The reason why generation stopped
                enum: [max_tokens, stop_sequence, time_limit]
    
    TextRequest:
      type: object
      required:
        - model_id
        - input
      properties:
        apikey:
          type: string
          description: API key for authentication
          example: "your-api-key-here"
        model_id:
          type: string
          description: The ID of the model to use for generation
          example: "meta-llama/llama-3-3-70b-instruct"
        input:
          type: string
          description: The input prompt for text generation
          example: ""
        parameters:
          type: object
          description: Parameters to control the text generation
          properties:
            decoding_method:
              type: string
              description: The decoding method to use
              enum: [greedy, sample]
              default: greedy
            max_new_tokens:
              type: integer
              description: The maximum number of tokens to generate
              default: 200
              minimum: 1
              maximum: 2048
              example: 200
            min_new_tokens:
              type: integer
              description: The minimum number of tokens to generate
              default: 0
              minimum: 0
              example: 0
            stop_sequences:
              type: array
              description: Sequences that will stop generation when produced
              items:
                type: string
              example: []
            repetition_penalty:
              type: number
              description: Penalty for repeating tokens
              minimum: 1.0
              default: 1.0
              example: 1
            time_limit:
              type: integer
              description: The time limit for generation in milliseconds
              default: 1000
              minimum: 100
              example: 1000
            temperature:
              type: number
              description: Controls randomness in generation (higher = more random)
              minimum: 0
              maximum: 2
              default: 1.0
            top_p:
              type: number
              description: Nucleus sampling parameter
              minimum: 0
              maximum: 1
              default: 1.0
            top_k:
              type: integer
              description: Top-k sampling parameter
              minimum: 1
              default: 50
        project_id:
          type: string
          description: The ID of the project
          example: "24d54a06-4324-493a-b800-aa4e25aeeda8"
        moderations:
          type: object
          description: Content moderation settings
          properties:
            hap:
              type: object
              description: Hate, Abuse, and Profanity moderation settings
              properties:
                input:
                  type: object
                  description: Input moderation settings for HAP
                  properties:
                    enabled:
                      type: boolean
                      description: Whether HAP input moderation is enabled
                      default: true
                    threshold:
                      type: number
                      description: Threshold for HAP detection
                      minimum: 0
                      maximum: 1
                      default: 0.5
                    mask:
                      type: object
                      description: Masking settings for detected content
                      properties:
                        remove_entity_value:
                          type: boolean
                          description: Whether to remove entity values
                          default: true
                output:
                  type: object
                  description: Output moderation settings for HAP
                  properties:
                    enabled:
                      type: boolean
                      description: Whether HAP output moderation is enabled
                      default: true
                    threshold:
                      type: number
                      description: Threshold for HAP detection
                      minimum: 0
                      maximum: 1
                      default: 0.5
                    mask:
                      type: object
                      description: Masking settings for detected content
                      properties:
                        remove_entity_value:
                          type: boolean
                          description: Whether to remove entity values
                          default: true
            pii:
              type: object
              description: Personally Identifiable Information moderation settings
              properties:
                input:
                  type: object
                  description: Input moderation settings for PII
                  properties:
                    enabled:
                      type: boolean
                      description: Whether PII input moderation is enabled
                      default: true
                    threshold:
                      type: number
                      description: Threshold for PII detection
                      minimum: 0
                      maximum: 1
                      default: 0.5
                    mask:
                      type: object
                      description: Masking settings for detected content
                      properties:
                        remove_entity_value:
                          type: boolean
                          description: Whether to remove entity values
                          default: true
                output:
                  type: object
                  description: Output moderation settings for PII
                  properties:
                    enabled:
                      type: boolean
                      description: Whether PII output moderation is enabled
                      default: true
                    threshold:
                      type: number
                      description: Threshold for PII detection
                      minimum: 0
                      maximum: 1
                      default: 0.5
                    mask:
                      type: object
                      description: Masking settings for detected content
                      properties:
                        remove_entity_value:
                          type: boolean
                          description: Whether to remove entity values
                          default: true
            granite_guardian:
              type: object
              description: Granite Guardian moderation settings
              properties:
                input:
                  type: object
                  description: Input moderation settings for Granite Guardian
                  properties:
                    enabled:
                      type: boolean
                      description: Whether Granite Guardian input moderation is enabled
                      default: false
                    threshold:
                      type: number
                      description: Threshold for detection
                      minimum: 0
                      maximum: 1
                      default: 1
    InferenceRequest:
      type: object
      required:
        - input
      properties:
        apikey:
          type: string
          description: API key for authentication
          example: "your-api-key-here"
        input:
          type: string
          description: The input data for inference
          example: "Classify the sentiment of this text: I really enjoyed the movie."
        parameters:
          type: object
          description: Parameters to control the inference
          properties:
            max_new_tokens:
              type: integer
              description: The maximum number of tokens to generate
              default: 100
              minimum: 1
              maximum: 2048
              example: 100
            time_limit:
              type: integer
              description: The time limit for inference in milliseconds
              default: 1000
              minimum: 100
              example: 1000
            task_type:
              type: string
              description: The type of inference task
              enum: [classification, question_answering, summarization, translation]
              example: "classification"
            return_options:
              type: object
              description: Options for what to return in the response
              properties:
                include_input:
                  type: boolean
                  description: Whether to include the input in the response
                  default: false
                include_intermediate_results:
                  type: boolean
                  description: Whether to include intermediate results
                  default: false
    
    InferenceResponse:
      type: object
      properties:
        model_id:
          type: string
          description: The ID of the model used for inference
        created_at:
          type: string
          format: date-time
          description: The timestamp when the response was created
        results:
          type: array
          description: The inference results
          items:
            type: object
            properties:
              result:
                type: string
                description: The inference result
              confidence:
                type: number
                description: Confidence score for the result
                minimum: 0
                maximum: 1
              processing_time:
                type: integer
                description: Processing time in milliseconds
    DeploymentListResponse:
      type: object
      properties:
        total_count:
          type: integer
          description: Total number of deployments matching the criteria
          example: 5
        resources:
          type: array
          description: Array of deployment resources
          items:
            $ref: '#/components/schemas/DeploymentResponse'
    
    DeploymentResponse:
      type: object
      properties:
        metadata:
          type: object
          description: Metadata about the deployment
          properties:
            id:
              type: string
              description: The unique identifier of the deployment
              example: "12345678-1234-1234-1234-123456789abc"
            name:
              type: string
              description: The name of the deployment
              example: "My Model Deployment"
            description:
              type: string
              description: Description of the deployment
            created_at:
              type: string
              format: date-time
              description: Timestamp when the deployment was created
            modified_at:
              type: string
              format: date-time
              description: Timestamp when the deployment was last modified
            space_id:
              type: string
              description: The ID of the space containing the deployment
              example: "aa6dc728-958e-42b7-acdf-d403e16d1e9e"
            owner:
              type: string
              description: The owner of the deployment
        entity:
          type: object
          description: The deployment entity details
          properties:
            asset:
              type: object
              description: Information about the deployed asset
              properties:
                id:
                  type: string
                  description: The ID of the deployed model or asset
                name:
                  type: string
                  description: The name of the deployed model or asset
            deployed_asset_type:
              type: string
              description: The type of asset being deployed
              example: "model"
            hardware_spec:
              type: object
              description: Hardware specifications for the deployment
              properties:
                id:
                  type: string
                  description: Hardware specification ID
                name:
                  type: string
                  description: Hardware specification name
                num_nodes:
                  type: integer
                  description: Number of nodes
            online:
              type: object
              description: Online deployment configuration
              properties:
                parameters:
                  type: object
                  description: Deployment parameters
            status:
              type: object
              description: Current status of the deployment
              properties:
                state:
                  type: string
                  description: The current state of the deployment
                  enum: [initializing, updating, ready, failed]
                  example: "ready"
                message:
                  type: string
                  description: Status message
    
    ErrorResponse:
      type: object
      properties:
        status_code:
          type: integer
          description: The HTTP status code
        error:
          type: string
          description: Error type
        message:
          type: string
          description: Error message
        trace_id:
          type: string
          description: Trace ID for debugging
  
  securitySchemes:
    IBMAuthMCSP:
      type: oauth2
      description: |
        Authentication for watsonx.ai API requires an IBM Cloud API key.
        The API key must be included in the request body as: {"apikey": "your-api-key-value"}
        
        To obtain an API key:
        1. Create an API key in IBM Cloud
        2. Include the API key in the request body of each API call
      flows:
        clientCredentials:
          tokenUrl: https://iam.platform.saas.ibm.com/siusermgr/api/1.0/apikeys/token
          scopes: {}
      x-ibm-iam-type: MCSP
    
    IBMCloudIAM:
      type: oauth2
      description: |
        Authentication for watsonx.ai API using IBM Cloud IAM.
        This scheme exchanges an API key for a bearer token using form-encoded credentials.
        
        The token endpoint expects a form-encoded body with:
        - grant_type: urn:ibm:params:oauth:grant-type:apikey
        - apikey: your-api-key-value
        
        To use this authentication:
        1. Create an API key in IBM Cloud
        2. Exchange it for a bearer token via the token endpoint
        3. Use the bearer token in the Authorization header
      flows:
        clientCredentials:
          tokenUrl: https://iam.cloud.ibm.com/identity/token
          scopes: {}
      x-ibm-iam-type: IBM

### Made with Bob
```

## Webhooks

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=guide-webhooks)

Webhooks permite la comunicación en tiempo real basada en eventos entre IBM OpenPages® y sistemas externos. Permite a desarrolladores y administradores crear soluciones con mayor capacidad de respuesta e interconectadas mediante OpenPages.

Puede configurar webhooks salientes que activen automáticamente las llamadas de retorno a HTTPS cuando se produzcan eventos específicos en los tipos de objetos a los que se haya suscrito.

### Requisitos de los puntos finales

Los puntos finales deben hacer lo siguiente:

- Habilitar SSL ( HTTPS )
- Aceptar solicitudes POST
- Gestión de eventos JSON
- Responder a carga útil JSON vacía (para probar conexiones)

[Como servicio](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue) Si está en IBM OpenPages as a Service, el dominio del endpoint debe estar en la lista de permitidos aprobada:

> **Nota:** El comodín (*) denota cualquier subdominio.

```
*.azure.com
*.lambda-url.*.on.aws
*.cloud.ibm.com
*.*.cloud.ibm.com
*.*.*.cloud.ibm.com 
*.amazonaws.com
*.*.amazonaws.com
*.*.*.amazonaws.com
```

### Autenticación

Los tipos de autenticación admitidos son los siguientes:

- Autenticación básica
- Señal portadora
- Clave API (Puede configurarse para utilizar prefijos de encabezado y token personalizados)
- OAuth 2.0 (Actualmente restringido a las claves IBM® API de IAM de.)

### Suscripciones de sucesos

Para los tipos de objeto que especifique, puede suscribirse a los siguientes tipos de eventos:

- `create`: Publicado cuando se crea un nuevo objeto.
- `update`: Publicado cuando se modifica un objeto existente.
- `delete`: Publicado cuando se elimina un objeto.
- `associate`: Publicado cuando un objeto está asociado a un objeto padre.
- `disassociate`: Publicado cuando se elimina un objeto de un objeto padre.

**Estructura común de los actos**

La carga útil del evento está en formato JSON y tiene una estructura externa común a todos los tipos de eventos con estos miembros notables:

- `events[]`: Matriz de elementos de eventos (actualmente uno por POST).
- `eventObject.action`: El verbo de evento, es decir, el evento que ocurrió: (`create`, `update`, `delete`, `associate`, `disassociate`).
- `eventObject.message.actor`: Contexto de usuario (`iam_id`, `user_id`, `user_name`), es decir, los datos del usuario que realizó la acción que desencadenó el evento.
- `eventObject.message.publishedDate`: Fecha y hora de publicación del evento, que muestra la fecha y hora en que el evento se publicó en la cola.
- `eventObject.message.event` Repite el verbo del evento, es decir, el nombre del evento ocurrido: (`create`, `update`, `delete`, `associate`, `disassociate`).
- `eventObject.objectType`: Nombre del sistema del tipo de objeto OpenPages en el modelo de objetos (por ejemplo, `Register`).
- `eventObject.type`: Siempre `GRC_OBJECT`, indicando un evento de datos.
- `routingKey`: Describe información clave sobre el evento. Puedes utilizarlo para varios propósitos de filtrado, por ejemplo, como un filtro rápido desde dentro del webhook para decidir si procesar un evento. La clave de enrutamiento tiene el siguiente formato:

  ```
  <version of event>.account.<account ID>.instance.<OpenPages instance
        ID>.type.GRC_OBJECT.parent.<parent ID>.object.<Object Type>.id.<Object
      ID>.<Event>
  ```

  A continuación se describen las distintas partes de la tecla de enrutamiento:

  - \<versión del evento>: El valor actual es siempre `v1`.
  - \<identificador de cuenta>: El identificador de cuenta bajo el que se despliega el servicio OpenPages , generalmente aplicable a IBM OpenPages as a Service. En el caso de las instancias locales y alojadas en la nube, puede estar en blanco.
  - \<ID de instanciaOpenPages >: En IBM OpenPages as a Service este es el ID de instancia OpenPages dentro de la cuenta. En el caso de las instancias locales o alojadas en la nube, se trata del nombre exclusivo asignado al servidor OpenPages . Puede utilizarse para verificar que el evento recibido procede de la fuente del servidor esperada.
  - \<ID padre>: El ID padre del objeto en el evento. Puede utilizarse para decidir si se gestiona el evento. Por ejemplo, si el endpoint sólo está interesado en objetos de una entidad de negocio específica, puede ignorar eventos de objetos de otras entidades de negocio. Tenga en cuenta que el ID de padre puede estar vacío para el evento `create` ya que aún no se ha asignado un padre para el objeto.
  - \<Tipo de objeto>: El tipo de objeto.
  - \<ID del objeto>: El ID del objeto para el que se generó el evento.

Los valores de otros objetos, por ejemplo, el objeto `details` , diferirán en función del evento.

A continuación se muestra un ejemplo de carga útil que ilustra la estructura común de eventos:

> **Nota:** Los corchetes y el texto dentro de ellos (`<xyz>`) representan valores de marcador de posición utilizados con fines ilustrativos.

```json
{
    "events": [
        {
            "eventObject": {
                "action": "<Event>",
                "message": {
                    "actor": {
                        "iam_id": "<User IAM ID>",
                        "user_id": "<User ID>",
                        "user_name": "<User name>"
                    },
                    "details": {
                        <Event-specific event information>
                    },
                    "event": "<Event name>",
                    "publishedDate": "<Publication date>"
                },
                "objectType": "<object type>",
                "type": "GRC_OBJECT"
            },
            "routingKey": "<version of event>.account.<account ID>.instance.<OpenPages instance ID>.type.GRC_OBJECT.parent.<parent ID>.object.<Object Type>.id.<Object ID>.<Event>""
        }
    ]
}
```

Aquí están los ejemplos de carga útil para cada tipo de evento específico:

Crear carga útil de muestra de eventos

```json
{
    "events": [
        {
            "eventObject": {
                "action": "create",
                "message": {
                    "actor": {
                        "iam_id": "john.doe@example.com",
                        "user_id": "1506",
                        "user_name": "john.doe@example.com"
                    },
                    "details": {
                        "last_modification": "2024-02-21 15:26:13.000Z",
                        "object_id": "25502",
                        "object_name": "Use Case",
                        "object_path": "/_op_sox/Project/Default/ICDocumentation/Registers/ABC Financial Institution/Use Case.txt"
                    },
                    "event": "create",
                    "publishedDate": "2024-02-21 15:26:13.644Z"
                },
                "objectType": "Register",
                "type": "GRC_OBJECT"
            },
            "routingKey": "v1.account.aa9999999a9a9999a9a9aaa9aaa9a999a.instance.aaa99a9a-99a9-9999-9999-a99aafa99aa.type.GRC_OBJECT.parent..object.Register.id.25502.create"
        }
    ]
}
```

Actualizar la carga útil de la muestra de eventos

```json
{
    "events": [
        {
            "eventObject": {
                "action": "update",
                "message": {
                    "actor": {
                        "iam_id": "john.doe@example.com",
                        "user_id": "1506",
                        "user_name": "john.doe@example.com"
                    },
                    "details": {
                        "last_modification": "2024-02-21 15:26:13.000Z",
                        "object_id": "25502",
                        "object_name": "Use Case",
                        "object_path": "/_op_sox/Project/Default/ICDocumentation/Registers/ABC Financial Institution/Use Case.txt",
                        "updated_fields": [
                            "MRG-AIFacts-ModelUseCase:Status"
                        ]
                    },
                    "event": "update",
                    "publishedDate": "2024-02-21 15:26:14.607Z"
                },
                "objectType": "Register",
                "type": "GRC_OBJECT"
            },
            "routingKey": "v1.account.aa9999999a9a9999a9a9aaa9aaa9a999a.instance.aaa99a9a-99a9-9999-9999-a99aafa99aa.type.GRC_OBJECT.parent..object.Register.id.25502.update"
        }
    ]
}
```

Borrar la carga útil de la muestra de eventos

```json
{
    "events": [
        {
            "eventObject": {
                "action": "delete",
                "message": {
                    "actor": {
                        "iam_id": "john.doe@example.com",
                        "user_id": "1506",
                        "user_name": "john.doe@example.com"
                    },
                    "details": {
                        "last_modification": "2024-02-21 15:31:12.678Z",
                        "object_id": "25502",
                        "object_name": "Use Case",
                        "object_path": "/_op_sox/Project/Default/ICDocumentation/Registers/ABC Financial Institution"
                    },
                    "event": "delete",
                    "publishedDate": "2024-02-21 15:31:12.683Z"
                },
                "objectType": "Register",
                "type": "GRC_OBJECT"
            },
            "routingKey": "v1.account.aa9999999a9a9999a9a9aaa9aaa9a999a.instance.aaa99a9a-99a9-9999-9999-a99aafa99aa.type.GRC_OBJECT.parent..object.Register.id.25502.delete"
        }
    ]
}
```

Asociar la carga útil de la muestra de eventos

```json
{
    "events": [
        {
            "eventObject": {
                "action": "associate",
                "message": {
                    "actor": {
                        "iam_id": "john.doe@example.com",
                        "user_id": "1506",
                        "user_name": "john.doe@example.com"
                    },
                    "details": {
                        "last_modification": "2024-02-21 15:26:13.000Z",
                        "object_id": "25502",
                        "object_name": "Use Case",
                        "object_path": "/_op_sox/Project/Default/ICDocumentation/Registers/ABC Financial Institution",
                        "parent_id": "7236",
                        "parent_name": "ABC Financial Institution",
                        "parent_path": "/_op_sox/Project/Default/BusinessEntity/ABC Financial Institution",
                        "parent_type": "SOXBusEntity"
                    },
                    "event": "associate",
                    "publishedDate": "2024-02-21 15:26:13.796Z"
                },
                "objectType": "Register",
                "type": "GRC_OBJECT"
            },
            "routingKey": "v1.account.aa9999999a9a9999a9a9aaa9aaa9a999a.instance.aaa99a9a-99a9-9999-9999-a99aafa99aa.type.GRC_OBJECT.parent.SOXBusEntity.object.Register.id.25502.associate"
        }
    ]
}
```

Desasociar la carga útil de la muestra de eventos

```json
{
    "events": [
        {
            "eventObject": {
                "action": "disassociate",
                "message": {
                    "actor": {
                        "iam_id": "OpenPagesAdministrator",
                        "user_id": "6",
                        "user_name": "OpenPagesAdministrator"
                    },
                    "details": {
                        "last_modification": "2024-02-02 17:00:49.000Z",
                        "object_id": "6338",
                        "object_name": "MOD-00002",
                        "object_path": "/_op_sox/Project/Default/ICDocumentation/Models/High Oaks Bank/North America/Corporate Banking",
                        "parent_id": "6291",
                        "parent_name": "Loan Automation Use Case",
                        "parent_path": "/_op_sox/Project/Default/ICDocumentation/Registers/High Oaks Bank/North America/Corporate Banking",
                        "parent_type": "Register"
                    },
                    "event": "disassociate",
                    "publishedDate": "2024-02-21 15:34:30.010Z"
                },
                "objectType": "Model",
                "type": "GRC_OBJECT"
            },
            "routingKey": "v1.account.aa9999999a9a9999a9a9aaa9aaa9a999a.instance.aaa99a9a-99a9-9999-9999-a99aafa99aa.type.GRC_OBJECT.parent.Register.object.Model.id.6338.disassociate"
        }
    ]
}
```

### Ejemplo de escenario de devolución de llamada

Consideremos un escenario en el que un usuario modifica un objeto de riesgo en OpenPages, provocando un cambio en su calificación de riesgo. Esta alteración puede tener implicaciones significativas para el cumplimiento, la preparación para auditorías o los umbrales operativos.

Mediante el soporte de webhook, OpenPages puede notificar instantáneamente a cualquier sistema externo que esté suscrito a este evento. Esta alerta en tiempo real permite a los sistemas externos responder de forma proactiva. Un sistema externo puede recuperar todos los detalles del objeto a través de la API OpenPages y realizar acciones inteligentes como:

- Reasignar el riesgo a otro propietario
- Escalándolo al equipo de cumplimiento
- Activación de flujos de trabajo externos para acciones posteriores

A continuación se muestra un ejemplo de carga útil de eventos para el escenario descrito anteriormente:

```json
{
  "action":"update",
  "type":"GRC_OBJECT",
  "objectType":"SOXRisk",
  "message":{
    "event":"update",
    "publishedDate":"2025-09-25 02:14:26.797Z",
    "details":{
      "object_id":"9032",
      "object_name":"RB-01-Risk00190",
      "object_path":"/_op_sox/Project/Default/ICDocumentation/Risks/Global Financial Services/North America/Retail Banking/RB-01-Risk00190.txt",
      "updated_fields":[
        "OPSS-Risk-Qual:Inherent Likelihood",
        "OPSS-Risk-Qual:Inherent Risk Rating",
        "OPSS-Risk-Quant:Inherent Frequency",
        "OPSS-Risk-Quant:Inherent Risk Exposure"
      ],
      "last_modification":"2025-08-30 08:58:48.000Z"
    },
    "actor":{
      "iam_id":"user1@ibm.com",
      "user_id":"2087",
      "user_name":"user1"
    }
  },
  "version":"9.1.2"
}
```

### Ejemplo de implementación de un webhook listener en Node.js

El código siguiente muestra cómo se puede aprovechar un evento de webhook para volver a llamar a la API IBM OpenPages , recuperar detalles del objeto y desencadenar acciones posteriores, como enviar alertas, actualizar sistemas externos, orquestar flujos de trabajo, etc.

```
const fs = require('fs');
const http = require('http');
const https = require('https');
const express = require('express');
const axios = require('axios');
const app = express();
const PORT_HTTP = 3000;
const PORT_HTTPS = 3443;
const BEARER_TOKEN = 'your-token'; // ideally from env in production
const IBM_CLOUD_API_KEY = 'your-ibm-cloud-api-key'; // Replace with actual API key in production
const OPENPAGES_BASE_URL = 'https://your-openpages-instance.com'; // Replace with actual OpenPages URL
const IS_SAAS = true; // Set to true for SaaS environment, false for on-premise
const OPENPAGES_USERNAME = 'your-op-username'; // Only used for on-premise environments
const OPENPAGES_PASSWORD = 'your-op-password'; // Only used for on-premise environments

// SSL cert
const sslOptions = {
  key: fs.readFileSync('./ssl/key.pem'),
  cert: fs.readFileSync('./ssl/cert.pem'),
};

// Parse JSON bodies
app.use(express.json());

function bearerTokenMiddleware(req, res, next) {
  const authHeader = req.headers['authorization'];

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ message: 'Missing or invalid Authorization header' });
  }

  const token = authHeader.split(' ')[1];
  if (token !== BEARER_TOKEN) {
    return res.status(403).json({ message: 'Forbidden: Invalid token' });
  }

  next();
}

// 🔓 Public route (GET only)
app.get('/', (req, res) => {
  res.send('Welcome to the public route 👋');
});

app.route('/bearer-protected')
  .all(bearerTokenMiddleware)
  .get((req, res) => {
    res.send('🔐 GET: Bearer token accepted.');
  })
  .post(async (req, res) => {
    try {
      console.log('Received webhook with Bearer token authentication:', JSON.stringify(req.body));
      
      // Extract object ID from the webhook payload
      const objectId = extractObjectIdFromWebhook(req.body);
      
      // If objectId is null, respond with success but skip OpenPages API call
      if (objectId === null) {
        console.log('No valid object ID found in webhook payload, skipping OpenPages API call');
        return res.status(200).json({
          success: true,
          message: '🔐 POST: Bearer token accepted but no valid object ID found',
          webhookData: req.body
        });
      }
      
      console.log(`Extracted object ID: ${objectId}`);
      
      // Get the object details from OpenPages
      const objectData = await getOpenPagesObject(objectId);
      
      // Process the object data
      console.log('Successfully retrieved object data from OpenPages');
      
      res.status(200).json({
        success: true,
        message: '🔐 POST: Bearer token accepted and processed OpenPages object',
        objectId: objectId,
        webhookData: req.body,
        openPagesData: objectData
      });
    } catch (error) {
      console.error('Error processing webhook with Bearer token:', error.message);
      res.status(500).json({
        success: false,
        message: error.message,
        webhookData: req.body
      });
    }
  });

// Function to get authentication credentials
async function getAuthCredentials() {
  if (IS_SAAS) {
    // SaaS environment: Use IAM token authentication
    try {
      console.log('Using SaaS authentication method (IAM token)');
      const response = await axios({
        method: 'post',
        url: 'https://iam.test.cloud.ibm.com/identity/token',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: new URLSearchParams({
          'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
          'apikey': IBM_CLOUD_API_KEY
        }).toString()
      });
      
      return {
        type: 'bearer',
        token: response.data.access_token
      };
    } catch (error) {
      console.error('Error getting IAM token:', error.message);
      if (error.response) {
        console.error('Response data:', error.response.data);
        console.error('Response status:', error.response.status);
      }
      throw new Error('Failed to retrieve IAM token');
    }
  } else {
    // On-premise environment: Use basic authentication
    console.log('Using on-premise authentication method (Basic Auth)');
    return {
      type: 'basic',
      username: OPENPAGES_USERNAME,
      password: OPENPAGES_PASSWORD
    };
  }
}

// Helper function to extract object ID from webhook request body
// Returns null if the object ID cannot be extracted
function extractObjectIdFromWebhook(body) {
  try {
    // Try the new structure from the example
    // {"events":[{"eventMessage":{"message":{"details":{"object_id":"14502"}}}}]}
    if (body && body.events && body.events.length > 0 &&
        body.events[0].eventMessage &&
        body.events[0].eventMessage.message &&
        body.events[0].eventMessage.message.details &&
        body.events[0].eventMessage.message.details.object_id) {
      const objectId = body.events[0].eventMessage.message.details.object_id;
      console.log(`Found object ID ${objectId} in events array webhook payload structure`);
      return objectId;
    }
    
    // First, try the direct structure from the example
    // {"action":"create","type":"GRC_OBJECT","objectType":"SOXBusEntity","message":{"details":{"object_id":"13002"}}}
    if (body && body.message && body.message.details && body.message.details.object_id) {
      const objectId = body.message.details.object_id;
      console.log(`Found object ID ${objectId} in direct webhook payload structure`);
      return objectId;
    }
    
    // Then try the nested eventObject structure we initially expected
    // {"eventObject":{"message":{"details":{"object_id":"25502"}}}}
    if (body && body.eventObject && body.eventObject.message &&
        body.eventObject.message.details && body.eventObject.message.details.object_id) {
      const objectId = body.eventObject.message.details.object_id;
      console.log(`Found object ID ${objectId} in nested eventObject webhook payload structure`);
      return objectId;
    }
    
    // If we reach here, we couldn't find the object ID in any expected structure
    console.log('Object ID not found in webhook payload, returning null');
    console.log('Payload structure:', JSON.stringify(body, null, 2));
    return null;
  } catch (error) {
    console.error('Error extracting object ID:', error.message);
    return null;
  }
}

// Function to get OpenPages object
async function getOpenPagesObject(objectId) {
  try {
    // Get authentication credentials
    const auth = await getAuthCredentials();
    
    // Create https agent that ignores SSL certificate validation
    const httpsAgent = new https.Agent({
      rejectUnauthorized: false // Ignore SSL certificate validation
    });
    
    // Set up request configuration
    const requestConfig = {
      method: 'get',
      url: `${OPENPAGES_BASE_URL}/opgrc/api/v2/contents/${objectId}`,
      headers: {
        'Content-Type': 'application/json',
        'User-Agent': 'NodeJS/Axios'
      },
      httpsAgent: httpsAgent, // Add the https agent to ignore SSL certificate validation
      validateStatus: function (status) {
        return status >= 200 && status < 500; // Accept all status codes less than 500
      }
    };
    
    // Apply the appropriate authentication method
    if (auth.type === 'bearer') {
      requestConfig.headers['Authorization'] = `Bearer ${auth.token}`;
    } else if (auth.type === 'basic') {
      // For basic auth with OpenPages
      const base64Auth = Buffer.from(`${auth.username}:${auth.password}`).toString('base64');
      requestConfig.headers['Authorization'] = `Basic ${base64Auth}`;
    }
    
    console.log(`Making API call to OpenPages: ${requestConfig.url}`);
    
    // Call OpenPages API with the appropriate authentication
    const response = await axios(requestConfig);
    
    if (response.status >= 400) {
      throw new Error(`OpenPages API returned status code ${response.status}`);
    }
    
    return response.data;
  } catch (error) {
    console.error('Error getting OpenPages object:', error.message);
    if (error.response) {
      console.error('Response data:', error.response.data);
      console.error('Response status:', error.response.status);
    }
    throw new Error(`Failed to retrieve OpenPages object with ID: ${objectId}`);
  }
}

// HTTPS server
https.createServer(sslOptions, app).listen(PORT_HTTPS, () => {
  console.log(`✅ HTTPS server running at https://localhost:${PORT_HTTPS}`);
});

// HTTP → HTTPS redirect
http.createServer((req, res) => {
  const host = req.headers['host'].replace(/:\d+$/, `:${PORT_HTTPS}`);
  res.writeHead(301, { Location: `https://${host}${req.url}` });
  res.end();
}).listen(PORT_HTTP, () => {
  console.log(`ℹ️  HTTP redirect server on http://localhost:${PORT_HTTP}`);
});
```

## API Java deIBM OpenPages GRC

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=guide-java-api)

Utilice la API deIBM OpenPages GRC Java™ para crear soluciones personalizadas en la aplicación OpenPages® .

Para ver la documentación de IBM OpenPages GRC Java API , descargue los [Javadocs comprimidos](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/op_sdk_javadoc_9.1.zip).

Para utilizar IBM OpenPages GRC Java API en soluciones personalizadas, debe ser un desarrollador Java y estar familiarizado con las infraestructuras Java EE , Spring REST, XML y conceptos de base de datos relacional.

La API de Java deIBM OpenPages GRC da soporte a ayudantes y desencadenantes JSP que se desarrollan utilizando Java y se compilan y despliegan en un jar de extensión estándar (`openpages-ext.jar`.)

Para iniciar una sesión con la API Java deIBM OpenPages GRC, cree un contexto para el usuario actual.

Para crear un nuevo contexto en el que ya tenga una sesión existente, utilice los mandatos siguientes.

```
Context context = new Context();
//add connection with an existing OpenpagesSession
context.put(Context.SERVICE_SESSION,openpagesSession);
```

## IBM OpenPages API REST GRC V2

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=guide-rest-api-v2)

Utilice esta versión de la IBM OpenPages GRC REST API para nuevas implementaciones.

La IBM OpenPages GRC REST API proporciona acceso a IBM OpenPages® datos y metadatos. Esta API centrada en datos se especifica en términos de recursos, sus URI y acciones que se pueden realizar en estos URI.

Para obtener información sobre cómo utilizar la IBM OpenPages GRC REST API V2, consulte la [documentación de referencia](https://developer.ibm.com/apis/catalog/openpages--ibm-openpages-with-watson-rest-api-v2).

### Requisitos previos

Para utilizar la API REST deIBM OpenPages GRC de forma eficaz, asegúrese de estar familiarizado con los siguientes temas:

- IBM OpenPages
- Servicios web como ASDL y REST
- JSON de lenguaje de scripts HTML y JavaScript
- Lenguajes de programación y entornos de desarrollo integrado (IDE), como el lenguaje de programación Java™ y el Eclipse IDE, o el lenguaje de programación C# y el IDE de Microsoft Visual Studio.

### Soporte de SCIM 2.0

IBM OpenPages GRC REST API V2 cumple la especificación SCIM 2.0 para el aprovisionamiento y la gestión de usuarios.

Para más información, consulte [Sistema de gestión de identidades entre dominios](https://www.ibm.com/links?url=https%3A%2F%2Fwww.rfc-editor.org%2Frfc%2Frfc7644).

### Rendimiento

Puede añadir índices para mejorar el rendimiento de la ejecución de una consulta.

Para obtener más información, consulte [Valores de la carpeta Esquema de elaboración de informes](3.3-guia-del-administrador.md#valores-de-la-carpeta-esquema-de-elaboración-de-informes).

### Seguridad y autenticación

La autenticación se delega en el IBM® WebSphere® Application Server, por lo que cada punto de entrada no necesita verificar el token de autenticación.

Utilice autenticación básica, autenticación de certificado de cliente y autenticación OAuth 2.0 0 con ' IBM OpenPages ' en las instalaciones o IBM OpenPages en Cloud.

Utilice la autenticación basada en señal con IBM OpenPages for IBM Cloud Pak for Data.

#### Autenticación básica

La autenticación básica se configura de forma predeterminada a través del servidor de aplicaciones OpenPages . El esquema de autorización básico sigue la especificación RFC 2617. El cliente implementa el esquema básico de autorización enviando una cabecera de solicitud HTTP. La autorización básica contiene el texto `Basic` seguido del nombre de usuario, dos puntos (:) y la contraseña. El texto debe estar codificado en Base64. Por ejemplo, para enviar el nombre de usuario `Aladdin` y la contraseña `open sesame`, utilice el siguiente campo de cabecera HTTP :

```
Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
```

La API REST GRC de OpenPages se ajusta al principio de falta de estado de los sistemas RESTful, por lo que cada solicitud realizada debe proporcionar las credenciales del usuario. La autenticación básica se considera segura si se utiliza con algún sistema seguro externo como, por ejemplo, SSL. Para una mayor seguridad, asegúrese de que los clientes sólo envían credenciales sin cifrar y que las solicitudes se envían a través de HTTPS.

#### Autenticación de certificado de cliente

OpenPages ofrece autenticación de certificado de cliente con WebSphere Liberty Profile (WLP).

La autenticación de certificado de cliente es un método de autenticación basado en certificado mutuo, donde el cliente proporciona su certificado de cliente al servidor para probar su identidad. El servidor sólo permite solicitudes después de autenticar el cliente. El cliente debe proporcionar un certificado de clave pública que identifique quién es el cliente. Para que el cliente se autentique, el servidor debe confiar en el certificado. WLP se puede configurar para que confíe en cualquier certificado de cliente añadiéndolo manualmente a su almacén de claves de confianza. WLP también puede confiar en el certificado de cliente si otro certificado de confianza firma digitalmente el certificado de cliente. Por ejemplo, WLP puede confiar en el certificado del cliente si una autoridad de certificación SSL conocida, como DigiCert, emite un certificado que firma el certificado del cliente para [ibm.com®.](https://www.ibm.com/links?url=http%3A%2F%2Fibm.com%2F)

Este tráfico se realiza a través de SSL HTTPS ), lo que garantiza la seguridad de la conexión y el cifrado. Además, el control a nivel de API proporciona una opción para configurar el modelo de seguridad para permitir que solo determinados clientes preaprobados realicen solicitudes a la API REST. Para permitir que la API REST de IBM OpenPages GRC utilice la autenticación de cliente en lugar de la autenticación básica, debe configurar IBM WebSphere Liberty. Para obtener información sobre cómo configurar una aplicación en IBM WebSphere Liberty para utilizar autenticación de certificado de cliente, consulte [Cómo configurar Liberty para utilizar autenticación basada en certificados](https://www.ibm.com/support/pages/how-setup-liberty-use-certificate-based-authentication).

La integración de OpenPages con la seguridad de IBM WebSphere Liberty requiere cambios de configuración. Para más información, consulte [Integración de OpenPages con la seguridad de IBM WebSphere Liberty](#ibm-openpages-api-rest-grc-v2).

#### Autenticación de señal

La autenticación de señal se configura de forma predeterminada a través del servidor de aplicaciones de OpenPages en IBM OpenPages for IBM Cloud Pak for Data. El token es un Microprofile JSON Web Token (MP-JWT) como se describe en [Eclipse MicroProfile Interoperable JWT RBAC](https://www.ibm.com/links?url=https%3A%2F%2Fdownload.eclipse.org%2Fmicroprofile%2Fmicroprofile-jwt-auth-1.2%2Fmicroprofile-jwt-auth-spec-1.2.html). El cliente envía una cabecera de autorización de solicitud HTTP que comienza con el texto `Bearer` seguido de un token MP-JWT válido como `Authorization: Bearer <Valid MP-JWT Token>`.

Para obtener un token válido, utilice una de las API de autenticación descritas en [Generación de un token de autorización o clave API](https://www.ibm.com/docs/en/SSQNUZ_4.8.x/dev/generate-token.html) en el servidor donde está instalado OpenPages.

La API REST deIBM OpenPages GRC se ajusta al principio de falta de estado de los sistemas RESTful, por lo que cada solicitud realizada debe proporcionar las credenciales del usuario. Todas las comunicaciones en IBM OpenPages for IBM Cloud Pak for Data aplican SSL de forma predeterminada.

#### Configuración de OAuth 2.0, utilizando un proveedor de autenticación de terceros

OAuth 2.0 permite a los usuarios mantener en privado sus nombres de usuario, contraseñas y otra información cuando comparten datos específicos con una aplicación. Puede configurar la autenticación OAuth2.0 para ' IBM OpenPages ' REST API V1 y V2 en ' IBM OpenPages ' on premises o ' IBM OpenPages ' on Cloud.

> **Consejo** : Si desea configurar la autenticación nativa OAuth 2.0 de OpenPages sin un proveedor de autenticación de terceros, consulte [Configuración de la autenticación nativa OAuth 2.0](3.1-guia-del-administrador.md#configuración-de-la-autenticación-nativa-oauth-20).

En esta configuración, ' OpenPages ' desempeña el papel de servidor de recursos en los flujos de autenticación OAuth 2.0. Puede utilizar un servidor de autorización OAuth 2.0 o un proveedor OpenID Connect (OIDC) como proveedor de identidadIdP).

##### Antes de empezar

Tu entorno debe cumplir los siguientes criterios:

- Un servidor de autorización OAuth 2.0 o proveedor OIDC está configurado y en funcionamiento.
- Registrar una cuenta de cliente que será utilizada por el servidor ' OpenPages ' para realizar una introspección o validar la identidad. Esta cuenta debe crearse en el proveedor OAuth 2.0 u OIDC. OpenPages utiliza el ID de cliente y el secreto de cliente sólo para la validación de tokens con el servidor de autorización.
- Cada cliente externo que utilice las API REST " OpenPages " debe tener asignado un ID de usuario de cuenta de servicio en el servidor de autorización OAuth 2.0 0, o disponer de una identidad de usuario en el proveedor OIDC. El nombre de usuario de la cuenta de servicio o ID funcional que se asigna a cada cliente debe coincidir con un usuario del sistema " OpenPages ".
- Si es necesario, cree un usuario en ' OpenPages ' con el nombre de usuario ' `service-account` y los permisos necesarios para que el flujo de credenciales de cliente funcione correctamente. El " `client_id` " procede del proveedor OIDC.
- OpenPages esté instalado y los servidores de OpenPages estén en funcionamiento.
- Puedes conectarte a la aplicación " OpenPages " desde tu navegador.

##### Acerca de esta tarea

En esta tarea se configura un servidor IBM WebSphere Liberty para que actúe como cliente de OpenID Connect. Para más información, consulte [OpenID Connect Client ( openidConnectClient](https://www.ibm.com/docs/en/was-liberty/core?topic=configuration-openidconnectclient) ).

Puede utilizar cualquier proveedor compatible con los protocolos OAuth 2.0 u OpenID Connect.

##### Procedimiento

1. Inicie sesión en el servidor de aplicaciones " OpenPages ".
2. Instale las funciones IBM WebSphere Liberty openidConnectClient-1.0 y transportSecurity-1.0 ejecutando los siguientes comandos:

   ```xml
   <WLP_HOME>/bin/installUtility install openidConnectClient-1.0
   <WLP_HOME>/bin/installUtility install transportSecurity-1.0
   ```
3. Vaya al directorio ' `<WLP_USER_DIR>/servers/<server_name>Server<#>/configDropins/overrides`.

   Si el directorio no existe, créelo.
4. ' Crear un archivo .xml. En el archivo, inserte las siguientes líneas después de reemplazar las variables OAuth2_OIDC_provider, como ' `<OAuth2_OIDC_provider_client_ID>`, con la información de su proveedor de OIDC.

   ```xml
   <server>
   <featureManager>
       <feature>openidConnectClient-1.0</feature>
       <feature>transportSecurity-1.0</feature>
   </featureManager>
   <openidConnectClient id="providerClient" inboundPropagation="required"
                        clientId="<OAuth2_OIDC_provider_client_ID>"
                        audiences="<OAuth2_OIDC_provider_client_ID>, account"
                        clientSecret="<OAuth2_OIDC_provider_client_SECRET>"
                        jwtAccessTokenRemoteValidation="require"
                        userIdentityToCreateSubject="<OAuth2_OIDC_Provider_username_attribute>"
                        issuerIdentifier="<OAuth2_OIDC_provider_ISSUER_ENDPOINT_URL>"
                        jwksUri="<OAuth2_OIDC_provider_JWKS_ENDPOINT_URL>"
                        validationEndpointUrl="<OAuth2_OIDC_provider_INTROSPECTION_ENDPOINT_URL>"
   >
       <authFilter id="oauthApiAuthFilter">
           <requestUrl id="apiCUrl" matchType="contains" urlPattern="/grc/api|/opgrc/api"/>
       </authFilter>
   </openidConnectClient>
   </server>
   ```

   Asegúrese de que el elemento " `<authFilter>` " no contiene filtros " `<requestUrl>` " que entren en conflicto.

   > **Consejo:** Para añadir más filtros, cree más elementos ' `<requestUrl>` '. Asigna a cada uno de ellos un " `id` único.
5. Exporte los certificados de autoridad de certificación raíz e intermedia de su servidor de autorización o proveedor de OIDC.

   Para más información, póngase en contacto con su proveedor.
6. Importe los certificados de autoridad de certificación raíz e intermedia al almacén de confianza " OpenPages ".

   Por ejemplo:

   ```
   keytool -importcert -v -alias <certificate_alias> -file <path_to_certificate> -keystore <OP_HOME>/wlp-usr/servers/<server_name>Server<#>/resources/security/key.p12 -storetype PKCS12
   ```
7. Detén todos los servicios de ' OpenPages '.
8. Reinicia todos los servicios de ' OpenPages '.

##### Qué hacer a continuación

Para utilizar el protocolo OAuth 2.0 para la autenticación pública de IBM OpenPages GRC REST API, utilice tokens de portador JSON Web Token (JWT) emitidos por el servidor de autorización o el proveedor de OpenID.

### Interacciones cliente/servidor

La interacción del cliente con la API REST deIBM OpenPages GRC, incluida la secuencia de sucesos, depende del diseño del cliente y de los objetivos de interacción. Una interacción recupera información de metadatos y configuración y, a continuación, envía más solicitudes al servidor para recopilar más datos o realizar actualizaciones.

*Figura 1. Interacción para crear un nuevo objeto GRC de tipo LossEvent*

![Este diagrama muestra la interacción para crear un nuevo objeto GRC de tipo LossEvent.](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/api_client_server_interaction.png)

### Integración de ' OpenPages ' con la seguridad de IBM WebSphere Liberty

OpenPages ofrece autenticación de certificados de cliente con WebSphere Liberty Profile (WLP). Para integrar ' OpenPages ' con Liberty security, debes cambiar la configuración de tu servidor.

#### Antes de empezar

- Debe tener acceso al servidor de aplicaciones OpenPages y permiso para modificar la configuración del servidor.
- Debe disponer de un certificado de clave pública x509 que represente a su cliente. Este certificado requiere un Asunto que identifique al usuario en ' OpenPages ' como el que este cliente se está autenticando. Por ejemplo, un asunto puede ser " `/CN=OpenPagesAdministrator` para un usuario " `OpenPagesAdministrator`, o " `/C=US/O=IBM/OU=WFSS/CN=brianl` para otro usuario con el nombre " `brianl`. Estos nombres de usuario deben existir como cuentas de usuario dentro de ' OpenPages.

#### Acerca de esta tarea

Esta tarea muestra cómo configurar un entorno recién instalado para permitir la autenticación de certificados de cliente para la API REST. Si ha modificado la configuración de seguridad global o los dominios de seguridad GRC (por ejemplo, para utilizar SSO), es posible que tenga que ajustar estos pasos a su entorno.

#### Procedimiento

1. Cambia los directorios a ' `<WLP_HOME>/usr/servers/<OP_SERVER>/configDropins/overrides`.

   Si el directorio ' `overrides` ' no existe, créalo.
2. Crea un archivo ' `.xml` ' que contenga los siguientes elementos:

   ```xml
   <server>
   <feature>transportSecurity-1.0</feature>
   <sslDefault sslRef="defaultSSLConfig" />
   <ssl id="defaultSSLConfig" keyStoreRef="defaultKeyStore" 
   sslProtocol="SSL_TLSv2" trustStoreRef="defaultTrustStore" clientAuthenticationSupported="true"/>
   <keyStore id="defaultTrustStore" password="defaultPWD" />
   <webAppSecurity allowFailOverToBasicAuth="true" />
   </server>
   ```

   - El atributo `<ssl>` `clientAuthenticationSupported` permite la autenticación de certificados de cliente.
   - El elemento ' `<keyStore>` ' debe especificar un truststore válido a utilizar, como ' `defaultTrustStore`, y la contraseña del truststore, como ' `defaultPWD`, como atributos. El almacén de claves por defecto se encuentra en ' `<WLP_HOME>/usr/servers/<OP_SERVER>/resources/security/key.p12`.
   - Si falla la autenticación de certificado, el atributo `<webAppSecurity>` `allowFailOverToBasicAuth` permite a la API utilizar la autenticación básica. Para más información, consulte [https://www.ibm.com/docs/en/was-liberty/base?topic=configuration-webappsecurity](https://www.ibm.com/docs/en/was-liberty/base?topic=configuration-webappsecurity).
3. Añada el certificado de firmante de CA al almacén de confianza.

   Por ejemplo:

   ```
   keytool -keystore <WLP_HOME>/usr/servers/<OP_SERVER>/resources/security/key.p12 -storepass <password> -importcert -alias <Certificate alias> -file <Path to CA certificate> -storetype PKCS12
   ```
4. En el archivo " `.xml` " recién creado, cree un elemento " `<openpagesUserRegistry/>` " dentro del elemento " `<server>` ".
5. 'Añada atributos al elemento ' `<openpagesUserRegistry/>` ', en función de los temas de su certificado de cliente. El registro de usuarios personalizado OpenPages utiliza estos atributos para analizar un nombre de usuario a partir de la entrada Subject del certificado del cliente.

   Ejemplo 1

   El siguiente ejemplo es un enfoque más sencillo que busca la primera aparición del CN= dentro de un asunto.

   ```xml
   <openpagesUserRegistry com.ibm.openpages.security.entry.user.key="CN" com.ibm.openpages.security.entry.user.delimiter="," com.ibm.openpages.security.cert.regex="true"/>
   ```

   Ejemplo 2

   Puede utilizar expresiones regulares (regex) para disponer de más flexibilidad a la hora de gestionar distintos formatos de Sujetos en certificados de cliente en función de las políticas y prácticas de su organización. Mediante el uso de expresiones regulares, puede especificar una lógica más granular para analizar un nombre de usuario a partir del elemento Asunto de un certificado. El elemento Asunto de un certificado puede contener varias partes. El siguiente ejemplo utiliza una expresión regular para analizar un nombre de usuario cuando un Asunto tiene la forma ' `"/C=US/O=IBM/OU=WFSS/CN=brianl"`.

   ```xml
   <openpagesUserRegistry com.ibm.openpages.security.entry.user.regex="(?:CN=)([^,]+),?" com.ibm.openpages.security.cert.regex="true"/>
   ```

   En regex, un grupo es una forma de tratar varios caracteres como una sola unidad. Se crean colocando los caracteres a agrupar dentro de un conjunto de paréntesis.

   Un grupo de captura captura el texto que coincide con la expresión regular dentro de los paréntesis en un grupo numerado. El grupo numerado puede reutilizarse con una referencia posterior numerada. Utilice un grupo de captura para aplicar operadores regex a toda la regex agrupada.

   Un grupo no capturador es una forma de agrupar un conjunto de caracteres o expresiones en una expresión regular sin capturar el texto coincidente. La sintaxis para un grupo no capturador, un signo de interrogación y dos puntos después del paréntesis de apertura, informa al motor de expresión regular de que no almacene el texto coincidente.

   En el ejemplo 2, el motor de expresiones regex busca un grupo no capturador que coincida con apariciones de " `CN=`. Cuando se encuentra una coincidencia, se captura el texto entre la ocurrencia coincidente y el delimitador de coma. Cuando Liberty interpreta el asunto del certificado del cliente, el resultado es " `"CN=brianl, OU=WFSS, O=IBM, C=US"`.

   La expresión regex coincide con ' `CN=brianl`, y el nombre de usuario que se toma de la coincidencia es el grupo de captura #1 identificado por la expresión regular como ' `brianl`.

   El siguiente ejemplo de texto del Asunto ilustra un escenario diferente, en el que el valor de " `CN=` " es una dirección de correo electrónico en lugar del nombre de usuario.

   ```
   Text "CN=brianl@us.ibm.com,
           OU=WFSS, O=IBM, C=US"
   ```

   La siguiente expresión regular compara el texto entre los símbolos " `CN=` " y " `@` " para obtener el nombre de usuario del asunto.

   ```
   (?:CN=)([^@]+),?
   ```
6. Detenga el servidor de aplicaciones ' OpenPages '.
7. 'En la sección ' `<login-config>` ' del archivo ' `web.xml` de la aplicación API REST, cambie el elemento ' `<auth-method>` ' para especificar el método de autenticación ' `CLIENT-CERT` ' en lugar del método de autenticación ' `BASIC` '. El archivo está en el directorio ' `<WLP_HOME>/usr/shared/apps/op-apps.ear/com.ibm.openpages.api.rest.war/WEB-INF`.

   Si el archivo " `web_merged.xml` " existe en el directorio " `<WLP_HOME>/usr/shared/apps/op-apps.ear/com.ibm.openpages.api.rest.war/WEB-INF` ", realice el mismo cambio en el archivo " `web_merged.xml` ".

   Después de realizar el cambio, la sección " `<login-config>` " de cada archivo aparece de la siguiente manera:

   ```xml
   <login-config>
           <auth-method>CLIENT-CERT</auth-method>
           <realm-name>OpenPagesRealm</realm-name>
       </login-config>
   ```
8. Si los usuarios necesitan abrir archivos de Microsoft Office desde OpenPages Cuando la autenticación de certificado de cliente está habilitada, siga los pasos de la nota técnica [No se pueden abrir archivos de Microsoft Office (doc, xls) desde OpenPages cuando la autenticación de certificado de cliente está habilitada](https://www.ibm.com/support/pages/node/6832726).
9. Reinicie el servidor de aplicaciones " OpenPages ".

#### Qué hacer a continuación

Puede probar cómo funciona la autenticación de certificado de cliente utilizando un cliente REST que admita este método de autenticación. Por ejemplo, el comando cURL de tipo UNIX admite este método.

Por ejemplo, si el certificado del cliente está en ' `client1.pem` y el del servidor es ' `my-op-server`, utilice el siguiente comando cURL:

```
curl --tlsv1.2
        --no-alpn --verbose --cert /path-to-/client1.pem
        https://my-op-server:10111/opgrc/api/v2/types
```

Este comando devuelve los siguientes resultados:

- Toda la salida que está relacionada con el handshake SSL debido a la inclusión de la opción ' `--verbose`.
- Un cuerpo de respuesta que contiene el JSON que describe el esquema de metadatos ' OpenPages ' porque la solicitud especifica que se deben devolver todos los tipos.

Si su servidor no utiliza un certificado SSL válido, puede añadir la opción " `--insecure` " al comando para realizar pruebas. La opción ' `--no-alpn` ' se introdujo en la versión 7.36.0 cURL. Si su versión de cURL es anterior a 7.36.0, elimine la opción ' `--no-alpn`.

Puede utilizar este método para probar otros puntos finales de la API REST deIBM OpenPages GRC.

### Asignación de eventos normativos a mandatos, submandatos y requisitos

Al importar eventos normativos mediante App Connect o la API REST deIBM OpenPages GRC, puede asignar los eventos normativos ingestados a los objetos de la biblioteca normativa: Mandatos, Submandatos y Requisitos.

#### Acerca de esta tarea

Para realizar la asociación, utilice una llamada a la API REST deIBM OpenPages GRC. Los ejemplos de esta tarea ilustran el caso de uso en el que se tiene un Hecho Normativo que debe asociarse a un Mandato y Submandato existentes.

#### Procedimiento

1. Obtiene el ID de recurso del evento regulador.

   ```
   https://<server_name>:<port_number>/opgrc/api/v2/query?q=SELECT * FROM [RegulatoryEvent] WHERE [RCM-RegulatoryEvent:Amended Citation] LIKE '<value>'
   ```

   Tipo de solicitud: GET

   Por ejemplo, consulte el campo " `RCM-RegulatoryEvent:Amended Citation` " y busque el valor " `12 CFR 1026`.

   ```
   https://server1.ibm.com:10111/opgrc/api/v2/query?q=SELECT * FROM [RegulatoryEvent] WHERE [RCM-RegulatoryEvent:Amended Citation] LIKE '%2512 CFR 1026%25' 
   ```

   El ID del recurso devuelto por esta consulta es " `12593`.
2. Obtiene el ID de recurso del mandato que se utilizará para la asociación.

   ```
   https://<server_name>:<port_number>/opgrc/api/v2/query?q=SELECT [Resource ID] FROM [Mandate] where [RCM-Mand:Citation] = '<value>'
   ```

   Tipo de solicitud: GET

   Por ejemplo, consulte el campo " `RCM-Mand:Citation` " y busque el valor " `12 CFR 1026`.

   ```
   https://server1.ibm.com:10111/opgrc/api/v2/query?q=SELECT [Resource ID] FROM [Mandate] where [RCM-Mand:Citation] = '12 CFR 1026'
   ```

   El ID del recurso devuelto por esta consulta es " `9946`.
3. Obtiene el ID de recurso del submandato que se utilizará para la asociación.

   ```
   https://<server_name>:<port_number>/opgrc/api/v2/query?q=SELECT [Resource ID] FROM [Submandate] where [RCM-SubMand:Citation] = '<value>'
   ```

   Tipo de solicitud: GET

   Por ejemplo, consulte el campo " `RCM-SubMand:Citation` " y busque el valor " `12 CFR 1026.8`.

   ```
   https://server1.ibm.com:10111/opgrc/api/v2/query?q=SELECT [Resource ID] FROM [Submandate] where [RCM-SubMand:Citation] = '12 CFR 1026.8'
   ```

   El ID del recurso devuelto por esta consulta es " `9981`.
4. Llame a la API REST de IBM OpenPages GRC para asociar el evento normativo a dos padres, un mandato y un submandato, utilizando los ID de recursos recuperados en los pasos anteriores URL :

   ```
   https://<server_name>:<port_number>/opgrc/api/v2/contents/<id>/associations/parents
   ```

   Tipo de solicitud: POST

   Parámetros de entrada en formato JSON: `{"associations":[{"id": "<id_of_mandate>"}, {"id": "<id_of_sub-mandate>"}]}`

   Por ejemplo:

   ```
    https://server1.ibm.com:10111/opgrc/api/v2/contents/12593/associations/parents
   ```

   Parámetros de entrada en formato JSON: `{"associations":[{"id": "9946"}, {"id": "9981"}]}`

## IBM OpenPages API REST GRC V1

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=guide-rest-api-v1)

Utilice esta versión de la IBM OpenPages GRC REST API para OpenPages® versiones anteriores a 9.0.0.0.

La IBM OpenPages GRC REST API proporciona acceso a IBM OpenPages datos y metadatos. Esta API centrada en datos se especifica en términos de recursos, sus URI y acciones que se pueden realizar en estos URI.

Para más información sobre la API V1, están disponibles los siguientes documentos:

- To configure OAuth 2.0 authentication for the IBM OpenPages REST API V1 on IBM OpenPages on premises or IBM OpenPages on Cloud, see the *Seguridad y autenticación* section of the ['IBM ' OpenPages GRC REST API ' V2](#ibm-openpages-api-rest-grc-v2) topic.
- El ' ['OpenPages GRC REST API ' V1 Guía de referencia](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/GRC_REST_API.pdf) ' le ofrece información detallada sobre la API REST en formato PDF.
- Descargue el ' [OpenPages Documentación HTML de la API REST de GRC](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/op_grc_rest_api_html.zip) comprimido , en el archivo ' op_grc_rest_api_html.zip, para tener una descripción HTML independiente del ' IBM OpenPages GRC REST API ' V1 ' OpenAPI.

  Al descomprimir el archivo .zip se crea un archivo `index.html` que puede abrir con un navegador web para ver la documentación de OpenAPI .
- Para ver el archivo JSON de ' OpenAPI ', vaya a ' ['OpenPages GRC REST API ' OpenAPI especificación](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/swagger2.json). Si desea ver el archivo JSON sin el formato, pulse el enlace que sigue al título de la especificación.

## Ejemplos de API

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=guide-api-samples)

Los ejemplos de API, basados en el conjunto de datos de ejemplo, muestran partes de la APIIBM OpenPages GRC Java™ y IBM OpenPages GRC.

Puede descargar el archivo de [ejemplos de API](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/op_sdk_rest_samples.zip) comprimido para probar las API de OpenPages® .

Al descomprimir el archivo .zip se crea una carpeta `samples` que contiene una carpeta para cada ejemplo y una carpeta `data` para el conjunto de datos de ejemplo y el esquema. El conjunto de datos de ejemplo modela un sistema de palabras reales. El conjunto de datos es un subconjunto de los objetos y campos estándar de ORM e incluye una plantilla FastMap con datos de ejemplo que se utilizan en los ejemplos y demostraciones.

. Cada carpeta de ejemplo incluye los siguientes archivos:

- Un archivo `readme.txt` o un archivo `readme.md` que describe lo que muestra el ejemplo.
- Archivos de origen que se utilizan para compilar, desplegar y ejecutar el código de ejemplo.

  El código de ejemplo se ejecuta en un sistema OpenPages con el esquema de ejemplo y el conjunto de datos cargados.

El modelo de objeto, el esquema y el conjunto de datos de ejemplo que se proporcionan en el archivo .zip de ejemplos de API son ejemplos para ayudar a los desarrolladores a comprender las prestaciones de OpenPages. Los ejemplos de API no están pensados para ser aplicaciones listas para producción.

Si un esquema personalizado ya está cargado en OpenPages, es posible que encuentre problemas de incompatibilidad. Consulte al representante de servicios IBM OpenPages antes de continuar.

> **Aviso:** al cargar el esquema se alteran los metadatos y la configuración del sistema. Estas operaciones no se pueden deshacer. Cree una copia de seguridad del sistema utilizando OPBackup antes de continuar. Para obtener más información sobre cómo ejecutar el programa de utilidad OPBackup, consulte [El programa de utilidad OPBackup (Db2®)](3.4-guia-del-administrador.md#el-programa-de-utilidad-opbackup-db2) o [El programa de utilidad OPBackup (Oracle)](3.4-guia-del-administrador.md#el-programa-de-utilidad-opbackup-oracle).

La tabla siguiente muestra los ejemplos de API por carpeta. Antes de utilizar los ejemplos de API, asegúrese de que realiza los pasos siguientes:

- Lea y siga las instrucciones del archivo `ReadMe.txt` en la carpeta `samples` .
- Lea el archivo `readme.txt` o el archivo `readme.md` para cualquier ejemplo que tenga previsto utilizar.

**Tabla 1. Descripciones de ejemplo de API**

| Carpeta de ejemplo | Descripción |
| --- | --- |
| `AnonLossEventFormREST` | Este ejemplo muestra cómo permitir que los usuarios anónimos especifiquen pérdidas financieras sin iniciar sesión en el sistema OpenPages . Los usuarios van a un sitio web de la empresa o a una infraestructura de portal web existente y completan un formulario con detalles de la pérdida. Después de que un usuario envíe el formulario, la pérdida se puede crear en OpenPages utilizando la API Java deIBM OpenPages GRC. |
| `BusinessEntityHelper` | Este ejemplo muestra cómo utilizar la API Java deIBM OpenPages GRC para recuperar metadatos e información de perfil para un tipo de objeto SOXBusEntity y crear dinámicamente un formulario HTML simple para crear objetos de ese tipo. |
| `Classifiers` | Este ejemplo muestra cómo utilizar la API Java deIBM OpenPages GRC para configurar un campo de clasificador y verlo en una vista de creación. |
| `CustomRESTService` | Este ejemplo muestra cómo crear y desplegar servicios REST personalizados en la aplicación web de la API REST GRC pública. Puede utilizar servicios REST personalizados para revelar la lógica empresarial específica del cliente a clientes externos o a aplicaciones que se integran con OpenPages. |
| `IssueHelperJSP` | Este ejemplo muestra cómo utilizar la API Java deIBM OpenPages GRC para recuperar metadatos e información de perfil para un tipo de objeto SOXIssue y crear dinámicamente un formulario HTML simple para crear objetos de ese tipo. |
| `QueryTestJSP` | Este ejemplo utiliza la API Java deIBM OpenPages GRC para proporcionar un formulario web simple para enviar una expresión de servicio de consulta y visualizar los resultados de la ejecución de la consulta en los datos. Puede utilizar el mismo formulario para crear prototipos rápidos y probar sus propias consultas durante el desarrollo. El código .jsp muestra cómo puede recuperar valores de los resultados de la consulta. |
| `ReactCarbonHelper` | Este ejemplo utiliza la API Java deIBM OpenPages GRC para demostrar cómo crear una aplicación React que se integre con OpenPages. El ejemplo utiliza TypeScript, Sass y Carbon.<br>Para obtener más información sobre TypeScript, consulte [https://www.typescriptlang.org/](https://www.ibm.com/links?url=https%3A%2F%2Fwww.typescriptlang.org%2F)<br>Para obtener más información sobre Sass, consulte [https://sass-lang.com/](https://www.ibm.com/links?url=https%3A%2F%2Fsass-lang.com%2F).<br>Para obtener más información sobre Carbon, consulte [https://carbondesignsystem.com/](https://www.ibm.com/links?url=https%3A%2F%2Fcarbondesignsystem.com%2F). |
| `TivoliDirectoryIntegratorConnector` | IBM Security® Directory Integrator, anteriormente IBM® Tivoli® Directory Integrator, es un entorno de desarrollo gráfico de marco de integración para crear y probar soluciones de consola de administración y supervisión basadas en web para la gestión (AMC). Tiene conectores para muchos protocolos y sistemas comunes, y tiene una arquitectura de plug-in para crear conectores y adaptadores personalizados. Correlaciona datos de varios sistemas en un flujo definido que se denomina línea de ensamblaje.<br>Este ejemplo utiliza la API REST deIBM OpenPages GRC para crear una línea de ensamblaje básica con un conector OpenPages . El ejemplo recupera LossEvents de OpenPages basándose en una consulta que utiliza la sintaxis de Query Service. Los LossEvents se correlacionan con una tabla de base de datos Losses que representa un sistema externo. |
| `Triggers` | Este ejemplo utiliza la API Java deIBM OpenPages GRC. Contiene un conjunto de desencadenantes que utilizan la infraestructura de desencadenantes GRC. Los disparadores incluyen disparadores Create y Update en LossEvent, y un disparador Create en SOXBusEntity. Los activadores utilizan ContentTypeMatchRule. |

## Activadores

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=dg-triggers)

Un desencadenante es un fragmento de código Java™ que se puede añadir antes o después de la ejecución de una operación que se realiza en la plataforma OpenPages® . La lógica de negocio y los requisitos de reglas más comunes se pueden cumplir utilizando los flujos de trabajo GRC o los cálculos GRC. Para los requisitos que no se pueden cumplir utilizando estas características, puede desarrollar desencadenantes para implementar reglas y lógica empresarial personalizadas.

Utilice el siguiente material de referencia para desarrollar desencadenantes:

- Ejemplo de API de desencadenantes

  Este ejemplo contiene un conjunto de desencadenantes que utilizan IBM OpenPages GRC Trigger Framework. Para obtener más información sobre el ejemplo de API de desencadenantes, consulte [Ejemplos de API](#ejemplos-de-api).
- [OpenPages Trigger-Guía del desarrollador](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/Trigger_Developer_Guide.pdf)

  La Guía del desarrollador de desencadenantes describe IBM OpenPages GRC Trigger Framework y cómo configurar desencadenantes.

## Avisos

`Guía del desarrollador` · [origen](https://www.ibm.com/docs/es/openpages/9.1.x?topic=dg-notices)

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

La información relacionada con productos que no son de IBM se ha obtenido de los proveedores de dichos productos, de sus anuncios publicados o de otras fuentes de disponibilidad pública. IBM no ha probado estos productos y no puede confirmar la precisión de su rendimiento, su compatibilidad o cualquier otra reclamación relacionada con productos que no sean de IBM. Las preguntas relacionadas con las prestaciones de los productos que no son de IBM deberán dirigirse a los proveedores de estos productos.

Todas las declaraciones relacionadas con futuras directrices o intenciones de IBM están sujetas a cambios o a su retirada sin previo aviso y sólo representan objetivos.

Esta información contiene ejemplos de datos e informes utilizados en operaciones comerciales diarias. Para ilustrarlas de la forma más completa posible, los ejemplos incluyen los nombres de personas, empresas, marcas y productos. Todos estos nombres son ficticios y cualquier similitud a los nombres y direcciones que haya utilizado una empresa real es pura coincidencia.

Si ha optado por visualizar la copia software de esta información, puede que no aparezcan las fotografías y las ilustraciones a color.

Esta oferta de software no utiliza cookies ni otro tipo de tecnología para recopilar información de identificación personal.

## Integración de OpenPages con la seguridad de IBM® WebSphere Liberty

`Guía del desarrollador › temas fuera del índice de IBM` · [origen](https://www.ibm.com/docs/es/SSFUEU_9.1/op_grc_dev/t_dev_api_client_cert_auth.html)

OpenPages® ofrece autenticación de certificados de cliente con WebSphere® Liberty Profile (WLP). Para integrar OpenPages con la seguridad de Liberty, debe cambiar la configuración del servidor.

### Antes de empezar

- Debe tener acceso al servidor de aplicaciones OpenPages y permiso para modificar la configuración del servidor.
- Debe tener un certificado de clave pública x509 que represente al cliente. Este certificado requiere un sujeto que identifique al usuario en OpenPages con el que se autentica este cliente. Por ejemplo, un asunto puede ser `/CN=OpenPagesAdministrator` para un usuario `OpenPagesAdministrator`, o `/C=US/O=IBM/OU=WFSS/CN=brianl` para otro usuario con el nombre `brianl`. Estos nombres de usuario deben existir como cuentas de usuario en OpenPages.

### Acerca de esta tarea

Esta tarea muestra cómo configurar un entorno recién instalado para permitir la autenticación de certificados de cliente para la API REST. Si ha modificado la configuración de seguridad global o los dominios de seguridad GRC (por ejemplo, para utilizar SSO), es posible que tenga que ajustar estos pasos para su entorno.

### Procedimiento

1. Cambie los directorios a `<WLP_HOME>/usr/servers/<OP_SERVER>/configDropins/overrides`.

   Si el directorio `overrides` no existe, créelo.
2. Crea un archivo `.xml` que contenga los siguientes elementos:

   ```xml
   <server>
   <feature>transportSecurity-1.0</feature>
   <sslDefault sslRef="defaultSSLConfig" />
   <ssl id="defaultSSLConfig" keyStoreRef="defaultKeyStore" sslProtocol="SSL_TLSv2" trustStoreRef="defaultTrustStore" clientAuthenticationSupported="true"/>
   <keyStore id="defaultTrustStore" password="defaultPWD" />
   <webAppSecurity allowFailOverToBasicAuth="true" />
   </server>
   ```

   - El `<ssl>` atributo `clientAuthenticationSupported` habilita la autenticación de certificado de cliente.
   - El elemento `<keyStore>` debe especificar un almacén de confianza válido para utilizarlo, como por ejemplo `defaultTrustStore`, y la contraseña del almacén de confianza, como por ejemplo `defaultPWD`, como atributos. El almacén de claves predeterminado se puede encontrar en `<WLP_HOME>/usr/servers/<OP_SERVER>/resources/security/key.p12`.
   - Si la autenticación de certificado falla, el `<webAppSecurity>` atributo `allowFailOverToBasicAuth` permite que la API utilice la autenticación básica. Para obtener más información, consulte [https://www.ibm.com/docs/en/was-liberty/base?topic=configuration-webappsecurity](https://www.ibm.com/docs/en/was-liberty/base?topic=configuration-webappsecurity).
3. Añada el certificado de firmante de CA al almacén de confianza.

   Por ejemplo:

   ```
   keytool -keystore <WLP_HOME>/usr/servers/<OP_SERVER>/resources/security/key.p12 -storepass <password> -importcert -alias <Certificate alias> -file <Path to CA certificate> -storetype PKCS12
   ```
4. En el archivo `.xml` recién creado, crea un elemento `<openpagesUserRegistry/>` dentro del elemento `<server>`.
5. Añada atributos al elemento `<openpagesUserRegistry/>` , en función de los asuntos del certificado de cliente. Estos atributos los utiliza el registro de usuarios personalizado de OpenPages para analizar un nombre de usuario de la entrada Asunto en el certificado de cliente.

   Ejemplo 1

   El ejemplo siguiente es un enfoque más simple que busca la primera aparición del CN= dentro de un sujeto.

   ```xml
   <openpagesUserRegistry com.ibm.openpages.security.entry.user.key="CN" com.ibm.openpages.security.entry.user.delimiter="," com.ibm.openpages.security.cert.regex="true"/>
   ```

   Ejemplo 2

   Puede utilizar expresiones regulares (regex) para proporcionarle más flexibilidad para manejar diferentes formatos de sujetos en certificados de cliente en función de las políticas y prácticas de su organización. Utilizando regex, puede especificar una lógica más granular para analizar un nombre de usuario del elemento Subject más grande de un certificado. El elemento Subject de un certificado puede contener muchas partes. El ejemplo siguiente utiliza una expresión regular para analizar un nombre de usuario cuando un sujeto tiene el formato `"/C=US/O=IBM/OU=WFSS/CN=brianl"`.

   ```xml
   <openpagesUserRegistry com.ibm.openpages.security.entry.user.regex="(?:CN=)([^,]+),?" com.ibm.openpages.security.cert.regex="true"/>
   ```

   En regex, un grupo es una forma de tratar varios caracteres como una sola unidad. Se crean colocando los caracteres que se van a agrupar dentro de un conjunto de paréntesis.

   Un grupo de captura captura el texto que coincide con la expresión regular dentro de los paréntesis en un grupo numerado. El grupo numerado se puede reutilizar con una referencia posterior numerada. Utilice un grupo de captura para aplicar operadores de expresión regular a toda la expresión regular agrupada.

   Un grupo que no es de captura es una forma de agrupar un conjunto de caracteres o expresiones en una expresión regular sin capturar el texto coincidente. La sintaxis para un grupo no de captura, un signo de interrogación y dos puntos después del paréntesis de apertura, informa al motor de expresiones regulares de que no almacene el texto coincidente.

   En el Ejemplo 2, el motor de expresiones regulares busca un grupo que no sea de captura que coincida con las apariciones de `CN=`. Cuando se encuentra una coincidencia, se captura el texto entre la aparición coincidente y el delimitador de coma. Cuando Liberty interpreta el sujeto del certificado de cliente, el resultado es `"CN=brianl, OU=WFSS, O=IBM, C=US"`.

   La expresión regular coincide con `CN=brianl`, y el nombre de usuario que se toma de la coincidencia es el grupo de captura #1 identificado por la expresión regular como `brianl`.

   El siguiente ejemplo de texto del asunto ilustra un escenario diferente, donde el valor de `CN=` es una dirección de correo electrónico en lugar del nombre de usuario.

   ```
   Text "CN=brianl@us.ibm.com,
           OU=WFSS, O=IBM, C=US"
   ```

   La siguiente expresión regular coincide con el texto entre el símbolo `CN=` y `@` para proporcionarle el nombre de usuario del sujeto.

   ```
   (?:CN=)([^@]+),?
   ```
6. Detenga el servidor de aplicaciones de OpenPages .
7. En la sección `<login-config>` del archivo `web.xml` de la aplicación API REST, cambie el elemento `<auth-method>` para especificar el método de autenticación `CLIENT-CERT` en lugar del método de autenticación `BASIC` . El archivo se encuentra en el directorio `<WLP_HOME>/usr/shared/apps/op-apps.ear/com.ibm.openpages.api.rest.war/WEB-INF`.

   Si el archivo `web_merged.xml` existe en el directorio `<WLP_HOME>/usr/shared/apps/op-apps.ear/com.ibm.openpages.api.rest.war/WEB-INF` , realice el mismo cambio en el archivo `web_merged.xml` .

   Después de realizar el cambio, la sección `<login-config>` de cada archivo aparece de la siguiente manera:

   ```xml
   <login-config>
           <auth-method>CLIENT-CERT</auth-method>
           <realm-name>OpenPagesRealm</realm-name>
       </login-config>
   ```
8. Reinicie el servidor de aplicaciones de OpenPages .

### Qué hacer a continuación

Puede probar cómo funciona la autenticación de certificado de cliente utilizando un cliente REST que tenga soporte para este método de autenticación. Por ejemplo, el mandato cURL de estilo UNIX da soporte a este método.

Por ejemplo, si el certificado de cliente está en `client1.pem` y el servidor es `my-op-server`, utilice el siguiente mandato cURL :

```
curl --tlsv1.2
        --no-alpn --verbose --cert /path-to-/client1.pem
        https://my-op-server:10111/opgrc/api/v2/types
```

Este mandato devuelve los resultados siguientes:

- Toda la salida que está relacionada con el reconocimiento SSL debido a la inclusión de la opción `--verbose` .
- Un cuerpo de respuesta que contiene el JSON que describe el esquema de metadatos OpenPages porque la solicitud especifica que se van a devolver todos los tipos.

Si el servidor no utiliza un certificado SSL válido, puede añadir la opción `--insecure` al mandato para fines de prueba. La opción `--no-alpn` se ha introducido en cURL versión 7.36.0. Si la versión de cURL es anterior a 7.36.0, elimine la opción `--no-alpn` .

Puede utilizar este método para probar otros puntos finales de IBM OpenPages GRC REST API .
