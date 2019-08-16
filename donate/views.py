from django.shortcuts import render
from django.conf import settings
from .forms import OrderForm, PaymentForm
import stripe
from django.utils import timezone
from django.contrib import messages

def donate(request):
    return render(request, 'donate/donate.html')
    
def charge(request):
    amount = request.GET['amount']
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method=='GET':
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'donate/charge.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'publishable' : publishable_key
        })
    else:
        # retrieve the token
        token = request.POST['stripe_id']
        
        # setup the api_key for the stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
           
            # get the amount the user is supposed to pay
            # IMPT: If you having a shopping cart, YOU MUST
            # recalculate the amount based on the cart
            total = request.POST['amount']
            
            try:
                # try to charge the customer
                customer = stripe.Charge.create(
                    amount = int(total) * 100,
                    currency = "SGD",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
                
                # if charge is successful
                if customer.paid:
                    # confirm the order
                    order = order_form.save(commit=False)
                    order.date=timezone.now()
                    order.save()
            
                    messages.error(request, "You have successfully paid")

                    # goes to a thank-you page
                    return render(request, 'donate/thank-you.html')
                else:
                    messages.error(request, "Unable to take payment")
                    
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            return render(request, 'donate/charge.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'publishable' : publishable_key
        })
        
        
        