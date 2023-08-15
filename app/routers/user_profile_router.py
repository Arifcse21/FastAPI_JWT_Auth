from fastapi import APIRouter, status, Depends, Request
from app.utils import Database, AccessTokenUtil, RefreshTokenUtil, verify_password
from app.models import Base, User
from app.schemas import UserLoginSchema
from app.utils import JWTBearer, decode_uuid_from_jwt
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder


db = Database()
engine, session = db()

user_profile_router = APIRouter()


@user_profile_router.post("/user/profile/", dependencies=[Depends(JWTBearer())], tags=["users"], status_code=status.HTTP_200_OK)
def user_profile(request: Request):
    uuid = decode_uuid_from_jwt(request.headers["Authorization"])
    
