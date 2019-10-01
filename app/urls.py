from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.root_view, name='index'),
    url(
        'customer/balance/',
        views.customer_balance,
        name='balance'
    ),
    url(
        'customer/',
        views.save_customer,
        name='customer'
    )
]