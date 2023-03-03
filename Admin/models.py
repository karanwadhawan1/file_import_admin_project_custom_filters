from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class City(models.Model):
    city=models.CharField( max_length=100)
    
    def __str__(self):
        return self.city
    
class User(AbstractUser):
    age=models.IntegerField(blank=True,null=True)
    city=models.ForeignKey(City, on_delete=models.CASCADE,blank=True,null=True)
    gender=models.CharField( max_length=10,blank=True,null=True)
    
    

