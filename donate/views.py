from django.shortcuts import render
from django.conf import settings

import stripe

# Create your views here.
def donate(request):
    return render(request, 'donate/donate.html')
    
def charge(request):
    if request.method == 'GET':
        amount = int(request.GET['amount']) * 100
        return render(request, 'donate/charge.html', {
            'amount' : amount,
            'key' : settings.STRIPE_PUBLISHABLE_KEY
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount=request.POST['amount'],
            currency='usd',
            description='A Django charge',
            source=token
        )

        # d = Donation()
        # d.donated_by = request.user
        # d.amount = amount
        # d.save()

        return render(request, "donate/thank-you.html")