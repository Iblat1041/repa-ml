"""
HTTP-эндпоинты для анализа тональности.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.sentiment_analyzer import SentimentAnalyzer

router = APIRouter()
analyzer = SentimentAnalyzer()

class SentimentIn(BaseModel):
    text: str


class SentimentOut(BaseModel):
    sentiment: str


@router.post("/analyze", response_model=SentimentOut)
async def analyze(payload: SentimentIn):
    """
    Получить тональность текста.
    """
    sentiment = await analyzer.analyze_text(payload.text)
    return SentimentOut(sentiment=sentiment)
