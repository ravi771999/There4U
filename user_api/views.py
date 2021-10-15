from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import viewsets

from user_api.models import User
from user_api.serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if pk is not None:
            queryset = User.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({"Invalid primary key given"})

    def create(self, request):
        user=request.data
        serializer=UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Unable to create the user right now.."})
        
    def destroy(self, request, pk=None):
        if pk is not None:
            user=User.objects.get(pk=pk)
            user.delete()
            return Response({"User successfully deleted"})
        return Response({"Invalid Primary Key given"})


    def update(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response({"Unable to update the user right now.."})

    def partial_update(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Unable to update the user right now.."})



#{"username": "raveet","email":"r@gmail.com", "password": "jtg"}
#{"name": "Raveet Kumar", "email": "kumarraveet52@gmail.com", "password": "admin", "city": "Fatehgarh", "state": "Uttar Pradesh", "zipcode": 209602, "balance": 1200, "phone": 9119628406}

