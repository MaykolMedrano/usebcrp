# `usebcrp` : download data from the Peruvian Central Bank into Stata

## Installation

```
cap ado uninstall usebcrp 
net install usebcrp, from(https://raw.githubusercontent.com/MaykolMedrano/usebcrp/master/source)
```

## Usage

First, go [here](https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales) and pick a series (or up to 10). Then, run:

```stata
usebcrp PN00001MM, range(2001m1 2016m12)
```

## Advanced Usage

- Use a folder as cache, to avoid downloading the dataset every time: `usebcrp	PN00001MM, range(2001m1 2016m12) cache(c:/somepath)`
- Can also manage different frequencies (daily, monthly, quarterly, annual).

- More information in the help file

