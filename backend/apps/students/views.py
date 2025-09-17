from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Application.registrar_estudiante import RegistrarEstudiante
from .repositories import EstudianteRepository

class RegistrarEstudianteAPI(APIView):
    def post(self, request):
        data = request.data
        try:
            usecase = RegistrarEstudiante(EstudianteRepository())
            estudiante = usecase.execute(
                data["nombre"],
                data["correo"],
                data["carrera"]
            )
            return Response({
                "id": str(estudiante.id),
                "nombre": estudiante.nombre,
                "correo": estudiante.correo,
                "carrera": estudiante.carrera
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
