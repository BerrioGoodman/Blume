from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Vacancy
from .serializers import VacancySerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        # Companies can see their own vacancies
        if hasattr(self.request.user, 'companies'):
            return Vacancy.objects.filter(company=self.request.user.companies)
        return Vacancy.objects.none()

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'companies'):
            serializer.save(company=self.request.user.companies)
        else:
            raise PermissionError("Solo empresas pueden crear vacantes")
