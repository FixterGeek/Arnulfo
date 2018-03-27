from import_export import resources
from .models import Purchase, Provider, Product, PurchaseItem


class PurchaseResource(resources.ModelResource):
    class Meta:
        model = Purchase

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider

class PurchaseItemResource(resources.ModelResource):
    class Meta:
        model = PurchaseItem