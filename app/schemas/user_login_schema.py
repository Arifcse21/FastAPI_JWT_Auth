from pydantic import BaseModel, EmailStr


class UserLoginSchema(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
