<div align="center"><a href="https://www.escuelaing.edu.co/es/investigacion-e-innovacion/centro-de-estudios-hidraulicos/" target="_blank"><img src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/CaseUse/.icons/IconCEHBanner.jpg" alt="J.HRAS" width="100%" border="0" /></a></div>

## Coeficientes de Manning a partir de Coberturas de Suelo
Keywords: `Hydraulics` `HEC-RAS` `LandCover` `Mannnig` 

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
    <a href="https://youtu.be/NZGZlJ6p5-A">
        <img src="../../.icons/Inicio_Actividad.png" alt="IMAGE ALT TEXT HERE" width="800"/>
    </a>
</div>

##

<div align="center">

![Results.png](Graph/LandCover_Manning.png)
</div>

### Alcance
En esta clase se presenta el proceso recomendado para la definición del coeficiente de Manning en el modelo hidráulico a partir de un archivo de cobertura de suelo mediante el uso de RAS Mapper.

### Objetivos

* Conocer el procedimiento para el cargue de mapas de cobertura de suelo.
* Conocer el procedimiento para el ajuste y edición de la geometría a partir de la información de coeficientes Manning.

### Requerimientos

* [**Sección 2. Modelación hidráulica básica**](../../Section02/Readme.md) 

### Coeficientes de Manning a partir de Coberturas de Suelo
A continuación se describen los pasos sugeridos para el cargue de información de cobertura de suelo, creación de mapa de coeficientes Manning y ajustes de la geometría definiendo coeficientes Manning.

#### Mapas de cobertura de suelo

Como mencioné en la Sección 1, es común que en un proyecto que implique la modelación hidráulica de un sistema natural, se cuente con información adicional como la cobertura y uso del suelo.  Así mismo, muchos estudios de medio ambiente incluyen la restitución de la cobertura en la cuenca o región de estudio. 

A partir de esta información de cobertura y uso de suelo, es posible asociar dicha información con valores **n** del coeficiente de Manning, teniendo en cuenta las recomendaciones mencionadas en la [Actividad 3](../../Section01/VariedFlow/Readme.md). 

En la siguiente imagen se muestra la asociación realizada para el ejemplo del curso, en donde a diferentes características de cobertura del suelo, se asigna un valor **n**.

<div align="center">
<img alt="Manning" src="Screens/Screen1.png" width="60%">
</div>

#### Creación de mapa de coeficientes Manning

1. En la herramienta HEC vaya a la herramienta RAS Mapper. Ahora realizamos la importación del archivo en formato vectorial con elementos geográficos dando clic en **Proyecto → Crear Nueva Capa RAS → Capa de cobertura de suelo** (Project → Create a New RAS Layer → Land Cover Layer).

<div align="center">
<img alt="Manning" src="Screens/Screen2.png" width="60%">
</div>

2. En la ventana desplegada seleccione el icono <kbd>+</kbd> para agregar el archivo. Luego seleccione la extensión del archivo como **"Geometries"** y posteriormente agregue el campo (clic en <kbd>Add Fiel...</kbd> ) de coeficientes Manning. 

<div align="center">
<img alt="Manning" src="Screens/Screen3.png" width="60%">
</div>

3. Revise los nombres de clasificación y la información del archivo de salida. Finalmente de clic en <kbd>Crate</kbd> y se iniciará el proceso.

<div align="center">
<img alt="Manning" src="Screens/Screen4.png" width="60%">
</div>
 
4. Una vez creada la capa podrá realizar la visualización y revisión de la información generada en el RAS Mapper.

<div align="center">
<img alt="Manning" src="Screens/Screen5.png" width="60%">
</div>

#### Ajuste de geometría y definición de coeficientes

1. Para el ajuste de la geometría 1D, inicie la opción de edición dando clic en el botón <kbd>:pencil2:</kbd>. Posteriormente de clic derecho sobre las secciones transversales y seleccione **Actualizar secciones transversales → Valores de Manning** (Update Cross Sections → Manning's Values). Detenga la edición y guarde los cambios.

<div align="center">
<img alt="Manning" src="Screens/Screen6.png" width="60%">
</div>

2. Podrá visualizar y revisar el ajuste a la información desde la ventana de información geométrica con ayuda de la tabla de edición de valores de Manning (Tables → Manning's n or k Values).
 
<div align="center">
<img alt="Manning" src="Screens/Screen7.png" width="60%">
</div>

### Referencias
- [HEC-RAS User’s Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/rasum/latest)
- [HEC-RAS Hydraulic Reference Manual.2020](https://www.hec.usace.army.mil/confluence/rasdocs/ras1dtechref/latest)
- [HEC-RAS Documentation. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs)
- [HEC-RAS Mapper User's Manual](https://www.hec.usace.army.mil/confluence/rasdocs/rmum/latest)
    
### Control de versiones

| Versión | Descripción                                                       |                    Autor                    | Horas |
|:-------:|-------------------------------------------------------------------|:-------------------------------------------:|:-----:|
| 2023.01 | Versión inicial con definición de estructura general y contenido. | [juanrodace](https://github.com/juanrodace) |  0.5  |
| 2023.01 | Inclusión de conceptos, procedimientos, esquemas y gráficos.      | [juanrodace](https://github.com/juanrodace) |  2.0  |
| 2023.01 | Desarrollo de contenido multimedia.                               | [juanrodace](https://github.com/juanrodace) |  1.5  |

### Licencia, cláusulas y condiciones de uso

| [:arrow_backward:Anterior](../Readme.md) | [:house: Inicio](../../Readme.md) | [:beginner: Ayuda/Colabora](https://github.com/juanrodace/J.HRAS/discussions/4) | [Siguiente:arrow_forward:](../Confluence/Readme.md) |
|------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------|

_J.HRAS es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/juanrodace/J.HRAS/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [juanrodace](https://github.com/juanrodace) en GitHub._

##

<div align="center"><a href="https://enlace-academico.escuelaing.edu.co/psc/FORMULARIO/EMPLOYEE/SA/c/EC_LOCALIZACION_RE.LC_FRM_ADMEDCO_FL.GBL" target="_blank"><img src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/CaseUse/.icons/IconCEHBannerCertificado.jpg" alt="J.HRAS" width="100%" border="0" /></a></div>

##

<div align="center"><a href="http://www.escuelaing.edu.co" target="_blank"><img src="../../.icons/Banner1.svg" alt="Support by" width="100%" border="0" /></a><sub><br>Este curso guía ha sido desarrollado con el apoyo de la Escuela Colombiana de Ingeniería - Julio Garavito. Encuentra más contenidos en https://github.com/uescuelaing</sub><br><br></div>