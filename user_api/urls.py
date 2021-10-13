from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', UserView.as_view(),name="testing"),
    path('insertData/',UserView.as_view(),name="insert_data"),
    path('register/',UserView.as_view(),name="register"),
    path('dashboard/',UserView.as_view(),name="dashboard")
]