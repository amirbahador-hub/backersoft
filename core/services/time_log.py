from django.http import HttpRequest
from django.utils import timezone

from core.models import Project, ProjectMember, TimeLog
from users.models import BaseUser
from django.db import transaction


@transaction.atomic
def logger(*, user:BaseUser, project:str) -> TimeLog:
    project, _ = Project.objects.get_or_create(name=project)
    project_member, _ = ProjectMember.objects.get_or_create(project=project, member=user)
    time_log = TimeLog.objects.filter(finish_at__isnull=True, project_member=project_member).first() 

    if  time_log: # stop timelog
        time_log.finish_at = timezone.now()
        time_log.save()
        return time_log
    return TimeLog.objects.create(project_member=project_member) # first timelog or start another timelog
