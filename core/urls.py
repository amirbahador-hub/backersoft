from django.urls import path
from .views import (
    TestCore,
)

app_name = "core"
urlpatterns = [
    path("test/", TestCore.as_view(), name="test"),
]
