from __future__ import absolute_import, unicode_literals
from django.shortcuts import render, HttpResponse

import os

from celery import Celery

# Creates a Celery app using our own 'settings.py'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerie.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('celerie')

# All Celery-related config keys should have a 'CELERY_' prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover files titled 'tasks.py' in Django apps
app.autodiscover_tasks()

