from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import String
from datetime import datetime

class Base(AsyncAttrs, DeclarativeBase):
    pass
