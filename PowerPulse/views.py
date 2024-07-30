from django.shortcuts import render
from store.models import Product


def home(request):
    popular_products = Product.objects.all().filter(is_trending=True)
    context = {
        'popular_products': popular_products,
    }
    return render(request, 'home.html', context)


def checkout(request):
    return render(request, 'checkout.html')


def login(request):
    return render(request, 'register/login.html')


def signup(request):
    return render(request, 'register/signup.html')


def profile(request):
    return render(request, 'profiles/profile.html')


def address(request):
    return render(request, 'profiles/address.html')
