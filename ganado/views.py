from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimalSerializer, CorralSerializer, LoteSerializer, AlimentoSerializer
from .models import Animal, Lote, Alimento, Corral


#VIews for the API

class AnimalViewSet(viewsets.ModelViewSet):
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer

class LoteViewSet(viewsets.ModelViewSet):
	queryset = Lote.objects.all()
	serializer_class = LoteSerializer

class CorralViewSet(viewsets.ModelViewSet):
	queryset = Corral.objects.all()
	serializer_class = CorralSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
	queryset = Alimento.objects.all()
	serializer_class = AlimentoSerializer
