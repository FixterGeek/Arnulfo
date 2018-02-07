# Importamos las librerías necesarias para crear apis
from rest_framework import serializers
# Importamos los modelos a utilizar
from .models import Item, Insumo, Formula
from egresos.serializers import ProviderSerializer



# Creamos los serializers
###################### Item ################################
class BasicItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


###################### Insumo ################################
class BasicInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'


class InsumoSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False, read_only=True)
    items = BasicItemSerializer(many=True, read_only=True)
    class Meta:
        model = Insumo
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    insumo = BasicInsumoSerializer(many=False, read_only=True)
    class Meta:
        model = Item
        fields = '__all__'


###################### Formula ################################
class BasicFormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = '__all__'


class FormulaSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Formula
        fields = '__all__'

