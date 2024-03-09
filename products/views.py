from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)