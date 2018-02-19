from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	admin = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección administrativa')
	ganado = models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del Ganado')

	def __str__(self):
		return self.user.username
