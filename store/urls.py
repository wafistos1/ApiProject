from django.urls import path, include
from .api import (
    ProductOrdersAdminView,
    AddItemCartView,
    OrdersAdminView,
    updateDeleteItemCartView,
    UpdateOrderUserView,
    OrderCreateUserView
    )

    
urlpatterns = [
    # path('orders/<int:id>', OrdersViewUpdate.as_view(), name='orders_update'),
    path('orders-admin/', OrdersAdminView.as_view(), name='orders'),
    path('order-user/', OrderCreateUserView.as_view(), name='order-user'),
    path('order-user/<int:id>', UpdateOrderUserView.as_view(), name='order-user-get'),
    
    path('order-product/', AddItemCartView.as_view(),),
    path('order-product/<int:pk>', updateDeleteItemCartView.as_view(),),
    
    path('order-product-admin/', ProductOrdersAdminView.as_view(),),
]