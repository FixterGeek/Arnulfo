from django.shortcuts import render
from rest_framework import viewsets
from .models import Acreedor, Disposicion, Recibo
from .serializers import AcreedorSerializer, DisposicionSerializer, ReciboBasicSerializer


class AcreedorViewSet(viewsets.ModelViewSet):
	queryset = Acreedor.objects.all()
	serializer_class = AcreedorSerializer

class DisposicionViewSet(viewsets.ModelViewSet):
	queryset = Disposicion.objects.all()
	serializer_class = DisposicionSerializer

class ReciboViewSet(viewsets.ModelViewSet):
	queryset= Recibo.objects.all()
	serializer_class = ReciboBasicSerializer 
