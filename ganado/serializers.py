from rest_framework import serializers
from .models import Animal, Lote, Corral, GastoAnimal, Peso, Raza
from ingresos.serializers import CompanySerializer
from ingresos.models import Company


class RazaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Raza
		fields = '__all__'

class BasicLoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lote
		fields = '__all__'

class CorralSerializer(serializers.ModelSerializer):
	lotes = BasicLoteSerializer(many=False, read_only=True)
	class Meta:
		model = Corral
		fields = '__all__'

class BasicCorralSerializer(serializers.ModelSerializer):
	class Meta:
		model = Corral
		fields = '__all__'

class BasicPesoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Peso
		fields = '__all__'


class AlimentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = GastoAnimal
		fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
	empresa = CompanySerializer(many=False, read_only=True)
	empresa_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True, allow_null=True, required=False)
	raza = RazaSerializer(many=False, read_only=True)
	raza_id = serializers.PrimaryKeyRelatedField(queryset=Raza.objects.all(), write_only=True, allow_null=True, required=False)
	lote = BasicLoteSerializer(many=False, read_only=True)
	lote_id = serializers.PrimaryKeyRelatedField(queryset=Lote.objects.all(), write_only=True, allow_null=True, required=False)
	aliments = AlimentoSerializer(many=True, read_only=True)
	pesadas = BasicPesoSerializer(many=True, read_only=True)
	class Meta:
		model = Animal
		fields = '__all__'

	def create(self, validated_data):
		print(validated_data)
		try:
			lote = validated_data.pop('lote_id')	
		except:
			lote = None
		try:
			raza = validated_data.pop('raza_id')	
		except:
			raza = None
		try:
			empresa = validated_data.pop('empresa_id')
		except:
			empresa = None
			
		
		animal = Animal.objects.create(lote=lote, raza=raza, empresa=empresa, **validated_data)
		return animal

	
	
class BasicAnimalSerializer(serializers.ModelSerializer):
	#aliments = AlimentoSerializer(many=True, read_only=True)
	#ote = serializers.SerializerMethodField()
	aliments = AlimentoSerializer(many=True, read_only=True)
	pesadas = BasicPesoSerializer(many=True, read_only=True)
	class Meta:
		model = Animal
		fields = '__all__'


class PesoSerializer(serializers.ModelSerializer):
	animal = BasicAnimalSerializer(many=False, read_only=True)
	class Meta:
		model = Peso
		fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):

	corral = BasicCorralSerializer(many=False, read_only=True)
	animals = BasicAnimalSerializer(many=True, read_only=True)
	class Meta:
		model = Lote
		fields = '__all__'




