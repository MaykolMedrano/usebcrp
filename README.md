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
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    &middot;
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

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

>https://../../../../[__códigos de series__]/../../../..

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

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
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  (.venv) pip install usebcrp
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/othneildrew/Best-README-Template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=othneildrew/Best-README-Template" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

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