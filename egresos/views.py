from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProviderSerializer, PurchaseSerializer, BasicPurchaseSerializer, EditPurchaseSerializer, ComprasSerializer, EditComprasSerializer
from .models import Provider, Purchase, Compras

#PAGINATION
from django.db.models import Q
from .pagination import ProveedorPagination, EgresosPagination, ComprasPagination

#VIews for the API

class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer
    pagination_class = ComprasPagination

    def get_serializer_class(self):
        if self.action == 'update':
            return EditComprasSerializer
        if self.action == 'partial_update':
            return EditComprasSerializer
        return ComprasSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = super(ComprasViewSet, self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(proveedor__provider__icontains=query)
            )

        return queryset_list

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    pagination_class = ProveedorPagination

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = super(ProviderViewSet, self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(provider__icontains=query)
            ).distinct()

        return queryset_list



class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    pagination_class = EgresosPagination

    def get_serializer_class(self):
        if self.action == 'update':
            return EditPurchaseSerializer
        if self.action == 'partial_update':
            return EditPurchaseSerializer
        return PurchaseSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = super(PurchaseViewSet, self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(provider_egreso__provider__icontains=query)
            )
        return queryset_list
