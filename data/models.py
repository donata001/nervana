from django.db import models
from django.utils import timezone


class Houses(models.Model):
    age = models.IntegerField(null=True)
    region = models.CharField(max_length=5, null=True)
    weight = models.FloatField(null=True)
    bedrooms = models.IntegerField(null=True)
    built_year = models.IntegerField(null=True)    
    value = models.IntegerField(null=True)
    vacancy = models.IntegerField(null=True)
    nunit = models.IntegerField(null=True)
    rooms = models.IntegerField(null=True)
    utility = models.FloatField(null=True)
    type = models.CharField(max_length=128, null=True)
    