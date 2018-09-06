from rest_framework import routers
from django.conf.urls import url
from django.urls import path, include
from .views import AcreedorViewSet, DisposicionViewSet

router = routers.DefaultRouter()
router.register('acreedores', AcreedorViewSet)
router.register('disposiciones', DisposicionViewSet)



app_name='creditos'

urlpatterns=[
	url('^', include(router.urls)),
	
	# url(r'^animalApi/$',AnimalAPI.as_view() )
]