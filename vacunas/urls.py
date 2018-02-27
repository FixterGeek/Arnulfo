# Importamos lo necesario para crear rutas
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
# importamos views
from .views import VacunaViewSet

router = routers.DefaultRouter()

router.register('vacunas', VacunaViewSet)

app_name='vacunas-urls'

urlpatterns = [
    url('^', include(router.urls))
]