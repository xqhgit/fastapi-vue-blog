import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI


from webapi.routers import api_router
from webapi.setting import settings


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router, prefix='/api')
    register_middleware(application)
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


app = create_application()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
