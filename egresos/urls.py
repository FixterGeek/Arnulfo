from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ProviderViewSet, PurchaseViewSet, ComprasViewSet



router = routers.DefaultRouter()

router.register('proveedores', ProviderViewSet)
router.register('egresos', PurchaseViewSet)
router.register('compras', ComprasViewSet)

app_name='egresos'

urlpatterns=[
	url('^', include(router.urls))
]