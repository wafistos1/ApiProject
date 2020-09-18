from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
# Logics
from .serializers import DeleverySerializer, CitiesDeleverySerializer, CitiesDelevery, OrdersSerializer
from .models import DeleveryEmployee, Orders, SalaryDelevery, CitiesDelevery


class DeleveryViewUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = DeleverySerializer
    lookup_url_kwarg = 'id'
    queryset = DeleveryEmployee.objects.all() 


class OrdersViewUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = OrdersSerializer
    lookup_url_kwarg = 'id'
    queryset = Orders.objects.all() 


class CitiesViewUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = CitiesDeleverySerializer
    lookup_url_kwarg = 'id'
    queryset = CitiesDelevery.objects.all() 
    

class DeleveryView(generics.ListCreateAPIView):
    
    serializer_class = DeleverySerializer
    queryset = DeleveryEmployee.objects.all()
    

class OrdersView(generics.ListCreateAPIView):
    
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all() 


class CitiesView(generics.ListCreateAPIView):
    
    serializer_class = CitiesDeleverySerializer
    queryset = CitiesDelevery.objects.all() 