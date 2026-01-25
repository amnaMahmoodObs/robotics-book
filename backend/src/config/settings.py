import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Load from .env if it exists (local dev), otherwise use environment variables (Vercel)
        env_file=".env",
        env_file_encoding='utf-8',
        extra="ignore"
    )

    OPENAI_API_KEY: str
    QDRANT_URL: str
    QDRANT_API_KEY: str
    QDRANT_COLLECTION_NAME: str
    DEBUG_MODE: bool = False


settings = Settings()