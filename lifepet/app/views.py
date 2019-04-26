from django.contrib.auth import get_user_model
from rest_framework import viewsets, views

from . import serializers


class UserView(viewsets.generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    model = get_user_model()


class AdminUserView(viewsets.generics.CreateAPIView):
    serializer_class = serializers.AdminUserSerializer
    model = get_user_model()
