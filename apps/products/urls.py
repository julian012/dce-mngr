from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    show_available_products
)

router = DefaultRouter()

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'products/list', show_available_products, name='products-list'),

]