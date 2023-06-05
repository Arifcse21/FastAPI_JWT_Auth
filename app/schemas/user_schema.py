from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    fullname: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    phone: str | None = None
    address: str | None = None
