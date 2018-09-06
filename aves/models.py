from django.db import models

# Create your models here.

class Lote(models.Model):
	identificador = models.CharField(max_length=100)

	def __unicode__(self):
		return self.identificador

class Ave(models.Model):
	identificador = models.CharField(max_length=100)

	def __unicode__(self):
		return self.identificador

class Huevo(models.Model):

	cantidad = models.IntegerField()
	fecha = models.DateTimeField(auto_now_add=False, db_index=True)
	ave = models.ForeignKey(Ave, related_name='huevos', on_delete=models.CASCADE)

	def __unicode__(self):
		return self.cantidad




