from django.db import models
from accounts.models import ClientUser, DeliveryMan, Address, DeliveryMan
from shop.models import Product, Store


class OrderProduct(models.Model):
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE, related_name='client_order')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='client_product')
    quatity = models.IntegerField(default=1)
    selected = models.BooleanField(default=False, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    
    
    
    def __str__(self):
        return f'Id: {self.pk}: [Quantity:{self.quatity} item: {self.item.name}] Owner: {self.client.user.username.upper()}'
    
    def get_total_price(self):
        pass
    
    def get_total_item(self):
        pass
    
    def get_amount_saved(self):
        pass
    
    def get_final_price(self):
        pass
    
    def get_remove_product_orders(self):
        pass
    
    def get_total_orderProduct(self):
        pass


class Orders(models.Model):
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE, related_name='Client_order')
    delevery_man = models.ForeignKey(DeliveryMan, on_delete=models.SET_NULL, null=True)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(Address, related_name='shipping_address', on_delete=models.SET_NULL, null=True)
    # Orders status
    being_deliverd = models.BooleanField(default=False) 
    received = models.BooleanField(default=False) 
    refund_requested = models.BooleanField(default=False) 
    refund_granted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['start_date']
    
    def __str__(self):
        return f'[{self.client.user.username.upper()}-->{self.shipping_address.location}] Delevered By {self.delevery_man.user.username.upper()}'
     
    def get_total(self):
        pass
