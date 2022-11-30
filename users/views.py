import random
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, EditForm
from .models import Customer
from cart.models import Cart
from products.models import Order, OrderItem


def signup(request):
    if request.method == 'POST':
        auth_logout(request)
        form = SignupForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            user = User.objects.create_user(
                username=instance.username,
                password=instance.password,
                email=instance.email,
                first_name=instance.first_name
            )
            customer = Customer.objects.create(
                user=user,
                name=instance.first_name,
            )
            Cart.objects.create(
                customer=customer,
            )
            Order.objects.create(customer=customer)
            auth_user = authenticate(
                request, username=instance.username, password=instance.password)

            if auth_user is not None:
                auth_login(request, auth_user)
                return HttpResponseRedirect(f'/users/{customer.id}/')
            else:
                form = SignupForm()
                context = {
                    'title': 'Signup page',
                    'form': form,
                    'error': True,
                    'message': 'Invalid format or user already exists'
                }
                return render(request, 'users/signup.html', context)

        else:
            form = SignupForm()
            context = {
                'title': 'Signup page',
                'form': form,
                'error': True,
                'message': 'Invalid format or user already exists'
            }
            return render(request, 'users/signup.html', context)

    else:
        form = SignupForm()
        context = {
            'title': 'Signup page',
            'form': form
        }
        return render(request, 'users/signup.html', context)


def login(request):
    if request.method == 'POST':
        auth_logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect('/')
        else:
            context = {
                'title': 'Login Page',
                'error': True,
                'message': 'Invalid username or password'
            }
            return render(request, 'users/login.html', context)
    else:
        context = {
            'title': 'Login Page'
        }
        return render(request, 'users/login.html', context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login/')
def profile(request, pk):
    user = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':

        form = EditForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(f'/users/{pk}/')

    initial = {
        'phone': user.phone,
        'address': user.address,
        'pin_code': user.pin_code
    }

    form = EditForm(initial=initial)
    cart_items = user.cart.items.all()
    orders = user.order.items.all().order_by('-ordered_date')
    context = {
        'user': user,
        'cart_items': cart_items,
        'title': user.name,
        'form': form,
        'orders':orders,
        'country': 0
    }
    return render(request, 'users/profile.html', context)



def orders(request,pk):
    user = get_object_or_404(Customer, pk=pk)
    orders = user.order.items.all().order_by('-ordered_date')
    is_author = False 
    if user.id == request.user.customer.id:
        is_author = True

    context = {
        'orders': orders,
        'is_author':is_author
    }
    return render(request, 'users/orders.html',context)



def order_item(request,id):
    order = OrderItem.objects.get(id=id)
    context = {
        'order':order
    }
    return render(request, 'users/order_item.html', context)