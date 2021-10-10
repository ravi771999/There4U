from django.db import models
from restaurant_api.models import Restaurant,Food
from user_api.models import User

# Create your models here.

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    delivery_first_address=models.CharField(max_length=100)
    delivery_second_address=models.CharField(max_length=100)
    total_price=models.IntegerField()
    order_status=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Order_Detail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)