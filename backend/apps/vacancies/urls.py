from django.urls import path
from .views import VacancyViewSet

urlpatterns = [
    path("lista/", VacancyViewSet.as_view({'get': 'list'}), name="vacantes-lista"),
    path("crear/", VacancyViewSet.as_view({'post': 'create'}), name="vacantes-crear"),
    path("<int:pk>/detalle/", VacancyViewSet.as_view({'get': 'retrieve'}), name="vacantes-detalle"),
    path("<int:pk>/actualizar/", VacancyViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name="vacantes-actualizar"),
    path("<int:pk>/eliminar/", VacancyViewSet.as_view({'delete': 'destroy'}), name="vacantes-eliminar"),
]