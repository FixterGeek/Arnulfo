from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet



router = routers.DefaultRouter()

router.register('clientes', ClientViewSet)

app_name='ingresos'

urlpatterns=[
	url('^', include(router.urls))
]