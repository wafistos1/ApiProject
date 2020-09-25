from django.contrib import admin
from .models import Orders, OrderProduct

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'delevery_man',
        'ref_code',
        'start_date',
        'being_deliverd',
        'received',
        'refund_requested',
        'refund_granted',
        )
    list_display_links = ('client', 'delevery_man')
    list_filter = ('client', 'delevery_man', 'received', 'ref_code')
    # search_fields = ['client', 'delevery_man', 'received', 'ref_code']
     
    
    
class OrdersProductAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'item',
        'quatity',
        'selected',
        'store',
        )
    list_display_links = ('client', 'item', 'store')
    # list_filter = ('client', 'item', 'store')
    
    search_fields = ['client', 'item', 'store']
    
    
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderProduct, OrdersProductAdmin)