from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer, TeacherRegistroSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None  # Disable pagination for list

    def get_queryset(self):
        # For educational purposes, allow listing all teachers
        # In production, add role-based logic
        return Teacher.objects.all()

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None  # Disable pagination for profile

    def get_queryset(self):
        return Teacher.objects.filter(user=self.request.user)

    def get_object(self):
        # For profile endpoints, return the user's teacher instance
        return self.get_queryset().first()

class RegistrarTeacherAPI(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @extend_schema(
        request=TeacherRegistroSerializer,
        responses={"201": TeacherRegistroSerializer},
        auth=[]
    )
    def create(self, request):
        serializer = TeacherRegistroSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            return Response({
                "id": teacher.id,
                "username": teacher.user.username,
                "email": teacher.user.email,
                "nombre": f"{teacher.user.first_name} {teacher.user.last_name}",
                "materia": teacher.materia,
                "departamento": teacher.departamento
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
