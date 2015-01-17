from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    desc = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    
    def __str__(self):    
        return self.name
    class Meta:
        ordering = ['name']