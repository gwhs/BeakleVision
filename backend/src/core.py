import os
import signal
import socket
from typing import Any, Optional

import orjson
import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.openapi.utils import get_openapi
from fastapi.responses import ORJSONResponse, Response
from fastapi.utils import is_body_allowed_for_status_code

from utils.config import ServerConfig
from utils.handler import InterruptHandler
from utils.responses.exceptions import (
    HTTPExceptionResponse,
    RequestValidationErrorResponse,
)

if os.name == "nt":
    from winloop import new_event_loop, run
else:
    from uvloop import new_event_loop, run

__title__ = "BeakleVision"
__description__ = """Docs"""
__version__ = "0.1.0a"


# Wrapper around uvicorn.Server to handle and force load uvloop/winloop
# Ensures that SIGINT and SIGTERM signals are handled. E.g., CTRL+C
class UvicornServer(uvicorn.Server):
    def __init__(self, config: uvicorn.Config):
        super().__init__(config)

    def run(self, sockets: Optional[list[socket.socket]] = None) -> None:
        self.loop = new_event_loop()
        handler = InterruptHandler(server=self, sockets=sockets)

        self.loop.add_signal_handler(signal.SIGINT, handler)
        self.loop.add_signal_handler(signal.SIGTERM, handler)
        return run(self.serve(sockets=sockets))


class BeakleVision(FastAPI):
    def __init__(self, *, config: ServerConfig):
        super().__init__(
            title=__title__,
            description=__description__,
            version=__version__,
            default_response_class=ORJSONResponse,
            responses={400: {"model": RequestValidationErrorResponse}},
            http="httptools",
            redoc_url="/docs",
            docs_url=None,
        )
        self.config = config

        self.add_exception_handler(
            HTTPException,
            self.http_exception_handler,  # type: ignore
        )
        self.add_exception_handler(
            RequestValidationError,
            self.request_validation_error_handler,  # type: ignore
        )

    ### Exception Handlers

    async def http_exception_handler(
        self, request: Request, exc: HTTPException
    ) -> Response:
        headers = getattr(exc, "headers", None)
        if not is_body_allowed_for_status_code(exc.status_code):
            return Response(status_code=exc.status_code, headers=headers)
        message = HTTPExceptionResponse(detail=exc.detail)
        return ORJSONResponse(
            content=message.model_dump(), status_code=exc.status_code, headers=headers
        )

    async def request_validation_error_handler(
        self, request: Request, exc: RequestValidationError
    ) -> ORJSONResponse:
        encoded = orjson.dumps(exc.errors()).decode("utf-8")
        message = RequestValidationErrorResponse(errors=encoded)
        return ORJSONResponse(
            content=message.model_dump(), status_code=status.HTTP_400_BAD_REQUEST
        )

    def openapi(self) -> dict[str, Any]:
        if not self.openapi_schema:
            self.openapi_schema = get_openapi(
                title=self.title,
                version=self.version,
                openapi_version=self.openapi_version,
                description=self.description,
                terms_of_service=self.terms_of_service,
                contact=self.contact,
                license_info=self.license_info,
                routes=self.routes,
                tags=self.openapi_tags,
                servers=self.servers,
            )
            for path in self.openapi_schema["paths"].values():
                for method in path.values():
                    responses = method.get("responses")
                    if str(status.HTTP_422_UNPROCESSABLE_ENTITY) in responses:
                        del responses[str(status.HTTP_422_UNPROCESSABLE_ENTITY)]
        return self.openapi_schema
