from import_export import resources
from .models import Purchase, Provider, PurchaseItem


class PurchaseResource(resources.ModelResource):
    class Meta:
        model = Purchase

class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider

class PurchaseItemResource(resources.ModelResource):
    class Meta:
        model = PurchaseItem