from rest_framework import serializers
from .models import Intensiones

class IntensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intensiones
        fields = '__all__'
