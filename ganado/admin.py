from django.contrib import admin
from .models import Animal, Lote, Corral, GastoAnimal, Peso

from django.http import HttpResponse


def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Animals.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Title"),
        smart_str(u"Lote"),
        smart_str(u"Fierro")
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.arete_rancho),
            smart_str(obj.lote),
            smart_str(obj.fierro_nuevo)
        ])
    return response
export_csv.short_description = u"Export CSV"


class AnimalAdmin(admin.ModelAdmin):
	list_display = ['arete_rancho','arete_siniga','owner','lote']
	list_filter = ['lote','status']
	actions = [export_csv]






admin.site.register(Lote)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Corral)
admin.site.register(GastoAnimal)
admin.site.register(Peso)
# Register your models here.

