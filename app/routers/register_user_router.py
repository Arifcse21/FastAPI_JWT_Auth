from fastapi import APIRouter, status
from app.utils import Database, AccessTokenUtil, RefreshTokenUtil, hash_password
from app.models import Base, User, UserProfile
from app.schemas import UserSchema
from sqlalchemy import select
from uuid import uuid4


db = Database()
engine, session = db()

register_user_router = APIRouter()

@register_user_router.post("/user/register/", tags=["users"], status_code=status.HTTP_201_CREATED)
def register_user(user: UserSchema):
    user_uuid = uuid4()

    chk_user = select(User).filter(User.username == user.username)
    if len(session.execute(chk_user).fetchall()):
        return {
            "response": "failed",
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": "username is already taken",  # same as all girls are taken, baler life
        }
    
    new_user = User(
        username = user.username,
        fullname = user.fullname,
        uuid = str(user_uuid),
        email = user.email,
        phone = user.phone,
        password = str(hash_password(user.password))
    )
    
    try:
        access_token = AccessTokenUtil.generate_access_token(str(user_uuid))
        # refresh_token = RefreshTokenUtil.generate_refresh_token(user_uuid)
        session.add(new_user)
        session.commit()

        session.refresh(new_user)
        new_profile = UserProfile(user=new_user)
        session.add(new_profile)
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

