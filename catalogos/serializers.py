from .models import Producto,Unidades,CFDI,Pago,BankAccount,Almacen,Presupuesto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = '__all__'

class UnidadesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Unidades
		fields = '__all__'

class CFDISerializer(serializers.ModelSerializer):
	class Meta:
		model = CFDI
		fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pago
		fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = BankAccount
		fields = '__all__'

class AlmacenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Almacen
		fields = '__all__'

class PresupuestoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Presupuesto
		fields = '__all__'