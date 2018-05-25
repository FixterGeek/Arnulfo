from rest_framework import serializers
from .models import Client, Sale, Company, BusinessLine, CuentaBanco
from inventario.serializers import AlmacenSerializer
from egresos.serializers import PurchaseSerializer
from egresos.models import Compras

class BasicCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = '__all__'


class BasicSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class BusinessLineBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLine
        fields = '__all__'

class CompanyBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class BusinessLineSerializer(serializers.ModelSerializer):
    almacenes = AlmacenSerializer(many=True, read_only=True)
    purchases = PurchaseSerializer(many=True, read_only=True)
    sales = BasicSaleSerializer(many=True, read_only=True)
    companies = CompanyBasicSerializer(many=True, read_only=True)
    compras = BasicCompraSerializer(many=True, read_only=True)
    class Meta:
        model = BusinessLine
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    line_comp = BusinessLineBasicSerializer(many=True, read_only=True)
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
    line_comp = BusinessLineBasicSerializer(many=True, read_only=True)
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




class CuentaBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBanco
        fields = '__all__'



class SaleSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False, read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=True, many=False, allow_null=True, required=False,)
    business_line = BusinessLineBasicSerializer(many=False, read_only=True)
    business_line_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=False, allow_null=True, required=False,)
    receivable = CuentaBasicSerializer(many=False, read_only=True)
    receivable_id = serializers.PrimaryKeyRelatedField(queryset=CuentaBanco.objects.all(), write_only=True, many=False, allow_null=True, required=False,)


    class Meta:
        model = Sale
        fields = '__all__'
    def create(self, validated_data):
        try:
            client = validated_data.pop('client_id')
        except:
            client = None
        try:
            business_line = validated_data.pop('business_line_id')
        except:
            business_line = None
        try:
            receivable = validated_data.pop('receivable_id')
        except:
            receivable = None


        client = Sale.objects.create(client=client, receivable=receivable, business_line=business_line, **validated_data)
        return client


class EditSaleSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False, read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=True, many=False, source='client')
    business_line = BusinessLineBasicSerializer(many=False, read_only=True)
    business_line_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True,
                                                          many=False, source='business_line')
    receivable = CuentaBasicSerializer(many=False, read_only=True)
    receivable_id = serializers.PrimaryKeyRelatedField(queryset=CuentaBanco.objects.all(), write_only=True, many=False, source='receivable')

    class Meta:
        model = Sale
        fields = '__all__'


class CuentaBancoSerializer(serializers.ModelSerializer):
    sales = SaleSerializer(many=True, read_only=True)
    class Meta:
        model = CuentaBanco
        fields = '__all__'



