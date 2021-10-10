from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    balance=models.IntegerField()
    phone=models.BigIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)