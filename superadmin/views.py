import json
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.decorator import superuser_only
from products.models import Product
from users.models import Customer
from cart.models import Cart
from cart.serializer import CartSerializer


def login(request):
    auth_logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                auth_login(request, user)

                return HttpResponseRedirect('/superadmin/dashboard/')

            else:
                return HttpResponseRedirect('/')
        else:
            context = {
                'title': 'Login Page',
                'error': True,
                'message': 'Invalid username or password'
            }
            return render(request, 'superadmin/login.html', context)
    else:
        context = {
            'title': 'Login Page',
        }
        return render(request, 'superadmin/login.html', context)


@superuser_only
def dashboard(request):
    return render(request, 'superadmin/dashboard.html')


@superuser_only
def manage_users(request):
    # products = Product.objects.all()
    customers = Customer.objects.all().order_by('-created_at').filter(is_deleted=False)
    if request.GET.get('filter_by'):
        filter = request.GET.get('filter_by')
        if filter == 'latest':
            customers = customers.order_by('-created_at')
        if filter == 'oldest':
            customers = customers.order_by('created_at')
    if request.GET.get('q'):
        q = request.GET.get('q')
        customers = customers.filter(name__istartswith=q)

    context = {
        'customers': customers
    }
    return render(request, 'superadmin/users.html', context)


@api_view(['GET'])
def fetch_cart(request, id):
    cart = Cart.objects.get(id=id)
    cart_items = CartSerializer(cart)
    if not cart_items.data:
        print('data not found')
        return Response(cart_items.data)
    else:
        return Response(cart_items.data)


def view_user_profile(request, pk):
    user = get_object_or_404(Customer, pk=pk)
    context = {'user': user}
    return render(request, 'superadmin/view_user.html',context)
