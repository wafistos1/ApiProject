from django.db import models
from accounts.models import DeliveryMan, Address, ClientUser, EmployeeUser


class Categorie(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name}'


class Store(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name}'
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    price_wholesale = models.IntegerField()
    price_detail = models.IntegerField()
    quantity = models.IntegerField(null=True)
    quantity_min = models.IntegerField(null=True)
    store = models.ManyToManyField(Store) 
    

    def __str__(self):
        return f'{self.name}:--> {self.quantity}:Categories--{self.category}'
    
    def get_name_product(self):
        return Product.objects.all().first().self.name








    
    

