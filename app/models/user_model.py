from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import String
from sqlalchemy.types import UUID
import uuid


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True))
    username: Mapped[str] = mapped_column(unique=True)
    fullname: Mapped[str]
    email: Mapped[str]= mapped_column(unique=True)
    phone: Mapped[str]
    password: Mapped[str]

    # Define relationship(s)
    profile = relationship("UserProfile", uselist=False, back_populates="user")


    def __repr__(self) -> str:
        return f"""User(
            id={self.id!r},
            uuid={self.uuid!r},
            username={self.username!r},
            fullname={self.fullname!r},
            email={self.email!r},
            phone={self.phone!r},
            profile={self.profile!r}
        )"""
    