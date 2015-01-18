from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    user = models.OneToOneField(User)
    
    class Meta:
        ordering = ['name']
        
class Tag(models.Model):
    vendor = models.ManyToManyField(Vendor)
    name = models.CharField(max_length=100)