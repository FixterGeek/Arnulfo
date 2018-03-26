from django.contrib import admin
from .models import Animal, Lote, Corral, GastoAnimal, Peso, Raza

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
        smart_str(u"arete_siniga"),
        smart_str(u"arete_rancho"),
        smart_str(u"fecha_entrada"),
        smart_str(u"fecha_registro"),
        smart_str(u"peso_entrada"),
        smart_str(u"descripcion"),
        smart_str(u"costo_kilo"),
        smart_str(u"raza"),
        smart_str(u"color"),
        smart_str(u"owner"),
        smart_str(u"lote"),
        smart_str(u"tipo_animal"),
        smart_str(u"status"),
        smart_str(u"costo_inicial"),
        smart_str(u"fierro_original"),
        smart_str(u"fierro_nuevo"),
        smart_str(u"ref_factura_original"),
        smart_str(u"merma"),
        smart_str(u"empresa"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.arete_siniga),
            smart_str(obj.arete_rancho),
            smart_str(obj.fecha_entrada),
            smart_str(obj.fecha_registro),
            smart_str(obj.peso_entrada),
            smart_str(obj.descripcion),
            smart_str(obj.costo_kilo),
            smart_str(obj.raza),
            smart_str(obj.color),
            smart_str(obj.owner),
            smart_str(obj.lote),
            smart_str(obj.tipo_animal),
            smart_str(obj.status),
            smart_str(obj.costo_inicial),
            smart_str(obj.fierro_original),
            smart_str(obj.fierro_nuevo),
            smart_str(obj.ref_factura_original),
            smart_str(obj.merma),
            smart_str(obj.empresa),
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
admin.site.register(Raza)
# Register your models here.

