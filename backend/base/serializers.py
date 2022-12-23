from rest_framework import serializers
from .models import User

class SellerRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['phone', 'password']

