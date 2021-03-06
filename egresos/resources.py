from import_export import resources
from .models import Purchase, Provider, PurchaseItem, Compras, GastoGanado


class GastoResource(resources.ModelResource):
    class Meta:
        model = GastoGanado

class PurchaseResource(resources.ModelResource):
    class Meta:
        model = Purchase

class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider

class PurchaseItemResource(resources.ModelResource):
    class Meta:
        model = PurchaseItem

class ComprasResource(resources.ModelResource):
    class Meta:
        model = Compras