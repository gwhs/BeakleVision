from os import cpu_count

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Status(BaseModel):
    code: int
    workers: int


@router.get("/status", response_model=Status)
def status():
    return Status(code=200,workers=cpu_count() or 1)
