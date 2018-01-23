from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ProviderViewSet



router = routers.DefaultRouter()

router.register('proveedores', ProviderViewSet)

app_name='egresos'

urlpatterns=[
	url('^', include(router.urls))
]