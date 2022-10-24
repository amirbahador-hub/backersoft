import pytest

from tests.factories import (
        ProjectFactory,
        ProjectMemberFactory,
        TimeLogFactory,
        BaseUserFactory,
        )

@pytest.fixture
def project1():
    return ProjectFactory()


@pytest.fixture
def user1():
    return BaseUserFactory()


@pytest.fixture
def project_member1(project1, user1):
    return ProjectMemberFactory(project=project1, member=user1)


@pytest.fixture
def timelog1(project_member1):
    return TimeLogFactory(project_member=project_member1)

