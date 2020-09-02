# `usebcrp` : download data from the Peruvian Central Bank into Stata

## Installation

```
cap ado uninstall usebcrp 
net install usebcrp, from(https://raw.githubusercontent.com/MaykolMedrano/usebcrp/master/source)
```
## System Requirements

Windows 10

## Usage

First, go [here](https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales) and pick a series (or up to 10). Then, run:

```stata
usebcrp PN00001MM, range(2001m1 2016m12)
usebcrp PN01288PM PN01289PM, range(2013m1 2016m9)
```
```
usebcrp PN03492MQ, range(2013q1 2016q4)
usebcrp PD04658MD, clear range(1jan1999 31dec2002)
```
usebcrp PM06069MA, clear range(2007 2009)
```
## Advanced Usage

- Use a folder as cache, to avoid downloading the dataset every time: `usebcrp	PN00001MM, range(2001m1 2016m12) cache(c:/somepath)`
- Can also manage different frequencies (daily, monthly, quarterly, annual).

- More information in the help file.

