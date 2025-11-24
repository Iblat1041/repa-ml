"""
Конфигурация ML-сервиса.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_PORT: int = 8002
    MODEL_NAME: str = "blanchefort/rubert-base-cased-sentiment"

    class Config:
        env_file = ".env"


settings = Settings()
