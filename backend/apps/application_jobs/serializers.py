from rest_framework import serializers
from .models import ApplicationJobModel

class ApplicationJobSerializer(serializers.ModelSerializer):
    estudiante_name = serializers.CharField(source='estudiante.user.username', read_only=True)
    vacante_titulo = serializers.CharField(source='vacante.titulo', read_only=True)
    company_name = serializers.CharField(source='vacante.company.nombre_empresa', read_only=True)

    class Meta:
        model = ApplicationJobModel
        fields = ['id', 'estudiante', 'estudiante_name', 'vacante', 'vacante_titulo', 'company_name', 'estado', 'fecha_postulacion']