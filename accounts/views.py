from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import Account
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        conform_password = request.POST.get("conform_password")

        if Account.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists.")
            return redirect("signup")
        elif password != conform_password:
            messages.warning(request, "Password do not match.")
            return redirect("signup")

        user = Account.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect("login")
    else:
        return render(request, "register/signup.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.warning(request, "Invalid email or password.")
            return redirect("login")

    return render(request, "register/login.html")


def logout(request):
    auth.logout(request)
    return redirect("login")


def my_account(request):
    return render(request, "profiles/my_account.html")


def userProfile(request):
    user = request.user
    context = {"user": user}
    return render(request, "profiles/my_account.html", context)


@login_required(login_url="/login") # To check if the user doesn't login -> If user doesn't login it'll take the user to login page
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        print("Edit profile test")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.phone_number = request.POST.get("phone_number")
        user.save()

    return redirect("my_account")
