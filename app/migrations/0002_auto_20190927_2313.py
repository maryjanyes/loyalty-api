# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-27 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='loyaltytransaction',
            table='loyalty_transaction',
        ),
    ]
