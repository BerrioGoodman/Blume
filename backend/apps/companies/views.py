from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanyRegistroSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny

class RegistrarCompanyAPI(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request = CompanyRegistroSerializer,
        responses={"201": CompanyRegistroSerializer},
        auth=[]
    )

    def post(self, request):
        serializer = CompanyRegistroSerializer(data=request.data)
        if serializer.is_valid():
            company = serializer.save()
            return Response({
                "id" : company.id,
                "username": company.user.username,
                "email": company.user.email,
                "nombre": f"{company.user.first_name} {company.user.last_name}",
                "nombre_empresa": company.nombre_empresa,
                "sector_industria": company.sector_industria,
                "direccion": company.direccion,
                "telefono": company.telefono
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)