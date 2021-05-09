from fastapi import APIRouter

from app.api.api_v1.endpoint import auth, posts, categories


api_router = APIRouter()
api_router.include_router(auth.router, tags=['auth'])
api_router.include_router(posts.router, tags=['posts'], prefix='/posts')
api_router.include_router(categories.router, tags=['categories'], prefix='/categories')
