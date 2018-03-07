from django.contrib import admin
from .models import Sale, SaleItem, Client, Company, BusinessLine

admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Client)
admin.site.register(Company)
admin.site.register(BusinessLine)
# Register your models here.
