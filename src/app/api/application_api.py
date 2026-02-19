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
    
    try:
        await crud.write_application(session, data)
    except Exception as error:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Возникла ошибка на стороне сервера!')

    return {"status" : "Успешно!", "message": "Заявка успешно создана!"}