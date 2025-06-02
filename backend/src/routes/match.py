from types.match import Match

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class UploadResponse(BaseModel):
    code: int


@router.post("/match/create", responses={200: {"model": UploadResponse}})
async def match(match: Match) -> UploadResponse:
    return UploadResponse(code=200)
