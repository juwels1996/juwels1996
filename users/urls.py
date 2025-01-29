from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import UserViewSet,index
from .views import index, update_user

# router = DefaultRouter()
# router.register('users', UserViewSet)  # Register the UserViewSet under 'users/'

urlpatterns = [
    path('user/', index),  # Keep this path for fetching user data
    path('user/<int:user_id>/', update_user),  # New path for updating user data by user_id
]