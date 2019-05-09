from django.urls import path
from . import views

urlpatterns = [
    path('adoption/', views.AdoptionListView.as_view()),
    path('adoption/<pk>', views.AdoptionRetrieveView.as_view()),
    path('care/', views.CareListView.as_view()),
    path('care/<pk>', views.CareRetrieveView.as_view()),
    path('move/', views.MoveListView.as_view()),
    path('move/<pk>', views.MoveRetrieveView.as_view()),
    path('report/', views.ReportListView.as_view()),
    path('report/<pk>', views.ReportRetrieveView.as_view()),
    path('find/', views.FindListView.as_view()),
    path('find/<pk>', views.FindRetrieveView.as_view()),
    path('community/', views.CommunityListView.as_view()),
    path('community/<pk>', views.CommunityRetrieveView.as_view())
]