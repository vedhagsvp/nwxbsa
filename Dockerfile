FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl git wget libicu-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy

COPY trainer /app/trainer

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "-m", "trainer.task"]
