from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.

class Med(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Med, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre
