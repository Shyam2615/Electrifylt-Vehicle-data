from django.db import models
from django.conf import settings

# Create your models here.
class VehicleData(models.Model):
    LicensePlate = models.CharField(max_length=50)
    Make = models.CharField(max_length=50)
    VIN = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    date_str = models.DateField(auto_now=True )
    MilesDriven = models.CharField(max_length=50)