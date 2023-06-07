from fastapi import APIRouter, status, Depends
from app.utils import Database, AccessTokenUtil, RefreshTokenUtil, hash_password
from app.models import Base, User
from app.schemas import UserLoginSchema
from app.utils import JWBearer
from sqlalchemy import select


db = Database()
engine, session = db()

login_user_router = APIRouter()


@login_user_router.post("/user/login/", dependencies=[Depends(JWBearer)], tags=["users"], status_code=status.HTTP_200_OK)
def login_user(login: UserLoginSchema):
    pass