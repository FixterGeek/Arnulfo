from django.contrib import admin
from .models import Animal, Lote, Corral, GastoAnimal, Peso

class AnimalAdmin(admin.ModelAdmin):
	list_display = ['arete_rancho','arete_siniga','owner','lote']
	list_filter = ['lote','status']


admin.site.register(Lote)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Corral)
admin.site.register(GastoAnimal)
admin.site.register(Peso)
# Register your models here.

