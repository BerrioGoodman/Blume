from django.urls import path
from .views import ApplicationJobViewSet

urlpatterns = [
    path("lista/", ApplicationJobViewSet.as_view({'get': 'list'}), name="postulaciones-lista"),
    path("crear/", ApplicationJobViewSet.as_view({'post': 'create'}), name="postulaciones-crear"),
    path("<int:pk>/detalle/", ApplicationJobViewSet.as_view({'get': 'retrieve'}), name="postulaciones-detalle"),
    path("<int:pk>/actualizar/", ApplicationJobViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name="postulaciones-actualizar"),
    path("<int:pk>/eliminar/", ApplicationJobViewSet.as_view({'delete': 'destroy'}), name="postulaciones-eliminar"),
]