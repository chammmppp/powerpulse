from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, email=email, password=password
        )
        user.save()
    else:

        return render(request, "register/signup.html")


def login(request):
    return render(request, "register/login.html")


def logout(request):
    pass
