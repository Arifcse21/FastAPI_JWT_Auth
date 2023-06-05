from fastapi import APIRouter, status
from app.utils import Database, AccessTokenUtil, RefreshTokenUtil, hash_password
from app.models import Base, User
from app.schemas import UserSchema
from uuid import uuid4


db = Database()
engine, session = db()

register_user_router = APIRouter()

@register_user_router.post("user/register/", tags=["users"], status_code=status.HTTP_201_CREATED)
def register_user(user: UserSchema):
    new_user = User(
        fullname = user.fullname,
        uuid = uuid4(),
        email = user.email,
        phone = user.phone,
        password = hash_password(user.password)
    )

    session.add(new_user)
    session.commit()

    response = {
        "response": "successful",
        "status_code": status.HTTP_201_CREATED,
        "message": "User created successfully",
        "data": user    
    }
    
    return response

