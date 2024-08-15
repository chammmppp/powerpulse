from django.urls import path
from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("order_history/", views.order_history, name="order_history"),
    path(
        "order_history/order_detail/<int:order_id>",
        views.order_detail,
        name="order_detail",
    ),
]
