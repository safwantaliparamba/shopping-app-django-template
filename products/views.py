from django.shortcuts import render

from .models import Product


def single_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'products/single_page.html', context)