from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)

class Transaction(models.Model):
    account_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    description = models.CharField(max_length=255)
    debit_credit_status = models.CharField(max_length=1, choices=[('D', 'Debit'), ('C', 'Credit')])
    amount = models.DecimalField(max_digits=15, decimal_places=2)
