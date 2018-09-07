from django.shortcuts import render
from rest_framework import viewsets
from .models import Acreedor, Disposicion
from .serializers import AcreedorSerializer, DisposicionSerializer


class AcreedorViewSet(viewsets.ModelViewSet):
	queryset = Acreedor.objects.all()
	serializer_class = AcreedorSerializer

class DisposicionViewSet(viewsets.ModelViewSet):
	queryset = Disposicion.objects.all()
	serializer_class = DisposicionSerializer
