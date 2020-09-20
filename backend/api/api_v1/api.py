from fastapi import APIRouter

from backend.api.api_v1.endpoint import login, posts, categories, attachments


api_router = APIRouter()
api_router.include_router(login.router, tags=['login'])
api_router.include_router(posts.router, tags=['posts'], prefix='/posts')
api_router.include_router(categories.router, tags=['categories'], prefix='/categories')
api_router.include_router(attachments.router, tags=['attachments'], prefix='/attachments')
