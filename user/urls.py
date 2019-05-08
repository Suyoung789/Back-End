from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('join/', views.UserView.as_view()),
    path('verify/', verify_jwt_token)
]

