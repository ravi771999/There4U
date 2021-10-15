from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

#ADD YOUR URL HERE
router=DefaultRouter()
router.register(r'users',UserViewSet,basename='user')

urlpatterns=router.urls
