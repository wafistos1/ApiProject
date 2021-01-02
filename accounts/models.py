
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import RegexValidator

User = get_user_model()

class City(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name}'
    

class Region(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} - {self.city.name}'


class Address(models.Model):
    # city =models.CharField(max_length=200, choices=CITY, default='City1')
    region =models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    location =models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.region.name}- {self.region.city}' 

  
class CustomEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Custom_employee')
    phone = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(default='default.jpg', upload_to='picture/employee')
    # add coordonee de l'utilisateur
    
    # class Meta:
    #     abstract = True
    
    def __str__(self):
        return self.user.username
    

class EmployeeUser(CustomEmployee):
    pass
    # store_auth = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='employee_store')  TODO: voir les relations entre CustomUser et store 


class DeliveryMan(CustomEmployee):
    pass


class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    phone = models.CharField(max_length=200, blank=True, null=True)
    facebook_name = models.CharField(max_length=200, blank=True, null=True)
    facebook_id = models.BigIntegerField(unique=True, validators=[
        RegexValidator(
            regex='^([0-9]{16})$',
            message='FaceBook id must be 16 digit',
            code='invalid_facebook_Id'
        ),
    ])
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='client_address', blank=True, null=True)
    # picture_client = models.ImageField(default='default_client.jpg', upload_to='picture/client')
    # logetitutde et largetude du client
    
    def __str__(self):
        return self.user.username

    
class SalaryCustomUser(models.Model):
    user = models.OneToOneField(CustomEmployee, on_delete=models.CASCADE, related_name='salary_customUser')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    working_hours = models.IntegerField()
    absence_hours = models.IntegerField()
    
    def get_working_hours_month(self):
        pass
    
    def get_absence_hours_month(self):
        pass
    
    def get_salary_month(self):
        pass
    
    def __str__(self):
        return self.user.user.username
