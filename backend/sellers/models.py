from django.db import models

from base.models import User

class Store(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length = 50, blank= False, null= False)
    address = models.TextField(blank= False, null= False)
    store_link = models.URLField()

    def __str__(self):
        return self.store_name

class Category(models.Model):
    
    category_name = models.CharField(max_length = 50, blank= False)

    def __str__(self):
        return self.category_name

class Product(models.Model):

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 50, blank= False)
    description = models.TextField()
    mrp = models.DecimalField(decimal_places = 2, max_digits = 6)
    sale_price = models.DecimalField(decimal_places = 2, max_digits = 6)

    def __str__(self):
        return self.product_name
