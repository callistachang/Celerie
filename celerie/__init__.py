from __future__ import absolute_import, unicode_literals

from .celery import app as celery_app

# ensures that Celery starts whenever Django starts
__all__ = ('celery_app',)
