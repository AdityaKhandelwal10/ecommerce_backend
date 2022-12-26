

# Create your views here.
from .models import User
from .serializers import ( 
    UserLoginRequestSerializer,
    UserOTPVerifyRequestSerializer, 
    UserOTPVerifyResponseSerializer,
    UserSignUpSerializer,
    )
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# class CreateSellerView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SellerRegistrationSerializer

#     def perform_create(self, serializer):

class LoginView(APIView):
    """
    Takes in the phone number and sends the OTP to the user
    """
    serializer_class = UserLoginRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        
        """
        Check if the user exists, if it doesn't raise an error
        """
        try:
            user = User.objects.select_for_update().get(phone = request.data['phone'])
        except User.DoesNotExist:
            raise ValueError("User does not exist")

        """
        Call the function here to send the OTP, we will assume that the OTP has been sent
        """
        return Response("An OTP has been sent to your mobile number. Please call the verify API to authenticate")

class VerifyView(APIView):

    serializer_class = UserOTPVerifyRequestSerializer
    permission_classes = [AllowAny]
    """
    verifies if the OTP is correct and issues an access token
    """
    def post(self, request):

        phone = request.data['phone']
        #Check if the User exists or not
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise ValueError("User does not exist")
        
        """ 
        Send the OTP here and store if it was a success
        We are going to bypass that process and set success to True
        """
        # success = True

        user_data = UserOTPVerifyResponseSerializer(user).data
        return Response(user_data)

class UserSignUpView(CreateAPIView):

    serializer_class=UserSignUpSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    
