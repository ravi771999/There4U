from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from rest_framework.views import APIView
from user_api.models import User
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.

class UserView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self,request,format=None): 
        return Response({"status":200 , "message":"how are you all"})


    def post(self,request,**data):
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
        
        create_user(name=name, email=email, city=city, state= state, zipcode=zipcode,balance=balance,phone=phone,password=password)
        obj.save()   
        return Response({"status":"Your Information has been stored"})

    def register(self,request):
        details = request.data
        print(details)
        user = User.objects.create_user(details["username"], details["email"], details["password"])
        new_token=str(Token.objects.create(user=user))
        detailsobj = User.objects.create(user=user, phone=details["phone"])
        detailsobj.save()
        return Response({"token":new_token})


    def dashboard(self, request):
        return Response("logined user")

# {"username": "raveet","email":"r@gmail.com", "password": "jtg"}
#{"name": "Raveet Kumar", "email": "kumarraveet52@gmail.com", "password": "admin", "city": "Fatehgarh", "state": "Uttar Pradesh", "zipcode": 209602, "balance": 1200, "phone": 9119628406}
