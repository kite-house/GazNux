from fastapi import FastAPI
from contextlib import asynccontextmanager

'''from src.app.api.shortener import router as shortener_router
from src.app.db.db import engine
from src.app.db.models import Base'''

'''@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield'''

app = FastAPI(
    title = 'GazNux',
    description= '-',
    lifespan=lifespan
)

app.include_router(shortener_router)