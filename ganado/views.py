from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimalSerializer, CorralSerializer, LoteSerializer, AlimentoSerializer, BasicAnimalSerializer, BasicLoteSerializer, PesoSerializer, BasicPesoSerializer
from .models import Animal, Lote, GastoAnimal, Corral, Peso
from .pagination import AnimalPagination
from django.db.models import Q


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

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get("q")
		lote_query = self.request.GET.get("lote")
		queryset_list = super(AnimalViewSet,self).get_queryset()
		if query:
			queryset_list = queryset_list.filter(
				Q(arete_rancho__icontains=query)|
				Q(arete_siniga__icontains=query)
				).distinct()
		if lote_query:
			queryset_list = queryset_list.filter(lote=lote_query)
		return queryset_list



class LoteViewSet(viewsets.ModelViewSet):
	queryset = Lote.objects.all()
	#serializer_class = LoteSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return LoteSerializer
		if self.action == 'retrieve':
			return LoteSerializer
		return BasicLoteSerializer 

class CorralViewSet(viewsets.ModelViewSet):
	queryset = Corral.objects.all()
	serializer_class = CorralSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
	queryset = GastoAnimal.objects.all()
	serializer_class = AlimentoSerializer

class PesoViewSet(viewsets.ModelViewSet):
	queryset = Peso.objects.all()
	#serializer_class = PesoSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return PesoSerializer
		if self.action == 'retrieve':
			return PesoSerializer
		return BasicPesoSerializer 
