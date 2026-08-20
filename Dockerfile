FROM python:3.9-slim

USER root

WORKDIR /app

# Ensure apt can create temporary files
RUN chmod 1777 /tmp

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        wget \
        libicu-dev \
        libncurses6 \
        libncursesw6 \
        libtinfo6 && \
    rm -rf /var/lib/apt/lists/*

# Copy application
COPY trainer /app/trainer
ENV PYTHONUNBUFFERED=1
# Make Python find the trainer package
ENV PYTHONPATH=/app

EXPOSE 8080

# Start your application
ENTRYPOINT ["python", "-m", "trainer.task"]
