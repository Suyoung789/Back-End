from django.urls import path
from . import views

urlpatterns = [
    path('adoption/', views.AdoptionListView.as_view()),
    path('adoption/<pk>', views.AdoptionRetrieveView.as_view()),
    path('care/', views.CareListView.as_view()),
    path('care/<pk>', views.CareRetrieveView.as_view())
]