from ctypes import addressof
from unicodedata import name
from django.conf import settings
from django.db import models
from django.utils import timezone

class Account(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_num = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits=19, decimal_places=2)

    CHEQUING = 'C'
    SAVING = 'S'
    ACCOUNT_TYPE_CHOICES = [
        (CHEQUING, 'Chequing'),
        (SAVING, 'Saving'),
    ]
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES, default=CHEQUING)

    def deposit(self, deposit_amount):
        self.amount = self.amount + deposit_amount

    def withdraw(self, withdraw_amount):
        self.amount = self.amount - withdraw_amount

