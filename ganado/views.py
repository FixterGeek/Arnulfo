from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimalSerializer
from .models import Animal


#VIews for the API

class AnimalViewSet(viewsets.ModelViewSet):
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer
