from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ApplicationJobModel
from .serializers import ApplicationJobSerializer

class ApplicationJobViewSet(viewsets.ModelViewSet):
    queryset = ApplicationJobModel.objects.all()
    serializer_class = ApplicationJobSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'estudiantes'):
            # Students see their own applications
            return ApplicationJobModel.objects.filter(estudiante=user.estudiantes)
        elif hasattr(user, 'companies'):
            # Companies see applications to their vacancies
            return ApplicationJobModel.objects.filter(vacante__company=user.companies)
        return ApplicationJobModel.objects.none()

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'estudiantes'):
            serializer.save(estudiante=self.request.user.estudiantes)
        else:
            raise PermissionError("Solo estudiantes pueden postularse")
