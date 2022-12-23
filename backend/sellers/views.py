from rest_framework import generics
 
# Create your views here.
from .models import Store, Category, Product
from .serializers import CreateStoreSerializer, CategorySerializer, CreateProductSerializer
from .permissions import IsOwner, IsStoreOwner 

class CreateStoreView(generics.CreateAPIView):

    queryset = Store.objects.all()
    serializer_class = CreateStoreSerializer

    # def perform_create(self, serializer):
# class CreateStoreHyperLinkedView(generics.CreateAPIView):

#     queryset = Store.objects.all()
#     serializer_class = CreateStoreHyperLinkedSerializer


class ListCreateCategoryView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductCreateView(generics.CreateAPIView):

    serializer_class = CreateProductSerializer
    permission_classes = [IsStoreOwner]

    def get_queryset(self):
        queryset = Product.objects.filter(store = self.request.data.get('store'))