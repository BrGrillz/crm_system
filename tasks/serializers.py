from rest_framework import serializers
from .models import Tasks, Comments, STATUS_CHOISES
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class TaskCreateViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = 'name', 'description', 'due_date', 'file', 'responsible', 'observer'


class TaskListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TaskDetailViewSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Tasks
        fields = '__all__'


class StatusChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = 'status',


class TaskChangeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = 'name', 'description', 'due_date', 'status', 'file', 'responsible', 'observer'
