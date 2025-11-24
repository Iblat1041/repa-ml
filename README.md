# REPA ML Service

Отдельный сервис для анализа тональности публикаций.

## Запуск

### Локально

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8002

```bash
repa-ml/
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── __init__.py
│   │       └── sentiment.py
│   ├── services
│   │   ├── __init__.py
│   │   └── sentiment_analyzer.py
│   ├── core
│   │   ├── __init__.py
│   │   └── config.py
│   └── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```