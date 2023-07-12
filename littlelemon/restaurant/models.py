from django.db import models

# Create your models here.
from django.db import models

class BookingTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

class MenuTable(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField()