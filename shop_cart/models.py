from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class CartManager(models.Manager):
    pass


class Cart(models.Model):
    objects = CartManager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Один пользователь – одна корзина

    def __str__(self):
        return f"Корзина {self.user.username}"

    def get_total_price(self):
        pass


class CartItemManager(models.Manager):
    pass


class CartItem(models.Model):
    objects = CartItemManager()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
