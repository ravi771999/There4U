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
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Restaurant(models.Model):
    restaurnat_name=models.CharField(max_length=50)
    first_address_line=models.TextField(max_length=100)
    second_address_line=models.TextField(max_length=100)
    delivery_status=models.IntegerField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    delivery_first_address=models.CharField(max_length=100)
    delivery_second_address=models.CharField(max_length=100)
    total_price=models.IntegerField()
    order_status=models.IntegerField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()


class Food(models.Model):
    name = models.CharField(max_length=100)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Order_Detail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Ownership(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()


class Menu(models.Model):
    name = models.CharField(max_length=50)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Restaurant_Menu(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()


class Menu_Food(models.Model):
    restaurant_menu_id = models.ForeignKey(Restaurant_Menu, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    order_count=models.IntegerField()
    cost=models.IntegerField()
    quantity_left=models.IntegerField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    