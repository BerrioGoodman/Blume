from django.urls import path
from .views import AdministratorViewSet, AdministratorProfileViewSet, RegistrarAdministratorAPI

urlpatterns = [
    path("registro/", RegistrarAdministratorAPI.as_view({'post': 'create'}), name="registrar-administrador"),
    path("perfil/", AdministratorProfileViewSet.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update'}), name="administrador-perfil"),
    path("lista/", AdministratorViewSet.as_view({'get': 'list'}), name="administradores-lista"),
]