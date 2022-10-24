from django.db.models.query import QuerySet
from core.filters import ProjectFilter 
from core.models import Project, TimeLog, ProjectMember


def log_list(*, filters=None) -> QuerySet[Project]:
    filters = filters or {}

    qs = Project.objects.all()

    project = ProjectFilter(filters, qs).qs
    project_member = ProjectMember.objects.filter(project__in=project)
    return  TimeLog.objects.filter(project_member__in=project_member)
