from rest_framework import serializers
from .models import Provider, Purchase, Compras
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

class BasicCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = '__all__'


class ComprasSerializer(serializers.ModelSerializer):
    proveedor = ProviderSerializer(many=False, read_only=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=True,
                                                      many=False, allow_null=True, required=False, )
    linea_compras = BusinessLineEgresosSerializer(many=False, read_only=True)
    linea_compras_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True,
                                                          many=False, allow_null=True, required=False, )

    class Meta:
        model = Compras
        fields = '__all__'

    def create(self, validated_data):
        try:
            proveedor = validated_data.pop('proveedor_id')
        except:
            proveedor = None
        try:
            linea_compras = validated_data.pop('linea_compras_id')
        except:
            linea_compras = None

        compras = Compras.objects.create(proveedor=proveedor, linea_compras=linea_compras, **validated_data)
        return compras

class EditComprasSerializer(serializers.ModelSerializer):
    proveedor = ProviderSerializer(many=False, read_only=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=True, many=False,
                                                     source='proveedor')
    linea_compras = BusinessLineEgresosSerializer(many=False, read_only=True)
    linea_compras_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True,
                                                          many=False, source='linea_compras')
    class Meta:
        model = Compras
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    provider_egreso = ProviderSerializer(many=False, read_only=True)
    provider_egreso_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=True, many=False, allow_null=True, required=False,)
    business_egreso = BusinessLineEgresosSerializer(many=False, read_only=True)
    business_egreso_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True,
                                                          many=False, allow_null=True, required=False,)
    compra_egreso = BasicCompraSerializer(many=False, read_only=True)
    compra_egreso_id = serializers.PrimaryKeyRelatedField(queryset=Compras.objects.all(), write_only=True, many=False, allow_null=True, required=False)


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
        try:
            compra_egreso = validated_data.pop('compra_egreso_id')
        except:
            compra_egreso = None

        purchase = Purchase.objects.create(provider_egreso=provider_egreso, business_egreso=business_egreso, compra_egreso=compra_egreso, **validated_data)
        return purchase

class EditPurchaseSerializer(serializers.ModelSerializer):
    provider_egreso = ProviderSerializer(many=False, read_only=True)
    provider_egreso_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=True, many=False,
                                                     source='provider_egreso')
    business_egreso = BusinessLineEgresosSerializer(many=False, read_only=True)
    business_egreso_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True,
                                                          many=False, source='business_egreso')
    compra_egreso = BasicCompraSerializer(many=False, read_only=True)
    compra_egreso_id = serializers.PrimaryKeyRelatedField(queryset=Compras.objects.all(), write_only=True, many=False,
                                                          source='compra_egreso')

    class Meta:
        model = Purchase
        fields = '__all__'



