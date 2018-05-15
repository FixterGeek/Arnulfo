from django.shortcuts import render
from .models import Product, Category, SaleOrder, OrderItem
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer, OrderItemSerializer, SaleOrderSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	#pagination clas

class OrderItemViewSet(viewsets.ModelViewSet):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemSerializer

class SaleOrderViewSet(viewsets.ModelViewSet):
	queryset = SaleOrder.objects.all()
	serializer_class = SaleOrderSerializer





