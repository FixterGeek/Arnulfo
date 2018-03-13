from django.shortcuts import render
from rest_framework import viewsets
from .models import Almacen, ItemAlmacen
from .serializers import AlmacenSerializer, ItemAlmacenSerializer


class AlmacenesViewSet(viewsets.ModelViewSet):
	queryset = Almacen.objects.all()
	serializer_class = AlmacenSerializer


class ItemAlmacenViewSet(viewsets.ModelViewSet):
	queryset = ItemAlmacen.objects.all()
	serializer_class = ItemAlmacenSerializer

