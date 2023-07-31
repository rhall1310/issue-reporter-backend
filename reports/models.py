from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Report(models.Model):
    category = models.CharField(max_length=120)
    title = models.CharField(max_length=60, null=True)
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    details = models.CharField(max_length=240)
    address = models.CharField(max_length=240, null=True)
    photo = models.FileField(blank=True)
    lon = models.FloatField(null=True, blank=True, default=0.0)
    lat = models.FloatField(null=True, blank=True, default=0.0)
    email = models.EmailField(max_length=120, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    resolved = models.BooleanField(null=True)


# Create your models here.
