# -*-coding:utf-8-*-
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from backend.core.config import settings
from backend.api.api_v1.api import api_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json'
)

# 设置跨域源
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# 挂载前端静态文件
# app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, prefix=settings.API_V1_STR)


# 设置前端静态文件入口
# @app.get('/')
# async def read_index():
#     return FileResponse('static/index.html')
#
#
# # 前端页面刷新重新返回index页面
# @app.exception_handler(404)
# async def not_found(request: Request, exc):
#     accept = request.headers.get('accept')
#     if exc.status_code == 404 and 'text/html' in accept:
#         return FileResponse('static/index.html')
#     else:
#         return JSONResponse(content={'error': "Not found"}, status_code=exc.status_code)


if __name__ == '__main__':
    import uvicorn
    # 开发
    uvicorn.run(f'{__name__}:app', port=5000, host='127.0.0.1', reload=True)
    # 生产
    # uvicorn.run(app, port=80, host='0.0.0.0', log_config=settings.LOGGING)
