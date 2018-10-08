from rest_framework import routers
from django.conf.urls import url
from django.urls import path, include
from .views import AcreedorViewSet, DisposicionViewSet, ReciboViewSet

router = routers.DefaultRouter()
router.register('acreedores', AcreedorViewSet)
router.register('disposiciones', DisposicionViewSet)
router.register('recibos', ReciboViewSet)



app_name='creditos'

urlpatterns=[
	url('^', include(router.urls)),
		
]