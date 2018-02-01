from django.contrib import admin
from .models import Formula,Insumo,Item

# Register your models here.
admin.site.register(Formula)
admin.site.register(Insumo)
admin.site.register(Item)