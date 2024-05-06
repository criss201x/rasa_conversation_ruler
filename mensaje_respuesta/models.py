from django.db import models
from django.core.validators import RegexValidator
from respuesta.models import Respuesta
# Create your models here.
class MensajeRespuesta(models.Model):
#id es generado automaticamente por django :)    
    # Primary Key is implicitly added by Django
    respuesta = models.ForeignKey(
        Respuesta,  # Adjust if the Category model is in another app
        on_delete=models.RESTRICT,
        null=False,  # Makes it optional
        blank=False
    )
    
    mensaje = models.TextField(null=False, blank=False)
    class Meta:
        verbose_name = "Mensaje respuesta"
        verbose_name_plural = "Mensaje respuestas"


    def __str__(self):
        return self.mensaje