import pathlib

import setuptools

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

# from usebcrp.__version__ import __version__ as pkgVersion

setuptools.setup(
    name="usebcrp",
    version="0.0.1",
    author="Jelsin Palomino & Maykol Medrano",
    author_email="maykolmedrano35@gmail.com & jstpalomino@hotmail.com",
    description="Python library that consumes the BCRP API, you can query the series and define the time range.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MaykolMedrano/usebcrp",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: Microsoft",
        "Intended Audience :: Education",
    ],
    install_requires=["pandas", "requests", "tqdm", "openpyxl"],
    keywords=[
        "Perú",
        "Peru",
        "BCRP",
        "Banco Central de Reservas del Perú",
        "Series de tiempo",
    ],
)
