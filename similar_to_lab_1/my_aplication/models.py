from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Workplace(models.Model):
    name = models.CharField(max_length=50)
    year_founded = models.IntegerField()
    repairs_oldTimers = models.BooleanField()

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    web_site = models.URLField()
    country = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=70)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    color = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.vehicle_type} - {self.max_speed} km/h'

class WorkplaceForManufacturers(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)

class Repairment(models.Model):
    code = models.CharField(max_length=8, unique=True)
    application_date = models.DateField()
    description_of_problem = models.TextField()
    user_reported = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='repairments/', null=True, blank=True)
    vehicle =models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)
