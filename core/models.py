from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django_cryptocoin.models import CryptoOrder
from django_cryptocoin.signals import after_pay_confirmation


class Message(models.Model):
    text = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()


class Order(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    comment = models.CharField('Comment for order', max_length=500, default='', blank=True)

    crypto_order = models.OneToOneField(CryptoOrder, related_name='order')

@receiver(after_pay_confirmation)
def send_message(sender, **kwargs):
    Message(
        date=timezone.now(),
        text=sender.order.text,
        author=sender.order.name
    ).save()
