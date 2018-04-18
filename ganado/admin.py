from django.contrib import admin
from .models import Animal, Lote, Corral, GastoAnimal, Peso, Raza
from django.http import HttpResponse
from .resources import LoteResource, AnimalResource, GastoAnimalResource, PesoResource, RazaResource, CorralResource
from import_export.admin import ImportExportModelAdmin

class AnimalAdmin(ImportExportModelAdmin):
    resource_class = AnimalResource
    list_display = ['arete_rancho','arete_siniga','owner','lote']
    list_filter = ['lote__name','status']


class LoteAdmin(ImportExportModelAdmin):
    resource_class = LoteResource
    list_display = ['name','corral','status']

class CorralAdmin(ImportExportModelAdmin):
    resource_class = CorralResource

class GastoAnimalAdmin(ImportExportModelAdmin):
    resource_class = GastoAnimalResource

class PesoAdmin(ImportExportModelAdmin):
    resource_class = PesoResource

class RazaAdmin(ImportExportModelAdmin):
    resource_class = RazaResource

admin.site.register(Lote, LoteAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Corral, CorralAdmin)
admin.site.register(GastoAnimal, GastoAnimalAdmin)
admin.site.register(Peso, PesoAdmin)
admin.site.register(Raza, RazaAdmin)
# Register your models here.

