from rest_framework import serializers
from .models import Product, Store
from django.contrib.auth import authenticate



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        
            model = Product
            fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        
            model = Store
            fields = '__all__'
