from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import AnimalViewSet, LoteViewSet, CorralViewSet, AlimentoViewSet, PesoViewSet



router = routers.DefaultRouter()

router.register('animals', AnimalViewSet)
router.register('lotes', LoteViewSet)
router.register('corrales', CorralViewSet)
router.register('alimentos', AlimentoViewSet)
router.register('pesadas', PesoViewSet)

app_name='ganado'

urlpatterns=[
	url('^', include(router.urls))
]