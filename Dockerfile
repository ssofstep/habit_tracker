FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \\\\
    gcc \\\\
    libpq-dev \\\\
    && apt-get clean \\\\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY=os.getenv("SECRET_KEY")
ENV CELERY_BROKER_URL='redis://localhost:6379'

EXPOSE 8000
