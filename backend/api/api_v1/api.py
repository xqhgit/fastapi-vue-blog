from fastapi import APIRouter

from backend.api.api_v1.endpoint import login


api_router = APIRouter()
api_router.include_router(login.router, tags=['login'])
