from rest_framework import serializers
from .models import Client, Sale


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False, read_only=True);
    class Meta:
        model = Sale
        fields = '__all__'

class BasicSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
