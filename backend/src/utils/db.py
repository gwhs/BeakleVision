from typing import AsyncGenerator

import sqlalchemy
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from utils.request import RouteRequest


async def session(request: RouteRequest) -> AsyncGenerator[AsyncSession, None]:
    """Function that yields an `AsyncSession`, which is utilized to access the database in FastAPI routes

    Args:
        request (RouteRequest): Subclassed instance of `fastapi.Request` that allows for obtaining server attributes

    Raises:
        HTTPException: HTTP 409 exception if the bound session creates an `IntegrityError`

    Returns:
        AsyncGenerator[AsyncSession, None]: Instance of `AsyncSession`

    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]: yields an instance of `AsyncSession`, used for database operations
    """
    async with request.app.get_session() as session:
        try:
            yield session
        except sqlalchemy.exc.IntegrityError:
            await session.rollback()
            raise HTTPException(status_code=409, detail="Conflict")
        except Exception:
            await session.rollback()
            raise RuntimeError("Unexpected error")
