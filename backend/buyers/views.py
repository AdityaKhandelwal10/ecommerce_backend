from rest_framework.views import APIView
from rest_framework import generics
from sellers import models as sellers_models
from .models import Order, OrderItem, CartItem
from .serializers import (BasicStoreDetailsSerializer, 
                        StoreProductsCatelogSerializer, 
                        AddItemToCartSerializers, 
                        CartToOrderItemSerializer, 
                       )


class BasicStoreDetailView(generics.ListAPIView):

    serializer_class = BasicStoreDetailsSerializer

    # def get(self, request, store_link, format=None):
    #     store_link = request.data['store_link']
    #     store_link_arr = store_link.split("/")
    #     store_id = store_link_arr[-1]

    #     store = sellers_models.Store.objects.filter(pk = store_id)
    #     return store

    def get_queryset(self):
        """
        Pass the store link as a query_param - {site}?storelink=<storelink> 
        """
        store_link = self.request.query_params.get('storelink')
        store_link_arr = store_link.split("/")
        store_id = store_link_arr[-1]
        store =  sellers_models.Store.objects.filter(pk = store_id)
        return store

class StoreProductsCatelogView(generics.ListAPIView):

    serializer_class = StoreProductsCatelogSerializer

    def get_queryset(self):
        """
        Pass the store link as a query_param - {site}?storelink=<storelink> 
        """
        store_link = self.request.query_params.get('storelink')
        store_link_arr = store_link.split("/")
        store_id = store_link_arr[-1]
        products =  sellers_models.Product.objects.filter(store_id = store_id)
        return products

class AddItemToCartView(generics.ListCreateAPIView):

    serializer_class = AddItemToCartSerializers

    def get_queryset(self):
        customer = self.request.user
        cart_items = CartItem.objects.filter(customer=customer)
        return cart_items

class CartToOrderItemView(generics.ListCreateAPIView):

    serializer_class = CartToOrderItemSerializer

    def get_queryset(self):
        customer = self.request.user
        cart = CartItem.objects.filter(customer=customer)
        return cart

