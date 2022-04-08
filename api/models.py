from django.db import models
from datetime import date

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=500, default="")
    location = models.CharField(max_length=100, default="")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

class Bracket(models.Model):
    division = models.CharField(max_length=50, default="")
