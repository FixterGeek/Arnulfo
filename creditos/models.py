from django.db import models

class Acreedor(models.Model):
	banco = models.CharField(max_length=100)
	saldo = models.DecimalField(decimal_places=2, max_digits=15)
	credito = models.IntegerField()

	def __unicode__(self):
		return self.banco


class Disposicion(models.Model):
	OPTIONS = (('revolvente', 'revolvente'),
				('simple', 'simple'))
	INTERESES = (('mensual', 'mensual'),
				('vencimiento', 'vencimiento'))
	CAPITAL = (('mensual', 'mensual'),
				('trimestral', 'trimestral'),
				('semestral', 'semestral'),
				('anual', 'anual'),
				('vencimiento', 'vencimiento'))
	acreedor = models.ForeignKey(Acreedor, related_name="disposiciones", on_delete=models.CASCADE)
	paid = models.BooleanField(default=False)
	tipo_credito = models.CharField(max_length=100, choices=OPTIONS)
	monto = models.DecimalField(decimal_places=2, max_digits=15)
	plazo = models.IntegerField()
	fecha_inicio = models.DateTimeField(auto_now_add=False, db_index=True)
	fecha_vencimiento = models.DateTimeField(auto_now_add=False, db_index=True)
	tasa = models.DecimalField(decimal_places=2, max_digits=5)
	gracia = models.DecimalField(decimal_places=2, max_digits=5)
	periodo_intereses = models.CharField(max_length=100, choices=INTERESES)
	periodo_capital = models.CharField(max_length=100, choices=CAPITAL)
	numero = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.id

class Recibo(models.Model):

	paid = models.BooleanField(default=False)
	disposicion = models.ForeignKey(Disposicion, related_name="recibos", on_delete=models.CASCADE)
	capital = models.DecimalField(max_digits=10, decimal_places=2)
	intereses = models.DecimalField(max_digits=10, decimal_places=2)
	saldo = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateField(auto_now_add=False, db_index=True)

	def __unicode__(self):
		return self.id

	class Meta:
		ordering = ['id']
	
	
		


