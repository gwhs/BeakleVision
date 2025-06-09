from typing import Any
import aiohttp
from yarl import URL
API_URL = URL("https://www.thebluealliance.com/api/v3/")

async def tba_api_call(endpoint: str, etag: str | None = None) -> tuple[Any | bool, str | None]:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}{endpoint}") as response:
            async with session.get('http://python.org') as response:
                print(f"CODE: {response.status}")
                print(f"YAP: {await response.text()}")
                return ("to", "do")
