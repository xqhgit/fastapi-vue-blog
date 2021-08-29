from fastapi import FastAPI
import uvicorn

from webapi.routers import category_router, post_router, user_router

app = FastAPI()
app.include_router(post_router.router)
app.include_router(category_router.router)
app.include_router(user_router.router)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
