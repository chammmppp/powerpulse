from . import views
from django.urls import path

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("my_account/", views.my_account, name="my_account"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
]
