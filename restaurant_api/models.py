from django.db import models
from user_api.models import User
# Create your models here.

"""
    This Restaurant model is going to store the information regarding the Restaurant such as:
    restaurant_name: to store the name of the restaurant
    first_address_line: to store the first address line of restaurant
    second_address_line: to store the second address line of restaurant
    delivery_status: to store the current status of restaurant ( open= True , close = False)
"""

class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=50)
    first_address_line=models.TextField(max_length=100)
    second_address_line=models.TextField(max_length=100)
    delivery_status=models.BooleanField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

"""
    This Food model is going to store the information regarding the Food such as:
    name: to store the name of the food item.
"""
class Food(models.Model):
    name = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

"""
    This Ownership model is going to store the information regarding the Restaurant and Owner relationship:
    restaurant_id: to store the id of the restaurant
    user_id: to store the user_id of the owner
"""
class Ownership(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

"""
    This Menu model is going to store the information regarding the menu such as:
    name: to store the name of the particular menu
"""
class Menu(models.Model):
    name = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

"""
    This Restaurant_Menu model is going to store the information regarding the Restaurant and their menu such as:
    restaurant_id: to store the id of the restaurant
    menu_id: to store the menu_id of the menu
"""
class Restaurant_Menu(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

"""
    This Menu_Food model is going to store the information regarding the Menu and Food Relationship such as:
    restaurant_menu_id: to store the id of the restaurant_menu table
    food_id: to store the food_id of the food item
    order_count: number of times this food item is ordered from this restaurant for this menu.
    cost: cost of this food item in this restaurant for this menu
    quantity_left: quantity left for this food item in this restaurant.
"""
class Menu_Food(models.Model):
    restaurant_menu_id = models.ForeignKey(Restaurant_Menu, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    order_count=models.IntegerField()
    cost=models.IntegerField()
    quantity_left=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
