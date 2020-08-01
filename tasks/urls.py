from django.urls import path
from .views import *


app_name = 'Task'
urlpatterns = [
    path('maketask/', TaskCreateView.as_view(), name='maketask'),
    path('alltasks/', TaskListView.as_view(), name='alltasks'),
    path('changetask/<int:pk>/', TaskChangeView.as_view(), name='changetask'),
]
