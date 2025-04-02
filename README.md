<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/MaykolMedrano/usebcrp">
    <img src="https://i.ibb.co/MDV7cGfC/5134453181701533346-1.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">USEBCRP</h3>

  <p align="center">
    Una biblioteca de Python que consume la API del Banco Central de Reservas del Perú (BCRP). Para descarga de series y rangos de tiempo determinados.
    <br />
    <a href="https://github.com/MaykolMedrano/usebcrp"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MaykolMedrano/usebcrp">View Demo</a>
    &middot;
    <a href="https://github.com/MaykolMedrano/usebcrp/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/MaykolMedrano/usebcrp/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del proyecto</a>
      <ul>
        <li><a href="#códigos-de-series">Códigos de series</a></li>
        <li><a href="#formato-de-salida">Formato de salida</a></li>
        <li><a href="#periodo-inicial-y-final">Periodo inicial y final</a></li>
        <li><a href="#idioma">Idioma</a></li>
        <li><a href="#construido-con">Construido con</a></li>
      </ul>
    </li>
    <li><a href="#instalación">Instalación</a></li>
    <li><a href="#uso">Uso</a>
    <ul>
        <li><a href="#metadatos">I.- Consulta a los metadatos</a></li>
        <li><a href="#installation">II.- Descarga de la información</a></li>
        <li><a href="#installation">III.- Exportamos una tabla de variaciones</a></li>
        <li><a href="#installation">IV.- Resultados</a></li>
      </ul>
    </li>
    <li><a href="#contribuidores">Contribuidores</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#como-citar-este-repositorio">Como citar este repositorio</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

![Product Name Screen Shot][product-screenshot]

Esta biblioteca de Python, dedicado a consumir el API del Banco Central de Reservas del Perú (BCRP) y que descarga series de datos publicados desde la institución. 

El API tiene la siguiente estructura:

>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/[códigos de series]/[formato de salida]/[periodo inicial]/[periodo final]/[idioma]

Tal como se observa en la API, esta conformado por una sección para:
- códigos de series
- formato de salida
- periodo inicial
- periodo final
- idioma

Esta información se encuentra en las tablas que comparten en el portal del BCRP.

<a href="https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/cuentas-monetarias"> 
  <img src="https://i.ibb.co/v46qnJRJ/5138681890537057606.jpg">
</a>
<br>
<br>
Las secciones se detallan a continuación.

### Códigos de series

Este es un parámetro obligatorio que requiere una extensión maxima de diez. Se puede agregar varios códigos de series separados por un guión.

En la estructura del API, la ubicación para ingresar los códigos de las series es la siguiente:

>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/[__códigos de series__]/../../../..

Los códigos de las series son un total de 16 446, los cuales están agrupadas en las siguientes categorías.

Nro|Categoría de series|Cantidad|Porcentaje
:-------|:-------|:-------|:-------
01|Balanza comercial|674|4.10%
02|Balanza de pagos|7|0.04%
03|Balanza de pagos BPM5|995|6.05%
04|Banco Central de Reserva|288|1.75%
05|Bolsa internacional|1|0.01%
06|Caja del tesoro|28|0.17%
07|Cotizaciones internacionales|53|0.32%
08|Cuenta financiera|119|0.72%
09|Deuda externa|69|0.42%
10|Deuda pública|206|1.25%
11|Empresas bancarias|1 591|9.67%
12|Entre 1930 a 1980|1 418|8.62%
13|Expectativas empresariales|156|0.95%
14|Expectativas Macroeconómicas|3|0.02%
15|Exportaciones e importaciones|1 482|9.01%
16|Gastos|274|1.67%
17|Indicadores Internacionales|29|0.18%
18|Indicadores de coyuntura|21|0.13%
19|Inflación|99|0.60%
20|Ingresos|283|1.72%
21|Mercado de capitales|218|1.33%
22|Mercado inmobiliario|28|0.17%
23|Moneda y crédito|111|0.67%
24|Operaciones de las empresas bancarias|106|0.64%
25|Otras cuentas monetarias|303|1.84%
26|Otros no categorizados|30|0.18%
27|PBI gasto|134|0.81%
28|PBI por sectores|538|3.27%
29|PBI y demografía|48|0.29%
30|Periodo colonial tardío|244|1.48%
31|Periodo colonial temprano|289|1.76%
32|Posición de activos y pasivos|86|0.52%
33|Precios|12|0.07%
34|Precios y tarifas|12|0.07%
35|Presupuesto público|4|0.02%
36|Primera centuria independiente|596|3.62%
37|Producción|1 449|8.81%
38|Remuneraciones y empleo|35|0.21%
39|Renta de factores|36|0.22%
40|Resultados de la balanza de pagos|104|0.63%
41|Resultado económico|395|2.40%
42|Sector público|1 195|7.27%
43|Servicios|54|0.33%
44|Sistema financiero|642|3.90%
45|Sistemas de pagos|1 058|6.43%
46|Sociedades creadoras de depósito|489|2.97%
47|Tasas de interés|235|1.43%
48|Tasas de interés internacionales|26|0.16%
49|Tipo de cambio|12|0.07%
50|Tipo de cambio de otras divisas|24|0.15%
51|Tipo de cambio nominal|81|0.49%
52|Tipo de cambio real|29|0.18%
53|Términos de intercambio|26|0.16%
54|Índice de reajuste diario|1|0.01%

Ejemplo
>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01270PM

### Formato de salida

>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/../[__formato de salida__]/../../..

Existen 7 formatos de salida disponibles para el API del BCRP y son:

Formato | Código para API|ejemplo
:-------|:-------|-------|
HTML|../html|https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/html
GRÁFICO|../grafico|https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/grafico
XLS|../xls| https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/xls
XML|../xml|https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/xml
JSON Y JSONP|../json|https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/json
TXT|../txt|https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/txt
CSV|../csv|https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/csv


### Periodo inicial y final

La ubicación de estos parámetros en la estructura del API es la siguiente:

>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/../../[__periodo inicial__]/[__periodo final__]/..

Con este parámetro se indica el periodo de tiempo, de la consulta de datos que se realiza a la API. Si no se coloca ningún datoa en estos espacios, se entiende que la consulta se realizara para los datos actuales.

Si se ingresa solo un periodo, la API respondera información solo de dicho periodo.

Ejemplos

- Un solo periodo
>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/csv/2016-9

- Un periodo inicial y final
>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/grafico/2010-1/2016-9/esp

- Sin periodo definido
>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM


### Idioma

La ubicación del parámetro correspondiente al idioma, dentro del API es la siguiente:

>https://estadisticas.bcrp.gob.pe/estadisticas/series/api/../../../../[__idioma__]

La API del BCRP soporta dos idiomas:
Idioma|Código|Ejemplo
:-------|:-----------|:-------|
Español|Sin necesidad de agregar algo|https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM-PN01289PM/csv/2010-1/2016-9
Ingles|../ing|https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/json/2010-1/2016-9/ing
-----

#### FUENTE

_Esta sección se construyo en base a la información disponible del BCRP en las siguientes páginas_

- [API para desarrolladores](https://estadisticas.bcrp.gob.pe/estadisticas/series/ayuda/api)
- [Metadatos](https://estadisticas.bcrp.gob.pe/estadisticas/series/ayuda/metadatos)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Construido con

<a href="https://pandas.pydata.org/docs/#">
  <img src="https://i.ytimg.com/vi/uFP-W_9UtfQ/maxresdefault.jpg" height=55> 
</a>
<br>
<div style="background-color: white; width: 190px; height: 35px;">
  <a href="https://openpyxl.readthedocs.io/en/stable/">
    <img src="https://openpyxl.readthedocs.io/en/stable/_static/logo.png" alt="Logo de OpenPyXL">
  </a>
</div>
<br>
<a href="https://requests.readthedocs.io/en/latest/">
  <img src="https://essentecla.com/wp-content/uploads/2022/03/python-request.jpeg" height=55> 
</a>
<br>
<a href="https://tqdm.github.io/docs/tqdm/">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEKuR3U-H-sWOyabOO3uUbcv2OeXEysQt4QA&s" height=55> 
</a>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Instalación

Este proyecto puede ser instalado directamente a su entorno virtual de trabajo.

La instalación se puede realizar de la siguiente manera:

- Desde una terminal

   ```sh
   (.venv) pip install usebcrp
   ```

- Desde Jupyter o Google Colaboratory
   ```py
   !pip install usebcrp
   ```
Ejecutando los códigos anteriores, automáticamente se realizara la instalación de los paquetes complementarios a __usebcrp__. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
### Uso
-------
<br>

La biblioteca de python, se puede usar de la siguiente manera:

1.- Se puede consultar en los metadatos, el nombre de una variable que se quiera descargar la información.

2.- Se puede descargar la información que expone el API del BCRP

Es importante señalar, que para el uso de la biblioteca "usebcrp" no necesitamos realizar alguna modificación en la API, dado que el paquete automaticamente gestiona la construcción del API para realizar las consultas. Esto lo realiza de acuerdo a los parametros que ingresemos.


### I.- Consulta a los metadatos

Para realizar la consulta a los metadatos de la existencia de un indicador que pueda ser expuesta por la API, se procede de la siguiente manera.

- Instanciamos la clase

```py
from usebcrp import BCRP

client_bcrp = BCRP()
```

- Luego de instanciar la clase, hacemos uso del metodo browse(), en este método se puede poner el texto del nombre de cualquier indicador que se quiera filtrar.

```py
series = client_bcrp.browse("pesca")
```

- Luego hacemos una impresión del objeto y sus columnas.

```py
# Imprimimos las variables
print(series.columns)

# Imprimimos los datos
print(series)
```

- Ejemplo completo

```py
from usebcrp import BCRP

client_bcrp = BCRP()
series = client_bcrp.browse("pesca")

print(series.columns)

print(series)
```
Este codigo se puede ejecutar en un archivo ejemplo.py llamandolo desde la terminal.

```sh
(.venv) python ejemplo.py
```

Los resultados mostrados son los siguientes:

<img src=https://i.ibb.co/1Jsjr5p6/Shared-Screenshot.jpg>

<img src="https://i.ibb.co/WvsyFc3C/Shared-Screenshot1.jpg">





_Nota_: El objetivo de este proceso, se centra en conocer la existencia de un indicador que se quiere descargar desde la API del BCRP, realizando una consulta a los metados del BCRP.


### II.- Descarga de la información

Una vez que se tenga identificado el indicador que se quiere descagar, podemos solicitar la información para luego exportarlo en un formato determinado.

- __Instanciamos la clase BCRP__

En este aspecto, se debe mencionar que los atributos de la clase BCRP son:

Atributos|Tipo de dato|Descripción|Valor por defecto
:-------|:-------|:-------|:-------|
__cachepath__|str, optional|Directory to cache API responses and export files.| None
__verbose__|bool, optional|If True, print debug messages.|False
__sleep_sec__|float, optional|Seconds to sleep after downloading to avoid overloading the server|1.0
<br>

Entonces vamos a instanciar la clase BCRP() de la siguiente manera:

```py
from usebcrp import BCRP

client_bcrp = BCRP(cachepath="cache_bcrp", verbose=True)
```

Se instancia en client_bcrp la clase BCRP(), con los atributos cachepath="cache_bcrp" que indica la creación de una carpeta que lleva este nombre; y el atributo "verbose=True" que permite que se muestren el procedimiento. En esta situación, no se instancio "sleep_sec", sin embargo, por defecto toma el valor de "1.0".

- __Se hace uso del metodo "stat()" de la clase BCRP__

En esta etapa, se llama el método stat() para descargar la información que se identificó con ayuda del metodo browse() o simplemente que ya se tenia mapeado anteriormente.

En este método, se puede ingresar el codigo de una serie o de varias series, asimismo, también se señala el periodo de tiempo que se quiere consultar.

Los argumentos de la función stat() son:

Argumentos|Tipo de variable|Descripción|Valor por defecto
:-------|:-------|:-------|:-------|
series|List|List of series codes to request||
range|str, optional|Date range as a string|None
<br>

La lista de codigos de los indicadores que se quieren consultar, se deben poner entre comillas y separadas por una coma dentro de corchetes. Para el caso de range, se tiene que agregar el periodo de tiempo dentro de comillas y separadas por un espacio, empezando por el año seguidos por el mes. 

```py
...
df_stat = client_bcrp.stat(series=["PN38706PM", "PN38707PM"], range="2013-1 2024-9")
```

Luego podemos imprimir los resultados.

```py
print("\n DataFrame from stat:")
print(df_stat.head())
```

Resultados

<img src="https://i.ibb.co/LDJ5pVCY/resultados.jpg">


- __Exportamos los resultados obtenidos__

Se hace uso del método export_df(), diseñado para exportar los datos en diferentes formatos como csv, xlsx y dta. Los argumentos del método son los siguientes:

Argumentos|Tipo de variable|Descripción|Valor por defecto
:-------|:-------|:-------|:-------|
df|pd.DataFrame|DataFrame to export||
filename|str|Base file name(without extensión)||
fmt|str, optional|Export format: "csv", "xlsx", "dta"|"csv"|
<br>

Para exportar la información consultada, se ejecuta el siguiente código que es diferente para cada extensión.

En formato .csv
```py
client_bcrp.export_df(df_stat, filename="data_stat", fmt="csv")
```
En formato .xlsx
```py
client_bcrp.export_df(df_stat, filename="data_stat", fmt="xlsx")
```
En formato .dta
```py
client_bcrp.export_df(df_stat, filename="data_stat", fmt="dta")
```

Los resultados de los códigos de exportación, se presentan a continuación:

<img src="https://i.ibb.co/gLZKNdMY/Exportamos-Archivos.jpg">

<br>

- __Ejemplo completo__

```py
from usebcrp import BCRP

client = BCRP(cachepath="cache_bcrp", verbose=True)
df_stat = client.stat(series=["PN38706PM", "PN38707PM"], range="2013-1 2024-9")
print("DataFrame from stat:")
print(df_stat.head())

client.export_df(df_stat, filename="data_stat", fmt="csv")
client.export_df(df_stat, filename="data_stat", fmt="xlsx")
client.export_df(df_stat, filename="data_stat", fmt="dta")
```

### III.- Exportamos una tabla de variaciones

Para esta sección, se hara uso del método table() de la clase BCRP que tiene los siguientes argumentos:

Argumentos|Tipo de variable|Descripción|Valor por defecto
:-------|:-------|:-------|:-------|
series|list|List of series codes to request.||
range|str, optional|Date range as a string (e.g., "2013-1 2024-9").|None|
names|list, optional|New names for the columns (must match the length of series).|None|
freq|str, optional|Resampling frequency (e.g., "ME" for month end, "MS" for month start, "QE" for quearter end, "QS" for quarter start, "YE" for year end, "YS" for year start).|None|
collapse|function, str, list, or dict, optional|Aggregation function for resampling. Required if freq is specified.|None|
variation|int of str, optional| If an integer, the number of months to shift for percent change; otherwise, passed directly to pct_change.|None|
resample_kwargs|dict, optional|Additional keyword arguments for DataFrame.resample.|None|
agg_kwargs|dict, optional|Additional keyword arguments for DataFrame.aggregate.|None|

<br>

El código completo que hace uso del método table() es el siguiente:

```py
# Importamos la clase BCRP()
from usebcrp import BCRP

# Instanciamos la clase BCRP
client_bcrp = BCRP(cachepath="cache_client_table_bcrp", verbose=True)

# Señalamos los nombres de las columnas que exportamos
names = ["IPC sin alimentos", "IPC Alimentos"]

# Llamamos al método table()
df_table = client_bcrp.table(
    series=["PN38706PM", "PN38707PM"],
    range="2013-1 2024-9",
    names=names,
    freq="ME",  # "ME" for month end; alternatives: "MS", "QE", "QS", "YE", "YS"
    collapse="mean",
    variation=1
)

# Exportamos los archivos
client_bcrp.export_df(df_stat, filename="data_stat", fmt="csv")
client_bcrp.export_df(df_stat, filename="data_stat", fmt="xlsx")
client_bcrp.export_df(df_stat, filename="data_stat", fmt="dta")
```

### IV.- Resultados

Los resultados se presentan a continuación

<img src="https://i.ibb.co/tTjSyPDq/resultados-Carpeta.jpg">


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contribuidores

Las contribuciones son lo que hace de la comunidad de código abierto un lugar increíble para aprender, inspirarse y crear. Cualquier contribución que hagas es **muy apreciada**.

Si tienes alguna sugerencia para mejorar esto, por favor, bifurca el repositorio y crea una solicitud de extracción. También puedes simplemente abrir una incidencia con la etiqueta "mejora". ¡No olvides darle una estrella al proyecto! ¡Gracias de nuevo!

1. Fork el proyecto
2. Crea tu Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push el Branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Principales contribuidores:

<a href="https://github.com/MaykolMedrano/usebcrp/graphs/contributors">
  <img src="https://avatars.githubusercontent.com/u/56744917?v=4" alt="contrib.rocks image" style="border-radius: 50%; width: 80px; height: 80px;"/>
</a>
<a href="https://github.com/MaykolMedrano/usebcrp/graphs/contributors">
  <img src="https://avatars.githubusercontent.com/u/51071130?v=4" alt="contrib.rocks image" style="border-radius: 50%; width: 80px; height: 80px;"/>
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## Licencia

Distributed under the Unlicense License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Como citar este repositorio




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contacto

Jelsin Palomino - [@Linkedin](https://www.linkedin.com/in/jstpalomino/) - jstpalomino@hotmail.com

Maykol Medrano - [@Linkedin](https://www.linkedin.com/in/maykolmedrano/) - maykolmedrano35@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://i.ibb.co/DH1VSw5V/forRepo.jpg

[Pandas]: https://pandas.pydata.org/static/img/pandas_white.svg
[Pandas-url]: https://pandas.pydata.org/docs/

[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 