### Modelación hidráulica bidimensional 2D
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Unsteady` `Hydraulic`

<div align="center">
<img alt="SF2D" src="Graph/Simulation2D.png" width="85%">
</div>

### Alcance
En esta clase se presenta el proceso recomendado para la definición de datos y condiciones de frontera y la simulación bidimensional (2D) en condición de flujo no permanente.

### Objetivos

* Definir información de flujo y condiciones de frontera.
* Configuración del plan de simulación.
* Simulación hidráulica bidimensional.

### Requerimientos

* [Sección 1. Introducción y fundamentos](../../Section01/Readme.md)
* [Sección 2. Modelación hidráulica básica](../../Section02/Readme.md)

### Información de flujo y condiciones de frontera

1. Para iniciar, vamos a ingresar a la ventana de **Información de flujo permanente (Steady flow data)**. En la ventana emergente, seleccione **Archivo → Nuevo/Guardar información de flujo no permanente** (File → New/Save unsteady flow data) e ingrese el nombre que desee asignarle a la información del flujo y de clic en el botón <kbd>**OK**</kbd>.

<div align="center">
<img alt="S2D" src="Screens/Screen1.png" width="60%">
<img alt="S2D" src="Screens/Screen2.png" width="60%">
</div>

2. En la ventana de **Información de flujo no permanente** (Unsteady flow data), podrá ingresar una descripción de la información de flujo, así como definir las condiciones de frontera, condiciones iniciales y agregar información metereológica u observada en el sistema a modelar. Para este ejercicio, agregaremos un hidrograma de flujo aguas arriba del canal (BC Upstream 1) y definiremos flujo uniforme en la sección aguas abajo (BC Downstream 1). Una vez ingrese toda la información de clic en el botón <kbd>**Apply Data**</kbd> que encontrará en la parte superior derecha de la ventana. Finalmente, seleccione <kbd>**Plot Data**</kbd> para verificar y revisar el cargue de la información.  Recuerde guardar los cambios realizados a las características del flujo y condiciones hidráulicas

<div align="center">
<img alt="S2D" src="Screens/Screen3.png" width="60%">
<img alt="S2D" src="Screens/Screen4.png" width="70%">
</div>

> Recuerde que en el caso de los hidrogramas o curvas de estación-flujo, deberá definir correctamente los tiempos de inicio y fin del hidrograma, así como el intervalo de tiempo y la pendiente de la línea de energía (EG slope for distributing flow). 

> _Nota: Si desea evaluar diferentes periodos de retorno, deberá crear un archivo de información de flujo no permanente para cada periodo de retorno.._

### Plan de simulación y simulación

1. 