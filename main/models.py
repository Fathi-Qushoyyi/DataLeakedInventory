from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Employee(models.Model):
    #one to one field
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)