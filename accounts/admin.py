from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.models import (
    DeliveryMan,
    Address,
    ClientUser,
    SalaryCustomUser,
    EmployeeUser,
    CustomEmployee,
    City,
    Region,
    )



admin.site.register(City) 
admin.site.register(Region) 
admin.site.register(DeliveryMan) 
admin.site.register(Address) 
admin.site.register(ClientUser)
admin.site.register(SalaryCustomUser)  
admin.site.register(EmployeeUser)  
admin.site.register(CustomEmployee)  

