from fastapi import APIRouter, status, Depends
from app.utils import Database, AccessTokenUtil, RefreshTokenUtil, verify_password
from app.models import Base, User
from app.schemas import UserLoginSchema
from app.utils import JWTBearer
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder


db = Database()
engine, session = db()

login_user_router = APIRouter()


@login_user_router.post("/user/login/", tags=["users"], status_code=status.HTTP_200_OK)
def login_user(login: UserLoginSchema):
    email = login.email
    password = login.password

    hashed_password = None
    user_uuid = None
    query_user = select(User).filter(email == login.email)
    check_user = session.execute(query_user).fetchall()
    if len(check_user):
        hashed_password = [jsonable_encoder(obj[0].__dict__) for obj in check_user][0]["password"]
        user_uuid = [jsonable_encoder(obj[0].__dict__) for obj in check_user][0]["uuid"]

    is_valid_password = verify_password(password=password, hashed_password=hashed_password)

    if is_valid_password:
        access_token = AccessTokenUtil.generate_access_token(uuid=user_uuid)
        refresh_token = RefreshTokenUtil.generate_refresh_token(uuid=user_uuid)
        response = {
            "response": "successful",
            "status_code": status.HTTP_200_OK,
            "message": "User logged in successfully",
            "access_token": str(access_token),
            "refresh_token": str(refresh_token),
        }
        return response
    
    else:
        response = {
            "response": "failed",
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": "Wrong Password"
        }
        return response
