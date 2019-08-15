from django.shortcuts import render
from .forms import ChargeForm
from django.conf import settings
import stripe
# Create your views here.
def index(request):
    return render(request, 'donate/index.html', {
        'form' : ChargeForm()
    })
        
def charge(request):
    if request.method == 'GET':
        amount = int(request.GET['amount']) * 100
        key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'donate/charge.html',{
            'key' : key,
            'amount' : amount
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=int(request.POST['amount']),
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, "donate/thank-you.html")
    
