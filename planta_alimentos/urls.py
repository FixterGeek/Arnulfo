# Importamos lo necesario para crear rutas
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
# importamos views
from .views import InsumoViewSet, ItemViewSet, FormulaViewSet

router = routers.DefaultRouter()

router.register('insumos', InsumoViewSet)
router.register('items', ItemViewSet)
router.register('formulas', FormulaViewSet)

app_name='planta_alimentos'

urlpatterns = [
    url('^', include(router.urls))
]