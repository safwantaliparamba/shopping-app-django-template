from django.shortcuts import render

from products.models import Product


def index(request):
    products = Product.objects.all().order_by('-added_date')
    context = {
        'products': products
    }
    return render(request, 'web/index.html',context)
