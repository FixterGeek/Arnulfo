from import_export import resources
from .models import Almacen, ItemAlmacen
from import_export.admin import ImportExportModelAdmin


class AlmacenResource(resources.ModelResource):
    class Meta:
        model = Almacen

class ItemAlmacenResource(resources.ModelResource):
	class Meta:
		model = ItemAlmacen