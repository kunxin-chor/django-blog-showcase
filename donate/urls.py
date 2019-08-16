from django.urls import path, include
from .views import donate, charge, success, cancel
urlpatterns = [
    path('', donate, name='donate'),
    path('charge/', charge, name='charge'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel')
  
] 
