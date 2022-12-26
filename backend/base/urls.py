from django.urls import path


from .views import LoginView, VerifyView, UserSignUpView

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('verify/', VerifyView.as_view(), name='verify'),
    path('sign-up/', UserSignUpView.as_view(), name='sign-up')
    
]
