from rest_framework import serializers
from .models import Animal, Lote, Corral, GastoAnimal, Peso, Raza, Factura, SaleNote, FierroO, FierroN
from ingresos.serializers import CompanySerializer
from ingresos.models import Company, Client

class FierroOSerializer(serializers.ModelSerializer):
	class Meta:
		model = FierroO
		fields = '__all__'

class FierroNSerializer(serializers.ModelSerializer):
	class Meta:
		model = FierroN
		fields = '__all__'


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

class BasicFacturaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Factura
		fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
	empresa = CompanySerializer(many=False, read_only=True)
	empresa_id = serializers.PrimaryKeyRelatedField(
		queryset=Company.objects.all(), 
		write_only=True, 
		allow_null=True, 
		required=False)
	raza = RazaSerializer(many=False, read_only=True)
	raza_id = serializers.PrimaryKeyRelatedField(queryset=Raza.objects.all(), write_only=True, allow_null=True, required=False)
	lote = BasicLoteSerializer(many=False, read_only=True)
	lote_id = serializers.PrimaryKeyRelatedField(queryset=Lote.objects.all(), write_only=True, allow_null=True, required=False)
	aliments = AlimentoSerializer(many=True, read_only=True)
	pesadas = BasicPesoSerializer(many=True, read_only=True)
	ref_factura_original = BasicFacturaSerializer(many=False, read_only=True)
	ref_factura_original_id = serializers.PrimaryKeyRelatedField(queryset=Factura.objects.all(), write_only=True, allow_null=True, required=False)
	fierroO = FierroOSerializer(many=False, read_only=True)
	fierroO_id = serializers.PrimaryKeyRelatedField(queryset=FierroO.objects.all(), write_only=True, allow_null=True, required=False)
	fierroN = FierroNSerializer(many=False, read_only=True)
	fierroN_id = serializers.PrimaryKeyRelatedField(queryset=FierroN.objects.all(), write_only=True, allow_null=True, required=False)
	class Meta:
		model = Animal
		fields = '__all__'

	def create(self, validated_data):
		#print(validated_data)
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
		try:
			ref_factura_original = validated_data.pop('ref_factura_original_id')
		except:
			ref_factura_original = None
		try:
			fierroO = validated_data.pop('fierroO_id')
		except:
			fierroO = None
		try:
			fierroN = validated_data.pop('fierroN_id')
		except:
			fierroN = None


			
		
		animal = Animal.objects.create(lote=lote, raza=raza, empresa=empresa, ref_factura_original=ref_factura_original,fierroO=fierroO, fierroN=fierroN, **validated_data)
		return animal

class EditAnimalSerializer(serializers.ModelSerializer):
	empresa = CompanySerializer(many=False, read_only=True)
	empresa_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True, allow_null=True, required=False, source='empresa', many=False)
	raza = RazaSerializer(many=False, read_only=True)
	raza_id = serializers.PrimaryKeyRelatedField(queryset=Raza.objects.all(), write_only=True, allow_null=True, required=False, source='raza')
	lote = BasicLoteSerializer(many=False, read_only=True, allow_null=True, required=False)
	lote_id = serializers.PrimaryKeyRelatedField(queryset=Lote.objects.all(), write_only=True, allow_null=True, required=False, source='lote')
	aliments = AlimentoSerializer(many=True, read_only=True)
	pesadas = BasicPesoSerializer(many=True, read_only=True)
	ref_factura_original = BasicFacturaSerializer(many=False, read_only=True)
	ref_factura_original_id = serializers.PrimaryKeyRelatedField(queryset=Factura.objects.all(), write_only=True, allow_null=True, required=False, source="ref_factura_original")
	fierroO = FierroOSerializer(many=False, read_only=True)
	fierroO_id = serializers.PrimaryKeyRelatedField(queryset=FierroO.objects.all(), write_only=True, allow_null=True, required=False, source="fierroO")
	fierroN = FierroNSerializer(many=False, read_only=True)
	fierroN_id = serializers.PrimaryKeyRelatedField(queryset=FierroN.objects.all(), write_only=True, allow_null=True, required=False, source="fierroN")

	class Meta:
		model = Animal
		fields = '__all__'

	
	
class BasicAnimalSerializer(serializers.ModelSerializer):
	#aliments = AlimentoSerializer(many=True, read_only=True)
	#ote = serializers.SerializerMethodField()
	lote = BasicLoteSerializer(many=False, read_only=True, allow_null=True)
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

class FacturaSerializer(serializers.ModelSerializer):
	animals = AnimalSerializer(many=True, read_only=True)
	class Meta:
		model = Factura
		fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Client
		fields = '__all__'

class SaleNoteSerializer(serializers.ModelSerializer):
	animals = AnimalSerializer(many=True, read_only=True)
	animals_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), write_only=True, many=True)
	client = ClientSerializer(many=False, read_only=True)
	client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=True, many=False)
	
	class Meta:
		model = SaleNote
		fields = '__all__'
		
	def create(self, validated_data):
		#print(validated_data)
		try:
			client = validated_data.pop('client_id')
		except:
			client = None
		animals = validated_data.pop('animals_id')
		sale_note = SaleNote.objects.create(client=client, **validated_data)
		for a in animals:
			sale_note.animals.add(a)
			print('added')
		return sale_note



