from rest_framework import serializers
from .models import Disposicion, Acreedor



# class DisposicionBasicSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Disposicion
# 		fields = '__all__'

class AcreedorSerializer(serializers.ModelSerializer):
	# disposiciones = DisposicionBasicSerializer(many=True, read_only=True)
	class Meta:
		model = Acreedor
		fields = '__all__'

class DisposicionSerializer(serializers.ModelSerializer):
	acreedor = AcreedorSerializer(many=False, read_only=True)
	acreedor_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Acreedor.objects.all(), write_only=True, source='acreedor', required=False)
	class Meta:
		model = Disposicion
		fields = '__all__'

	def create(self, validated_data):
		print(validated_data)
		# try:
		# 	acreedor = validated_data.pop('acreedor_id')
		# except:
		# 	acreedor = None

		d = Disposicion.objects.create( **validated_data)
		return d

