# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core import serializers

from models import Customer, LoyaltyTransaction

def save_tx(count, customer_pk):
    tx = LoyaltyTransaction(
        point_value=count,
        owner_id=customer_pk
    )
    tx.save()
    return LoyaltyTransaction.objects.filter(owner_id=customer_pk)

def root_view(request):
    return render(
        request,
        './root-index.html'
    )

@csrf_exempt
def customer_balance(request):

    if not request.session.get('auth_key'):
        return HttpResponse('Access denied: provide `session_key`')

    if request.method == "POST":
        customer_id = request.GET['customer_id']
        is_accrual = request.GET['is_accrual']
        count = int(request.GET['count'])
        customer = Customer.objects.filter(pk=customer_id)

        if not customer[0]:
            return HttpResponse('Specify `customerId`.')

        if is_accrual:
            fresh_balance = customer[0].points + count
            Customer.objects.filter(pk=customer_id).update(points=fresh_balance)
            customer_txs = save_tx(count, customer[0].pk)

            return HttpResponse(serializers.serialize('json', customer_txs))

        elif not is_accrual and (customer[0].points > count or customer[0].points == count):
            fresh_balance = customer[0].points - count
            Customer.objects.filter(pk=customer_id).update(points=fresh_balance)
            customer_txs = save_tx(count, customer[0].pk)

            return HttpResponse(serializers.serialize('json', customer_txs))

    if request.method == "GET":
        customer_id = request.GET['customer_id']
        customers = Customer.objects.filter(pk=customer_id)
        customer = customers[0]

        return HttpResponse(customer.points)

def save_customer(request):

    if not request.session.get('auth_key'):
        return HttpResponse('Access denied: provide `session_key`')

    name = request.GET['name']
    family_name = request.GET['family_name']
    email = request.GET['email']

    customer = Customer(
        name=name,
        family_name=family_name,
        email=email
    )

    customer.save()

    return HttpResponse('Customer saved.')