from typing import Any

import orjson
import valkey.asyncio as valkey

import utils.cache.jsoncache as jsoncache

conn = valkey.Valkey()


async def set_cache(data: dict[str, Any], title: str, write_json: bool) -> None:
    if write_json:
        await jsoncache.write_cache_json(data, title)
    dat = str(await conn.set(title, orjson.dumps(data)))
    if dat is None:
        return None
    elif dat is not None:
        print(f"ERR: {title} had an issue when writing to valkey cache")


async def get_cache(data_name: str, check_json: bool) -> str | None:
    if await conn.ping():
        exit(1)

    if check_json:
        json_data = await jsoncache.read_cache_json(data_name)
        if json_data is not None:
            return json_data
    dat = conn.get(data_name)
    if dat is not None:
        return str(dat)
    else:
        print(f"ERR: {data_name} does not exist in valkey cache")
        return None
