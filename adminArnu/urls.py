from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from ganado import urls as ganadoUrls
from accounts import urls as authUrls
from egresos import urls as egresosUrls
from ingresos import urls as ingresosUrls
from planta_alimentos import urls as plantaUrls
from vacunas import urls as vacunasUrls
from inventario import urls as inventarioUrls
from catalogos import urls as catalogosUrls


class Home(TemplateView):
    template_name = 'index.html'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/ganado/', include(ganadoUrls, namespace='ganado-urls')),
    path('api/auth/', include(authUrls, namespace='auth-urls')),
    path('api/egresos/', include(egresosUrls, namespace='egresos-urls')),
    path('api/ingresos/', include(ingresosUrls, namespace='ingresos-urls')),
    path('api/planta_alimentos/', include(plantaUrls, namespace='planta_alimentos-urls')),
    path('api/vacunas/', include(vacunasUrls, namespace='vacunas-urls')),
    path('api/inventario/', include(inventarioUrls, namespace='inventario-urls')),
    path('api/catalogos/', include(catalogosUrls, namespace='catalogos-urls')),
   
    url(r'^api-auth/', include('rest_framework.urls')),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
]
