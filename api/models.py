from datetime import date
from django.db import models

# Create your models here.

class city(models.Model):
    cityName = models.CharField(max_length=500,null=False)

class event(models.Model):
    eventName = models.CharField(max_length=500,null=False)
    eventCity = models.CharField(max_length=100,null=False)
    eventOrganizer = models.CharField(max_length=200,null=False)
    eventType = models.CharField(max_length=100,null=False, default="misc")
    eventPrice = models.IntegerField(null=False)
    eventImage = models.CharField(max_length=600, default="https://cdn.pixabay.com/photo/2016/11/18/17/47/iphone-1836071_960_720.jpg")
    eventDate = models.DateField(null=False, default=date.today)
    totalTicket = models.IntegerField(null=True)

def __str__(self):
    return self.name
