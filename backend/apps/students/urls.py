from django.urls import path
from .views import RegistrarEstudianteAPI

urlpatterns = [
    path("", RegistrarEstudianteAPI.as_view(), name="registrar-estudiante"),
]
