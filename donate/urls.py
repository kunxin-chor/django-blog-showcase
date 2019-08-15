from django.urls import path
from .views import donate, charge

urlpatterns = [
    path('', donate, name='donate'),
    path('charge/', charge, name='charge')

]
