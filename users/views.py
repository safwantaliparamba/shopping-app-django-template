from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.shortcuts import HttpResponseRedirect

from .forms import SignupForm
from .models import Customer


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            user = User.objects.create_user(
                username=instance.username,
                password=instance.password,
                email=instance.email,
                first_name=instance.first_name,
            )
            customer = Customer.objects.create(
                user=user,
                name=instance.first_name,
            )
            auth_user = authenticate(request,username=instance.username,password=instance.password)

            if auth_user is not None:
                auth_login(request, auth_user)
                return HttpResponseRedirect('/')
            else:
                form = SignupForm()
                context = {
                    'form': form,
                    'error': True,
                    'message': 'Invalid format or user already exists'
                }
                return render(request, 'users/signup.html', context)

        else:
            form = SignupForm()
            context = {
                'form': form,
                'error': True,
                'message': 'Invalid format or user already exists'
            }
            return render(request, 'users/signup.html', context)

    else:
        form = SignupForm()
        context = {
            'form': form
        }
        return render(request, 'users/signup.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            auth_login(request, user)

            return HttpResponseRedirect('/')
        else:
            context = {
                'error': True,
                'message': 'Invalid username or password'
            }
            return render(request, 'users/login.html',context)
    else:
        return render(request, 'users/login.html')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
