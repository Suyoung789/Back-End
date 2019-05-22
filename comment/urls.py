from django.urls import path
from . import views

urlpatterns = [
    path('adoption/<post_id>', views.CommentAdoptionListView.as_view()),
    path('care/<post_id>', views.CommentCareListView.as_view()),
    path('move/<post_id>', views.CommentMoveListView.as_view()),
    path('find/<post_id>', views.CommentFindListView.as_view()),
    path('report/<post_id>', views.CommentReportListView.as_view()),
    path('community/<post_id>', views.CommentCommunityListView.as_view())
]