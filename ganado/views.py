from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimalSerializer, CorralSerializer, LoteSerializer, AlimentoSerializer, BasicAnimalSerializer, BasicLoteSerializer
from .models import Animal, Lote, GastoAnimal, Corral
from .pagination import AnimalPagination


#VIews for the API

class AnimalViewSet(viewsets.ModelViewSet):
	queryset = Animal.objects.all()
	#serializer_class = AnimalSerializer
	pagination_class = AnimalPagination

	def get_serializer_class(self):
		if self.action == 'list':
			return AnimalSerializer
		if self.action == 'retrieve':
			return AnimalSerializer
		return BasicAnimalSerializer 

class LoteViewSet(viewsets.ModelViewSet):
	queryset = Lote.objects.all()
	serializer_class = LoteSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return LoteSerializer
		if self.action == 'retrieve':
			return LotelSerializer
		return BasicLoteSerializer 

class CorralViewSet(viewsets.ModelViewSet):
	queryset = Corral.objects.all()
	serializer_class = CorralSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
	queryset = GastoAnimal.objects.all()
	serializer_class = AlimentoSerializer
