from django.contrib import admin
from .models import DeleveryEmployee, CitiesDelevery, Orders, SalaryDelevery

# Register your models here.

admin.site.register(DeleveryEmployee)
admin.site.register(CitiesDelevery)
admin.site.register(Orders)
admin.site.register(SalaryDelevery)