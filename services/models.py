from django.db import models
from django import forms


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name 