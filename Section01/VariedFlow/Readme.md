## Flujo uniforme y variado en condición permanente
Keywords: `Hydraulics` ` Open Channel flow` `Manning` `FGV (GVF)` `FRV (RVF)`

<div align="center">

![ChannelFlow.jpeg](https://github.com/juanrodace/J.HRAS/blob/main/Section01/VariedFlow/Graph/ChannelFlow.jpg)
</div>

> En la ilustración, canal en hidroeléctrica de Colombia. _Fuente anónima_.

### Alcance

El flujo en canales a superficie libre también se clasifica como uniforme (FU) o variado, dependiendo del cambio o no de la profundidad del flujo `y` a lo largo del canal. Así mismo, los flujos variados se clasifican en flujo de rápidamente variado (FRV) y flujo gradualmente variado (FGV). En esta clase se revisan los conceptos particulares del flujo uniforme, gradualmente variado y rápidamente variado en un sistema de flujo a superficie libre en condiciones permanentes.

### Objetivos

* Comprender las características del flujo uniforme en condición permanente.
* Analizar las características del flujo gradualmente variado.
* Estudiar los conceptos del flujo rápidamente variado.

### Requerimientos

* Conocimientos en mecánica de fluidos.
* Microsoft Excel
* Python (Opcional)

### Flujo uniforme

Se dice que un sistema a superficie libre se encuentra en condición de flujo uniforme y permanente cuando sus propiedades permanecen constantes a lo largo del canal. Específicamente, cuando la profundidad de flujo `y`, la velocidad media `V` y el flujo o caudal `Q` permanecen constantes en todas las secciones. Así mismo, se afirma que las pendientes de su superficie libre `Sw`, su línea de energía `Se` y su fondo `So` son iguales, es decir, son líneas paralelas. 

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/VariedFlow/Graph/UniformFlow.png" width="65%">
</div>

> Flujo uniforme en canal a superficie libre. _Tomado de Fig.2.1.[^1]

Esta condición de flujo estrictamente uniforme es muy difícil de encontrar y casi imposible en canales naturales. Este flujo ses puede encontrar en canales largos y rectos con una pendiente y
sección transversal constantes y un revestimiento de las superficies homogéneo.

La profundidad del flujo en flujos uniformes se le llama profundidad normal `Yn`. El flujo permanecerá en la condición uniforme mientras la pendiente `So`, el área de la sección `A` y la rugosidad del canal no tengan algún cambio. 

#### Establecimiento

Desde el punto de vista dinámico, el establecimiento del flujo uniforme será posible cuando las fuerzas gravitacionales y las fuerzas de resistencia al flujo encuentren un equilibrio. Dicha resistencia se relaciona con los esfuerzos de corte los cuales dependen de la velocidad.  Si al inicio o al final de un canal no se encuentra este equilibrio, se presentará una aceleración o desaceleración del flujo, aumentando o reduciendo su velocidad y consecuentemente su resistencia de manera gradual, hasta encontrar el balance entre las fuerzas y, por lo tanto, el flujo uniforme. En este sentido, se puede llegar una expresión matemática que representa el flujo uniforme como la relación entre el esfuerzo de corte `τ`, el peso específico `γ`, el radio hidráulico `R` y la pendiente del canal `So`.

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/VariedFlow/Equations/UniformFlow.png" width="20%">
</div>

#### Ecuación de Manning

En 1889 el ingeniero irlandés Robert Manning presentó esta ecuación, la cual es la más utilizada para cálculos de flujo en canales a superficie libre.

<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/VariedFlow/Equations/Manning.png" width="20%"><br>
<sub>Donde, <b>V</b> es la velocidad media del flujo, <b>n</b> corresponde al coeficiente de rugosidad o de Manning,<br>
<b>R</b> es el radio hidráulico de la sección transversal (relación de área y perímetro, A/P) <br>
y <b>S<sub>o</sub></b> es la pendiente del fondo del canal.</sub><br><br>
</div>

La mayor dificultad en la aplicación de la ecuación, está en la definición del coeficiente `n`. Para su determinación, Ven T. Chow[^2] recomienda tener en cuenta las siguientes consideraciones: 
- Entender los factores que afectan su valor.
- Consultar una tabla de valores comunes para canales de diferentes tipos.
- Examinar y familiarizarse con la apariencia de algunos canales comunes con coeficientes conocidos.
- Determinar el valor de **n** mediante un proceso analítico basado en la distribución de velocidades en la sección y datos medidos de velocidad y rugosidad.

Como referencia para la definición del coeficiente **n**, se recomienda consultar la tabla de coeficientes de rugosidad de Chow[^2], el cual considera varios tipos de canal con descripción y algunos valores generalmente recomendados para el diseño. Y la [Guía](https://github.com/juanrodace/J.HRAS/blob/main/.refs/Guide%20for%20selecting%20Manning's%20Roughness%20Coef.%20USGS.%20P2339..pdf)[^3] o [Reporte](https://github.com/juanrodace/J.HRAS/blob/main/.refs/Roughness%20Characteristics%20of%20Natural%20Channels.%20USGS.pdf)[^4] del USGS. 

Como material adicional, puedes acceder al siguiente video de la USGS sobre selección del coeficiente de rugosidad. 

<div align="center"><a href="https://www.usgs.gov/media/videos/selection-roughness-coefficients" target="_blank"><img src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/VariedFlow/Graph/IMG_USGS_Clip.png" alt="IMAGE ALT TEXT HERE" width="420" border="10" /></a><sub><br>(https://www.usgs.gov/media/videos/selection-roughness-coefficients)</sub><br><br></div>

### Flujo gradualmente variado

El movimiento o flujo gradualmente variado (FGV), es aquel en el cual hay un cambio suave en la profundidad de flujo a lo largo del canal, y consecuentemente, un cambio en su velocidad. A diferencia del flujo uniforme, las pendientes de energía, flujo y fondo serán diferentes. Esta es una condición mucho más aproximada al flujo a superficie libre en canales naturales y artificiales, considerando los posibles cambios de sección, pendiente, rugosidad y alineamiento. El remanso producido por una presa o vertedero a través de un canal o rio y la caída producida por una caída o desnivel repentino son algunos ejemplos típicos de FGV.

El análisis del FGV parte dos supuestos básicos:
- La pérdida de carga en una sección es la misma que correspondería a un flujo uniforme con la misma velocidad y radio hidráulico que la sección mencionada. Esto quiere decir que, la ecuación de Manning puede usarse para la estimación de la línea de energía en un perfil de FGV, con la condición de que el término de pendiente que se utiliza sea la pendiente de energía y no la pendiente del fondo. 
- La distribución de presiones en cada sección es hidrostática, al considerar que los cambios en la superficie libre y fondo son graduales, dando lugar a aceleraciones normales insignificantes. 
 
<div align="center">
<img alt="J.HRAS" src="https://github.com/juanrodace/J.HRAS/blob/main/Section01/VariedFlow/Graph/FGV.png" width="65%">
</div>

> Flujo gradualmente variado en un canal a superficie libre. _Tomado de Fig.8.6._[^1]

#### Ecuación dinámica del FGV

Para establecer esta ecuación, partimos de la imagen previa y la ecuación de energía en un tramo <kbd>dx</kbd> de canal a superficie libre con FGV: **$H=z+y+\frac{V^{2}}{2g}$**. Se evalúa la variación de la energía total en el espacio <kbd>dx</kbd> y considerando las definiciones de la pendiente del fondo $S_{0}=\frac{dz}{dx}$ y la pendiente de la línea de energía $S_{E}=\frac{dH}{dx}$, para posteriormente despejar la variación del perfil de flujo en el espacio $S_{W}=\frac{dy}{dx}$, obteniendo la siguiente ecuación.

#### Características de los perfiles

### Flujo rápidamente variado

### Referencias
- Fluid mechanics. Fundamentals and Applications.. Cengel Y., Cimbala J. McGraw-Hill.2006.
- Introduction to fluid mechanics. Fox and McDonald's. 8th Ed., Jhon Wilwy & Sons, Inc. 2011. 
- The hydraulics of Channel Flow: An Introduction. Chanson H. 2nd Ed.,Elsevier Butterworth-Heinemann. 2004.
- Open channel Hydraulics. Chow, Ven Te. 2nd Ed., Blackburn Press. 2009.
- Flow in open channels. Subramanya K. 3th Ed., Tata McGraw-Hill Publishing. 2009. 


### Control de versiones


| Versión    | Descripción                                                       |                    Autor                    | Horas |
|------------|-------------------------------------------------------------------|:-------------------------------------------:|:-----:|
| 2022.08.17 | Versión inicial con definición de estructura general y contenido. | [juanrodace](https://github.com/juanrodace) |  1.0  |
| 2022.08.20 | Inclusión de conceptos y diagramas.                               | [juanrodace](https://github.com/juanrodace) |  2.0  |
| 2022.08.23 | Inclusión de conceptos y diagramas.                               | [juanrodace](https://github.com/juanrodace) |  1.0  | 
| 2022.08.25 | Inclusión de conceptos y diagramas.                               | [juanrodace](https://github.com/juanrodace) |  1.0  |

### Licencia, cláusulas y condiciones de uso

| [:arrow_backward:Anterior](https://github.com/juanrodace/J.HRAS/tree/main/Section01/FundamentalConcepts) | [:house: Inicio](https://github.com/juanrodace/J.HRAS/wiki) | [:beginner: Ayuda/Colabora](https://github.com/juanrodace/J.HRAS/discussions/3) | [Siguiente:arrow_forward:](https://github.com/juanrodace/J.HRAS/tree/main/Section01/UnstadyFlow) |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|

_J.HRAS es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/juanrodace/J.HRAS/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [juanrodace](https://github.com/juanrodace) en GitHub._

[^1]: Hidráulica de tuberías y canales. Rocha Arturo.
[^2]: Open channel Hydraulics. Chow, Ven Te. 2nd Ed., Blackburn Press. 2009.
[^3]: [Guide for selecting Manning's roughness coefficients for natural channels and flood plains. Paper 2339. USGS.](https://pubs.usgs.gov/wsp/2339/report.pdf)
[^4]: [Roughness Characteristics of Natural Channels. Paper 1849. USGS.](https://pubs.usgs.gov/wsp/wsp_1849/pdf/wsp_1849.pdf)
