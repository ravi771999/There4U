from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

"""
    This User model is going to store the information of the User such as:
    email: email id of the user
    city: city where user resides
    state: state where user resides
    zipcode: to store the zipcode of the area of user
    phone: to store the phone number of the user
"""
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=50,null = True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    balance=models.IntegerField()
    phone=models.BigIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.



