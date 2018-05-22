from rest_framework import serializers
from .models import Client, Sale, Company, BusinessLine, CuentaBanco
from inventario.serializers import AlmacenSerializer


class BusinessLineSerializer(serializers.ModelSerializer):
    almacenes = AlmacenSerializer(many=True, read_only=True)
    class Meta:
        model = BusinessLine
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    line_comp = BusinessLineSerializer(many=True, read_only=True)
    line_comp_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=True)
    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        blines = validated_data.pop('line_comp_id')
        company = Company.objects.create(**validated_data)
        for bl in blines:
            company.line_comp.add(bl)

        return company

class EditCompanySerializer(serializers.ModelSerializer):
    line_comp = BusinessLineSerializer(many=True, read_only=True)
    line_comp_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=True, source='line_comp')
    class Meta:
        model = Company
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     print('instance', instance.line_comp)
    #     print('vdata', validated_data)
    #     blines = validated_data.pop('line_comp_id')
    #     #blines  = filter(None, validated_data['line_comp_id'])
    #     instance = super(CompanySerializer, self).update(instance, validated_data)
    #     instance.line_comp = None
    #     for bl in blines:
    #         instance.line_comp.add(bl)
    #     instance.save()
        
    #     return instance



        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class BasicSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False, read_only=True)
    #receivable = CuentaBancoSerializer(many=False, read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'

class CuentaBancoSerializer(serializers.ModelSerializer):
    sales = SaleSerializer(many=True, read_only=True)
    class Meta:
        model = CuentaBanco
        fields = '__all__'
