from decimal import Decimal, ROUND_HALF_UP
import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.utils import timezone
from core.forms import OrderForm
from core.models import Message
from django_cryptocoin.models import CryptoOrder, ExchangeRate
from django_cryptocoin.settings import CRYPTO_COINS


def home(request):
    price_usd = Decimal(0.1)
    crypto_prices = {}
    for currency in CRYPTO_COINS.keys():
        crypto_prices[currency] = Decimal(price_usd * ExchangeRate.get_exchange_rate('usd', currency))\
            .quantize(Decimal(10) ** -5, rounding=ROUND_HALF_UP)

    form = OrderForm(request.POST or None)
    if form.is_valid():
        crypto_order = CryptoOrder(
            currency=form.cleaned_data['currency'],
            amount=crypto_prices[form.cleaned_data['currency']],
            date=timezone.now(),
            redirect_to=reverse('home')
        )
        crypto_order.save()
        form.instance.crypto_order = crypto_order
        form.save()
        return redirect('cryptocoin-order-process', addr=crypto_order.addr)

    return render(request, 'home.html', {
        'form': form,
        'crypto_prices': crypto_prices,
        'messages': Message.objects.all()
    })