from django.contrib import admin
from .models import Address, Product, Store

class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price_wholesale',
        'price_detail',
        )
    list_display_links = ('name', 'category')
    list_filter = ('name', 'category', 'price_wholesale', 'price_detail')
    # search_fields = ['client', 'delevery_man', 'received', 'ref_code']

admin.site.register(Product, ProductsAdmin) 

class StoresAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'quantity',
        'quantity_min',
        )
    list_display_links = ('name', 'quantity')
    list_filter = ('name', 'quantity', 'quantity_min')
    # search_fields = ['client', 'delevery_man', 'received', 'ref_code']
    


admin.site.register(Store, StoresAdmin) 

