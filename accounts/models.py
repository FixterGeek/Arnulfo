from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	admin = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección administrativa')
	ganado = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del Ganado')
	#vendedor = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección de Ventas')
	vacunas = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección de vacunas')
	alimentos = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del alimentos')
	cerdos = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del cerdos')
	aves = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del aves')


	def __unicode__(self):
		return self.user.username
