from django.contrib import admin
from .models import Address, Product, Store, Categorie

admin.site.register(Categorie)

class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price_wholesale',
        'price_detail',
        'quantity',
        'delivery_company',
        'store_item',
        'details',
        )
    list_display_links = ('name', 'category' ,'quantity', 'store_item', 'delivery_company')
    list_filter = ('name', 'category', 'price_wholesale', 'price_detail', 'delivery_company')
    # search_fields = ['client', 'delevery_man', 'received', 'ref_code']
    def store_item(self, obj):
        return '\n'.join([a.name for a in obj.store.all()])

admin.site.register(Product, ProductsAdmin) 

class StoresAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'All_products', 
        )
    list_display_links = ('name', 'All_products',)
    list_filter = ('name',)
    # search_fields = ['client', 'delevery_man', 'received', 'ref_code']
    
    def All_products(self, obj):
        products = []
        for product in Product.objects.filter(store=obj):
            products.append(product)
        return products
    


admin.site.register(Store, StoresAdmin) 

