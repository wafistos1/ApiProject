from django.contrib import admin
from django.conf.urls.static import static
from .api import ProductListView
from django.urls import path, include

urlpatterns = [
    
    path('product/', ProductListView.as_view(),),
]