from django import forms
from .models import Order


        
class ChargeForm(forms.Form):
    amount = forms.DecimalField(label='Amount',  min_value=0)