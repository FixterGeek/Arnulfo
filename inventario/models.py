from django.db import models
from ingresos.models import BusinessLine
from planta_alimentos.models import Insumo
from vacunas.models import Vacuna

class Almacen(models.Model):
	name = models.CharField(max_length=100)
	bline = models.ForeignKey(BusinessLine, related_name='almacenes',blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.name

class ItemAlmacen(models.Model):
	
	almacen = models.ForeignKey(Almacen, related_name='items', blank=True, null=True, on_delete=models.SET_NULL)
	costo_u = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	unity = models.CharField(max_length=100, blank=True, null=True)
	product_type = models.CharField(max_length=100, blank=True, null=True)
	insumo = models.ForeignKey(Insumo, related_name='items_almacen', blank=True, null=True, on_delete=models.SET_NULL)
	vacuna = models.ForeignKey(Vacuna, related_name='items_almacen', blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return 'item {} de almacen {}'.format(self.id, self.almacen.id)