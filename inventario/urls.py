from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ItemAlmacenViewSet, AlmacenesViewSet



router = routers.DefaultRouter()

router.register('items', ItemAlmacenViewSet)
router.register('almacenes', AlmacenesViewSet)


app_name='inventario'

urlpatterns=[
	url('^', include(router.urls))
]