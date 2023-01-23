### Cálculo y definición de propiedades hidráulicas y geométricas
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Properties` `Cells` `Hydraulic`

<div align="center">
<img alt="Properties" src="Graph/Properties.png" width="85%">
</div>

### Alcance
En esta clase se presenta el proceso recomendado para el cálculo de las propiedades hidráulicas y geométricas en las celdas y caras de la malla

### Objetivos

* Definir el coeficiente de rugosidad asociado a una capa de cobertura.
* Calcular las tablas de propiedades hidráulicas y geométricas.
* Estudiar las propiedades en celdas y sus caras.
* Trazar la condición de frontera aguas arriba y aguas abajo.

### Requerimientos

* [Sección 1. Introducción y fundamentos](../../Section01/Readme.md)
* [Sección 2. Modelación hidráulica básica](../../Section02/Readme.md)
* [Actividad 13. Manning desde cobertura](../../Section03/Manning/Readme.md)
* [Actividad 17. Creación del MDT](../MDT/Readme.md)

### Cálculo y revisión de las propiedades en la malla

A continuación se presenta el proceso recomendado para el cálculo de diferentes propiedades para las celdas y sus caras como elevación, perímetro hidráulico, área hidráulica, coeficiente de rugosidad, entre otras:

1. Siga los pasos sugeridos para el cargue de información de cobertura de suelo y creación de mapa de coeficientes Manning, presentado en la [Actividad 13](../../Section03/Manning/Readme.md). Revise la asociación de la capa con la geometría 2D, dando clic derecho en el **Geometries** y seleccionando **Manage Geometry Associations**.

<div align="center">
<img alt="Property" src="Screens/Screen0.png" width="70%">
</div>

3. Manteniendo el modo edición, de clic derecho a **Perímetros** (Perimeters) y luego clic en **Editar las propiedades del área 2D** (Edit 2D Area Properties). Para realizar el cálculo de las propiedades de clic al botón <kbd>Compute Property Tables</kbd>. Finalice y guarde los cambios de edición.

<div align="center">
<img alt="Property" src="Screens/Screen1.png" width="70%">
</div>

2. En el mapa podrá acercarse a cualquier celda (cell) o cara(face) y dar clic derecho sobre esta, luego seleccione **Graficar tabla de propiedades** (Plot Property Table) y a continuación seleccione la propiedad que desee revisar.

* Volume vs. Elevation: Presenta una gráfica y tabla con el cálculo del volumen almacenado desde el punto más bajo hasta el punto más alto de la celda a partir de las elevaciones del modelo de terreno.
* Face - Profile: Perfil de terreno en la cara de la celda seleccionada.
* Area vs. Elevation: Corresponde al área hidráulica en función de la elevación.
* Manning vs. Elevation: Corresponde al coeficiente ed rugosidad de Manning (n) en función de la elevación. 
* Conveyance vs. Elevation: Corresponde a la capacidad de transporte en función del cambio de pendiente a partir de los diferentes valores de elevación presentes en la cara de la celda.
   
<div align="center">
<img alt="Property" src="Screens/Screen2.png" width="70%">
<img alt="Property" src="Screens/Screen3.png" width="70%">
</div>

### Condiciones de frontera

La localización espacial de dos diferentes condiciones de frontera (BC – Boundary Condition Line), no debe ser definida sobre una misma celda de la malla. Múltiples condiciones de frontera pueden ser agregadas a la malla compuesta. Se pueden asociar múltiples hidrogramas de entrada, por ejemplo, en el cauce principal y los cauces laterales. 

Para la modelación, por lo menos se debe ingresar una línea de condición de frontera aguas arriba y otra aguas abajo. Las líneas de condición de frontera pueden ser trazadas interna o externamente. Por ejemplo, el flujo base o flujo subterráneo puede ser definido en cualquier zona interna del modelo. Las líneas BC podrán ser dibujadas o importadas usando un archivo de formas (shapefile). Se recomienda importar estas líneas cuando se trate de elementos no rectos como vertederos circulares o curvos.

A continuación se presenta el proceso recomendado para trazar las líneas para condiciones de frontera:

1. 