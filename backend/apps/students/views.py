from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EstudianteRegistroSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny

class RegistrarEstudianteAPI(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request = EstudianteRegistroSerializer,
        responses={"201": EstudianteRegistroSerializer},
        auth=[]
    )

    def post(self, request):
        serializer = EstudianteRegistroSerializer(data=request.data)
        if serializer.is_valid():
            estudiante = serializer.save()
            return Response({
                "id" : estudiante.id,
                "username": estudiante.user.username,
                "email": estudiante.user.email,
                "nombre": f"{estudiante.user.first_name} {estudiante.user.last_name}",
                "carrera": estudiante.carrera,
                "semestre": estudiante.semestre
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)