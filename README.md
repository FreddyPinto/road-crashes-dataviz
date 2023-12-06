<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT Licencia][Licencia-shield]][Licencia-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FreddyPinto/road-crashes-dataviz">
    <img src="images/logo.png" alt="Logo" width="100" height="100">
    
  </a>

<h3 align="center">Análisis y Visualización de Datos de Siniestros Viales</h3>

  <p align="center">
    Análisis y visualización de datos de siniestros viales en Buenos Aires entre 2016 y 2021.
    <br />
    <a href="https://github.com/FreddyPinto/road-crashes-dataviz"><strong>Explorar docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/FreddyPinto/road-crashes-dataviz/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/FreddyPinto/road-crashes-dataviz/issues">Request Feature</a>
  </p>
</div>



<!-- Tabla de contenido -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del Proyecto</a>
      <ul>
        <li><a href="#desarrollado-con">Desarrollado con:</a></li>
      </ul>
    </li>
    <li>
      <a href="#metodología-aplicada">Metodología Aplicada</a>
    </li>
    <li><a href="#kpis">KPIs</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contribuciones">Contribuciones</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
    <li><a href="#agradecimientos">Agradecimientos</a></li>
  </ol>
</details>



<!-- Acerca del Proyecto -->
## Acerca del Proyecto

<!-- <p align="center">
  <img src="images/screenshot-api-home.png" alt="screenshot"/>
</p> -->

Este proyecto fue desarrollado como parte de la etapa de Labs del bootcamp de la carrera de data science en SoyHenry, que consistía en asumir el rol de un Data Analyst miembro del equipo de analistas de datos de una empresa consultora a la cual el **Observatorio de Movilidad y Seguridad Vial (OMSV)**, que es un centro de estudios que se encuentra bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA), le solicitó la elaboración de un proyecto de análisis de datos.

El objetivo de este proyecto es generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales en la Ciudad de Buenos Aires. Para ello, se hace uso de los datos de los [homicidios](data/raw/homicidios.xlsx) en siniestros viales ocurridos en la ciudad durante el periodo 2016-2021, proporcionados por el Observatorio de Movilidad y Seguridad Vial (OMSV). 

El proyecto consta de tres etapas principales: extracción, transformación y carga (ETL) de los datos, análisis exploratorio de datos (EDA) y visualización de los resultados mediante un dashboard interactivo.


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


### Desarrollado con:

* [![Python][Python]][Python-url]
* [![Jupiter][Jupiter]][Jupiter-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Seaborn][Seaborn]][Seaborn-url]
* [![PowerBI][PowerBI]][PowerBI-url]
* [![VSC][VSC]][VSC-url]


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- Methodology -->
##  Metodología Aplicada

- **[ETL](notebooks/1.0-fp-etl.ipynb)** : Se realizó el proceso de extracción, transformación y carga de los datos de un dataset en formato *xlsx*, que contiene dos hojas con información sobre los hechos y las víctimas de los siniestros viales. Se resolvieron los problemas de calidad y consistencia de los datos, se eliminaron los valores nulos y duplicados, se cambiaron los tipos de datos y se crearon nuevas columnas derivadas. Se obtuvo un DataFrame limpio y estructurado para su posterior análisis y visualización.

- **[EDA](notebooks/2.0-fp-eda.ipynb)**: Se realizó el análisis exploratorio de datos, donde se obtuvo información relevante y descriptiva sobre el fenómeno estudiado. Se identificaron las características, las tendencias, las relaciones y las anomalías de los datos, se calcularon estadísticas descriptivas y se generaron visualizaciones que facilitaron su comprensión y comunicación. Se respondieron preguntas de interés sobre los datos, como la distribución temporal y espacial de los siniestros, las características de las víctimas, los factores de riesgo, etc.

- **[Visualización](reports/1.0-fp-dashboard.pbix)**: Se realizó la visualización de los resultados mediante un dashboard interactivo, que permitio explorar y filtrar los datos de forma dinámica y atractiva. Se usaron gráficos de diferentes tipos, como mapas, barras, líneas, sectores, etc. Se incluyeron indicadores clave de rendimiento (KPIs) que resumieron la información más importante de los datos, como el número total de siniestros, el porcentaje de víctimas fatales, la tasa de mortalidad, etc.


<!-- KPIS -->
## KPIs

Se plantearon dos objetivos en relación a la disminución de la cantidad de víctimas fatales de los siniestros viales, de los cuales elaboraron dos indicadores de rendimiento clave o KPI.

1. _Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior_.

    Se definió la **tasa de homicidios en siniestros viales** como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico. Su fórmula es:

    $\text{Tasa de homicidios en siniestros viales} = \frac{\text{Número de homicidios en siniestros viales}}{\text{Población total}}\times 100,000$


    Se observaron tendencias y cambios en la tasa de homicidios en siniestros viales a lo largo de los semestres:

    - A lo largo de los semestres, se observó una tendencia general a la baja en la tasa de homicidios en siniestros viales, aunque hubo semestres con aumentos respecto al semestre anterior. El semestre **1** del **2020** muestra la mayor baja, probablemente debido a la menor circulación de autos por las restricciones de la pandemia de Coronavirus.

    - En el último semestre analizado (segundo semestre de 2021), se logró una reducción del **23%** en la tasa de homicidios en comparación con el semestre anterior, superando con creces el objetivo del KPI de una reducción del **10%**. Esto indica que las medidas implementadas durante este período fueron efectivas.

    - Para el primer semestre de 2021, la tasa de homicidios en siniestros viales fue de **1.76**, lo que significa que hubo aproximadamente **1.76** homicidios en accidentes de tránsito por cada 100,000 habitantes. El objetivo era reducir esta tasa a **1.60** para el segundo semestre de **2021**. Al calcular el KPI para este período, se obtuvo una tasa de **1.35**, lo que indica que se cumplió con el objetivo propuesto.

    - En resumen, aunque la curva no es estacionaria y muestra fluctuaciones semestrales, la tendencia general es a la baja, lo que es un indicativo positivo. Sin embargo, es importante seguir monitoreando estos datos y ajustando las medidas de seguridad vial según sea necesario para mantener esta tendencia a la baja.

2. _Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior_.

    Definimos a la **cantidad de accidentes mortales de motociclistas en siniestros viales** como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal.
    La fórmula para medir la evolución de los accidentes mortales con víctimas en moto es:

    $\text{Cantidad de accidentes mortales de motociclistas} = -\frac{\text{Víctimas moto año anterior - Víctimas moto año actual}}{\text{Víctimas moto año anterior}}\times 100$

    A partir de los datos analizados, podemos observar varias tendencias y cambios en el número de accidentes mortales de motociclistas a lo largo de los años:

    - En **2017**, los accidentes mortales de motociclistas **disminuyeron en un 13.85%** en comparación con el año anterior. Esto podría ser un indicativo de que las estrategias de seguridad vial implementadas en ese año tuvieron un impacto positivo.

    - En **2018**, hubo un **aumento del 1.79%** en comparación con 2017. Aunque es un aumento, la tasa de cambio es relativamente pequeña, lo que podría indicar que la situación se mantuvo relativamente estable.

    - En **2019**, hubo una **disminución del 12.28%** en comparación con 2018. Esto es una buena señal y podría indicar que las medidas de seguridad implementadas ese año fueron efectivas.

    - En **2020**, hubo una **disminución significativa del 44%** en comparación con 2019. Este es un cambio notable y podría estar relacionado con factores excepcionales como la pandemia de COVID-19, que pudo haber reducido la cantidad de tráfico y, por lo tanto, el número de accidentes.

    - En **2021**, hubo un **aumento significativo del 64.29%** en comparación con 2020. Este es un cambio preocupante y sugiere que se deben tomar medidas para abordar este aumento.

Estes análisis subraya la importancia de seguir implementando y mejorando las medidas de seguridad para los motociclistas. También destacan cómo factores externos, como una pandemia, pueden tener un impacto significativo en las tasas de accidentes.


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- ROADMAP -->
## Conclusiones
Entre los años 2016 y 2021, se produjeron 717 accidentes de tránsito con víctimas fatales en la Ciudad Autónoma de Buenos Aires. El análisis de los datos y su visualización a través del dashboard permiten identificar algunos patrones y factores asociados a estos siniestros.

La mayoría de los accidentes mortales (70%) ocurrieron durante los días hábiles, especialmente en las franjas horarias de ingreso y salida laboral (5-9h y 17-18h) y de almuerzo (12-14h). Sin embargo, durante los fines de semana, los siniestros se concentraron en las horas de la madrugada (3-7h), coincidiendo con las salidas nocturnas. Diciembre fue el mes con mayor cantidad de víctimas fatales en el período analizado.

El perfil de las víctimas fatales fue mayoritariamente masculino (77%), con una edad promedio de 35 años. El 42% de las víctimas eran motociclistas, seguidos por los peatones (25%). El 62% de los accidentes ocurrieron en avenidas, siendo el 82% de ellos en cruces con otras calles. Las comunas 1 y 4 fueron las que registraron más siniestros viales con víctimas fatales.

En el segundo semestre del año 2021, se logró reducir la tasa de homicidios en siniestros viales respecto al año anterior, pero no se alcanzaron los objetivos de disminuir la cantidad de accidentes mortales en motociclistas ni en avenidas.


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


## Recomendaciones

A partir de estas conclusiones, se recomienda:

- Mantener el seguimiento de los objetivos propuestos y acompañarlos con campañas de prevención y concientización, enfocadas especialmente en los conductores de motos y los usuarios de las avenidas.

- Intensificar las campañas de seguridad vial durante los fines de semana, sobre todo en el mes de diciembre, cuando se incrementa el flujo vehicular y el consumo de alcohol.

- Mejorar las señales y los controles en las avenidas y los cruces de calles, donde se producen la mayoría de los siniestros.

- Orientar las campañas de seguridad hacia el sexo masculino, que representa el mayor porcentaje de víctimas fatales, especialmente en el rango etario de 15 a 44 años.


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- ROADMAP -->
## Roadmap

Algunos aspectos de este proyecto se podrían mejorar en un futuro, con la finalidad de lograr un producto más completo y robusto. Algunas de las posibles mejoras son:

- [ ] Ampliar el periodo de análisis, incorporando datos de años anteriores o posteriores al 2016-2021.

- [ ] Enriquecer el dataset, agregando otras fuentes de datos que puedan aportar información relevante sobre los siniestros viales, como el clima, el estado de las vías, el tráfico, etc. 

- [ ] Realizar un análisis de causalidad, para determinar qué variables o factores influyen más en la ocurrencia y la gravedad de los siniestros viales.

- [ ] Crear un modelo predictivo, que permita estimar el riesgo de sufrir un siniestro vial en función de las características del conductor, el vehículo, la vía y el entorno. 

- [ ] Desplegar el proyecto en una plataforma web, que permita acceder a los dashboards de forma pública y gratuita, sin necesidad de instalar ninguna librería o herramienta adicional. 

Consulta los [issues abiertos](https://github.com/FreddyPinto/road-crashes-dataviz/issues) para proponer características (y problemas conocidos).


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- CONTRIBUTING -->
## Contribuciones

Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar increíble para apJupiter, inspirarse y crear. Cualquier contribución que hagas será **muy apreciada**.

Si tienes una sugerencia para mejorar este proyecto, haz un fork del repositorio y crea un pull request. También puedes simplemente abrir un issue con la etiqueta *“enhancement”*. ¡No olvides darle una estrella al proyecto! Gracias de nuevo.

1. Haz un fork del Proyecto
2. Crea tu feature Branch (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la Branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- Licencia -->
## Licencia

Distribuido bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- Contacto -->
## Contacto

Freddy Pinto - freddypinto@outlook.com 

[![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/FreddyPinto/road-crashes-dataviz](https://github.com/FreddyPinto/road-crashes-dataviz)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Agradecimientos
Quiero agradecer a las siguientes personas y recursos que me han ayudado a realizar este proyecto:

* A [SoyHenry](https://www.soyhenry.com/) por ofrecerme esta gran oportunidad de participar en el bootcamp de data science y desarrollar este proyecto.
* A la comunidad de Henry, especialmente a los profesores y compañeros que me han apoyado y guiado durante el proceso de aprendizaje.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/FreddyPinto/road-crashes-dataviz.svg?style=for-the-badge
[contributors-url]: https://github.com/FreddyPinto/road-crashes-dataviz/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/FreddyPinto/road-crashes-dataviz.svg?style=for-the-badge
[forks-url]: https://github.com/FreddyPinto/road-crashes-dataviz/network/members
[stars-shield]: https://img.shields.io/github/stars/FreddyPinto/road-crashes-dataviz.svg?style=for-the-badge
[stars-url]: https://github.com/FreddyPinto/road-crashes-dataviz/stargazers
[issues-shield]: https://img.shields.io/github/issues/FreddyPinto/road-crashes-dataviz.svg?style=for-the-badge
[issues-url]: https://github.com/FreddyPinto/road-crashes-dataviz/issues
[Licencia-shield]: https://img.shields.io/github/license/FreddyPinto/road-crashes-dataviz.svg?style=for-the-badge
[Licencia-url]: https://github.com/FreddyPinto/road-crashes-dataviz/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/FreddyPinto-/
[product-screenshot]: images/screenshot.jpg
[Python]: https://img.shields.io/badge/Python-333333?style=flat&logo=python&labelColor=white
[Python-url]: https://www.python.org/
[PowerBI]: https://img.shields.io/badge/-Power_BI-333333?style=flat&logo=powerbi&labelColor=white
[PowerBI-url]: https://powerbi.microsoft.com/
[Jupiter]: https://img.shields.io/badge/-Jupyter_Notebook-333333?style=flat&logo=jupyter&labelColor=white
[Jupiter-url]: https://jupyter.org/
[Seaborn]:https://img.shields.io/badge/-Seaborn-333333?style=flat
[Seaborn-url]:https://seaborn.pydata.org/
[Pandas]:https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas&logoColor=black&labelColor=white
[Pandas-url]:https://pandas.pydata.org/
[VSC]:https://img.shields.io/badge/-Visual_Studio_Code-333333?style=flat&logo=visualstudiocode&logoColor=blue&labelColor=white
[VSC-url]:https://code.visualstudio.com/
[Matplotlib]:https://img.shields.io/badge/-Matplotlib-333333?style=flat
[Matplotlib-url]:https://matplotlib.org/