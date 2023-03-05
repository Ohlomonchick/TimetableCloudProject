#!/bin/bash

cd /app/

# APP_PORT=${PORT:-8000}
# /opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm timetable_django.wsgi:application --bind "0.0.0.0:${APP_PORT}"

source /opt/venv/bin/activate
/opt/venv/bin/python manage.py runserver 0.0.0.0:8000