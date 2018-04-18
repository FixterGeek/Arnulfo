from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Purchase, Provider, Product, PurchaseItem
from .resources import PurchaseResource, ProviderResource, ProductResource, PurchaseItemResource


class PurchaseAdmin(ImportExportModelAdmin):
    resource_class = PurchaseResource

class ProviderAdmin(ImportExportModelAdmin):
    resource_class = ProviderResource

class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource

class PurchaseItemAdmin(ImportExportModelAdmin):
    resource_class = PurchaseItemResource

admin.site.register(Product, ProductAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem, PurchaseItemAdmin)

