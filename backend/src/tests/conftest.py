from pathlib import Path
from types import TracebackType
from typing import AsyncGenerator, Generator, NamedTuple, Optional, Self, Type, TypeVar
from urllib.parse import quote

import httpx
import pytest
import pytest_asyncio
import valkey
import valkey.exceptions
from asgi_lifespan import LifespanManager
from testcontainers.cockroachdb import CockroachDBContainer
from testcontainers.core.container import DockerContainer
from testcontainers.core.exceptions import ContainerStartException
from testcontainers.core.utils import raise_for_deprecated_parameter
from testcontainers.core.waiting_utils import wait_container_is_ready, wait_for_logs
from yarl import URL

from core import BeakleVision
from utils.config import ServerConfig

BE = TypeVar("BE", bound=BaseException)

ROOT = Path(__file__).parents[2]
CONFIG_PATH = ROOT / "config.yml"

config = ServerConfig(CONFIG_PATH)

### Types


class BeakleServices(NamedTuple):
    cockroach: CockroachDBContainer
    valkey: "ValkeyContainer"


### Overridden generic docker test containers


class ValkeyContainer(DockerContainer):
    def __init__(
        self,
        image: str = "valkey/valkey:latest",
        port: int = 6379,
        password: Optional[str] = None,
        **kwargs,
    ) -> None:
        raise_for_deprecated_parameter(kwargs, "port_to_expose", "port")
        super().__init__(image, **kwargs)
        self.port = port
        self.password = password
        self.with_exposed_ports(self.port)
        if self.password:
            self.with_command(f"valkey-server --requirepass {self.password}")

    @wait_container_is_ready(valkey.exceptions.ConnectionError)
    def _connect(self) -> None:
        client = self.get_client()
        if not client.ping():
            raise valkey.exceptions.ConnectionError("Could not connect to Valkey")

    def get_client(self, **kwargs) -> valkey.Valkey:
        return valkey.Valkey(
            host=self.get_container_host_ip(),
            port=self.get_exposed_port(self.port),
            password=self.password,
            **kwargs,
        )

    def get_connection_url(self, dbname: Optional[str] = None) -> str:
        if self._container is None:
            raise ContainerStartException("container has not been started")

        host = self.get_container_host_ip()
        port = self.get_exposed_port(self.port)
        url = f"valkey://{host}:{port}"

        if self.password:
            quoted_password = quote(self.password, safe=" +")
            url = f"valkey://default:{quoted_password}@{host}:{port}"

        if dbname:
            url = f"{url}/{dbname}"
        return url

    def start(self) -> Self:
        super().start()
        self._connect()
        return self


### Test client


class BeakleTestClient:
    def __init__(self, app: BeakleVision):
        self._host = app.config["beakle"]["host"]
        self._port = app.config["beakle"]["port"]
        self._transport = httpx.ASGITransport(app=app, client=(self._host, self._port))
        self.client = httpx.AsyncClient(
            transport=self._transport,
            base_url=str(URL.build(scheme="http", host=self._host, port=self._port)),
        )

    async def close(self) -> None:
        await self.client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BE]],
        exc: Optional[BE],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.close()


### Function and session fixtures


@pytest.fixture(scope="session")
def get_app() -> BeakleVision:
    return BeakleVision(config=config)


@pytest.fixture(scope="session")
def setup() -> Generator[BeakleServices, None]:
    with (
        CockroachDBContainer(
            image="cockroachdb/cockroach:latest-v25.2", dialect="cockroachdb+asyncpg"
        ) as cockroach,
        ValkeyContainer() as valkey,
    ):
        wait_for_logs(cockroach, "end", timeout=15.0)
        wait_for_logs(valkey, "accept connections tcp", timeout=15.0)
        yield BeakleServices(cockroach, valkey)


@pytest_asyncio.fixture(scope="function")
async def app(
    get_app: BeakleVision, setup: BeakleServices
) -> AsyncGenerator[BeakleTestClient, None]:
    get_app.config["cockroach_uri"] = setup.cockroach.get_connection_url()
    get_app.config["valkey_uri"] = setup.valkey.get_connection_url()

    async with (
        LifespanManager(app=get_app),
        BeakleTestClient(app=get_app) as client,
    ):
        yield client
