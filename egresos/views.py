from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProviderSerializer, PurchaseSerializer, BasicPurchaseSerializer
from .models import Provider, Purchase

#VIews for the API

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    #serializer_class = PurchaseSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PurchaseSerializer
        if self.action == 'retrieve':
            return PurchaseSerializer
        return BasicPurchaseSerializer
