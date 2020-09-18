from rest_framework import serializers
from .models import CitiesDelevery, DeleveryEmployee, SalaryDelevery, Orders


class DeleverySerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = DeleveryEmployee
        fields ='__all__'  


class CitiesDeleverySerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = CitiesDelevery
        fields ='__all__'  



class SalaryDeleverySerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = SalaryDelevery
        fields ='__all__'  


class OrdersSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    
    class Meta:
        
        model = Orders
        fields ='__all__'  
