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
        fields = ('ref_code',  'shipping_address', 'being_deliverd')  


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
        
class OrderProductAdminSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = OrderProduct
        fields = '__all__'

class OrdersAdminSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = Orders
        fields = '__all__'

