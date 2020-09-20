from django.urls import path, include
from .api import OrdersAllView, AddItemCartView, productOrdersAllView, updateDeleteItemCartView

    
urlpatterns = [
    # path('orders/<int:id>', OrdersViewUpdate.as_view(), name='orders_update'),
    path('orders/', OrdersAllView.as_view(), name='orders'),
    
    path('order-product/', AddItemCartView.as_view(),),
    path('order-product/<int:pk>', updateDeleteItemCartView.as_view(),),
    
    path('orderproduct/', productOrdersAllView.as_view(),),
]