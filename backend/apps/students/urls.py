from django.urls import path
from .views import EstudianteViewSet, RegistrarEstudianteAPI, VacancyListView

urlpatterns = [
    path("registro/", RegistrarEstudianteAPI.as_view({'post': 'create'}), name="registrar-estudiante"),
    path("perfil/", EstudianteViewSet.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update'}), name="estudiante-perfil"),
    path("vacantes/", VacancyListView.as_view({'get': 'list'}), name="estudiante-vacantes"),
]
