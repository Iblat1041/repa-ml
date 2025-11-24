FROM python:3.12-slim

WORKDIR /app

# Ускоряем работу Torch — ставим только CPU-версию
RUN apt-get update && apt-get install -y git && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

EXPOSE 8002

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
