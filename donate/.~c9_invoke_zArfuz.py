from django.shortcuts import render
from django.conf import settings
from .forms import OrderForm, PaymentForm


def donate(request):
    return render(request, 'donate/donate.html')
    
def charge(request):
    amount = request.GET['amount']
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    order_form = OrderForm()
    payment_form = PaymentForm()
    return render(request, 'donate/charge.html', {
        'order_form' : order_form,
        'payment_form' : payment_form,
        'amount' : amount,
        'publishable' : publishable_key
    })