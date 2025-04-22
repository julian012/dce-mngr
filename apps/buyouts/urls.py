from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    show_user_history
)

router = DefaultRouter()

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'history/list', show_user_history, name='history-list'),
]