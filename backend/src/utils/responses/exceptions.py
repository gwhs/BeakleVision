from pydantic import BaseModel


### Error responses
class ErrorResponse(BaseModel, frozen=True):
    result: str = "error"
    detail: str


### Responses for HTTP 400-499 status codes


# HTTP 400
class BadRequestResponse(ErrorResponse, frozen=True):
    detail: str


# HTTP 404
class NotFoundResponse(ErrorResponse, frozen=True):
    detail: str = "Resource not found"


# HTTP 409
class ConflictResponse(ErrorResponse, frozen=True):
    detail: str


# HTTP 400/422
class RequestValidationErrorResponse(BaseModel, frozen=True):
    result: str = "error"
    errors: str


# Any status codes
class HTTPExceptionResponse(ErrorResponse, frozen=True):
    detail: str
