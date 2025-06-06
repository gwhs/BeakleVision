API_URL = "https://www.thebluealliance.com/api/v3/"
from typing import Any

import requests


def tba_api_call(endpoint: str, etag: str | None = None) -> tuple[Any | bool, str | None]:
    if etag is not None:
        data = requests.get(f"{API_URL}/{endpoint}", 
            headers={
            "Etag": "",
            "X-TBA-Auth-Key": "",
            "If-None-Match": "",
            },
            timeout=10
            )
        if data.status_code == 304:
            # no change
            return ("","foo") # I need the caching pr to be merged so it returns nonesense for now

        if data.status_code == 200:
            return (data.headers.get("Etag"),data.text)
    return ("deez", "yk what")

