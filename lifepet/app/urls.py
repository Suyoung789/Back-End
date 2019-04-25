from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views

urlpatterns= [
    path('login/', obtain_jwt_token),
    path('join/', views.UserView.as_view()),
    path('joinAdmin/', views.AdminUserView.as_view()),
    path('refresh/', refresh_jwt_token)
]