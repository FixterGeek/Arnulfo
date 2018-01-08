from django.contrib import admin
from .models import Animal, Lote, Corral, Alimento

admin.site.register(Lote)
admin.site.register(Animal)
admin.site.register(Corral)
admin.site.register(Alimento)
# Register your models here.

