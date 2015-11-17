from django.db import models

# Create your models here.


class hist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    temperature = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
