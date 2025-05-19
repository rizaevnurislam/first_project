from shop_cart.models import Cart


def cart(request):
    cart_data = None
    if request.user.is_authenticated:
        cart_data, created = Cart.objects.get_or_create(user=request.user)
    return {"cart": cart_data}  # Добавляем cart в контекст
