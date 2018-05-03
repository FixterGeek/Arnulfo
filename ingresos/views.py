from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer, SaleSerializer, BasicSaleSerializer, CompanySerializer, BusinessLineSerializer, EditCompanySerializer
from .models import Client, Sale, Company, BusinessLine

#PAGINATION
from .pagination import ClientePagination

#VIews for the API

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return EditCompanySerializer
        if self.action == 'partial_update':
            return EditCompanySerializer
        return CompanySerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    #pagination_class = ClientePagination

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    #serializer_class = SaleSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return SaleSerializer
        if self.action == 'retrieve':
            return SaleSerializer
        return BasicSaleSerializer


class BusinessLineViewSet(viewsets.ModelViewSet):
    queryset = BusinessLine.objects.all()
    serializer_class = BusinessLineSerializer




    