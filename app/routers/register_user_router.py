from fastapi import APIRouter, status
from app.utils import Database, AccessTokenUtil, RefreshTokenUtil, hash_password
from app.models import Base, User
from app.schemas import UserSchema
from uuid import uuid4


db = Database()
engine, session = db()

register_user_router = APIRouter()

@register_user_router.post("/user/register/", tags=["users"], status_code=status.HTTP_201_CREATED)
def register_user(user: UserSchema):
    user_uuid = str(uuid4())
    print(type(user_uuid))
    new_user = User(
        fullname = user.fullname,
        uuid = str(user_uuid),
        email = user.email,
        phone = user.phone,
        password = str(hash_password(user.password))
    )

    
    
    try:
        access_token = AccessTokenUtil.generate_access_token(user_uuid)
        # refresh_token = RefreshTokenUtil.generate_refresh_token(user_uuid)
        session.add(new_user)
        session.commit()

        response = {
            "response": "successful",
            "status_code": status.HTTP_201_CREATED,
            "message": "User created successfully",
            "access_token": str(access_token),
        }
        return response
    
    except Exception as e: 
        response = {
        "response": "failed",
        "status_code": status.HTTP_400_BAD_REQUEST,
        "message": str(e),
        }
    
        return response

