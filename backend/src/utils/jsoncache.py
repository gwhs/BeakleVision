import os
import pwd

import orjson

cache_path = f"{pwd.getpwuid(os.getuid()).pw_dir}/.cache/beaklevision/tba"
def init_cache() -> None:
    if os.path.exists(cache_path):
        pass
    else:
        os.mkdir(cache_path)

def write_cache_json(data: str, title: str) -> None:
    init_cache()
    try:
        with open(f"{cache_path}/{title}.json", 'x') as file:
            dat = orjson.dumps(data)
            file.write(str(dat))
            file.close()
    except PermissionError:
        print(f"ERR: permission denied when trying to open {title}.json")
        

def read_cache_json(title: str) -> str | None:
    init_cache()
    try :
        with open(f"{cache_path}/{title}.json", 'r') as file:
            dat = file.read()
            file.close()
    except FileNotFoundError:
        print(f"ERR: cache file {title}.json not found")
        return None
    return dat
