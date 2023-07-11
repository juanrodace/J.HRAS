<div align="center"><a href="https://www.escuelaing.edu.co/es/investigacion-e-innovacion/centro-de-estudios-hidraulicos/" target="_blank"><img src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/CaseUse/.icons/IconCEHBanner.jpg" alt="J.HRAS" width="100%" border="0" /></a></div>

# Estructuras
Keywords: `Hydraulics` `HEC-RAS` `Structures` `Bridge` `Culvert` `Dams` `Weirs` `Spillways` 

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
    <a href="https://youtu.be/7mn0G_ZEws8">
        <img src="../../.icons/Inicio_Actividad.png" alt="IMAGE ALT TEXT HERE" width="800"/>
    </a>Video Actividad - Parte 1
</div>

##

<div align="center">
<img alt="Structures" src="Graph/Structures.jpg" width="85%">
</div>

### Alcance
En esta clase se presentan la inclusión de diferentes estructuras en el sistema hidráulico a modelar como puentes, pontones, alcantarillas, presas, vertederos, entre otros.

### Objetivos

* Conocer la definición y edición de puentes en el modelo.
* Conocer la definición y edición de alcantarillas en el modelo.
* Conocer la definición y edición de estructuras longitudinales en el modelo.
* Conocer la definición y edición de estructuras laterales en el modelo.

### Requerimientos

* [**Sección 2. Modelación hidráulica básica**](../../Section02/Readme.md)

### Estructuras en el sistema hidráulico

A continuación se describen los pasos sugeridos para la definición y simulación de los diferentes tipos de estructura en el modelo hidráulico.

#### Estructuras transversales. Puentes y alcantarillas.

1. Para iniciar, en la ventana de edición geométrica seleccionamos el ícono <img alt="Structures" src="Graph/Bridge_Icon.png" width="4%">. Se desplegará la ventana de creación y edición de estructuras transversales de puentes y alcantarillas. Allí se debe ir al menú **Opciones → Agregar puente y/o alcantarilla** (Options → Add a bridge and/or culvert). 

A continuación, ingrese el número de la estación en la cual desea crear la estructura. En la ventana de edición e información aparecerán las secciones aguas arriba y aguas abajo de la estructura.

<div align="center">
<img alt="Structures" src="Screens/Screen1.png" width="60%">
</div>

2. Para definir la geometría del puente o alcantarilla de clic en el botón <kbd>**Deck/Roadway**</kbd>. Se desplegará una ventana en la que puede definir dimensiones y características del puente o paso de vía como son: distancia a la sección transversal, ancho de la estructura, coeficiente de vertido, geometría (estación y alturas), taludes aguas arriba y aguas abajo e información en caso de que la estructura trabaje como vertedero.

Igualmente, para el caso de los puentes, al dar clic en el botón <kbd>**Pier**</kbd> o *"Pila"*, se abrirá la ventana para definir, si es el caso, la información de las pilas del puente. Acá podrá definir la geometría, ubicación y cantidad de pilas del puente. Al dar clic en el botón <kbd>OK</kbd>, se podrá visualizar el esquema de la estructura en las secciones aguas arriba y aguas abajo de esta. 

<div align="center">
<img alt="Structures" src="Screens/Screen2.png" width="60%">
</div>

3. A continuación, podemos ingresar los datos de cálculo de la estructura, dando clic en el botón <kbd>**Bridge Modeling Approach**</kbd>. Se desplegará una ventana en la cual podrá definir los métodos de cálculo de la estructura tanto por encima como por debajo de esta (High Flow y Low Flow respectivamente).

<div align="center">
<img alt="Structures" src="Screens/Screen3.png" width="40%">
</div>

4. Una vez finalizada la definición, en el editor de geometría podrá observar la estructura creada en planta. 

<div align="center">
<img alt="Structures" src="Screens/Screen4.png" width="60%">
</div>

5. Para el caso de la alcantarilla, primero se debe definir la geometría general de estructura o cubierta del paso de vía mediante el botón <kbd>**Deck/Roadway**</kbd>, como se indicó en el paso 2. Posteriormente dando clic al botón <kbd>**Culvert**</kbd>, se desplegará la ventana de edición para ingresar la información de la(s) alcantarilla(s). En esta ventana se podrá definir: tipo, forma y material de la alcantarilla, geometría y dimensiones, distancia aguas arriba, longitud total, coeficientes de pérdida, coeficiente 'n' de Manning, cantidad y ubicación.  Al dar clic en el botón <kbd>OK</kbd>, se podrá visualizar el esquema de la estructura en las secciones aguas arriba y aguas abajo de esta.
 
<div align="center">
<img alt="Structures" src="Screens/Screen5.png" width="60%">
</div>

6. Una vez más, al finalizar la definición, en el editor de geometría podrá observar la estructura creada en planta.

<div align="center">
<img alt="Structures" src="Screens/Screen6.png" width="60%">
</div>

7. Luego de crear la estructura, puede realizar la simulación (de flujo permanente o no permanente) y posteriormente visualizar los resultados.

<div align="center">
<img alt="Structures" src="Screens/Screen7.png" width="60%">
<img alt="Structures" src="Screens/Screen8.png" width="60%">
</div>

##
<div align="center">
    <a href="https://youtu.be/7mn0G_ZEws8">
        <img src="../../.icons/Inicio_Actividad.png" alt="IMAGE ALT TEXT HERE" width="800"/>
    </a> Video Actividad - Parte 2
</div>
##

#### Estructuras en el canal. Presas, vertederos, compuertas, orificios y alcantarillas.

1. Para iniciar, en la ventana de edición geométrica seleccionamos el ícono <img alt="Structures" src="Graph/Inline_Icon.png" width="4%">. Se desplegará la ventana de creación y edición de estructuras en línea o sobre el canal. Allí debe ir al menú **Opciones → Agregar estructura en el canal** (Options → Add a inline structure). 

A continuación, ingrese el número de la estación en la cual desea crear la estructura. En la ventana de edición e información aparecerán la sección aguas arriba de la estructura.

<div align="center">
<img alt="Structures" src="Screens/Screen9.png" width="60%">
</div>

2. Para definir la geometría de la presa o vertedero de clic en el botón <kbd>**Weir/Embankment**</kbd>. Se desplegará una ventana en la que puede definir dimensiones y características de la estructura como son: distancia a la sección transversal, ancho de la estructura, coeficiente de vertido, geometría (estación y alturas), taludes aguas arriba y aguas abajo e información de la forma y coeficientes del vertedero.  Al dar clic en el botón <kbd>OK</kbd>, se podrá visualizar el esquema de la estructura.

<div align="center">
<img alt="Structures" src="Screens/Screen10.png" width="60%">
</div>

3. Si la estructura tiene compuertas, se podrán definir dando clic al botón <kbd>**Gate**</kbd>, donde se desplegará la ventana de edición para ingresar la información de la(s) compuerta(s). En esta ventana se podrá definir: tipo y forma, datos de flujo, coeficientes, geometría, cantidad y ubicación. Al dar clic en el botón <kbd>OK</kbd>, se podrá visualizar el esquema de la estructura en las secciones aguas arriba y aguas abajo de esta.

<div align="center">
<img alt="Structures" src="Screens/Screen11.png" width="60%">
</div>

>**Nota:** Es importante tener en cuenta que al definir compuertas dentro de la estructura en el canal, se deben definir condiciones hidráulicas y de frontera en la ventana de información del flujo (permanente o no permanente) como se muestra a continuación.

<div align="center">
<img alt="Structures" src="Screens/Screen17.png" width="100%">
</div>

4. Si la estructura tiene alcantarillas o tuberías, se podrán definir dando clic al botón <kbd>**Gate**</kbd>, donde se desplegará la ventana de edición para ingresar la información de la(s) alcantarillas(s), igual que en la definición de puentes o pasos de vía. En esta ventana se podrá definir:tipo, forma y material de la alcantarilla, geometría y dimensiones, distancia aguas arriba, longitud total, coeficientes de pérdida, coeficiente 'n' de Manning, cantidad y ubicación.  Al dar clic en el botón <kbd>OK</kbd>, se podrá visualizar el esquema de la estructura en las secciones aguas arriba y aguas abajo de esta.

<div align="center">
<img alt="Structures" src="Screens/Screen12.png" width="60%">
</div>

#### Estructuras laterales. Vertederos, compuertas, orificios y alcantarillas.

1.  Para iniciar, en la ventana de edición geométrica seleccionamos el ícono <img alt="Structures" src="Graph/Lateral_Icon.png" width="4%">. Se desplegará la ventana de creación y edición de estructuras laterales. Allí debe ir al menú **Opciones → Agregar estructura lateral** (Options → Add a lateral structure). 

<div align="center">
<img alt="Structures" src="Screens/Screen13.png" width="60%">
</div>

A continuación, ingrese el número de la estación en la cual desea crear la estructura. En la ventana de edición e información podrá agregar una descripción, definir la posición de la estructura y definir el tipo de conexión.

<div align="center">
<img alt="Structures" src="Screens/Screen14.png" width="60%">
</div>

2. Para definir la geometría de la presa o vertedero lateral, de clic en el botón <kbd>**Weir/Embankment**</kbd>. Se desplegará una ventana en la que puede definir dimensiones y características de la estructura como son: ancho, método y ecuaciones de cálculo, forma de la cresta, distancia a la sección aguas arriba y geometría (estación, elevación).  Al dar clic en el botón <kbd>OK</kbd>, se podrá visualizar el esquema de la estructura definida.

<div align="center">
<img alt="Structures" src="Screens/Screen15.png" width="60%">
</div>

En la ventana de edición geométrica, también podrá visualizar la estructura en planta.

<div align="center">
<img alt="Structures" src="Screens/Screen16.png" width="60%">
</div>

3. Si la estructura tiene compuertas, se podrán definir dando clic al botón <kbd>**Gate**</kbd>, donde se desplegará la ventana de edición para ingresar la información de la(s) compuerta(s). En esta ventana se podrá definir: tipo y forma, datos de flujo, coeficientes, geometría, cantidad y ubicación. Al dar clic en el botón <kbd>OK</kbd>, se podrá visualizar el esquema de la estructura en las secciones aguas arriba y aguas abajo de esta.

<div align="center">
<img alt="Structures" src="Screens/Screen16A.png" width="50%">
</div>

>**Nota:** Es importante tener en cuenta que al definir compuertas dentro de la estructura en el canal, se deben definir condiciones hidráulicas y de frontera en la ventana de información del flujo (permanente o no permanente) como se muestra a continuación.

<div align="center">
<img alt="Structures" src="Screens/Screen17.png" width="100%">
</div>

4. Si la estructura tiene alcantarillas o tuberías, se podrán definir dando clic al botón <kbd>**Gate**</kbd>, donde se desplegará la ventana de edición para ingresar la información de la(s) alcantarillas(s), igual que en la definición de puentes o pasos de vía. En esta ventana se podrá definir:tipo, forma y material de la alcantarilla, geometría y dimensiones, distancia aguas arriba, longitud total, coeficientes de pérdida, coeficiente 'n' de Manning, cantidad y ubicación.  Al dar clic en el botón <kbd>OK</kbd>, se podrá visualizar el esquema de la estructura en las secciones aguas arriba y aguas abajo de esta.

<div align="center">
<img alt="Structures" src="Screens/Screen16B.png" width="50%">
</div>

5. Luego de crear la(s) estructura(s), puede realizar la simulación (de flujo permanente o no permanente) y posteriormente visualizar los resultados.

<div align="center">
<img alt="Structures" src="Screens/Screen18.png" width="60%">
<img alt="Structures" src="Screens/Screen19.png" width="60%">
<img alt="Structures" src="Screens/Screen20.png" width="60%">
</div>

### Referencias
- [HEC-RAS User’s Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/rasum/latest)
- [HEC-RAS Hydraulic Reference Manual.2020](https://www.hec.usace.army.mil/confluence/rasdocs/ras1dtechref/latest)
- [HEC-RAS Documentation. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs)
    
### Control de versiones

| Versión | Descripción                                                       |                    Autor                    | Horas |
|:-------:|-------------------------------------------------------------------|:-------------------------------------------:|:-----:|
| 2023.01 | Versión inicial con definición de estructura general y contenido. | [juanrodace](https://github.com/juanrodace) |  1.0  |
| 2023.01 | Inclusión de conceptos, procedimientos, esquemas y gráficos.      | [juanrodace](https://github.com/juanrodace) |  3.5  |
| 2023.01 | Desarrollo de contenido multimedia.                               | [juanrodace](https://github.com/juanrodace) |  3.5  |

### Licencia, cláusulas y condiciones de uso

| [:arrow_backward:Anterior](../Levees/Readme.md) | [:house: Inicio](../../Readme.md) | [:beginner: Ayuda/Colabora](https://github.com/juanrodace/J.HRAS/discussions/4) | [Siguiente:arrow_forward:](../Scour/Readme.md) |
|-------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------|------------------------------------------------|

_J.HRAS es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/juanrodace/J.HRAS/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [juanrodace](https://github.com/juanrodace) en GitHub._

##

<div align="center"><a href="https://enlace-academico.escuelaing.edu.co/psc/FORMULARIO/EMPLOYEE/SA/c/EC_LOCALIZACION_RE.LC_FRM_ADMEDCO_FL.GBL" target="_blank"><img src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/CaseUse/.icons/IconCEHBannerCertificado.jpg" alt="J.HRAS" width="100%" border="0" /></a></div>

##

<div align="center"><a href="http://www.escuelaing.edu.co" target="_blank"><img src="../../.icons/Banner1.svg" alt="Support by" width="100%" border="0" /></a><sub><br>Este curso guía ha sido desarrollado con el apoyo de la Escuela Colombiana de Ingeniería - Julio Garavito. Encuentra más contenidos en https://github.com/uescuelaing</sub><br><br></div>