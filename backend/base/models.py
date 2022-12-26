from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser, User


class CustomUserManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('Users must have a Phone number')
        
        user = self.model(phone = phone, **extra_fields)
        # user.set_unusable_password()
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password = None):
        user = self.create_user(phone = phone, password = password)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

#Expose different views for sellers and buyers, (can do it at view or serializer)

class User(AbstractBaseUser, PermissionsMixin):

    phone = models.CharField(max_length=12, blank= False, unique=True)
    first_name = models.CharField(max_length=20, blank= True)
    last_name = models.CharField(max_length=20, blank = True)
    is_seller = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    class Meta:
        verbose_name = ('Account')
        verbose_name_plural = ("Accounts")
        
        

    def __str__(self):
        
        return self.phone
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.phone

    def get_short_name(self):
        # The user is identified by their email address
        return self.phone