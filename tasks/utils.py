from django_filters import rest_framework as filters
from .models import Tasks


class UserFilter(filters.FilterSet):
    class Meta:
        model = Tasks
        fields = ['author', 'responsible', 'observer']
