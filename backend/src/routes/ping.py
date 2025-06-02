from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/ping", include_in_schema=False)
async def ping() -> Response:
    return Response("pong")
