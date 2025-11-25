from django.urls import path
from .views import CompanyViewSet, RegistrarCompanyAPI, ApplicationManagementViewSet

urlpatterns = [
    path("registro/", RegistrarCompanyAPI.as_view({'post': 'create'}), name="registrar-empresa"),
    path("perfil/", CompanyViewSet.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update'}), name="empresa-perfil"),
    path("postulaciones/<int:pk>/actualizar-estado/", ApplicationManagementViewSet.as_view({'patch': 'update_status'}), name="empresa-actualizar-estado"),
]