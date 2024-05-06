from rest_framework import serializers
from .models import MensajeRespuesta

class MensajeRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensajeRespuesta
        fields = '__all__'
