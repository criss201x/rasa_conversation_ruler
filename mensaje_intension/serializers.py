from rest_framework import serializers
from .models import Mensajes

class MensajeIntensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
        fields = '__all__'
