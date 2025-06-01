from fastapi import APIRouter
from pydantic import BaseModel
from types.match import Match
router = APIRouter()

class UploadResponse(BaseModel):
    code: int

@router.post("/match", response_model=UploadResponse)
def match(match: Match):
    return UploadResponse(code=200) 
