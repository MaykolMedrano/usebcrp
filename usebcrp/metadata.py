import io

import pandas as pd
import requests

# Variable global para almacenar en caché el DataFrame descargado
_BCRP_DATA_CACHE = None


class Metadata:
    def __init__(self, text_inf: str):
        """
        Initialize Metadata

        Parameters
        ----------
        text_inf : str
                   In this text, we write the variables for searching in BCRP and result the list of the search
        """
        self.text_inf = text_inf

    @staticmethod
    def _load_bcrp_metadata() -> pd.DataFrame:
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

    def _browse(self, cache: bool = True) -> pd.DataFrame:
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
            df = self._load_bcrp_metadata()
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
                    df[col]
                    .astype(str)
                    .str.contains(self.text_inf, case=False, na=False)
                ].reset_index(drop=True)
                if not result.empty:
                    return result

        # Si no se enceuntra en ninguna columna, se retorna un DataFrame vacio.
        return pd.DataFrame()
