from pathlib import Path

from core import BeakleVision
import uvicorn

app = BeakleVision()

if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        access_log=True,
    )

    server = uvicorn.Server(config)
    server.run()