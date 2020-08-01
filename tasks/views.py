from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import TaskViewSerializer, TaskViewListSerializer, TaskViewChangeSerializer
from .models import TasksView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrReadOnly
User = get_user_model()


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskViewSerializer
    queryset = TasksView.objects.all()
    permission_classes = (IsAuthenticated,)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskViewListSerializer
    queryset = TasksView.objects.all()
    permission_classes = (IsAuthenticated,)


class TaskChangeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskViewChangeSerializer
    queryset = TasksView.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)