from django.urls import path, include
from .views import index, charge
urlpatterns = [
    path('', index),
    path('charge/', charge, name='charge')
  
] 
