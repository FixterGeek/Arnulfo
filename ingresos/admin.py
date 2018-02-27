from django.contrib import admin
from .models import Sale, SaleItem, Client, Company

admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Client)
admin.site.register(Company)
# Register your models here.
