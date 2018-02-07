from rest_framework import serializers
from .models import Provider, Purchase


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class BasicPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False, read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'


