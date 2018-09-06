from .models import Producto,Unidades,CFDI,Pago,BankAccount,Almacen,Presupuesto
from rest_framework import serializers
from ingresos.models import BusinessLine

class BLSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusinessLine
		fields = ['id', 'name']


class ProductoSerializer(serializers.ModelSerializer):
	bl = BLSerializer(many=False, read_only=True)
	bl_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=False, source='bl')
	
	class Meta:
		model = Producto
		fields = '__all__'

	def create(self, validated_data):
		print(validated_data)
		bl = validated_data.pop('bl')

		obj = Producto.objects.create(bl=bl, **validated_data)
		return obj



class UnidadesSerializer(serializers.ModelSerializer):
	bl = BLSerializer(many=False, read_only=True)
	bl_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=False, source='bl')
	class Meta:
		model = Unidades
		fields = '__all__'

	def create(self, validated_data):
		bl = validated_data.pop('bl')

		obj = Unidades.objects.create(bl=bl, **validated_data)
		return obj



class CFDISerializer(serializers.ModelSerializer):
	bl = BLSerializer(many=False, read_only=True)
	bl_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=False, source='bl')
	class Meta:
		model = CFDI
		fields = '__all__'

	def create(self, validated_data):
		bl = validated_data.pop('bl')

		obj = CFDI.objects.create(bl=bl, **validated_data)
		return obj



class PagoSerializer(serializers.ModelSerializer):
	bl = BLSerializer(many=False, read_only=True)
	bl_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=False, source='bl')
	class Meta:
		model = Pago
		fields = '__all__'

	def create(self, validated_data):
		bl = validated_data.pop('bl')

		obj = Pago.objects.create(bl=bl, **validated_data)
		return obj



class BankAccountSerializer(serializers.ModelSerializer):
	bl = BLSerializer(many=False, read_only=True)
	bl_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=False, source='bl')
	class Meta:
		model = BankAccount
		fields = '__all__'

	def create(self, validated_data):
		bl = validated_data.pop('bl')

		obj = BankAccount.objects.create(bl=bl, **validated_data)
		return obj



class AlmacenSerializer(serializers.ModelSerializer):
	bl = BLSerializer(many=False, read_only=True)
	bl_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=False, source='bl')
	class Meta:
		model = Almacen
		fields = '__all__'

	def create(self, validated_data):
		bl = validated_data.pop('bl')

		obj = Almacen.objects.create(bl=bl, **validated_data)
		return obj



class PresupuestoSerializer(serializers.ModelSerializer):
	bl = BLSerializer(many=False, read_only=True)
	bl_id = serializers.PrimaryKeyRelatedField(queryset=BusinessLine.objects.all(), write_only=True, many=False, source='bl')
	class Meta:
		model = Presupuesto
		fields = '__all__'

	def create(self, validated_data):
		bl = validated_data.pop('bl')

		obj = Presupuesto.objects.create(bl=bl, **validated_data)
		return obj

