from django.contrib import admin
from .models import *

# Register your models here.

class Data_admin(admin.ModelAdmin):
    list_display = ["LicensePlate","Make","VIN","Model","Type","date_str","MilesDriven"]

admin.site.register(VehicleData, Data_admin)