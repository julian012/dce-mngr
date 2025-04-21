"""
URL configuration for dce_mngr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Api
    path('api/', include('apps.buyouts.urls')),
    path('api/', include('apps.payment_methods.urls')),
    path('api/', include('apps.products.urls')),
    path('api/', include('apps.shopping_cart.urls')),
    path('api/', include('apps.users.urls')),

    # Auth
    path('auth/', include('djoser.urls.base')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)