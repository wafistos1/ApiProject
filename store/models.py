from django.db import models
from accounts.models import CustomUser


class CitiesDelevery(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    address1= models.CharField(max_length=200)
    address2= models.CharField(max_length=200, null=True, blank=True)
    city= models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    
    def __str__(self):
        return self.address1


class DeleveryEmployee(models.Model):
    """
    delevery employee

    Args:
        models ([type]): [description]
    """
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='delevery_employee')
    create_delevery = models.DateTimeField(auto_now_add=True)
    # salary_delevery = models.ForeignKey("????") TODO: ajouter dans l'app sotre
    palace_work = models.ForeignKey(CitiesDelevery, on_delete=models.CASCADE, related_name='work_address', null=True, blank=True) 
    # orders = models.OneToOneField('order>??') TODO: ajouter dans l'app sotre
    # orders_groups = models.OneToOneField('order>??') TODO: ajouter dans l'app sotre
    orders_delevery_not_paid = models.IntegerField()
    orders_delevery_paid = models.IntegerField()
    
    def __str__(self):
        return f"{self.employee} --> {self.palace_work}"


CHOICES_CITIES = [
    
    ('Usa', 'Usa'),
    ('Ar', 'Algeria'),
    ('Fr', 'France'),
    ('Gr', 'Germania'),
]


CHOICES_CATEGORY = [
    ('L', 'livrer'),
    ('A', 'en attente'),
    ('P', 'payer'),
    ('N', 'not pay'),
    
]



class SalaryDelevery(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    city_name = models.CharField(max_length=200, choices=CHOICES_CITIES)
    salary_delevery = models.IntegerField()
    
    def __str__(self):
        return self.salary_delevery
    

class Orders(models.Model):
    category = models.CharField(max_length=200, choices=CHOICES_CATEGORY)
    # number TODO: parler avec pour explications
    address = models.ForeignKey(CitiesDelevery, related_name='order_address', on_delete=models.CASCADE)
    employee_responsable = models.ForeignKey(CustomUser, related_name='employe_responsable', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.address}---> {self.employee_responsable}'
    