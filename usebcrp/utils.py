import pandas as pd
import re

class ParseDates:
    def __init__(self, date_str: str):
        self.date_str = date_str

    def _parse_spanish_date(self):
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
        match = re.match(r"([A-Za-z]+)\.?(\d{4})", self.date_str.strip())
        if not match:
            return pd.NaT
        month_abbr, year = match.groups()
        month_abbr = month_abbr[:3].capitalize()
        eng_month = month_map.get(month_abbr, month_abbr)
        formatted_date = f"{eng_month}.01.{year}"
        
        return pd.to_datetime(formatted_date, format="%b.%d.%Y", errors="coerce")