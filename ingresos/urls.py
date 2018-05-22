from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet, SaleViewSet, CompanyViewSet, BusinessLineViewSet, CuentaBancoViewSet



router = routers.DefaultRouter()

router.register('clientes', ClientViewSet)
router.register('ingresos', SaleViewSet)
router.register('empresas', CompanyViewSet)
router.register('blines', BusinessLineViewSet)
router.register('cuentas', CuentaBancoViewSet)

app_name='ingresos'

urlpatterns=[
	url('^', include(router.urls))
]