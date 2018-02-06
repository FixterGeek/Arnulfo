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


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = BasicItemSerializer


class FormulaViewSet(viewsets.ModelViewSet):
    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer
