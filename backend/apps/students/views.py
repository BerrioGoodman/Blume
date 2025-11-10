from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import EstudianteModel
from .serializers import EstudianteSerializer, EstudianteRegistroSerializer
from apps.vacancies.models import Vacancy
from apps.vacancies.serializers import VacancySerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = EstudianteModel.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EstudianteModel.objects.filter(user=self.request.user)

class RegistrarEstudianteAPI(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @extend_schema(
        request=EstudianteRegistroSerializer,
        responses={"201": EstudianteRegistroSerializer},
        auth=[]
    )
    def create(self, request):
        serializer = EstudianteRegistroSerializer(data=request.data)
        if serializer.is_valid():
            estudiante = serializer.save()
            return Response({
                "id": estudiante.id,
                "username": estudiante.user.username,
                "email": estudiante.user.email,
                "nombre": f"{estudiante.user.first_name} {estudiante.user.last_name}",
                "carrera": estudiante.carrera,
                "semestre": estudiante.semestre
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacancyListView(viewsets.ReadOnlyModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Students can view all vacancies
        return Vacancy.objects.all()