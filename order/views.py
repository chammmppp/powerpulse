from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from carts.models import Cart, CartItem
from order.models import Order, OrderDetail
from store.models import Product
from carts.views import _cart_id
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


@login_required(login_url="/login")
def checkout(request):
    total = 0
    tax_rate = 0.07
    grand_total = 0
    quantity = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)

        for item in cart_items:
            total += item.product.price * item.quantity
            quantity += item.quantity
            tax = round(tax_rate * total, 2)  # คำนวณภาษี
            grand_total = total + tax

    except ObjectDoesNotExist:
        cart_items = None

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        house_no = request.POST.get("house_no")
        village_no = request.POST.get("village_no")
        lane = request.POST.get("lane")
        road = request.POST.get("road")
        sub_district = request.POST.get("sub_district")
        district = request.POST.get("district")
        province = request.POST.get("province")
        postal_code = request.POST.get("postal_code")

        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone,
            house_no=house_no,
            village_no=village_no,
            lane=lane,
            road=road,
            sub_district=sub_district,
            district=district,
            province=province,
            postal_code=postal_code,
            user=request.user,
            total=total,
        )
        order.save()

        for item in cart_items:
            detail_order = OrderDetail.objects.create(
                product=item.product,  # Store Product object
                quantity=item.quantity,
                price=item.product.price,
                order=order,
            )
            detail_order.save()

            # Deduct stock
            product = Product.objects.get(pk=item.product.id)
            product.stock -= item.quantity
            product.save()
            item.delete()

        # cart.delete()
        cart_items.delete()
        order_completed = True
        return render(request, "checkout.html", {"order_completed": order_completed})

    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_items,
        "tax": tax,
        "grand_total": grand_total,
    }
    return render(request, "checkout.html", context)
