from django.contrib import admin
from .models import Orders, OrderProduct
from accounts.models import ClientUser


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'client',
        'client_phone',
        'client_facebook',
        'client_facebook_id',
        'delevery_man',
        'OrderProduct',
        'ref_code',
        'start_date',
        'being_deliverd',
        'received',
        'refund_requested',
        'refund_granted',
        )
    list_display_links = ('pk','client', 'delevery_man', 'client_facebook','client_facebook_id')
    list_filter = ('client', 'delevery_man', 'received', 'ref_code', 'refund_requested', 'refund_granted','start_date')
    # search_fields = ['client', 'delevery_man', 'received', 'ref_code']
     
    def OrderProduct(self, obj):
        return '\n'.join([a.item.name for a in obj.items.all()])
    
    def count(self, request):
        client = ClientUser.objects.get(user=request.client.user)
        qs = Orders.objects.filter(client=client)
        return qs.count()
    
    def client_phone(self, request):
        client = ClientUser.objects.get(user=request.client.user)
        return client.phone
    
    def client_facebook(self, request):
        try:
            client = ClientUser.objects.get(user=request.client.user)
        except:
            pass
        return client.facebook_name
    
    def client_facebook_id(self, request):
        try:
            client = ClientUser.objects.get(user=request.client.user)
        except:
            pass
        return client.facebook_id
    
class OrdersProductAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'item',
        'quatity',
        'selected',
        'store',
        )
    list_display_links = ('client', 'item', 'store')
    list_filter = ('client', 'item', 'store')
    # search_fields = ['client', 'item', 'store']
    
    
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderProduct, OrdersProductAdmin)