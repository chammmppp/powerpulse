from django.shortcuts import render, get_object_or_404

from store.models import Product
from category.models import Category


# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category,
                                       slug=category_slug)  # Get an object if not exist it's will be raises 404
        products = Product.objects.filter(category=categories,
                                          is_available=True)  # Get object products that exist on database
    else:
        products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'product_detail.html', context)
