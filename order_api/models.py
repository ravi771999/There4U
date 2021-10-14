from django.db import models
from restaurant_api.models import Restaurant,Food
from user_api.models import User
# Create your models here.

"""
    This Order model is going to store the information regarding the order such as:
    user_id: the person who placed this order
    restaurant_id: it will store the id of the restaurant in which the order has been placed.
    delivery_first_address: It will store the first line of delivery address
    delivery_second_address: It will store the second line of delivery address
    total_price: the total_price of the order
    order_status: tells the current status of order (like delivered == 1, on_the_way == 2, preparing == 3 )
"""
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    delivery_first_address=models.CharField(max_length=100)
    delivery_second_address=models.CharField(max_length=100)
    total_price=models.IntegerField()
    order_status=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


"""
    This Order_Detail model is going to store the information regarding the details of order such as:
    order_id: the order id of the order of which details is stored
    food_id: it will store the id of the food which is included in the order
    quantity: tells the quantity of food item, a user is buying
    total_price: what is the total price of this food_item (= quantity * food_id_price)
"""
class Order_Detail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

