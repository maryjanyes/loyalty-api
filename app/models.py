# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.postgres.fields import JSONField

class Customer(models.Model):

    class Meta:
        db_table = 'customer'

    name = models.CharField(max_length = 20)
    family_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    points = models.PositiveIntegerField(help_text='(updates on save)', default=0)
    points_chain = ArrayField(JSONField(blank=False), default=[])

    @classmethod
    def create(
        cls,
        name,
        family_name,
        email
    ):
        c_s = cls(
            name,
            family_name,
            email
        )
        return c_s


class LoyaltyTransaction(models.Model):

    class Meta:
        db_table = 'loyalty_transaction'

    # owner_id=models.ForeignKey('Customer', on_delete=models.CASCADE)
    owner_id = models.PositiveIntegerField()
    datetime = models.DateTimeField(auto_now=True)
    point_value = models.PositiveIntegerField()