from pathlib import Path

import uvicorn

from core import BeakleVision, UvicornServer
from routes import router
from utils.config import ServerConfig

CONFIG_PATH = Path(__file__).parents[1] / "config.yml"

server_config = ServerConfig(CONFIG_PATH)

app = BeakleVision(config=server_config)
app.include_router(router)

if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        access_log=True,
    )

    server = UvicornServer(config)
    server.run()
