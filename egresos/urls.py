from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ProviderViewSet, PurchaseViewSet



router = routers.DefaultRouter()

router.register('proveedores', ProviderViewSet)
router.register('egresos', PurchaseViewSet)

app_name='egresos'

urlpatterns=[
	url('^', include(router.urls))
]