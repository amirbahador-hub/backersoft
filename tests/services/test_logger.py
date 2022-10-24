import pytest

from core.services.time_log import logger
from core.models import TimeLog


@pytest.mark.django_db
def test_example(user1, project1, project_member1, timelog1):
    a = logger(project=project1.name, user=user1)
    assert isinstance(a, TimeLog)
