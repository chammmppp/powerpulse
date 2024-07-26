from django.shortcuts import render
from store.models import Product


def home(request):
    popular_products = Product.objects.all().filter(is_trending=True)
    context = {
        'popular_products': popular_products,
    }
    return render(request, 'home.html', context)


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


# def product_detail(request):
#     return render(request, 'product_detail.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')
