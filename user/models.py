from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from timestamp import models as timestamp_models

class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, user and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email,name and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = True
        user.staff=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,timestamp_models.Timestamp):
    """
    This User model is going to store the information of the User such as:
    email: email id of the user
    city: city where user resides
    state: state where user resides
    zipcode: to store the zipcode of the area of user
    phone: to store the phone number of the user
    """
    email = models.EmailField(
        verbose_name='Email_address',
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    state=models.CharField(max_length=50,null=True,blank=True)
    zipcode=models.IntegerField(blank=True,null=True)
    balance=models.IntegerField(null=True,default=1000,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    class META:
        indexes = [
            models.Index(fields=['created_at'], name='created_at_idx'),
        ]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their Username ;)
        return self.name

    def get_short_name(self):
        # The user is identified by their Username address
        return self.name
        
    def __str__(self):
        return str(self.email) if self.email else ''

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin

    @property
    def is_active(self):
        """Is the user active?"""
        return self.active

    objects=MyUserManager()
