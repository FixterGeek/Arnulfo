from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProviderSerializer
from .models import Provider

#VIews for the API

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
