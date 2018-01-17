from django.contrib import admin
from .models import Animal, Lote, Corral, GastoAnimal, Peso

admin.site.register(Lote)
admin.site.register(Animal)
admin.site.register(Corral)
admin.site.register(GastoAnimal)
admin.site.register(Peso)
# Register your models here.

