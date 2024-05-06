from import_export.admin import ExportActionMixin
from django.contrib import admin
from .models import Mensajes

class MensajeIntensionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','intension', 'mensaje')
    list_filter = ('intension',)
    search_fields = ('intension', 'mensaje')


# Register your models here.
admin.site.register(Mensajes, MensajeIntensionAdmin)