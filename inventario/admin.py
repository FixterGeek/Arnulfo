from django.contrib import admin
from .models import Almacen, ItemAlmacen
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from .resources import AlmacenResource, ItemAlmacenResource




class AdminItem(admin.StackedInline):
	model = ItemAlmacen
 
class AdminAlmacen(ImportExportModelAdmin):
    resource_class = AlmacenResource
    inlines = (AdminItem, )

class ItemAlmacenAdmin(ImportExportModelAdmin):
    resource_class = ItemAlmacenResource
    

admin.site.register(Almacen, AdminAlmacen)
admin.site.register(ItemAlmacen, ItemAlmacenAdmin)
