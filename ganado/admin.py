from django.contrib import admin
from .models import Animal, Lote, Corral, GastoAnimal

admin.site.register(Lote)
admin.site.register(Animal)
admin.site.register(Corral)
admin.site.register(GastoAnimal)
# Register your models here.

