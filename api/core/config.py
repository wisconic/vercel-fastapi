import os
from typing import Optional, Tuple

from dotenv import load_dotenv


def get_value(
    settings: Tuple[str, Optional[any]],
    overrides: Optional[dict[str, any]] = None,
) -> str:
    """Tries to set value using os.getenv() -- overrides take precedence to .env"""
    if overrides is not None:
        return overrides.get(settings[0])
    return os.getenv(*settings)


class Config:
    """Shared config variables"""

    def __init__(self, overrides=None):
        load_dotenv()
        self.MONGO_DB_DEPLOYMENT: str = get_value(
            settings=("MONGO_DB_DEPLOYMENT", ""),
            overrides=overrides,
        )
        self.MONGO_DB_DATABASE: str = get_value(
            settings=("MONGO_DB_DATABASE", ""),
            overrides=overrides,
        )
        self.MONGO_DB_USERNAME: str = get_value(
            settings=("MONGO_DB_USERNAME", ""),
            overrides=overrides,
        )
        self.MONGO_DB_PASSWORD: str = get_value(
            settings=("MONGO_DB_PASSWORD", ""),
            overrides=overrides,
        )


CONFIG = Config()
