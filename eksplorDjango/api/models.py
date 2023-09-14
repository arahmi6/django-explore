from django.db import models

# Create your models here.
class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nama