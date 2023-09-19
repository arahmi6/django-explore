from django.db import models

class Customer(models.Model):
  nama = models.CharField(max_length=20)
  kota = models.CharField(max_length=255)
