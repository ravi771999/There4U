from django.urls import path
from rest_framework.routers import DefaultRouter

from user_api.views import UserViewSet
from .auth import CustomAuthToken

router=DefaultRouter()
router.register(r'users',UserViewSet,basename='user')

urlpatterns=[
    path('api-token-auth/', CustomAuthToken.as_view())
]

urlpatterns+=router.urls
