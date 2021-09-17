import uvicorn
from fastapi import FastAPI

from webapi.routers import api_router


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router, prefix='/api')
    return application


app = create_application()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
