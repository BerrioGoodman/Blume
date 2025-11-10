from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import companyModel
from .serializers import CompanySerializer, CompanyRegistroSerializer
from apps.application_jobs.models import ApplicationJobModel
from apps.application_jobs.serializers import ApplicationJobSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = companyModel.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return companyModel.objects.filter(user=self.request.user)

class RegistrarCompanyAPI(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @extend_schema(
        request=CompanyRegistroSerializer,
        responses={"201": CompanyRegistroSerializer},
        auth=[]
    )
    def create(self, request):
        serializer = CompanyRegistroSerializer(data=request.data)
        if serializer.is_valid():
            company = serializer.save()
            return Response({
                "id": company.id,
                "username": company.user.username,
                "email": company.user.email,
                "nombre": f"{company.user.first_name} {company.user.last_name}",
                "nombre_empresa": company.nombre_empresa,
                "sector_industria": company.sector_industria,
                "direccion": company.direccion,
                "telefono": company.telefono
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationManagementViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        application = get_object_or_404(ApplicationJobModel, pk=pk)
        # Check if the company owns the vacancy
        if application.vacante.company.user != request.user:
            return Response({"error": "No tienes permiso para modificar esta aplicación"}, status=status.HTTP_403_FORBIDDEN)
        
        new_status = request.data.get('estado')
        if new_status not in ['pendiente', 'aceptada', 'rechazada']:
            return Response({"error": "Estado inválido"}, status=status.HTTP_400_BAD_REQUEST)
        
        application.estado = new_status
        application.save()
        serializer = ApplicationJobSerializer(application)
        return Response(serializer.data)