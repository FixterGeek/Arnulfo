from django.contrib import admin
from .models import Sale, SaleItem, Client, Company, BusinessLine
from import_export.admin import ImportExportModelAdmin
from .resources import SaleResource, SaleItemResource, ClientResource, CompanyResource, BusinessLineResource


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



admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleItem, SaleItemAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(BusinessLine, BusinessLineAdmin)
# Register your models here.
