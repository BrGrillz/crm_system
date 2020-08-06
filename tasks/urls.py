from django.urls import path
from .views import *


urlpatterns = [
    path('maketask/', TaskCreateView.as_view(), name='maketask'),
    path('alltasks/', TaskListView.as_view(), name='alltasks'),
    path('changetask/<int:pk>/', TaskEditView.as_view(), name='changetask'),
    path('comments/', CommentCreateView.as_view(), name='comments'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('change/status/<int:pk>/', ChangeStatusView.as_view(), name='detail'),
]
