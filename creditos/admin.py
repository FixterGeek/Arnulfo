from django.contrib import admin
from .models import Disposicion, Acreedor, Recibo
# Register your models here.

admin.site.register(Disposicion)
admin.site.register(Recibo)
admin.site.register(Acreedor)
