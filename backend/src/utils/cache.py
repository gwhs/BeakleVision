import jsoncache
import valkey
from valkey.exceptions import ConnectionError as ValkeyConnectionError # I HATE THIS STUPID BS WHY ARE THERE MULTIPLE CONNECTION ERRORS ISWTG THIS IS THE STUPIDEST BUG EVER,
# I SPENT 2 HOURS FIGURING THIS OUT FML
from typing import Any

conn = valkey.Valkey()


async def set_cache(data: dict[str, Any], title: str, write_json: bool) -> None:

    try:
        await conn.ping()
    except ValkeyConnectionError:
        print("ERR: Valkey server is down")
        return


    return None

    if write_json:
        jsoncache.write_cache_json(data,title)
    dat = str(await conn.set(title,str(data)))
    if dat is None:
        return None
    elif dat is not None:
        print(f"ERR: {title} had an issue when writing to valkey cache")


async def get_cache(data_name: str, check_json: bool) -> str | None:
    if await conn.ping():
        exit(1)

    if check_json:
        json_data = jsoncache.read_cache_json(data_name)
        if json_data is not None:
            return json_data
    dat = conn.get(data_name)
    if dat is not None:
        return str(dat)
    else:
        print(f"ERR: {data_name} does not exist in valkey cache")
        return None
