from django.shortcuts import render
from .models import Product

def all_products(request):
    # products = Product.objects.all()
    # for product in products:
    #     product.save()
    products = Product.objects.exclude(image_url__isnull=True).exclude(image_url__exact='').exclude(image_url__exact='[]').all()
    context = {
        'products': products,
        
    }
    return render(request, 'products/products.html', context)
