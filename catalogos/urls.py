from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet, UnidadesViewSet, CFDIViewSet, PagoViewSet, BankAccountViewSet, AlmacenViewSet, PresupuestoViewSet

app_name='catalogos'


router = routers.DefaultRouter()
router.register('products', ProductoViewSet)
router.register('unidades', UnidadesViewSet)
router.register('cfdis', CFDIViewSet)
router.register('pagos', PagoViewSet)
router.register('banks', BankAccountViewSet)
router.register('almacenes', AlmacenViewSet)
router.register('presupuestos', PresupuestoViewSet)


urlpatterns=[
	url('^', include(router.urls))
]