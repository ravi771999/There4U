from django.db import models

from user_api import models as users_models

class Restaurant(models.Model):
    """
    This Restaurant model is going to store the information regarding the Restaurant such as:
    restaurant_name: to store the name of the restaurant
    first_address_line: to store the first address line of restaurant
    second_address_line: to store the second address line of restaurant
    delivery_status: to store the current status of restaurant ( open= True , close = False)
    """
    restaurant_name=models.CharField(max_length=50)
    first_address_line=models.TextField(max_length=100,null=True)
    second_address_line=models.TextField(max_length=100,null=True)
    delivery_status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)


class Food(models.Model):
    """
    This Food model is going to store the information regarding the Food such as:
    name: to store the name of the food item.
    """
    name = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)


class Ownership(models.Model):
    """
    This Ownership model is going to store the information regarding the Restaurant and Owner relationship:
    restaurant_id: to store the id of the restaurant
    user_id: to store the user_id of the owner
    """
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_id = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)


class Menu(models.Model):
    """
    This Menu model is going to store the information regarding the menu such as:
    name: to store the name of the particular menu
    """
    name = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)


class Restaurant_Menu(models.Model):
    """
    This Restaurant_Menu model is going to store the information regarding the Restaurant and their menu such as:
    restaurant_id: to store the id of the restaurant
    menu_id: to store the menu_id of the menu
    """
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)


class Menu_Food(models.Model):
    """
    This Menu_Food model is going to store the information regarding the Menu and Food Relationship such as:
    restaurant_menu_id: to store the id of the restaurant_menu table
    food_id: to store the food_id of the food item
    order_count: number of times this food item is ordered from this restaurant for this menu.
    cost: cost of this food item in this restaurant for this menu
    quantity_left: quantity left for this food item in this restaurant.
    """     
    restaurant_menu_id = models.ForeignKey(Restaurant_Menu, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    order_count=models.IntegerField(default=0)
    cost=models.IntegerField()
    quantity_left=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)


