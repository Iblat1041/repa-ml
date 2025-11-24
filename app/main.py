"""
Точка входа в FastAPI-приложение ML-сервиса.
"""

from fastapi import FastAPI
from app.api.v1.sentiment import router as sentiment_router

app = FastAPI(
    title="REPA ML Service",
    version="1.0.0",
)

app.include_router(sentiment_router, prefix="/api/v1/sentiment")


@app.get("/health")
def health():
    """Проверка, что сервис жив."""
    return {"status": "ok"}
