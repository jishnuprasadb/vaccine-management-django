from django.contrib import admin

# Register your models here.
from vaccine_app import models

admin.site.register(models.User)
admin.site.register(models.Vaccine)
admin.site.register(models.Nurse)
admin.site.register(models.Hospital)