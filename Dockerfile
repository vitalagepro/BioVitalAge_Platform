FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Installa dipendenze di sistema per psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         gcc \
         libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e installa pacchetti Python
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia il resto del progetto
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
