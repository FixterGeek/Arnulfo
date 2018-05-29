from import_export import resources
from .models import Sale, SaleItem, Client, Company, BusinessLine, CuentaBanco

class CuentaBancoResource(resources.ModelResource):
	class Meta:
		model = CuentaBanco

class SaleResource(resources.ModelResource):
	class Meta:
		model = Sale

class SaleItemResource(resources.ModelResource):
	class Meta:
		model = SaleItem

class ClientResource(resources.ModelResource):
	class Meta:
		model = Client

class CompanyResource(resources.ModelResource):
	class Meta:
		model = Company

class BusinessLineResource(resources.ModelResource):
	class Meta:
		model = BusinessLine