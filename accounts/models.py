
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Address(models.Model):
    city =models.CharField(max_length=200)
    region =models.CharField(max_length=200)
    location =models.CharField(max_length=200)
    
    def __str__(self):
        return self.location
    
class CustomEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Custom_employee')
    phone = models.CharField(max_length=200, blank=True, null=True)
    picture = models.ImageField(default='default.jpg', upload_to='picture/employee')
    
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
    facebook_id = models.IntegerField(unique=True)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='client_address')
    city = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    
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