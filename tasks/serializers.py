from rest_framework import serializers
from .models import Tasks


class TaskCreateViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TaskListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TaskChangeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = 'name', 'description', 'until_time', 'recipient', 'status', 'file'