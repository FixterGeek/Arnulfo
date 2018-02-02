"""adminArnu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from ganado import urls as ganadoUrls
from accounts import urls as authUrls
from egresos import urls as egresosUrls
from ingresos import urls as ingresosUrls
from planta_alimentos import urls as plantaUrls

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/ganado/', include(ganadoUrls, namespace='ganado-urls')),
    path('api/auth/', include(authUrls, namespace='auth-urls')),
    path('api/egresos/', include(egresosUrls, namespace='egresos-urls')),
    path('api/ingresos/', include(ingresosUrls, namespace='ingresos-urls')),
    path('api/planta_alimentos/', include(plantaUrls, namespace='planta_alimentos-urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
]
