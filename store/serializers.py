from rest_framework import serializers
from .models import Orders, OrderProduct
from rest_framework.fields import CurrentUserDefault


class OrdersSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = Orders
        fields ='__all__'  


class OrderProductSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = OrderProduct
        fields =('quatity', 'item', 'store') 
        
    
class OrderProductUpdateSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = OrderProduct
        fields =('quatity', 'item', )     