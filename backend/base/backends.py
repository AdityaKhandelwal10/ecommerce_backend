from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model



User = get_user_model()

def authenticate_otp(self, otp):
        """"
        Logic to authenticate if otp is valid. 
        To bypass this is set to True
        """
        #Logic comes here

        return True

class CustomModelBackend(ModelBackend):

    def authenticate(self, request, phone = None, otp = None):
        
        if phone and otp:
            try:
                user = User.objects.get(phone = phone)
                valid_otp = authenticate_otp(self,otp)
                if valid_otp:
                    return user
            except User.DoesNotExist:
                return None
                