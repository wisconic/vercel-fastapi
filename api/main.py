import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/:id")
def hello():
    return f"hello, {id}"


@app.get("/")
def hello():
    return "hello, world"


if __name__ == "__main__":
    asyncio.run(
        uvicorn.run(app="api.main:app", host="127.0.0.1", port="8000", reload=True)
    )
