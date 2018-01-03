from django.contrib import admin
from .models import Product, Sale, SaleItem, Client

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Client)
# Register your models here.
