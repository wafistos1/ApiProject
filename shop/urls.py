from django.contrib import admin
from django.conf.urls.static import static
from .api import (
    ProductListUserView,
    ProductUserSearchView,
    DisplayProductStoreView,
    )
from django.urls import path, include

urlpatterns = [
    
    path('product/', ProductListUserView.as_view(),),
    
    path('product-search/<str:query>', ProductUserSearchView.as_view()),
    path('store-product/<str:store>', DisplayProductStoreView.as_view()), 
]