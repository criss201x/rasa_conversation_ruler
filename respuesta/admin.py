from import_export.admin import ExportActionMixin
from django.contrib import admin
from .models import Respuesta

class RespuestaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','intension', 'nombre','descripcion_respuesta','categoria')
    list_filter = ('intension',)
    search_fields = ('nombre', 'descripcion_respuesta')

# Register your models here.
admin.site.register(Respuesta,RespuestaAdmin)