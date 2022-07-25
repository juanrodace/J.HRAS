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
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/FundamentalConcepts/Graph/NaturalChannel_Animas.jpeg" width="85%">
</div>

>  En la ilustración, Arroyo Las Ánimas, Cesar, Col. _Fuente propia_.

 La mayoría de los flujos naturales encontrados en la práctica, como los de agua en riachuelos, ríos e inundaciones además de cunetas a los lados de carreteras, estacionamientos o techos, son también flujos en canales abiertos. Los sistemas de flujo en canal abierto hechos por el hombre incluyen sistemas de irrigación, alcantarillas, desagües y cunetas.

### Distribución de velocidades

En un canal a superficie libre, la velocidad del flujo es cero sobre las superficies laterales y en el fondo del canal debido a la condición de no deslizamiento, y máxima ocurre abajo de la superficie libre en algún lugar entre 25% de profundidad como se muestra en la figura. Además, la velocidad varía en la dirección del flujo varía en la en la mayoría de los casos. Por lo tanto, la distribución de la velocidad (y en consecuencia el flujo) en canales es en general tridimensional. [^1]

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/FundamentalConcepts/Graph/VelocityChannelSections.png" width="80%">
</div>

> Distribución típica de velocidad en secciones de canal abierto.[^2].

Ahora bien, en la práctica de la ingeniería las ecuaciones se trabajan en términos de la velocidad media en secciones transversales del canal. Debido a que la velocidad media varía solamente en la durección del flujo. Esta hipótesis de unidimensionalidad hace posible resolver problemas importantes de la vida real de manera simple, precisa y aplicada comúnmente en la práctica.

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/FundamentalConcepts/Graph/VelocityProfile.png" width="80%">
</div>

> Distribución típica del perfil de velocidades en canal a superficie libre.[^3].

### Elementos geométricos de la sección transversal



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