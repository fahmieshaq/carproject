from django.contrib import admin
from . import models

admin.site.register(models.Branch)
admin.site.register(models.Vehicle)
admin.site.register(models.VehicleDetail)
admin.site.register(models.Renter)