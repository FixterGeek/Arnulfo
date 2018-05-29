from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import FacturaViewSet, AnimalViewSet, LoteViewSet, CorralViewSet, AlimentoViewSet, PesoViewSet, RazasViewSet, ResumenView #AnimalAPI



router = routers.DefaultRouter()

router.register('animals', AnimalViewSet)
router.register('lotes', LoteViewSet)
router.register('corrales', CorralViewSet)
router.register('alimentos', AlimentoViewSet)
router.register('pesadas', PesoViewSet)
router.register('razas', RazasViewSet)
router.register('facturas', FacturaViewSet)

app_name='ganado'

urlpatterns=[
	url('^', include(router.urls)),
	url('resumen/', ResumenView.as_view())
	# url(r'^animalApi/$',AnimalAPI.as_view() )
]