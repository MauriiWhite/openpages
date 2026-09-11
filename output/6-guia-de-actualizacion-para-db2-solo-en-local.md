---
product: IBM OpenPages 9.0.0
product_key: SSFUEU_9.0.0
file: 6
guide: Guía de actualización para Db2 (solo en local)
covers: Guía de actualización para Db2 (solo en local) — Avisos
chapters: 6
topics: 67
words: 24123
tasks: 40
concepts: 25
references: 1
tables: 5
code_blocks: 137
figures: 17
applies_to: De forma local
updated: 2025-03-24
lang: es
source: https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrade-guide-db2-prem-only
extracted: 2026-09-11
---

# 6 · Guía de actualización para Db2 (solo en local)

> **Qué hay en este archivo.** «Guía de actualización para Db2 (solo en local)» de IBM OpenPages 9.0.0, completa: 6 capítulos. 67 temas, 40 de ellos procedimientos paso a paso, 5 tablas, 137 bloques de código, 17 figuras y 24.123 palabras.
>
> **Capítulos:** Guía de actualización para Db2 (solo en local) · Cómo empezar · Determinar la ruta de actualización · Preparación de la actualización · Actualizar OpenPages · Avisos.
>
> **Se aplica a:** De forma local.
>
> **Si lo que buscas no está acá.** El índice de los 2.511 temas del producto, con su archivo y su ancla, está en `index.md`.

**Términos propios de este archivo:** agente, search, remoto, technology, alrededor, fixpack, argumento, text, autorizaciones, despliegues, situ, edition, migrando, lanzador.

## Índice de este archivo

- [Guía de actualización para Db2 (solo en local)](#guía-de-actualización-para-db2-solo-en-local)
- [Cómo empezar](#cómo-empezar)
  - [Ubicaciones de instalación](#ubicaciones-de-instalación)
  - [Cambios realizados en el proceso de instalación](#cambios-realizados-en-el-proceso-de-instalación)
  - [Caracteres especiales en las contraseñas](#caracteres-especiales-en-las-contraseñas)
- [Determinar la ruta de actualización](#determinar-la-ruta-de-actualización)
- [Preparación de la actualización](#preparación-de-la-actualización)
  - [Revisión de las características y arreglos nuevos](#revisión-de-las-características-y-arreglos-nuevos)
  - [Copia de seguridad del entorno](#copia-de-seguridad-del-entorno)
    - [Copia de seguridad de la base de datos OpenPages (Db2)](#copia-de-seguridad-de-la-base-de-datos-openpages-db2)
    - [Copia de seguridad de la base de datos de Cognos (Db2)](#copia-de-seguridad-de-la-base-de-datos-de-cognos-db2)
    - [Copia de seguridad de asistentes de soluciones, imágenes y otros archivos](#copia-de-seguridad-de-asistentes-de-soluciones-imágenes-y-otros-archivos)
  - [Actualizar software de requisito previo](#actualizar-software-de-requisito-previo)
    - [Actualizar o actualizar Db2](#actualizar-o-actualizar-db2)
      - [Instalación de un Db2 fix pack (Windows)](#instalación-de-un-db2-fix-pack-windows)
      - [Actualización de Db2 (Windows)](#actualización-de-db2-windows)
      - [Actualización de Db2 (Linux)](#actualización-de-db2-linux)
      - [Descarte del índice de búsqueda e inhabilitación de Db2 Text Search](#descarte-del-índice-de-búsqueda-e-inhabilitación-de-db2-text-search)
    - [Actualización de Cognos](#actualización-de-cognos)
    - [Obtención de una copia del SDK de IBM (Windows)](#obtención-de-una-copia-del-sdk-de-ibm-windows)
    - [Obtención de una copia de IBM SDK (Linux®)](#obtención-de-una-copia-de-ibm-sdk-linux)
  - [Verificación de los servidores antes de la actualización](#verificación-de-los-servidores-antes-de-la-actualización)
- [Actualizar OpenPages](#actualizar-openpages)
  - [Actualice la base de datos OpenPages (Db2)](#actualice-la-base-de-datos-openpages-db2)
    - [Preparación de la actualización de la base de datos (Db2)](#preparación-de-la-actualización-de-la-base-de-datos-db2)
      - [Ejecución de un script personalizado durante la actualización de la base de datos (Db2®)](#ejecución-de-un-script-personalizado-durante-la-actualización-de-la-base-de-datos-db2)
    - [Ejecución del script de DBA previo a la actualización (Db2)](#ejecución-del-script-de-dba-previo-a-la-actualización-db2)
    - [Validación del paso de DBA previo a la actualización (Db2)](#validación-del-paso-de-dba-previo-a-la-actualización-db2)
    - [Actualización de la base de datos (Db2)](#actualización-de-la-base-de-datos-db2)
    - [Ejecución del script de DBA posterior a la actualización (Db2)](#ejecución-del-script-de-dba-posterior-a-la-actualización-db2)
    - [Validación del paso de DBA posterior a la actualización (Db2)](#validación-del-paso-de-dba-posterior-a-la-actualización-db2)
  - [Preparación del servidor de instalación](#preparación-del-servidor-de-instalación)
    - [Configuración del servidor de instalación en Windows](#configuración-del-servidor-de-instalación-en-windows)
    - [Configuración del servidor de instalación en Linux®](#configuración-del-servidor-de-instalación-en-linux)
    - [Instalación manual de agentes](#instalación-manual-de-agentes)
    - [Actualización del servidor de instalación y los agentes](#actualización-del-servidor-de-instalación-y-los-agentes)
      - [Actualización del servidor de instalación](#actualización-del-servidor-de-instalación)
      - [Actualización manual de un agente](#actualización-manual-de-un-agente)
    - [Migración de despliegues y usuarios del servidor de instalación](#migración-de-despliegues-y-usuarios-del-servidor-de-instalación)
    - [Inicio manual del agente de instalación](#inicio-manual-del-agente-de-instalación)
    - [Parada manual del agente de instalación](#parada-manual-del-agente-de-instalación)
  - [Actualización OpenPages](#actualización-openpages)
  - [Tareas posteriores a la actualización](#tareas-posteriores-a-la-actualización)
    - [Actualización de los valores de instancia de Db2](#actualización-de-los-valores-de-instancia-de-db2)
    - [Eliminar el botón de lanzamiento de interfaz de usuario de cuestionario heredado de la vista de administración para las evaluaciones de cuestionario](#eliminar-el-botón-de-lanzamiento-de-interfaz-de-usuario-de-cuestionario-heredado-de-la-vista-de-administración-para-las-evaluaciones-de-cuestionario)
    - [Actualización de aplicaciones opcionales](#actualización-de-aplicaciones-opcionales)
    - [Restaurar valores del servidor de aplicaciones personalizado](#restaurar-valores-del-servidor-de-aplicaciones-personalizado)
    - [Restauración de asistentes de soluciones, imágenes y otros archivos](#restauración-de-asistentes-de-soluciones-imágenes-y-otros-archivos)
    - [Volver a crear el índice para la búsqueda global](#volver-a-crear-el-índice-para-la-búsqueda-global)
    - [Actualizar informes](#actualizar-informes)
    - [Habilitar LDAP después de actualizar o migrar](#habilitar-ldap-después-de-actualizar-o-migrar)
    - [Tareas posteriores a la actualización para las soluciones](#tareas-posteriores-a-la-actualización-para-las-soluciones)
      - [Sustitución de campos calculados por cálculos y campos de lanzador de URL (IAM e ITG)](#sustitución-de-campos-calculados-por-cálculos-y-campos-de-lanzador-de-url-iam-e-itg)
      - [Sustitución de campos calculados por campos de lanzamiento de URL (RCSA)](#sustitución-de-campos-calculados-por-campos-de-lanzamiento-de-url-rcsa)
      - [Importación del paquete de informes de soluciones](#importación-del-paquete-de-informes-de-soluciones)
    - [Actualización de campos calculados personalizados](#actualización-de-campos-calculados-personalizados)
    - [Actualización del esquema de elaboración de informes](#actualización-del-esquema-de-elaboración-de-informes)
    - [Regeneración del entorno de elaboración de informes](#regeneración-del-entorno-de-elaboración-de-informes)
    - [Actualización de vistas de detalles a vistas de administración](#actualización-de-vistas-de-detalles-a-vistas-de-administración)
    - [Utilización de vistas de creación personalizadas con la aplicación Loss Event Entry](#utilización-de-vistas-de-creación-personalizadas-con-la-aplicación-loss-event-entry)
    - [Cambios y mejoras en la configuración](#cambios-y-mejoras-en-la-configuración)
      - [Rellenar el campo Título del sistema después de actualizar o migrar](#rellenar-el-campo-título-del-sistema-después-de-actualizar-o-migrar)
  - [Tareas adicionales para actualizaciones](#tareas-adicionales-para-actualizaciones)
    - [Realización de una actualización silenciosa](#realización-de-una-actualización-silenciosa)
    - [Retrotracción de una actualización](#retrotracción-de-una-actualización)
    - [Carga manual de los datos de configuración de una actualización](#carga-manual-de-los-datos-de-configuración-de-una-actualización)
- [Avisos](#avisos)


# Guía de actualización para Db2 (solo en local)

`Guía de actualización para Db2 (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrade-guide-db2-prem-only)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Esta guía proporciona instrucciones para actualizar despliegues de OpenPages® que utilizan  IBM® Db2®  .

Utilice esta guía si está actualizando OpenPages in situ. Si está migrando o realizando una instalación nueva, consulte la publicación *IBM OpenPages Guía de instalación y despliegue*.

## IBM OpenPages documentación

IBM mantiene un conjunto de servicios de documentación IBM OpenPages, IBM OpenPages for IBM Cloud Pak for Datay IBM OpenPages on Cloud despliegues. La documentación de IBM OpenPages describe determinadas características y funciones que pueden no estar disponibles en la nube.

Si tiene alguna pregunta sobre la funcionalidad disponible en la versión del producto que está utilizando, póngase en contacto con el soporte deIBM utilizando el [portal de soporte de IBM](https://www.ibm.com/mysupport).

## Funciones de accesibilidad

Las características de accesibilidad ayudan a los usuarios que tienen alguna discapacidad física, por ejemplo movilidad restringida o visión limitada, a utilizar productos de tecnología de la información. La documentación de OpenPages tiene características de accesibilidad. Los documentos PDF son complementarios y no incluyen características de accesibilidad.

## Cómo empezar

`Guía de actualización para Db2 (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ugdpo-getting-started)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Lea esta sección para preparar la actualización de los despliegues de OpenPages®.

### Ubicaciones de instalación

`Guía de actualización para Db2 (solo en local) › Cómo empezar` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=gs-installation-locations)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

El directorio de instalación es la ubicación de los artefactos de producto una vez está instalado un paquete, producto o componente. La tabla siguiente lista las convenciones que se utilizan para hacer referencia a la ubicación de instalación de componentes y productos instalados:

> **Importante:** las ubicaciones de directorio que contienen espacios no están soportadas. IBM OpenPages® o cualquier software que utilice no debe instalarse en un directorio con espacios. Por ejemplo, no instale el servidor de bases de datos, el cliente de bases de datos o el software del servidor de aplicaciones en el directorio `Program Files` .

Si utiliza IBM OpenPages for IBM Cloud Pak for Data, consulte [Archivos y directorios en IBM OpenPages for IBM Cloud Pak for Data](https://www.ibm.com/docs/SSQNUZ_4.7.x/svc-openpages/openpages_files_dirs.html).

**Tabla 1. Notaciones variables para los directorios de instalación**

| Directorio | Descripción |
| --- | --- |
| `<installation_server_home>` | El directorio donde está instalado el servidor de instalación de IBM OpenPages .<br>Por ejemplo:<br>• En Windows: `C:\IBM\OPInstall\OP_<version>_Installer`.<br>• En Linux®: `/home/opuser/IBM/OPInstall/OP_<version>_Installer`. |
| `<agent_home>` | El directorio donde está instalado el agente de instalación de IBM OpenPages en un servidor remoto.<br>Por ejemplo:<br>• En Windows: `C:\IBM\OPAgent`.<br>• En Linux: `/home/opuser/IBM/OPAgent`. |
| `<OP_HOME>` | El directorio donde está instalado OpenPages .<br>Por ejemplo:<br>• En Windows: `C:\IBM\OpenPages`.<br>• En Linux: `/opt/opuser/IBM/OpenPages`.<br>En la aplicación de instalación, especifique el directorio `<OP_HOME>` en el campo **Directorio de inicio de OP** cada tarjeta de **Servidor de aplicaciones** . |
| `<DB2_HOME>` | La ubicación de instalación del software IBM® Db2® .<br>Por ejemplo:<br>• En Windows: `C:\IBM\SQLLIB`.<br>• En Linux: `/home/db2inst1/sqllib`. |
| `<WLP_HOME>` | La ubicación de instalación de IBM WebSphere® Liberty.<br>Por ejemplo:<br>• En Windows: `<OP_HOME>\wlp`.<br>• En Linux: `<OP_HOME>/wlp`. |
| `<WLP_USER_HOME>` | La ubicación de los archivos de aplicación OpenPages y los archivos de configuración del servidor.<br>Por ejemplo:<br>• En Windows: `<OP_HOME>\wlp-usr`.<br>• En Linux: `<OP_HOME>/wlp-usr`. |
| `<COGNOS_HOME>` | La ubicación de instalación de IBM Cognos® Analytics.<br>Por ejemplo:<br>• En Windows: `C:\IBM\cognos\analytics`.<br>• En Linux: `/usr/IBM/cognos/analytics`. |
| `<JAVA_HOME>` | La ubicación de instalación de IBM SDK, Java™ Technology Edition o Java Runtime Environment (JRE).<br>Ejemplo de IBM SDK en un servidor de aplicaciones:<br>• En Windows: `C:\IBM\java_8.0_64`.<br>• En Linux: `/opt/IBM/java_8.0_64`.<br>Ejemplo de JRE en un servidor de informes donde está instalado IBM Cognos Analytics :<br>• En Windows: `C:\IBM\cognos\analytics\ibm-jre\jre`.<br>• En Linux: `/usr/IBM/cognos/analytics/ibm-jre/jre`.<br>Ejemplo de IBM SDK en un servidor de búsqueda:<br>• En Windows: `C:\IBM\java_8.0_64\`.<br>• En Linux: `/opt/IBM/java_8.0_64/`. |
| `<CC_HOME>` | La ubicación de instalación de OpenPages CommandCenter.<br>Por ejemplo:<br>• En Windows: `C:\IBM\OpenPages\CommandCenter`.<br>• En Linux: `/opt/IBM/OpenPages/CommandCenter`. |
| `<SEARCH_HOME>` | Ubicación de instalación de la búsqueda global.<br>El directorio `<SEARCH_HOME>` contiene los archivos `opsearchtools.jar`, Apache Solr y otros archivos de búsqueda global. El directorio de indexación de búsqueda global también se almacena en el directorio `<SEARCH_HOME>`.<br>Por ejemplo:<br>• En Windows: `C:\IBM\OpenPages\OPSearch`.<br>• En Linux: `/opt/IBM/OpenPages/OPSearch`.<br>En la aplicación de instalación, especifique el directorio `<SEARCH_HOME>` en el campo de **directorio de inicio de búsqueda** en la tarjeta de **servidor de búsqueda**. |

### Cambios realizados en el proceso de instalación

`Guía de actualización para Db2 (solo en local) › Cómo empezar` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=gs-changes-installation-process)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si ha instalado versiones anteriores de IBM OpenPages®, observará muchas diferencias. A partir de la versión 8.3, la IU estándar ya no está soportada y se ha eliminado de OpenPages.

Las secciones siguientes describen los cambios principales que afectan a la instalación, actualización y migración.

#### Cambios en el proceso de instalación en 9.0.0.1

Los scripts de actualización de base de datos para fixpacks se encuentran ahora en los directorios siguientes:

- `<fix_pack_kit>/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/UPGRADE_SCRIPTS`

#### Cambios en el proceso de instalación en 9.0

Revise los cambios siguientes:

- **Java™ en servidores de informes**

  En OpenPages 9.0.x, ya no es necesario utilizar el JRE que se proporciona con IBM® Cognos® Analytics para los servidores de informes. Puede utilizar cualquiera de las opciones siguientes:

  - Utilice el JRE que se proporciona con IBM Cognos Analytics
  - Utilice el SDK deIBM que se proporciona en el soporte de instalación
  - Utilice su propio Java.

    > **Importante:** Si desea utilizar su propio Java, asegúrese de que cumple los requisitos de Java para Cognos. Para obtener más información, consulte la [documentación deCognos](https://www.ibm.com/support/knowledgecenter/en/SSEP7J_11.2.0/com.ibm.swg.ba.cognos.inst_cr_winux.doc/c_inst_updatethejavaenvironment.html#inst_UpdatetheJavaEnvironment).

  En la versión 8.3, el JRE que se proporciona con IBM Cognos Analytics se tenía que utilizar para los servidores de informes.

Los scripts de actualización de base de datos ya no requieren `apache-ant-1.10.12`.

#### Cambios en el proceso de instalación en 8.3.x

Si está actualizando o migrando desde 8.2, revise también estos cambios:

- **Cambios en el servidor de instalación y la aplicación**

  - Las operaciones **Copia de seguridad** y **Restaurar** se han eliminado de la aplicación de instalación. La tarea `file-migration` en el archivo `deploy.properties` ya no está soportada.

- **Archivos de aplicación**

  Los archivos de aplicación están ahora en `taskui.war`. Se han eliminado `openpages.war` y `sosa.war`.

  Durante una actualización, el servidor de instalación realiza una copia de seguridad de los archivos personalizados que están en `sosa.war` y los restaura en `taskui.war`.

  Durante una migración, debe realizar una copia de seguridad de los archivos personalizados y restaurarlos manualmente.

- **Ubicación de los JSP personalizados**

  En 8.2.x, las JSP personalizadas se han almacenado en las ubicaciones siguientes:

  ```xml
  <OP_HOME>/wlp-usr/shared/apps/op-apps.ear/openpages.war
  ```

  ```xml
  <OP_HOME>/wlp-usr/shared/apps/op-apps.ear/publishweb.war
  ```

  ```xml
  <OP_HOME>/wlp-usr/shared/apps/op-apps.ear/sosa.war
  ```

  Ahora, los JSP personalizados se almacenan en las siguientes ubicaciones:

  ```xml
   <OP_HOME>/wlp-usr/shared/apps/op-apps.ear/publishweb.war
  ```

  ```xml
  <OP_HOME>/wlp-usr/shared/apps/op-apps.ear/taskui.war
  ```

- **Generación de entorno**

  OpenPages ya no utiliza el servicio `IBMOpenPagesFrameworkModelGenerator`. OpenPages ahora utiliza el SDK de Cognos para generar la infraestructura. Tenga en cuenta los cambios siguientes:

  - `BmtScriptPlayer.sh` ya no se utiliza.
  - El servicio `IBMOpenPagesFrameworkModelGenerator` ya no se utiliza.
  - Si utiliza Oracle y sólo utiliza modelos de entorno DQM, el software de cliente Oracle de 32 bits ya no es necesario.

    Si está actualizando o migrando y desea continuar utilizando modelos CQM, el cliente Oracle de 32 bits sigue siendo necesario.
  - Los archivos y carpetas para la generación de entorno se almacenan ahora en los servidores de aplicaciones de OpenPages. Las carpetas `framework`, `FrameworkGeneration` y `wlp` se han eliminado del servidor de informes, junto con los archivos relacionados con el entorno.

    Por ejemplo, los asuntos de consulta de modelo ahora se almacenan en `<OP_HOME>/aurora/framework/conf/mqs`. Anteriormente, se almacenaban en el servidor de informes en el directorio `<CC_HOME>/framework/conf/mqs`.
  - La mayoría de las propiedades se han eliminado del archivo `framework.properties`. Las propiedades restantes son:

    - `datasource`
    - `database.schema`
    - `security.namespace`
  - La propiedad `cognos.framework.refresh.servlet` se ha eliminado del archivo `aurora.properties`.
  - Los campos **Puerto de infraestructura** y **Directorio de salida de infraestructura** se han eliminado de las tarjetas **Servidor de informes** en la aplicación de instalación. Además, las propiedades `framework_port` y `framework_output_directory` se han eliminado del archivo `deploy.properties`.

- **Ubicación de Java en servidores de informes**

  En OpenPages 8.3, debe utilizar el JRE que se proporciona con IBM Cognos Analytics para los servidores de informes. Además, ya no es necesario copiar el archivo `bcprov-jdk15to18-1.nn.jar` del servidor de aplicaciones a los servidores de informes.

### Caracteres especiales en las contraseñas

`Guía de actualización para Db2 (solo en local) › Cómo empezar` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=gs-special-characters-in-passwords)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede utilizar determinados caracteres especiales en determinadas contraseñas.

Los caracteres especiales que puede utilizar en las contraseñas son:

```
. + - [ ] * ~ _ # : ?
```

> **Nota:** Los espacios no están soportados.

Puede utilizar estos caracteres especiales en las contraseñas de usuario de bases de datos y las cuentas de sistemas operativos de propietarios de esquemas de base de datos.

Si utiliza caracteres especiales en una contraseña, debe entrecomillar la contraseña. Utilice la siguiente sintaxis:

- **Series de conexión de IBM® Db2®**

  Para bases de datos Db2 , cuando proporcione una contraseña en una serie de conexión, utilice la sintaxis siguiente:

  En Linux®, utilice `\'` alrededor de la contraseña. Por ejemplo:

  ```
  clpplus -nw openpage/\'DB~Password\'@host:50000/opx
  ```

  En Windows, utilice comillas simples alrededor de la contraseña:

  ```
  clpplus -nw openpage/'DB~Password'@host:50000/opx
  ```

- **IBM Db2 en CLPPlus**

  Para bases de datos Db2 , cuando proporcione una contraseña en un parámetro de script, utilice la sintaxis siguiente:

  En Linux, utilice una de las opciones siguientes:

  - Utilice `\'` alrededor de la contraseña. Por ejemplo:

    ```
    clpplus -nw @sql-wrapper CustomIndexing_Step1_AddTextIndexing_to_DB.sql /tmp/log.log c6de0652985e:50000/OPX db2inst1 \'DB~Password\' openpage
    ```
  - Utilice `\"` alrededor de la contraseña:

    ```
    clpplus -nw @sql-wrapper CustomIndexing_Step1_AddTextIndexing_to_DB.sql /tmp/log.log c6de0652985e:50000/OPX db2inst1 \"DB~Password\" openpage
    ```

  En Windows, utilice una de las opciones siguientes:

  - Utilice `'` alrededor de la contraseña. Por ejemplo:

    ```
    clpplus -nw @sql-wrapper CustomIndexing_Step1_AddTextIndexing_to_DB.sql /tmp/log.log server.corp.com:50000/OPX db2admin 'DB~Password' openpage
    ```
  - Utilice `\"` alrededor de la contraseña:

    ```
    clpplus -nw @sql-wrapper CustomIndexing_Step1_AddTextIndexing_to_DB.sql /tmp/log.log server.corp.com:50000/OPX db2admin \"DB~Password\" openpage
    ```

- **Utilidades de Db2**

  Cuando ejecute programas de utilidad de Db2 , como `db2 connect` o `db2rbind`, no utilice comillas alrededor de las contraseñas.

- **Scripts de instalación, herramientas y programas de utilidad**

  En herramientas y programas de utilidad que aceptan la contraseña como parámetro, utilice la sintaxis siguiente:

  - En Windows, utilice comillas dobles alrededor de la contraseña.

    ```
    op-validate-dba-install.bat "DB~Password"
    ```
  - En Linux, utilice comillas simples alrededor de la contraseña.

    ```bash
    ./op-validate-dba-install.sh 'DB~Password'
    ```

- **Contraseñas en archivos de propiedad**

  En los archivos `.env` y los archivos `.properties`, no utilice comillas alrededor de las contraseñas.

## Determinar la ruta de actualización

`Guía de actualización para Db2 (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=only-determine-your-upgrade-path)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Utilice esta lista para determinar las opciones para actualizar IBM OpenPages®.

- **Si el entorno de origen tiene la versión 8.2.x o 8.3.x**

  Tiene dos opciones:

  - Actualización (también denominada actualización «“in situ”» o «“superpuesta”»).

    Con esta opción, instala la versión 9.0 encima del despliegue existente. Consulte [Preparación para la actualización](#preparación-de-la-actualización).
  - Actualización con migración

    Con esta opción, realiza una instalación nueva de 9.0 y, a continuación, migra archivos y datos. Consulte la publicación [*IBM OpenPages Guía de instalación y despliegue*](5.1-guia-de-instalacion-y-despliegue-solo-local.md#determinación-de-la-ruta-de-instalación).

    Utilice esta opción, por ejemplo, si desea utilizar hardware nuevo.

- **Si el entorno de origen tiene la versión 8.1.x o anterior**

  Primero debe actualizar o migrar a 8.2.x o 8.3.x. A continuación, puede actualizar o migrar a 9.0.

## Preparación de la actualización

`Guía de actualización para Db2 (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=only-prepare-upgrade)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Prepare la actualización de IBM OpenPages®.

> **Nota:** Estos temas sólo se aplican a las actualizaciones in situ. Si está migrando a 9.0, consulte la publicación *IBM OpenPages Guía de instalación y despliegue*. Para obtener más información sobre las vías de acceso de actualización, consulte [Determinar la vía de acceso de actualización](#determinar-la-ruta-de-actualización).

### Revisión de las características y arreglos nuevos

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrade-review-new-features-fixes)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de actualizar OpenPages®, revise las nuevas características y arreglos.

Para obtener más información sobre las nuevas características, consulte la versión más reciente de la [Guía de características nuevas](2-caracteristicas-nuevas.md#características-nuevas) .

Para obtener información adicional sobre OpenPages, consulte la versión más reciente de las [Notas del release](1-notas-del-release.md#notas-del-release) .

Puede encontrar información sobre las correcciones de defectos en la [Lista de arreglos](https://www.ibm.com/support/pages/node/6998091).

Asegúrese de revisar la siguiente información antes de actualizar: [Problemas críticos de instalación y configuración para IBM OpenPages](https://www.ibm.com/support/pages/node/6212189).

### Copia de seguridad del entorno

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrade-backing-up-your-environment)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de actualizar, haga una copia de seguridad de IBM OpenPages®.

#### Acerca de esta tarea

Al realizar una actualización, el servidor de instalación realiza automáticamente una copia de seguridad de la mayoría de los archivos. Sin embargo, es necesario realizar una copia de seguridad manual de algunos de archivos. También es necesario realizar una copia de seguridad de las bases de datos, el directorio `openpages-storage` y los archivos que haya personalizado, como por ejemplo informes y JSP.

#### Procedimiento

1. Pare los servidores de aplicaciones (administrativos y no administrativos), los servidores de informes (activos y en espera), el servidor de bases de datos y el servidor de búsquedas (si utiliza la búsqueda global).
2. Haga una copia de seguridad de la base de datos de OpenPages .

   Para obtener más información, consulte [Copia de seguridad de la base de datos OpenPages (Db2)](#copia-de-seguridad-de-la-base-de-datos-openpages-db2).
3. Haga una copia de seguridad del almacén de contenido de Cognos® .

   Para obtener más información, consulte [Copia de seguridad de la base de datos de Cognos (Db2)](#copia-de-seguridad-de-la-base-de-datos-de-cognos-db2).
4. Haga una copia de seguridad del directorio `openpages-storage` .

   El directorio `openpages-storage` se puede localizar en un servidor en el despliegue o puede ser una compartición de red independiente.

   La ubicación predeterminada es `<OP_HOME>/openpages-storage`.
5. En cada servidor de aplicaciones, como usuario de instalación de OpenPages (`opuser`), cree una copia de seguridad del directorio `OpenPages` de nivel superior. Asigne el nombre `OpenPages-<current-version>`a la copia de seguridad. Por ejemplo, si está actualizando desde la versión 8.2.0.1, asigne el nombre `OpenPages-8201`a la copia de seguridad.

   > **Nota:** No elimine ni cambie el nombre del directorio `OpenPages` .

   Si ha realizado cambios en los archivos `<OP_HOME>/aurora/conf/Server<#>-server.properties` y `Server<#>-sosa.properties`, puede utilizar las copias de seguridad para restaurar los cambios después de la actualización.

   También puede utilizar este directorio de copia de seguridad para restaurar la versión actual de OpenPages si necesita retrotraer la actualización.
6. En cada servidor de informes, como usuario de instalación de OpenPages (`opuser`), cree una copia de seguridad del directorio `CommandCenter` de nivel superior. Asigne el nombre `CommandCenter-<current-version>`a la copia de seguridad. Por ejemplo, si está actualizando desde la versión 8.2.0.1, asigne el nombre `CommandCenter-8201`a la copia de seguridad.

   > **Nota:** No elimine ni cambie el nombre del directorio `CommandCenter` .

   Puede utilizar este directorio de copia de seguridad para restaurar el directorio actual de `<CC_HOME>` si necesita retrotraer la actualización.
7. En el servidor de búsqueda, como usuario de instalación de OpenPages (`opuser`), cree una copia de seguridad del directorio `OpenPages` de nivel superior. Asigne el nombre `OpenPages-Search-<current-version>`a la copia de seguridad. Por ejemplo, si está actualizando desde la versión 8.2.0.1, asigne el nombre `OpenPages-Search-8201`a la copia de seguridad.

   > **Nota:** No elimine ni cambie el nombre del directorio `OpenPages` .

   Puede utilizar este directorio de copia de seguridad para restaurar la versión actual del servidor de búsqueda si tiene que retrotraer la actualización.
8. Si ha modificado los informes estándar que se proporcionan con OpenPages, cópielos en una carpeta de copia de seguridad o en sus carpetas personales.

   Los informes estándar de OpenPages se pueden sobrescribir al actualizar.

   Una vez que se haya completado la actualización, puede cambiar los informes y restringir el acceso a ellos.
9. Si ha personalizado otros archivos como, por ejemplo, JSP, haga copia de seguridad de los mismos.

#### Copia de seguridad de la base de datos OpenPages (Db2)

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Copia de seguridad del entorno` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=environment-backing-up-openpages-database-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Cree una copia de seguridad de la base de datos de OpenPages® .

##### Antes de empezar

Si Db2® Text Search está habilitado en el entorno de origen, descarte los índices de búsqueda de texto e inhabilite Db2 Text Search antes de realizar una copia de seguridad de la base de datos.

##### Acerca de esta tarea

Utilice los programas de utilidad que se proporcionan con IBM® Db2 para realizar una copia de seguridad de la base de datos.

> **Nota:** Puede realizar una copia de seguridad de la base de datos utilizando otros métodos. Por ejemplo, puede utilizar una combinación de las copias de seguridad completas e incrementales. Si desea utilizar un método alternativo, es fundamental que tenga las habilidades necesarias disponibles dentro su organización para completar todos los aspectos de la copia de seguridad y la restauración de la actividad.

Para obtener información sobre el desarrollo de una estrategia de copia de seguridad y restauración de base de datos, consulte [Visión general de la copia de seguridad](http://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.admin.ha.doc/doc/c0006150.html) en la documentación de Db2 .

Para obtener más información sobre los mandatos que se utilizan en este procedimiento, consulte la [documentación deIBM Db2](http://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/).

##### Procedimiento

1. Asegúrese de que no haya procesos de OpenPages en ejecución, como trabajos de restablecimiento de objetos.
2. Concluir todos los componentes de OpenPages : servidores de aplicaciones (admin y no admin), servidores de informes (activos y en espera) y el servidor de búsqueda.

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
3. Abra una ventana de mandatos o shell y conéctese a la base de datos OpenPages como propietario de la instancia de base de datos.

   Sólo para usuarios de Windows , debe utilizar el mandato `db2cmd` en la ventana **Indicador de mandatos** para inicializar el procesador de línea de mandatos (CLP) de Db2 .
4. Vaya al directorio `sqllib` .
5. Fuerce todas las aplicaciones desde la base de datos.

   Ejecute el mandato siguiente:

   ```
   db2 force application all
   ```
6. Desactive la base de datos.

   Ejecute el mandato siguiente:

   ```
   db2 deactivate database <db_name>
   ```
7. Cree un directorio en el que almacenar la copia de seguridad.
8. Realice una copia de seguridad fuera de línea utilizando el mandato `db2 backup` .

   ```
   db2 backup database <db_name> to <backup_directory>
   ```

   Ejemplo:

   ```
   db2 backup database opx to /home/db2inst1/backup
   ```

#### Copia de seguridad de la base de datos de Cognos (Db2)

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Copia de seguridad del entorno` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=environment-backing-up-cognos-database-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Cree una copia de seguridad de la base de datos de Cognos® . Realice este procedimiento si utiliza una base de datos independiente para Cognos.

##### Acerca de esta tarea

Utilice los programas de utilidad que se proporcionan con IBM® Db2® para realizar una copia de seguridad de la base de datos.

> **Nota:** Puede realizar una copia de seguridad de la base de datos utilizando otros métodos. Por ejemplo, puede utilizar una combinación de las copias de seguridad completas e incrementales. Si desea utilizar un método alternativo, es fundamental que tenga las habilidades necesarias disponibles dentro su organización para completar todos los aspectos de la copia de seguridad y la restauración de la actividad.

Para obtener información sobre el desarrollo de una estrategia de copia de seguridad y restauración de base de datos, consulte [Visión general de la copia de seguridad](http://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.admin.ha.doc/doc/c0006150.html) en la documentación de Db2 .

Para obtener más información sobre los mandatos que se utilizan en este procedimiento, consulte la [documentación de IBM DB2®](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/).

##### Procedimiento

1. Concluir todos los componentes de OpenPages® : servidores de aplicaciones (admin y no admin), servidores de informes (activos y en espera) y el servidor de búsqueda.

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
2. Asegúrese de que todos los componentes de Cognos estén apagados.
3. Abra una ventana de mandatos o shell y conéctese a la base de datos de Cognos como propietario de instancia de base de datos.

   Sólo para usuarios de Windows , debe utilizar el mandato `db2cmd` en la ventana **Indicador de mandatos** para inicializar el procesador de línea de mandatos (CLP) de Db2 .
4. Vaya al directorio `sqllib` .
5. Fuerce todas las aplicaciones desde la base de datos.

   Ejecute el mandato siguiente:

   ```
   db2 force application all
   ```
6. Desactive la base de datos.

   Ejecute el mandato siguiente:

   ```
   db2 deactivate database <db_name>
   ```
7. Cree un directorio en el que almacenar la copia de seguridad.
8. Realice una copia de seguridad fuera de línea utilizando el mandato `db2 backup` .

   ```
   db2 backup database <db_name> to <backup_directory>
   ```

   Ejemplo:

   ```
   db2 backup database cognosdb to /home/db2inst2/backup
   ```

#### Copia de seguridad de asistentes de soluciones, imágenes y otros archivos

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Copia de seguridad del entorno` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=environment-backing-up-solutions-helpers-images-other-files)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Haga una copia de seguridad de los asistentes de soluciones, imágenes y entregas personalizadas.

##### Acerca de esta tarea

Realice esta tarea si se aplica alguna de las condiciones siguientes:

- Ha instalado el esquema de soluciones
- Ha recibido entregas personalizadas de IBM® Expert Labs
- Tiene código personalizado

##### Procedimiento

1. Cree un directorio de copia de seguridad.

   Por ejemplo, `C:\OpenPages<current_version>\patch\helper_backup`.
2. Copie las JSP de asistente personalizadas, las imágenes y el código personalizado en el directorio de copia de seguridad para poder restaurarlos más tarde.

### Actualizar software de requisito previo

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrade-prerequisite-software)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de actualizar, actualice el software que necesita IBM OpenPages®

Revise los requisitos previos de software para los servidores de aplicaciones, los servidores de informes, el servidor de base de datos y el servidor de búsqueda. Para obtener más información, consulte [Requisitos previos de software](5.1-guia-de-instalacion-y-despliegue-solo-local.md#requisitos-previos-de-software).

- **Obligatorio**

  - Actualice a una versión soportada de IBM® Db2®. La versión 11.5.5 es la versión mínima soportada para OpenPages 9.0. Ver [Actualizar o actualizar Db2](#actualizar-o-actualizar-db2).
  - Actualice IBM Cognos® Analytics a la versión 11.2.1 o a un release continuo posterior. Puede realizar una actualización in situ, también denominada actualización «“superpuesta”». Consulte [Actualización de Cognos](#actualización-de-cognos).
  - Instale IBM SDK, Java™ Technology Edition en cada servidor de aplicaciones y en el servidor de búsqueda. Para obtener más información, consulte [Obtención de una copia de IBM SDK (Windows)](#obtención-de-una-copia-del-sdk-de-ibm-windows) o [Obtención de una copia de IBM SDK (Linux)](#obtención-de-una-copia-de-ibm-sdk-linux).

- **Opcional**

  - Instale los fixpacks de IBM Db2 . Puede instalar los fixpacks antes o después de actualizar OpenPages.

Además, asegúrese de que los usuarios tienen un navegador soportado.

Si utiliza aplicaciones y componentes opcionales, como IBM OpenPages SDI Connector for UCF Common Controls Hub, puede actualizarlos después de actualizar OpenPages.

#### Actualizar o actualizar Db2

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Actualizar software de requisito previo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=software-upgrade-update-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si estas usando IBM® Db2®, asegúrese de estar utilizando una versión compatible. La versión 11.5.5 es la versión mínima soportada para IBM OpenPages® 9.0.

- **Si estas usando Db2 11.5.x**

  Aplique el paquete de correcciones 11.5.5, 11.5.8 o un paquete de correcciones 11.5.x posterior. También puede instalar compilaciones especiales acumulativas. Para obtener más información, consulte [Instalación de un Db2 fix pack (Windows)](#instalación-de-un-db2-fix-pack-windows) o [Aplicación de fix packs en entornos de bases de datos Db2](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.qb.server.doc/doc/t0006352.html).

  Se construye una compilación especial acumulativa basada en la última versión e incorpora correcciones.

  Puedes aplicar un Db2 11.5.x fixpack antes o después de la instalaciónOpenPages , actualizar a 9.0, o migrar a 9.0.

  > **Ejemplo:** Si usted tiene`DB2/LINUXX8664 11.5.5.0` , instalar`DB2/LINUXX8664 11.5.8.0` .

- **Si estas usando Db2 11.x**

  Siga los pasos siguientes:

  1. Actualizar a 11.5.

     Para obtener más información, consulte [Actualización de Db2 (Linux)](#actualización-de-db2-linux) o [Actualización de Db2 (Windows)](#actualización-de-db2-windows).
  2. Aplicar paquete de arreglos 11.5.5 o después.

     Para obtener más información, consulte [Instalación de un Db2 fix pack (Windows)](#instalación-de-un-db2-fix-pack-windows) o [Aplicación de fix packs en entornos de bases de datos Db2](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.qb.server.doc/doc/t0006352.html).

  > **Ejemplo:** Si usted tiene`DB2/LINUXX8664 11.5.x.x` , actualizar a`DB2/LINUXX8664 11.5` y luego instalar`DB2/LINUXX8664 11.5.8.0` .

##### Instalación de un Db2 fix pack (Windows)

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Actualizar software de requisito previo › Actualizar o actualizar Db2` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uud-installing-db2-fix-pack-windows)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Aplique paquetes de correcciones para asegurarse de que IBM® Db2® está actualizado.

Realice esta tarea cuando desee actualizar de Db2 11.5.x a un fix pack posterior 11.5.x.

###### Antes de empezar

- Revisa el siguiente tema: [Aplicación de paquetes de correcciones en entornos de bases de datos Db2](https://www.ibm.com/docs/SSEPGG_11.5.0/com.ibm.db2.luw.qb.server.doc/doc/t0006352.html).
- Descargue el paquete de reparación Db2. Para obtener más información, consulte [Obtención de paquetes de correcciones](https://www.ibm.com/docs/SSEPGG_11.5.0/com.ibm.db2.luw.qb.server.doc/doc/t0024972.html).

###### Procedimiento

1. Ejecute el comando `db2prereqcheck` para verificar que su sistema cumple los requisitos previos de instalación.

   Para obtener más información, consulte [db2prereqcheck - Comprobar los requisitos previos de instalación](http://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0059710.html).

   ```
   db2prereqcheck -v <version>
   ```

   Donde `<version>` es la versión de Db2 que desea instalar.

   Este ejemplo muestra el comando para 11.5.8:

   ```
   cd C:\Users\Administrator\Desktop\v11.5.8_ntx64_universal_fixpack\UNIVERSAL
   db2prereqcheck -v 11.5.8.0
   ```
2. Obtenga una lista de las instancias de base de datos que están vinculadas a la instalación de Db2 ejecutando el comando `db2ilist`:

   ```
   cd <DB2PATH>\bin\
   db2ilist
   ```

   Donde `<DB2PATH>` es el directorio de instalación de Db2.

   Por ejemplo:

   ```bat
   C:\IBM\SQLLIB\BIN>db2ilist
   ```

   El script devuelve una lista de instancias, por ejemplo:

   ```
   DB2INST2
   DB2INST1
   ```
3. Detén todos los servicios Db2 mediante la aplicación **Servicios**.

   Para abrir la aplicación, haz clic en **Panel de control** > **Herramientas administrativas** > **Servicios**.
4. Detén las instancias de la base de datos ejecutando el comando `db2stop`:

   ```
   cd <DB2PATH>\bin\
   db2stop
   ```

   Donde `<DB2PATH>` es el directorio de instalación de Db2.

   Por ejemplo:

   ```bat
   C:\IBM\SQLLIB\BIN>db2stop
   ```

   El comando `db2stop` también garantiza la desconexión de cualquier cliente de base de datos activo.
5. Ve al directorio donde extrajiste el kit fix pack.
6. Vaya al directorio de su producto Db2 y localice el comando setup.

   Por ejemplo, el comando `setup` para Db2 Enterprise Server Edition se encuentra en el directorio `SERVER`.

   ```bat
   C:\fixpackinstall\SERVER\Universal\setup
   ```
7. Haz doble clic en el archivo `setup.exe`.
8. Haga clic en **Instalar un producto** y **Trabajar con el existente**.

   Cuando se complete el proceso de instalación, compruebe los archivos de registro.
9. Reinicie los servicios Db2 mediante la aplicación **Servicios**.
10. Inicie las instancias de la base de datos ejecutando el comando `db2start`:

    ```
    cd <DB2PATH>\bin\
    db2start
    ```

    Donde `<DB2PATH>` es el directorio de instalación de Db2.

    Por ejemplo:

    ```bat
    C:\IBM\SQLLIB\BIN>db2start
    09/11/2025 17:51:31     0   0   SQL1063N  DB2START processing was successful.
    SQL1063N  DB2START processing was successful.
    ```

##### Actualización de Db2 (Windows)

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Actualizar software de requisito previo › Actualizar o actualizar Db2` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uud-upgrading-db2-windows)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Debe actualizar a una versión soportada de IBM® Db2® antes de migrar o actualizar a IBM OpenPages® 9.0.

Realiza esta tarea si utilizas una versión anterior a 11.5.x. Para obtener más información, consulte [Actualización o actualización de Db2](#actualizar-o-actualizar-db2).

Esta tarea proporciona los pasos básicos para actualizar IBM Db2. Para obtener más información sobre este proceso, consulte la [IBM Db2 documentación](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/c0023662.html).

###### Acerca de esta tarea

Esta tarea utiliza los siguientes convenios:

- `db2admin`: propietario de la instancia de base de datos OpenPages
- `openpage`: El usuario de base de datos OpenPages
- `opx`: el nombre de la base de datos OpenPages
- `db2inst2`: el propietario de la instancia de base de datos de Cognos®
- `cognosdb`: El nombre del almacén de contenido de Cognos
- `<db_server>`: el nombre de host del servidor de bases de datos Db2

Los pasos que debe realizar dependen de si está utilizando el servidor de bases de datos existente para OpenPages o si está utilizando un nuevo servidor de bases de datos. Si está utilizando un nuevo servidor de bases de datos, omita los pasos sobre la actualización de las instancias de base de datos y la actualización de las bases de datos. Más adelante en el proceso de migración de OpenPages , restaure las bases de datos y, a continuación, actualícelas a la nueva versión de Db2 .

> **Nota:** Cuando ejecute programas de utilidad de Db2 , como `db2 connect` o `db2rbind`, no utilice comillas alrededor de las contraseñas.

###### Procedimiento

1. Detenga los siguientes servidores:

   - Detenga todos los servidores de aplicaciones de OpenPages .
   - Detenga los servicios de búsqueda global.
   - Detenga todos los servicios de IBM Cognos .
2. Compruebe que el sistema cumple con los requisitos previos de instalación.

   Para obtener más información, consulte [db2prereqcheck - Comprobar los requisitos previos de instalación](http://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0059710.html).

   1. Vaya al directorio donde ha extraído el paquete de instalación de Db2 .
   2. Como usuario root o `sudo` , compruebe los requisitos de instalación.

      ```
      db2prereqcheck –i -v <version>
      ```

      Donde `<version>` es la versión de Db2 que desea instalar.

      Por ejemplo:

      ```
      db2prereqcheck –i -v 11.5.5.0
      ```

      Si se realiza correctamente, verá el mensaje `DBT3533I The db2prereqcheck utility has confirmed that all installation prerequisites were met.`
   3. Revise el archivo de registro.
   4. Como propietario de la instancia de OpenPages (por ejemplo, db2admin), ejecute las comprobaciones previas a la actualización:

      ```
      db2ckupgrade OPX -l c:\tmp\db2ckupgrade.log -u db2admin -p password
      ```
3. Complete las tareas previas a la actualización de Db2 para la base de datos OpenPages y el almacén de contenido de Cognos . Para obtener más información, consulte [Tareas previas a la actualización para servidores Db2](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0050541.html).

   Si recibe avisos sobre la función `SYSFUN.ASCII1` que se ha dejado de mantener, puede ignorarlos.
4. Compruebe el valor del tamaño de almacenamiento dinámico de la aplicación para la base de datos de Cognos .

   1. Abra el procesador de línea de mandatos (CLP) de Db2 .
   2. Ejecute el siguiente mandato como propietario de la instancia de base de datos. Sustituya `<cognosdb>` por el nombre de la base de datos de Cognos .

      ```
      db2 get db cfg for <cognosdb> | findstr APPLHEAPSZ
      ```
   3. Si el valor es inferior a 4096, increméntelo hasta un mínimo de 4096.

      Ejecute el siguiente mandato como propietario de la instancia de base de datos. Sustituya `<cognosdb>` por el nombre de la base de datos de Cognos .

      ```
      db2 update db cfg for <cognosdb> using applheapsz 4096
      ```
5. Descarte el índice de Db2 Text Search e inhabilite Db2 Text Search.

   Para obtener más información, consulte [Eliminación del índice de búsqueda y desactivación de Db2](#descarte-del-índice-de-búsqueda-e-inhabilitación-de-db2-text-search).
6. Haga una copia de seguridad de la base de datos de OpenPages y del almacén de contenido de Cognos .
7. Ejecute el programa de instalación de IBM Db2 .

   El programa de instalación instala Db2 y actualiza las instancias de base de datos existentes. Para obtener más información, consulte [Actualización de un servidor DB2® (Windows)](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0007199.html).

   1. Pulse **Instalar un producto**.
   2. Pulse **Trabajar con existente**.
   3. Seleccione la instalación que utiliza para OpenPages.
   4. Seleccione la opción **Personalizado** .
   5. Expanda **Server Support** y seleccione **Db2 Text Search** para la instalación.
   6. Si no utiliza Tivoli ® SA MP, desmarque el recuadro de selección **Tivoli SA MP** .
   7. Acepte los valores predeterminados en cada página del asistente hasta que se le soliciten las credenciales de **db2admin** .
   8. Escriba el dominio y la contraseña para el usuario db2admin.
   9. Acepte los valores predeterminados en las páginas restantes del asistente. Pulse **Finalizar**.

   Cuando se complete el proceso de instalación, compruebe los archivos de registro.
8. Actualice la base de datos de OpenPages .

   Para obtener más información, consulte [Actualización de bases de datos](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0007193.html).

   Por ejemplo, inicie el procesador de línea de mandatos (CLP) de DB2 y ejecute los mandatos siguientes:

   ```bat
   set db2instance=db2inst1 
   db2start 
   db2 upgrade database opx user db2admin using password
   ```
9. Actualice la base de datos del almacén de contenido de Cognos .

   Para obtener más información, consulte [Actualización de bases de datos](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0007193.html).

   Por ejemplo, inicie el procesador de línea de mandatos (CLP) de DB2 y ejecute los mandatos siguientes:

   ```bat
   set db2instance=db2inst2 
   db2start 
   db2 upgrade database cognosdb user db2admin using password
   ```
10. Revalidar objetos y volver a vincular paquetes en la base de datos de OpenPages .

    1. Inicie el procesador de línea de mandatos (CLP) de Db2 .
    2. Ejecute el mandato siguiente:

       ```bat
       set db2instance=db2inst1
       ```
    3. Copie el directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/INSTALL_SCRIPTS` en el servidor de bases de datos.
    4. Vaya al directorio donde ha copiado el directorio `INSTALL_SCRIPTS` y, a continuación, vuelva a validar los objetos de base de datos.

       Ejecute los mandatos siguientes:

       ```
       db2 connect to OPX user openpage using password
       db2 -td@ -f pks_OP_CURRENCY_MGR.sql
       db2 -td@ -f pkb_OP_CURRENCY_MGR.sql
       clpplus -nw openpage/password@<db_server>:50000/opx @sql-wrapper revalidate.sql revalidate.log openpage
       ```
    5. Vuelva a enlazar los paquetes.

       Por ejemplo:

       ```
       db2rbind opx -l opbind.log all -u db2admin -p password -r any
       ```
11. Revalidar objetos y volver a vincular paquetes en el almacén de contenido de Cognos .

    > **Nota:** Cuando ejecute mandatos de Db2 , como `db2 connect` o `db2rbind`, no utilice comillas alrededor de las contraseñas.

    1. Inicie el procesador de línea de mandatos (CLP) de Db2 .
    2. Ejecute el mandato siguiente:

       ```bat
       set db2instance=db2inst2
       ```
    3. Vuelva a validar los objetos de base de datos.

       Por ejemplo:

       ```
       db2 connect to cognosdb user db2admin using password
       db2 "call sysproc.admin_revalidate_db_objects()"
       ```
    4. Vuelva a vincular los paquetes en la base de datos de Cognos .

       Por ejemplo:

       ```
       db2rbind cognosdb -l cogbind.log -u db2admin -p password
       ```
12. Opcional: Haga una copia de seguridad de las bases de datos.
13. Aplicar la licencia de IBM Db2 .

    1. Extraiga el archivo de activación de inicio rápido para IBM Db2.
    2. Inicie el procesador de línea de mandatos (CLP) de Db2 .
    3. Vaya al directorio donde está almacenado el archivo de licencia, `db2ese_u.lic`.
    4. Ejecute el mandato siguiente:

       ```
       db2licm –a db2ese_u.lic
       ```
14. Inicie todos los servicios de IBM OpenPages .
15. Configure y habilite Db2 Text Search, cree el índice y planifique un trabajo para sincronizar el índice.

    Para obtener más información, consulte «“Programas de utilidad para filtrar contenido de campo de serie larga en una base de datos Db2”» en la publicación *IBM OpenPages Guía del administrador*.

##### Actualización de Db2 (Linux)

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Actualizar software de requisito previo › Actualizar o actualizar Db2` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uud-upgrading-db2-linux)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Debe actualizar a una versión soportada de IBM® Db2® antes de migrar o actualizar a IBM OpenPages® 9.0.

Esta tarea proporciona los pasos básicos para actualizar IBM Db2. Para obtener más información sobre este proceso, consulte la [documentación de IBM Db2](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/c0023662.html).

###### Acerca de esta tarea

Esta tarea utiliza los siguientes convenios:

- `db2inst1`: propietario de la instancia de base de datos OpenPages
- `openpage`: El usuario de base de datos OpenPages
- `opx`: el nombre de la base de datos OpenPages
- `db2inst2`: el propietario de la instancia de base de datos de Cognos®
- `cognosdb`: El nombre del almacén de contenido de Cognos
- `<db_server>`: el nombre de host del servidor de bases de datos Db2

Los pasos que debe realizar dependen de si está utilizando el servidor de bases de datos existente para OpenPages o si está utilizando un nuevo servidor de bases de datos. Si está utilizando un nuevo servidor de bases de datos, omita los pasos sobre la actualización de las instancias de base de datos y la actualización de las bases de datos. Más adelante en el proceso de migración de OpenPages , restaure las bases de datos y, a continuación, actualícelas a la nueva versión de Db2 .

> **Nota:** Cuando ejecute programas de utilidad de Db2 , como `db2 connect` o `db2rbind`, no utilice comillas alrededor de las contraseñas.

###### Procedimiento

1. Detenga los siguientes servidores:

   - Detenga todos los servidores de aplicaciones de OpenPages .
   - Detenga los servicios de búsqueda global.
   - Detenga todos los servicios de IBM Cognos .
2. Monte el soporte de instalación de IBM Db2 o extraiga el paquete de instalación descargado en el sistema de archivos.

   1. Inicie sesión como propietario de la instancia.
   2. Cree un directorio. No lo cree en `/sqllib`.
   3. Extraiga el paquete de instalación de Db2 en el directorio que ha creado.
3. Compruebe que el sistema cumple con los requisitos previos de instalación.

   Para obtener más información, consulte [db2prereqcheck -Comprobar requisitos previos de instalación](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0059710.html).

   1. Vaya al directorio donde ha extraído el paquete de instalación de Db2 .
   2. Como usuario root o `sudo` , compruebe los requisitos de instalación.

      ```bash
      ./db2prereqcheck –i -v <version>
      ```

      Donde `<version>` es la versión de Db2 que desea instalar.

      Por ejemplo:

      ```bash
      ./db2prereqcheck –i -v 11.5.5.0
      ```

      Si se realiza correctamente, verá el mensaje `DBT3533I The db2prereqcheck utility has confirmed that all installation prerequisites were met.`
   3. Revise el archivo de registro.
   4. Como propietario de la instancia de OpenPages (por ejemplo, db2inst1), ejecute las comprobaciones previas a la actualización:

      ```bash
      ./db2ckupgrade OPX -l /tmp/db2ckupgrade.log -u db2inst1 -p password
      ```
4. Complete las tareas previas a la actualización de Db2 para la base de datos de OpenPages y la base de datos de Cognos . Para obtener más información, consulte [Tareas previas a la actualización para servidores Db2](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0050541.html).

   Si recibe avisos sobre la función `SYSFUN.ASCII1` que se ha dejado de mantener, puede ignorarlos.
5. Compruebe el valor del tamaño de almacenamiento dinámico de la aplicación para la base de datos de Cognos .

   1. Ejecute el siguiente mandato como propietario de la instancia de base de datos. Sustituya `<cognosdb>` por el nombre de la base de datos de Cognos .

      ```
      db2 get db cfg for <cognosdb> | grep -i APPLHEAPSZ
      ```
   2. Si el valor es inferior a 4096, increméntelo hasta un mínimo de 4096.

      Ejecute el siguiente mandato como propietario de la instancia de base de datos. Sustituya `<cognosdb>` por el nombre de la base de datos de Cognos .

      ```
      db2 update db cfg for <cognosdb> using applheapsz 4096
      ```
6. Descarte el índice de Db2 Text Search e inhabilite Db2 Text Search.

   Para obtener más información, consulte [Descarte del índice de búsqueda e inhabilitación de Db2 Text Search](#descarte-del-índice-de-búsqueda-e-inhabilitación-de-db2-text-search).
7. Haga una copia de seguridad de la base de datos de OpenPages y de la base de datos de Cognos .
8. Ejecute el programa de instalación de Db2 para actualizar IBM Db2

   Para obtener más información, consulte [Actualización de un servidor Db2 (Linux® y UNIX)](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0007200.html).

   1. Inicie sesión en el servidor de bases de datos como usuario root. Ir al directorio que ha creado en el paso 2. Ejecute el mandato `db2setup` .

      ```bash
      ./db2setup
      ```
   2. Pulse **Instalar un producto** y **Nueva instalación**.
   3. Para el producto , elija **DB2 Versión 11.5 Server Editions**.
   4. Seleccione la opción **Personalizado** .
   5. Realice uno de los pasos siguientes:

      - **Si está pasando a un nuevo servidor de bases de datos**

        Marque la casilla de verificación **Crear una instancia**.

        Por ejemplo, si está migrando a una nueva versión de OpenPages y desea utilizar un nuevo servidor de bases de datos, habilite la opción **Crear una instancia** .

      - **Si utiliza el servidor de bases de datos existente**

        Desmarque la casilla de verificación **Crear una instancia**.

        Por ejemplo, si está actualizando o si está migrando y utiliza el servidor de bases de datos existente, desmarque la casilla de verificación.
   6. Expanda **Server Support** y seleccione **Db2 Text Search** para la instalación.
   7. Si no utiliza Tivoli ® SA MP, desmarque el recuadro de selección **Tivoli SA MP** .
   8. Acepte los valores predeterminados en las páginas restantes del asistente.
   9. Cuando se complete el proceso de instalación, revise los archivos de registro.
   10. Pulse **Finalizar**.
9. Si está actualizando Db2 en el servidor de bases de datos existente, actualice la instancia de base de datos de OpenPages .

   Realice este paso como usuario root. Para obtener más información, consulte la [documentación de Db2](http://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0007196.html?pos=2).

   Si está utilizando un nuevo servidor de bases de datos, vaya al paso 14.

   1. Detenga todas las bases de datos Db2 11.x .
   2. Edite el archivo `/etc/services` y elimine cualquier entrada existente para el servicio de texto Db2 .

      Por ejemplo, elimine `db2j_db2inst1 55000/tcp`, que es la entrada predeterminada.
   3. Actualice la instancia de base de datos de OpenPages .

      Ejecute el mandato `db2iupgrade`. Por ejemplo:

      ```bash
      cd /opt/ibm/db2/V11.5/instance
      ./db2iupgrade -u db2fenc1 -j "TEXT_SEARCH,db2j_db2inst1,55000" db2inst1
      ```
   4. Vea el archivo de registro, por ejemplo `/tmp/db2iupgrade.log.20620`. Compruebe que la actualización se haya realizado correctamente. Busque el mensaje `DBI1070I Program db2iupgrade completed successfully`.
   5. Verifique la actualización.

      ```bash
      cd /opt/ibm/db2/V11.5/bin/
      ./db2val
      ```
   6. Compruebe el nivel de instalación de la instancia de base de datos de OpenPages .

      Para obtener más información, consulte [db2level -Mostrar mandato de nivel de servicio de Db2](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0009195.html).

      ```
      db2level
      ```

      Busque un valor de retorno que coincida con la versión que está instalando. Por ejemplo, busque un valor de retorno de `DB2 v11.5.5.0`.
10. Actualice la instancia de base de datos de Cognos .

    Realice este paso como usuario root

    Para obtener más información, consulte la [documentación de Db2](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0007196.html?pos=2).

    > **Nota:** realice este paso después de que la actualización de la instancia de base de datos de OpenPages se haya completado correctamente.

    1. Actualice la instancia de base de datos de Cognos .

       Ejecute el mandato `db2iupgrade`. Por ejemplo:

       ```bash
       cd /opt/ibm/db2/V11.5/instance
       ./db2iupgrade -u db2fenc1 db2inst2
       ```
    2. Vea el archivo de registro, por ejemplo `/tmp/db2iupgrade.log.18463`. Compruebe que la actualización se haya realizado correctamente. Busque el mensaje `DBI1070I Program db2iupgrade completed successfully`.
    3. Verifique la actualización.

       ```bash
       cd /opt/ibm/db2/V11.5/bin/
       ./db2val
       ```
    4. Compruebe el nivel de instalación de la instancia de base de datos de Cognos .

       Para obtener más información, consulte [db2level -Mostrar mandato de nivel de servicio de Db2](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0009195.html).

       ```
       db2level
       ```

       Busque un valor de retorno que coincida con la versión que está instalando. Por ejemplo, busque un valor de retorno de `DB2 v11.5.5.0`.
11. Si utiliza Db2 Administration Server (DAS), actualice el servicio.

    Para obtener más información, consulte [Actualización del Servidor de administración de Db2 (DAS)](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0009303.html?pos=2).

    Por ejemplo:

    ```bash
    cd /opt/ibm/db2/V11.5/instance
    ./dasmigr
    ```

    El valor `DBI1070I Program dasmigr completed successfully` indica un resultado correcto.
12. Actualice la base de datos de OpenPages .

    Realice este paso como usuario con la autorización SYSADM.

    Para obtener más información, consulte [Actualización de bases de datos](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0007193.html) en la documentación de Db2 .

    Por ejemplo:

    ```
    db2start 
    db2 upgrade database opx user db2inst1 using password
    ```
13. Actualice la base de datos de Cognos .

    Realice este paso como usuario con la autorización SYSADM.

    Para obtener más información, consulte [Actualización de bases de datos](http://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.qb.upgrade.doc/doc/t0007193.html) en la documentación de Db2 .

    Por ejemplo:

    ```
    db2start 
    db2 upgrade database cognosdb user db2inst2 using password
    ```
14. Configure y habilite Db2 Text Search, cree el índice y planifique un trabajo para sincronizar el índice.

    1. Iniciar Db2 Text Search.

       ```
       db2ts START FOR TEXT
       ```
    2. Cree el índice.

       Vaya al directorio que ha creado en el paso 2, vaya al subdirectorio `TEXT_INDEXING` y, a continuación, ejecute el mandato siguiente:

       ```
       clpplus -nw @sql-wrapper CustomIndexing_Step1_AddTextIndexing_to_DB.sql CustomIndexing_Step1_AddTextIndexing_to_DB.log <db_server>:50000/opx db2inst1 'password' OPENPAGE
       ```

       Se espera un aviso como el siguiente mensaje y puede ignorarlo:

       ```
       MESSAGE = <CIE99>CIE0212W Incomplete enablement of the Text Search server.
        Reason code = "01"
       ```
    3. Actualice la configuración del servidor de texto en la base de datos.

       ```
       cd /home/db2inst1/sqllib/db2tss/bin
       TS_AUTH_TOKEN=`configTool printToken | awk 'NR == 2 {print}'`
       TS_ENCRYPT_KEY=`configTool printToken | awk 'NR == 4 {print}'`
       db2 connect to OPX
       db2 select "*" from sysibmts.tsservers | grep $TS_AUTH_TOKEN
       if [ $? != 0 ]; then
           echo "*** Registering text search server manually! ***"
           db2 "insert into SYSIBMTS.TSSERVERS (HOST, PORT, TOKEN, key, SERVERTYPE, SERVERSTATUS) 
           values ('<db_server>', 55000, '$TS_AUTH_TOKEN', '$TS_ENCRYPT_KEY', 1, 0)"
       fi
       ```
    4. Vuelva a crear los índices de texto y configure una planificación para renovarlos.

       Vaya al directorio que ha creado en el paso 2, vaya al subdirectorio `TEXT_INDEXING` y, a continuación, ejecute el mandato siguiente:

       ```
       clpplus -nw @sql-wrapper CustomIndexing_Step2_IndexCreate.sql CustomIndexing_Step2_IndexCreate.log <db_server>:50000/OPX openpage passw0rd "'*'" "'*'" "0,5,10,15,20,25,30,35,40,45,50,55" 1 && \
       clpplus -nw @sql-wrapper CustomIndexing_Step3_IndexRefresh.sql CustomIndexing_Step3_IndexRefresh.log <db_server>:50000/OPX openpage passw0rd "'*'" "'*'" "0,5,10,15,20,25,30,35,40,45,50,55" 1
       ```
    5. Verifique que Db2 Text Search esté en ejecución.

       ```
       db2 "select count(*) from <openpages_database_user>.propertyvals_clob 
         where contains(CLOB_VALUE, 'RPS') = 1"
       ```

       El resultado esperado es:

       ```
       1
       -----------
                 0

         1 record(s) selected.
       ```
15. Revalidar objetos y volver a vincular paquetes en la base de datos de OpenPages .

    Realice estos pasos como usuario de base de datos de OpenPages . En los ejemplos siguientes, el usuario de base de datos es `openpage`.

    1. Copie el directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/INSTALL_SCRIPTS` en el servidor de bases de datos.
    2. Vaya al directorio donde ha copiado el directorio `INSTALL_SCRIPTS` y, a continuación, vuelva a validar los objetos de base de datos.

       Ejecute los mandatos siguientes:

       ```
       db2 connect to OPX user openpage using password
       db2 -td@ -f pks_OP_CURRENCY_MGR.sql
       db2 -td@ -f pkb_OP_CURRENCY_MGR.sql
       clpplus -nw openpage/password@<db_server>:50000/opx @sql-wrapper revalidate.sql revalidate.log openpage
       ```
    3. Vuelva a enlazar los paquetes.

       Por ejemplo:

       ```
       db2rbind opx -l opbind.log all -u db2inst1 -p password -r any
       ```
16. Revalidar objetos y volver a vincular paquetes en la base de datos de Cognos .

    Realice estos pasos como propietario de la instancia para la base de datos de Cognos .

    1. Vuelva a validar los objetos de base de datos.

       Por ejemplo:

       ```
       db2 connect to cognosdb user db2inst2 using password
       db2 "call sysproc.admin_revalidate_db_objects()"
       ```
    2. Vuelva a vincular los paquetes en la base de datos de Cognos .

       Por ejemplo:

       ```
       db2rbind cognosdb -l cogbind.log -u db2inst2 -p password
       ```
17. Opcional: Haga una copia de seguridad de las bases de datos.

    - Para la base de datos OpenPages , ejecute los mandatos siguientes como propietario de la instancia para la base de datos OpenPages :

      ```
      mkdir db2v11bu
      cd db2v11bu
      db2 backup database opx to .
      ```
    - Para la base de datos de Cognos , ejecute los mandatos siguientes como propietario de instancia para la base de datos de Cognos :

      ```
      mkdir db2v11bu
      cd db2v11bu
      db2 backup database cognosdb to .
      ```
18. Aplicar la licencia de IBM Db2 .

    Para más información, consulte [db2licm - Comando de la herramienta de gestión de licencias](http://www.ibm.com/docs/en/SSEPGG_11.5.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0002451.html).

    1. Obtenga una licencia para IBM Db2.
    2. Ejecute el mandato `db2licm` .

       Por ejemplo:

       ```
       db2licm -a <license_file>
       ```

       Donde `<license_file>` es la vía de acceso completa y el nombre de archivo de la licencia de IBM Db2 .
    3. Verifique la licencia ejecutando el mandato `db2licm -l` .
19. Inicie todos los servicios de IBM OpenPages .

##### Descarte del índice de búsqueda e inhabilitación de Db2 Text Search

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Actualizar software de requisito previo › Actualizar o actualizar Db2` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uud-dropping-search-index-disabling-db2-text-search)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si Db2® Text Search está habilitado en el entorno de origen, descarte los índices de búsqueda de texto, inhabilite el servicio de búsqueda de texto, elimine la tarea administrativa Db2 para actualizar los índices e inhabilite Db2 Text Search. Realice este procedimiento antes de realizar una copia de seguridad de la base de datos de OpenPages® .

###### Procedimiento

1. Inicie sesión en un sistema como usuario de instalación de OpenPages , por ejemplo `opuser`.

   Puede utilizar cualquier sistema con acceso a CLPPlus que se conecta al servidor de base de datos.
2. Descarte el índice de Db2 Text Search.

   1. Vaya al directorio `<OP_HOME>/aurora/bin/full-text-index` .
   2. Abra una ventana de mandatos o de shell y ejecute el siguiente mandato:

      ```
      clpplus -nw @sql-wrapper CustomIndexing_Step5_IndexDrop.sql 
        <LOG_FILE_NAME>
                              <DB2_SERVER_NAME>:<DB2_PORT_NUMBER>/<DATABASE_NAME>
                              <OP_DB_USER>
                              <OP_DB_PASSWORD>
                              <FORCE_DROP_INDEX>
                     
      ```

      Si la contraseña `<OP_DB_PASSWORD>` contiene caracteres especiales, debe entrecomillar la contraseña.

      - Windows: `"password"`
      - Linux®: `'password'`

      Por ejemplo

      - Windows:

        ```
        clpplus -nw @sql-wrapper CustomIndexing_Step5_IndexDrop.sql 
           CustomIndexing_Step5_IndexDrop.log localhost:50000/OPX OPENPAGE "password" Y
        ```
      - Linux:

        ```
        clpplus -nw @sql-wrapper CustomIndexing_Step5_IndexDrop.sql 
           CustomIndexing_Step5_IndexDrop.log localhost:50000/OPX OPENPAGE 'password' Y
        ```

      Para obtener más información, consulte [Descartar un índice de serie larga](3.4-guia-del-administrador.md#eliminación-de-un-índice-de-cadena-larga).
3. Ejecute el mandato siguiente para determinar si Db2 Text Search está habilitado.

   ```sql
   select * from all_tables where table_schema = 'SYSIBMTS';
   ```

   Si el mandato devuelve datos, DB2 Text Search está habilitado. Continúe con el paso siguiente para inhabilitar DB2 Text Search.
4. Inicie sesión en la base de datos OpenPages como usuario db2inst1 .

   ```
   db2 connect to opx user opuser using password
   ```
5. Ejecute el mandato siguiente para inhabilitar Db2 Text Search.

   Para obtener más información, consulte [Procedimiento SYSTS_DISABLE-Inhabilitar la base de datos actual para la búsqueda de texto](http://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.sql.rtn.doc/doc/r0051993.html).

   ```
   db2 "call sysproc.systs_disable('','en_US',?)"
   ```

   De forma alternativa, utilice estos mandatos.

   ```bash
   db2 GRANT SYSTS_ADM TO db2inst1 
   db2 grant SYSTS_MGR to db2inst1
   db2 connect reset 
   db2ts start for text
   export DB2DBDFT=OPX
   db2ts DISABLE DATABASE FOR TEXT
   ```
6. Elimine la tarea administrativa de Db2 para actualizar los índices

   Para obtener más información, consulte el tema siguiente en la documentación de Db2 : [Eliminación de una tarea del planificador de tareas administrativas](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.admin.gui.doc/doc/t0054384.html).

#### Actualización de Cognos

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Actualizar software de requisito previo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=software-upgrading-cognos-analytics)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Actualice a una versión soportada de IBM® Cognos® Analytics.

##### Antes de empezar

Revise los requisitos de software para Cognos. Si utiliza Linux®, verifique que tiene instalados los paquetes necesarios. Para obtener más información, consulte [IBM Cognos Analytics en local 11.2.x: Entornos de software soportados](https://www.ibm.com/support/pages/node/6440667).

El fixpack 9.0.0.1 añade soporte para los releases de IBM Cognos Analytics 12.0.1 y posteriores 12.0.x . Si desea utilizar Cognos 12.0.x, instale el fixpack 9.0.0.1.

> **Importante:** Debido a problemas conocidos, es posible que tenga que corregir los informes si actualiza a Cognos 12.0.x. Para obtener más información, consulte [Revisar cambios importantes](5.2-guia-de-instalacion-y-despliegue-solo-local.md#revisar-cambios-importantes) .

##### Acerca de esta tarea

Puede actualizar Cognos in situ.

##### Procedimiento

1. Inicie sesión en el servidor de informes como un usuario con privilegios administrativos.
2. Detenga todos los servicios de Cognos .
3. Actualice IBM Cognos Analytics. Consulte [Actualización de la versión actual de Cognos Analytics 11](https://www.ibm.com/support/knowledgecenter/en/SSEP7J_11.2.0/com.ibm.swg.ba.cognos.inst_cr_winux.doc/c_r_type_release.html).
4. Reinicie los servidores de informes.
5. Vuelva a importar los certificados SSL de OpenPages® en el JRE de Cognos .

   Para obtener más información, consulte  [Importación del certificado de CA para Java Runtime Environment de Cognos Analytics](3.4-guia-del-administrador.md#importación-del-certificado-de-ca-para-java-runtime-environment-de-ibm-cognos-analytics) .

#### Obtención de una copia del SDK de IBM (Windows)

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Actualizar software de requisito previo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=software-getting-sdk-windows)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de instalar OpenPages®, instale IBM® SDK, Java™ Technology Edition y configure las variables de entorno del sistema para Java en cada servidor de aplicaciones y el servidor de búsqueda. También puede utilizar los pasos para instalar IBM SDK en el servidor de instalación.

##### Acerca de esta tarea

Para los servidores de aplicaciones, la versión de IBM SDK debe ser la misma en cada uno de los servidores.

##### Procedimiento

1. Localice el SDK deIBM en el soporte de instalación de IBM OpenPages .

   La vía de acceso es `\OP_<version>_Main\IBM_Java\WIN64\java_8.0_64`
2. Copie IBM SDK en el disco duro local del servidor.

   Puede copiar IBM SDK en cualquier directorio del servidor.

   Por ejemplo, copie IBM SDK en la raíz de la unidad C bajo `C:\IBM`.
3. Establezca las variables de entorno del sistema para Java.

   1. En el recuadro de búsqueda Windows , escriba `environment variables`y, a continuación, pulse **Editar variables de entorno del sistema**.
   2. En la pestaña **Avanzado** , pulse **Variables de entorno**.
   3. En el panel **Variables del sistema** , pulse **Nueva**.
   4. Escriba `JAVA_HOME` en el campo **Nombre de variable** .
   5. Escriba `C:\IBM\java_8.0_64` en el campo **Valor de variable** .
   6. Pulse **Aceptar**.
   7. En Variables del sistema, seleccione la variable **Vía de acceso** y, a continuación, pulse **Editar**.
   8. Escriba `%JAVA_HOME%\bin;` al principio de la lista de vías de acceso en el campo **Valor de variable** .
   9. Pulse **Aceptar**.

   > **Nota:** Inicie un nuevo indicador de mandatos para ver los cambios en las variables de entorno.
4. Verifique la versión de Java que está en el servidor.

   Ejecute el mandato `java -version`. El resultado tiene que ser similar al siguiente ejemplo:

   ```
   java version "1.8.0_351"
   Java(TM) SE Runtime Environment (build 8.0.7.20 - pxa6480sr7fp20-20221020_01(SR7 FP20))
   IBM J9 VM (build 2.9, JRE 1.8.0 Windows Server 2016 amd64-64-Bit Compressed References 
   20220929_3782 (JIT enabled, AOT enabled)
   OpenJ9   - 02180fe
   OMR      - 48fc32a
   IBM      - bf759bf)
   JCL - 20220922_01 based on Oracle jdk8u351-b10
   ```

Si la ubicación de Java cambia más adelante, puede actualizarla. Para obtener más información, consulte las siguientes notas técnicas:

- [Cómo cambiar la ubicación de Java en un servidor de aplicaciones OpenPages](https://www.ibm.com/support/pages/node/6202563)
- [Cómo cambiar la ubicación de Java en un servidor de búsqueda global de OpenPages](https://www.ibm.com/support/pages/node/6202570)

> **Sugerencia:** También puede cambiar la ubicación de Java en el servidor de informes. Consulte [Cómo cambiar la ubicación de Java en un servidor de informes de OpenPages](https://www.ibm.com/support/pages/node/6202567).

#### Obtención de una copia de IBM SDK (Linux®)

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización › Actualizar software de requisito previo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=software-getting-sdk-linux)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de instalar OpenPages®, instale IBM® SDK, Java™ Technology Edition y configure las variables de entorno del sistema para Java en cada servidor de aplicaciones y el servidor de búsqueda. También puede utilizar los pasos para instalar IBM SDK en el servidor de instalación.

##### Acerca de esta tarea

Para los servidores de aplicaciones, la versión de IBM SDK debe ser la misma en cada uno de los servidores.

##### Procedimiento

1. Localice el SDK deIBM en el soporte de instalación de IBM OpenPages .

   La vía de acceso es `/OP_<version>_Main/IBM_Java/Linux64/java_8.0_64`.
2. Copie IBM SDK en el disco duro local del servidor.

   Puede copiar IBM SDK en cualquier directorio del servidor.

   Por ejemplo, copie IBM SDK en `/opt/IBM/`.
3. Otorgue permisos de lectura, escritura y ejecución en Java al usuario de instalación de OpenPages (`opuser`).

   Ejecute el mandato siguiente:

   ```bash
   chmod -R +x /opt/IBM/java_8.0_64
   ```
4. Establezca las variables de entorno del sistema para Java.

   1. En función del shell que esté utilizando y de la cuenta bajo la que se ejecutará el servidor, edite el archivo `.profile` o `.bashrc` .
   2. Asegúrese de que `JAVA_HOME` esté establecido en `/opt/IBM/java_8.0_64`.
   3. Asegúrese de que `PATH` incluya `$JAVA_HOME/bin` como primer elemento.

   > **Nota:** Inicie una nueva ventana de shell para ver los cambios en las variables de entorno.
5. Verifique la versión de Java que está en el servidor.

   Ejecute el mandato `java -version`. El resultado tiene que ser similar al siguiente ejemplo:

   ```
   java version "1.8.0_351"
   Java(TM) SE Runtime Environment (build 8.0.7.20 - pxa6480sr7fp20-20221020_01(SR7 FP20))
   IBM J9 VM (build 2.9, JRE 1.8.0 Linux amd64-64-Bit Compressed References 20220929_37824 (JIT enabled, AOT enabled)
   OpenJ9   - 02180fe
   OMR      - 48fc32a
   IBM      - bf759bf)
   JCL - 20220922_01 based on Oracle jdk8u351-b10
   ```

Si la ubicación de Java cambia más adelante, puede actualizarla. Para obtener más información, consulte las siguientes notas técnicas:

- [Cómo cambiar la ubicación de Java en un servidor de aplicaciones OpenPages](https://www.ibm.com/support/pages/node/6202563)
- [Cómo cambiar la ubicación de Java en un servidor de búsqueda global de OpenPages](https://www.ibm.com/support/pages/node/6202570)

> **Sugerencia:** También puede cambiar la ubicación de Java en el servidor de informes. Consulte [Cómo cambiar la ubicación de Java en un servidor de informes de OpenPages](https://www.ibm.com/support/pages/node/6202567).

### Verificación de los servidores antes de la actualización

`Guía de actualización para Db2 (solo en local) › Preparación de la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrade-verifying-servers-before-you)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de actualizar, verifique el estado de los servidores en el despliegue.

#### Procedimiento

1. Asegúrese de que no haya ningún usuario conectado a la aplicación OpenPages® .

   Los usuarios no deben iniciar sesión hasta que se haya completado la actualización.
2. Si utiliza el inicio de sesión único (SSO) y lo ha configurado para que requiera un inicio de sesión SSO para acceder a los URL de la API REST en `/grc/api/*`, inhabilite SSO.
3. Asegúrese de que no haya scripts de base de datos en ejecución.

   Los scripts de base de datos, excepto los scripts de actualización, no se deben ejecutar hasta que se haya completado la actualización.
4. Actualice el archivo `ObjectManager.properties` con los siguientes valores:

   ```properties
   configuration.manager.vendor.mode=true
   configuration.manager.force.update.object.strings=false
   configuration.manager.force.update.application.strings=false
   configuration.manager.disable.triggers=true
   ```
5. Asegúrese de que no haya procesos OpenPages de larga ejecución.

   Los ejemplos de procesos de larga ejecución incluyen importaciones de FastMap y procesos de indexación de búsqueda global.
6. Si utiliza la búsqueda global, asegúrese de que los servicios de búsqueda se han detenido.

   Para obtener más información, consulte [Iniciar o detener los servicios de búsqueda global](5.2-guia-de-instalacion-y-despliegue-solo-local.md#inicio-o-detención-de-los-servicios-de-búsqueda-global).
7. Detenga el gestor de despliegue, todos los servidores de aplicaciones OpenPages (admin y no admin) y todos los servidores de informes (activos y en espera).

## Actualizar OpenPages

`Guía de actualización para Db2 (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=only-upgrading)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Complete las tareas siguientes para actualizar IBM OpenPages®.

> **Nota:** Esta lista sólo se aplica a las actualizaciones in situ. Si está migrando a 9.0, consulte la publicación *IBM OpenPages Guía de instalación y despliegue*. Para obtener más información sobre las vías de acceso de actualización, consulte [Determinar la vía de acceso de actualización](#determinar-la-ruta-de-actualización).

- Realice las tareas de preparación:

  - Descargue el kit de instalación desde Passport Advantage
  - [Revisión de las características y arreglos nuevos](#revisión-de-las-características-y-arreglos-nuevos)
  - [Copia de seguridad del entorno](#copia-de-seguridad-del-entorno)
  - [Actualizar software de requisito previo](#actualizar-software-de-requisito-previo)
  - [Verificación de los servidores antes de la actualización](#verificación-de-los-servidores-antes-de-la-actualización)
- Actualice la base de datos OpenPages manualmente. Para obtener más información, consulte [Actualizar la base de datos OpenPages (Db2)](#actualice-la-base-de-datos-openpages-db2).
- Prepare el servidor de instalación. Para obtener más información, consulte [Preparación del servidor de instalación](#preparación-del-servidor-de-instalación)
- Actualice IBM OpenPages. Para obtener más información, consulte [Actualización de OpenPages](#actualización-openpages).
- Realice las tareas posteriores a la instalación para las actualizaciones in situ. Para obtener más información, consulte [Tareas posteriores a la actualización](#tareas-posteriores-a-la-actualización).

### Actualice la base de datos OpenPages (Db2)

`Guía de actualización para Db2 (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrading-upgrade-openpages-database-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Actualice la base de datos de OpenPages® ejecutando scripts. Utilice estos temas si está actualizando OpenPages in situ.

Debe ejecutar todos los scripts de actualización por orden para actualizar el esquema de base de datos.

Dos de los scripts requieren privilegios de DBA: un script previo a la actualización y un script posterior a la actualización. Si tiene privilegios de DBA, puede ejecutar todos los scripts. Si no tiene privilegios de DBA, póngase en contacto con el administrador de base de datos.

Un usuario de esquema puede ejecutar los scripts que no requieren privilegios de DBA.

- **Paso previo a la actualización – Requiere privilegios de DBA**

  Durante este paso, el administrador de base de datos ejecuta un script para preparar la base de datos para la actualización.

  Necesita las autorizaciones DBADM y SECADM para ejecutar este script.

- **Validar el paso previo a la actualización**

  Durante este paso, se ejecuta un script para verificar que el script previo a la actualización se ha completado correctamente y que el esquema de base de datos está listo para la actualización.

- **Paso de actualización**

  Durante este paso, se ejecuta un script para actualizar la base de datos. El script determina la versión actual de los objetos de esquema de base de datos y, a continuación, ejecuta los scripts de actualización necesarios para actualizar la base de datos.

- **Paso posterior a la actualización – Requiere privilegios de DBA**

  Durante este paso, el administrador de base de datos ejecuta un script para completar la actualización y establecer parámetros de ajuste de base de datos.

  Necesita las autorizaciones DBADM y SECADM para ejecutar este script.

- **Validar el paso posterior a la actualización**

  Durante este paso, se ejecuta un script para validar el paso posterior a la actualización.

#### Preparación de la actualización de la base de datos (Db2)

`Guía de actualización para Db2 (solo en local) › Actualización › Actualice la base de datos OpenPages (Db2)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodd-preparing-database-upgrade-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Prepare la actualización de objetos de base de datos.

##### Procedimiento

1. Cierre todos los componentes de OpenPages® : servidores de aplicaciones (admin y no admin), servidores de informes (activos y en espera) y el servidor de búsqueda (si utiliza la búsqueda global).

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
2. Asegúrese de que el servidor de bases de datos IBM® Db2® esté en ejecución.
3. Inicie sesión en el sistema del servidor de bases de datos Db2 como usuario con privilegios administrativos.
4. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/UPGRADE_SCRIPTS` .
5. Verifique que tiene permiso de escritura en el archivo `sql-wrapper.sql` . Si no es así, cambie el permiso en el archivo utilizando el mandato `chmod` .
6. Edite el archivo `sql-wrapper.sql` .

   > **Restricción:** cambie sólo los parámetros que se describen en este paso.

   **Tabla 1. Parámetros en el archivo `sql-wrapper.sql` para bases de datos Db2**

   | Propiedad | Descripción |
   | --- | --- |
   | `opx_db2_instance_owner` | El propietario de la instancia de base de datos para OpenPages.<br>El usuario que especifique debe tener las autorizaciones DBADM y SECADM<br>Si el administrador de base de datos va a ejecutar los scripts de DBA en lugar del usuario, puede dejar este valor vacío al ejecutar los scripts que no son de DBA. |
   | `opx_db2_server_name` | Nombre del servidor de bases de datos |
   | `opx_db2_port_number` | Número de puerto de base de datos, por ejemplo `50000` |
   | `opx_db2_db_name` | El nombre de la base de datos OpenPages. |
   | `opx_db_owner` | El propietario del esquema de la base de datos de OpenPages . |
   | `opx_dflt_stor_srv_root` | La vía de acceso al directorio de almacenamiento de OpenPages .<br>Ejemplo:<br>`define opx_dflt_stor_srv_root='/home/opuser/OP/OpenPages/openpages-storage'` |
   | `opx_override_ver_check` | Utilice el valor predeterminado, `N`, a menos que vuelva a ejecutar los scripts de actualización de base de datos después de una anomalía.<br>Si la actualización de la base de datos ha fallado en medio del proceso de actualización del esquema, establezca este parámetro en `Y`. Al volver a ejecutar el script de actualización, el proceso de actualización se reanuda a partir del último paso de actualización de esquema satisfactorio. |
   | `sqllib_dir` | La vía de acceso al directorio de instalación del cliente de Db2 en el servidor de aplicaciones de administración (App Server1)<br>Ejemplo:<br>• Windows: `define sqllib_dir='C:\IBM\SQLLIB'`<br>• Linux®: `define sqllib_dir='/home/db2inst1/sqllib'` |
7. Si desea ejecutar un script personalizado durante el proceso de actualización, consulte [Ejecución de un script personalizado durante la actualización de la base de datos (Db2)](#ejecución-de-un-script-personalizado-durante-la-actualización-de-la-base-de-datos-db2).
8. Si el administrador de base de datos va a ejecutar los scripts que requieren privilegios de DBA, prepare los archivos para el administrador de base de datos.

   1. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/UPGRADE_SCRIPTS` .
   2. Abra el archivo `op-dba-upgrade-file-list.txt` .
   3. Enviar a su administrador de base de datos el archivo `sql-wrapper.sql` que ha actualizado junto con los archivos listados en el archivo `op-dba-upgrade-file-list.txt` .
   4. Envíe al DBA las instrucciones para ejecutar los scripts de DBA.

      - [Ejecución del script de DBA previo a la actualización (Db2)](#ejecución-del-script-de-dba-previo-a-la-actualización-db2)
      - [Ejecución del script de DBA posterior a la actualización (Db2)](#ejecución-del-script-de-dba-posterior-a-la-actualización-db2)

##### Ejecución de un script personalizado durante la actualización de la base de datos (Db2®)

`Guía de actualización para Db2 (solo en local) › Actualización › Actualice la base de datos OpenPages (Db2) › Preparación de la actualización de la base de datos (Db2)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=db2-running-custom-script)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si desea ejecutar un script personalizado durante el proceso de actualización de la base de datos, edite el archivo `sql-wrapper.sql` para especificar el script que se ejecutará.

###### Acerca de esta tarea

Puede utilizar el parámetro `custom_data_upgrade_script` para configurar un script personalizado.

El script que especifique se ejecuta durante el paso de actualización de base de datos. El script `op-database-product-upgrade.sh/bat` llama al script personalizado después de que se completen los demás pasos de actualización, como los cambios de DDL, los cambios de código PL/SQL y los cambios de datos de nivel de base de datos.

###### Procedimiento

1. Abra el archivo `sql-wrapper.sql` .
2. Verifique que la vía de acceso de `sqllib_dir` sea correcta. Si está ejecutando el script personalizado desde un sistema distinto al servidor de base de datos, actualice la vía de acceso.
3. Edite los siguientes parámetros:

   ```
   define custom_data_upgrade_script=no-op.sql
   ```

   Sustituya `no-op.sql` por el script que desea ejecutar.
4. Coloque el script personalizado en el mismo directorio que el archivo `sql-wrapper.sql` .

#### Ejecución del script de DBA previo a la actualización (Db2)

`Guía de actualización para Db2 (solo en local) › Actualización › Actualice la base de datos OpenPages (Db2)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodd-running-pre-upgrade-dba-script)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Solicite al administrador de base de datos que ejecute el script previo a la actualización. O, si tiene las autorizaciones de Db2® necesarias, puede ejecutar el script.

##### Antes de empezar

- El servidor de bases de datos IBM® Db2 se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- La variable del sistema `JAVA_HOME` se define y apunta a IBM SDK, Java™ Technology Edition que se instala con Db2. Por ejemplo:

  ```bash
  export JAVA_HOME=/db2/V11.5/java/jdk64
  export PATH=$JAVA_HOME/bin:$PATH
  ```

  Si está ejecutando el script desde otro host, asegúrese de que `JAVA_HOME` apunte a IBM SDK, Java Technology Edition que está instalado en el sistema.
- Se ha definido la variable del sistema `DB2_HOME`.

##### Acerca de esta tarea

Ejecute el siguiente script: `op-database-dba-upgrade.sh|.bat`. El script utiliza las propiedades definidas en el archivo `sql-wrapper.sql`.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de bases de datos Db2 como administrador de bases de datos (DBA).
2. Localice los scripts.

   Si es un administrador de base de datos, obtenga los scripts de su equipo de OpenPages .

   O bien, puede obtener los scripts del directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución sobre los scripts en el directorio `UPGRADE_SCRIPTS` y sus subdirectorios.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno.

   1. Para el parámetro `opx_db2_instance_owner` , especifique un usuario que tenga las autorizaciones siguientes:

      Si está actualizando, utilice el propietario de instancia de Db2 , que tiene las autorizaciones DBADM y SECADM.

      Si está migrando, utilice un usuario de Db2 con las autorizaciones siguientes:

      - Releases anteriores a Db2 11.5.6: Autoridades `DBADM` y `SECADM`
      - Releases después de las autorizaciones Db2 11.5.7: `DBADM`, `SECADM`y `SYSADM`

        Si desea evitar el requisito `SYSADM` que se introdujo en Db2 11.5.7, un método alternativo es modificar la variable de registro `DB2_ALTERNATE_AUTHZ_BEHAVIOUR` para incluir el valor `NOT_FENCED_ROUTINE_DBAUTH` . Para obtener más información, consulte la [documentación deDb2](https://www.ibm.com/docs/es/SSEPGG_11.5.0/com.ibm.db2.luw.sql.ref.doc/doc/r0000958.html).
   2. Si ha personalizado los nombres de espacios de tablas, actualice los parámetros `define opx_dflt_*` con los nombres de espacios de tablas personalizados.
5. Ejecute el mandato siguiente:

   - En Linux®:

     ```bash
     ./op-database-dba-upgrade.sh pre '<dba_password>'
     ```
   - Windows:

     ```
     op-database-dba-upgrade.bat pre "<dba_password>"
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales. Consulte [Caracteres especiales en contraseñas](#caracteres-especiales-en-las-contraseñas).
6. Verifique que el código de retorno es 0, lo que indica que es satisfactorio.

   También puede comprobar el archivo de registro, `op-database-dba-upgrade.pre.*.log`.

##### Qué hacer a continuación

Valide el script de DBA previo a la actualización.

#### Validación del paso de DBA previo a la actualización (Db2)

`Guía de actualización para Db2 (solo en local) › Actualización › Actualice la base de datos OpenPages (Db2)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodd-validating-pre-upgrade-dba-step-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Ejecute el script para validar los pasos de DBA previos a la actualización.

##### Antes de empezar

- El servidor de bases de datos IBM® Db2® se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- La variable del sistema `JAVA_HOME` se define y apunta a IBM SDK, Java™ Technology Edition que se instala con Db2. Por ejemplo:

  ```bash
  export JAVA_HOME=/db2/V11.5/java/jdk64
  export PATH=$JAVA_HOME/bin:$PATH
  ```

  Si está ejecutando el script desde otro host, asegúrese de que `JAVA_HOME` apunte a IBM SDK, Java Technology Edition que está instalado en el sistema.
- Se ha definido la variable del sistema `DB2_HOME`.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de bases de datos IBM Db2 como usuario de la aplicación OpenPages , `opuser`.
2. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución sobre los scripts en `UPGRADE_SCRIPTS` y sus subdirectorios.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno.
5. Ejecute el mandato siguiente:

   - En Linux®:

     ```bash
     ./op-database-product-upgrade.sh preupgrade '<op_password>'
     ```
   - Windows:

     ```
     op-database-product-upgrade.bat preupgrade "<op_password>"
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales. Consulte [Caracteres especiales en contraseñas](#caracteres-especiales-en-las-contraseñas).
6. Verifique que el script se ha completado correctamente.

   Busque el siguiente mensaje:`Status:Success`o un código de retorno de 0.

   También puede comprobar el archivo de registro, `op-database-product-upgrade.preupgrade.*.log`.

##### Qué hacer a continuación

Ejecute el script para actualizar los objetos de base de datos.

#### Actualización de la base de datos (Db2)

`Guía de actualización para Db2 (solo en local) › Actualización › Actualice la base de datos OpenPages (Db2)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodd-upgrading-database-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Ejecute el script para actualizar los datos y objetos de esquema de base de datos.

##### Antes de empezar

- El servidor de bases de datos IBM® Db2® se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- La variable del sistema `JAVA_HOME` se define y apunta a IBM SDK, Java™ Technology Edition que se instala con Db2. Por ejemplo:

  ```bash
  export JAVA_HOME=/db2/V11.5/java/jdk64
  export PATH=$JAVA_HOME/bin:$PATH
  ```

  Si está ejecutando el script desde otro host, asegúrese de que `JAVA_HOME` apunte a IBM SDK, Java Technology Edition que está instalado en el sistema.
- Se ha definido la variable del sistema `DB2_HOME`.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de bases de datos IBM Db2 como usuario de la aplicación OpenPages , `opuser`.
2. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución sobre los scripts en el directorio `UPGRADE_SCRIPTS` y sus subdirectorios.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno.
5. Ejecute el mandato siguiente:

   - Windows:

     ```
     op-database-product-upgrade.bat upgrade "<op_schema_owner_password>"
     ```
   - En Linux®:

     ```bash
     ./op-database-product-upgrade.sh upgrade '<op_schema_owner_password>'
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales. Consulte [Caracteres especiales en contraseñas](#caracteres-especiales-en-las-contraseñas).
6. Verifique que el código de retorno es 0, lo que indica que es satisfactorio.

   También puede comprobar el archivo de registro, `op-database-product-upgrade.upgrade.*.log`.

##### Qué hacer a continuación

Solicite al administrador de base de datos que ejecute el script de DBA posterior a la actualización.

#### Ejecución del script de DBA posterior a la actualización (Db2)

`Guía de actualización para Db2 (solo en local) › Actualización › Actualice la base de datos OpenPages (Db2)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodd-running-post-upgrade-dba-script-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Solicite al administrador de base de datos que ejecute el script posterior a la actualización. O, si tiene las autorizaciones de Db2® necesarias, puede ejecutar el script.

##### Antes de empezar

- El servidor de bases de datos IBM® Db2 se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- La variable del sistema `JAVA_HOME` se define y apunta a IBM SDK, Java™ Technology Edition que se instala con Db2. Por ejemplo:

  ```bash
  export JAVA_HOME=/db2/V11.5/java/jdk64
  export PATH=$JAVA_HOME/bin:$PATH
  ```

  Si está ejecutando el script desde otro host, asegúrese de que `JAVA_HOME` apunte a IBM SDK, Java Technology Edition que está instalado en el sistema.
- Se ha definido la variable del sistema `DB2_HOME`.
- El script `op-database-product-upgrade.sh|.bat` se ha completado satisfactoriamente.

##### Acerca de esta tarea

Ejecute el siguiente script: `op-database-dba-upgrade.sh|.bat`. El script utiliza los parámetros definidos en el archivo `sql-wrapper.sql`.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de bases de datos IBM Db2 como administrador de bases de datos (DBA).
2. Localice los scripts que son necesarios.

   Si es un administrador de base de datos, obtenga los scripts de su equipo de OpenPages .

   O bien, puede obtener los scripts del directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución sobre los scripts en `UPGRADE_SCRIPTS` y sus subdirectorios.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno.

   Si está actualizando, utilice el propietario de instancia de Db2 , que tiene las autorizaciones DBADM y SECADM.

   Si está migrando, utilice un usuario de Db2 con las autorizaciones siguientes:

   - Releases anteriores a Db2 11.5.6: Autoridades `DBADM` y `SECADM`
   - Releases después de las autorizaciones Db2 11.5.7: `DBADM`, `SECADM`y `SYSADM`

     Si desea evitar el requisito `SYSADM` que se introdujo en Db2 11.5.7, un método alternativo es modificar la variable de registro `DB2_ALTERNATE_AUTHZ_BEHAVIOUR` para incluir el valor `NOT_FENCED_ROUTINE_DBAUTH` . Para obtener más información, consulte la [documentación deDb2](https://www.ibm.com/docs/es/SSEPGG_11.5.0/com.ibm.db2.luw.sql.ref.doc/doc/r0000958.html).
5. Ejecute el mandato siguiente:

   - En Linux®:

     ```bash
     ./op-database-dba-upgrade.sh post '<dba_password>'
     ```
   - Windows:

     ```
     op-database-dba-upgrade.bat post "<dba_password>"
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales. Consulte [Caracteres especiales en contraseñas](#caracteres-especiales-en-las-contraseñas).
6. Verifique que el código de retorno es 0, lo que indica que es satisfactorio.

   También puede comprobar el archivo de registro: `op-database-dba-upgrade.post.*.log`.

##### Qué hacer a continuación

Valide el paso de DBA posterior a la actualización.

#### Validación del paso de DBA posterior a la actualización (Db2)

`Guía de actualización para Db2 (solo en local) › Actualización › Actualice la base de datos OpenPages (Db2)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodd-validating-post-upgrade-dba-step-db2)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Ejecute el script para validar los pasos de DBA posteriores a la actualización.

##### Antes de empezar

- El servidor de bases de datos IBM® Db2® se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- La variable del sistema `JAVA_HOME` se define y apunta a IBM SDK, Java™ Technology Edition que se instala con Db2. Por ejemplo:

  ```bash
  export JAVA_HOME=/db2/V11.5/java/jdk64
  export PATH=$JAVA_HOME/bin:$PATH
  ```

  Si está ejecutando el script desde otro host, asegúrese de que `JAVA_HOME` apunte a IBM SDK, Java Technology Edition que está instalado en el sistema.
- Se ha definido la variable del sistema `DB2_HOME`.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de bases de datos IBM Db2 como usuario de la aplicación OpenPages , `opuser`.
2. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/DB2/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución sobre los scripts en `UPGRADE_SCRIPTS` y sus subdirectorios.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno.
5. Ejecute el mandato siguiente:

   - En Linux®:

     ```bash
     ./op-database-product-upgrade.sh postdba '<op_password>'
     ```
   - Windows:

     ```
     op-database-product-upgrade.bat postdba "<op_password>"
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales. Consulte [Caracteres especiales en contraseñas](#caracteres-especiales-en-las-contraseñas).
6. Verifique que el script se ha completado correctamente.

   Busque el siguiente mensaje:`Status:Success`o un código de retorno de 0.

   También puede comprobar el archivo de registro, `op-database-product-upgrade.postdba.*.log`.
7. Elimine las contraseñas del archivo `sql-wrapper.sql` por motivos de seguridad.

##### Resultados

Se actualiza la base de datos de OpenPages .

### Preparación del servidor de instalación

`Guía de actualización para Db2 (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrading-preparing-installation-server)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Instale el servidor de instalación de 9.0 y migre los despliegues y usuarios al nuevo servidor de instalación.

> **Nota:** El servidor de instalación no se puede actualizar in situ. Debe instalar el servidor de instalación de 9.0 en un directorio nuevo.

Tiene dos opciones:

- Puede instalar el servidor de instalación y migrar los despliegues y usuarios durante el proceso de instalación.
- Puede instalar el servidor de instalación y migrar los despliegues y los usuarios más adelante.

Si gestiona los agentes de instalación manualmente, también debe instalar el software de agente 9.0 en cada servidor remoto. Si desea conservar el software de agente existente en un servidor remoto, por ejemplo a efectos de copia de seguridad, realice los pasos siguientes:

1. Detenga el agente anterior a9.0 si se está ejecutando.
2. Instale el software de agente de 9.0 en un directorio nuevo.
3. En la aplicación de instalación 9.0 , actualice el campo **Directorio de agente** en la tarjeta del servidor para que apunte al nuevo directorio.
4. Pulse **Validar**.

> **Nota:** Puede instalar distintas versiones del servidor de instalación en el mismo host. Si lo hace, debe utilizar un número de puerto y un directorio diferentes para cada servidor de instalación. Puede especificar el número de puerto del servidor 9.0 durante el proceso de configuración.

#### Configuración del servidor de instalación en Windows

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=server-setting-up-installation-windows)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede configurar el servidor de instalación en un servidor en el despliegue o en un sistema distinto. Utilice un sistema que se pueda comunicar con los servidores del entorno de OpenPages® .

Después de configurar el servidor de instalación, puede utilizar la aplicación de instalación de OpenPages para crear y gestionar despliegues.

> **Nota:** Si ya ha configurado el servidor de instalación y desea actualizarlo con un fixpack, consulte [Actualizar el servidor de instalación y los agentes](#actualización-del-servidor-de-instalación-y-los-agentes).

##### Antes de empezar

El sistema donde configura el servidor de instalación debe cumplir los siguientes requisitos:

- IBM® SDK, Java™ Technology Edition o Java Runtime Environment (JRE) está instalado.
- Java se incluye en la variable de entorno del sistema PATH.

También es posible que desee una aplicación de lector de PDF en el sistema. Al instalar o actualizar OpenPages, puede descargar los informes de validación en formato PDF.

##### Procedimiento

1. Descargue el paquete OpenPages 9.0 desde Passport Advantage.
2. Inicie sesión en el sistema como administrador.
3. Si está ejecutando una versión anterior del servidor de instalación, párela.
4. Realice uno de los pasos siguientes:

   - Actualice la política de antivirus en el sistema del servidor de instalación para permitir `Node.js`.
   - Inhabilite el software antivirus en el sistema del servidor de instalación. Puede volver a habilitarlo después de instalar el servidor de instalación.
5. Cree un nuevo directorio.

   Si tiene más de una versión del servidor de instalación en el mismo host, utilice un directorio independiente para cada versión.

   Por ejemplo, `C:\IBM\OPInstall<version>`.
6. Localice los archivos de instalación.

   Los archivos se almacenan en `\OP_<version>_Main\OP_<version>_Installer`.
7. Copie el contenido del directorio `\OP_<version>_Installer` en el directorio que ha creado.
8. Cambie el directorio a `<installation_server_home>\OP_<version>_Installer\install\Windows`.
9. Abra un indicador de mandatos como administrador.
10. Ejecute el script de instalación.

    Puede utilizar los siguientes argumentos opcionales:

    - `/p:<password>`: establece la contraseña para el usuario de la aplicación de instalación inicial, denominada `admin`. Si excluye el argumento, el script `install.bat` le solicitará la contraseña.
    - `/n:<port>`: establece el puerto en el que se ejecuta el servidor de instalación cuando se inicia. Si tiene varios servidores de instalación que se ejecutan en el mismo hardware, asegúrese de que cada servidor de instalación utiliza un número de puerto diferente. Especifique un entero en el rango de 0 a 65535. Si excluye este argumento, se utiliza el número de puerto predeterminado (8443).
    - `/m:<old_directory>` -Migra los despliegues existentes y las cuentas de usuario del servidor de instalación al servidor de instalación de 9.0 . Utilice este argumento si tiene 8.2.x o 8.3.x despliegues que desea utilizar con el nuevo servidor de instalación. Para `<old_directory>`, especifique la vía de acceso completa al directorio de inicio del servidor de instalación 8.2.x o 8.3.x . De forma alternativa, puede migrar despliegues y usuarios después de instalar el servidor de instalación de 9.0 . Para obtener más información, consulte [Migración de despliegues y usuarios del servidor de instalación](#migración-de-despliegues-y-usuarios-del-servidor-de-instalación).
    - `/s`: impide que el servidor de instalación se inicie después de que se complete `install.bat`. Si excluye este argumento, el servidor de instalación se inicia automáticamente después de que se complete el script `install.bat` .

    Sintaxis:

    ```bat
    install.bat –acceptLicense [/p:password] [/m:<old_directory>] [/n:<port>] [/s]
    ```
11. Si no ha utilizado el parámetro `/p` , escriba una contraseña y, a continuación, pulse Intro.
12. Una vez completada la instalación, vuelva a habilitar el software antivirus en el servidor de instalación.

    Realice este paso si ha inhabilitado el software antivirus en el paso 4.
13. Actualice el servidor de instalación a la versión más reciente del fixpack.

    Consulte [Actualizar el servidor de instalación y los agentes](#actualización-del-servidor-de-instalación-y-los-agentes).

##### Resultados

El servidor de instalación de OpenPages está instalado.

Si ha utilizado el argumento `/s`, inicie el servidor de instalación. Para obtener más información, consulte [Inicio del servidor de instalación](5.1-guia-de-instalacion-y-despliegue-solo-local.md#inicio-del-servidor-de-instalación).

Ahora puede iniciar la sesión. Para el nombre de usuario, escriba `admin`. Para la contraseña, escriba la contraseña establecida cuando se ejecutó el script `install.bat`. Para obtener más información, consulte [Inicio de sesión en la aplicación de instalación](5.1-guia-de-instalacion-y-despliegue-solo-local.md#inicio-de-sesión-en-la-aplicación-de-instalación).

> **Nota:** Si ha utilizado el argumento `/m` pero algunos despliegues o usuarios no se han migrado, no vuelva a ejecutar el script `install.bat` . En lugar de ello, repita la migración sin volver a instalar. Consulte [Migración de despliegues y usuarios del servidor de instalación](#migración-de-despliegues-y-usuarios-del-servidor-de-instalación).

#### Configuración del servidor de instalación en Linux®

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=server-setting-up-installation-linux)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede configurar el servidor de instalación en un servidor en el despliegue o en un sistema distinto. Utilice un sistema que se pueda comunicar con los servidores del entorno de OpenPages® .

Después de configurar el servidor de instalación, puede utilizar la aplicación de instalación de OpenPages para crear y gestionar despliegues.

> **Importante:** Si utiliza servidores Windows en el despliegue, configure el servidor de instalación de OpenPages en un sistema Windows. Consulte [Configuración del servidor de instalación en Windows](#configuración-del-servidor-de-instalación-en-windows).

> **Nota:** Si ya ha configurado el servidor de instalación y desea actualizarlo con un fixpack, consulte [Actualizar el servidor de instalación y los agentes](#actualización-del-servidor-de-instalación-y-los-agentes).

##### Antes de empezar

El sistema donde configura el servidor de instalación debe cumplir los siguientes requisitos:

- IBM® SDK, Java™ Technology Edition o Java Runtime Environment (JRE) está instalado.
- Java se incluye en la variable de entorno del sistema PATH.
- `JAVA_HOME` está establecido.

También es posible que desee una aplicación de lector de PDF en el sistema. Al instalar o actualizar OpenPages, puede descargar los informes de validación en formato PDF.

##### Acerca de esta tarea

En este vídeo se muestra cómo configurar el servidor de instalación. Los pasos son similares para 9.0:

[En este vídeo se muestra cómo configurar el servidor de instalación.](https://video.ibm.com/embed/channel/25817967/video/op-installation)

##### Procedimiento

1. Inicie sesión en el sistema como administrador.
2. Si está ejecutando una versión anterior del servidor de instalación, párela.
3. Realice uno de los pasos siguientes:

   - Actualice la política de antivirus en el sistema del servidor de instalación para permitir `Node.js`.
   - Inhabilite el software antivirus en el sistema del servidor de instalación. Puede volver a habilitarlo después de instalar el servidor de instalación.
4. Cree un directorio.

   Si tiene más de una versión del servidor de instalación en el mismo host, utilice un directorio independiente para cada versión.

   Por ejemplo, `/home/opuser/IBM/OPInstall<version>`.
5. Localice los archivos de instalación.

   Los archivos se almacenan en `/OP_<version>_Main/OP_<version>_Installer`.
6. Copie el contenido del directorio `OP_<version>_Installer` en el directorio que ha creado.
7. Cambie el directorio a `/home/opuser/IBM/OPInstall/OP_<version>_Installer/install/Linux`.
8. Otorgue el permiso `+rwx` al usuario en el directorio, subdirectorios y scripts del servidor de instalación.
9. Abra un shell y ejecute el script de configuración.

   Puede utilizar los siguientes argumentos opcionales:

   - `-p <password>`: establece la contraseña para el usuario de la aplicación de instalación inicial, denominada `admin`. Si excluye el argumento, el script `install.bat` le solicitará la contraseña.
   - `-n <port>`: establece el puerto en el que se ejecuta el servidor de instalación cuando se inicia. Si tiene varios servidores de instalación que se ejecutan en el mismo hardware, asegúrese de que cada servidor de instalación utiliza un número de puerto diferente. Especifique un entero en el rango de 0 a 65535. Si excluye este argumento, se utiliza el número de puerto predeterminado (8443).
   - `-m <old_directory>` -Migra los despliegues existentes y las cuentas de usuario del servidor de instalación al servidor de instalación de 9.0 . Utilice este argumento si tiene 8.2.x o 8.3.x despliegues que desea utilizar con el nuevo servidor de instalación. Para `<old_directory>`, especifique la vía de acceso completa al directorio de inicio del servidor de instalación 8.2.x o 8.3.x . De forma alternativa, puede migrar despliegues y usuarios después de instalar el servidor de instalación de 9.0 . Para más información, ver [Migración de implementaciones y usuarios del servidor de instalación](#migración-de-despliegues-y-usuarios-del-servidor-de-instalación).
   - `-s`: impide que el servidor de instalación se inicie después de que se complete el script `install.sh`. Si excluye este argumento, el servidor de instalación se inicia automáticamente después de que se complete el script `install.sh` .

   Sintaxis:

   ```bash
   ./install.sh –-acceptLicense [-p password] [-m <old_directory>] [-n <port>] [-s]
   ```
10. Si no ha utilizado el parámetro `-p` , escriba una contraseña y, a continuación, pulse Intro.
11. Cierre la ventana de shell.
12. Una vez completada la instalación, vuelva a habilitar el software antivirus en el servidor de instalación.

    Realice este paso si ha inhabilitado el software antivirus en el paso 3.
13. Actualice el servidor de instalación a la versión más reciente del fixpack.

    Ver [Actualizar el servidor de instalación y los agentes.](#actualización-del-servidor-de-instalación-y-los-agentes).

##### Resultados

El servidor de instalación de OpenPages está instalado.

Si ha utilizado el argumento `-s`, inicie el servidor de instalación. Para obtener más información, consulte [Inicio del servidor de instalación](5.1-guia-de-instalacion-y-despliegue-solo-local.md#inicio-del-servidor-de-instalación).

Ahora puede iniciar la sesión. Para el nombre de usuario, escriba `admin`. Para la contraseña, escriba la contraseña establecida cuando se ejecutó el script `install.sh`. Para obtener más información, consulte [Inicio de sesión en la aplicación de instalación](5.1-guia-de-instalacion-y-despliegue-solo-local.md#inicio-de-sesión-en-la-aplicación-de-instalación).

> **Nota:** Si ha utilizado el argumento `-m` pero algunos despliegues o usuarios no se han migrado, no vuelva a ejecutar el script `install.sh` . En lugar de ello, repita la migración sin volver a instalar. Ver [Migración de implementaciones y usuarios del servidor de instalación](#migración-de-despliegues-y-usuarios-del-servidor-de-instalación).

#### Instalación manual de agentes

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=server-installing-agents-manually)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

El servidor de instalación puede instalar automáticamente el software de agente en servidores remotos. Sin embargo, puede instalar manualmente el software de agente, si lo prefiere.

##### Antes de empezar

El sistema en el que se instale el software de agente debe cumplir los siguientes requisitos:

- IBM® SDK, Java™ Technology Edition o Java Runtime Environment (JRE) está instalado.
- Java se incluye en la variable de entorno del sistema PATH.

##### Acerca de esta tarea

Al especificar las propiedades de despliegue de un servidor remoto, se le solicitará que proporcione el nombre de usuario y la contraseña de una cuenta de administrador en el servidor remoto. El servidor de instalación utiliza estas credenciales para instalar el software de agente en el servidor remoto. Sin embargo, es posible que su organización tenga políticas que restrinjan el uso de credenciales de administrador. En este caso, puede instalar el software de agente manualmente antes de instalar OpenPages®.

El proceso global implica los pasos siguientes:

1. Instale manualmente el software de agente e iniciar el agente en cada servidor remoto, excepto en el servidor de base de datos. El software de agente no es necesario en el servidor de base de datos.
2. En la aplicación de instalación, especifique las propiedades de despliegue de los servidores remotos.

   - Habilite la opción **Despliegue remoto**.
   - Deje vacíos los campos **Nombre de usuario local** y **Contraseña de usuario local**.
   - En el campo **Directorio de agente**, escriba la ruta completa al directorio del servidor remoto en el que ha instalación el software de agente. Este directorio es el directorio `<agent_home>` .

##### Procedimiento

1. Inicie sesión en el servidor remoto como administrador.
2. Realice uno de los pasos siguientes:

   - Actualice la política de antivirus en el servidor remoto para permitir `Node.js`.
   - Inhabilite el software antivirus en el servidor remoto. Puede volver a habilitarlo después de instalar el software de agente.
3. Cree un directorio.

   Por ejemplo:

   - Windows: `C:\IBM\OPAgent`
   - Linux®: `/home/opuser/IBM/OPAgent`

   Este directorio será el directorio `<agent_home>` para el servidor remoto.
4. Copie el software de instalación del agente en el servidor remoto.

   1. Localice el archivo siguiente en el servidor de instalación: `<installation_server_home>/op-installer-agent.zip`.
   2. Copie `op-installer-agent.zip` en el directorio `<agent_home>` que ha creado en el servidor remoto.
   3. Extraiga el archivo `op-installer-agent.zip` en el directorio `<agent_home>` .
5. Abra una ventana de shell o de mandatos. Si utiliza Windows, abra la ventana de mandatos como administrador.
6. Vaya al directorio `<agent_home>/install/<OS>` .
7. Ejecute el script siguiente para instalar el software de agente:

   - Windows:

     ```bat
     install.bat -acceptLicense [/n <port>] [/s]
     ```

     Puede utilizar los siguientes argumentos opcionales:

     - `/n:<port>` - Establece el puerto en el que se ejecuta el agente de instalación al iniciarlo. Especifique un entero en el rango de 0 a 65535. Si excluye este argumento, se utiliza el número de puerto predeterminado (8443).
     - `/s`: impide que el agente de instalación se inicie después de que se complete el script `install.bat`. Si excluye este argumento, el agente de instalación se inicia automáticamente después de que se complete el script `install.bat`.
   - Linux:

     ```bash
     chmod 755 install.sh
     ./install.sh --acceptLicense [-n <port>] [-s]
     ```

     Puede utilizar los siguientes argumentos opcionales:

     - `-n <port>` - Establece el puerto en el que se ejecuta el agente de instalación al iniciarlo. Especifique un entero en el rango de 0 a 65535. Si excluye este argumento, se utiliza el número de puerto predeterminado (8443).
     - `-s`: impide que el agente de instalación se inicie después de que se complete el script `install.sh`. Si excluye este argumento, el agente de instalación se inicia automáticamente después de que se complete el script `install.sh`.
8. Cuando se complete el script, cierre la ventana de shell o la ventana de mandatos.
9. Inicie el agente.

   Consulte [Inicio manual del agente de instalación](#inicio-manual-del-agente-de-instalación).
10. Actualice el software de agente a la última versión del fixpack.

    Para obtener más información, consulte [Actualizar el servidor de instalación y los agentes](#actualización-del-servidor-de-instalación-y-los-agentes).
11. Repita estos pasos en cada servidor remoto, excepto en el servidor de base de datos.

##### Qué hacer a continuación

Cuando especifique las propiedades del servidor en la aplicación de instalación o en el archivo `deploy.properties`, realice los pasos siguientes:

- Habilite la opción **Despliegue remoto**.
- En el campo **Directorio de agente**, escriba la vía de acceso completa al directorio `<agent_home>` en el servidor remoto.
- Deje vacíos los campos **Nombre de usuario local** y **Contraseña de usuario local**.

Asegúrese de que los agentes se han iniciado antes de realizar tareas de instalación. Consulte [Inicio manual del agente de instalación](#inicio-manual-del-agente-de-instalación).

#### Actualización del servidor de instalación y los agentes

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=server-update-installation-agents)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Actualice el servidor de instalación de 9.0 para utilizar la última versión de 9.0.x.

La última versión del servidor de instalación se proporciona en el kit de instalación del fixpack.

Realice las tareas siguientes:

- Actualice el servidor de instalación.
- Si ha instalado el software de agente manualmente en servidores remotos, actualice el software de agente en cada servidor remoto.

##### Actualización del servidor de instalación

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación › Actualización del servidor de instalación y los agentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uisa-updating-installation-server)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de instalar una nueva versión de OpenPages® (un release, fixpack o arreglo temporal), actualice el servidor de instalación de 9.0 a la versión de fixpack 9.0.x más reciente.

###### Antes de empezar

El servidor de instalación de 9.0 ya debe estar instalado. Si está actualizando o migrando, instale el servidor de instalación de 9.0 y, a continuación, actualícelo a la última versión de 9.0.x.

###### Acerca de esta tarea

Este vídeo muestra cómo actualizar el servidor de instalación:

[En este vídeo se muestra cómo actualizar el servidor de instalación.](https://video.ibm.com/embed/channel/25817967/video/op-upgrade-installer)

###### Procedimiento

1. Descargue el fixpack de OpenPages más reciente de Fix Central.
2. Inicie la sesión en el sistema del servidor de instalación de OpenPages como el usuario que ha instalado el servidor de instalación.

   De forma alternativa, puede iniciar sesión como cualquier usuario que tenga permisos completos en los directorios del servidor de instalación y que pueda ejecutar `Node.js`.
3. Localice el archivo `openpages_installer_<version>.zip` en el kit de fixpack.

   El archivo se almacena en `/OP_<version>_Main/OP_<version>_Installer`.
4. Copie el archivo en el directorio `<Installation_server_home>/src/assets/maintenance` del servidor de instalación.
5. Detenga el servidor de instalación si se está ejecutando.
6. Actualice el servidor de instalación.

   1. Abra un indicador de mandatos como administrador o abra una ventana de shell.
   2. Vaya al directorio `<Installation_server_home>` y ejecute el mandato siguiente:

      ```
      npm run upgrade
      ```
7. Si la salida del mandato `npm run upgrade` incluye un mensaje sobre una actualización disponible para `Node.js`, ejecute el script de actualización especificado en el mensaje.

   Por ejemplo, la salida puede incluir el mensaje siguiente:

   ```
   ***Node.js  upgrade is available. Run the script
   "<InstallerHome>/install/<OS>/upgradeNode.sh|.bat" to finish  the upgrade.***
   ```

   Espere a que se complete la actualización y, a continuación, continúe con el paso 8.
8. Inicie el servidor de instalación.
9. Verifique la actualización. Inicie sesión en la aplicación de instalación, abra cualquier despliegue y pulse **Acerca de** para ver el número de versión.
10. Si ha instalado el software de agente manualmente en los servidores remotos en el despliegue, actualice el software de agente en cada servidor remoto.

    Para más información, ver [Actualizar agentes manualmente](#actualización-manual-de-un-agente).

    > **Nota:** No pulse **Validar** hasta que haya actualizado el software de agente en cada servidor remoto.

    Si el servidor de instalación ha instalado el software de agente en los servidores remotos, no es necesario actualizar manualmente los agentes. El servidor de instalación actualiza los agentes automáticamente al pulsar **Validar**.

##### Actualización manual de un agente

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación › Actualización del servidor de instalación y los agentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uisa-updating-agents-manually)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Utilice este procedimiento para actualizar el software de agente manualmente a una versión de fixpack 9.0.0.x.

###### Antes de empezar

El servidor de instalación de 9.0 y los agentes ya deben estar instalados. Si está actualizando o migrando, instale el servidor de instalación y los agentes de 9.0 y, a continuación, actualícelos a la última versión de 9.0.x.

###### Acerca de esta tarea

El servidor de instalación puede actualizar automáticamente el software de agente en servidores remotos. Pero puede actualizar el software de agente manualmente, si lo prefiere.

Al especificar las propiedades de despliegue de un servidor remoto, se le solicitará que proporcione el nombre de usuario y la contraseña de una cuenta de administrador en el servidor remoto. El servidor de instalación utiliza estas credenciales para actualizar el software de agente en el servidor remoto. Sin embargo, es posible que su organización tenga políticas que restrinjan el uso de credenciales de administrador. En este caso, puede actualizar el software de agente manualmente antes de instalar OpenPages® o aplicar un fixpack.

El proceso global implica los pasos siguientes:

1. Actualice el servidor de instalación. Consulte [Actualización del servidor de instalación](#actualización-del-servidor-de-instalación).
2. Actualice manualmente el software de agente e inicie el agente en cada servidor remoto, excepto en el servidor de base de datos. El software de agente no es necesario en el servidor de base de datos.
3. En la aplicación de instalación, especifique las propiedades de despliegue de los servidores remotos.

   - Habilite la opción **Despliegue remoto**.
   - Puede dejar vacíos los campos **Nombre de usuario local** y **Contraseña de usuario local**.
   - En el campo **Directorio de agente**, escriba la ruta completa al directorio en el servidor remoto en el que está instalado el software de agente. Este directorio es el directorio `<agent_home>` .
4. Valide el despliegue y continúe con la instalación de OpenPages o el fixpack.

###### Procedimiento

1. Inicie sesión en el servidor remoto como usuario que ha instalado el software de agente.

   De forma alternativa, puede iniciar sesión como cualquier usuario que tenga permisos completos en los directorios del agente y que pueda ejecutar `Node.js`.
2. Detenga el agente.

   Para obtener más información, consulte [Detención manual del agente de instalación](#parada-manual-del-agente-de-instalación).
3. Copie el archivo de instalación en el servidor remoto.

   1. Localice el archivo siguiente en el kit de fixpack 9.0.0.x: `openpages_installer_<version>.zip`

      El archivo se almacena en `/OP_<version>_Main/OP_<version>_Installer`.
   2. Copie `openpages_installer_<version>.zip` en el directorio `<agent_home>/src/assets/maintenance` del servidor de instalación.

      No extraiga el archivo.
4. Actualice el software de agente.

   En Windows:

   1. Verifique que no haya solicitudes de mandatos o aplicaciones, como el Explorador de Windows, que accedan al directorio `<agent_home>` o a sus subdirectorios.
   2. Abra un indicador de mandatos como administrador.
   3. Vaya al directorio `<agent_home>`
   4. Ejecute el siguiente mandato.

      ```
      npm run upgrade
      ```

   En Linux®:

   1. Abra un shell y vaya al directorio `<agent_home>` .
   2. Ejecute el siguiente mandato.

      ```
      npm run upgrade
      ```

   Cuando se complete el proceso, se visualiza el siguiente mensaje:

   ```
   Installer upgrade is successful...
   ```
5. Si la salida del mandato `npm run upgrade` incluye un mensaje sobre una actualización disponible para `Node.js`, ejecute el script de actualización especificado en el mensaje.

   Por ejemplo, la salida puede incluir el mensaje siguiente:

   ```
   ***Node.js  upgrade is available. Run the script
         "<InstallerHome>/install/<OS>/upgradeNode.sh|.bat" to finish  the upgrade.***
   ```

   Espere a que se complete la actualización y, a continuación, continúe con el paso 6.
6. Inicie el agente.

   Consulte [Inicio manual del agente de instalación](#inicio-manual-del-agente-de-instalación).
7. Repita estos pasos en cada servidor remoto, excepto en el servidor de base de datos.

###### Qué hacer a continuación

Cuando especifique las propiedades del servidor, realice lo siguiente:

- Habilite la opción **Despliegue remoto**.
- En el campo **Directorio de agente**, escriba la vía de acceso completa al directorio `<agent_home>` en el servidor remoto.
- Puede dejar vacíos los campos **Nombre de usuario local** y **Contraseña de usuario local**.

  > **Nota:** Si deja vacíos los campos **Nombre de usuario local** y **Contraseña de usuario local** , debe iniciar los agentes manualmente. Consulte [Inicio manual del agente de instalación](#inicio-manual-del-agente-de-instalación).

#### Migración de despliegues y usuarios del servidor de instalación

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=server-migrating-deployments-installation-users)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede migrar despliegues y cuentas de usuario desde un servidor de instalación de 8.2.x o 8.3.x al servidor de instalación de 9.0 OpenPages® .

##### Acerca de esta tarea

Realice esta tarea si se cumplen las condiciones siguientes:

- Tiene un servidor de instalación 8.2.x o 8.3.x (el servidor de instalación de origen).
- Configure el servidor de instalación de 9.0 (el servidor de instalación de destino).
- Al configurar el servidor de instalación de 9.0 , no ha migrado despliegues y cuentas de usuario del servidor de instalación de origen utilizando el argumento `/m` (Microsoft Windows) o `-m` (Linux®).

  O bien, los ha migrado, pero algunos despliegues o cuentas de usuario no se han migrado.

Al realizar la migración, tenga en cuenta las siguientes consideraciones:

- Los despliegues y usuarios que ya existen en el servidor de instalación de 9.0 no se migran.
- Las cuentas de usuario del servidor de instalación de origen en las que faltan contraseñas no se migran.
- Un despliegue no se migra si se están ejecutando procesos de validación, instalación o configuración.

##### Procedimiento

1. Si la aplicación de instalación está abierta, cierre la sesión y cierre la ventana del navegador.
2. Detenga el servidor de instalación de 8.2.x o 8.3.x .

   - **Windows**

     - Detenga `ibmopenpageswithwatsoninstaller<version>.exe`.
     - O bien, vaya al directorio `<installation_server_home>` del servidor de instalación que desea detener. Abra un indicador de mandatos como administrador y ejecute el siguiente mandato:

       ```
       npm run stop
       ```

   - **Linux**

     1. Abra un shell y vaya al directorio `<installation_server_home>` del servidor de instalación que desea detener, por ejemplo `/home/opuser/IBM/OPInstall/OP_<version>_Installer`.
     2. Ejecute el mandato siguiente:

        ```
        npm run stop
        ```
3. Inicie sesión en el sistema en el que ha configurado el servidor de instalación de 9.0 .
4. Migrar despliegues y cuentas de usuario al servidor de instalación de 9.0 .

   1. Abra un shell o una ventana de mandatos y vaya al directorio `<installation_server_home>` , por ejemplo `/home/opuser/IBM/OPInstall/OP_<version>_Installer`.
   2. Ejecute el mandato siguiente:

      Sustituya `<old_directory>` por la vía de acceso completa al directorio de inicio del servidor de instalación 8.2.xo 8.3.x .

      ```
      npm run migration <old_directory>
      ```

   Si un despliegue o una cuenta de usuario no se migra, solucione los problemas y, a continuación, vuelva a ejecutar la migración.

#### Inicio manual del agente de instalación

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=server-starting-installation-agent-manually)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede iniciar manualmente el agente en un servidor remoto.

##### Acerca de esta tarea

Al especificar las propiedades de despliegue de un servidor remoto, se le solicitará que proporcione el nombre de usuario y la contraseña de una cuenta de administrador en el servidor remoto. El servidor de instalación utiliza estas credenciales para iniciar y detener el software de agente en el servidor remoto. Si no especifica credenciales de inicio de sesión en las propiedades de despliegue e instala el software de agente manualmente, debe iniciar y detener manualmente el agente. No puede utilizar la aplicación de instalación para iniciar o detener el agente.

También puede iniciar y detener los agentes manualmente si prefiere utilizar la línea de mandatos.

##### Procedimiento

1. Inicie sesión en el servidor remoto como usuario que ha instalado el software de agente.

   De forma alternativa, puede iniciar sesión como cualquier usuario que tenga permisos completos en los directorios del agente y que pueda ejecutar `Node.js`.
2. Inicie el agente de instalación.

   - **Windows**

     Realice uno de los pasos siguientes:

     - Inicie el servicio `ibmopenpageswithwatsoninstaller<version>.exe`.
     - Vaya al directorio `<agent_home>\install\Windows`. Pulse con el botón derecho del ratón en el archivo `startup.bat` y pulse **Ejecutar como administrador**.

   - **Linux®**

     1. Abra un shell y vaya al directorio `<agent_home>/install/Linux`.
     2. Ejecute el mandato siguiente:

        ```bash
        ./startup.sh
        ```

##### Resultados

El agente de instalación se está ejecutando.

#### Parada manual del agente de instalación

`Guía de actualización para Db2 (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=server-stopping-installation-agent-manually)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

El agente de un servidor remoto se puede parar manualmente.

##### Acerca de esta tarea

Al especificar las propiedades de despliegue de un servidor remoto, se le solicitará que proporcione el nombre de usuario y la contraseña de una cuenta de administrador en el servidor remoto. El servidor de instalación utiliza estas credenciales para iniciar y detener el software de agente en el servidor remoto. Si no especifica credenciales de inicio de sesión en las propiedades de despliegue e instala el software de agente manualmente, debe iniciar y detener manualmente el agente. No puede utilizar la aplicación de instalación para iniciar o detener el agente.

También puede iniciar y detener los agentes manualmente si prefiere utilizar la línea de mandatos.

##### Procedimiento

1. Inicie sesión en el servidor remoto como usuario que ha instalado el software de agente.

   De forma alternativa, puede iniciar sesión como cualquier usuario que tenga permisos completos en los directorios del agente y que pueda ejecutar `Node.js`.
2. Pare el agente de instalación.

   - Windows: Detenga el servicio `ibmopenpageswithwatsoninstaller<version>.exe` . O bien, abra un indicador de mandatos como administrador, vaya al directorio `<agent_home>` y ejecute el mandato siguiente:

     ```
     npm run stop
     ```
   - Linux®: Vaya al directorio `<agent_home>` y ejecute el mandato siguiente:

     ```
     npm run stop
     ```

##### Resultados

El agente de instalación ha parado.

### Actualización OpenPages

`Guía de actualización para Db2 (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrading-openpages)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Realice una actualización para obtener los últimos arreglos y características.

#### Antes de empezar

- Lleve a cabo las siguientes tareas de preparación:

  - Descargue el kit de instalación desde Passport Advantage®
  - [Revisión de las características y arreglos nuevos](#revisión-de-las-características-y-arreglos-nuevos)
  - [Copia de seguridad del entorno](#copia-de-seguridad-del-entorno)
  - [Verificación de los servidores antes de la actualización](#verificación-de-los-servidores-antes-de-la-actualización)
- Si ha instalado manualmente los agentes en servidores remotos, asegúrese de que los agentes están en ejecución.
- Si los servidores de aplicaciones no pueden acceder a Internet y ha actualizado las características de WebSphere® Liberty manualmente en el pasado, realice los pasos del 1 al 6 en la tarea siguiente: [Actualización manual de las características de WebSphere](5.1-guia-de-instalacion-y-despliegue-solo-local.md#actualización-manual-de-las-características-de-websphere-liberty) .
- Actualice la base de datos de OpenPages . Para obtener más información, consulte [Actualizar la base de datos OpenPages (Db2)](#actualice-la-base-de-datos-openpages-db2).
- Asegúrese de que IBM® Cognos® Configuration no se esté ejecutando.
- Asegúrese de que el gestor de despliegue, todos los servidores de aplicaciones OpenPages (admin y no admin) y el servidor de búsqueda estén detenidos.
- Asegúrese de que todos los servidores de informes (activos y en espera) están en ejecución.

#### Acerca de esta tarea

Utilice el servidor de instalación para actualizar OpenPages.

#### Procedimiento

1. Inicie sesión en la aplicación de instalación de OpenPages .

   Para obtener más información, consulte [Inicio de sesión en la aplicación de instalación](5.1-guia-de-instalacion-y-despliegue-solo-local.md#inicio-de-sesión-en-la-aplicación-de-instalación).
2. Abra el despliegue que desea actualizar.

   Si el despliegue ya está abierto, renueve la página.
3. Revise los valores de cada tarjeta de servidor.
4. Pulse la lista **Tarea de despliegue** y seleccione **Actualizar**y, a continuación, seleccione la versión que desea instalar.

   Si **Actualizar** no se muestra en la lista **Tarea de despliegue**, pulse **Validar**.

   *Figura 1. Selección de la tarea de actualización*

   ![La lista de tipos de despliegue se expande y se selecciona Actualizar. También se muestra la versión, 9.0.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/op_inst_upgrade.png)
5. En cada tarjeta de servidor de aplicaciones, verifique que **Directorio de inicio de Java** esté establecido en IBM SDK, Java™ Technology Edition que ha instalado en el servidor de aplicaciones.
6. Pulse **Validar**.
7. Pulse **Instalar**.

   > **Sugerencia:** Puede cerrar la sesión y cerrar la ventana del navegador. El proceso de **instalación** continúa ejecutándose. Cuando vuelve a iniciar la sesión en la aplicación de instalación, la aplicación muestra el estado del despliegue. También puede cerrar la ventana de navegador durante el proceso de **configuración**.
8. Pulse **Configurar**.

#### Qué hacer a continuación

Lleve a cabo las tareas posteriores a la instalación. Para obtener más información, consulte [Tareas posteriores a la actualización](#tareas-posteriores-a-la-actualización).

### Tareas posteriores a la actualización

`Guía de actualización para Db2 (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrading-post-upgrade-tasks)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Después de actualizar IBM OpenPages®, debe completar algunas tareas adicionales.

- Actualice los valores de instancia de Db2® . Consulte [Actualización de los valores de instancia de Db2](#actualización-de-los-valores-de-instancia-de-db2).
- Actualice el archivo `ObjectManager.properties` con los siguientes valores:

  ```properties
  configuration.manager.vendor.mode=false
  configuration.manager.disable.triggers=false
  ```
- Restaure las personalizaciones y los valores de configuración del servidor de aplicaciones. Consulte [Restaurar la configuración personalizada del servidor de aplicaciones](#restaurar-valores-del-servidor-de-aplicaciones-personalizado).
- Si utiliza la búsqueda global, vuelva a crear el índice. Véase [Volver a crear el índice para la búsqueda global](#volver-a-crear-el-índice-para-la-búsqueda-global).
- Actualice los informes de plataforma y soluciones. Véase [Actualización de informes](#actualizar-informes).
- Si ha utilizado vistas del sistema en el entorno de origen, es posible que tenga que realizar alguna remediación. Durante una migración se actualizan las vistas del sistema, pero el esquema no. Cuando abra una vista, es posible que vea errores como, por ejemplo, «“El campo `<field_name>` es obligatorio.”» Edite las vistas para resolver errores, por ejemplo eliminando o añadiendo los campos, grupos de campos o dependencias de campos que no estén en el esquema.
- Si utiliza LDAP, debe volver a habilitarlo. Consulte [Activar LDAP después de actualizar o migrar](#habilitar-ldap-después-de-actualizar-o-migrar).
- Si utiliza campos calculados, consulte [Actualización de campos calculados personalizados](#actualización-de-campos-calculados-personalizados).
- Actualice el esquema de elaboración de informes. Véase [Actualización del esquema de informes](#actualización-del-esquema-de-elaboración-de-informes).
- Vuelva a generar el entorno de elaboración de informes.

  En función de su entorno, es posible que necesite volver a generar el entorno de elaboración de informes. Para más información, véase [Regenerar el marco de información](#regeneración-del-entorno-de-elaboración-de-informes).

#### Actualización de los valores de instancia de Db2

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-updating-db2-settings-after-migration-upgrade)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Después de migrar o actualizar IBM OpenPages®, debe actualizar los valores de la instancia de Db2® .

##### Procedimiento

1. Inicie sesión en el servidor de bases de datos como propietario de instancia de Db2 , por ejemplo `db2inst1` en Linux® o `db2admin` en Windows.
2. Ejecute el mandato `db2set` .

   El mandato devuelve una lista de variables de perfil de Db2 y sus valores, por ejemplo:

   ```properties
   DB2_DEFERRED_PREPARE_SEMANTICS=YES
   DB2_ATS_ENABLE=YES
   DB2_COMPATIBILITY_VECTOR=ORA
   DB2_OPTPROFILE=YES
   DB2_NUM_CKPW_DAEMONS=0
   DB2_REDUCED_OPTIMIZATION=JULIE
   DB2_EVALUNCOMMITTED=ON
   DB2_EXTENDED_OPTIMIZATION=NO_HVCHECK_ALL,IXOR
   DB2_SKIPDELETED=ON
   DB2COMM=SSL,TCPIP
   DB2_PARALLEL_IO=*
   DB2AUTOSTART=YES
   ```
3. En los resultados del paso 2, busque `DB2COMPOPT`y, a continuación, realice uno de los pasos siguientes:

   - Si `DB2COMPOPT` no aparece en la lista, ejecute el mandato siguiente para establecerlo:

     ```
     db2set DB2COMPOPT=NO_SCALAR2OJ_ROW
     ```
   - O, si se lista `DB2COMPOPT`, ejecute el mandato siguiente para actualizar su valor:

     ```
     db2set DB2COMPOPT=<existing_values>,NO_SCALAR2OJ_ROW
     ```
4. Vuelva a ejecutar `db2set` y verifique los cambios en `DB2COMPOPT`.

   Por ejemplo:

   ```properties
   DB2_DEFERRED_PREPARE_SEMANTICS=YES
   DB2_ATS_ENABLE=YES
   DB2_COMPATIBILITY_VECTOR=ORA
   DB2_OPTPROFILE=YES
   DB2_NUM_CKPW_DAEMONS=0
   DB2_REDUCED_OPTIMIZATION=JULIE
   DB2_EVALUNCOMMITTED=ON
   DB2_EXTENDED_OPTIMIZATION=NO_HVCHECK_ALL,IXOR
   DB2_SKIPDELETED=ON
   DB2COMPOPT=NO_SCALAR2OJ_ROW
   DB2COMM=SSL,TCPIP
   DB2_PARALLEL_IO=*
   DB2AUTOSTART=YES
   ```
5. En los resultados del paso 4, busque `DB2_EXTENDED_OPTIMIZATION`y, a continuación, realice uno de los pasos siguientes:

   - Si los resultados muestran `DB2_EXTENDED_OPTIMIZATION=NO_HVCHECK_ALL,IXOR`, ejecute el mandato siguiente para actualizar la variable:

     ```
     db2set DB2_EXTENDED_OPTIMIZATION=NO_HVCHECK_ALL,IXOR,"MAX_CSE_SGSIZE 20"
     ```
   - O bien, ejecute el mandato siguiente para actualizar la variable sin sobrescribir sus valores existentes:

     ```
     db2set DB2_EXTENDED_OPTIMIZATION=<existing_values>,"MAX_CSE_SGSIZE 20"
     ```
6. Vuelva a ejecutar `db2set` y verifique los cambios en `DB2_EXTENDED_OPTIMIZATION`.

   Por ejemplo:

   ```properties
   DB2_DEFERRED_PREPARE_SEMANTICS=YES
   DB2_ATS_ENABLE=YES
   DB2_COMPATIBILITY_VECTOR=ORA
   DB2_OPTPROFILE=YES
   DB2_NUM_CKPW_DAEMONS=0
   DB2_REDUCED_OPTIMIZATION=JULIE
   DB2_EVALUNCOMMITTED=ON
   DB2_EXTENDED_OPTIMIZATION=NO_HVCHECK_ALL,IXOR,MAX_CSE_SGSIZE 20
   DB2_SKIPDELETED=ON
   DB2COMPOPT=NO_SCALAR2OJ_ROW
   DB2COMM=SSL,TCPIP
   DB2_PARALLEL_IO=*
   DB2AUTOSTART=YES
   ```
7. Reinicie la instancia de Db2 . Debe reiniciar la instancia para que los cambios entren en vigor.

#### Eliminar el botón de lanzamiento de interfaz de usuario de cuestionario heredado de la vista de administración para las evaluaciones de cuestionario

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-remove-legacy-questionnaire-ui-launch-button-from-admin-view-questionnaire-assessments)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

La vista de administrador de evaluación de cuestionario muestra el botón **Iniciar interfaz de usuario de cuestionario** heredado. Si un administrador pulsa este botón, se visualiza una página de error 404.

##### Acerca de esta tarea

Para eliminar este botón, cree una vista de administrador personalizada para las evaluaciones de cuestionario y elimine el campo **IU de cuestionario** de la vista y haga que la vista de administrador personalizada sea la predeterminada.

Puesto que los campos que están en el perfil pero que no están ya en la vista se añadirán automáticamente en tiempo de ejecución, elimine todas las referencias al campo **RespQuest** de todos los perfiles utilizados por los administradores.

##### Procedimiento

1. Haz clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Vistas**.
2. Pulse **Nueva vista**.
3. Especifique un **Nombre**. Los caracteres permitidos son A-Z, a-z, 0-9, subrayado, guion y espacios. No se permiten caracteres especiales.

   El **Nombre** que especifique se copia en **Etiqueta**.
4. Opcional: especifique una **Descripción**.
5. Pulse **Tipo** y seleccione **Admin**.
6. Haga clic en **Tipo de objeto** y seleccione **Evaluación de cuestionario**.
7. Dejar **habilitado** seleccionado.
8. Seleccione **Utilizar como vista predeterminada para este tipo de objeto para todos los perfiles** para hacer que la vista sea la vista de administrador predeterminada para el tipo de objeto.
9. En **Copiar de vista**, pulse **Seleccionar una vista**. Seleccione la vista de administración predeterminada actual para las evaluaciones de cuestionario.
10. Pulse **Crear**.

    Se abre el Diseñador de vistas con la pestaña **Diseño** visualizada.
11. Realice uno de los pasos siguientes:

    - Suprima el campo **Interfaz de usuario de cuestionario** del área de lienzo.
    - Pulse la pestaña **JSON** .

      Busque y elimine las líneas siguientes del JSON:

      ```json
      {
                "name": "OPSS-QAssessment:RespQuest",
                "readonly": true
               },
      ```
12. Pulse **Publicar**.
13. Haz clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Perfiles**.
14. Para cada perfil utilizado por los administradores, realice los pasos siguientes:

    1. Pulse el perfil.
    2. Expanda **Tipos de objeto**.
    3. Haga clic en **Evaluación de cuestionario**.
    4. Expanda **Campos** y busque **RespQuest**.
    5. Seleccione **RespQuest** y pulse **Eliminar**.

#### Actualización de aplicaciones opcionales

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tasks-updating-optional-apps)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si utiliza apps opcionales, como conectores IBM OpenPages® , es posible que tenga que actualizarlas al actualizar a 9.0.

##### Actualización desde 8.2.0.0

Si utiliza IBM OpenPages SDI Connector for UCF Common Controls Hub o el conector QRadar® , debe actualizar IBM® Security Directory Integrator a la versión 7.2.0.6.

- [Actualización de UCF](5.1-guia-de-instalacion-y-despliegue-solo-local.md#actualización-de-ibm-openpages-sdi-connector-for-ucf-common-controls-hub)
- [Actualización de QRadar](5.1-guia-de-instalacion-y-despliegue-solo-local.md#actualización-de-ibm-security-directory-integrator-para-el-conector-qradar)

#### Restaurar valores del servidor de aplicaciones personalizado

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tasks-restore-custom-application-server-settings)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Después de actualizar, restaure los valores de configuración y las personalizaciones del servidor de aplicaciones.

Si ha realizado cambios en los siguientes archivos en el entorno previo a la actualización, vuelva a implementar los cambios después de la actualización.

- `<OP_HOME>/aurora/conf/aurora.properties`
- `<OP_HOME>/aurora/conf/Server<#>-server.properties`
- `<OP_HOME>/aurora/conf/Server<#>-sosa.properties`

Por ejemplo, consulte [Acortar la URL para OpenPages®](3.4-guia-del-administrador.md#acortar-la-url-para-openpages)

Si se ha configurado el inicio de sesión único (SSO) en el sistema de origen, debe actualizar la configuración de SSO en el entorno de destino. Para obtener más información, consulte [Integración de inicio de sesión único para el servidor de aplicaciones OpnePages](5.2-guia-de-instalacion-y-despliegue-solo-local.md#integración-de-inicio-de-sesión-único-para-el-servidor-de-aplicaciones-openpages).

#### Restauración de asistentes de soluciones, imágenes y otros archivos

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-restoring-solutions-helpers-images-other-files)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Restaure los asistentes de soluciones, imágenes y otras entregas personalizadas de las que ha realizado copia de seguridad.

##### Acerca de esta tarea

Si ha realizado una copia de seguridad de los elementos siguientes, restáurelos:

- Esquema de soluciones
- Entregables personalizados de IBM® Expert Labs
- Código personalizado

#### Volver a crear el índice para la búsqueda global

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-re-creating-index-global-search)

**Se aplica a:** En los locales

Puede volver a crear el índice para la búsqueda global.

> **Importante:** Si ha actualizado o migrado a ' IBM OpenPages® 9 9.0.0 desde 8.2.0.x, debe volver a crear el índice para la búsqueda global. Si no vuelve a crear el índice, la búsqueda global no funcionará.

Si necesita solucionar un problema al volver a crear el índice para la búsqueda global, o si prefiere utilizar una interfaz de línea de comandos, puede utilizar la CLI para volver a crear el índice. Para obtener más información, consulte [¿Cómo automatizar las tareas de Solr?](https://www.ibm.com/support/pages/node/6409982)

##### Procedimiento

1. Inicie sesión en ' OpenPages ' como usuario con privilegios administrativos.
2. Haz clic en " **Abrir el menú Administración ' ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Búsqueda global** " y en " **Desactivar**".
3. Pulse **Descartar** para descartar el índice de búsqueda.

   Espere a que finalice el proceso de descartado.
4. Pulse **Crear** para volver a crear el índice de búsqueda.

#### Actualizar informes

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-updating-reports)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si ha actualizado o migrado desde 8.2, actualice los informes de IBM® Cognos® Analytics .

> **Nota:** Si ha actualizado o migrado desde 8.3 o posterior, no es necesario que realice esta tarea.

Siga los pasos siguientes:

- **Si ha migrado**

  1. Importe el paquete de **OpenPages PlatformV6**

     La ubicación del paquete es:

     - IBM Db2®: `OP_<version>_Main/OP_<version>_Configuration/Platform/Upgrade/DB2/`
     - Oracle: `OP_<version>_Main/OP_<version>_Configuration/Platform/Upgrade/Oracle/`
  2. Aplique la extensión OpenPages® para IBM Cognos Analytics.

     El nombre y la ubicación del paquete son: `OP_<version>_Main/OP_<version>_Configuration/Platform/Upgrade/OpenPages.zip`

     Para obtener más información, consulte la [documentación deCognos](https://www.ibm.com/docs/en/SSEP7J_11.1.0/com.ibm.swg.ba.cognos.ag_manage.doc/c_mng_cust_manage.html#cust_mng_th_rext__title__4).
  3. Cree un parámetro de autenticación para OpenPages. Utilice el valor `optoken`.

     Para obtener más información, consulte la [documentación deCognos](https://www.ibm.com/docs/en/SSEP7J_11.1.0/com.ibm.swg.ba.cognos.ag_manage.doc/t_ca_manage_allow_login_parameters_url.html).
  4. Importe el paquete de **OpenPages SolutionsV6**. Para obtener más información, consulte [Importación del paquete de informes de soluciones](#importación-del-paquete-de-informes-de-soluciones).
  5. Si desea utilizar informes personalizados del entorno de origen, impórtelos en el entorno de 9.0 . Para obtener más información, consulte [Mover el contenido con un archivo de despliegue](https://www.ibm.com/docs/SSEP7J_11.2.0/com.ibm.swg.ba.cognos.inst_cr_winux.doc/c_moveyourcontentusingadeploymentarchive.html) en la documentación de Cognos. A continuación, actualice los enlaces CrossTrack en los informes.
  6. Actualice los enlaces CrossTrack en los informes de soluciones V6, informes de plataforma V6 y cualquier informe personalizado.

- **Si ha actualizado**

  1. Importe el paquete de **OpenPages SolutionsV6**. Para obtener más información, consulte [Importación del paquete de informes de soluciones](#importación-del-paquete-de-informes-de-soluciones).
  2. Actualice los enlaces CrossTrack en los informes de soluciones V6, informes de plataforma V6 y cualquier informe personalizado.

##### Actualización de enlaces CrossTrack en informes

Este release incluye enlaces JavaScript actualizados para CrossTrack en informes de plataforma y solución.

Actualice los informes que desea seguir utilizando en 9.0:

- Actualice los informes en la carpeta **OpenPages Platform v6** para utilizar el JavaScript actualizado para enlaces CrossTrack . Es posible que pueda utilizar algunos de los informes de la carpeta de **Informes de OpenPages Platform** en su lugar, en función del esquema.
- Actualice los informes de soluciones con el JavaScriptactualizado. para enlaces CrossTrack.
- Si tiene informes personalizados, actualícelos para utilizar el JavaScriptactualizado. para enlaces CrossTrack..

Para obtener más información, consulte los siguientes temas:

- [Adición de enlaces CrossTrack a informes autónomos y padres](10-guia-del-creador-de-informes.md#adición-de-enlaces-crosstrack-a-informes-autónomos-y-padres)
- [Adición de enlaces CrossTrack a informes de acceso a detalles](10-guia-del-creador-de-informes.md#adición-de-enlaces-crosstrack-a-informes-de-acceso-a-detalles)

##### Carpetas de informes

Después de completar estas tareas, tiene las carpetas siguientes en IBM Cognos Analytics:

- **Contenido del equipo** > **OpenPages Platform**

  Esta carpeta contiene los informes de la plataforma 9.0 .
- **Team Content** > **OpenPages Platform V6**

  Esta carpeta contiene los informes previos a la plataforma9.0 .
- **Team Content** > **OpenPages Solutions V6**

  Esta carpeta contiene los informes de soluciones anteriores a9.0 .

#### Habilitar LDAP después de actualizar o migrar

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-enable-ldap-after-upgrading-migrating)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si ha utilizado LDAP en la versión anterior de IBM OpenPages®, debe volver a habilitar LDAP.

Para obtener más información, consulte [Habilitación de LDAP de modalidad mixta](3.1-guia-del-administrador.md#configuración-de-la-autenticación-de-modo-mixto).

#### Tareas posteriores a la actualización para las soluciones

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=tasks-post-upgrade-solutions)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Después de actualizar OpenPages®, es posible que tenga que realizar algunas tareas posteriores a la instalación para actualizar las soluciones de OpenPages .

> **Nota:**

> La versión 9.0 incluye muchas actualizaciones de las soluciones. Estas actualizaciones sólo están disponibles en instalaciones nuevas. Las soluciones no se actualizan cuando el usuario actualiza porque las soluciones están diseñadas para trabajar con el modelo de objetos (tipos de objetos, relaciones de objetos, campos, etc.) de una versión específica. Puesto que OpenPages es muy configurable, el modelo de objeto se puede cambiar fácilmente. El proceso de actualización no puede suponer que el modelo de objeto existente no ha cambiado y que los cambios para las soluciones de 9.0 se pueden integrar en el modelo de objeto.

> Si desea actualizar las soluciones, póngase en contacto con el representante de IBM® o el socio de IBM para debatir un compromiso de servicios.

##### Actualización desde 8.3

- Realice una copia de seguridad de los informes de soluciones y luego importe el paquete de informes de soluciones para actualizar los informes. Para obtener más información, consulte [Importación del paquete de informes de soluciones](#importación-del-paquete-de-informes-de-soluciones).
- Sustituir los campos computados RCSA por campos URL. Véase [Sustitución de campos calculados por campos de lanzador de URL (RCSA)](#sustitución-de-campos-calculados-por-campos-de-lanzamiento-de-url-rcsa).
- Si ha migrado a 8.3 y luego a 9.0, compruebe que ha completado los pasos de [Sustitución de campos computados por cálculos y campos de lanzador de URL (IAM e ITG)](#sustitución-de-campos-calculados-por-cálculos-y-campos-de-lanzador-de-url-iam-e-itg).
- Si tiene campos calculados personalizados que generan HTML que contiene JavaScript, sustitúyalos por campos de lanzador de URL. Consulte [Actualización de campos calculados personalizados](#actualización-de-campos-calculados-personalizados).

##### Actualización desde 8.2

- Realice una copia de seguridad de los informes de soluciones y luego importe el paquete de informes de soluciones para actualizar los informes. Para obtener más información, consulte [Importación del paquete de informes de soluciones](#importación-del-paquete-de-informes-de-soluciones).
- Sustituya los campos calculados para las soluciones siguientes:

  - IBM OpenPages Internal Audit Management
  - IBM OpenPages IT Governance

  Para obtener más información, consulte [Sustitución de campos calculados por cálculos y campos de lanzador de URL (IAM e ITG)](#sustitución-de-campos-calculados-por-cálculos-y-campos-de-lanzador-de-url-iam-e-itg).
- Sustituir los campos computados RCSA por campos URL. Véase [Sustitución de campos calculados por campos de lanzador de URL (RCSA)](#sustitución-de-campos-calculados-por-campos-de-lanzamiento-de-url-rcsa).
- Si tiene campos calculados personalizados que generan HTML que contiene JavaScript, sustitúyalos por campos de lanzador de URL. Consulte [Actualización de campos calculados personalizados](#actualización-de-campos-calculados-personalizados).

##### Sustitución de campos calculados por cálculos y campos de lanzador de URL (IAM e ITG)

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización › Tareas posteriores a la actualización para las soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=puts-replacing-computed-fields-calculations-url-launcher-fields-iam-itg)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

IBM OpenPages® Internal Audit Management y IBM OpenPages IT Governance han utilizado campos calculados en releases anteriores. Puede actualizar los campos para utilizar cálculos y enlaces GRC en lugar de campos calculados. Los campos se sustituyen por campos nuevos que utilizan los mismos nombres. Esta tarea es opcional.

###### Acerca de esta tarea

> **Nota:** No es necesario realizar esta tarea en los casos siguientes:

> - Ha realizado una instalación nueva de 8.2 o posterior y, a continuación, ha migrado a 8.3 o 9.0.
> - Está migrando desde 8.2 o posterior y ya ha completado estos pasos en el entorno de origen.

Esta tarea realiza los cambios siguientes en el entorno:

- Sustituye los campos calculados siguientes por campos calculados:

  - AuditableEntity: OPSS-AudEnt: Weighted Risk Score
  - AuditProgram: OPSS-Aud: Actual T&E
  - AuditProgram: OPSS-Aud: Actual Hours
  - Plan: OPSS-Plan: Actual Hours
  - Plan: OPSS-Plan: Actual T&E
- Sustituye los siguientes campos calculados por campos de lanzador de URL (Enlace):

  - AuditProgram: OPSS-Aud: Close Audit
  - AuditProgram: OPSS-Aud: Plans
  - RiskEntity: OPSS-RiskEnt: Baselines
  - Resource: OPSS-Res: Resource Links
- Añade un padre primario a objetos Preference . Esta actualización es necesaria para el cálculo de la puntuación de riesgo ponderado de la entidad auditable.

Si desea revisar los cambios antes de implementarlos, consulte los archivos listados en el paso 1.

###### Procedimiento

1. Copie los archivos siguientes del soporte de instalación al servidor de aplicaciones. O, si ejecuta ObjectManager desde un sistema remoto, como el portátil, copie los archivos en el sistema remoto.

   - `IAM_ITG_computed_field_replacement-op-config.xml`
   - `IAM_computed_field_preference_updates.xls`

   Los archivos se encuentran en el directorio `/OP_<version>_Main/OP_<version>_Configuration/Modules/IAM_ITG`.
2. Abra una línea de mandatos.

   Si utiliza Microsoft Windows, abra un indicador de mandatos con la opción **Ejecutar como administrador** .
3. Vaya al directorio `<OP_HOME>/bin` .

   O, si está ejecutando ObjectManager desde un sistema remoto, vaya al directorio `openpages-tools-client/bin` .
4. Ejecute el mandato siguiente para cargar los campos actualizados.

   Sustituya `<loader-file-path>` por la ubicación del archivo `IAM_ITG_computed_field_replacement-op-config.xml` .

   ```bat
   ObjectManager.cmd|sh l c <OpenPages Administrator user> <OpenPages Administrator password> <loader-file-path> IAM_ITG_computed_field_replacement
   ```

   Si encuentra algún error, revise el archivo de registro, `<loader-file-path>/ObjectManager.log`.
5. Actualice el tipo de visualización de los campos que se convirtieron en campos de lanzador de URL.

   1. Inicie sesión en OpenPages como usuario con privilegios administrativos.
   2. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** >**Configuración de la solución** >**Tipos de objeto**.
   3. Pulse el tipo de objeto **Auditoría** .
   4. En el campo `OPSS-Aud` , agrupe, actualice los campos siguientes para utilizar el tipo de visualización **Enlace** :

      - Cerrar auditoría
      - Planes
   5. Repita estos pasos para los campos siguientes:

      - RiskEntity: OPSS-RiskEnt: Baselines
      - Resource: OPSS-Res: Resource Links
6. Utilice FastMap para cargar los cambios de objeto de preferencia:

   1. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **FastMap Importar**.
   2. Pulse **Elegir archivo** y seleccione el archivo `IAM_computed_field_preference_updates.xls` .
   3. Pulse **Importar datos**.
   4. Revise el informe de verificación y, a continuación, pulse **Importar datos**.

###### Qué hacer a continuación

Siga los pasos descritos en [Sustitución de campos calculados por campos de lanzador de URL (RCSA)](#sustitución-de-campos-calculados-por-campos-de-lanzamiento-de-url-rcsa).

##### Sustitución de campos calculados por campos de lanzamiento de URL (RCSA)

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización › Tareas posteriores a la actualización para las soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=puts-replacing-computed-fields-url-launcher-fields-rcsa)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Los ayudantes de RCSA han utilizado campos calculados en releases anteriores. Puede cambiar los campos a campos URL en lugar de campos computados. Los campos se sustituyen por campos nuevos que utilizan los mismos nombres.

###### Acerca de esta tarea

Esta tarea sustituye los siguientes campos calculados por campos URL :

- Risk Assessment: OPSS-RA: RCSA Completion Helper
- Risk Assessment: OPSS-RA: RCSA Process Alignment Helper

Si desea revisar los cambios antes de implementarlos, consulte el archivo que se lista en el paso 1.

> **Nota:** Estos pasos utilizan Gestor de objetos, pero puede utilizar **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Migración del sistema** > **Importar configuración** para importar el archivo `ORM_computed_field_url_field_replacement-op-config.xml`. Para obtener más información, consulte [Importación de un archivo de migración](3.5-guia-del-administrador.md#importación-de-un-archivo-de-migración).

###### Procedimiento

1. Copie el archivo siguiente del soporte de instalación de 9.0 en el servidor de aplicaciones. O, si ejecuta ObjectManager desde un sistema remoto, como el portátil, copie los archivos en el sistema remoto.

   `/OP_<version>_Main/OP_<version>_Configuration/Modules/ORM/ORM_computed_field_url_field_replacement-op-config.xml`
2. Abra una línea de mandatos.

   Si utiliza Microsoft Windows, abra un indicador de mandatos con la opción **Ejecutar como administrador** .
3. Vaya al directorio `<OP_HOME>/bin` .

   O, si está ejecutando ObjectManager desde un sistema remoto, vaya al directorio `openpages-tools-client/bin` .
4. Ejecute el mandato siguiente para cargar los campos actualizados.

   Sustituya `<loader-file-path>` por la ubicación del archivo `ORM_computed_field_url_field_replacement-op-config.XML`

   ```bat
   ObjectManager.cmd|sh l c <OpenPages Administrator user> <OpenPages Administrator password> <loader-file-path> ORM_computed_field_url_field_replacement
   ```

   Si encuentra algún error, revise el archivo de registro, `<loader-file-path>/ObjectManager.log`.

###### Qué hacer a continuación

Si aún no lo ha hecho, siga los pasos descritos en [Sustitución de campos calculados por cálculos y campos de lanzador de URL (IAM e ITG)](#sustitución-de-campos-calculados-por-cálculos-y-campos-de-lanzador-de-url-iam-e-itg).

##### Importación del paquete de informes de soluciones

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización › Tareas posteriores a la actualización para las soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=puts-importing-solutions-report-package)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si ha actualizado o migrado, importe los informes de soluciones para actualizarlos.

Para obtener más información sobre la importación de contenido, consulte la publicación *IBM Cognos Analytics Guía de administración y seguridad*.

###### Procedimiento

1. Haga una copia de seguridad de los archivos siguientes si existen:.

   - `<COGNOS_HOME>/deployment/OpenPages_Solutions.zip`
   - `<COGNOS_HOME>/deployment/OpenPages_Solutions_V6.zip`
2. Localice el directorio de la base de datos que está utilizando:

   - IBM® Db2®: `OP_<version>_Main/OP_<version>_Configuration/Platform/Upgrade/DB2/`
   - Oracle: `OP_<version>_Main/OP_<version>_Configuration/Platform/Upgrade/Oracle/`
3. Obtenga la versión más reciente del paquete de informes de soluciones.

   - Si ha actualizado o migrado desde 8.2, copie `OpenPages_Solutions_V6.zip`
   - Si ha actualizado o migrado desde 8.3 o posterior, copie `OpenPages_Solutions_Reports.zip`
4. Copie el archivo en el directorio siguiente en el servidor de Cognos® : `<COGNOS_HOME>/deployment`. Sobrescriba el archivo existente.
5. Desde un navegador, inicie sesión en IBM Cognos Analytics.

   De forma predeterminada, el URL es `http://<hostname>:<port>/ibmcognos/bi`

   Donde `<hostname>` es el nombre del servidor Cognos y `<port>` es el número de puerto de pasarela Cognos (80 de forma predeterminada).
6. Pulse **Gestionar** > **Consola de administración** para abrir la página **IBM Cognos Administration** .
7. Pulse la pestaña **Configuración** y pulse **Administración de contenido**.

   > **Sugerencia:** Para acceder a esta área en IBM Cognos Administration, debe tener los permisos necesarios para la característica protegida **Administración** .
8. En la barra de herramientas, pulse **Nueva importación**.
9. En la lista **Archivo de implementación**, seleccione **OpenPages_Solutions_Reports**.
10. Pulse **Siguiente**.
11. Escriba un nombre exclusivo, una descripción opcional y una sugerencia para el archivo de despliegue, seleccione la carpeta donde desea guardarlo y, a continuación, pulse **Siguiente**.
12. En el recuadro **Contenido de carpetas públicas, directorio y biblioteca** , seleccione **OpenPages Informes de soluciones**y, a continuación, pulse **Siguiente**.
13. En la página **Especificar las opciones generales** , acepte las opciones predeterminadas y pulse **Siguiente**.
14. En la página **Revisar el resumen** , revise los valores y pulse **Siguiente**.
15. En la página **Seleccionar una acción**, pulse **Finalizar**.
16. Pulse **Sustituir la entrada existente**y, a continuación, pulse **Aceptar**.
17. En la página **Ejecutar con opciones** , pulse **Ejecutar**.
18. En la página **IBM Cognos software** , pulse **Aceptar**.
19. Para ver los paquetes e informes importados, pulse el icono **Inicio** y seleccione la carpeta donde los ha importado.

###### Qué hacer a continuación

Si ha actualizado o migrado desde 8.2, actualice los informes para utilizar el JavaScriptactualizado. para enlaces CrossTrack. (Si ha actualizado o migrado desde 8.3, no es necesario actualizar los enlaces CrossTrack .)

Para obtener más información, consulte los siguientes temas:

- [Adición de enlaces CrossTrack a informes autónomos y padres](10-guia-del-creador-de-informes.md#adición-de-enlaces-crosstrack-a-informes-autónomos-y-padres)
- [Adición de enlaces CrossTrack a informes de acceso a detalles](10-guia-del-creador-de-informes.md#adición-de-enlaces-crosstrack-a-informes-de-acceso-a-detalles)

#### Actualización de campos calculados personalizados

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-updating-custom-computed-fields)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si tiene campos calculados personalizados que generan HTML que contiene JavaScript, sustitúyalos por campos de lanzador de URL.

Para obtener información sobre los campos del lanzador URL, consulte [Añadir un campo lanzador URL](3.2-guia-del-administrador.md#adición-de-un-campo-de-iniciador-de-url).

Por ejemplo, en releases anteriores a 9.0, el campo calculado Ayudante de alineación de RCSA generaba el siguiente HTML:

```xml
<a href="#" onclick="openReport(report.tree.post.do?label=Current+Reporting+Period&mainNavReport=true&amp;submitAction=preview&amp;actionContext=preview&reportId=2196&resourceId=11574leftPos=0&amp;topPos=0')">RCSA Alignment Helper</a>
```

En la 9.0 y posteriores, el reemplazo es un campo de Lanzador de URL con el siguiente valor por defecto:

```
${ 
	"labelKey": "orm.rcsa.alignment.helper.url", 
	"path": "/report.tree.post.do",
	"parameters": {
		"reportPath": "/_cw_channels/Reporting/Hidden Reports/ORM Custom Reports/RCSA Process Alignment Helper.pagespec",
		"reportingPeriodId": "$reportingPeriodId", 
		"resourceId":"$objectId" 
	}, 
	"popUp" : { 
		"windowAttributes" : "height=600,width=800,menubar=no,status=yes,toolbar=no,scrollbars=yes,resizable=yes" 
	}
}
```

Si algunos de los argumentos de URL generados por el campo calculado fueron calculados, puede reemplazarlos creando Cálculos GRC y luego haciendo referencia a esos campos de salida en la configuración del lanzador de URL. Consulte [Configuración de cálculos GRC](3.3-guia-del-administrador.md#configuración-de-grc-calculations).

#### Actualización del esquema de elaboración de informes

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-updating-reporting-schema)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Actualice el esquema de elaboración de informes.

##### Antes de empezar

Asegúrese de que no se estén ejecutando informes, copias de seguridad u otros trabajos. No ejecute ningún informe, copia de seguridad u otros trabajos durante el proceso de actualización del esquema.

##### Acerca de esta tarea

Cuando actualiza el esquema de informes, todos los índices personalizados que haya definido previamente se recrean automáticamente utilizando la última definición que se encuentra en la configuración de registro adecuada. Esta función está habilitada de forma predeterminada, pero se puede inhabilitar. Para obtener más información sobre los valores para crear índices, consulte  [Valores de la carpeta Esquema de elaboración de informes](3.3-guia-del-administrador.md#valores-de-la-carpeta-esquema-de-elaboración-de-informes).

##### Procedimiento

1. Inicie sesión en OpenPages® como usuario con privilegios administrativos.
2. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** >**Activar el modo Administración del sistema**.
3. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Esquema de informes**.
4. Pulse **Actualizar**.
5. Pulse **Renovar** hasta que el proceso se haya completado al 100%.
6. Inhabilite SAM. Haga clic en **Abrir menú de administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Desactivar el modo de administración del sistema**.

#### Regeneración del entorno de elaboración de informes

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-regenerating-reporting-framework)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Después de actualizar IBM OpenPages®, es posible que tenga que volver a generar el entorno de elaboración de informes.

La versión 9.0 añade una serie de campos de sistema y tipos de objeto nuevos. Si tiene previsto utilizar las nuevas prestaciones y desea poder acceder a los nuevos campos y tipos de objeto en los informes, vuelva a generar el entorno de elaboración de informes.

También debe volver a generar el entorno de elaboración de informes si alguno de los casos siguientes se aplica en su caso:

- Utiliza más de una URL para acceder a OpenPages. Al volver a generar el entorno, seleccione **Modelo de entorno**, **Asuntos de consulta personalizada** y **Todos los modelos**.
- Ha añadido nuevos campos y desea utilizar los campos nuevos en informes.

Vuelva a generar el entorno de elaboración de informes después de completar todas las tareas de instalación y actualización.

Para obtener más información, consulte [Generación del entorno de elaboración de informes](3.5-guia-del-administrador.md#generación-del-entorno-de-elaboración-de-informes).

#### Actualización de vistas de detalles a vistas de administración

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-upgrading-detail-views-admin-views)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si está actualizando o migrando desde 8.2, puede actualizar las vistas de detalles a las vistas de administración.

Para obtener más información sobre las vistas de administración, consulte [Vistas de administración](3.6-guia-del-administrador.md#vistas-de-administrador).

##### Procedimiento

1. Haz clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Vistas**.
2. Pulse **Generar vistas de administración**. Se visualiza un recuadro de diálogo que explica cómo utilizar la característica. Siga las instrucciones del recuadro de diálogo para actualizar las vistas de detalles.

   *Figura 1. Recuadro de diálogo Generar vistas de administración*

   ![Recuadro de diálogo Generar vistas de administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/generate_admin_views.png)

#### Utilización de vistas de creación personalizadas con la aplicación Loss Event Entry

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-using-custom-creation-views-loss-event-entry-application)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

En releases anteriores a OpenPages® 8.3, la selección y el orden de los campos de la aplicación Loss Event Entry se controlaban mediante las vistas de creación que se especificaban en la herramienta de configuración de Loss Event Entry. En OpenPages 8.3, las vistas se eligen ahora utilizando las reglas y las prioridades de la vista en lugar de utilizar las vistas que se especifican explícitamente. Las vistas de creación listas para usar son `SysView-New-LossEvent-LEE`, `SysView-New-LossImpact-LEE` y `SysView-New-LossRecovery-LEE`. Todas ellas tienen reglas de visualización que hacen se apliquen solo a los usuarios que utilizan el perfil de Loss Event Entry. Estas vistas se han creado basándose en las versiones anteriores de las vistas de creación listas para usar.

Si ha personalizado las vistas de creación utilizadas para la aplicación Loss Event Entry, puede volver a crear las vistas personalizadas copiando las vistas existentes y, a continuación, aplicando las personalizaciones a las copias. Asegúrese de utilizar una regla de vista para que la vista que cree solo se aplique al perfil de Loss Event Entry.

#### Cambios y mejoras en la configuración

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-configuration-changes-enhancements)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Revise la siguiente lista de cambios y nuevas características. Estos cambios pueden afectar a la configuración.

##### Actualizaciones importantes en 9.0

Revise los cambios siguientes.

- **Utilizar la migración del sistema para exportar e importar plantillas de cuestionario**

  En OpenPages® versión 9.0.0.2 y posteriores, no utilice Fastmap para importar o exportar plantillas de cuestionario. Sin embargo, puede importar plantillas de cuestionario que ha exportado de una versión anterior.

  Para exportar plantillas de cuestionario, utilice **Migración del sistema > Configuración de exportación**. Para obtener más información, consulte [Exportación de elementos de configuración desde el entorno de origen](3.5-guia-del-administrador.md#exportación-de-elementos-de-configuración-desde-el-entorno-de-origen).

  Para importar plantillas de cuestionarios, utilice **Migración del sistema > Importar configuración**. Para obtener más información, consulte [Importación de elementos de configuración al entorno de destino](3.5-guia-del-administrador.md#importación-de-los-elementos-de-configuración-al-entorno-de-destino).

- **Permisos de aplicación**

  El permiso de aplicación **Motor de reglas** ahora da acceso al elemento de menú **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Normas de los actos reglamentarios**.

- **FastMap sólo da soporte a `.xlsx`**

  En la versión 9.0, FastMap sólo da soporte a archivos `.xlsx` . El formato `.xls` ya no está soportado.

  - La plantilla de exportación predeterminada está ahora en formato `.xlsx` . El archivo `.xls` existente no se elimina pero ya no se utiliza.

    Si ha personalizado `DefaultTemplate.xls`, descárguelo, vuelva a guardarlo como un archivo `.xlsx` utilizando Microsoft Excel y, a continuación, cargue el archivo `DefaultTemplate.xlsx` .

    > **Nota:** El nombre de archivo debe ser `DefaultTemplate.xlsx`.
  - Si utiliza plantillas de exportación específicas de objeto, actualícelas al formato `.xlsx` . Descárguelos, vuelva a guardarlos como archivos `.xlsx` utilizando Microsoft Excel y, a continuación, cárguelos.

    Si una plantilla específica de objeto está en formato `.xls` , se utiliza `DefaultTemplate.xlsx` .
  - Los archivos de importación de FastMap deben estar en formato `.xlsx` . Si necesita importar un archivo de un entorno más antiguo, guarde el archivo como `.xlsx`y, a continuación, impórtelo.
  - El formato `.xlsx` da soporte a un mayor número de columnas y filas. Para obtener más información, consulte la documentación de Microsoft Excel.

  > **Nota:** Se espera que el rendimiento sea más lento con los archivos `.xlsx` debido a las características del formato de archivo `.xlsx` . Este problema de rendimiento no es específico de OpenPages.

- **Nuevo título del sistema, campo**

  El nuevo campo Título del sistema proporciona opciones adicionales que los administradores pueden utilizar para hacer referencia a objetos. Antes de la versión 9.0, los administradores se proporcionaban con una sola opción: el campo Nombre (`System Fields:Name`).

  Si desea utilizar el nuevo campo Título para un tipo de objeto, establezca **Habilitar componente de título** en **True** para el tipo de objeto. Esta opción controla cómo se visualizan las referencias a un objeto.

  Si **Habilitar componente de título** se establece en **False** (que es el valor predeterminado para la actualización o migración de clientes), no experimentará ningún cambio en el comportamiento del campo Nombre del sistema.

  Puede utilizar un script para rellenar el campo Título con contenido de un campo existente. Para obtener más información, consulte [Rellenar el campo Título del sistema después de actualizar o migrar](#rellenar-el-campo-título-del-sistema-después-de-actualizar-o-migrar).

- **El filtrado de campos que tienen reglas de seguridad a nivel de campo ahora está inhabilitado de forma predeterminada**

  De forma predeterminada, los campos con reglas FLS no están disponibles para los usuarios para el filtrado.

  Permitir que los usuarios filtren en campos con reglas FLS puede tener un impacto significativo en el rendimiento porque las reglas deben evaluarse en cada registro que se está filtrando. OpenPages ahora impide a los usuarios filtrar por campos FLS. Si los usuarios tienen filtros existentes que utilizan campos FLS, se visualiza una notificación que indica que no se permite el filtrado en campos FLS.

  Puede volver al comportamiento anterior, pero tenga en cuenta las implicaciones en el rendimiento. Para obtener más información, consulte [Habilitación e inhabilitación del filtrado en campos FLS](3.3-guia-del-administrador.md#habilitar-o-inhabilitar-el-filtrado-en-campos-con-reglas-fls).

- **Configuración de entrada de evento de pérdida**

  La herramienta de configuración de eventos de pérdida ahora forma parte de OpenPages. Haga clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Integraciones** > **Aplicación de registro de siniestros** para configurar la entrada de eventos de pérdida.

- **NPS**

  En instalaciones nuevas, NPS está ahora habilitado de forma predeterminada. Además, si actualiza a 9.0 desde una versión anterior a la que NPS está disponible, NPS está habilitado de forma predeterminada.

  Si migra a 9.0, los valores de NPS del entorno de origen se conservan.

  Para obtener más información, consulte [Configuración de una encuesta Net Promoter Score (NPS)](3.2-guia-del-administrador.md#configuración-de-una-encuesta-net-promoter-score).

##### Actualización o migración desde 8.2.x

Si el entorno de origen estaba en la versión 8.2.x, revise también los cambios siguientes.

- **Permisos de aplicación**

  **Tabla 1. Permisos de aplicación añadidos o modificados en 8.3**

  | Característica | Permisos de aplicación |
  | --- | --- |
  | Visualice los registros de la aplicación mediante el elemento de menú **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Otros** > **Registros**. | **Todos los permisos** > **SOX** > **Administración** > **Registros** |
  | Configure los clasificadores mediante el elemento de menú **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Integraciones** > **Sugerencias sobre cartografía y taxonomía**. | **Todos los permisos** > **SOX** > **Administración** > **Watson** |
  | Vea los procesos en segundo plano mediante el elemento de menú **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_db2/settings_menu_icon_task_focused_ui.jpg)** > **Otros** > **Procesos de fondo**. | El permiso de aplicación **Todos los permisos** > **API** > **Administración** > **Proceso en segundo plano** > **Obtener información de proceso** ahora también proporciona acceso al elemento de menú **Procesos en segundo plano** |
  | Publique informes en IBM® Cognos® Analytics y gestione páginas y plantillas de informe. | **Todos los permisos** > **Publicación** |

- **Desencadenantes y ayudantes personalizados**

  Si utiliza `/OpenPages/Solutions/PCM/Attestation/Email Sender Name` o `/OpenPages/Solutions/PCM/Attestation/Email Sender Address` en cualquiera de sus códigos personalizados, estos valores se eliminarán en un release futuro. Para asegurarse de que el código sigue funcionando, realice los pasos siguientes:

  1. Modifique su código sustituyendo `/OpenPages/Solutions/PCM/Attestation/Email Sender Name` por `/Applications/Common/Email/Mail From Name` y `/OpenPages/Solutions/PCM/Attestation/Email Sender Address` por `/Applications/Common/Email/Mail From Address`.
  2. Asegúrese de que `/Applications/Common/Email/Mail From Name` y `/Applications/Common/Email/Mail From Address` se han establecido correctamente para las notificaciones de correo electrónico.

  Si tiene desencadenantes personalizados, si utilizan el atributo `from.address` y ese atributo está vacío o tiene un valor de `donotreply@openpages.com`, el valor se sustituye por el valor del valor de registro `/Applications/Common/Email/Mail From Address`.

##### Rellenar el campo Título del sistema después de actualizar o migrar

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas posteriores a la actualización › Cambios y mejoras en la configuración` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=cce-populating-system-title-field-after-upgrading-migrating)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

La versión 9.0 introduce un nuevo campo de sistema opcional denominado Título (`System Fields:Title`). El campo es un componente de nombres de tipo de objeto y está diseñado para almacenar los nombres fáciles de usar de las instancias de objeto.

###### En segundo plano

Anteriormente, el campo Nombre sólo almacenaba los nombres de los objetos. Puesto que los nombres deben ser exclusivos dentro de una vía de acceso de carpeta, a menudo se ha utilizado otro campo, como por ejemplo Descripción, para proporcionar un nombre fácil de usar para los objetos.

En 9.0 y posteriores, el campo Nombre tiene componentes separados para almacenar el nombre (ID) y el título de los objetos: **Name.ID** (`System Fields:Name`) y **Name.Title** (`System Fields:Title`). Puede especificar qué componentes se deben visualizar en las vistas y otras áreas de la aplicación. Por ejemplo, puede utilizar el campo Título en una vista de tarea. O puede visualizar el ID y el título.

Para ayudarle a aprovechar el nuevo campo Título, OpenPages® incluye un script que puede utilizar para rellenar el campo Título con el contenido de otro campo.

Para obtener más información, consulte [Rellenar el campo Título del sistema](3.2-guia-del-administrador.md#llenado-del-componente-título-de-los-objetos).

> **Nota:** Esta tarea es opcional.

### Tareas adicionales para actualizaciones

`Guía de actualización para Db2 (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrading-additional-tasks-upgrades)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Es posible que desee completar tareas adicionales para una actualización de OpenPages® .

#### Realización de una actualización silenciosa

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas adicionales para actualizaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrades-performing-silent-upgrade)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede actualizar desde la línea de mandatos.

##### Antes de empezar

Lleve a cabo las siguientes tareas de preparación:

- [Revisión de las características y arreglos nuevos](#revisión-de-las-características-y-arreglos-nuevos)
- [Copia de seguridad del entorno](#copia-de-seguridad-del-entorno)
- [Actualizar software de requisito previo](#actualizar-software-de-requisito-previo)
- [Verificación de los servidores antes de la actualización](#verificación-de-los-servidores-antes-de-la-actualización)
- [Actualizar la base de datos OpenPages (Db2)](#actualice-la-base-de-datos-openpages-db2)
- [Preparación del servidor de instalación](#preparación-del-servidor-de-instalación)
- Si ha instalado manualmente el software de agente en servidores remotos, asegúrese de que el software de agente se haya actualizado y que los agentes estén en ejecución.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de instalación como usuario que ha instalado el servidor de instalación.

   De forma alternativa, puede iniciar sesión como cualquier usuario que tenga permisos completos en los directorios del servidor de instalación y que pueda ejecutar `Node.js`.
2. Vaya al directorio `<Installation_server_home>/src/deployment/<deployment name>` .
3. Edite el archivo `deploy.properties` .

   1. Cambie el valor de la propiedad `task` a `upgrade`.
   2. Cambie el valor de la propiedad `maintenance_version` a `9.0`.
   3. Actualice el valor de la propiedad `install_db` . Establézcalo en `done`.

      Para obtener más información, consulte [Propiedades del archivo de despliegue](5.2-guia-de-instalacion-y-despliegue-solo-local.md#propiedades-del-archivo-de-despliegue).
   4. Guarde el archivo y ciérrelo.
4. Ejecute la instalación silenciosa desde la línea de mandatos.

   1. Abra un indicador de mandatos o abra una ventana de shell como administrador.
   2. Vaya al directorio `<Installation_server_home>` .
   3. Ejecute el mandato siguiente:

      ```
      npm run silent <deployment name> acceptLicense
      ```

      > **Nota:** No cierre el indicador de mandatos o la ventana de shell hasta que finalice el proceso.
5. Compruebe los registros para asegurarse de que la instalación se ha realizado correctamente.

#### Retrotracción de una actualización

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas adicionales para actualizaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrades-rolling-back-upgrade)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si ha realizado una copia de seguridad de su entorno antes de actualizar, puede retrotraer la actualización.

##### Antes de empezar

Para retrotraer una actualización, necesita los siguientes archivos de copia de seguridad:

- Los directorios de copia de seguridad que ha creado antes de actualizar.
- La copia de seguridad del directorio `openpages-storage` que ha creado antes de actualizar.
- La copia de seguridad de base de datos que ha creado antes de actualizar.
- Cualquier otro archivo de copia de seguridad que haya creado antes de la actualización, como por ejemplo informes personalizados, JSP, etc.

También necesita las versiones del software de soporte, como por ejemplo IBM® Cognos® Analytics, que ha utilizado antes de la actualización.

##### Acerca de esta tarea

El procedimiento siguiente se aplica a actualizaciones in situ, no a actualizaciones con migración.

En estos pasos, los directorios de copia de seguridad utilizan el nombre `OpenPages8001Backup`. Especifique el nombre que ha elegido al crear los directorios de copia de seguridad.

##### Procedimiento

1. Detenga todos los servidores:

   - Servidores de aplicaciones OpenPages® (admin y no admin)
   - Servidores IBM Cognos (activos y en espera)
   - OpenPages servidor de búsqueda

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
2. Para servidores de aplicaciones:

   1. Si utiliza Microsoft Windows, suprima los servicios de Windows para OpenPages.
   2. Si está utilizando miembros de clúster vertical, ejecute el siguiente mandato en cada uno de ellos:

      ```
      sc delete <server name> 
      ```
   3. Restaure los directorios de copia de seguridad que se crearon antes de la actualización.
3. Para el servidor de base de datos:

   1. Si se ha actualizado el software de base de datos, restablezca la versión anterior del software de base de datos.
   2. Restaure la base de datos utilizando la copia de seguridad de base de datos que se ha creado antes de la actualización.
4. Para todos los demás servidores, restaure los directorios de copia de seguridad que se crearon antes de la actualización.

   Después de que se hayan restaurado todos los servidores y todos los productos de terceros estén en las versiones necesarias para el despliegue anterior de OpenPages , el despliegue anterior de OpenPages funciona sin más acciones.
5. Restaure la copia de seguridad del directorio `openpages-storage` que ha creado antes de la actualización.
6. Restaure todos los demás archivos de copia de seguridad que ha creado antes de la actualización, como informes personalizados, JSP, etc.
7. Inicie todos los servidores:

   - OpenPages servidores de aplicaciones
   - servidores IBM Cognos
   - OpenPages servidor de búsqueda

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).

#### Carga manual de los datos de configuración de una actualización

`Guía de actualización para Db2 (solo en local) › Actualización › Tareas adicionales para actualizaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrades-manually-loading-configuration-data-upgrade)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Al actualizar IBM OpenPages® a la versión 9.0, IBM OpenPages carga automáticamente los datos de aplicación y habilita el acceso de usuario a los informes estándar de IBM® Cognos® Analytics . En situaciones limitadas, puede actualizar manualmente los datos de configuración del cargador.

##### Antes de empezar

IBM OpenPages debe estar instalado.

Los servicios de OpenPages deben estar en ejecución.

##### Acerca de esta tarea

Si los archivos del cargador de actualización que se ejecutan durante la actualización tienen errores, puede corregir los problemas que han provocado los errores y, después, ejecutar los archivos del cargador de actualización manualmente.

##### Procedimiento

1. Inicie sesión en el servidor de aplicaciones de administración de OpenPages como usuario con privilegios administrativos.
2. Vaya al directorio `<OP_HOME>/installer/maintenance/upgrade-9.0/addon_module/loaderdata` .
3. Haga una copia de seguridad del archivo `schema_loader_properties.sh|.bat` .
4. Abra el archivo `schema_loader_properties` original en un editor de texto.
5. En la línea siguiente, actualice la contraseña del superadministrador de OpenPages para borrar el texto.

   ```
   SET OPXUserName=<Super_Administrator_user_name>
   SET OPXUserPassword=********
   ```

   El nombre de usuario predeterminado es `OpenPagesAdministrator`.

   La contraseña del usuario `OPXUserName` está enmascarada por asteriscos (***). Sustituya la máscara por texto simple.
6. Guarde el archivo y ciérrelo.
7. Vaya al directorio `<OP_HOME>/bin` .
8. Edite el archivo `ObjectManager.properties` y actualice los valores siguientes tal como se muestra:

   ```properties
   configuration.manager.vendor.mode=true
   configuration.manager.force.update.object.strings=false
   configuration.manager.force.update.application.strings=false
   configuration.manager.disable.triggers=true
   ```
9. Guarde el archivo y ciérrelo.
10. En función de la ruta de actualización, ejecute los scripts en el orden que se indica:

    | Ruta de actualización | Archivos Windows que se deben ejecutar |
    | --- | --- |
    | 8.2.x a 9.0 | • `openpages-op820x-to-830x-loader-data.bat`<br>• `openpages-op830x-to-9000-loader-data.bat`<br>• `op-sysviews-loader.bat` |
    | 8.3.x a 9.0 | • `openpages-op830x-to-9000-loader-data.bat`<br>• `op-sysviews-loader.bat` |

    | Ruta de actualización | Archivos Linux que se deben ejecutar |
    | --- | --- |
    | 8.2.x a 9.0 | • `openpages-op820x-to-8300-loader-data.sh`<br>• `openpages-op830x-to-9000-loader-data.sh`<br>• `op-sysviews-loader.sh` |
    | 8.3.x a 9.0 | • `openpages-op830x-to-9000-loader-data.sh`<br>• `op-sysviews-loader.sh` |
11. Vaya al directorio `<OP_HOME>/bin` .
12. Edite el archivo `ObjectManager.properties` y actualice los valores siguientes tal como se muestra:

    ```properties
    configuration.manager.vendor.mode=false
    configuration.manager.disable.triggers=false
    ```
13. Guarde el archivo y ciérrelo.
14. Vaya al directorio `<OP_HOME>/installer/maintenance/upgrade-9.0/addon_module/loaderdata` .
15. Abra el archivo `schema_loader_properties` en un editor de texto.
16. En la línea siguiente, oculte la contraseña de texto simple para el superadministrador de OpenPages cambiándola por asteriscos (***).

    ```
    SET OPXUserPassword=********
    ```
17. Guarde el archivo y ciérrelo.
18. Reinicie los servicios de OpenPages .

## Avisos

`Guía de actualización para Db2 (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ugdpo-notices)

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
