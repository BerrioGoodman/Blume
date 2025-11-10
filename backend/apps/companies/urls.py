from django.urls import path
from .views import RegistrarCompanyAPI

urlpatterns = [
    path("register/", RegistrarCompanyAPI.as_view(), name="registrar-company"),
]