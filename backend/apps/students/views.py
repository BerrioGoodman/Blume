from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EstudianteRegistroSerializer

class RegistrarEstudianteAPI(APIView):
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