FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# ВАЖНО: запуск миграций и сервера ПРИ СТАРТЕ
CMD ["sh", "-c", "python manage.py migrate && python manage.py createsu && gunicorn sakartvelo.wsgi:application --bind 0.0.0.0:8000"]

