from __future__ import absolute_import
import os
from datetime import datetime

from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from celery.decorators import periodic_task, task
from django.core import serializers
from django.db.models import Sum
from loyalty import settings
from local_logger import open_file_and_log
# from balance.clickhouse import click_house_db
# todo: make configurations smartify

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

    from app.models import Customer
    customers_with_large_balance = Customer.objects.extra(where=["points > 1000"])
    average_balance_sum = Customer.objects.aggregate(Sum('points'))
    stamp_now = datetime.now()
    date_string = stamp_now.strftime("%d/%m/%Y %H:%M:%S")
    open_file_and_log('Date: ' + date_string + '\n' + 'Sum: ' + average_balance_sum)
    # click_house_db.insert_tx_sum_by_timestamp(average_balance_sum)

    if len(customers_with_large_balance) > 0:
        open_file_and_log(serializers.serialize('json', customers_with_large_balance))
