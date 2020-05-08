"""
WSGI config for FTL_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import traceback

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FTL_project.settings")

application = StaticFilesHandler(get_wsgi_application())
