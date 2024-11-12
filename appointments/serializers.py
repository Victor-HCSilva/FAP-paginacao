from rest_framework import serializers
from .models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__' 
        # ou especifique os campos específicos que você deseja serializar
        extra_kwargs = {
            'date': {'required': True},
            'time': {'required': True},
            'patient': {'required': True},
            'doctor': {'required': True},
        } 