from django.urls import path
from . import views
from .views import checkout, remove_from_cart, update_cart, cart_count_view

app_name = "shop_cart"

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("add/<int:product_id>/", views.cart_add, name="cart_add"),
    path("remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("checkout/", checkout, name="checkout"),
    path("update/<int:product_id>/<str:action>/", update_cart, name="update_cart"),
    path("remove/<int:product_id>/", remove_from_cart, name="remove_from_cart"),
    path("clear/", views.cart_clear, name="clear"),
    path("count/", cart_count_view, name="cart_count")

]
