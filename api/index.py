import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return "hello, world"


@app.get("/hello/{id}")
def hello_input(id: str):
    return f"hello, {id}"


if __name__ == "__main__":
    asyncio.run(
        uvicorn.run(app="api.main:app", host="127.0.0.1", port=8000, reload=True)
    )
