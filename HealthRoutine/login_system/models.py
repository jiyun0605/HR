from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,UserManager

class User(AbstractBaseUser,PermissionsMixin):        

    objects = UserManager()
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'username'
    REQUIRED_FILEDS = ['email']