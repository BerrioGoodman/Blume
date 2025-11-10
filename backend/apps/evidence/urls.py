from django.urls import path
from .views import EvidenceViewSet

urlpatterns = [
    path("lista/", EvidenceViewSet.as_view({'get': 'list'}), name="evidencias-lista"),
    path("crear/", EvidenceViewSet.as_view({'post': 'create'}), name="evidencias-crear"),
    path("<int:pk>/detalle/", EvidenceViewSet.as_view({'get': 'retrieve'}), name="evidencias-detalle"),
    path("<int:pk>/actualizar/", EvidenceViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name="evidencias-actualizar"),
    path("<int:pk>/eliminar/", EvidenceViewSet.as_view({'delete': 'destroy'}), name="evidencias-eliminar"),
]