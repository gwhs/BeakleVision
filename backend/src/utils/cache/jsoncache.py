# not to be confused with the stdlib json
import os
from pathlib import Path
from typing import Any

import aiofiles
import orjson

cache_path = Path(__file__).home() / ".cache" / "beaklevision" / "tba"
def init_cache() -> None:
    if os.path.exists(cache_path):
        pass
    else:
        os.mkdir(cache_path)

async def write_cache_json(data: dict[str,Any], title: str) -> None:
    init_cache()
    try:
        async with aiofiles.open(f"{cache_path}/{title}.json", 'x') as file:
            dat = orjson.dumps(data)
            await file.write(str(dat))
            await file.close()
    except PermissionError:
        print(f"ERR: permission denied when trying to open {title}.json")
        

async def read_cache_json(title: str) -> str | None:
    init_cache()
    try :
        async with aiofiles.open(f"{cache_path}/{title}.json", 'r') as file:
            contents = await file.read()
            dat = orjson.loads(contents)
            await file.close()
    except FileNotFoundError:
        print(f"ERR: cache file {title}.json not found")
        return None
    return dat
