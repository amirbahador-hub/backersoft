import django_filters

from core.models import Project 


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ("members", "name", "status") 
