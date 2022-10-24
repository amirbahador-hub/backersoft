from django.urls import path, include

urlpatterns = [
    path(
        'auth/', include(('authentication.urls', 'authentication'))
    ),
    path('users/', include(('users.urls', 'users'))),
    path('errors/', include(('errors.urls', 'errors'))),
    path('files/', include(('files.urls', 'files'))),
]
