from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str | None = None
    fullname: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str | None = None
    
