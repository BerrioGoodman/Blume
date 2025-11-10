from django.urls import path
from .views import TeacherViewSet, TeacherProfileViewSet, RegistrarTeacherAPI

urlpatterns = [
    path("registro/", RegistrarTeacherAPI.as_view({'post': 'create'}), name="registrar-docente"),
    path("perfil/", TeacherProfileViewSet.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update'}), name="docente-perfil"),
    path("lista/", TeacherViewSet.as_view({'get': 'list'}), name="docentes-lista"),
]