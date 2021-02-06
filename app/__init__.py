# -*-coding:utf-8-*-
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from app.core.config import settings
from app.api.api_v1.api import api_router


def create_app():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f'{settings.API_V1_STR}/openapi.json'
    )
    if settings.BACKEND_CORS_ORIGINS:
        register_cors(app)
    register_static(app)
    register_exception_handler(app)
    return app


def register_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_static(app):
    # mount frontend static files
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.get('/')
    async def read_index():
        return FileResponse('static/index.html')


def register_exception_handler(app):
    @app.exception_handler(404)
    async def not_found(request: Request, exc):
        accept = request.headers.get('accept')
        if exc.status_code == 404 and 'text/html' in accept:
            return FileResponse('static/index.html')
        else:
            return JSONResponse(content={'error': "Not found"}, status_code=exc.status_code)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        print(request)
        print('Validation Exception', exc)
        return await request_validation_exception_handler(request, exc)
