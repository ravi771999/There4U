from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', testing),
    path('insertData',insert_data)
]