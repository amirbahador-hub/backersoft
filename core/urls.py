from django.urls import path
from .apis import (
    TimeTrackApi,
)

app_name = "core"
urlpatterns = [
    path("time_tracker/", TimeTrackApi.as_view(), name="time_tracker"),
]
