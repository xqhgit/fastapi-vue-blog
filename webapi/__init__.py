# -*- coding: UTF-8 -*-
import time
import traceback
import asyncio
import os
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from webapi.routers import api_router
from webapi.setting import settings


def create_application() -> FastAPI:
    # 等待其他组件启动完成
    time.sleep(3)
    application = FastAPI()
    application.include_router(api_router, prefix='/api')
    register_middleware(application)
    register_static(application)
    register_event(application)
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
    # 挂载静态文件
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


async def register_elasticsearch():
    from webapi.utils.elastic import es, INDEX
    import aiomysql

    async def create_index():
        # 清除索引
        await es.indices.delete(index=INDEX, ignore=[400, 404])
        # 创建索引
        await es.indices.create(index=INDEX, ignore=400)
        mapping = {
            'properties': {
                'title': {
                    'type': 'text',
                    'analyzer': 'ik_max_word',
                    'search_analyzer': 'ik_max_word'
                },
                'description': {
                    'type': 'text',
                    'analyzer': 'ik_max_word',
                    'search_analyzer': 'ik_max_word'
                },
                'body': {
                    'type': 'text',
                    'analyzer': 'ik_max_word',
                    'search_analyzer': 'ik_max_word'
                }
            }
        }
        await es.indices.put_mapping(index=INDEX, body=mapping)
        await inject_data_to_es()

    async def inject_data_to_es():
        # 将数据注入elasticsearch
        loop = asyncio.get_running_loop()
        conn = await aiomysql.connect(
            host=settings.DB_HOST, port=settings.DB_PORT,
            user=settings.DB_USER, password=settings.DB_PASSWORD, db=settings.DB_NAME,
            loop=loop
        )
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute("SELECT p.id, p.title, p.description, p.body, p.timestamp FROM Post p WHERE p.is_published=true")
        data = await cur.fetchall()
        await cur.close()
        conn.close()
        for d in data:
            await es.index(index=INDEX, document=d, id=d['id'], ignore=[400, 404])

    await create_index()


def register_event(app):
    @app.on_event("startup")
    async def startup_event():
        try:
            await register_elasticsearch()
        except Exception as e:
            traceback.print_exc()

    @app.on_event("shutdown")
    async def shutdown_event():
        from webapi.utils.elastic import es
        await es.close()
