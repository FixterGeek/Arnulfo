from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Purchase, Provider, PurchaseItem, Compras
from .resources import PurchaseResource, ProviderResource, PurchaseItemResource, ComprasResource


class PurchaseAdmin(ImportExportModelAdmin):
    resource_class = PurchaseResource

class ProviderAdmin(ImportExportModelAdmin):
    resource_class = ProviderResource


class PurchaseItemAdmin(ImportExportModelAdmin):
    resource_class = PurchaseItemResource

class ComprasAdmin(ImportExportModelAdmin):
    resource_class = ComprasResource


admin.site.register(Provider, ProviderAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem, PurchaseItemAdmin)
admin.site.register(Compras, ComprasAdmin)

