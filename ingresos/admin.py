from django.contrib import admin
from .models import Sale, SaleItem, Client, Company, BusinessLine, CuentaBanco
from import_export.admin import ImportExportModelAdmin
from .resources import SaleResource, SaleItemResource, ClientResource, CompanyResource, BusinessLineResource, CuentaBancoResource


class SaleAdmin(ImportExportModelAdmin):
    resource_class = SaleResource

class SaleItemAdmin(ImportExportModelAdmin):
    resource_class = SaleItemResource

class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource

class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource

class BusinessLineAdmin(ImportExportModelAdmin):
    resource_class = BusinessLineResource

class CuentaBancoAdmin(ImportExportModelAdmin):
    resource_class = CuentaBancoResource



admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleItem, SaleItemAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(BusinessLine, BusinessLineAdmin)
admin.site.register(CuentaBanco, CuentaBancoAdmin)
# Register your models here.
