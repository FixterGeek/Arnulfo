from rest_framework import serializers
from .models import Provider, Purchase
from ingresos.models import BusinessLine


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class BusinessLineEgresosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLine
        fields = '__all__'


class BasicPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    provider_egreso = ProviderSerializer(many=False, read_only=True)
    provider_egreso_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=True, many=False, allow_null=True, required=False,)
    business_egreso = BusinessLineEgresosSerializer(many=False, read_only=True)
    business_egreso_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True,
                                                          many=False, allow_null=True, required=False,)


    class Meta:
        model = Purchase
        fields = '__all__'

    def create(self, validated_data):
        try:
            provider_egreso = validated_data.pop('provider_egreso_id')
        except:
            provider_egreso = None
        try:
            business_egreso = validated_data.pop('business_egreso_id')
        except:
            business_egreso = None

        purchase = Purchase.objects.create(provider_egreso=provider_egreso, business_egreso=business_egreso, **validated_data)
        return purchase

class EditPurchaseSerializer(serializers.ModelSerializer):
    provider_egreso = ProviderSerializer(many=False, read_only=True)
    provider_egreso_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=True, many=False,
                                                     source='provider_egreso')
    business_egreso = BusinessLineEgresosSerializer(many=False, read_only=True)
    business_egreso_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True,
                                                          many=False, source='business_egreso')

    class Meta:
        model = Purchase
        fields = '__all__'



