from fastapi import APIRouter, HTTPException, status, Query, Depends
from typing import Annotated
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.dependencies import get_session
from src.app.schemas.application_schema import Application as AppSchema
from src.app.db import crud

router = APIRouter()


@router.post('/application')
async def create_application(
    session: Annotated[AsyncSession, Depends(get_session)],
    data: AppSchema
):
    
    await crud.write_application(session, data)

    return {"status" : "Успешно!", "message": "Заявка успешно создана!"}
