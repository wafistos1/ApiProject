from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
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


class ProductListUserView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Product.objects.all() 
        products = ProductSerializer(qs, many=True)
        
        message = f'All Products'
        
        context = {
            'Message': message,
            'Orders': products.data,
            'Status': 'status.HTTP_200 ',
        }
        return Response(context)
  
    
class ProductUserSearchView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, query):
        qs = Product.objects.filter(
            Q(name__icontains=query)
        )
        print(qs)
        if qs: 
            products = ProductSerializer(qs, many=True)
        
            message = f'All Products with title: {query}'
            
            context = {
                'Message': message,
                'Orders': products.data,
                'Status': 'status.HTTP_200 ',
            }
            return Response(context)
        else:
            message = f'no Product with title: {query}'
            context = {
                'Message': message,
                'Status': 'status.HTTP_200 ',
            }
            return Response(context)
        
        
class ProductAdminSearchView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, query):
        qs = Product.objects.filter(
            Q(name__icontains=query)
        )
        print(type(qs))
        if qs is not None:
            products = ProductSerializer(qs, many=True)
        
            message = f'All Products with title: {query}'
            
            context = {
                'Message': message,
                'Orders': products.data,
                'Status': 'status.HTTP_200 ',
            }
            return Response(context)
        else:
            message = f'no Product with title: {query}'
            context = {
                'Message': message,
                'Status': 'status.HTTP_200 ',
            }
            return Response(context)

        
class SearchWithFilterAdminView(APIView):
    
    def get(self, request, store):
        pass


class SendProductToStroeView(APIView): # تحول بظاعة
    pass


class DisplayProductStoreView(APIView): # جرد البظاعة
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self, request, store, format=None):
        qs = Store.objects.filter(name__icontains=store)
        store = StoreSerializer(qs, many=True)
        
        message = f'All Products {store} store'
        
        context = {
            'Message': message,
            'Orders': store.data,
            'Status': 'status.HTTP_200 ',
        }
        return Response(context)


class BulletinBoardDeleveryView(APIView): # تخليص المندوبين
    pass


class ReceipAmountsView(APIView): # استلام مبالغ الجملة
    pass


class WholesaleOrdersView(APIView): # طلبيات الجملة
    pass

