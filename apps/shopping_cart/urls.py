from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    show_shopping_cart,
    delete_from_shopping_cart,
    add_product_shopping_cart
)

router = DefaultRouter()

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'shopping_cart/list', show_shopping_cart, name='shopping-cart-list'),
    path(r'shopping_cart/<int:product_id>/remove', delete_from_shopping_cart, name='shopping-cart-remove'),
    path(r'shopping_cart/add', add_product_shopping_cart, name='shopping-cart-add'),
]