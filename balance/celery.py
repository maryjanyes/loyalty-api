from __future__ import absolute_import
from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from celery.decorators import periodic_task, task

from loyalty import settings
from local_logger import open_file_and_log

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loyalty.settings')
app = Celery('loyalty')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute=1)),
    name="check_balance_and_writing_to_db"
)
def check_balance_and_writing_to_db():
    open_file_and_log('My simple message')