from django.urls import path

from .views import (BasicStoreDetailView, 
    StoreProductsCatelogView, 
    AddItemToCartView, 
    CartToOrderItemView)


urlpatterns = [
    path('basic-store-detail/', BasicStoreDetailView.as_view(), name='basic-store-detail'),
    path('store-catelog/', StoreProductsCatelogView.as_view(), name='store-catelog'),
    path('add-item-to-cart/', AddItemToCartView.as_view(), name = 'add-item-to-cart'),
    path('create-order/', CartToOrderItemView.as_view(), name='create-order'),
   
    
]
