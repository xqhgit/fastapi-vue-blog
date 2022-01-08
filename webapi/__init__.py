import os
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from webapi.routers import api_router
from webapi.setting import settings


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router, prefix='/api')
    register_middleware(application)
    register_static(application)
    return application


def register_middleware(application):
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_static(app):
    # ¹ÒÔØ¾²Ì¬ÎÄ¼þ
    backend = os.path.dirname(os.path.abspath(__file__))
    app.mount('/static', StaticFiles(directory=os.path.join(backend, 'static')))

    @app.get('/')
    async def read_index():
        return FileResponse(os.path.join(backend, 'static', 'index.html'))

    @app.exception_handler(404)
    async def not_found(request: Request, exc):
        accept = request.headers.get('accept')
        if not accept:
            return JSONResponse(content={'error': "Not found"}, status_code=exc.status_code)
        if exc.status_code == 404 and 'text/html' in accept:
            return FileResponse(os.path.join(backend, 'static', 'index.html'))
        else:
            return JSONResponse(content={'error': "Not found"}, status_code=exc.status_code)
