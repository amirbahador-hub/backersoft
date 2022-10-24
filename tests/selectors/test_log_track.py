import pytest

from core.selectors.time_log import log_list 


@pytest.mark.django_db
def test_log_list(project1, user1, project_member1, timelog1):
    filters = {
            "all_members":True,
            "project": project1.name,
            } 
    a = log_list(user=user1)[0]
    assert a == timelog1
