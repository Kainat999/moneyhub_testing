from django.urls import path
from .views import transaction_list, home, webhook_receiver

urlpatterns = [
    path('', home, name='home'),
    path('transactions/', transaction_list, name='transaction_list'),
    path('webhook/', webhook_receiver, name='webhook_receiver'),
]
