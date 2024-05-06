from import_export.admin import ExportActionMixin
from django.contrib import admin
from .models import MensajeRespuesta

class MensajeRespuestaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','respuesta', 'mensaje')
    list_filter = ('respuesta',)
    search_fields = ('respuesta', 'mensaje')


# Register your models here.
admin.site.register(MensajeRespuesta, MensajeRespuestaAdmin)