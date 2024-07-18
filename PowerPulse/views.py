from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())


def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())


def detailproduct(request):
    template = loader.get_template('detailproduct.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())


def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())


def store(request):
    template = loader.get_template('store.html')
    return HttpResponse(template.render())
