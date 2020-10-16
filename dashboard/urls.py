from django.urls import path, include
from .views import dashboroadView, dashView


urlpatterns = [
    path('dashboard/', dashboroadView.as_view(), name='dashboard'),
    path('dash/', dashView.as_view(), name='dash'),
]