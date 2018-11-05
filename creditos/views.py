from django.shortcuts import render
from rest_framework import viewsets
from .models import Acreedor, Disposicion, Recibo
from .serializers import AcreedorSerializer, DisposicionSerializer, ReciboBasicSerializer, ReciboSerializer
from datetime import datetime, timedelta

class AcreedorViewSet(viewsets.ModelViewSet):
	queryset = Acreedor.objects.all()
	serializer_class = AcreedorSerializer

class DisposicionViewSet(viewsets.ModelViewSet):
	queryset = Disposicion.objects.all()
	serializer_class = DisposicionSerializer

class ReciboViewSet(viewsets.ModelViewSet):	
	queryset= Recibo.objects.all()
	serializer_class = ReciboBasicSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return ReciboSerializer
		if self.action == 'retrieve':
			return ReciboSerializer
		return ReciboBasicSerializer  

	def get_queryset(self):
		corte = datetime.now() + timedelta(30)
		queryset_list = super(ReciboViewSet, self).get_queryset()
		if self.action == 'list':
			return queryset_list.filter(paid=False, fecha__lt=corte)
		return queryset_list



