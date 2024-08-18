from django.shortcuts import render
from store.models import Product


def home(request):
    popular_products = Product.objects.all().filter(is_trending=True)
    context = {
        "popular_products": popular_products,
    }
    return render(request, "home.html", context)
