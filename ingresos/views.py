from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer, SaleSerializer, BasicSaleSerializer
from .models import Client, Sale

#VIews for the API

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    #serializer_class = SaleSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return SaleSerializer
        if self.action == 'retrieve':
            return SaleSerializer
        return BasicSaleSerializer