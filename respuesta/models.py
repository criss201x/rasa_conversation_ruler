from django.db import models
from django.core.validators import RegexValidator
from intension.models import Intensiones
from rules.models import Categoria
# Create your models here.
class Respuesta(models.Model):
#id es generado automaticamente por django :)    
    # Primary Key is implicitly added by Django
    intension = models.ForeignKey(
        Intensiones,  # Adjust if the Category model is in another app
        on_delete=models.RESTRICT,
        null=False,  # Makes it optional
        blank=False
    )
    
    nombre = models.CharField(
        max_length=250,  # Adjust the length as needed
        unique=True,
        validators=[
            RegexValidator(
                regex='^[^\s]*$',  # No spaces allowed
                message='El nombre no debe tener espacios.',
                code='invalid_name'
            )
        ]
    )
        
    descripcion_respuesta = models.TextField(null=True, blank=True)

    categoria = models.ForeignKey(
        Categoria,  # Adjust if the Category model is in another app
        on_delete=models.RESTRICT,
        null=True,  # Makes it optional
        blank=True
    )
    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"


    def __str__(self):
        return self.nombre