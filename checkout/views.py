from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.contexts import cart_contents

import stripe
import json


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OuQHlP4n1eUx6wh21cWopbPzKxoBf2vBiJRIuf6Ovdfd37HOBJp1F7stG0vvDWaKyJ4FT3R0681RzyAua4ECDU800st7Gi8aX',
        'client_secret': 'client_secret',
    }

    return render(request, template, context)