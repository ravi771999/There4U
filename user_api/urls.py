from django.urls import path
from rest_framework.routers import DefaultRouter

from user_api import views as user_views
from .auth import CustomAuthToken

router=DefaultRouter()
router.register(r'users',user_views.UserViewSet,basename='user')

urlpatterns=[
    path('api-token-auth/', CustomAuthToken.as_view())
]

urlpatterns+=router.urls
