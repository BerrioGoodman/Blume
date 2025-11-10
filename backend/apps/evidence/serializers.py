from rest_framework import serializers
from .models import EvidenceModel

class EvidenceSerializer(serializers.ModelSerializer):
    estudiante_name = serializers.CharField(source='trabajo_aplicado.estudiante.user.username', read_only=True)
    vacante_titulo = serializers.CharField(source='trabajo_aplicado.vacante.titulo', read_only=True)

    class Meta:
        model = EvidenceModel
        fields = ['id', 'trabajo_aplicado', 'estudiante_name', 'vacante_titulo', 'archivo', 'fecha_subida']