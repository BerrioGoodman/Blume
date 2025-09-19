from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class companyModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="companies")
    nombre_empresa = models.CharField(max_length=200)
    sector_industria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=20)

    class Meta:
        db_table = "companies"

    def __str__(self):
        return f"{self.nombre_empresa} - {self.sector_industria}"
