from fastapi import FastAPI
from app.routers import (
    register_user_router,
    login_user_router
)
from app.utils import Database
from app.models import Base


db = Database()
engine, session = db()

Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(register_user_router)
app.include_router(login_user_router)
