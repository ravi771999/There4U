from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from restaurant_api import models

# Create your views here.

@api_view(['GET'])
def testing(request): 
    return Response({"status":200 , "message":"how are you all"})

@api_view(['POST'])
def insert_data(request):
    data=request.data
    print(data)
    name=data["name"]
    email=data["email"]
    password=data["password"]
    city=data["city"]
    state=data["state"]
    zipcode=data["zipcode"]
    balance=data["balance"]
    phone=data["phone"]
    now = datetime.now()
    created_at=now
    updated_at=now
    obj=models.User(name=name, email=email,password=password, city=city, state= state, zipcode=zipcode,balance=balance,phone=phone,created_at=created_at,updated_at=updated_at)
    obj.save()   
    return Response({"status":"Your Information has been stored"})

{"name": "Raveet Kumar", "email": "kumarraveet52@gmail.com", "password": "admin", "city": "Fatehgarh", "state": "Uttar Pradesh", "zipcode": 209602, "balance": 1200, "phone": 9119628406}