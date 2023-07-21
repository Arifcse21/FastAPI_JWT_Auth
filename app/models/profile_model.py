from pydantic import BaseModel
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import (
    DeclarativeBase, mapped_column, 
    Mapped, relationship
)

from app.models import Base


class UserProfile(Base):
    __tablename__ = "Profile"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"), unique=True)
    # image: Mapped[str] = mapped_column(String(length=2100000))    # VARCHAR(max) to store image base64 string
   
    address: Mapped[str] = mapped_column(String(100), default="N/A")

    # Define relationship(s)
    user = relationship("User", back_populates="profile")


    def __repr__(self) -> str:
        return f"""UserProfile(
            id={self.id!r},
            user_id={self.user_id!r},
            address={self.address!r}
            )
        """