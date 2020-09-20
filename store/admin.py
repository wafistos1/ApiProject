from django.contrib import admin
from .models import Orders, OrderProduct

# Register your models here.

admin.site.register(Orders)
admin.site.register(OrderProduct)