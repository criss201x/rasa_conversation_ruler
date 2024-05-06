from django.db import models
from django.core.validators import RegexValidator
from rules.models import Categoria
# Create your models here.
class Intensiones(models.Model):
#id es generado automaticamente por django :)    
    # Primary Key is implicitly added by Django
    nombre = models.CharField(
        max_length=250,  # Adjust the length as needed
        null=False,
        blank=False,
        unique=True,
        validators=[
            RegexValidator(
                regex='^[^\s]*$',  # No spaces allowed
                message='El nombre no debe tener espacios.',
                code='invalid_name'
            )
        ]
    )

    descripcion = models.TextField(null=False, blank=False,)  # No max length, but can set if required
    categoria = models.ForeignKey(
        Categoria,  # Adjust if the Category model is in another app
        on_delete=models.RESTRICT,
        null=True,  # Makes it optional
        blank=True
    )
    class Meta:
        verbose_name = "intención"
        verbose_name_plural = "Intensiones"

    def __str__(self):
        return self.nombre