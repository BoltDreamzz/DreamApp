# forms.py

from django import forms


class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    phone_number = forms.CharField(max_length=15)
    shipping_address = forms.CharField(widget=forms.Textarea)
