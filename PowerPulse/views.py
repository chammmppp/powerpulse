from django.shortcuts import render
from store.models import Product


def home(request):
    popular_products = Product.objects.all().filter(is_trending=True)
    context = {
        "popular_products": popular_products,
    }
    return render(request, "home.html", context)


def my_account(request):
    return render(request, "profiles/my_account.html")


def address(request):
    return render(request, "profiles/address.html")


def order_purchases(request):
    return render(request, "profiles/history_purchase.html")
