from django.shortcuts import render
from .models import Producto,Unidades,CFDI,Pago,BankAccount,Almacen,Presupuesto
from rest_framework import viewsets
from .serializers import ProductoSerializer,UnidadesSerializer,CFDISerializer,PagoSerializer,BankAccountSerializer,AlmacenSerializer,PresupuestoSerializer
# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer


class UnidadesViewSet(viewsets.ModelViewSet):
	queryset = Unidades.objects.all()
	serializer_class = UnidadesSerializer


class CFDIViewSet(viewsets.ModelViewSet):
	queryset = CFDI.objects.all()
	serializer_class = CFDISerializer


class PagoViewSet(viewsets.ModelViewSet):
	queryset = Pago.objects.all()
	serializer_class = PagoSerializer


class BankAccountViewSet(viewsets.ModelViewSet):
	queryset = BankAccount.objects.all()
	serializer_class = BankAccountSerializer


class AlmacenViewSet(viewsets.ModelViewSet):
	queryset = Almacen.objects.all()
	serializer_class = AlmacenSerializer


class PresupuestoViewSet(viewsets.ModelViewSet):
	queryset = Presupuesto.objects.all()
	serializer_class = PresupuestoSerializer






