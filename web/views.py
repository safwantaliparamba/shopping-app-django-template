from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from products.models import Product

@login_required(login_url='/users/login/')
def index(request):
    products = Product.objects.all().order_by('-added_date')
    
    not_found = False
    if request.GET.get('category'):
        category = request.GET.get('category')
        products = products.filter(category=category)

    if request.GET.get('q'):
        q = request.GET.get('q')
        products = products.filter(name__istartswith=q)
        if not products:
            not_found = True

    context = {
        'products': products,
        'not_found': not_found
    }
    return render(request, 'web/index.html',context)
