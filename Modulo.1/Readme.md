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

* ArcGIS for Desktop 10+ (opcional)
* ArcGIS Pro (opcional)
* QGIS 3+ (opcional)


### Alcance

Para la realización del Balance Hidrológico de Largo Plazo o LTWB (Long-term water balance), se ha definido como caso de estudio la Zonificación Hidrográfica de Colombia y la red de estaciones terrestres hidroclimatológicas del [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM de Colombia](http://www.ideam.gov.co/). A nivel particular se estudiará a detalle la zona hidrográfica 28, denominada _Cesar_ que hace parte del área hidrográfica principal 2, correspondiente a _Magdalena - Cauca_ que se compone de las siguientes subzonas:

| SZH  | Subzona Hidrográfica |
|------|----------------------|
| 2801 | Alto Cesar           |
| 2802 | Medio Cesar          |
| 2804 | Río Ariguaní         |
| 2805 | Bajo Cesar           |

> Estudiantes que aplicaron para curso certificado, desarrollan casos de estudio individuales asignados para zonas hidrográficas específicas.  


### Zonificación hidrográfica de Colombia

La zonificación hidrográfica de Colombia desde el punto de vista hidrológico, tiene sus inicios en el HIMAT mediante la Resolución 0337 del 1978, la cual establece que el país está conformado por cinco Áreas hidrográficas (1-Caribe, 2- Magdalena - Cauca, 3- Orinoco, 4- Amazonas y 5-Pacífico) que a su vez están divididas en Zonas Hidrográficas y subdivididas en Subzonas Hidrográficas. En ese entonces, el propósito de la zonificación fue de adoptar un sistema de codificación para estaciones Hidrometerológicas. Posteriormente, el IDEAM introduce esta zonificación para otros fines, tales como estudios y análisis hidrológicos relacionados con los informes ambientales, p.ej, el Índice de Aridez, el Escurrimiento y el Rendimiento Hídrico.[^1]

La zonificación de cuencas hidrográficas corresponde a tres niveles de jerarquía: áreas, zonas y subzonas hidrográficas. Las áreas hidrográficas corresponden a las regiones hidrográficas o vertientes que, en sentido estricto, son las grandes cuencas que agrupan un conjunto de ríos con sus afluentes que desembocan en un mismo mar. Ahora bien, en Colombia se distinguen cuatro vertientes, dos de ellas asociadas a ríos de importancia continental (vertiente del Orinoco y vertiente del Amazonas) y las vertientes del Atlántico y del Pacífico. Se delimita adicionalmente como áea hidrográfica la cuenca Magdalena-Cauca, que aunque tributa y forma parte de la vertiente del Atlántico, tiene importancia socioeconómica por su alto poblamiento y aporte al producto interno bruto.[^2]

| AH  | Área Hidrográfica |
|-----|-------------------|
| 1   | Caribe            |
| 2   | Magdalena-Cauca   |
| 3   | Orinoco           |
| 4   | Amazonas          |
| 5   | Pacífico          |

![ZonaHidrografica2013.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Graph/ZonaHidrografica2013.png)

Las cuencas hidrográficas que entregan o desembocan sus aguas superficiales directamente de una área hidrográfica se denominaran zonas hidrográficas. Agrupan varias cuencas que se presentan como un subsistema hídrico con características de relieve y drenaje homogéneo y sus aguas tributan a través de un afluente principal hacia un área hidrográfica. Están integradas por cuencas de las partes altas, medias o bajas de una zona hidrográfica que captan agua y sedimentos de los tributarios de diferente orden tales como nacimientos de agua, arroyos, quebradas y ríos. Las cuencas que tributan sus aguas a su vez a las zonas hidrográficas se denomina subzonas hidrográficas. Ahora bien, respecto a la toponimia con que se identifican zonas y subzonas hidrográficas, a estas unidades se les asignó la toponimia de acuerdo con el nombre de la corriente más representativa o río principal o con el nombre heredado de la zonificación del HIMAT, que puede corresponder al espacio geográfico o región a la cual drenan las aguas superficiales.[^2]

| AH  | Área Hidrográfica | ZH  | Zona Hidrográfica                  |
|-----|-------------------|-----|------------------------------------|
| 1   | Caribe            | 11  | Atrato - Darién                    |
| 1   | Caribe            | 12  | Caribe - Litoral                   |
| 1   | Caribe            | 13  | Sinú                               |
| 1   | Caribe            | 15  | Caribe - La Guajira                |
| 1   | Caribe            | 16  | Catatumbo                          |
| 1   | Caribe            | 17  | Islas del Caribe                   |
| 2   | Magdalena - Cauca | 21  | Alto Magdalena                     |
| 2   | Magdalena - Cauca | 22  | Saldaña                            |
| 2   | Magdalena - Cauca | 23  | Medio Magdalena                    |
| 2   | Magdalena - Cauca | 24  | Sogamoso                           |
| 2   | Magdalena - Cauca | 25  | Bajo Magdalena - Cauca - San Jorge |
| 2   | Magdalena - Cauca | 26  | Cauca                              |
| 2   | Magdalena - Cauca | 27  | Nechí                              |
| 2   | Magdalena - Cauca | 28  | Cesar                              |
| 2   | Magdalena - Cauca | 29  | Bajo Magdalena                     |
| 3   | Orinoco           | 31  | Inírida                            |
| 3   | Orinoco           | 32  | Guaviare                           |
| 3   | Orinoco           | 33  | Vichada                            |
| 3   | Orinoco           | 34  | Tomo                               |
| 3   | Orinoco           | 35  | Meta                               |
| 3   | Orinoco           | 36  | Casanare                           |
| 3   | Orinoco           | 37  | Arauca                             |
| 3   | Orinoco           | 38  | Orinoco Directos                   |
| 3   | Orinoco           | 39  | Apure                              |
| 4   | Amazonas          | 41  | Guainía                            |
| 4   | Amazonas          | 42  | Vaupés                             |
| 4   | Amazonas          | 43  | Apaporis                           |
| 4   | Amazonas          | 44  | Caquetá                            |
| 4   | Amazonas          | 45  | Yarí                               |
| 4   | Amazonas          | 46  | Caguán                             |
| 4   | Amazonas          | 47  | Putumayo                           |
| 4   | Amazonas          | 48  | Amazonas - Directos                |
| 4   | Amazonas          | 49  | Napo                               |
| 5   | Pacífico          | 51  | Mira                               |
| 5   | Pacífico          | 52  | Patía                              |
| 5   | Pacífico          | 53  | Tapaje - Dagua - Directos          |
| 5   | Pacífico          | 54  | San Juan                           |
| 5   | Pacífico          | 55  | Baudó - Directos Pacífico          |
| 5   | Pacífico          | 56  | Pacífico - Directos                |
| 5   | Pacífico          | 57  | Islas del Pacífico                 |

> En el presente análisis no se han incluido resultados para la ZH - zona hidrográfica 57, correspondiente a las Islas del Pacífico, debido a que la capa geográfica SZH - subzonas hidrográficas no contiene el polígono de delimitación. 


### Delimitación de la zona de estudio

#### Instrucciones en ArcGIS for Desktop (10.2.2)

El proceso de delimitación se realiza a partir de la cobertura de Subzonas hidrográficas de Colombia, este mapa representa las unidades de análisis para el ordenamiento ambiental de territorio definidas por el IDEAM en convenio con el Instituto Geográfico Agustín Codazzi (IGAC), a escala 1:500.000. [^3]

1. Ingrese al portal http://www.ideam.gov.co/en/capas-geo y en el cuadro de búsqueda escriba _Zonificación Hidrográfica_, observará que a 2022.07.07 existen dos versiones de la capa de zonificación correspondientes al año 2010 y 2013. Realice la descarga del archivo de formas Shapefile del año 2013, consulte sus metadatos y el catálogo de objetos disponible.

> La descarga permite obtener el archivo comprimido _[Zonificacion_Hidrografica_2013.zip](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/Zonificacion_Hidrografica_2013.zip)_ que contiene la capa geográfica en formato Shapefile, un mapa de muestra en formato .pdf, la ficha de representación gráfica y otros elementos complementarios. 

![IDEAMZonificacionHidrograficaDescarga.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/IDEAMZonificacionHidrograficaDescarga.png)

Catálogo de objetos en Subzonas [^4]
| Nombre       | Alias          | Definición                                                                   | Tipo de dato |
|--------------|----------------|------------------------------------------------------------------------------|--------------|
| OBJECTID     | OBJECTID       | Identificador de objeto geográfico.                                          | Texto        |
| Shape        | Shape          | Tipo de geometría.                                                           | Geometría    |
| COD_AH       | Código Area    | Código del Area hidrográfica a la que corresponde.                           | Entero       |
| COD_ZH       | Código Zona    | Código de la Zona hidrográfica a la que corresponde.                         | Entero       |
| COD_SZH      | Código Subzona | Código de Subzona hidrográfica a la que corresponde.                         | Entero       |
| NOM_AH       | Nombre Área    | Nombre del área hidrográfica a la que corresponde. Dominio Área Hidográfica. | Texto        |
| NOM_ZH       | Nombre Zona    | Nombre de la zona hidrográfica a la que corresponde.                         | Texto        |
| NOM_SZH      | Nombre Subzona | Nombre de la Subzona hidrográfica a la que corresponde.                      | Texto        |
| Shape_Length | Shape_Length   | Perímetro en las unidades del sistema de referencia espacial.                | Entero       |
| Shape_Area   | Shape_Area     | Área en las unidades del sistema de referencia espacial.                     | Entero       |
| RULEID       | RULEID         | Id único asignado por el sistema a la representación gráfica.                | Entero       |
| Override     | Override       | Representación gráfica.                                                      | Blob         |

2. Descomprima solo los datos contenidos en la carpeta _\Shape_ del comprimido obtenido, dentro de la carpeta _.shp_ localizada en _D:\R.LTWB_

3. Cree un mapa nuevo en blanco y agregue la capa de Subzonas Hidrográficas. Simbolice por categorías de valores únicos o _Unique Values_ a partir del campo `NOM_ZH` correspondiente a la Zona Hidrográfica y rotule las zonas a partir del campo de atributos `COD_SZH` correspondiente a los códigos de las subzonas, guarde el mapa como _R.LTWB.mxd_ en la carpeta _.Map_ localizada en _D:\R.LTWB_

![ArcGISDesktop10.2.2ZonaHidrografica2013.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaHidrografica2013.png)

> Recuerde que en ArcGIS for Desktop es necesario desde el catálogo, realizar la conexión a la unidad de disco o a una carpeta específica para poder agregar datos al mapa.

4. A partir de las Subzonas Hidrográficas y utilizando la expresión `"COD_ZH" = 28`, filtre los polígonos del caso de estudio correspondientes a la Subzona 28 - Cesar. Abra la tabla de atributos, podrá observar que contiene las subzonas Alto Cesar, Medio Cesar, Bajo Cesar y Río Ariguaní. Cambie la simbología de representación a relleno color gris al 20%.

![ArcGISDesktop10.2.2ZonaHidrografica2013Query.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaHidrografica2013Query.png)

5. Utilizando la herramienta _Dissolve_ disponible en el menú _Geoprocessing_, disuelva los polígonos de la zona de estudio para obtener un único polígono perimetral (no es necesario definir ningún campo de disolución). Nombrar como _ZonaEstudio.shp_. Simbolice solo por contorno utilizando borde externo negro en grosor 3.

![ArcGISDesktop10.2.2ZonaHidrografica2013Dissolve.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaHidrografica2013Dissolve.png)

6. En la Tabla de Contenido, asigne en las propiedades de Layers o Capas el sistema de proyección de coordenadas MAGNA_Colombia_CTM12 correspondiente al identificador EPSG 9377 ó ESRI 103599.

> La versiones antiguas de ArcGIS for Desktop (p.ej, 10.2.2) no incluyen el sistema de proyección del origen único nacional CTM12 o 9377, por lo que la asignación debe ser realizada a través de un archivo de proyección de coordenadas .prj. La definición de un sistema proyectado permitirá realizar el cálculo de áreas y perímetros en unidades del sistema internacional. En la carpeta _[.ProjectionFile](https://github.com/rcfdtools/R.LTWB/tree/main/.ProjectionFile)_ de este repositorio se encuentran diferentes archivos de proyección, incluido _MAGNA_OrigenNacional.prj_ correspondiente al CRS requerido.

Parámetros del archivo de proyección origen único nacional de Colombia: [MAGNA_OrigenNacional.prj](https://github.com/rcfdtools/R.LTWB/tree/main/.ProjectionFile)
```
MAGNA_Colombia_Origen_Unico
Authority: Custom

Projection: Transverse_Mercator
False_Easting: 5000000.0
False_Northing: 2000000.0
Central_Meridian: -73.0
Scale_Factor: 0.9992
Latitude_Of_Origin: 4.0
Linear Unit: Meter (1.0)

Geographic Coordinate System: GCS_MAGNA
Angular Unit: Degree (0.0174532925199433)
Prime Meridian: Greenwich (0.0)
Datum: D_MAGNA
  Spheroid: GRS_1980
    Semimajor Axis: 6378137.0
    Semiminor Axis: 6356752.314140356
    Inverse Flattening: 298.257222101
```
![ArcGISDesktop10.2.2CRS9377.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2CRS9377.png)

7. En la tabla de atributos de la capa geográfica _ZonaEstudio.shp_, cree dos campos de atributos numéricos dobles y nómbrelos como Akm2 y Pkm correspondientes al área en km² y perímetro en km, cree un campo de texto con longitud de 55 caracteres con el nombre ZH. Utilizando el calculador de geometría obtenga el área y el perímetro y asigne manualmente el código y nombre de la subzona en el campo ZH como _ZH 2 - Cesar_.

> En ArcGIS, nuevos campos pueden ser creados desde las propiedades de la tabla de atributos utilizando la opción _Add Field_. 
> Para el cálculo del área y perímetros, de clic derecho en la cabecera de los campos y seleccione la opción _Calculate Geometry_.

![ArcGISDesktop10.2.2ZonaEstudioAddField.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaEstudioAddField.png)

Rotule indicando la zona, área y perímetro utilizando las siguientes expresiones: 

* Parser VBScript: `[ZH] &VbNewLine& "Área, km²: " & round( [Akm2], 2) &VbNewLine& "Perímetro, km: " & round( [Pkm], 2)`
* Parser Python: `[ZH] + "\nArea, km2: " +  [Akm2]  + "\nPerimetro, km: " + [Pkm]`

![ArcGISDesktop10.2.2ZonaEstudioCalculateGeometry.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaEstudioCalculateGeometry.png)

8. Utilizando la herramienta _Data Management / Features / Feature Envelope to Polygon_, cree el polígono regular envolvente de la zona de estudio y nómbrelo como _ZonaEstudioEnvelope.shp_. Agregue los campos de atributos flotantes Akm2, Pkm y de texto ZHEnvelope, asigne la etiqueta _ZH envelope 2 - Cesar_ y rotule con estos 3 campos.

![ArcGISDesktop10.2.2ZonaEstudioEnvelope.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaEstudioEnvelope.png)


#### Instrucciones en ArcGIS Pro (3.0.0)

En ArcGIS Pro, cree un proyecto nuevo en blanco en la ruta _D:\R.LTWB\\.map_ y nómbrelo como ArcGISPro. Automáticamente serán creados el mapa de proyecto, la base de datos geográfica en formato .gdb, la carpeta para volcado de informes de registro de importación _ImportLog_ y la carpeta _Index_. Utilizando el Panel de catálogo y desde la sección _Folders_, realice la conexión a la carpeta _D:\R.LTWB_.

![ArcGISPro3.0.0NewMapProject.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0NewMapProject.png)

Agregue la capa de Subzonas Hidrográficas y simbolice por categorías de valores únicos o _Unique Values_ a partir del campo `NOM_ZH` correspondiente a la Zona Hidrográfica y rotule las zonas a partir del campo de atributos `COD_SZH` correspondiente a los códigos de las subzonas.

![ArcGISPro3.0.0ZonaHidrografica2013.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0ZonaHidrografica2013.png)

Para el filtrado, desde las propiedades de la capa seleccione la pestaña _Definition Query_ y ensamble la expresión de filtrado o ingrese la instrucción SQL `COD_ZH = 28`.

![ArcGISPro3.0.0ZonaHidrografica2013Query.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0ZonaHidrografica2013Query.png)

La disolución de los polígonos para la creación de la zona de estudio se realiza desde el panel de herramientas _Geoprocessing - Data Management Tools - Generalization - Dissolve_ que puede ser lanzado desde el menú _Analysis_ seleccionando la opción _Tools_.

![ArcGISPro3.0.0ZonaHidrografica2013Dissolve.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0ZonaHidrografica2013Dissolve.png)

Para cambiar el sistema de proyección de coordenadas, en las propiedades del mapa _Map_ de la tabla de contenidos _Contents_, seleccione la pestaña _Coordinate Systems_ y en la caja de búsqueda ingrese 103599 correspondiente a MAGNA-SIRGAS CMT12.

![ArcGISPro3.0.0CRS103599.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0CRS103599.png)

Para la creación de campos de atributo, abra la tabla de atributos y de clic en la opción Add, agregue los campos Akm2, Pkm y ZH.

![ArcGISPro3.0.0ZonaEstudioAddField.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0ZonaEstudioAddField.png)

Calcule la geometría de los campos numéricos y asigne el nombre de la zona en el campo ZH utilizando el texto 'ZH 2 - Cesar' sobre Python 3 como _Expression Type_.

![ArcGISPro3.0.0ZonaEstudioCalculateGeometry.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0ZonaEstudioCalculateGeometry.png)

Para la rotulación compuesta, utilice cualquiera de las siguientes instrucciones:

* Parser VBScript: `[ZH] &VbNewLine& "Área, km²: " & round( [Akm2], 2) &VbNewLine& "Perímetro, km: " & round( [Pkm], 2)`
* Parser Python: `[ZH] + "\nArea, km2: " +  [Akm2]  + "\nPerimetro, km: " + [Pkm]`
* Parser Arcade: `$feature.ZH + '\nÁrea, km²: ' + Round($feature.Akm2, 2) + '\nPerímetro, km: : ' + Round($feature.Pkm, 2)`

![ArcGISPro3.0.0ZonaEstudioLabelArcade.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0ZonaEstudioLabelArcade.png)

Utilizando la herramienta _Data Management Tools / Features / Feature Envelope to Polygon_, cree el polígono regular envolvente de la zona de estudio. 

![ArcGISPro3.0.0ZonaEstudioEnvelope.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISPro3.0.0ZonaEstudioEnvelope.png)


#### Instrucciones en QGIS (3.26.0)

Cree un mapa de proyecto, agregue la capa Zonificacion_hidrografica_2013.shp y guarde en la carpeta _.map_ como _R.LTWB.qgz_

El filtrado de entidades se realiza a través de la ventana de propiedades de la capa desde la pestaña _Source_ y el _Query Builder_.

![QGIS3.26.0ZonaHidrografica2013Query.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/QGIS3.26.0ZonaHidrografica2013Query.png)

El proceso de disolución se realiza utilizando la herramienta _Vector geometry - Dissolve_ del _Processing Toolbox_ que se carga oprimiendo la combinación de teclas `Ctrl+Alt+T` o desde la barra de menús _Processing_.

![QGIS3.26.0ZonaHidrografica2013Dissolve.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/QGIS3.26.0ZonaHidrografica2013Dissolve.png)

Para cambiar el sistema de proyección, oprima la combinación de teclas `Ctrl+Shift+P` para acceder a la ventana de propiedades del proyecto y en la ventana _CRS_ ingrese en la casilla de filtro o búsqueda el valor 9377, correspondiente al sistema de referencia de coordenadas MAGNA-SIRGAS / Origen-Nacional. Seleccione y de clic en _Apply_ y _Ok_. En la parte inferior derecha de QGIS, podrá observar el sistema asignado como _EPSG: 9377_.

![QGIS3.26.0CRS9377.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/QGIS3.26.0CRS9377.png)

Nuevos campos de atributos pueden ser creados directamente desde las opciones del _Field Calculator_, p. ej. para el cálculo del área en km² se crea el campo Akm2 y se calcula la geometría con la expresión `$area / (1000*1000)`. Para el perímetro utilizar la expresión `$perimeter / 1000`.

![QGIS3.26.0ZonaEstudioAddField.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/QGIS3.26.0ZonaEstudioAddField.png)

La rotulación compuesta indicando la zona, área y perímetro se realiza con la siguiente expresión: `concat("ZH",  '\nÁrea, km²: ', round("Akm2",2), '\nPerímetro, km: ', round("Pkm", 2))`

![QGIS3.26.0ZonaEstudioLabel.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/QGIS3.26.0ZonaEstudioLabel.png)

El proceso de obtención del polígono perimetral se realiza con la herramienta _Vector geometry - Bounding boxes_ del _Processing Toolbox_ que se carga oprimiendo la combinación de teclas `Ctrl+Alt+T` o desde la barra de menús _Processing_.

![QGIS3.26.0ZonaEstudioBoundingBoxes.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/QGIS3.26.0ZonaEstudioBoundingBoxes.png)


Ahora dispone de un polígono que podrá utilizar como máscara de selección para la obtención de información satelital o para la selección de estaciones dentro de la zona de estudio.


### Autores

* Creado por r.cfdtools@gmail.com (8.5 horas)


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier herramienta SIG que disponga de herramientas de geoprocesamiento para disolución de polígonos y creación de polígonos envolventes.

> Las herramientas computacionales requeridas, librerías, complementos y sus versiones son especificadas en cada actividad del curso.


### Control de versiones


| Versión      | Descripción                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------|
| 2022.07.09   | Inclusión de procedimiento para delimitación de la zona de estudio usando ArcGIS Pro.                |
| 2022.07.08   | Inclusión de procedimiento para delimitación de la zona de estudio usando ArcGIS for Desktop y QGIS. |
| 2022.07.06   | Versión inicial con definición general del caso de estudio y mapas de referencia.                    |


### Licencia, cláusulas y condiciones de uso

R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]()  |
|------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_

[^1]: http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
[^2]: http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf
[^3]: http://geoservicios.ideam.gov.co/geonetwork/srv/eng/catalog.search#/metadata/7696695f-ae9c-4780-a6d0-d3cd1808819a
[^4]: http://geoservicios.ideam.gov.co/CatalogoObjetos/queryByUUID?uuid=bcd645c9-0f11-4770-926e-1e1fdfbf5ce6
