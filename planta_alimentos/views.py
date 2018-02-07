from django.shortcuts import render
# Necesario para crear apis
from rest_framework import viewsets
from rest_framework.response import Response
# importamos serializers
from .serializers import BasicItemSerializer, BasicFormulaSerializer, BasicInsumoSerializer, FormulaSerializer, InsumoSerializer
# importamos los modelos
from .models import Item, Formula, Insumo
# importamos reglas para paginacion
from .pagination import PlantaAlimentosPagination
#
from django.db.models import Q
# Create your views here.

# Vistas

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    pagination_class = PlantaAlimentosPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return InsumoSerializer
        if self.action == 'retrieve':
            return InsumoSerializer
        return BasicInsumoSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        provider_query = self.request.GET.get("provider")
        queryset_list = super(InsumoViewSet, self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
            ).distinct()
        if provider_query:
            queryset_list = queryset_list.filter(provider=provider_query)
        return queryset_list


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = BasicItemSerializer


class FormulaViewSet(viewsets.ModelViewSet):
    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer
