from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from . import serializers


@permission_classes((AllowAny, ))
class UserView(viewsets.generics.CreateAPIView):
    serializer_class = serializers.UserSerializers
    model = get_user_model()


# class AdminUserView(viewsets.generics.CreateAPIView):
#     serializer_class = serializers.AdminUserSerializers
#     model = get_user_model()
