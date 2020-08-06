from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    TaskCreateViewSerializer,
    TaskListViewSerializer,
    TaskChangeViewSerializer,
    CommentsSerializer,
    TaskDetailViewSerializer,
    StatusChangeSerializer
)
from .models import Tasks, Comments
from rest_framework.permissions import IsAuthenticated
from .utils import UserFilter

User = get_user_model()


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateViewSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListViewSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter

    # def list(self, request, *args, **kwargs):
    #     if request.user.is_superuser:
    #         tasks = Tasks.objects.all().distinct().order_by("-create_date")
    #     else:
    #         tasks = (
    #             Tasks.objects.filter(Q(author=request.user)
    #                                  | Q(responsible=request.user)
    #                                  | Q(observer=request.user))
    #             .distinct().order_by("-create_date")
    #         )
    #     page = self.paginate_queryset(tasks)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(tasks, many=True)
    #     return Response(serializer.data)


class TaskEditView(generics.UpdateAPIView):
    serializer_class = TaskChangeViewSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class TaskDetailView(generics.ListAPIView):
    serializer_class = TaskDetailViewSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class ChangeStatusView(generics.UpdateAPIView):
    serializer_class = StatusChangeSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsAuthenticated, )
