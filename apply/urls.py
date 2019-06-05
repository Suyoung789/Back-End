from django.urls import path
from . import views

urlpatterns = [
    path('adoption/', views.ApplyAdoptionListView.as_view()),
    path('adoption/<post_id>', views.ApplyAdoptionCreateView.as_view()),
    path('adoption/<post_id>/<pk>', views.ApplyAdoptionRetrieveView.as_view()),
    path('care/', views.ApplyCareListView.as_view()),
    path('care/<post_id>', views.ApplyCareCreateView.as_view()),
    path('care/<post_id>/<pk>', views.ApplyCareRetrieveView.as_view()),
    path('move/', views.ApplyMoveListView.as_view()),
    path('move/<post_id>', views.ApplyMoveCreateView.as_view()),
    path('move/<post_id>', views.ApplyMoveRetrieveView.as_view())
]
