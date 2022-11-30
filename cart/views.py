import json
from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Cart, CartItem
from products.models import Product, OrderItem


@login_required(login_url='/users/login/')
def add_to_cart(request, pro_id):
    product = Product.objects.get(id=pro_id)
    cart = request.user.customer.cart
    try:
        is_on_cart = cart.items.get(product=product)
    except:
        is_on_cart = False
    finally:
        if is_on_cart:
            is_on_cart.quantity = is_on_cart.quantity + 1
            is_on_cart.save()
        else:
            CartItem.objects.create(
                product=product,
                cart=cart,
                quantity=1
            )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login/')
def view_cart(request):
    cart = request.user.customer.cart
    cart_items = cart.items.all()

    product_total = 0
    delivery_charges = 0
    discount_total = 0

    query_link = ''

    for item in cart_items:
        product_total = product_total + item.total_price
        delivery_charges += item.product.delivery_charge
        discount_total += item.product.discount * item.quantity

        query_link += f'pro_id={item.product.id}&quantity={item.quantity}&'

    cart_total = (delivery_charges + product_total) - discount_total

    context = {
        'title': 'View Cart',
        'cart_items': cart_items,
        'product_total': product_total,
        'delivery_charges': delivery_charges,
        'cart_total': cart_total,
        'discount_total': discount_total,
        'query_link': query_link
    }
    return render(request, 'cart/view_cart.html', context)


@login_required(login_url='/users/login/')
def remove_from_cart(request, pro_id):
    product = Product.objects.get(id=pro_id)
    cart = request.user.customer.cart
    cart_item = cart.items.get(product=product)
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()

    return HttpResponseRedirect('/cart/')


def checkout(request):
    pro_id = request.GET.getlist('pro_id')
    quantities = request.GET.getlist('quantity')

    is_cart = False
    if request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/cart/':
        is_cart = True

    items = []
    cart_items = []
    for i in range(len(pro_id)):
        product = Product.objects.get(id=pro_id[i])
        cart_items.append({
            'pro_id': product.id,
            'image': product.image,
            'price': product.total_price,
            'quantity': int(quantities[i]),
            'total_price': (int(quantities[i]) * product.total_price)
        })
        item = {
            'product': product,
            'quantity': int(quantities[i]),
            'total_price': (int(quantities[i]) * product.total_price)
        }
        items.append(item)


    product_total = 0
    delivery_charges = 0
    discount_total = 0

    for item in items:
        product_total += item['total_price']
        delivery_charges += item['product'].delivery_charge
        discount_total += item['product'].discount * item['quantity']

    cart_total = (delivery_charges + product_total) - discount_total

    context = {
        'title': 'View Cart',
        'cart_items': cart_items,
        'product_total': product_total,
        'delivery_charges': delivery_charges,
        'cart_total': cart_total,
        'discount_total': discount_total,
        'is_cart': is_cart
    }
    return render(request, 'cart/checkout.html', context)


def checkout_confirm(request):
    payment_method = request.POST.get('payment_method')
    pro_id = request.POST.getlist('pro_id')
    quantities = request.POST.getlist('quantity')
    total_price = request.POST.getlist('total_price')
    is_cart = request.POST.get('is_cart')

    user = request.user.customer

    items = []
    for i in range(len(pro_id)):
        product = Product.objects.get(id=pro_id[i])
        product.total_quantity = product.total_quantity - 1
        product.save()
        order = OrderItem.objects.create(
            order=user.order,
            product=product,
            quantity=int(quantities[i]),
            payment_method=payment_method,
            total_price=int(total_price[i])
        )

    if is_cart == 'True':
        user.cart.items.all().delete()

    response_obj = {
        'status':'success',
        'redirect':f'/users/order/{order.id}/'
    }

    return HttpResponse(json.dumps(response_obj))


def cancel_order(request, id):
    item = get_object_or_404(OrderItem, id=id)
    item.is_canceled = True
    item.save()

    return HttpResponseRedirect(f'/users/{request.user.customer.id}/')