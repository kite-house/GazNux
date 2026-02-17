from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import String, ForeignKey
from datetime import datetime

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Services(Base):
    __tablename__ = "services"
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[float]

class Applications(Base):
    __tablename__ = "applications"
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    name: Mapped[str] = mapped_column(String(30))
    number: Mapped[str] = mapped_column(String(18))
    comment: Mapped[str|None] = mapped_column(String(400), nullable=True)
    service_id: Mapped[int] = mapped_column(ForeignKey(Services.id))
    source: Mapped[str] = mapped_column(String(100))
    date_created: Mapped[datetime]

class Reviews(Base):
    __tablename__ = "reviews"
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    owner: Mapped[str] = mapped_column(String(30))
    text: Mapped[str] = mapped_column(String(500))
    date_created: Mapped[datetime]

    