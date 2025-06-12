from types import TracebackType
from typing import Any, Optional, Self, Type, TypeVar

import orjson
import valkey.asyncio as valkey
from argon2 import PasswordHasher
from pydantic import BaseModel
from valkey.asyncio import ConnectionPool, Valkey

BE = TypeVar("BE", bound=BaseException)

import utils.cache.jsoncache as jsoncache

conn = valkey.Valkey()


class ValkeyCache:
    def __init__(self, *, pool: ConnectionPool):
        self.client = Valkey(connection_pool=pool)

        self._ph = PasswordHasher()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BE]],
        exc: Optional[BE],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.client.aclose(close_connection_pool=True)

    def _build_key(self, endpoint: str, *, event: str, match: int) -> str:
        return f"{event}:m{match}:{endpoint}"

    ### CRUD operations

    async def set(
        self, data: BaseModel, *, endpoint: str, ttl: Optional[int] = 60
    ) -> Optional[Any]:
        return await self.client.set(
            name="", value=orjson.dumps(data.model_dump()), ex=ttl, get=True
        )

    async def get(self, key: str) -> Optional[Any]:
        return await self.client.get(key)


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
