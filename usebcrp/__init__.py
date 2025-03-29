import hashlib
import io
import json
import os
import re
import time
from typing import List, Optional

import pandas as pd
import requests
from tqdm import tqdm


class BCRP:
    def __init__(
        self,
        cachepath: Optional[str] = None,
        verbose: bool = False,
        sleep_sec: float = 1.0,
    ):
        """
        Initialize the BCRP client.

        Parameters
        ----------

        cachepath : str, optional
                    Directory to cache API responses and export files.
        verbose   : bool, optional
                    If True, print debug messages.
        sleep_sec : float, optional
                    Seconds to sleep after downloading to avoid overloading the server
        """
        self.cachepath = cachepath
        self.verbose = verbose
        self.sleep_sec = sleep_sec

        if self.cachepath:
            os.makedirs(self.cachepath, exist_ok=True)

    @staticmethod
    def parse_spanish_date(date_str: str) -> str:
        """
        Convert a Spanish month-year string (e.g., "Ene2020" or "Ene.2020") into a pandas Timestamp.

        Parameters
        ----------
        date_str : str
                   A string representing the month and year in Spanish.

        Returns
        -------
        pd.Timestamp
                    A pandas Timestamp or pd.NaT if parsing fails.
        """
        month_map = {
            "Ene": "Jan",
            "Feb": "Feb",
            "Mar": "Mar",
            "Abr": "Apr",
            "May": "May",
            "Jun": "Jun",
            "Jul": "Jul",
            "Ago": "Aug",
            "Sep": "Sep",
            "Oct": "Oct",
            "Nov": "Nov",
            "Dic": "Dec",
        }
        match = re.match(r"([A-Za-z]+)\.?(\d{4})", date_str.strip())
        if not match:
            return pd.NaT
        month_abbr, year = match.groups()
        month_abbr = month_abbr[:3].capitalize()
        eng_month = month_map.get(month_abbr, month_abbr)
        formatted_date = f"{eng_month}.01.{year}"
        return pd.to_datetime(formatted_date, format="%b.%d.%Y", errors="coerce")

    def stat(self, series: List[str], range: Optional[str] = None) -> pd.DataFrame:
        """
        Download BCRP data as JSON, process it, and return a DataFrame.
        Each column is named after the series code and metadata is stored in df.attrs["series_metadata"].

        Parameters
        ----------

        series : List
                 List of series codes to request.
        range  : str, optional
                 Date range as a string (e.g., "2023-1 2024-9")

        Returns
        -------

        pd. DataFrame
                  DataFrame with the processed data.
        """
        if not series:
            raise ValueError("At least one series code is required.")

        # Determine date range parts
        start, end = None, None
        if range:
            parts = range.split()
            if len(parts) == 2:
                start, end = parts
            elif len(parts) == 1:
                start = parts[0]

        base_url = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
        series_str = "-".join(series)
        url_parts = [base_url, series_str, "json"]
        if start:
            url_parts.append(start)
            if end:
                url_parts.append(end)
        elif end:
            url_parts.append(end)
        url = "/".join(url_parts)

        if self.verbose:
            print(f"[URL] {url}")

        download = True
        cache_file = None
        if self.cachepath:
            h = hashlib.sha1(url.encode("utf-8")).hexdigest()
            cache_file = os.path.join(self.cachepath, f"bcrp-{h}.json")
            if os.path.exists(cache_file):
                if self.verbose:
                    print(f" - Using cached file: {cache_file}")
                download = False

        if download:
            if self.verbose:
                print(" - Downloading data...")
            response = requests.get(url)
            response.raise_for_status()
            content = response.content
            if cache_file:
                with open(cache_file, "wb") as f:
                    f.write(content)
            time.sleep(self.sleep_sec)
        else:
            with open(cache_file, "rb") as f:
                content = f.read()

        data = json.loads(content.decode("utf-8", errors="replace"))
        if "periods" not in data:
            raise ValueError("JSON does not contain 'periods'. Unexpected structure.")
        if "config" not in data or "series" not in data["config"]:
            raise ValueError(
                "JSON does not contain 'config.series'. Unexpected structure."
            )

        title = data["config"].get("title", "")
        series_info = data["config"]["series"]
        long_names = [s["name"] for s in series_info]
        decimals = [s.get("dec", "") for s in series_info]

        rows = []
        for period in tqdm(
            data["periods"], desc="Processing periods", total=len(data["periods"])
        ):
            date_val = self.parse_spanish_date(period["name"])
            values = period["values"]
            row = {"time": date_val}
            for i, value in enumerate(values):
                col_name = long_names[i]
                try:
                    row[col_name] = float(value)
                except Exception:
                    row[col_name] = None
            rows.append(row)

        df = pd.DataFrame(rows).sort_values("time").reset_index(drop=True)
        df.set_index("time", inplace=True)
        df.attrs["title"] = title
        df.attrs["decimals"] = decimals
        meta = {code: long_names[i] for i, code in enumerate(series)}
        df.attrs["series_metadata"] = meta

        if self.verbose:
            print(f" - Detected series: {long_names}")
            print(f" - Metadata (code -> name): {df.attrs['series_metadata']}")

        rename_map = dict(zip(df.columns.tolist(), series))
        df.rename(columns=rename_map, inplace=True)

        return df

    def table(
        self,
        series: List[str],
        range: Optional[str] = None,
        *,
        names: List[str] = None,
        freq: str = None,
        collapse=None,
        variation: int = None,
        resample_kwargs: dict = None,
        agg_kwargs: dict = None,
    ) -> pd.DataFrame:
        """
        Build a DataFrame from download data (using stat) and apply additional transformations:
        renaming columns, resampling, and computing percent change.

        Parameters
        ----------
        series          : list
                        List of series codes to request.
        range           : str, optional
                        Date range as a string (e.g., "2013-1 2024-9").
        names           : list, optional
                        New names for the columns (must match the length of series).
        freq            : str, optional
                        Resampling frequency (e.g., "ME" for month end, "MS" for month start,
                                            "QE" for quearter end, "QS" for quarter start,
                                            "YE" for year end, "YS" for year start).
        collapse        : function, str, list, or dict, optional
                        Aggregation function for resampling. Required if freq is specified.
        variation       : int of str, optional
                        If an integer, the number of months to shift for percent change; otherwise, passed directly to pct_change.
        resample_kwargs : dict, optional
                          Additional keyword arguments for DataFrame.resample.
        agg_kwargs      : dict, optional
                          Additional keyword arguments for DataFrame.aggregate.

        Returns
        -------
        pd.DataFrame
                    Final DataFrame after transformations.
        """
        df = self.stat(series=series, range=range)
        df = df[[s for s in series if s in df.columns]]

        if names:
            if len(names) != len(series):
                raise ValueError("Names length must match series length.")
            rename_dict = dict(zip(series, names))
            df = df.rename(columns=rename_dict)

        if freq:
            if not collapse:
                raise ValueError(
                    "An aggregation function (collapse) must be specified when resampling."
                )
            resample_kwargs = resample_kwargs or {}
            agg_kwargs = agg_kwargs or {}
            df = df.resample(freq, **resample_kwargs).aggregate(collapse, **agg_kwargs)

        if variation:
            shift_val = (
                pd.DateOffset(months=variation)
                if isinstance(variation, int)
                else variation
            )
            df = df.pct_change(freq=shift_val)

        return df

    def export_df(self, df: pd.DataFrame, filename: str, fmt: str = "csv"):
        """
        Export the DataFrame to a file in CSV, XLSX, or DTA format.
        The file is saved in the cachepath if provided.

        Parameters
        ----------
        df          : pd.DataFrame
                      DataFrame to export.
        filename    : str
                      Base file name (without extensión).
        fmt         : str, optional
                      Export format: "csv", "xlsx", or "dta" (default is "csv")
        """
        if self.cachepath:
            filepath = os.path.join(self.cachepath, f"{filename}.{fmt}")
        else:
            filepath = f"{filename}.{fmt}"

        fmt = fmt.lower()
        if fmt == "csv":
            df.to_csv(filepath)
        elif fmt == "xlsx":
            df.to_excel(filepath)
        elif fmt == "dta":
            df.to_stata(filepath)
        else:
            raise ValueError("Unsupported format. Use 'csv', 'xlsx', or 'dta'.")

        if self.verbose:
            print(f"Exported data in {fmt.upper()} format to: {filepath}")


# Variable global para almacenar en caché el DataFrame descargado
_BCRP_DATA_CACHE = None


def load_bcrp_metadata() -> pd.DataFrame:
    """
    Descarga y carga los metadatos desde el BCRP en un DataFrame.

    Returns
    -------
    pd.DataFrame
                DataFrame con los metadatos de las series
    """
    url = "https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "*/*",
        "Referer": "https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata",
    }
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 200:
        # Se asume que requests maneja automaticamente la descompresión gzip.
        df = pd.read_csv(
            io.BytesIO(response.content), encoding="latin-1", delimiter=";"
        )
        return df
    else:
        raise Exception(
            f"Error al descargar los datos. Código de estado: {response.status_code}"
        )


def browse(contains: str, cache: bool = True) -> pd.DataFrame:
    """
    Busca series en el DataFrame de metadatos usando un orden de prioridad:
    primero se evalúa "Nombre de serie", y si no hay coincidencia, se revisan las
    columnas "Categoria de serie", "Grupo de serie" y "Grupo de publicación" (en ese orden).

    Parameters
    ----------
    contains        : str
                      Cadena de texto o expresión regular para buscar en los campos de la serie.
    cache           : bool, optional
                      Si es True, utiliza datos en caché (si ya se descargaron) para evitar descargas repetitivas
                      por defecto es True.

    Returns
    -------
    pd.DataFrame
                      DataFrame filtrado con las series que coinciden con la busqueda, según la prioridad.
    """
    global _BCRP_DATA_CACHE

    # Uso de caché si ya esta disponible
    if cache and _BCRP_DATA_CACHE is not None:
        df = _BCRP_DATA_CACHE
    else:
        df = load_bcrp_metadata()
        if cache:
            _BCRP_DATA_CACHE = df

    # Definir el orden de prioridad para las columnas de búsqueda.
    priority_columns = [
        "Codigo de serie",
        "Nombre de serie",
        "Categoria de serie",
        "Grupo de serie",
        "Grupo de publicación",
        "Fuente",
        "Frecuencia",
        "Área que publica",
    ]

    # Se busca en cada columna, siguiendo el orden de prioridad.
    for col in priority_columns:
        if col in df.columns:
            result = df[
                df[col].astype(str).str.contains(contains, case=False, na=False)
            ].reset_index(drop=True)
            if not result.empty:
                return result

    # Si no se enceuntra en ninguna columna, se retorna un DataFrame vacio.
    return pd.DataFrame()
