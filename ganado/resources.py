from import_export import resources
from .models import Animal, Lote, Corral, GastoAnimal, Peso, Raza


class LoteResource(resources.ModelResource):
    class Meta:
        model = Lote

class AnimalResource(resources.ModelResource):
    class Meta:
        model = Animal

class CorralResource(resources.ModelResource):
    class Meta:
        model = Corral

class PesoResource(resources.ModelResource):
    class Meta:
        model = Peso

class RazaResource(resources.ModelResource):
    class Meta:
        model = Raza

class GastoAnimalResource(resources.ModelResource):
    class Meta:
        model = GastoAnimal