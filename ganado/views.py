from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EditAnimalSerializer, AnimalSerializer, CorralSerializer, LoteSerializer, AlimentoSerializer, BasicAnimalSerializer, BasicLoteSerializer, PesoSerializer, BasicPesoSerializer, RazaSerializer, FacturaSerializer
from .models import Animal, Lote, GastoAnimal, Corral, Peso, Raza, Factura
from .pagination import AnimalPagination, LotePagination, FacturaPagination
from django.db.models import Q

class FacturaViewSet(viewsets.ModelViewSet):
	queryset = Factura.objects.all()
	serializer_class = FacturaSerializer
	pagination_class = FacturaPagination

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get("q")
		query_list = super(FacturaViewSet, self).get_queryset()
		if query:
			query_list = query_list.filter(
				Q(factura__icontains=query)
			).distinct()
		return query_list


#VIews for the API

# class AnimalAPI(APIView):

# 	def post(self, request):
# 		data = request.data
# 		print(data)
# 		animal = BasicAnimalSerializer(data=request.data)
# 		animal.is_valid()
# 		animal.save()
# 		instance = Animal.objects.get(id=animal.data['id'])
# 		serializer2 = AnimalSerializer(instance)
# 		serializer2.is_valid()
# 		return Response(serializer2.data)


class AnimalViewSet(viewsets.ModelViewSet):
	#queryset = Animal.objects.all().filter(status=True)
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer
	pagination_class = AnimalPagination

	def get_serializer_class(self):
	 	if self.action == 'update':
	 		return EditAnimalSerializer
	 	if self.action == 'partial_update':
	 		return EditAnimalSerializer
	 	return AnimalSerializer 

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get("q")
		lote_query = self.request.GET.get("lote")
		queryset_list = super(AnimalViewSet,self).get_queryset()
		if query:
			queryset_list = queryset_list.filter(
				Q(arete_rancho__icontains=query)|
				Q(arete_siniga__icontains=query)|
				Q(owner__icontains=query)
				).distinct()
		if lote_query:
			queryset_list = queryset_list.filter(Q(lote__name__iexact=lote_query))
		return queryset_list

class LoteViewSet(viewsets.ModelViewSet):
	queryset = Lote.objects.all()
	serializer_class = LoteSerializer
	#pagination_class = LotePagination

	def get_serializer_class(self):
		if self.action == 'list':
			return LoteSerializer
		if self.action == 'retrieve':
			return LoteSerializer
		return BasicLoteSerializer

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get("q")
		
		queryset_list = super(LoteViewSet,self).get_queryset()
		if query:
			queryset_list = queryset_list.filter(
				Q(name__icontains=query)
				).distinct()
	
		return queryset_list

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





class RazasViewSet(viewsets.ModelViewSet):
	queryset = Raza.objects.all()
	serializer_class = RazaSerializer




