<div align="center">
<br>
<img alt="J.HRAS" src=".icons/0_HRAS.png" width="250px">
<br><b>Modelación hidráulica a superficie libre con HEC-RAS</b><br>
by Juan Rodriguez <a href="https://github.com/juanrodace/"><i>(juanrodace)</i></a><br>
<br></div>

La modelación hidráulica pretende reproducir determinados fenómenos o procesos relacionados con el flujo o transporte del agua. Sus resultados se emplean en el ámbito de la ingeniería para tratar diferentes aspectos, como los relacionados con el transporte y distribución del agua, la intervención de cauces, el desarrollo de estructuras o vías, la hidráulica fluvial, entre otros. Los sistemas computacionales son hoy en día una poderosa herramienta en la modelación numérica, permitiendo reducir el tiempo y mejorar la calidad de los estudios hidráulicos en la ingeniería. HEC-RAS es quizás una de las herramientas más aprobadas y utilizadas desde el punto de vista práctico, ya que además de contar con modelos 1D y 2D, tiene la ventaja de ser un software de libre acceso, volviéndolo muy accesible por los diferentes usuarios a través de todo el mundo.

En este curso, la Universidad Escuela Colombiana de Ingeniería ofrece la formación necesaria para realizar estos modelos de canales artificiales y/o cauces naturales empleando el programa de HEC-RAS desarrollado por el Centro de Ingeniería Hidrológica (HEC) del US Army Corps of Engineers (USACE). Este software permite desarrollar modelos de flujo a superficie libre en condición permanente y no permanente, unidimensional y bidimensional, inclusión de obras hidráulicas, gestión del riesgo, determinación de áreas de inundación, modelos con transporte de sedimentos y socavación y modelado de calidad.

## Dirigido a

Entidades públicas, empresas prestadoras de servicios, autoridades ambientales, privados, profesionales y/o estudiantes en Ingeniería Civil, Ingeniería Sanitaria y Ambiental, personal que labore áreas de consultoría en la Gestión del Riesgo, en el sector de agua y obras hidráulicas y el modelamiento de inundaciones como herramienta de planificación para el ordenamiento del territorio.

## Objetivos

Es este curso aprenderá a conocimientos mínimos acerca de la modelación hidráulica y aquellos necesarios para el manejo del software de simulación hidráulica HEC-RAS tanto unidimensional como bidimensional en condición de flujo permanente y no permanente, de forma que sea capaz de aplicarlo en la resolución de casos prácticos relacionados con la ingeniería fluvial y de canales abiertos a nivel local, regional y global.

- Entender los conceptos básicos de una modelación hidráulica.
- Comprender las características generales de funcionamiento del software HEC-RAS.
- Aprender las principales funciones de integración de las características geométricas, topográficas, físicas e hidráulicas de un modelo.
- Utilizar la herramienta HEC-RAS para el desarrollo de modelos hidráulicos unidimensionales y bidimensional en condición de flujo permanente y no permanente.
- Aplicar la herramienta de modelación HEC-RAS en solución de casos prácticos de ingeniería.

## Resultados de aprendizaje

- Comprende y explica los conceptos fundamentales del transporte de fluidos en sistemas a superficie libre. 
- Identifica las características de un estudio hidráulico, la modelación de sistemas hidráulicos y sus condiciones de frontera.
- Evalúa y carga la información geométrica y/o topográfica para la modelación de un sistema hidráulico a superficie libre en el software HEC-RAS. 
- Define las condiciones hidráulicas de un modelo unidimensional y bidimensional en flujo permanente y no permanente en la herramienta HEC-RAS.
- Usa e incorpora características avanzadas en la modelación hidráulica HEC-RAS como estructuras de paso, diques, cobertura de suelo, confluencias, y estimación de la socavación.
- Analiza y resuelve problemas prácticos en HEC-RAS de sistemas de transporte a superficie libre, con sus diferentes controles y características de flujo, así como posibles estructuras y alteraciones geométricas.

## Metodología

El curso virtual tendrá un enfoque teórico-práctico. La parte teórica comprende videos y presentaciones de forma tal que se abarcan con rigor y reflexión los conceptos básicos y fundamentales sobre HEC-RAS; y como parte del componente práctico, se desarrollarán ejemplos de modelación y ejecuciones del modelo.

* Se revisan los procesos de métodos básicos de creación de modelos hidráulicos, incluyendo en cada tema ejercicios resueltos paso a paso. Tanto los fundamentos como las prácticas con HEC-RAS están explicados en documentos de texto, presentaciones, y videotutoriales, planificados con una complejidad progresiva. 
* El material multimedia está disponible en un repositorio GitHub con videos asociados a la plataforma YouTube, al que cada alumno puede acceder libremente.
* El aprendizaje es remoto, y, por lo tanto, resulta compatible con su actividad diaria: el alumno hace el curso a su ritmo, siguiendo su mejor horario. 
* Es posible contar con acompañamiento y certificación del curso, para esto consulta la página de la [Escuela](https://www.escuelaing.edu.co). Para esto se incluyen actividades con HEC-RAS para evaluar el aprovechamiento y aprendizaje del curso.
* Las consultas pueden formularse por medio del espacio de [🔰Ayuda](https://github.com/juanrodace/J.HRAS/discussions) del repositorio en GitHub o mensaje en plataforma de Microsoft Teams en el caso de acompañamiento y certificación. 


## Requisitos académicos

* Ser estudiante o profesional en ingeniería civil, ambiental, sanitario o carreras afines.
* Nociones básicas en propiedades de los fluidos y su transporte.
* Nociones básicas en sistemas de información geográfica (SIG).

## Requisitos técnicos

* Computador con Microsoft® Windows 98/NT/2000/XP/Vista/7/8/8.1/10, audio y video.
* Contar con conexión a internet.
* Software de modelación hidráulica HEC-RAS.
* Software QGIS o similar.

##

<div align="center"><a href="Section01/Readme.md"><img src=".icons/Start.png" alt="INICIO" width="210" border="10" /></a></div>


## Contenido
### Sección 1. Introducción y fundamentos generales

| Microcontenido                                                                  | Detalle                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Conceptos básicos de flujo a superficie libre.](Section01/FundamentalConcepts) | En esta clase se presentan los conceptos generales requeridos para entender el flujo a superficie libre, en diferentes condiciones, considerando sus características geométricas, cinéticas y dinámicas. Dentro de esta clase revisaremos los siguientes temas: Flujo a superficie libre, distribución de velocidades, elementos geométricos de la sección de un canal, clasificación del flujo, profundidad crítica y secciones de control.                                 |
| [Ecuaciones fundamentales.](Section01/FundamentalEquations)                     | En esta clase se presentan los ecuaciones fundamentales de la hidráulica, continuidad, conservación de la energía y conservación del momentum aplicados a sistemas de flujo a superficie libre.                                                                                                                                                                                                                                                                              |
| [Flujo uniforme y variado.](Section01/VariedFlow)                               | En esta clase se revisan los conceptos generales del flujo uniforme, gradualmente variado y rápidamente variado en un sistema de flujo a superficie libre en condiciones permanentes.                                                                                                                                                                                                                                                                                        |
| [Flujo no permanente](Section01/UnsteadyFlow)                                   | En esta clase se estudian los conceptos básicos y ecuaciones del flujo no permanente en sistemas hidráulicos a superficie libre.                                                                                                                                                                                                                                                                                                                                             |
| [Sistemas hidráulicos y modelación.](Section01/HydraulicSystems)                | En esta clase se presentan los conceptos básicos de la gestión y planificación de sistemas de recursos hídricos, sus objetivos, características y aspectos. Así mismo se presenta la relación de los estudios o evaluación hidráulica en la planificación y gestión integral del recurso. Igualmente, se presentan los conceptos generales asociados a los estudios hidráulicos y modelación a tener en cuenta antes de iniciar con el uso de una herramienta computacional. |
| [HEC-RAS. Generalidades, usos y estructura.](Section01/HECRAS)                  | En esta clase se presentan las generalidades del software de modelación hidráulica desarrollado por el Hydrological Engineering Center, el cual es uno de los programas de referencia dentro de su campo. Así mismo, su obtención, descarga, instalación, características básicas, uso generalizado, actualización y estructura.                                                                                                                                             |

### Sección 2. Modelación hidráulica básica

| Microconteido                                          | 
|--------------------------------------------------------|
| Cargue y   validación geométrica básica.               |
| Cargue de   información topográfica.                   |
| Modificación de la geometría.                          |
| Definición de   condiciones hidráulicas y de frontera. |
| Simulación en   régimen permanente 1D.                 |
| Simulación en   régimen no permanente 1D.              |
| Visualización   de resultados.                         |
| Errores y   avisos comunes.                            |

### Sección 3. Modelación con opciones avanzadas

| Microconteido                                             |
|-----------------------------------------------------------|
| Definición de coeficiente Manning a partir de coberturas. |
| Tramos con confluencias.                                  |
| Incorporación de estructuras hidráulicas.                 |
| Uso de diques en la modelación.                           |
| Cálculo de la socavación general y local.                 |


### Sección 4. Modelación de flujo bidimensional

| Microconteido                                      |
|----------------------------------------------------|
| Herramienta RAS Mapper.                            |
| Procesamiento del MDT.                             |
| Cargue de la geometría y definición de la malla.   |
| Condiciones hidráulicas iniciales y de frontera.   |
| Simulaciones de flujo bidimensional.               |
| Visualización y generación de mapas de inundación. |
| Obras hidráulicas en modelaciones bidimensionales. |

##

_:beginner: Ayuda / Colabora: a través de la pestaña _[Discussions](https://github.com/juanrodace/J.HRAS/discussions)_ localizada en la parte superior de esta ventana, podrás encontrar y participar en los [_anuncios o noticias_](https://github.com/juanrodace/J.HRAS/discussions/categories/announcements) publicados, enviarnos tus [_ideas_](https://github.com/juanrodace/J.HRAS/discussions/categories/ideas) para actividades complementarias, participar en preguntas, respuestas y consultas específicas [_Q&A_](https://github.com/juanrodace/J.HRAS/discussions/categories/q-a) y realizar [_publicaciones o consultas generales_](https://github.com/juanrodace/J.HRAS/discussions/categories/general) públicas._

_J.HRAS es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](License.md)._

_Clonación: para compatibilidad completa de las rutas utilizadas en los scripts y herramientas de J.HRAS, en Microsoft Windows clonar y/o descomprimir en _D:\J.HRAS_. Enlace para clonación https://github.com/juanrodace/J.HRAS.git._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [juanrodace](https://github.com/juanrodace) en GitHub._

##

<div align="center"><a href="http://www.escuelaing.edu.co" target="_blank"><img src=".icons/Banner1.svg" alt="Support by" width="100%" border="0" /></a><sub><br>Este curso ha sido desarrollado con el apoyo de la Universidad Escuela Colombiana de Ingeniería Julio Garavito. Encuentra más contenidos en https://github.com/uescuelaing</sub><br><br></div>