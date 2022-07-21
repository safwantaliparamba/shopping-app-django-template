from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

from .models import Cart
from products.models import Product


def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    user = request.user.customer

    try:
        is_on_cart = {}
        is_on_cart.quantity = is_on_cart.quantity + 1
    except:
        Cart.objects.create(
            product=product,
            customer=user
        )

    return HttpResponseRedirect('/')
