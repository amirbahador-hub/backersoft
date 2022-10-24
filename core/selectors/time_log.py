from django.db.models.query import QuerySet
from core.filters import ProjectFilter 
from core.models import Project, TimeLog, ProjectMember
from django.http import HttpRequest


def log_list(*, filters=None, request:HttpRequest) -> QuerySet[Project]:
    filters = filters or {}
    all_members = filters.get("all_members", True)

    qs = Project.objects.all()

    project = ProjectFilter(filters, qs).qs
    if all_members:
        project_member = ProjectMember.objects.filter(project__in=project)
    else:
        project_member = ProjectMember.objects.filter(project__in=project, member=request.user)
    return  TimeLog.objects.filter(project_member__in=project_member)
