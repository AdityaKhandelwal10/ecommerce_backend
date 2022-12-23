from django.db import models

# Create your models here.
from sellers.models import Store, Category, Product
from base.models import User

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(decimal_places = 2, max_digits = 6)

    def __str__(self):
        id = str(self.id)
        return id
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name = 'order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.DecimalField(decimal_places = 2, max_digits = 6)
    total_price = models.DecimalField(decimal_places = 2, max_digits = 6)

    def __str__(self):
        return self.order

class CartItem(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.DecimalField(decimal_places = 2, max_digits = 6)
    total_price = models.DecimalField(decimal_places = 2, max_digits = 6)

    def __str__(self):
        return self.customer.first_name, self.product.product_name, self.price
       