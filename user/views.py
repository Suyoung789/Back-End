from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

from . import serializers
from .models import User


@permission_classes((AllowAny, ))
class UserView(viewsets.generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    model = get_user_model()


@permission_classes((AllowAny, ))
class AdminUserView(viewsets.generics.CreateAPIView):
    serializer_class = serializers.AdminUserSerializer
    model = get_user_model()


class AdminJWT(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        username = request.data.get('username')
        user = User.objects.get(username=username)
        if not user.isAdmin:
            return Response({'message': 'Fordidden'}, 403)
        return response
