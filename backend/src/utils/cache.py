import jsoncache
import valkey

conn = valkey.Valkey()

async def check_up():
    try:
        foo = await conn.ping()
        if not foo:
            raise ConnectionError
    except Exception:
        raise ConnectionError

async def set_cache(data: str, title: str, write_json: bool) -> None | ConnectionError:
    try:
     await check_up()
    except ConnectionError:
        print("ERR: Valkey is DOWN")
        exit(1)
    if write_json:
        jsoncache.write_cache_json(data,title)
    dat = str(await conn.set(title,data))
    if dat is None:
        return None
    elif dat is not None:
        print(f"ERR: {title} had an issue when writing to valkey cache")


async def get_cache(data_name: str, check_json: bool) -> str | None:
    await check_up()
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
