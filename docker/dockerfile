FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DB_USER="postgres"
ENV DB_PASSWORD="Bari2025"
ENV DB_PORT=8082
ENV PORT=5000
ENV DB_HOST="host.docker.internal"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]