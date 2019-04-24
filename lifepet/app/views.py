from django.contrib.auth import get_user_model
from rest_framework import viewsets, views

from . import Serializers


class UserView(viewsets.generics.CreateAPIView):
    serializer_class = Serializers.UserSerializer
    model = get_user_model()


class AdminUserView(viewsets.generics.CreateAPIView):
    serializer_class = Serializers.AdminUserSerializer
    model = get_user_model()
