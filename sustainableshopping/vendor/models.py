from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    desc = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    user = models.OneToOneField(User)
    
    def __str__(self):    
        return self.name
    class Meta:
        ordering = ['name']
        
class Tag(models.Model):
    vendor = models.ManyToManyField(Vendor)
    name = models.CharField(max_length=100)