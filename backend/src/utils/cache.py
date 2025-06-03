import jsoncache
import valkey

valk = valkey.Valkey()

def check_up() -> bool:
    up = str(valk.ping())
    if up is not None:
        return True
    else:
        print("WARN: valkey might be down")
        return False


def set_cache(data: str, title: str, write_json: bool) -> None:
    check_up()
    if write_json:
        jsoncache.write_cache_json(data,title)
    dat = str(valk.set(title,data))
    if dat is None:
        return None
    elif dat is not None:
        print(f"ERR: {title} had an issue when writing to valkey cache")


def get_cache(data_name, check_json: bool) -> str | None:
    check_up()
    if check_json:
        jsoncache.read_cache_json(data_name)
    else:
        pass
    dat = valk.get(data_name)
    if dat is not None:
        return str(dat)
    else:
        print(f"ERR: {data_name} does not exist in valkey cache")
        return None
