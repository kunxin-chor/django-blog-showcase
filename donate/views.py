from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
import stripe
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
            'order_form' : OrderForm(),
            'amount': request.GET['amount']
        })
    
    else:
        #process form
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            total = request.POST['amount']
            stripe.api_key = settings.STRIPE_SECRET_KEY
            customer = None
            try:
                customer = stripe.Charge.create(
                    amount = int(total) * 100,
                    currency = "SGD",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
                
                
                if customer.paid:
                    messages.error(request, "You have successfully paid")
                    request.session['cart'] = {}
                    return render(request, 'donate/thank-you.html')
                else:
                    messages.error(request, "Unable to take payment")
                    
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                    
           
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
        #show the form again along with the error messages
        return render(request, 'donate/charge.html', {
            'publishable' : settings.STRIPE_PUBLISHABLE_KEY,
            'payment_form' : payment_form,
            'order_form' : order_form,
            'amount': request.GET['amount']
        })
