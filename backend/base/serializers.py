from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token

# class SellerRegistrationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['phone', 'password']


class UserSignUpSerializer(serializers.Serializer):
    """
    Serializer for Users to Signup and set if they are a seller or not.
    Frontend needs to send information about 'is_seller' 
    """
    phone = serializers.IntegerField(required=True)
    is_seller = serializers.BooleanField(default=False)

    def create(self, validated_data):
        phone = validated_data['phone']
        is_seller = validated_data['is_seller']
        
        try:
            user = User.objects.create_user(phone=phone)
            user.is_seller = is_seller
            user.save()
            return user
        except Exception as e:
            raise e

class UserLoginRequestSerializer(serializers.Serializer):
    """
    User Login Serializer
    """
    phone = serializers.IntegerField(required=True)

    def validate(self, data):
        """
        Check for the phone number
        """
        lower_phone_limit = 1000000000
        upper_phone_limit = 9999999999
        
        phone = data['mobile']
        if lower_phone_limit<=phone<=upper_phone_limit:
            return data
        else:
            raise ValidationError({'phone': 'Please enter a valid phone number.'})

# class UserLoginResponseSerializer(serializers.Serializer):
#     """
#     After User has entered the number for login
#     """

class UserOTPVerifyRequestSerializer(serializers.Serializer):
    """
    User OTP Verify Request Serializer
    """
    phone = serializers.IntegerField()
    otp = serializers.IntegerField()


class UserOTPVerifyResponseSerializer(serializers.ModelSerializer):
    """
    User OTP Verify Response Serializer which gives back an access token
    """
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'phone',
            'first_name',
            'last_name',
            'is_seller',
            'access_token',
        ]
        read_only_fields = ['access_token']

    def get_access_token(self,user):
        """
        returns access token for User
        """
        token,_ = Token.objects.get_or_create(user=user)
        return token.key