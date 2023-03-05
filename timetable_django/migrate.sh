#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"default@email.com"}

cd /app/

/opt/venv/bin/python manage.py makemigrations --noinput
/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
