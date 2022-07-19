## Conceptos básicos
Keywords: `Case study` `Colombia` `Cesar` `IDEAM` `Weather` `Zona hidrogeográfica` `Station` `ArcGIS` `QGIS` `Dissolve` `Feature Envelope to Polygon` `Add Field` `Field Calculator` `Bounding boxes`

Definición de la zona de estudio a partir de la cobertura de subzonas hidrográficas de Colombia con creación de polígono envolvente. En esta actividad se define el sistema de proyección de coordenadas a utilizar en los diferentes mapas y capas geográficas.

![CaseStudy.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Graph/CaseStudy.png)

> En la ilustración, _COD_ZH_ corresponde al código de la Zona Hidrográfica.


### Objetivos

* Estudiar la estructura general de la zonificación hidrográfica de Colombia.
* Crear una capa geográfica que delimite la zona geográfica de estudio.
* Crear el polígono regular del dominio espacial que envuelve la zona de estudio.
* Calcular el área y perímetro de la zona de estudio y su dominio espacial.
* Definir el sistema de proyección de coordenadas a utilizar en los mapas y capas geográficas.

> El polígono regular permitirá en actividades posteriores del curso, realizar la descarga de información satelital y seleccionar las estaciones hidroclimatológicas de la zona de estudio. 

### Requerimientos

* Conocimientos en mecánica de fluidos.
* Microsoft Excel
* Python (Opcional)


### Alcance

Para la realización del Balance Hidrológico de Largo Plazo o LTWB (Long-term water balance), se ha definido como caso de estudio la Zonificación Hidrográfica de Colombia y la red de estaciones terrestres hidroclimatológicas del [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM de Colombia](http://www.ideam.gov.co/). A nivel particular se estudiará a detalle la zona hidrográfica 28, denominada _Cesar_ que hace parte del área hidrográfica principal 2, correspondiente a _Magdalena - Cauca_ que se compone de las siguientes subzonas:

| SZH  | Subzona Hidrográfica |
|------|----------------------|
| 2801 | Alto Cesar           |
| 2802 | Medio Cesar          |
| 2804 | Río Ariguaní         |
| 2805 | Bajo Cesar           |

> Estudiantes que aplicaron para curso certificado, desarrollan casos de estudio individuales asignados para zonas hidrográficas específicas.  


### Distribución de velocidades

### Elementos geométricos de la sección transversal


| AH  | Área Hidrográfica |
|-----|-------------------|
| 1   | Caribe            |
| 2   | Magdalena-Cauca   |
| 3   | Orinoco           |
| 4   | Amazonas          |
| 5   | Pacífico          |

![ZonaHidrografica2013.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Graph/ZonaHidrografica2013.png)

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

* Creado por ing.juanrodace@gmail.com (0.5 horas)


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier herramienta SIG que disponga de herramientas de geoprocesamiento para disolución de polígonos y creación de polígonos envolventes.

> Las herramientas computacionales requeridas, librerías, complementos y sus versiones son especificadas en cada actividad del curso.


### Control de versiones


| Versión      | Descripción                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------|
| 2022.07.19   | Inclusión de distribución de velocidades y características geométricas de lassecciones trasversales. |
| 2022.xx.xx   | Inclusión de ecuaciones fundamentales.                                                               |


### Licencia, cláusulas y condiciones de uso

J.HRAS es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/juanrodace/J.HRAS/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/juanrodace/J.HRAS/wiki) | [Actividad siguiente]()  |
|------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_

[^1]: http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
[^2]: http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf
[^3]: http://geoservicios.ideam.gov.co/geonetwork/srv/eng/catalog.search#/metadata/7696695f-ae9c-4780-a6d0-d3cd1808819a
[^4]: http://geoservicios.ideam.gov.co/CatalogoObjetos/queryByUUID?uuid=bcd645c9-0f11-4770-926e-1e1fdfbf5ce6
