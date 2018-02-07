from rest_framework import serializers
from .models import Animal, Lote, Corral, GastoAnimal, Peso



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

	def create(self, validated_data):
		print(validated_data)
		 
		lote = BasicLoteSerializer(data=validated_data.get('lote'))
		lote.is_valid()
		lote.save()
		animal =  Animal.objects.create(**validated_data)
		animal.lote = lote
		animal.save()

		return animal



	def update(self, instance, validated_data):
		print(validated_data)
		print(instance.lote)
		instance = validated_data
		return instance


class BasicPesoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Peso
		fields = '__all__'


class AlimentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = GastoAnimal
		fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):

	lote = BasicLoteSerializer(many=False, read_only=True)
	aliments = AlimentoSerializer(many=True, read_only=True)
	pesadas = BasicPesoSerializer(many=True, read_only=True)
	class Meta:
		model = Animal
		fields = '__all__'

	

	
class BasicAnimalSerializer(serializers.ModelSerializer):
	#aliments = AlimentoSerializer(many=True, read_only=True)
	#ote = serializers.SerializerMethodField()
	
	class Meta:
		model = Animal
		fields = '__all__'

	# def get_lote(self, obj):
	# 	print(obj.lote)
	# 	return str(obj.lote.name)


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




