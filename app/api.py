from fastapi import FastAPI
from app.routers import register_user_router


app = FastAPI()


app.include_router(register_user_router)
