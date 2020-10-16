from django.db import models
from accounts.models import DeliveryMan, Address, ClientUser, EmployeeUser


CATEGORY = (
    ('Mobil', 'Mobil'),
    ('Swatch','Swatch'),
    ('Medical','Medical'),
    ('Toys','Toys'),
    ('women_bags', 'women bags'),
    ('other', 'other'),
)


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY, default='other')
    price_wholesale = models.IntegerField()
    price_detail = models.IntegerField()

    def __str__(self):
        return f'{self.name}:--> ${self.price_detail}'
    
    def get_name_product(self):
        return Product.objects.all().first().self.name


class Store(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)
    quantity_min = models.IntegerField(null=True)
    product = models.ManyToManyField(Product, related_name='product') 
    
    def get_quatity_min_alert(self):
        pass
    
    def __str__(self):
        return f'{self.name}' 





    
    

