#!/bin/bash

cd /app/

# APP_PORT=${PORT:-8000}
# /opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm timetable_django.wsgi:application --bind "0.0.0.0:${APP_PORT}"

source /opt/venv/bin/activate

SUPERUSER_NAME=${DJANGO_SUPERUSER_USERNAME:-"admin"}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"default@email.com"}

cd /app/

/opt/venv/bin/python manage.py makemigrations --noinput
/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --username "$SUPERUSER_NAME" --email "$SUPERUSER_EMAIL" --noinput || true
#/opt/venv/bin/python manage.py collectstatic --noinput

/opt/venv/bin/python manage.py runserver 0.0.0.0:8000