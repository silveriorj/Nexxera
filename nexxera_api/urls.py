from django.conf.urls import url
from . import views

urlpatterns = [
    # ACCOUNT
    url(r'^accounts/$', views.AccountList.as_view(), name='account-list'),

    # TRANSACTIONS
    url(r'^transaction/$', views.Transactions.as_view(), name='extract'),
]
