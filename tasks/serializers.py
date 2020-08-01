from rest_framework import serializers
from .models import TasksView


class TaskViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksView
        fields = '__all__'


class TaskViewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksView
        fields = 'name', 'description', 'createdate', 'untiltime', 'author', 'recipient', 'status'


class TaskViewChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksView
        fields = 'name', 'description', 'untiltime', 'recipient', 'status'