import factory

from tests.utils import faker
from core.models import (
        TimeLog,
        Project,
        ProjectMember,
)
from users.models import  BaseUser
from django.utils import timezone
from datetime import datetime, timedelta


class BaseUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseUser

    email = factory.LazyAttribute(lambda _: "{faker.unique.company()@faker.domain_name()}")
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')

class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project 

    name = factory.LazyAttribute(lambda _: f'backersoft')


class ProjectMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectMember

    project  = factory.SubFactory(ProjectFactory)
    member   = factory.SubFactory(BaseUserFactory)


class TimeLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TimeLog

    start_at       = factory.LazyAttribute(lambda _: f'{timezone.now()}')
    finish_at      = factory.LazyAttribute(lambda _: f'{timezone.now() + timedelta(days=1)}')
    project_member = factory.SubFactory(ProjectMemberFactory)


