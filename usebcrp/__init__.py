import hashlib
import json
import os
import time
from typing import List, Optional

import pandas as pd
import requests
from tqdm import tqdm

from .metadata import Metadata
from .utils import ParseDates, _export_df

class BCRP(Metadata, ParseDates):
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
        text_inf  : str, optional
                    This text is for searching the names and codes of series's BCRP
        """
        self.cachepath = cachepath
        self.verbose = verbose
        self.sleep_sec = sleep_sec

        if self.cachepath:
            os.makedirs(self.cachepath, exist_ok=True)

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
            date_val = ParseDates(period["name"])._parse_spanish_date()
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
        return _export_df(self.cachepath, df, filename, fmt, self.verbose)
    
    def browse(self, text_inf):
        """We use the text_inf for searching the codes and names of series's BCRP

        Returns:
            _type_: _DataFrame_
        """
        return Metadata(text_inf)._browse()