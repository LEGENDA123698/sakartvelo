FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
RUN DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_EMAIL=admin@example.com \
DJANGO_SUPERUSER_PASSWORD=admin \
python manage.py createsuperuser --noinput

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "sakartvelo.wsgi", "-b", "0.0.0.0:8000"]