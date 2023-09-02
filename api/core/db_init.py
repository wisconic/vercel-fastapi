import beanie
import motor.motor_asyncio

from api.core.config import Config


async def db_init(config: Config, database: str, models: list) -> None:
    """Initializes database connection"""
    uri = f"mongodb+srv://{config.MONGO_DB_USERNAME}:{config.MONGO_DB_PASSWORD}@{config.MONGO_DB_DEPLOYMENT}.rongfka.mongodb.net/?retryWrites=true&w=majority"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)

    await beanie.init_beanie(
        database=client.get_database(database),
        document_models=models,
    )
