from import_export import resources
from .models import Disposicion, Acreedor


class AcreedorResource(resources.ModelResource):
    class Meta:
        model = Acreedor


class DisposicionResource(resources.ModelResource):
	class Meta:
		models = Disposicion