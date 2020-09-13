from fastapi import APIRouter

from config import API_V1
from .foo.bar import router as home_router

api_router = APIRouter()
api_router.include_router(home_router, prefix=API_V1)
