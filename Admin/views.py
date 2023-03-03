from django.shortcuts import render
from .models import City,User
from rest_framework import viewsets
from .serializers import UserSerializers,CitySerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
# import django_filters

import django_filters
from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    start= filters.DateTimeFilter(field_name="date_joined", lookup_expr='date__gte')
    end= filters.DateTimeFilter(field_name="date_joined", lookup_expr='date__lte')
    gender=filters.CharFilter(field_name='gender',lookup_expr='iexact')
    city=filters.CharFilter(field_name='city',lookup_expr='city__iexact')
    date_joined=filters.DateTimeFilter(field_name="date_joined", lookup_expr='date')

    class Meta:
        model = User
        fields = ['start','end','date_joined','gender','city','email','age']



class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
   
    
    
    # def list(self, request):
    #     queryset = self.get_queryset() 
        
    #     search_dict = {}
    #     b ={'age':"age",'email':"email",'city':"city__city",'gender':"gender__iexact",'start':"date_joined__date__gte",'end':"date_joined__date__lte"}

    #     for i in b:
    #         if request.query_params.get(i) is not None:
    #             search_dict[b[i]]=request.query_params.get(i)
        
    #     data = queryset.filter(**search_dict)
    #     if data:
    #         serializer = UserSerializers(data,many=True)
    #         return Response(serializer.data)
    #     serializer = UserSerializers(queryset,many=True)
    #     return Response(serializer.data)
      
        
        
        
    
    


