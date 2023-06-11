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
    image: Mapped[str] = mapped_column(String(length="max"))    # VARCHAR(max) to store image base64 string
    email_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"))
    phone_id: Mapped[int] = mapped_column(Integer, ForeignKey("User.id"))
    address: Mapped[str] = mapped_column(String(100), default="N/A")

    # Define relationship(s)
    user = relationship("User", back_populates="profile")
    email = relationship("User", foreign_keys="[UserProfile.email_id]")
    phone = relationship("User", foreign_keys="[UserProfile.phone_id]")


    def __repr__(self) -> str:
        return f"""UserProfile(
            id={self.id!r},
            user_id={self.user_id!r},
            image={self.image!r},
            email_id={self.email_id!r},
            phone_id={self.phone_id!r},
            address={self.address!r}
            )
        """
    