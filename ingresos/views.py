from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client

#VIews for the API

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer