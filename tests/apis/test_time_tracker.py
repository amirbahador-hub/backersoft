import pytest
from django.test import Client
from django.urls import reverse
import json


@pytest.mark.django_db
def test_time_track_post_api(user1, project1, project_member1, timelog1):
    client = Client()
    url_ = reverse("core:time_tracker")
    req_body = { "project":project1.name }
            
    response = client.post(url_, data=json.dumps(req_body), content_type='application/json')
    data = json.loads(response.content)

    assert response.status_code == 401
  
