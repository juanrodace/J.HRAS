<div align="center"><a href="https://www.escuelaing.edu.co/es/investigacion-e-innovacion/centro-de-estudios-hidraulicos/" target="_blank"><img src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/CaseUse/.icons/IconCEHBanner.jpg" alt="J.HRAS" width="100%" border="0" /></a></div>

## Creación y procesamiento del modelo de terreno
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `MDT` `Terrein`

<div align="center">
<br>
<img alt="J.HRAS" src="../../.icons/0_HRAS.svg" width="400px">
<br><b>Universidad Escuela Colombiana de Ingeniería Julio Garavito</b><br>
<a href="https://github.com/juanrodace/">Juan David Rodriguez Acevedo</a><br>
Profesor del Centro de Estudios Hidráulicos<br>
juan.rodrigueza@escuelaing.edu.co
<br>
<br></div>

<div align="center">
    <a href="https://youtu.be/vcepglrD5y8">
        <img src="../../.icons/Inicio_Actividad.png" alt="IMAGE ALT TEXT HERE" width="800"/>
    </a>
</div>

##

<div align="center">
<img alt="MDT" src="Graph/MDT.png" width="90%">
</div>

### Alcance
En esta clase se presenta el proceso recomendado la creación del proyecto, configuración del RAS Mapper y creación del modelo de terreno.

### Objetivos

* Crear el proyecto HEC-RAS y establecer la configuración general de RAS Mapper.
* Crear el terreno (.hdf) RAS Mapper a partir de la capa raster.
* Visualizar y representar el modelo de terreno en RAS Mapper.
* Asociar mapas e imágenes de dominio público como fondo.

### Requerimientos

* [Sección 1. Introducción y fundamentos](../../Section01/Readme.md)
* [Sección 2. Modelación hidráulica básica](../../Section02/Readme.md)

### Creación de proyecto y configuración de RAS-Mapper

A continuación se presenta el proceso recomendado para la creación del proyecto y configuración del RAS Mapper.

1. Una vez inicie el programa, vaya al menú **Archivo → Nuevo proyecto** (File →New Project). En la ventana emergente podrá indicar el nombre del proyecto a crear y dar clic en <kbd>OK</kbd>. Revise y/o ajuste el sistema de unidades a utilizar en el menú **Opciones → Sistema de unidades** (Options → Unit system).

<div align="center">
<img alt="MDT" src="Screens/Screen1.png" width="50%">
</div>

2. Ingrese a la herramienta RAS Mapper, dando clic en el botón <img alt="MDT" src="Graph/Mapper.png" width="4%">. Luego seleccione **Herramientas → Definir sistema proyección del proyecto** (Tools → Set Projection for Project). En la ventana emergente, seleccione el archivo de proyección a utilizar.

<div align="center">
<img alt="MDT" src="Screens/Screen2.png" width="50%">
</div>

3. En esta misma ventana o a través de **Herramientas → Opciones** (Tools → Options), es posible configurar varias opciones del RAS Mapper, como se describe a continuación.

   - Modo de renderizado (Render mode): Podrá seleccionar el modo de renderizado entre inclinado (Sloping), horizontal (Horizontal) o híbrido (Hybrid). El primero es realizado a partir de la interpolación de las elevaciones de lámina de agua en cada lado de la celda y permite que la superficie se presente inclinada y continua. El segundo es presentado a partir de las elevaciones de lámina de agua obtenidas en cada celda.
   - Configuración general (Global Settings- General): Contiene simbología de las herramientas de visualización de los mapas y dígitos decimales para visualización de resultados al vuelo en pantalla.
   - Configuración de capas (Global Settings- RAS Layers): Contiene la simbología de visualización de diferentes capas que componen el modelo.
   - Herramientas de edición (Global Settings- Editing Tools): Contiene la simbología de las herramientas de edición y las tolerancias de aproximación para puntos y líneas cercanas.

<div align="center">
<img alt="MDT" src="Screens/Screen3.png" width="50%">
</div>

### Creación y procesamiento del modelo de terreno

A continuación se presenta el proceso recomendado para la creación y procesamiento del modelo de terreno.

1. En el RAS Mapper vamos al menú **Proyecto → Crear nuevo terreno RAS** (Project → Create New Ras Terrain).

<div align="center">
<img alt="MDT" src="Screens/Screen4.png" width="50%">
</div>

2. En la ventada desplegada **Nueva capa de terreno** (New Terrain Layer), podrá cargar la información en formato Raster (librería GDAL, tipo Raster Floating Point Format, y GRID). Allí puede cargar uno o varios archivos e incluso unir (merge) varios archivos raster en el nuevo modelo de terreno RAS. En la ventana podrá seleccionar el redondeo o precisión del nuevo archivo, la creación de puntadas (stitches) si se realiza una unión (merge), conversión o no de unidades y nombre del archivo a crear. El nuevo archivo será guardado por defecto en la carpeta **Terrain** en formato <kbd>.hdf</kbd>. 

<div align="center">
<img alt="MDT" src="Screens/Screen5.png" width="50%">
</div>

3. De clic en **Crear** <kbd>Create</kbd> y se abrirá una ventana con el proceso de creación.

<div align="center">
<img alt="MDT" src="Screens/Screen6.png" width="50%">
</div>

4. A continuación, podrá visualizar el terreno creado en el RAS Mapper. Así mismo podrá modificar las opciones de visualización.

<div align="center">
<img alt="MDT" src="Screens/Screen7.png" width="50%">
</div>

### Mapas e imágenes de dominio público

Una característica adicional de RAS Mapper, es la inclusión de mapas e imágenes satelitales de fondo. Esta característica solo podrá ser utilizada sí al proyecto se le ha asignado sistema de proyección de coordenadas. Para agregar, de clic derecho en **Map Layers → AddWebImageryLayer** y escoja por ejemplo, la imagen satelital de Google y como método de muestreo, vecino más cercano (Near). Desde las propiedades de la imagen, establezca transparencia en aproximadamente 25%.

<div align="center">
<img alt="MDT" src="Screens/Screen8.png" width="50%">
</div>

### Referencias
- [HEC-RAS User’s Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/rasum/latest)
- [HEC-RAS Hydraulic Reference Manual.2020](https://www.hec.usace.army.mil/confluence/rasdocs/ras1dtechref/latest)
- [HEC-RAS Documentation. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs)
- [HEC-RAS Mapper User's Manual](https://www.hec.usace.army.mil/confluence/rasdocs/rmum/latest)
- [HEC-RAS 2D User’s Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/r2dum/latest)
- Herramientas computacionales para el diseño y modelación de cauces. r.cfdtools@gmail.com.  [(rcftools)](https://github.com/rcftools]).
    
### Control de versiones

| Versión | Descripción                                                       |                    Autor                    | Horas |
|:-------:|-------------------------------------------------------------------|:-------------------------------------------:|:-----:|
| 2023.01 | Versión inicial con definición de estructura general y contenido. | [juanrodace](https://github.com/juanrodace) |  1.0  |
| 2023.01 | Inclusión de conceptos, procedimientos, esquemas y gráficos.      | [juanrodace](https://github.com/juanrodace) |  2.0  |
| 2023.02 | Desarrollo de contenido multimedia.                               | [juanrodace](https://github.com/juanrodace) |  1.0  |

### Licencia, cláusulas y condiciones de uso

| [:arrow_backward:Anterior](../Readme.md) | [:house: Inicio](../../Readme.md) | [:beginner: Ayuda/Colabora](https://github.com/juanrodace/J.HRAS/discussions/5) | [Siguiente:arrow_forward:](../Mesh/Readme.md) |
|------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------|

_J.HRAS es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/juanrodace/J.HRAS/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [juanrodace](https://github.com/juanrodace) en GitHub._

##

<div align="center"><a href="https://enlace-academico.escuelaing.edu.co/psc/FORMULARIO/EMPLOYEE/SA/c/EC_LOCALIZACION_RE.LC_FRM_ADMEDCO_FL.GBL?&" target="_blank"><img src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/CaseUse/.icons/IconCEHBotonCertificado.png" alt="J.HRAS" width="260" border="0" /></a></div>

##

<div align="center"><a href="http://www.escuelaing.edu.co" target="_blank"><img src="../../.icons/Banner1.svg" alt="Support by" width="100%" border="0" /></a><sub><br>Este curso guía ha sido desarrollado con el apoyo de la Escuela Colombiana de Ingeniería - Julio Garavito. Encuentra más contenidos en https://github.com/uescuelaing</sub><br><br></div>