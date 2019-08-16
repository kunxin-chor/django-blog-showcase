from django.shortcuts import render, reverse, HttpResponse
from django.conf import settings
import stripe


def donate(request):
    return render(request, 'donate/donate.html')
    
def charge(request):
    amount = int( request.GET['amount']) * 100
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(payment_method_types=['card'],
        line_items=[
            {
                'name': 'Donation',
                'description':'A simple donation',
                'amount':amount ,
                'currency':'usd',
                'quantity':1
            }
        ],
        success_url= request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel'))
    )
    return render(request, 'donate/charge.html', {
        'CHECKOUT_SESSION_ID': session.id,
        'publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })
    
   
    
def success(request):
    return HttpResponse("We have gotten your money")
    
def cancel(request):
    return HttpResponse("No, don't go!")
        
        