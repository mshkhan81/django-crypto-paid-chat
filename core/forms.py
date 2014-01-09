from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from django.forms import TextInput, Textarea
from core.models import Order
from django_cryptocoin.settings import CRYPTO_COINS


class OrderForm(forms.ModelForm):
    currency = forms.CharField(max_length=50, widget=forms.Select(choices=CRYPTO_COINS.items()))

    class Meta:
        model = Order
        exclude = ['date', 'crypto_order']

    helper = FormHelper()
    helper.form_tag = False
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
