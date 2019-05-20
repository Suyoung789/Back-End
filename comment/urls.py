from django.urls import path
from . import views

urlpatterns = [
    path('adoption/<pk>', views.CommentAdoptionListView.as_view()),
    path('care/<pk>', views.CommentCareListView.as_view()),
    path('move/<pk>', views.CommentMoveListView.as_view()),
    path('find/<pk>', views.CommentFindListView.as_view()),
    path('report/<pk>', views.CommentReportListView.as_view()),
    path('community/<pk>', views.CommentCommunityListView.as_view())
]