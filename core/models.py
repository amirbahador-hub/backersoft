from django.db import models
from django.utils import timezone

from common.models import BaseModel
from users.models import  BaseUser


class Project(BaseModel):
    class Status(models.TextChoices):
        FINISH     = "FINISH", "Finish"
        PENDING    = "PENDING", "Pending"
        PROCESSING = "PROCESSING", "Processing"

    status = models.CharField(
        max_length=255,
        db_index=True,
        choices=Status.choices,
        default=Status.PENDING
    )

    name = models.CharField(max_length=255, primary_key=True)
    members = models.ManyToManyField('users.BaseUser', through='ProjectMember', related_name='projects')

    def __str__(self):
        return f"{self.name}"


class ProjectMember(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='project_members',
        null=True,
        on_delete=models.CASCADE
    )
    member = models.ForeignKey(
        BaseUser,
        related_name='project_members',
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.project} - {self.member}"


class TimeLog(models.Model):
    project_member = models.ForeignKey(
        ProjectMember,
        null=True,
        on_delete=models.CASCADE
    )
    start_at = models.DateTimeField(default=timezone.now())
    finish_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.project_member} - from {self.start_at} to {self.finish_at}"

