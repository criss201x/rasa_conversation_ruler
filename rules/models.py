from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Categoria(models.Model):
#id es generado automaticamente por django :)    
    prefijo = models.CharField(
        max_length=5, 
        unique=True, 
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]*$', 
                message='La categoría debe ser alfanumérica y no contener espacios ni caracteres especiales.', 
                code='categoria_invalida'
            )
        ]
    )
    categoria_descripcion = models.TextField(null=False, blank=False)
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria_descripcion