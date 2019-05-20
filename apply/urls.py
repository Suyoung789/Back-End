from django.urls import path
from . import views

urlpatterns = [
    path('adoption/<pk>', views.ApplyAdoptionListView.as_view()),
    path('care/<pk>', views.ApplyCareListView.as_view()),
    path('move/<pk>', views.ApplyMoveListView.as_view())
]