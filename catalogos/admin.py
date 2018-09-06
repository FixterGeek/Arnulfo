from django.contrib import admin
from .models import Producto,Unidades,CFDI,Pago,BankAccount,Almacen,Presupuesto

# Register your models here.

admin.site.register(Producto)
admin.site.register(Unidades)
admin.site.register(CFDI)
admin.site.register(Pago)
admin.site.register(BankAccount)
admin.site.register(Almacen)
admin.site.register(Presupuesto)
