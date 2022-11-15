from django.shortcuts import render

# Create your views here.
from .models import User
from .serializers import SellerRegistrationSerializer
from rest_framework.generics import CreateAPIView

# class CreateSellerView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SellerRegistrationSerializer

#     def perform_create(self, serializer):
