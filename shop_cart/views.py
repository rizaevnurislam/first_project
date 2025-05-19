from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItem
from shop.models import Product
from django.http import JsonResponse


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    items = cart.items.select_related("product")

    # Получаем предыдущий URL
    previous_page = request.META.get('HTTP_REFERER',
                                     '/')  # Если нет реферера, переходит на главную  # Если нет, то главная

    return render(request, "shop_cart/cart.html", {
        "cart": cart,
        "items": items,
        "previous_page": previous_page,
    })


@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:  # ✅ Если товар уже в корзине, увеличиваем количество
        cart_item.quantity += 1
        cart_item.save()

    # Считаем общее количество товаров
    cart_count = sum(item.quantity for item in cart.items.all())

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"success": True, "cart_count": cart_count})

    return redirect("shop_cart:cart_detail")


@login_required
def cart_remove(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

    cart_item.delete()

    return redirect("shop_cart:cart_detail")


def checkout(request):
    return render(request, "shop_cart/checkout.html")


def update_cart(request, product_id, action):
    if request.method == "POST":
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, id=product_id)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if action == "increase":
            item.quantity += 1
        elif action == "decrease" and item.quantity > 1:
            item.quantity -= 1

        item.save()

        return JsonResponse({
            "success": True,
            "quantity": item.quantity,
            "product_total": item.get_total_price(),
            "total_price": cart.get_total_cost(),
        })

    return JsonResponse({"success": False})


def remove_from_cart(request, product_id):
    if request.method == "POST":
        cart, created = Cart.objects.get_or_create(user=request.user)
        item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
        if item:
            item.delete()

        return JsonResponse({
            "success": True,
            "total_price": cart.get_total_cost(),
        })

    return JsonResponse({"success": False})


@login_required
def cart_clear(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.all().delete()  # Удаляем все товары из корзины
    return redirect("shop_cart:cart_detail")


def cart_count_view(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_count = cart.items.count()
    return JsonResponse({"cart_count": cart_count})
