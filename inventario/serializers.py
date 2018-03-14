from rest_framework import serializers
from .models import ItemAlmacen, Almacen
from planta_alimentos.serializers import BasicInsumoSerializer
from planta_alimentos.models import Insumo
from vacunas .serializers import VacunaSerializer
from vacunas.models import Vacuna

class BasicAlmacenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Almacen
		fields = '__all__'

class ItemAlmacenSerializer(serializers.ModelSerializer):
	insumo = BasicInsumoSerializer(many=False, read_only=True)
	insumo_id = serializers.PrimaryKeyRelatedField(queryset=Insumo.objects.all(), write_only=True, allow_null=True, required=False)
	almacen = BasicAlmacenSerializer(many=False, read_only=True)
	almacen_id = serializers.PrimaryKeyRelatedField(queryset=Almacen.objects.all(), write_only=True, allow_null=True, required=False)
	vacuna = VacunaSerializer(many=False, read_only=True)
	vacuna_id = serializers.PrimaryKeyRelatedField(queryset=Vacuna.objects.all(), write_only=True, allow_null=True, required=False)

	class Meta:
		model = ItemAlmacen
		fields = '__all__'

	def create(self, validated_data):
		#print(validated_data)
		try:
			insumo = validated_data.pop('insumo_id')	
		except:
			insumo = None
		try:
			almacen = validated_data.pop('almacen_id')	
		except:
			almacen = None
		try:
			vacuna = validated_data.pop('vacuna_id')	
		except:
			vacuna = None
		
			
		
		item = ItemAlmacen.objects.create(insumo=insumo, vacuna=vacuna, almacen=almacen, **validated_data)
		return item

class AlmacenSerializer(serializers.ModelSerializer):
	items = ItemAlmacenSerializer(many=True, read_only=True)
	class Meta:
		model = Almacen
		fields = '__all__'