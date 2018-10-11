from datetime import date, timedelta
from monthdelta import monthdelta
import calendar
from rest_framework import serializers
from .models import Disposicion, Acreedor, Recibo
import decimal



class ReciboBasicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recibo
		fields = '__all__'

class AcreedorSerializer(serializers.ModelSerializer):
	# disposiciones = DisposicionBasicSerializer(many=True, read_only=True)
	class Meta:
		model = Acreedor
		fields = '__all__'

class DisposicionSerializer(serializers.ModelSerializer):
	recibos = ReciboBasicSerializer(many=True, read_only=True)
	acreedor = AcreedorSerializer(many=False, read_only=True)
	acreedor_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Acreedor.objects.all(), write_only=True, source='acreedor', required=False)
	class Meta:
		model = Disposicion
		fields = '__all__'

	def create(self, validated_data):
		print(validated_data)
		d = Disposicion.objects.create( **validated_data)
		plazo = validated_data.pop('plazo')
		monto = validated_data.pop('monto')
		p_capital = validated_data.pop('periodo_capital')
		p_interes = validated_data.pop('periodo_intereses')
		d_date = validated_data.pop('fecha_inicio')
		tasa = validated_data.pop('tasa')
		saldo_a = monto
		#generando los recibos
		#Recibo.objects.create(disposicion=d,fecha=d_date, capital=0, saldo=monto, intereses=0)
		for i in range(0,plazo+1):			
			pago=0
			saldo=0			
			intereses=0
			#la fucking fecha			
			fecha = date(d_date.year, d_date.month, d_date.day) + monthdelta(i)
			
			#capital			
			if p_capital=='mensual' and i!=0:
				pago = monto/plazo
				
			elif p_capital=='trimestral' and i%3==0 and i!=0:
				pago = monto/plazo*3
				
			elif p_capital=='semestral' and i%6==0 and i!=0:
				pago = monto/plazo*6
				
			elif p_capital=='anual' and i%12==0 and i!=0:
				pago = monto/plazo*12
				
			elif p_capital=='vencimiento' and i==plazo:
				pago = monto
			
			pago = decimal.Decimal(pago)
				
			#interes
			if p_interes=='mensual' and i!=0:
				intereses = saldo_a*(tasa/100)/12		
			elif p_interes=='vencimiento' and i==plazo:			
				intereses = (monto*(tasa/100)/12)*plazo


			intereses = decimal.Decimal(intereses)

			#saldo
			saldo = saldo_a-pago
			saldo_a = saldo
			
			saldo = decimal.Decimal(saldo)
			print(pago, intereses, saldo)
			Recibo.objects.create(disposicion=d,fecha=fecha, capital=pago, saldo=saldo, intereses=intereses)
		return d

