from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VacunaSerializer
from .models import Vacuna

#VIews for the API

class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer