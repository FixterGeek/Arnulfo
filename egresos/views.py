from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProviderSerializer, PurchaseSerializer
from .models import Provider, Purchase

#VIews for the API

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
