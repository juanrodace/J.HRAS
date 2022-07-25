## Conceptos básicos
Keywords: `Hydraulics` `Channel` `Channel flow` `Continuity equation` `Energy equation` `Manning` `FGV (GVF)`

_Explicación general de conceptos requeridos para entender el flujo a superficie libre, en condición permanente y no permanente._

<div align="center">

![OpenChannelFlow.jpg](https://github.com/juanrodace/J.HRAS/blob/main/Section01/FundamentalConcepts/Graph/OpenChannelFlow.jpg)
</div>

> En la ilustración, perfil de flujo en canal a superficie libre.
___

### Objetivos

* Estudiar las características de un canal a superficie libre.
* Estudiar los conceptos básicos del flujo a superficie libre.
* Calcular la profundidad crítica en un canal a superficie libre.
* Calcular el caudal en un canal regular en condiciones de flujo uniforme.
* Calcular diferentes parámetros asociados a un canal regular en condiciones de flujo permanente.
* Analizar las características del flujo gradualmente variado.
* Estudiar los conceptos del flujo no permanente en canales.

> Se incluye actividad para estimación de parámetros. 
> Estudiantes que aplicaron para curso certificado, desarrollan su propia hoja de calculo o script python .

### Requerimientos

* Conocimientos en mecánica de fluidos.
* Microsoft Excel
* Python (Opcional)

___

### Flujo a superficie libre

El flujo a superficie libre implica que el fluido está expuesto a la atmósfera, esto puede darse en un canal abierto o en un conducto cuyo líquido no ocupa la sección por completo, y, por lo tanto, hay una superficie libre. Este flujo se distingue del flujo en tuberías o conductos cerrados a presión, los cuales permiten el transporte de liquidos y gases. Sin embargo, el flujo a superficie libre implica la existencia de una interfaz líquido-gas. El flujo en tuberías se conduce por una diferencia de presión, mientras que el flujo a superficie libre se conduce de manera natural por gravedad. El flujo del agua en un río, por ejemplo, se conduce por la diferencia de elevación entre río corriente arriba y río corriente abajo. La razón de flujo en un canal a superficie libre está establecida por el balance dinámico entre gravedad y fricción. [^1]

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/FundamentalConcepts/Graph/NaturalChannel_Animas.jpeg" width="75%">
</div>

>  En la ilustración, Arroyo Las Ánimas, Cesar, Col. _Fuente propia_.

 La mayoría de los flujos naturales encontrados en la práctica, como los de agua en riachuelos, ríos e inundaciones además de cunetas a los lados de carreteras, estacionamientos o techos, son también flujos en canales abiertos. Los sistemas de flujo en canal abierto hechos por el hombre incluyen sistemas de irrigación, alcantarillas, desagües y cunetas.

### Distribución de velocidades

En un canal a superficie libre, la velocidad del flujo es cero sobre las superficies laterales y en el fondo del canal debido a la condición de no deslizamiento, y máxima ocurre abajo de la superficie libre en algún lugar entre 25% de profundidad como se muestra en la figura. Además, la velocidad varía en la dirección del flujo varía en la en la mayoría de los casos. Por lo tanto, la distribución de la velocidad (y en consecuencia el flujo) en canales es en general tridimensional. Ahora bien, en la práctica de la ingeniería las ecuaciones se trabajan en términos de la velocidad media en secciones transversales del canal. Debido a que la velocidad media varía solamente en la durección del flujo. Esta hipótesis de unidimensionalidad hace posible resolver problemas importantes de la vida real de manera simple, precisa y aplicada comúnmente en la práctica. [^1]

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/FundamentalConcepts/Graph/VelocityChannelSections.png" width="70%">
</div>

> Distribución típica de velocidad en secciones de canal abierto.[^2].

La distribución de velocidades en una sección de canal depende también de otros factores, como una forma inusual de la sección, la rugosidad del canal y la presencia de curvas. En una corriente ancha, rápida y poco profunda o en un canal muy liso, la velocidad máxima por lo general se encuentra en la superficie libre. La rugosidad del canal causa un incremento en la curvatura del perfil vertical de velocidades.

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/FundamentalConcepts/Graph/VelocityProfile.png" width="70%">
</div>

> Distribución típica del perfil de velocidades en canal a superficie libre.[^3].

### Elementos geométricos de la sección transversal

Los canales pueden ser naturales o artificiales. Un canal que tiene la misma sección transversal y la misma pendiente de fondo se denomina canal prismático, mientras que un canal que tiene una sección transversal y/o pendiente variable se denomina canal no prismático. Un canal largo puede estar compuesto por varios canales regulares. Una sección transversal normal a la dirección del flujo se denomina **sección del canal**. Las secciones de canales naturales son, por lo general, muy irregulares y pueden constar de una sección principal y una o más secciones laterales. Los canales artificiales, suelen ser diseñados con seccione de figuras geométricas regulares, más comunmente trapezoidales, cuadrados o triangulares. La sección cerradas, por lo general cirulares, son usadas en alcantarillados y estructuras de paso (culverts).  

Los **elementos geométricos** son propiedades de una sección de canal que pueden ser definidos por completo por la geometría de la sección y la profundidad de flujo. La **profundidad de flujo**, _'y'_, en una sección es la distancia vertical desde el punto más bajo de la sección del canal hasta la superficie libre. La **profundidad de flujo de la sección**, _'d'_, es la profundidad de flujo normal o perpendicular a la dirección del flujo. El **ancho superficial**, _T_, es el ancho de la sección del canal en la superficie libre. El **área de flujo** o área mojada, _'A'_, es el área de la sección transversal del canal normal a la dirección del flujo. El **perímetro mojado** o perímetro hidráulico, _'P'_ se define como la longitud de la línea de intersección de la superficie mojada del canal con un plano transversal perpendicular a la dirección del flujo. El **radio hidráulico**, _'R'_, es la relación del área (A) y el perímetro mojado (P). la **profundidad hidráulica**, _'D'_, es la relación entre el área mojada (A) y el ancho superficial (T). Y el **factor de sección** para la estimación del flujo crítico,_'Z'_, se definen como el producto del área (A) y la raíz cuadrada de la profundidad hidráulica (D).

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/FundamentalConcepts/Graph/GeometricPropierties.png" width="70%">
</div>

> Propiedades geométricas comunes en canales a superficie libre.[^2].

Para secciones de canal regulares y simples, los elementos geométricos pueden expresarse mateméticamente en terminos de la profundidad de flujo y de otras dimensiones de la sección. Para el caso de secciones complicadas y secciones naturales (irregulares), no se puede escribir una expresión algebráica simple, pero pueden prepararse curvas que representen la relación entre estos elementos y la profundidad de flujo. 


### Tipos de flujo y clasificación

En el movimiento o dinámica de los fluidos existes diferentes clasificaciones en función de sus variables y características. A continuación revisamos de forma general estas clasificaciones.

#### Flujo permanente y no permanente

#### Flujo laminar y turbulento

#### Flujo crítico, subcrítico y supercrítico

| Número de Froude  | Tipo de flujo        |
|-------------------|----------------------|
| menor a 1         | Subcrítco            |
| igual a 1         | Crítico              |
| mayor a 1         | Supercritico         |

### Ecuaciones fundamentales en flujo a superficie libre

Las  

#### Continuidad

#### Conservación de la energía

#### Conservación del momentum

### Energía específica

### Fuerza específica

### Profundidad crítica

### Flujo uniforme

#### Ecuación de Manning

### Flujo gradualmente variado

### Flujo no permanente


### Autores

* Creado por ing.juanrodace@gmail.com (3 horas)


### Compatibilidad

* Esta actividad puede ser desarrollada .......

> Las herramientas computacionales requeridas, librerías, complementos y sus versiones son especificadas en cada actividad del curso.


### Control de versiones


| Versión    | Descripción                                                                                                                     |
|------------|---------------------------------------------------------------------------------------------------------------------------------|
| 2022.07.19 | Creación estructura general y contenido. |
| 2022.07.25 | Inclusión de conceptos: flujo superficie libre, distribución velocidades, características y elementos geométricos.              |


### Licencia, cláusulas y condiciones de uso

J.HRAS es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/juanrodace/J.HRAS/wiki/License).


| [Actividad anterior](https://github.com/juanrodace/J.HRAS/tree/main/Section01/Introduction) | [Inicio](https://github.com/juanrodace/J.HRAS/wiki) | [Actividad siguiente](https://github.com/juanrodace/J.HRAS/tree/main/Section01/HydraulicModeling) |
|------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_


[^1]: Mecánica de fluidos, fundamentos y aplicaciones. Cengel Y., Cimbala J. McGraw-Hill.2006.
[^2]: Introduction to Fluid Mechanics. Fox and McDonald's. 8th Ed., Jhon Wilwy & Sons, Inc. 2011. 
[^3]: The Hydraulics of Channel Flow: An Introdution. Chanson H. 2nd Ed.,Elsevier Butterworth-Heinemann. 2004. _(Fig.1.2.)_
[^4]:
[^5]:
[^6]:
[^7]:

Hidráulica de tuberías y canales. Rocha Arturo. 