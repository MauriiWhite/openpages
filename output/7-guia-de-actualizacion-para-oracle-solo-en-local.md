---
product: IBM OpenPages 9.0.0
product_key: SSFUEU_9.0.0
file: 7
guide: Guía de actualización para Oracle (solo en local)
covers: Guía de actualización para Oracle (solo en local) — Avisos
chapters: 6
topics: 65
words: 20894
tasks: 38
concepts: 25
references: 1
tables: 6
code_blocks: 63
figures: 17
applies_to: De forma local
updated: 2025-04-02
lang: es
source: https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrade-guide-oracle-prem-only
extracted: 2026-09-11
---

# 7 · Guía de actualización para Oracle (solo en local)

> **Qué hay en este archivo.** «Guía de actualización para Oracle (solo en local)» de IBM OpenPages 9.0.0, completa: 6 capítulos. 65 temas, 38 de ellos procedimientos paso a paso, 6 tablas, 63 bloques de código, 17 figuras y 20.894 palabras.
>
> **Capítulos:** Guía de actualización para Oracle (solo en local) · Cómo empezar · Determinar la ruta de actualización · Preparación de la actualización · Actualizar OpenPages · Avisos.
>
> **Se aplica a:** De forma local.
>
> **Si lo que buscas no está acá.** El índice de los 2.511 temas del producto, con su archivo y su ancla, está en `index.md`.

**Términos propios de este archivo:** agente, remoto, situ, sysdba, fixpack, argumento, despliegues, lanzador, alrededor, crosstrack, restaure, migrando, antivirus, opss.

## Índice de este archivo

- [Guía de actualización para Oracle (solo en local)](#guía-de-actualización-para-oracle-solo-en-local)
- [Cómo empezar](#cómo-empezar)
  - [Ubicaciones de instalación](#ubicaciones-de-instalación)
  - [Cambios realizados en el proceso de instalación](#cambios-realizados-en-el-proceso-de-instalación)
  - [Caracteres especiales en las contraseñas](#caracteres-especiales-en-las-contraseñas)
- [Determinar la ruta de actualización](#determinar-la-ruta-de-actualización)
- [Preparación de la actualización](#preparación-de-la-actualización)
  - [Revisión de las características y arreglos nuevos](#revisión-de-las-características-y-arreglos-nuevos)
  - [Copia de seguridad del entorno](#copia-de-seguridad-del-entorno)
    - [Copia de seguridad de la base de datos OpenPages (Oracle)](#copia-de-seguridad-de-la-base-de-datos-openpages-oracle)
    - [Copia de seguridad del almacén de contenido de Cognos (Oracle)](#copia-de-seguridad-del-almacén-de-contenido-de-cognos-oracle)
    - [Copia de seguridad de asistentes de soluciones, imágenes y otros archivos](#copia-de-seguridad-de-asistentes-de-soluciones-imágenes-y-otros-archivos)
  - [Actualizar software de requisito previo](#actualizar-software-de-requisito-previo)
    - [Opciones de actualización de Oracle y Oracle PDB](#opciones-de-actualización-de-oracle-y-oracle-pdb)
      - [Actualización de Oracle a 19c (in situ)](#actualización-de-oracle-a-19c-in-situ)
      - [Actualización de Oracle a 19c (migración)](#actualización-de-oracle-a-19c-migración)
    - [Actualización de Cognos](#actualización-de-cognos)
    - [Obtención de una copia del SDK de IBM (Windows)](#obtención-de-una-copia-del-sdk-de-ibm-windows)
    - [Obtención de una copia de IBM SDK (Linux®)](#obtención-de-una-copia-de-ibm-sdk-linux)
  - [Verificación de los servidores antes de la actualización](#verificación-de-los-servidores-antes-de-la-actualización)
- [Actualizar OpenPages](#actualizar-openpages)
  - [Actualizar la base de datos de OpenPages (Oracle)](#actualizar-la-base-de-datos-de-openpages-oracle)
    - [Preparación de la base de datos de Oracle](#preparación-de-la-base-de-datos-de-oracle)
    - [Preparación de los scripts de actualización de la base de datos (Oracle)](#preparación-de-los-scripts-de-actualización-de-la-base-de-datos-oracle)
      - [Ejecución de scripts personalizados durante la actualización de base de datos (Oracle)](#ejecución-de-scripts-personalizados-durante-la-actualización-de-base-de-datos-oracle)
    - [Ejecución del script de DBA previo a la actualización (Oracle)](#ejecución-del-script-de-dba-previo-a-la-actualización-oracle)
    - [Validación del paso de DBA previo a la actualización (Oracle)](#validación-del-paso-de-dba-previo-a-la-actualización-oracle)
    - [Actualización del esquema (Oracle)](#actualización-del-esquema-oracle)
    - [Ejecución del script de DBA posterior a la actualización (Oracle)](#ejecución-del-script-de-dba-posterior-a-la-actualización-oracle)
    - [Validación del paso de DBA posterior a la actualización (Oracle)](#validación-del-paso-de-dba-posterior-a-la-actualización-oracle)
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


# Guía de actualización para Oracle (solo en local)

`Guía de actualización para Oracle (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrade-guide-oracle-prem-only)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Esta guía proporciona instrucciones para actualizar los despliegues de OpenPages® que utilizan Oracle.

Utilice esta guía si está actualizando OpenPages in situ. Si está migrando o realizando una instalación nueva, consulte la publicación *IBM OpenPages Guía de instalación y despliegue*.

## IBM OpenPages documentación

IBM® mantiene un conjunto de servicios de documentación IBM OpenPages, IBM OpenPages for IBM Cloud Pak for Datay IBM OpenPages on Cloud despliegues. La documentación de IBM OpenPages describe determinadas características y funciones que pueden no estar disponibles en la nube.

Si tiene alguna pregunta sobre la funcionalidad disponible en la versión del producto que está utilizando, póngase en contacto con el soporte deIBM utilizando el [portal de soporte de IBM](https://www.ibm.com/mysupport).

## Funciones de accesibilidad

Las características de accesibilidad ayudan a los usuarios que tienen alguna discapacidad física, por ejemplo movilidad restringida o visión limitada, a utilizar productos de tecnología de la información. La documentación de OpenPages tiene características de accesibilidad. Los documentos PDF son complementarios y no incluyen características de accesibilidad.

## Cómo empezar

`Guía de actualización para Oracle (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ugopo-getting-started)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Lea esta sección para preparar la actualización de los despliegues de OpenPages®.

### Ubicaciones de instalación

`Guía de actualización para Oracle (solo en local) › Cómo empezar` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=gs-installation-locations-1)

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
| `<ORACLE_HOME>` | Ubicación de la instalación del software de base de datos de Oracle.<br>Por ejemplo:<br>• En Windows:<br>• `C:\app\oracle\product\19.3.0\client_1` (Cliente de administración deOracle ).<br>• `C:\oracle\instantclient_19_9` (Oracle Instant Client).<br>• `C:\app\oracle\product\19.3.0\dbhome_1` (servidor).<br>• En Linux:<br>• `/home/oracle/app/oracle/product/19.3.0/client_1` (Cliente de administración deOracle ).<br>• `/home/oracle/instantclient_19_9` (Oracle Instant Client).<br>• `/home/oracle/app/oracle/product/19.3.0/dbhome_1` (servidor). |
| `<WLP_HOME>` | La ubicación de instalación de IBM® WebSphere® Liberty.<br>Por ejemplo:<br>• En Windows: `<OP_HOME>\wlp`.<br>• En Linux: `<OP_HOME>/wlp`. |
| `<WLP_USER_HOME>` | La ubicación de los archivos de aplicación OpenPages y los archivos de configuración del servidor.<br>Por ejemplo:<br>• En Windows: `<OP_HOME>\wlp-usr`.<br>• En Linux: `<OP_HOME>/wlp-usr`. |
| `<COGNOS_HOME>` | La ubicación de instalación de IBM Cognos® Analytics.<br>Por ejemplo:<br>• En Windows: `C:\IBM\cognos\analytics`.<br>• En Linux: `/usr/IBM/cognos/analytics`. |
| `<JAVA_HOME>` | La ubicación de instalación de IBM SDK, Java™ Technology Edition o Java Runtime Environment (JRE).<br>Ejemplo de IBM SDK en un servidor de aplicaciones:<br>• En Windows: `C:\IBM\java_8.0_64`.<br>• En Linux: `/opt/IBM/java_8.0_64`.<br>Ejemplo de JRE en un servidor de informes donde está instalado IBM Cognos Analytics :<br>• En Windows: `C:\IBM\cognos\analytics\ibm-jre\jre`.<br>• En Linux: `/usr/IBM/cognos/analytics/ibm-jre/jre`.<br>Ejemplo de IBM SDK en un servidor de búsqueda:<br>• En Windows: `C:\IBM\java_8.0_64\`.<br>• En Linux: `/opt/IBM/java_8.0_64/`. |
| `<CC_HOME>` | La ubicación de instalación de OpenPages CommandCenter.<br>Por ejemplo:<br>• En Windows: `C:\IBM\OpenPages\CommandCenter`.<br>• En Linux: `/opt/IBM/OpenPages/CommandCenter`. |
| `<SEARCH_HOME>` | Ubicación de instalación de la búsqueda global.<br>El directorio `<SEARCH_HOME>` contiene los archivos `opsearchtools.jar`, Apache Solr y otros archivos de búsqueda global. El directorio de indexación de búsqueda global también se almacena en el directorio `<SEARCH_HOME>`.<br>Por ejemplo:<br>• En Windows: `C:\IBM\OpenPages\OPSearch`.<br>• En Linux: `/opt/IBM/OpenPages/OPSearch`.<br>En la aplicación de instalación, especifique el directorio `<SEARCH_HOME>` en el campo de **directorio de inicio de búsqueda** en la tarjeta de **servidor de búsqueda**. |

### Cambios realizados en el proceso de instalación

`Guía de actualización para Oracle (solo en local) › Cómo empezar` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=gs-changes-installation-process-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si ha instalado versiones anteriores de IBM OpenPages®, observará muchas diferencias. A partir de la versión 8.3, la IU estándar ya no está soportada y se ha eliminado de OpenPages.

Las secciones siguientes describen los cambios principales que afectan a la instalación, actualización y migración.

#### Cambios en el proceso de instalación en 9.0.0.1

Los scripts de actualización de base de datos para fixpacks se encuentran ahora en los directorios siguientes:

- `<fix_pack_kit>/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS`

Para Oracle, tenga en cuenta los cambios siguientes para los fixpacks:

- Los privilegios SYSDBA ya no son necesarios para ejecutar los scripts de actualización de base de datos. En su lugar, debe utilizar un usuario de DBA normal que no tenga privilegios SYSDBA.

#### Cambios en el proceso de instalación en 9.0

Revise los cambios siguientes:

- **Oracle: Cambios en la instalación y actualización de la base de datos**

  La versión 9.0 introduce los cambios siguientes:

  - Debe realizar algunos pasos manuales para configurar la base de datos antes de ejecutar los scripts de base de datos. Estos pasos manuales requieren privilegios SYSDBA.
  - Los privilegios SYSDBA ya no son necesarios para ejecutar los scripts de instalación y actualización de la base de datos. En su lugar, utilice un usuario de DBA normal.
  - El script `init-db-cleanup.sql` tiene un nuevo parámetro: `keepuser`

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
  - La opción **Oracle Text** se ha eliminado de la tarjeta de servidor de base de datos en la aplicación de instalación. El parámetro `oracle_enable_text` del archivo `deploy.properties` ya no se utiliza. En su lugar, habilite Oracle Text manualmente después de instalar OpenPages.

    De forma alternativa, puede utilizar los scripts de base de datos para crear la base de datos y hacer que dichos scripts instalen Oracle Text como parte del proceso de instalación de la base de datos. Sin embargo, para instalar Oracle Text, los scripts de base de datos se deben ejecutar desde el servidor de bases de datos. La instalación de Oracle Text no se puede realizar desde un sistema remoto.

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

`Guía de actualización para Oracle (solo en local) › Cómo empezar` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=gs-special-characters-in-passwords-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede utilizar determinados caracteres especiales en determinadas contraseñas.

Los caracteres especiales que puede utilizar en las contraseñas son:

```
. + - [ ] * ~ _ # : ?
```

> **Nota:** Los espacios no están soportados.

Puede utilizar estos caracteres especiales en las contraseñas de usuario de bases de datos y las cuentas de sistemas operativos de propietarios de esquemas de base de datos.

Si utiliza caracteres especiales en una contraseña, debe entrecomillar la contraseña. Utilice la siguiente sintaxis:

- **Series de conexión de Oracle**

  Para bases de datos Oracle, cuando proporcione una contraseña en una serie de conexión, utilice `\"` alrededor de la contraseña. Por ejemplo:

  ```
  sqlplus sys/\"DB~Password\"@op as dba
  ```

- **Parámetros de script de Oracle SQL*Plus**

  En bases de datos Oracle, cuando proporcione una contraseña en un parámetro de script, utilice la sintaxis siguiente:

  - En Windows, utilice comillas dobles alrededor de la contraseña.

    ```
    sqlplus /nolog @sql-wrapper.sql update-storage c:\temp\upd-storage-output.log op openpages "pass~word" LFS eng11 eng11 Windows c:\OpenPages\openpages-storage
    ```
  - En Linux®, utilice comillas simples alrededor de la contraseña.

    ```
    sqlplus /nolog @sql-wrapper.sql update-storage /home/op/upd-storage-output.log op openpages 'pass~word' LFS  eng11 end11 Unix /usr/opdata/openpages-storage
    ```

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

`Guía de actualización para Oracle (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ugopo-determine-your-upgrade-path)

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

`Guía de actualización para Oracle (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ugopo-prepare-upgrade)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Prepare la actualización de IBM OpenPages®.

> **Nota:** Estos temas sólo se aplican a las actualizaciones in situ. Si está migrando a 9.0, consulte la publicación *IBM OpenPages Guía de instalación y despliegue*. Para obtener más información sobre las vías de acceso de actualización, consulte [Determinar la vía de acceso de actualización](#determinar-la-ruta-de-actualización).

### Revisión de las características y arreglos nuevos

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pu-review-new-features-fixes)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de actualizar OpenPages®, revise las nuevas características y arreglos.

Para obtener más información sobre las nuevas características, consulte la versión más reciente de la [Guía de características nuevas](2-caracteristicas-nuevas.md#características-nuevas) .

Para obtener información adicional sobre OpenPages, consulte la versión más reciente de las [Notas del release](1-notas-del-release.md#notas-del-release) .

Puede encontrar información sobre las correcciones de defectos en la [Lista de arreglos](https://www.ibm.com/support/pages/node/6998091).

Asegúrese de revisar la siguiente información antes de actualizar: [Problemas críticos de instalación y configuración para IBM OpenPages](https://www.ibm.com/support/pages/node/6212189).

### Copia de seguridad del entorno

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pu-backing-up-your-environment)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de actualizar, haga una copia de seguridad de IBM OpenPages®.

#### Acerca de esta tarea

Al realizar una actualización, el servidor de instalación realiza automáticamente una copia de seguridad de la mayoría de los archivos. Sin embargo, es necesario realizar una copia de seguridad manual de algunos de archivos. También es necesario realizar una copia de seguridad de las bases de datos, el directorio `openpages-storage` y los archivos que haya personalizado, como por ejemplo informes y JSP.

#### Procedimiento

1. Pare los servidores de aplicaciones (administrativos y no administrativos), los servidores de informes (activos y en espera), el servidor de bases de datos y el servidor de búsquedas (si utiliza la búsqueda global).
2. Haga una copia de seguridad de la base de datos de OpenPages .

   Para obtener más información, consulte [Copia de seguridad de la base de datos de OpenPages (Oracle)](#copia-de-seguridad-de-la-base-de-datos-openpages-oracle).
3. Haga una copia de seguridad del almacén de contenido de Cognos® .

   Para obtener más información, consulte [Copia de seguridad del almacén de contenido de Cognos (Oracle)](#copia-de-seguridad-del-almacén-de-contenido-de-cognos-oracle).
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

#### Copia de seguridad de la base de datos OpenPages (Oracle)

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Copia de seguridad del entorno` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=environment-backing-up-openpages-database-oracle)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Ejecute el programa de utilidad OPBackup para realizar una copia de seguridad de la base de datos IBM OpenPages® .

##### Acerca de esta tarea

Ejecute el programa de utilidad OPBackup con el parámetro `dbonly`.

> **Nota:**

> Puede hacer copia de seguridad de las bases de datos utilizando otros métodos. Algunos ejemplos de métodos alternativos son:

> - Hacer una copia de seguridad física completa utilizando RMAN
> - Una combinación de copia de seguridad completa e incremental mediante RMAN
> - Hacer una exportación de bomba de datos de Oracle.

> Si desea utilizar un método alternativo, es fundamental que tenga las habilidades necesarias disponibles dentro su organización para completar todos los aspectos de la copia de seguridad y la restauración de la actividad.

Para obtener más información sobre la copia de seguridad del entorno, consulte la publicación *IBM OpenPages Guía del administrador*.

##### Procedimiento

1. Asegúrese de que no haya procesos de OpenPages en ejecución, como trabajos de restablecimiento de objetos.
2. Concluir todos los componentes de OpenPages : servidores de aplicaciones (admin y no admin), servidores de informes (activos y en espera) y el servidor de búsqueda.

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
3. Abra una ventana de mandatos o de shell en el servidor de aplicaciones de administración.
4. Vaya al directorio `<OP_HOME>/aurora/bin` .
5. Realizar una copia de seguridad completa de la base de datos del esquema de OpenPages utilizando OPBackup.

   Windows:

   ```bat
   OPBackup.cmd <backup_directory> dbonly
   ```

   Linux®:

   ```bash
   ./OPBackup.sh <backup_directory> dbonly
   ```

   `<backup_directory>` es la vía de acceso completa a un directorio del servidor de bases de datos. Este directorio es donde se guardan los archivos de registro. Si no se especifica la vía de acceso de archivo, el mandato OPBackup utiliza la ubicación especificada por el parámetro `BACKUP_LOCATION` en el archivo `<OP_HOME>/aurora/bin/op-backup-restore.env`.

   Se crea un archivo de volcado en el directorio `OP_DATAPUMP_DIRECTORY`.

   Para buscar el directorio `OP_DATAPUMP_DIRECTORY`, ejecute el siguiente SQL como usuario de `system`:

   ```sql
   select directory_name, directory_path from dba_directories 
   where directory_name = upper ('OP_DATAPUMP_DIRECTORY');
   ```
6. Examine el registro de copia de seguridad y tome nota del nombre del archivo de volcado. El convenio de denominación es `openpage_<timestamp>.dmp`.

#### Copia de seguridad del almacén de contenido de Cognos (Oracle)

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Copia de seguridad del entorno` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=environment-backing-up-cognos-content-store-oracle)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede utilizar OPCCBackup para realizar una copia de seguridad del almacén de contenido de Cognos® .

##### Acerca de esta tarea

Ejecute el programa de utilidad OPCCBackup con el parámetro `dbonly`.

> **Nota:** Puede realizar una copia de seguridad del almacén de contenido utilizando otros métodos. Algunos ejemplos de métodos alternativos son:

> - Hacer una copia de seguridad física completa utilizando RMAN
> - Una combinación de copia de seguridad completa e incremental mediante RMAN
> - Hacer una exportación de bomba de datos de Oracle.

> Si desea utilizar un método alternativo, es fundamental que tenga las habilidades necesarias disponibles dentro su organización para completar todos los aspectos de la copia de seguridad y la restauración de la actividad.

Para obtener más información sobre la copia de seguridad del entorno, consulte la publicación  [*IBM OpenPages Guía del administrador*](3.4-guia-del-administrador.md#utilización-del-programa-de-utilidad-de-copia-de-seguridad-de-cognos) .

##### Procedimiento

1. Asegúrese de que no haya procesos de OpenPages® en ejecución, como trabajos de restablecimiento de objetos.
2. Concluir todos los componentes de OpenPages : servidores de aplicaciones (admin y no admin), servidores de informes (activos y en espera) y el servidor de búsqueda.

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
3. Asegúrese de que todos los componentes de Cognos estén apagados.
4. Abra una ventana de mandatos o shell en el servidor de aplicaciones de administración en el entorno de origen.
5. Vaya a la página web`<OP_HOME>/CommandCenter/tools/bin`.
6. Realizar una copia de seguridad completa de la base de datos del esquema de Cognos utilizando OPCCBackup.

   Windows:

   ```bat
   OPCCBackup.cmd <backup_directory> dbonly
   ```

   Linux®:

   ```bash
   ./OPCCBackup.sh <backup_directory> dbonly
   ```

   `<backup_directory>` es la vía de acceso completa a un directorio del servidor de bases de datos. Este directorio es donde se guardan los archivos de registro. Si no se especifica la vía de acceso de archivo, el mandato OPCCBackup utiliza la ubicación especificada por el parámetro `OP_CC_BACKUP_HOME` en el archivo `<CC_HOME>/tools/bin/op-cc-backup-restore.env`.

   Se crea un archivo de volcado en el directorio `OP_DATAPUMP_DIRECTORY`. El archivo se llama `openpage_cc_<timestamp>.dmp`.

   Para buscar el directorio `OP_DATAPUMP_DIRECTORY`, ejecute el siguiente SQL como usuario de `system`:

   ```sql
   select directory_name, directory_path from dba_directories 
   where directory_name = upper ('OP_DATAPUMP_DIRECTORY');
   ```

   Si recibe el aviso`tools.jar file is not found`, ver lo siguiente[nota técnica](https://www.ibm.com/support/pages/openpages-opccbackup-command-fails-complete-without-errors-when-backing-oracle-content-store) .

#### Copia de seguridad de asistentes de soluciones, imágenes y otros archivos

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Copia de seguridad del entorno` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=buye-backing-up-solutions-helpers-images-other-files)

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

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pu-upgrade-prerequisite-software)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Antes de actualizar, actualice el software que necesita IBM OpenPages®

Revise los requisitos previos de software para los servidores de aplicaciones, los servidores de informes, el servidor de base de datos y el servidor de búsqueda. Para obtener más información, consulte [Requisitos previos de software](5.1-guia-de-instalacion-y-despliegue-solo-local.md#requisitos-previos-de-software).

- **Obligatorio**

  - Actualice a una versión soportada de Oracle. La versión 19c es la versión soportada para OpenPages 9.0. Consulte las opciones de actualización de [Oracle y Oracle PDB](#opciones-de-actualización-de-oracle-y-oracle-pdb).
  - Actualice IBM® Cognos® Analytics a la versión 11.2.1 o a un release continuo posterior. Puede realizar una actualización in situ, también denominada actualización «“superpuesta”». Consulte [Actualización de Cognos](#actualización-de-cognos).
  - Instale IBM SDK, Java™ Technology Edition en cada servidor de aplicaciones y en el servidor de búsqueda. Para obtener más información, consulte [Obtención de una copia de IBM SDK (Windows)](#obtención-de-una-copia-del-sdk-de-ibm-windows) o [Obtención de una copia de IBM SDK (Linux)](#obtención-de-una-copia-de-ibm-sdk-linux).

- **Opcional**

  - Si desea utilizar Oracle Instant Client, consulte  «“Actualización a 9.0.x”» en [Oracle Instant Client](5.1-guia-de-instalacion-y-despliegue-solo-local.md#oracle-instant-client) .

Además, asegúrese de que los usuarios tienen un navegador soportado.

Si utiliza aplicaciones y componentes opcionales, como IBM OpenPages SDI Connector for UCF Common Controls Hub, puede actualizarlos después de actualizar OpenPages.

#### Opciones de actualización de Oracle y Oracle PDB

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Actualizar software de requisito previo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ups-oracle-upgrade-options-oracle-pdb)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Tiene varias opciones al actualizar IBM OpenPages®.

##### Actualizar Oracle

Debe actualizar Oracle a la versión 19c.

- **Oracle 12.x**

  Si utiliza Oracle 12.2.0.1, debe actualizar a una versión soportada de Oracle antes de actualizar OpenPages. Para obtener información, consulte la publicación *IBM OpenPages Guía de instalación y despliegue*.

- **Oracle 18c**

  Si utiliza Oracle 18c, debe actualizar a una versión soportada de Oracle antes de actualizar.

  Al actualizar Oracle, dispone de dos opciones:

  - Actualizar Oracle in situ. Consulte [Actualización de Oracle a 19c (in situ)](#actualización-de-oracle-a-19c-in-situ).
  - Instalar Oracle y migrar la base de datos. Consulte [Actualización de Oracle a 19c (migración)](#actualización-de-oracle-a-19c-migración).

##### Oracle PDB (multiarrendatario)

Puede utilizar una base de datos conectable (PDB) para la base de datos OpenPages . OpenPages da soporte a Oracle PDB con Oracle 19c.

Puede actualizar OpenPages, crear una base de datos de contenedor (CDB) y, a continuación, importar la base de datos de OpenPages en una base de datos conectable en blanco.

Para obtener más información, consulte [Introducción a la arquitectura multiarrendatario](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fdatabase%2Foracle%2Foracle-database%2F19%2Fmulti%2Fintroduction-to-the-multitenant-architecture.html%23GUID-267F7D12-D33F-4AC9-AA45-E9CD671B6F22) en la documentación de Oracle .

##### Actualización de Oracle a 19c (in situ)

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Actualizar software de requisito previo › Opciones de actualización de Oracle y Oracle PDB` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pdb-upgrading-oracle-19c-in-place)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Debe actualizar Oracle a la versión 19c (19.x). Siga estos pasos si desea actualizar Oracle realizando la instalación encima del despliegue de Oracle existente (actualización in situ).

###### Acerca de esta tarea

Este tema proporciona una descripción general del proceso de actualización. Para obtener más información, consulte las [guías de instalación y actualización deOracle](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fdatabase%2Foracle%2Foracle-database%2F19%2Finstall-and-upgrade.html).

Póngase en contacto con el administrador de base de datos (DBA) de Oracle antes de empezar este procedimiento.

> **Nota:** Si utiliza caracteres especiales en las contraseñas de base de datos, antes de actualizar, asegúrese de que las contraseñas de base de datos no contengan el carácter @.

###### Procedimiento

1. Realice los pasos previos a la actualización de Oracle y compruebe que el sistema cumple con los requisitos previos de instalación.

   Para obtener más información, consulte la publicación [Oracle Database Upgrade Guide](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fdatabase%2Foracle%2Foracle-database%2F19%2Fupgrd%2Fintro-to-upgrading-oracle-database.html%23GUID-FA024F34-A61A-4C4B-AA60-C123A9191A16).
2. Detenga todos los servidores de aplicaciones OpenPages® (admin y no admin), todos los servidores de informes (activos y en espera) y el servidor de búsqueda.

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
3. Realice una copia de seguridad de las bases de datos OpenPages y Cognos® utilizando los programas de utilidad OPBackup y OPCCBackup.

   Para obtener más información, consulte:

   - [Copia de seguridad de la base de datos OpenPages (Oracle)](#copia-de-seguridad-de-la-base-de-datos-openpages-oracle)
   - [Copia de seguridad del almacén de contenido de Cognos (Oracle)](#copia-de-seguridad-del-almacén-de-contenido-de-cognos-oracle)
4. Instale la nueva versión de Oracle.

   Para obtener más información, consulte [Instalación de Oracle](5.1-guia-de-instalacion-y-despliegue-solo-local.md#instalación-de-oracle-19c) y la documentación de Oracle .
5. Vaya al directorio `ORACLE_HOME` y, a continuación, inicie el **Asistente de actualización de base de datos**.

   - Windows: Pulse **Iniciar** > **Oracle `<HOME_NAME>`** > **Herramientas de configuración y migración** > **Asistente de actualización de base de datos**.
   - Linux®: Ejecute `dbua` desde el directorio `<ORACLE_HOME/bin` . Por ejemplo:

     ```bash
     cd /home/oracle/app/product/19.3/bin/
     ./dbua
     ```
6. Actualice las bases de datos.

   Confirme las opciones con el administrador de base de datos de Oracle. Normalmente, se pueden utilizar los valores predeterminados, con las excepciones siguientes:

   1. Seleccione la base de datos de OpenPages y la base de datos de Cognos . Escriba las credenciales `sysdba`. Pulse **Siguiente**.

      Compruebe la lista de acciones necesarias y recomendadas. Resuelva cualquier problema.
   2. En la pestaña **Seleccionar opciones de actualización** , utilice las opciones predeterminadas.
   3. En la pestaña **Seleccionar opciones de recuperación** , utilice las opciones recomendadas por el administrador de base de datos de Oracle .

      Para omitir por completo las copias de seguridad, seleccione **I have my own backup and restore strategy** (Tengo mi propia estrategia de copia de seguridad y recuperación).
   4. En los separadores **Configurar red** y **Configurar gestión** , utilice las opciones predeterminadas.
   5. Revise la página **Resumen** . Verifique que los valores de **Target Oracle Home** y **Source Oracle Home** sean correctos. Verifique los otros valores de la página **Summary** y pulse **Next**.
7. Realice los pasos posteriores a la actualización de Oracle.

   Para obtener más información, consulte [Tareas posteriores a la actualización para Oracle Database](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fdatabase%2Foracle%2Foracle-database%2F19%2Fupgrd%2Fpost-upgrade-tasks-oracle-database.html%23GUID-637ADBD0-866B-4B64-9513-4C7CDE84895C)
8. Siga estos pasos en todos los servidores de aplicaciones y todos los servidores de informes:

   1. Instale la nueva versión del software de cliente de Oracle.

      Utilice la misma versión que el software de base de datos Oracle.
   2. Actualice la variable de entorno `<ORACLE_HOME>` para que apunte a la instalación de Oracle actualizada.
   3. Copie los siguientes archivos de la instalación de cliente de Oracle anterior en la instalación de cliente de Oracle actualizada:

      - `sqlnet.ora` (si existe)
      - `tnsnames.ora`

      Verifique que el parámetro `HOST` del archivo `tnsnames.ora` esté establecido en el nombre de host del servidor Oracle actualizado.
9. Inicie todos los servidores de aplicaciones OpenPages (admin y no admin), todos los servidores de informes (activos y en espera) y el servidor de búsqueda.

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).

##### Actualización de Oracle a 19c (migración)

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Actualizar software de requisito previo › Opciones de actualización de Oracle y Oracle PDB` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pdb-upgrading-oracle-19c-migration)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede instalar Oracle 19c (19.x) en hardware nuevo y, a continuación, migrar las bases de datos OpenPages® y Cognos® .

###### Acerca de esta tarea

Si desea actualizar Oracle in situ, consulte [Actualización de Oracle a 19c (in situ)](#actualización-de-oracle-a-19c-in-situ).

> **Nota:** Si utiliza caracteres especiales en las contraseñas de base de datos, antes de actualizar, asegúrese de que las contraseñas de base de datos no contengan el carácter @.

###### Procedimiento

1. Realice los pasos previos a la actualización de Oracle y compruebe que el sistema cumple con los requisitos previos de instalación.

   Para obtener más información, consulte la publicación [Oracle Database Upgrade Guide](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fdatabase%2Foracle%2Foracle-database%2F19%2Fupgrd%2Fintro-to-upgrading-oracle-database.html%23GUID-FA024F34-A61A-4C4B-AA60-C123A9191A16).
2. Instale la nueva versión de Oracle.

   Para obtener más información, consulte [Instalación de Oracle](5.1-guia-de-instalacion-y-despliegue-solo-local.md#instalación-de-oracle-19c) y la documentación de Oracle .
3. Detenga todos los servidores de aplicaciones OpenPages (admin y no admin), todos los servidores de informes (activos y en espera) y el servidor de búsqueda.

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
4. Haga una copia de seguridad de las bases de datos OpenPages y Cognos utilizando los programas de utilidad OPBackup y OPCCBackup.

   Para obtener más información, consulte:

   - [Copia de seguridad de la base de datos OpenPages (Oracle)](#copia-de-seguridad-de-la-base-de-datos-openpages-oracle)
   - [Copia de seguridad del almacén de contenido de Cognos (Oracle)](#copia-de-seguridad-del-almacén-de-contenido-de-cognos-oracle)
5. Restaure las bases de datos OpenPages y Cognos utilizando los programas de utilidad OPRestore y OPCCRestore.
6. Siga estos pasos en todos los servidores de aplicaciones y todos los servidores de informes:

   1. Instale la nueva versión del software de cliente de Oracle.

      Utilice la misma versión que el software de base de datos Oracle.
   2. Actualice la variable de entorno `<ORACLE_HOME>` para que apunte a la instalación de Oracle actualizada.
   3. Copie los siguientes archivos de la instalación de cliente de Oracle anterior en la instalación de cliente de Oracle actualizada:

      - `sqlnet.ora` (si existe)
      - `tnsnames.ora`

      Verifique que el parámetro `HOST` del archivo `tnsnames.ora` esté establecido en el nombre de host del servidor Oracle actualizado.
7. Inicie todos los servidores de aplicaciones OpenPages (admin y no admin), todos los servidores de informes (activos y en espera) y el servidor de búsqueda.

#### Actualización de Cognos

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Actualizar software de requisito previo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ups-upgrading-cognos-analytics)

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

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Actualizar software de requisito previo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ups-getting-sdk-windows)

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

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización › Actualizar software de requisito previo` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ups-getting-sdk-linux)

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

`Guía de actualización para Oracle (solo en local) › Preparación de la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pu-verifying-servers-before-you-upgrade)

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

`Guía de actualización para Oracle (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ugopo-upgrading)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Complete las tareas siguientes para actualizar IBM OpenPages®.

> **Nota:** Esta lista sólo se aplica a las actualizaciones in situ. Si está migrando a 9.0, consulte la publicación *IBM OpenPages Guía de instalación y despliegue*. Para obtener más información sobre las vías de acceso de actualización, consulte [Determinar la vía de acceso de actualización](#determinar-la-ruta-de-actualización).

- Realice las tareas de preparación:

  - Descargue el kit de instalación desde Passport Advantage
  - [Revisión de las características y arreglos nuevos](#revisión-de-las-características-y-arreglos-nuevos)
  - [Copia de seguridad del entorno](#copia-de-seguridad-del-entorno)
  - [Actualizar software de requisito previo](#actualizar-software-de-requisito-previo)
  - [Verificación de los servidores antes de la actualización](#verificación-de-los-servidores-antes-de-la-actualización)
- Actualice la base de datos OpenPages manualmente. Para obtener más información, consulte [Actualización de la base de datos OpenPages (Oracle)](#actualizar-la-base-de-datos-de-openpages-oracle).
- Prepare el servidor de instalación. Para obtener más información, consulte [Preparación del servidor de instalación](#preparación-del-servidor-de-instalación)
- Actualice IBM OpenPages. Para obtener más información, consulte [Actualización de OpenPages](#actualización-openpages).
- Realice las tareas posteriores a la instalación para las actualizaciones in situ. Para obtener más información, consulte [Tareas posteriores a la actualización](#tareas-posteriores-a-la-actualización).

### Actualizar la base de datos de OpenPages (Oracle)

`Guía de actualización para Oracle (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=upgrading-upgrade-openpages-database-oracle)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Actualice la base de datos de OpenPages® ejecutando scripts. Utilice estos temas si está actualizando OpenPages in situ.

Realice las tareas siguientes:

1. Prepare la base de datos para la actualización.

   Un usuario con privilegios SYSDBA debe realizar esta tarea. Consulte [Preparación de la base de datos Oracle](#preparación-de-la-base-de-datos-de-oracle).
2. Prepare los guiones para la actualización. Consulte [Preparación de los scripts de actualización de la base de datos (Oracle)](#preparación-de-los-scripts-de-actualización-de-la-base-de-datos-oracle).
3. Ejecute los scripts de actualización de la base de datos.

   Debe ejecutar todos los scripts de actualización en secuencia.

   1. [Ejecución del script de DBA previo a la actualización (Oracle)](#ejecución-del-script-de-dba-previo-a-la-actualización-oracle)

      Durante este paso, un administrador de base de datos ejecuta un script para preparar la base de datos para la actualización. Utilice un usuario DBA que no tenga privilegios SYSDBA para ejecutar este script.
   2. [Validación del paso de DBA previo a la actualización (Oracle)](#validación-del-paso-de-dba-previo-a-la-actualización-oracle)

      Durante este paso, se ejecuta un script para verificar que el script previo a la actualización se ha completado correctamente y que el esquema de base de datos está listo para la actualización.

      El propietario del esquema puede ejecutar este script.
   3. [Actualización del esquema (Oracle)](#actualización-del-esquema-oracle)

      Durante este paso, se ejecuta un script para actualizar el esquema. El script determina la versión actual del esquema de base de datos y, a continuación, ejecuta los scripts de actualización necesarios para actualizar el esquema.

      El propietario del esquema puede ejecutar este script.
   4. [Ejecución del script de DBA posterior a la actualización (Oracle)](#ejecución-del-script-de-dba-posterior-a-la-actualización-oracle)

      Durante este paso, un administrador de la base de datos ejecuta un script para completar la actualización de la base de datos y establecer los parámetros de ajuste de la base de datos. Utilice un usuario DBA que no tenga privilegios SYSDBA para ejecutar este script.
   5. [Validación del paso de DBA posterior a la actualización (Oracle)](#validación-del-paso-de-dba-posterior-a-la-actualización-oracle)

      Durante este paso, se ejecuta un script para validar el paso posterior a la actualización.

      El propietario del esquema puede ejecutar este script.

#### Preparación de la base de datos de Oracle

`Guía de actualización para Oracle (solo en local) › Actualización › Actualice la base de datos OpenPages (Oracle)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodo-preparing-database-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Un usuario con privilegios SYSDBA debe realizar algunos pasos para configurar la base de datos antes de actualizarla.

##### Acerca de esta tarea

Un DBA con privilegios SYSDBA debe ejecutar el script `op-database-sysdba-upgrade.sql` antes de actualizar la base de datos. El script concede los privilegios necesarios para la actualización del esquema de la base de datos.

Esta tarea es necesaria en los siguientes casos:

- Al instalar un 9.0 fix pack
- Al realizar una actualización in situ a 9.0.0.0
- Cuando estás migrando de 8.x a 9.0.0.0

##### Procedimiento

1. Inicie la sesión en el servidor de base de datos como un usuario con privilegios administrativos.
2. Ve al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS`.
3. Verifica que tienes permiso de ejecución sobre los ficheros del directorio `UPGRADE_SCRIPTS` y sus subdirectorios. Si no es así, cambia los permisos mediante el comando `chmod`.
4. En SQL*Plus, ejecute la secuencia de comandos `op-database-sysdba-upgrade.sql` como usuario con privilegios SYSDBA.

   ```
   sqlplus <sysdba_user>/<sysdba_password>@<oracle_tns_alias> as sysdba @op-database-sysdba-upgrade.sql <op_user>
   ```

   **Tabla 1. Parámetros del script `op-database-sysdba-upgrade.sql` para bases de datos Oracle**

   | Parámetro | Descripción |
   | --- | --- |
   | `<oracle_tns_alias>` | El alias TNS de la instancia de base de datos Oracle, por ejemplo `OP` |
   | `<sysdba_user>` | Un usuario con privilegios SYSDBA, por ejemplo `sys` |
   | `<sysdba_password>` | Contraseña del usuario SYSDBA<br>Si la contraseña contiene caracteres especiales, utilice `\"` alrededor de la contraseña. Para obtener más información, consulte [Caracteres especiales en las contraseñas](#caracteres-especiales-en-las-contraseñas). |
   | `<op_user>` | El propietario del esquema OpenPages®, por ejemplo `openpage` |

   Por ejemplo:

   ```
   sqlplus sys/<sysdba_password>@OP as sysdba @op-database-sysdba-upgrade.sql openpage
   ```

#### Preparación de los scripts de actualización de la base de datos (Oracle)

`Guía de actualización para Oracle (solo en local) › Actualización › Actualice la base de datos OpenPages (Oracle)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodo-preparing-database-upgrade-scripts)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Prepare el entorno para la actualización del esquema de base de datos.

##### Procedimiento

1. Concluir todos los componentes de OpenPages® : servidores de aplicaciones (admin y no admin), servidores de informes (activos y en espera) y el servidor de búsqueda.

   Para obtener más información, consulte [Inicio y detención de servidores](5.2-guia-de-instalacion-y-despliegue-solo-local.md#iniciar-y-detener-servidores).
2. Asegúrese de que el servidor de bases de datos Oracle esté en ejecución.
3. Inicie sesión en el sistema servidor de bases de datos Oracle como usuario con privilegios administrativos.
4. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS` .
5. Verifique que tiene permiso de escritura en el archivo `sql-wrapper.sql` .
6. Edite el archivo `sql-wrapper.sql` .

   > **Nota:** Cambie sólo los parámetros que se describen en este paso.

   **Tabla 1. Parámetros en el archivo `sql-wrapper.sql` para bases de datos Oracle**

   | Propiedad | Descripción |
   | --- | --- |
   | `opx_datafile_storage_dir` | Define la ubicación física de los archivos de datos que están asociados con los espacios de tabla que se crean. Este valor debe establecerse en un valor adecuado a su entorno. |
   | `opx_dflt_sid` | Alias TNS de la base de datos de Oracle para OpenPages. |
   | `opx_db_owner` | El propietario de la base de datos de OpenPages |
   | `opx_oracle_dba_user` | Nombre de un usuario DBA. Si el administrador de base de datos va a ejecutar los scripts de DBA en lugar del usuario, puede dejar este valor vacío al ejecutar los scripts que no son de DBA. |
   | `opx_override_ver_check` | Utilice el valor predeterminado, `N`, a menos que vuelva a ejecutar los scripts de actualización de base de datos después de una anomalía.<br>Si la actualización de la base de datos ha fallado en medio del proceso de actualización del esquema, establezca este parámetro en `Y`. Al volver a ejecutar el script de actualización, el proceso de actualización se reanuda a partir del último paso de actualización de esquema satisfactorio. |
7. Si desea ejecutar un script personalizado durante el proceso de actualización, consulte [Ejecución de scripts personalizados durante la actualización de la base de datos (Oracle)](#ejecución-de-scripts-personalizados-durante-la-actualización-de-base-de-datos-oracle).
8. Si el administrador de base de datos va a ejecutar los scripts que requieren privilegios de DBA, prepare los archivos para el administrador de base de datos.

   1. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS` .
   2. Abra el archivo `op-dba-upgrade-file-list.txt` .
   3. Enviar a su administrador de base de datos el archivo `sql-wrapper.sql` que ha actualizado junto con los archivos listados en el archivo `op-dba-upgrade-file-list.txt` .
   4. Envíe al DBA las instrucciones para ejecutar los scripts de DBA.

      - [Ejecución del script de DBA previo a la actualización (Oracle)](#ejecución-del-script-de-dba-previo-a-la-actualización-oracle)
      - [Ejecución del script de DBA posterior a la actualización (Oracle)](#ejecución-del-script-de-dba-posterior-a-la-actualización-oracle)

##### Ejecución de scripts personalizados durante la actualización de base de datos (Oracle)

`Guía de actualización para Oracle (solo en local) › Actualización › Actualice la base de datos OpenPages (Oracle) › Preparación de los scripts de actualización de la base de datos` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=scripts-running-custom-during-database-upgrade-oracle)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si desea ejecutar scripts personalizados durante el proceso de actualización de la base de datos, edite el archivo `sql-wrapper.sql` para especificar los scripts que se deben ejecutar.

###### Acerca de esta tarea

Puede utilizar el parámetro `custom_data_upgrade_script` para configurar un script personalizado.

El script que especifique se ejecuta durante el paso de actualización de base de datos. El script `op-database-product-upgrade.sh/bat` llama al script personalizado después de que se completen los demás pasos de actualización, como los cambios de DDL, los cambios de código PL/SQL y los cambios de datos de nivel de base de datos.

###### Procedimiento

1. Abra el archivo `sql-wrapper.sql` .
2. Edite los siguientes parámetros:

   ```
   define custom_data_upgrade_script=no-op.sql
   ```

   Sustituya `no-op.sql` por el script que desea ejecutar.
3. Coloque los scripts personalizados en el mismo directorio que el archivo `sql-wrapper.sql` .

#### Ejecución del script de DBA previo a la actualización (Oracle)

`Guía de actualización para Oracle (solo en local) › Actualización › Actualice la base de datos OpenPages (Oracle)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodo-running-pre-upgrade-dba-script)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Solicite al administrador de base de datos que ejecute el script previo a la actualización. O, si tiene el rol DBA, puede ejecutar el script.

##### Antes de empezar

- El servidor de bases de datos Oracle se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- Se ha definido la variable del sistema `JAVA_HOME`.
- Se ha definido la variable del sistema `ORACLE_HOME`.

##### Acerca de esta tarea

Ejecute el siguiente script: `op-database-dba-upgrade.sh|.bat`. El script utiliza los parámetros definidos en el archivo `sql-wrapper.sql`.

##### Procedimiento

1. Inicie la sesión en el sistema del servidor de bases de datos Oracle como administrador de base de datos (DBA).
2. Localice los scripts que son necesarios.

   Si es un administrador de base de datos, obtenga los scripts de su equipo de OpenPages .

   O bien, puede obtener los scripts del directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución en los scripts.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno.

   1. Para el parámetro `opx_oracle_dba_user` , especifique un usuario DBA que no tenga privilegios SYSDBA.
   2. Si ha personalizado los nombres de espacios de tablas, actualice los parámetros `define opx_dflt_*` con los nombres de espacios de tablas personalizados.
   3. Si desea ejecutar scripts personalizados durante la actualización, consulte [Ejecución de scripts personalizados durante la actualización de la base de datos (Oracle)](#ejecución-de-scripts-personalizados-durante-la-actualización-de-base-de-datos-oracle).
5. Ejecute el mandato siguiente:

   - Windows:

     ```
     op-database-dba-upgrade.bat pre "<dba_password>"
     ```
   - En Linux®:

     ```bash
     ./op-database-dba-upgrade.sh pre '<dba_password>'
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales. Consulte [Caracteres especiales en contraseñas](#caracteres-especiales-en-las-contraseñas).
6. Verifique que el código de retorno es 0, lo que indica que es satisfactorio.

   También puede comprobar el archivo de registro, `op-database-dba-upgrade.pre.*.log`.

##### Qué hacer a continuación

Validar el script previo a la actualización.

#### Validación del paso de DBA previo a la actualización (Oracle)

`Guía de actualización para Oracle (solo en local) › Actualización › Actualice la base de datos OpenPages (Oracle)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodo-validating-pre-upgrade-dba-step)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Ejecute el script para validar los pasos de DBA previos a la actualización.

##### Antes de empezar

- El servidor de bases de datos Oracle se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- Se ha definido la variable del sistema `JAVA_HOME`.
- Se ha definido la variable del sistema `ORACLE_HOME`.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de bases de datos Oracle como usuario de la aplicación OpenPages , `opuser`.
2. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución en los scripts.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno.
5. Ejecute el mandato siguiente:

   - Windows:

     ```
     op-database-product-upgrade.bat preupgrade "<op_schema_owner_password>"
     ```
   - En Linux®:

     ```bash
     ./op-database-product-upgrade.sh preupgrade '<op_schema_owner_password>'
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales.
6. Verifique que el script se ha completado correctamente.

   Busque el siguiente mensaje:`Status:Success`o un código de retorno de 0.

   También puede comprobar el archivo de registro, `op-database-product-upgrade.preupgrade.*.log`.

##### Qué hacer a continuación

Ejecute el script para actualizar el esquema de base de datos.

#### Actualización del esquema (Oracle)

`Guía de actualización para Oracle (solo en local) › Actualización › Actualice la base de datos OpenPages (Oracle)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodo-upgrading-schema)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Ejecute el script para actualizar el esquema de base de datos.

##### Antes de empezar

- El servidor de bases de datos Oracle se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- Se ha definido la variable del sistema `JAVA_HOME`.
- Se ha definido la variable del sistema `ORACLE_HOME`.
- El script `op-database-product-upgrade.sh|.bat preupgrade` se ha completado satisfactoriamente.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de bases de datos Oracle como usuario de la aplicación OpenPages , `opuser`.
2. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS` .
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

#### Ejecución del script de DBA posterior a la actualización (Oracle)

`Guía de actualización para Oracle (solo en local) › Actualización › Actualice la base de datos OpenPages (Oracle)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodo-running-post-upgrade-dba-script)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Solicite al administrador de base de datos que ejecute el script posterior a la actualización. O, si tiene el rol DBA, puede ejecutar el script.

##### Antes de empezar

- El servidor de bases de datos Oracle se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- Se ha definido la variable del sistema `JAVA_HOME`.
- Se ha definido la variable del sistema `ORACLE_HOME`.
- El script `op-database-product-upgrade.sh|.bat upgrade` se ha completado satisfactoriamente.

##### Acerca de esta tarea

Ejecute el siguiente script: `op-database-dba-upgrade.sh|.bat`. El script utiliza los parámetros definidos en el archivo `sql-wrapper.sql`.

##### Procedimiento

1. Inicie la sesión en el sistema del servidor de bases de datos Oracle como administrador de base de datos (DBA).
2. Localice los scripts que son necesarios.

   Si es un administrador de base de datos, obtenga los scripts de su equipo de OpenPages .

   O bien, puede obtener los scripts del directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución en los scripts.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno. En el parámetro `opx_oracle_dba_user` , especifique un usuario DBA que no tenga privilegios SYSDBA.
5. Ejecute el mandato siguiente:

   - Windows:

     ```
     op-database-dba-upgrade.bat post "<dba_password>"
     ```
   - En Linux®:

     ```bash
     ./op-database-dba-upgrade.sh post '<dba_password>'
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales. Consulte [Caracteres especiales en contraseñas](#caracteres-especiales-en-las-contraseñas).
6. Verifique que el código de retorno es 0, lo que indica que es satisfactorio.

   También puede comprobar el archivo de registro: `op-database-dba-upgrade.post.*.log`.

##### Qué hacer a continuación

Valide el paso de DBA posterior a la actualización.

#### Validación del paso de DBA posterior a la actualización (Oracle)

`Guía de actualización para Oracle (solo en local) › Actualización › Actualice la base de datos OpenPages (Oracle)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uodo-validating-post-upgrade-dba-step)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Ejecute el script para validar los pasos de DBA posteriores a la actualización.

##### Antes de empezar

- El servidor de bases de datos Oracle se está ejecutando. Todos los demás servidores de OpenPages® se detienen.
- Se ha definido la variable del sistema `JAVA_HOME`.
- Se ha definido la variable del sistema `ORACLE_HOME`.

##### Procedimiento

1. Inicie sesión en el sistema del servidor de bases de datos Oracle como usuario de la aplicación OpenPages , `opuser`.
2. Vaya al directorio `/OP_<version>_Main/OP_<version>_Configuration/Database/ORACLE/UPGRADE_SCRIPTS` .
3. Verifique que tiene permiso de ejecución en los scripts.
4. Abra el archivo `sql-wrapper.sql` . Verifique que los valores son adecuados para su entorno.
5. Ejecute el mandato siguiente:

   - Windows:

     ```
     op-database-product-upgrade.bat postdba "<op_schema_owner_password>"
     ```
   - En Linux®:

     ```bash
     ./op-database-product-upgrade.sh postdba '<op_schema_owner_password>'
     ```

   > **Nota:** Las comillas son necesarias alrededor de una contraseña sólo si la contraseña contiene caracteres especiales. Consulte [Caracteres especiales en contraseñas](#caracteres-especiales-en-las-contraseñas).
6. Verifique que el script se ha completado correctamente.

   Busque el siguiente mensaje:`Status:Success`o un código de retorno de 0.

   También puede comprobar el archivo de registro, `op-database-product-upgrade.postdba.*.log`.
7. Elimine las contraseñas del archivo `sql-wrapper.sql` por motivos de seguridad.

##### Resultados

Se actualiza el esquema de base de datos OpenPages .

### Preparación del servidor de instalación

`Guía de actualización para Oracle (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=u-preparing-installation-server)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pis-setting-up-installation-server-windows)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pis-setting-up-installation-server-linux)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pis-installing-agents-manually)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pis-update-installation-server-agents)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Actualice el servidor de instalación de 9.0 para utilizar la última versión de 9.0.x.

La última versión del servidor de instalación se proporciona en el kit de instalación del fixpack.

Realice las tareas siguientes:

- Actualice el servidor de instalación.
- Si ha instalado el software de agente manualmente en servidores remotos, actualice el software de agente en cada servidor remoto.

##### Actualización del servidor de instalación

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación › Actualización del servidor de instalación y los agentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uisa-updating-installation-server-1)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación › Actualización del servidor de instalación y los agentes` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=uisa-updating-agents-manually-1)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pis-migrating-deployments-installation-server-users)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pis-starting-installation-agent-manually)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Preparación del servidor de instalación` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=pis-stopping-installation-agent-manually)

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

`Guía de actualización para Oracle (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=u-upgrading-openpages)

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
- Actualice la base de datos de OpenPages . Para obtener más información, consulte [Actualizar la base de datos de OpenPages (Oracle)](#actualizar-la-base-de-datos-de-openpages-oracle).
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
4. En la tarjeta **Servidor de bases de datos** , revise el campo **Usuario de DBA** . Asegúrese de que el **Usuario de DBA** tenga el rol de DBA y no tenga privilegios SYSDBA.

   Si las cuentas de administrador de base de datos de su entorno tienen un subconjunto del rol de DBA estándar, debe realizar una de las opciones siguientes:

   - Otorgue temporalmente el rol de administrador de base de datos al usuario de administrador de base de datos.
   - Cambie la opción **Instalar base de datos** a **Sólo no DBA** o **Ya instalado**. Con este método puede utilizar un DBA que no tenga el rol de DBA estándar.
5. Pulse la lista **Tarea de despliegue** y seleccione **Actualizar**y, a continuación, seleccione la versión que desea instalar.

   Si **Actualizar** no se muestra en la lista **Tarea de despliegue**, pulse **Validar**.

   *Figura 1. Selección de la tarea de actualización*

   ![La lista de tipos de despliegue se expande y se selecciona Actualizar. También se muestra la versión, 9.0.](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/op_inst_upgrade.png)
6. En cada tarjeta de servidor de aplicaciones, verifique que **Directorio de inicio de Java** esté establecido en IBM SDK, Java™ Technology Edition que ha instalado en el servidor de aplicaciones.
7. Pulse **Validar**.
8. Pulse **Instalar**.

   > **Sugerencia:** Puede cerrar la sesión y cerrar la ventana del navegador. El proceso de **instalación** continúa ejecutándose. Cuando vuelve a iniciar la sesión en la aplicación de instalación, la aplicación muestra el estado del despliegue. También puede cerrar la ventana de navegador durante el proceso de **configuración**.
9. Pulse **Configurar**.

#### Qué hacer a continuación

Lleve a cabo las tareas posteriores a la instalación. Para obtener más información, consulte [Tareas posteriores a la actualización](#tareas-posteriores-a-la-actualización).

### Tareas posteriores a la actualización

`Guía de actualización para Oracle (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=u-post-upgrade-tasks)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Después de actualizar IBM OpenPages®, debe completar algunas tareas adicionales.

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

#### Eliminar el botón de lanzamiento de interfaz de usuario de cuestionario heredado de la vista de administración para las evaluaciones de cuestionario

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-remove-legacy-questionnaire-ui-launch-button-from-admin-view-questionnaire-assessments-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

La vista de administrador de evaluación de cuestionario muestra el botón **Iniciar interfaz de usuario de cuestionario** heredado. Si un administrador pulsa este botón, se visualiza una página de error 404.

##### Acerca de esta tarea

Para eliminar este botón, cree una vista de administrador personalizada para las evaluaciones de cuestionario y elimine el campo **IU de cuestionario** de la vista y haga que la vista de administrador personalizada sea la predeterminada.

Puesto que los campos que están en el perfil pero que no están ya en la vista se añadirán automáticamente en tiempo de ejecución, elimine todas las referencias al campo **RespQuest** de todos los perfiles utilizados por los administradores.

##### Procedimiento

1. Haz clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Vistas**.
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
13. Haz clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Perfiles**.
14. Para cada perfil utilizado por los administradores, realice los pasos siguientes:

    1. Pulse el perfil.
    2. Expanda **Tipos de objeto**.
    3. Haga clic en **Evaluación de cuestionario**.
    4. Expanda **Campos** y busque **RespQuest**.
    5. Seleccione **RespQuest** y pulse **Eliminar**.

#### Actualización de aplicaciones opcionales

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-updating-optional-apps)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si utiliza apps opcionales, como conectores IBM OpenPages® , es posible que tenga que actualizarlas al actualizar a 9.0.

##### Actualización desde 8.2.0.0

Si utiliza IBM OpenPages SDI Connector for UCF Common Controls Hub o el conector QRadar® , debe actualizar IBM® Security Directory Integrator a la versión 7.2.0.6.

- [Actualización de UCF](5.1-guia-de-instalacion-y-despliegue-solo-local.md#actualización-de-ibm-openpages-sdi-connector-for-ucf-common-controls-hub)
- [Actualización de QRadar](5.1-guia-de-instalacion-y-despliegue-solo-local.md#actualización-de-ibm-security-directory-integrator-para-el-conector-qradar)

#### Restaurar valores del servidor de aplicaciones personalizado

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-restore-custom-application-server-settings)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Después de actualizar, restaure los valores de configuración y las personalizaciones del servidor de aplicaciones.

Si ha realizado cambios en los siguientes archivos en el entorno previo a la actualización, vuelva a implementar los cambios después de la actualización.

- `<OP_HOME>/aurora/conf/aurora.properties`
- `<OP_HOME>/aurora/conf/Server<#>-server.properties`
- `<OP_HOME>/aurora/conf/Server<#>-sosa.properties`

Por ejemplo, consulte [Acortar la URL para OpenPages®](3.4-guia-del-administrador.md#acortar-la-url-para-openpages)

Si se ha configurado el inicio de sesión único (SSO) en el sistema de origen, debe actualizar la configuración de SSO en el entorno de destino. Para obtener más información, consulte [Integración de inicio de sesión único para el servidor de aplicaciones OpnePages](5.2-guia-de-instalacion-y-despliegue-solo-local.md#integración-de-inicio-de-sesión-único-para-el-servidor-de-aplicaciones-openpages).

#### Restauración de asistentes de soluciones, imágenes y otros archivos

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-restoring-solutions-helpers-images-other-files-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Restaure los asistentes de soluciones, imágenes y otras entregas personalizadas de las que ha realizado copia de seguridad.

##### Acerca de esta tarea

Si ha realizado una copia de seguridad de los elementos siguientes, restáurelos:

- Esquema de soluciones
- Entregables personalizados de IBM® Expert Labs
- Código personalizado

#### Volver a crear el índice para la búsqueda global

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-re-creating-index-global-search-1)

**Se aplica a:** En los locales

Puede volver a crear el índice para la búsqueda global.

> **Importante:** Si ha actualizado o migrado a ' IBM OpenPages® 9 9.0.0 desde 8.2.0.x, debe volver a crear el índice para la búsqueda global. Si no vuelve a crear el índice, la búsqueda global no funcionará.

Si necesita solucionar un problema al volver a crear el índice para la búsqueda global, o si prefiere utilizar una interfaz de línea de comandos, puede utilizar la CLI para volver a crear el índice. Para obtener más información, consulte [¿Cómo automatizar las tareas de Solr?](https://www.ibm.com/support/pages/node/6409982)

##### Procedimiento

1. Inicie sesión en ' OpenPages ' como usuario con privilegios administrativos.
2. Haz clic en " **Abrir el menú Administración ' ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Búsqueda global** " y en " **Desactivar**".
3. Pulse **Descartar** para descartar el índice de búsqueda.

   Espere a que finalice el proceso de descartado.
4. Pulse **Crear** para volver a crear el índice de búsqueda.

#### Actualizar informes

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-updating-reports-1)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-enable-ldap-after-upgrading-migrating-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si ha utilizado LDAP en la versión anterior de IBM OpenPages®, debe volver a habilitar LDAP.

Para obtener más información, consulte [Habilitación de LDAP de modalidad mixta](3.1-guia-del-administrador.md#configuración-de-la-autenticación-de-modo-mixto).

#### Tareas posteriores a la actualización para las soluciones

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-post-upgrade-tasks-solutions)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización › Tareas posteriores a la actualización para las soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=puts-replacing-computed-fields-calculations-url-launcher-fields-iam-itg-1)

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
   2. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** >**Configuración de la solución** >**Tipos de objeto**.
   3. Pulse el tipo de objeto **Auditoría** .
   4. En el campo `OPSS-Aud` , agrupe, actualice los campos siguientes para utilizar el tipo de visualización **Enlace** :

      - Cerrar auditoría
      - Planes
   5. Repita estos pasos para los campos siguientes:

      - RiskEntity: OPSS-RiskEnt: Baselines
      - Resource: OPSS-Res: Resource Links
6. Utilice FastMap para cargar los cambios de objeto de preferencia:

   1. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **FastMap Importar**.
   2. Pulse **Elegir archivo** y seleccione el archivo `IAM_computed_field_preference_updates.xls` .
   3. Pulse **Importar datos**.
   4. Revise el informe de verificación y, a continuación, pulse **Importar datos**.

###### Qué hacer a continuación

Siga los pasos descritos en [Sustitución de campos calculados por campos de lanzador de URL (RCSA)](#sustitución-de-campos-calculados-por-campos-de-lanzamiento-de-url-rcsa).

##### Sustitución de campos calculados por campos de lanzamiento de URL (RCSA)

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización › Tareas posteriores a la actualización para las soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=puts-replacing-computed-fields-url-launcher-fields-rcsa-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Los ayudantes de RCSA han utilizado campos calculados en releases anteriores. Puede cambiar los campos a campos URL en lugar de campos computados. Los campos se sustituyen por campos nuevos que utilizan los mismos nombres.

###### Acerca de esta tarea

Esta tarea sustituye los siguientes campos calculados por campos URL :

- Risk Assessment: OPSS-RA: RCSA Completion Helper
- Risk Assessment: OPSS-RA: RCSA Process Alignment Helper

Si desea revisar los cambios antes de implementarlos, consulte el archivo que se lista en el paso 1.

> **Nota:** Estos pasos utilizan Gestor de objetos, pero puede utilizar **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Migración del sistema** > **Importar configuración** para importar el archivo `ORM_computed_field_url_field_replacement-op-config.xml`. Para obtener más información, consulte [Importación de un archivo de migración](3.5-guia-del-administrador.md#importación-de-un-archivo-de-migración).

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

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización › Tareas posteriores a la actualización para las soluciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=puts-importing-solutions-report-package-1)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-updating-custom-computed-fields-1)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-updating-reporting-schema-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Actualice el esquema de elaboración de informes.

##### Antes de empezar

Asegúrese de que no se estén ejecutando informes, copias de seguridad u otros trabajos. No ejecute ningún informe, copia de seguridad u otros trabajos durante el proceso de actualización del esquema.

##### Acerca de esta tarea

Cuando actualiza el esquema de informes, todos los índices personalizados que haya definido previamente se recrean automáticamente utilizando la última definición que se encuentra en la configuración de registro adecuada. Esta función está habilitada de forma predeterminada, pero se puede inhabilitar. Para obtener más información sobre los valores para crear índices, consulte  [Valores de la carpeta Esquema de elaboración de informes](3.3-guia-del-administrador.md#valores-de-la-carpeta-esquema-de-elaboración-de-informes).

##### Procedimiento

1. Inicie sesión en OpenPages® como usuario con privilegios administrativos.
2. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** >**Activar el modo Administración del sistema**.
3. Haga clic en **Abrir menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Configuración del sistema** > **Esquema de informes**.
4. Pulse **Actualizar**.
5. Pulse **Renovar** hasta que el proceso se haya completado al 100%.
6. Inhabilite SAM. Haga clic en **Abrir menú de administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Desactivar el modo de administración del sistema**.

#### Regeneración del entorno de elaboración de informes

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-regenerating-reporting-framework-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Después de actualizar IBM OpenPages®, es posible que tenga que volver a generar el entorno de elaboración de informes.

La versión 9.0 añade una serie de campos de sistema y tipos de objeto nuevos. Si tiene previsto utilizar las nuevas prestaciones y desea poder acceder a los nuevos campos y tipos de objeto en los informes, vuelva a generar el entorno de elaboración de informes.

También debe volver a generar el entorno de elaboración de informes si alguno de los casos siguientes se aplica en su caso:

- Utiliza más de una URL para acceder a OpenPages. Al volver a generar el entorno, seleccione **Modelo de entorno**, **Asuntos de consulta personalizada** y **Todos los modelos**.
- Ha añadido nuevos campos y desea utilizar los campos nuevos en informes.

Vuelva a generar el entorno de elaboración de informes después de completar todas las tareas de instalación y actualización.

Para obtener más información, consulte [Generación del entorno de elaboración de informes](3.5-guia-del-administrador.md#generación-del-entorno-de-elaboración-de-informes).

#### Actualización de vistas de detalles a vistas de administración

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-upgrading-detail-views-admin-views-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Si está actualizando o migrando desde 8.2, puede actualizar las vistas de detalles a las vistas de administración.

Para obtener más información sobre las vistas de administración, consulte [Vistas de administración](3.6-guia-del-administrador.md#vistas-de-administrador).

##### Procedimiento

1. Haz clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Vistas**.
2. Pulse **Generar vistas de administración**. Se visualiza un recuadro de diálogo que explica cómo utilizar la característica. Siga las instrucciones del recuadro de diálogo para actualizar las vistas de detalles.

   *Figura 1. Recuadro de diálogo Generar vistas de administración*

   ![Recuadro de diálogo Generar vistas de administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/generate_admin_views.png)

#### Utilización de vistas de creación personalizadas con la aplicación Loss Event Entry

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-using-custom-creation-views-loss-event-entry-application-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

En releases anteriores a OpenPages® 8.3, la selección y el orden de los campos de la aplicación Loss Event Entry se controlaban mediante las vistas de creación que se especificaban en la herramienta de configuración de Loss Event Entry. En OpenPages 8.3, las vistas se eligen ahora utilizando las reglas y las prioridades de la vista en lugar de utilizar las vistas que se especifican explícitamente. Las vistas de creación listas para usar son `SysView-New-LossEvent-LEE`, `SysView-New-LossImpact-LEE` y `SysView-New-LossRecovery-LEE`. Todas ellas tienen reglas de visualización que hacen se apliquen solo a los usuarios que utilizan el perfil de Loss Event Entry. Estas vistas se han creado basándose en las versiones anteriores de las vistas de creación listas para usar.

Si ha personalizado las vistas de creación utilizadas para la aplicación Loss Event Entry, puede volver a crear las vistas personalizadas copiando las vistas existentes y, a continuación, aplicando las personalizaciones a las copias. Asegúrese de utilizar una regla de vista para que la vista que cree solo se aplique al perfil de Loss Event Entry.

#### Cambios y mejoras en la configuración

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=put-configuration-changes-enhancements-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Revise la siguiente lista de cambios y nuevas características. Estos cambios pueden afectar a la configuración.

##### Actualizaciones importantes en 9.0

Revise los cambios siguientes.

- **Utilizar la migración del sistema para exportar e importar plantillas de cuestionario**

  En OpenPages® versión 9.0.0.2 y posteriores, no utilice Fastmap para importar o exportar plantillas de cuestionario. Sin embargo, puede importar plantillas de cuestionario que ha exportado de una versión anterior.

  Para exportar plantillas de cuestionario, utilice **Migración del sistema > Configuración de exportación**. Para obtener más información, consulte [Exportación de elementos de configuración desde el entorno de origen](3.5-guia-del-administrador.md#exportación-de-elementos-de-configuración-desde-el-entorno-de-origen).

  Para importar plantillas de cuestionarios, utilice **Migración del sistema > Importar configuración**. Para obtener más información, consulte [Importación de elementos de configuración al entorno de destino](3.5-guia-del-administrador.md#importación-de-los-elementos-de-configuración-al-entorno-de-destino).

- **Permisos de aplicación**

  El permiso de aplicación **Motor de reglas** ahora da acceso al elemento de menú **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Configuración de la solución** > **Normas de los actos reglamentarios**.

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

  La herramienta de configuración de eventos de pérdida ahora forma parte de OpenPages. Haga clic en **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Integraciones** > **Aplicación de registro de siniestros** para configurar la entrada de eventos de pérdida.

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
  | Visualice los registros de la aplicación mediante el elemento de menú **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Otros** > **Registros**. | **Todos los permisos** > **SOX** > **Administración** > **Registros** |
  | Configure los clasificadores mediante el elemento de menú **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Integraciones** > **Sugerencias sobre cartografía y taxonomía**. | **Todos los permisos** > **SOX** > **Administración** > **Watson** |
  | Vea los procesos en segundo plano mediante el elemento de menú **Abrir el menú Administración ![menú Administración](https://www.ibm.com/docs/es/SSFUEU_9.0.0/op_grc_upgrade_ora/settings_menu_icon_task_focused_ui.jpg)** > **Otros** > **Procesos de fondo**. | El permiso de aplicación **Todos los permisos** > **API** > **Administración** > **Proceso en segundo plano** > **Obtener información de proceso** ahora también proporciona acceso al elemento de menú **Procesos en segundo plano** |
  | Publique informes en IBM® Cognos® Analytics y gestione páginas y plantillas de informe. | **Todos los permisos** > **Publicación** |

- **Desencadenantes y ayudantes personalizados**

  Si utiliza `/OpenPages/Solutions/PCM/Attestation/Email Sender Name` o `/OpenPages/Solutions/PCM/Attestation/Email Sender Address` en cualquiera de sus códigos personalizados, estos valores se eliminarán en un release futuro. Para asegurarse de que el código sigue funcionando, realice los pasos siguientes:

  1. Modifique su código sustituyendo `/OpenPages/Solutions/PCM/Attestation/Email Sender Name` por `/Applications/Common/Email/Mail From Name` y `/OpenPages/Solutions/PCM/Attestation/Email Sender Address` por `/Applications/Common/Email/Mail From Address`.
  2. Asegúrese de que `/Applications/Common/Email/Mail From Name` y `/Applications/Common/Email/Mail From Address` se han establecido correctamente para las notificaciones de correo electrónico.

  Si tiene desencadenantes personalizados, si utilizan el atributo `from.address` y ese atributo está vacío o tiene un valor de `donotreply@openpages.com`, el valor se sustituye por el valor del valor de registro `/Applications/Common/Email/Mail From Address`.

##### Rellenar el campo Título del sistema después de actualizar o migrar

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas posteriores a la actualización › Cambios y mejoras en la configuración` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=cce-populating-system-title-field-after-upgrading-migrating-1)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

La versión 9.0 introduce un nuevo campo de sistema opcional denominado Título (`System Fields:Title`). El campo es un componente de nombres de tipo de objeto y está diseñado para almacenar los nombres fáciles de usar de las instancias de objeto.

###### En segundo plano

Anteriormente, el campo Nombre sólo almacenaba los nombres de los objetos. Puesto que los nombres deben ser exclusivos dentro de una vía de acceso de carpeta, a menudo se ha utilizado otro campo, como por ejemplo Descripción, para proporcionar un nombre fácil de usar para los objetos.

En 9.0 y posteriores, el campo Nombre tiene componentes separados para almacenar el nombre (ID) y el título de los objetos: **Name.ID** (`System Fields:Name`) y **Name.Title** (`System Fields:Title`). Puede especificar qué componentes se deben visualizar en las vistas y otras áreas de la aplicación. Por ejemplo, puede utilizar el campo Título en una vista de tarea. O puede visualizar el ID y el título.

Para ayudarle a aprovechar el nuevo campo Título, OpenPages® incluye un script que puede utilizar para rellenar el campo Título con el contenido de otro campo.

Para obtener más información, consulte [Rellenar el campo Título del sistema](3.2-guia-del-administrador.md#llenado-del-componente-título-de-los-objetos).

> **Nota:** Esta tarea es opcional.

### Tareas adicionales para actualizaciones

`Guía de actualización para Oracle (solo en local) › Actualización` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=u-additional-tasks-upgrades)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Es posible que desee completar tareas adicionales para una actualización de OpenPages® .

#### Realización de una actualización silenciosa

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas adicionales para actualizaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=atu-performing-silent-upgrade)

**Se aplica a:** [De forma local](3.6-guia-del-administrador.md#openpages-tipos-de-despliegue)

Puede actualizar desde la línea de mandatos.

##### Antes de empezar

Lleve a cabo las siguientes tareas de preparación:

- [Revisión de las características y arreglos nuevos](#revisión-de-las-características-y-arreglos-nuevos)
- [Copia de seguridad del entorno](#copia-de-seguridad-del-entorno)
- [Actualizar software de requisito previo](#actualizar-software-de-requisito-previo)
- [Verificación de los servidores antes de la actualización](#verificación-de-los-servidores-antes-de-la-actualización)
- [Actualizar la base de datos de OpenPages (Oracle)](#actualizar-la-base-de-datos-de-openpages-oracle)
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
   4. Cambie `dba_username` y `dba_password` por un usuario de DBA que no tenga privilegios SYSDBA.
   5. Guarde el archivo y ciérrelo.
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

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas adicionales para actualizaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=atu-rolling-back-upgrade)

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

`Guía de actualización para Oracle (solo en local) › Actualización › Tareas adicionales para actualizaciones` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=atu-manually-loading-configuration-data-upgrade)

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

`Guía de actualización para Oracle (solo en local)` · [origen](https://www.ibm.com/docs/es/openpages/9.0.0?topic=ugopo-notices)

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

Esta información contiene ejemplos de datos e informes utilizados en operaciones comerciales diarias. Para ilustrarlas de la forma más completa posible, los ejemplos incluyen los nombres de personas, empresas, marcas y productos. Todos estos nombres son ficticios y cualquier similitud a los nombres y direcciones que haya utilizado una empresa real es pura coincidencia.

Si ha optado por visualizar la copia software de esta información, puede que no aparezcan las fotografías y las ilustraciones a color.

Esta oferta de software no utiliza cookies ni otro tipo de tecnología para recopilar información de identificación personal.
