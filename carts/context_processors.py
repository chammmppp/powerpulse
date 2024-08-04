from .models import Cart, CartItem
from . import _cart_id

def counter(request):
    if "admin" in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id= _cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
        except 