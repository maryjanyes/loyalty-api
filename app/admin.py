# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Customer, LoyaltyTransaction

admin.site.register(Customer)
admin.site.register(LoyaltyTransaction)

admin.site.site_header = 'Loyalty: SITE HEADER'
admin.site.site_title = 'Loyalty: SITE'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'family_name', 'points']
    list_filter = ('name', 'family_name')