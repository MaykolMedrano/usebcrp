import hashlib
import os
import time

import requests


class ConectionBCRP:

    def __init__(self, series, range):
        self.series = series
        self.range = range

    def conectionAPI(self, cachepath, verbose, sleep_sec):
        start, end = None, None
        if self.range:
            parts = self.range.split()
            if len(parts) == 2:
                start, end = parts
            elif len(parts) == 1:
                start = parts[0]

        base_url = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
        series_str = "-".join(self.series)
        url_parts = [base_url, series_str, "json"]
        if start:
            url_parts.append(start)
            if end:
                url_parts.append(end)
        elif end:
            url_parts.append(end)
        url = "/".join(url_parts)

        if verbose:
            print(f"[URL] {url}")

        download = True
        cache_file = None
        if cachepath:
            h = hashlib.sha1(url.encode("utf-8")).hexdigest()
            cache_file = os.path.join(cachepath, f"bcrp-{h}.json")
            if os.path.exists(cache_file):
                if verbose:
                    print(f" - Using cached file: {cache_file}")
                download = False

        if download:
            if verbose:
                print(" - Downloading data...")
            response = requests.get(url)
            response.raise_for_status()
            content = response.content
            if cache_file:
                with open(cache_file, "wb") as f:
                    f.write(content)
            time.sleep(sleep_sec)
        else:
            with open(cache_file, "rb") as f:
                content = f.read()
        # print(type(content))
        return content
