from rest_framework import serializers
from .models import Vacancy

class VacancySerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.nombre_empresa', read_only=True)

    class Meta:
        model = Vacancy
        fields = ['id', 'company', 'company_name', 'titulo', 'descripcion', 'requisitos', 'fecha_publicacion', 'salario']