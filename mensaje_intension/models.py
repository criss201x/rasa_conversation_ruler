from django.db import models
from django.core.validators import RegexValidator
from intension.models import Intensiones
# Create your models here.
class Mensajes(models.Model):
#id es generado automaticamente por django :)    
    # Primary Key is implicitly added by Django
    
    intension = models.ForeignKey(
        Intensiones,  # Adjust if the Category model is in another app
        on_delete=models.RESTRICT,
        null=False,  # Makes it optional
        blank=False
    )
    
    mensaje = models.TextField(null=False, blank=False)
    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"


    def __str__(self):
        return self.mensaje