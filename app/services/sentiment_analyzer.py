"""
Сервис анализа тональности текста.
Содержит: загрузку ML-модели и fallback-алгоритм.
"""

from transformers import pipeline
import structlog
import re

logger = structlog.get_logger("ml.sentiment")


class SentimentAnalyzer:
    """
    Обёртка над ML-моделью + fallback.
    """

    def __init__(self):
        try:
            self.model = pipeline(
                "sentiment-analysis",
                model="blanchefort/rubert-base-cased-sentiment",
                truncation=True,
                max_length=1500,
            )
            logger.info("model_loaded", model="rubert-base-cased-sentiment")
        except Exception as e:
            logger.error("model_load_failed", error=str(e))
            self.model = None

    async def analyze_text(self, text: str) -> str:
        """
        Возвращает 'positive' или 'negative'.
        """

        text = text.strip()
        if not text:
            return "positive"

        # --- ML (если модель загружена)
        if self.model:
            try:
                r = self.model(text[:1500])[0]
                label = r["label"].lower()
                return "positive" if "pos" in label else "negative"
            except Exception as e:
                logger.error("ml_failed", error=str(e))

        # --- Простейший fallback
        text_lower = text.lower()
        pos = ["побед", "успех", "выигр", "лучший", "сильный"]
        neg = ["проигр", "провал", "кризис", "ошиб", "скандал"]

        score = 0
        for w in pos:
            if w in text_lower:
                score += 1
        for w in neg:
            if w in text_lower:
                score -= 1

        return "positive" if score >= 0 else "negative"
