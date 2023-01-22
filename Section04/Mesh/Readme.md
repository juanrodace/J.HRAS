### Definición de área de drenaje y malla del modelo
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Mesh` `Area` `Perimeter`

<div align="center">
<img alt="MDT" src="Graph/Mesh.png" width="85%">
</div>

### Alcance
En esta clase se presenta el proceso recomendado para la delimitación del área de drenaje y la creación de la malla del modelo bidimensional (2D).

### Objetivos

* Crear el límite geográfico de la zona de estudio o modelación.
* Definir el espaciamiento de la malla entre celdas.
* Generar los puntos computacionales.

### Requerimientos

* [Sección 1. Introducción y fundamentos](../../Section01/Readme.md)
* [Sección 2. Modelación hidráulica básica](../../Section02/Readme.md)
* [Actividad 17. Creación del MDT](../MDT/Readme.md)

### Definición y delimitación del área de drenaje

La modelación 2D requiere además de un modelo digital de terreno (MDT), el límite geográfico de la zona de estudio dentro de la cual se definirá el mallado bidimensional. Es HEC-RAS, estas áreas se conocen como **2D Flow Áreas** y pueden ser dibujadas manualmente desde esta herramienta o a partir de un archivo vectorial previamente definido con otra herramienta. 

A continuación se presenta el proceso recomendado para la delimitación geográfica de la zona de estudio, drenaje o modelación.

1. En el RAS Mapper de clic derecho sobre **Geometrías** (Geometries) y, seleccione **Agregar nueva geometría** (Add New Geometry). En la ventana emergente, agregue el nombre que desee.

<div align="center">
<img alt="Mesh" src="Screens/Screen1.png" width="70%">
</div>

2. Inicie la opción de edición, dando clic al botón <kbd>:pencil2:</kbd>. Despliegue el arbol de **Áreas de flujo 2D** (2D Flow Areas) y seleccione **Perímetros** (Perimeters). Utilizando la barra de dibujo podrá trazar manualmente el perímetro 2D de la zona de estudio.

<div align="center">
<img alt="Mesh" src="Screens/Screen2.png" width="70%">
</div>

> El área de flujo 2D también puede ser importada desde un archivo geográfico vectorial. Para esto, en el modo de edición, de clic derecho en **Perimeters** y seleccione **Import Features From Shapefile**. Seleccione el archivo y luego revise todas las propiedades parametrizables para el perímetro importado.

3. Al finalizar podrá visualizar el perímetro trazado en el mapa.

<div align="center">
<img alt="Mesh" src="Screens/Screen3.png" width="70%">
</div>

### Creación y definición de la malla 2D

