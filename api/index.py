import asyncio
from typing import Optional

import beanie
import motor
import uvicorn
from beanie import Document
from fastapi import FastAPI
from pydantic import Field

from api.core.config import CONFIG
from api.core.db_init import db_init

app = FastAPI()


class GolfEventDocument(Document):
    tournamentName: str = Field(...)
    id: str = Field()
    beautyImage: str = Field(...)
    champion: str = Field(...)
    champions: list[dict[str, str]] = Field(...)
    championEarnings: str = Field(...)
    championId: str = Field(...)
    city: str = Field(...)
    country: str = Field(...)
    countryCode: str = Field(...)
    courseName: str = Field(...)
    date: str = Field(...)
    dateAccessibilityText: str = Field(...)
    purse: str = Field(...)
    sortDate: str = Field(...)
    startDate: int = Field(...)
    state: str = Field(...)
    stateCode: str = Field(...)
    status: Optional[str] = Field(None)
    ticketsURL: Optional[str] = Field(None)
    tourStandingHeading: str = Field(...)
    tourStandingValue: str = Field(...)
    tournamentLogo: str = Field(...)
    display: str = Field(...)
    sequenceNumber: int = Field(...)

    class Settings:
        name = "golf_events"


@app.on_event("startup")
async def connect_db():
    try:
        await db_init(
            config=CONFIG,
            database=CONFIG.MONGO_DB_DATABASE,
            models=[GolfEventDocument],
        )
    except Exception as err:
        print("ERROR: unable to connect - ", err)


@app.get("/golf")
async def get_golf():
    return await GolfEventDocument.find_all().to_list()


@app.get("/")
def hello_world():
    return "hello, world"


@app.get("/hello/{id}")
def hello_input(id: str):
    return f"hello, {id}"


if __name__ == "__main__":
    uvicorn.run(app="api.index:app", host="127.0.0.1", port=8000, reload=True)
