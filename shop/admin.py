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
        'product_item',
        'quantity_min',
        )
    list_display_links = ('name', 'quantity', 'product_item')
    list_filter = ('name', 'quantity', 'quantity_min')
    # search_fields = ['client', 'delevery_man', 'received', 'ref_code']
    
    def product_item(self, obj):
        return '\n'.join([a.name for a in obj.product.all()])
    


admin.site.register(Store, StoresAdmin) 

