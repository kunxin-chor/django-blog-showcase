from django.shortcuts import render
from django.conf import settings
from .forms import *

# Create your views here.
def donate(request):
    return render(request, 'donate/donate.html')
    
def charge(request):
    if request.method == 'GET':
        #show form
        return render(request, 'donate/charge.html', {
            'publishable' : settings.STRIPE_PUBLISHABLE_KEY,
            'payment_form' : PaymentForm(),
            'order_form' : OrderForm()
        })
    
    else:
        pass
        #process form
        
