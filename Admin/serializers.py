from rest_framework import serializers
from .models import User,City

class UserSerializers(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.city')
    class Meta:
        model=User
        fields =['first_name','last_name','username','email','city_name','age','gender','date_joined']
        
        
class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=['id','city']
        

