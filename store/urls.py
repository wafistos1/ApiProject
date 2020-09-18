from django.contrib import admin
from django.urls import path, include
from .views import DeleveryView, OrdersView, CitiesView, DeleveryViewUpdate, OrdersViewUpdate, CitiesViewUpdate

urlpatterns = [
    path('develery/<int:id>', DeleveryViewUpdate.as_view(), name='delevery_update'),
    path('orders/<int:id>', OrdersViewUpdate.as_view(), name='orders_update'),
    path('address/<int:id>', CitiesViewUpdate.as_view(), name='address_update'),
    
    path('develery/', DeleveryView.as_view(), name='delevery'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('address/', CitiesView.as_view(), name='address'),
]