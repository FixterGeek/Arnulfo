from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer, SaleSerializer, BasicSaleSerializer, CompanySerializer, BusinessLineSerializer, EditCompanySerializer
from .models import Client, Sale, Company, BusinessLine
from django.db.models import Q

#PAGINATION
from .pagination import ClientePagination, BlinePagination, CompanyPagination, IngresoPagination

#VIews for the API

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CompanyPagination

    def get_serializer_class(self):
        if self.action == 'update':
            return EditCompanySerializer
        if self.action == 'partial_update':
            return EditCompanySerializer
        return CompanySerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = super(CompanyViewSet, self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(company__icontains=query)
            ).distinct()

        return queryset_list

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientePagination

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = super(ClientViewSet, self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(client__icontains=query)
            ).distinct()

        return queryset_list



class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    #serializer_class = SaleSerializer
    pagination_class = IngresoPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return SaleSerializer
        if self.action == 'retrieve':
            return SaleSerializer
        return BasicSaleSerializer


class BusinessLineViewSet(viewsets.ModelViewSet):
    queryset = BusinessLine.objects.all()
    serializer_class = BusinessLineSerializer
    pagination_class = BlinePagination

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = super(BusinessLineViewSet, self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
            ).distinct()

        return queryset_list




    