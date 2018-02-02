from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnimalSerializer, CorralSerializer, LoteSerializer, AlimentoSerializer, BasicAnimalSerializer, BasicLoteSerializer, PesoSerializer, BasicPesoSerializer
from .models import Animal, Lote, GastoAnimal, Corral, Peso
from .pagination import AnimalPagination
from django.db.models import Q


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
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer
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

	# def create(self, request, *args, **kwargs):
	# 	serializer = self.get_serializer(data=request.data)
	# 	serializer.is_valid(raise_exception=True)
	# 	self.perform_create(serializer)
	# 	headers = self.get_success_headers(serializer.data)
	# 	instance = Animal.objects.get(id=serializer.data['id'])
	# 	serializer2 = AnimalSerializer(instance, data=request.data)
	# 	serializer2.is_valid()
	# 	return Response(serializer2.data)

	# def update(self, request, *args, **kwargs):
	# 	#partial = kwargs.pop('partial', False)
	# 	instance = self.get_object()
	# 	data = request.data
	
	# 	serializer = self.get_serializer(instance, data=data)
	# 	serializer.is_valid(raise_exception=True)
	# 	self.perform_update(serializer)
	# 	seri2 = AnimalSerializer(instance, data=request.data, context={'request': request})
	# 	seri2.is_valid()
	# 	print(seri2.data)
	# 	return Response(seri2.data)

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
