from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimalSerializer, CorralSerializer, LoteSerializer, AlimentoSerializer
from .models import Animal, Lote, GastoAnimal, Corral
from .pagination import AnimalPagination


#VIews for the API

class AnimalViewSet(viewsets.ModelViewSet):
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer
	pagination_class = AnimalPagination

class LoteViewSet(viewsets.ModelViewSet):
	queryset = Lote.objects.all()
	serializer_class = LoteSerializer

class CorralViewSet(viewsets.ModelViewSet):
	queryset = Corral.objects.all()
	serializer_class = CorralSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
	queryset = GastoAnimal.objects.all()
	serializer_class = AlimentoSerializer
