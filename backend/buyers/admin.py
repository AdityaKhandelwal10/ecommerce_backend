from django.contrib import admin
from .models import CartItem, Order

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderDetailAdmin(admin.ModelAdmin):
    pass