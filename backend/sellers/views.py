from rest_framework import generics
 
# Create your views here.
from .models import Store, Category, Product
from .serializers import CreateStoreSerializer, CategorySerializer

class CreateStoreView(generics.CreateAPIView):

    queryset = Store.objects.all()
    serializer_class = CreateStoreSerializer

    # def perform_create(self, serializer):

class ListCreateCategoryView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    