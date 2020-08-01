from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import TaskCreateViewSerializer, TaskListViewSerializer, TaskChangeViewSerializer
from .models import Tasks
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrReadOnly
User = get_user_model()


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateViewSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsAuthenticated,)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListViewSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsAuthenticated,)


class TaskChangeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskChangeViewSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)