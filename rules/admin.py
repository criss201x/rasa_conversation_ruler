from import_export.admin import ExportActionMixin
from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','prefijo', 'categoria_descripcion')
    list_filter = ('categoria_descripcion',)
    search_fields = ('prefijo', 'categoria_descripcion')
# Register your models here.


admin.site.register(Categoria,CategoriaAdmin)