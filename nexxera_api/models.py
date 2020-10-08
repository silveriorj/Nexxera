from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from django.forms import ModelForm

from helpers.models import TimestampModel


TITLE_CHOICES = [
    ('DEBIT', 'Debit.'),
    ('CREDIT', 'Credit.'),
]


class Account(TimestampModel):
    account = models.CharField(
        max_length=64,
        verbose_name=_('account'),
        null=True,
        blank=True,
    )
    branch = models.CharField(
        max_length=64,
        verbose_name=_('branch'),
        null=True,
        blank=True,
    )
    number = models.IntegerField(
        verbose_name=_('number'),
        null=True,
        blank=True,
    )
    balance = models.FloatField(
        verbose_name=_('balance'),
        null=True,
        blank=True,
    )

    class Meta:
        index_together = ('account', 'branch', 'balance',)

    def __str__(self):
        return f'{self.account} | {self.branch}'


class Transaction(TimestampModel):
    account = models.ForeignKey(
        Account,
        verbose_name=_('bank account'),
        related_name='transacted_account',
        on_delete=models.CASCADE,
    )
    operation = models.CharField(
        max_length=64,
        verbose_name=_('operation'),
        choices=TITLE_CHOICES,
    )
    value = models.FloatField(
        verbose_name=_('value'),
    )
    description = models.CharField(
        max_length=256,
        verbose_name=_('description'),
    )
    date = models.DateField(
        verbose_name=_('date'),
        null=True,
        blank=True,
    )

    class Meta:
        index_together = ('account', 'operation', 'value')


class History(TimestampModel):
    account = models.ForeignKey(
        Account,
        verbose_name=_('bank account'),
        related_name='history_account',
        on_delete=models.CASCADE,
    )
    transaction = models.ForeignKey(
        Account,
        verbose_name=_('transaction'),
        related_name='history_transaction',
        on_delete=models.CASCADE,
    )
    last_balance = models.FloatField(
        verbose_name=_('last balance'),
    )
    new_balance = models.FloatField(
        verbose_name=_('balance'),
    )

    class Meta:
        index_together = ('account', 'transaction', 'last_balance', 'new_balance')
