from django.db import models
from restaurant_api.models import Restaurant,Food
from user_api.models import User


class Order(models.Model):
    """
    This Order model is going to store the information regarding the order such as:
    user_id: the person who placed this order
    restaurant_id: it will store the id of the restaurant in which the order has been placed.
    delivery_first_address: It will store the first line of delivery address
    delivery_second_address: It will store the second line of delivery address
    total_price: the total_price of the order
    order_status: tells the current status of order (like delivered == 1, on_the_way == 2, preparing == 3 )
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    delivery_first_address=models.CharField(max_length=100,null=True)
    delivery_second_address=models.CharField(max_length=100,null=True)
    total_price=models.IntegerField(null=True)
    order_status=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)


class Order_Detail(models.Model):
    """
    This Order_Detail model is going to store the information regarding the details of order such as:
    order_id: the order id of the order of which details is stored
    food_id: it will store the id of the food which is included in the order
    quantity: tells the quantity of food item, a user is buying
    total_price: what is the total price of this food_item (= quantity * food_id_price)
    """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)

