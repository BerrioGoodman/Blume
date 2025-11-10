from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import EvidenceModel
from .serializers import EvidenceSerializer

class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = EvidenceModel.objects.all()
    serializer_class = EvidenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'estudiantes'):
            # Students see their own evidence
            return EvidenceModel.objects.filter(trabajo_aplicado__estudiante=user.estudiantes)
        elif hasattr(user, 'companies'):
            # Companies see evidence for their vacancies
            return EvidenceModel.objects.filter(trabajo_aplicado__vacante__company=user.companies)
        return EvidenceModel.objects.none()

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'estudiantes'):
            serializer.save()
        else:
            raise PermissionError("Solo estudiantes pueden subir evidencia")
