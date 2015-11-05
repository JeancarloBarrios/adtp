
from django.db import models

# Create your models here.

class Med(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()

