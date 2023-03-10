"""
WSGI config for timetable_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path

import dotenv
from django.core.wsgi import get_wsgi_application


CURRENT_DIR: Path = Path(__file__).resolve().parent
ENV_FILE_PATH: Path = CURRENT_DIR.parent / ".env"

ENV_CONFIG_LOADED: bool = True
# if os.path.exists(ENV_FILE_PATH):
#     dotenv.read_dotenv(str(ENV_FILE_PATH))
#     ENV_CONFIG_LOADED = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_django.settings')

application = get_wsgi_application()
