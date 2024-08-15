from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.contrib import messages


def _cart_id(request):
    cart = (
        request.session.session_key
    )  # Get the session key from the user's session data
    if not cart:  # Checks if a session key does not exist.
        cart = request.session.create()  # Create a new session
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)  # Get the product by unique id

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()  # save() is a method in Django to save the current sate of the cart object to the database

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1  # เพิ่ม quantity ตามที่ผู้ใช้เลือก
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,  # ใช้ quantity ที่ผู้ใช้เลือก
            cart=cart,
        )
        cart_item.save()
    return redirect("cart")


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("cart")


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect("cart")


# Create your views here.
def cart(request, total=0, quantity=0, cart_items=None):
    tax_rate = 0.07
    grand_total = 0
    tax = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (
                cart_item.product.price * cart_item.quantity
            )  # Product price * quantity
            quantity += cart_item.quantity
        tax = round(tax_rate * total, 2)
        grand_total = total + tax
    except ObjectDoesNotExist:
        cart_items = None

    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_items,
        "tax": tax,
        "grand_total": grand_total,
    }
    return render(request, "stores/cart.html", context)
