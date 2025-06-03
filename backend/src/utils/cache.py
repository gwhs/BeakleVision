import valkey
from valkey.client import Valkey

valk = valkey.Valkey()

def check_up() -> bool:
    up = str(valk.ping())
    if up != None:
        return True
    else:
        print("WARN: valkey might be down")
        return False


def set_cache(data: str, title: str) -> None:
    check_up()
    valk.set(title,data)

def get_cache(data_name) -> str | None:
    check_up()
    dat = valk.get(data_name)
    if dat != None:
        return str(dat)
    else:
        print("ERR: empty cache")
        return None
