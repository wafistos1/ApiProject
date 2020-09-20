from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_list_or_404, get_object_or_404

# third party imports
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import authentication

# Logics
from .serializers import  ProductSerializer, StoreSerializer
from .models import Product, Store
from accounts.models import ClientUser


class ProductListView(generics.ListAPIView):
    
    pass
    
    
class AddItemCartView(APIView):
    """Add item in cart

    Args:
        APIView ([type]): [description]
    """
    serializer_class = ProductSerializer
    
    def post(self, request ):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'seriaizer is valid'})
            

    
    def get(self, request, format=None):
        qs = Product.objects.all()
        products = ProductSerializer(qs, many=True) 
        
        context = {
            
        }
        return Response(context)
        

class DeleteItemCartView(APIView):
    """Delete item from cart

    Args:
        APIView ([type]): [description]
    """
    pass

class UpdateItemCartView(APIView):
    """Update quantity in cart

    Args:
        APIView ([type]): [description]
    """
    pass