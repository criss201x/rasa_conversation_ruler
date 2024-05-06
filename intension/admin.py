from import_export.admin import ExportActionMixin
from django.contrib import admin
from .models import Intensiones

class IntensionAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion','categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')


# Register your models here.
admin.site.register(Intensiones, IntensionAdmin)