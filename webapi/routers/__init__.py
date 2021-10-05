from fastapi import APIRouter

from . import category_router
from . import post_router
from . import user_router
from . import comment_router

api_router = APIRouter()
api_router.include_router(user_router.router, tags=['User'], prefix='/admin')
api_router.include_router(post_router.router, tags=['Post'], prefix='/posts')
api_router.include_router(category_router.router, tags=['Category'], prefix='/categories')
api_router.include_router(comment_router.router, tags=['Comment'], prefix='/comments')
