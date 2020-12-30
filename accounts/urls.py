
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     # Djoser
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken')),
    
    # rest-auth
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')), 
    
]