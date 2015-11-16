from django.contrib import admin

from . import models
# Register your models here.

class MedAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

admin.site.register(models.Med, MedAdmin)


