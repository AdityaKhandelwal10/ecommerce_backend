from rest_framework import serializers
from sellers import models as sellers_models
from .models import Order, OrderItem, CartItem


class BasicStoreDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = sellers_models.Store
        fields = ['id', 'store_name', 'address', 'store_link']
        read_only_fields = ['store_link']

class StoreProductsCatelogSerializer(serializers.ModelSerializer):

    class Meta:
        model = sellers_models.Product
        fields = ['category', 'product_name', 'description', 'mrp', 'sale_price']

class AddItemToCartSerializers(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['customer', 'product' , 'quantity' , 'price', 'total_price']
        read_only_fields = ['price','total_price']

    def get_total_price(self, price, quantity):
        return price*quantity
    
    def get_price(self, product):
        return product.price

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'total_price']


class CartToOrderItemSerializer(serializers.ModelSerializer):

    # order = OrderCreateSerializer()

    class Meta: 
        model = OrderItem
        fields = ['product' , 'quantity' , 'price', 'total_price']
    
    def create(self, validated_data):
        request = self.context.get('request')
        customer = request.user
        #function for total price
        order_total_price = 100
        
        order = Order.objects.create(customer=customer, total_price = order_total_price)
        order_item = OrderItem.objects.create(
            order = order,
            product = validated_data.get('product'), 
            quantity = validated_data.get('quantity'),
            price = validated_data.get('price'),
            total_price = validated_data.get('total_price')
             )
        return order_item

