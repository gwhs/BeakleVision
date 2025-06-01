import uvicorn

from core import BeakleVision

app = BeakleVision()

if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        access_log=True,
    )

    server = uvicorn.Server(config)
    server.run()
