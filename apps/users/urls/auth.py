from django.urls import path

from apps.users.views import login, logout

urlpatterns = [
    path('token/login', login, name='login'),
    path('token/logout', logout, name='logout')
]