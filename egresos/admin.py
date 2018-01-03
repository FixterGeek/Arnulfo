from django.contrib import admin
from .models import Purchase, Provider, Product, PurchaseItem

admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)

