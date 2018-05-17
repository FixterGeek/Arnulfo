from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProviderSerializer, PurchaseSerializer, BasicPurchaseSerializer
from .models import Provider, Purchase

#PAGINATION
from django.db.models import Q
from .pagination import ProveedorPagination, EgresosPagination

#VIews for the API

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
    #serializer_class = PurchaseSerializer
    pagination_class = EgresosPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return PurchaseSerializer
        if self.action == 'retrieve':
            return PurchaseSerializer
        return BasicPurchaseSerializer

    # def get_queryset(self, *args, **kwargs):
    #     query = self.request.GET.get("q")
    #     queryset_list = super(PurchaseViewSet, self).get_queryset()
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(paid__icontains=query)
    #         ).distinct()
    #
    #     return queryset_list
