from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String
from sqlalchemy.types import UUID
import uuid


class Base(DeclarativeBase):
    pass


class User(Base):
    __table__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    fullname: Mapped[str]
    email: Mapped[str]