from django.db import models
from ingresos.models import BusinessLine

# Create your models here.

class Producto(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	code = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	bl = models.ForeignKey(BusinessLine, related_name="products", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name


class Unidades(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	code = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	bl = models.ForeignKey(BusinessLine, related_name="unidades", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class CFDI(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	code = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	bl = models.ForeignKey(BusinessLine, related_name="cfdis", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class Pago(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	code = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	bl = models.ForeignKey(BusinessLine, related_name="pagos", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class BankAccount(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	code = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	bl = models.ForeignKey(BusinessLine, related_name="bank_acounts", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class Almacen(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	code = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	bl = models.ForeignKey(BusinessLine, related_name="cat_almacenes", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class Presupuesto(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	code = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	pay_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
	concepto = models.CharField(max_length=100, blank=True, null=True)
	monto = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
	bl = models.ForeignKey(BusinessLine, related_name="presupuestos", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name



