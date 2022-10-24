from django.urls import path
from .apis import (
    TestCore,
)

app_name = "core"
urlpatterns = [
    path("test/", TestCore.as_view(), name="test"),
]
