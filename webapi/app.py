import uvicorn
from fastapi import FastAPI

from webapi.routers import category_router, post_router, user_router


def create_application() -> FastAPI:
    application = FastAPI()
    # application.include_router(post_router.router)
    application.include_router(category_router.router, prefix='/categories')
    application.include_router(user_router.router, prefix='/admin')
    return application


app = create_application()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
