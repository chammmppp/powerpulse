from django.db import models
from accounts.models import Account
from store.models import Product

# from django.utils import timezone

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now)
    payment_proof = models.FileField(
        upload_to="photos/payment_proof", null=True, blank=True
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    house_no = models.CharField(max_length=10)
    village_no = models.CharField(max_length=10, blank=True, null=True)
    lane = models.CharField(max_length=255, blank=True, null=True)
    road = models.CharField(max_length=255, blank=True, null=True)
    sub_district = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.email


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def sub_total(self):
        return self.product.price * self.quantity
