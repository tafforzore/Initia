# models.py
from django.db import models

class Payment(models.Model):
    status = models.CharField(max_length=50)
    ref_payment = models.CharField(max_length=100)
    transaction_number = models.CharField(max_length=100)
    public_key = models.CharField(max_length=100)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=20)
    operator = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    item_ref = models.CharField(max_length=50)
    item_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=10)
    error_code = models.CharField(max_length=10, blank=True)
    error_message = models.CharField(max_length=100, blank=True)
    sign_token = models.CharField(max_length=100)
    environement = models.CharField(max_length=20)

    def __str__(self):
        return self.ref_payment

