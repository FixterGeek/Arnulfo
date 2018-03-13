from django.contrib import admin
from .models import Almacen, ItemAlmacen
from django.contrib.auth.admin import UserAdmin


class AdminItem(admin.StackedInline):
	model = ItemAlmacen
 
class AdminAlmacen(admin.ModelAdmin):
	inlines = (AdminItem, )

admin.site.register(Almacen, AdminAlmacen)
admin.site.register(ItemAlmacen)
