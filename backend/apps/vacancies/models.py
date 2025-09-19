from django.db import models
from apps.companies.models import companyModel


# Create your models here.

class Vacancy(models.Model):
    id = models.BigAutoField(primary_key=True),
    company = models.ForeignKey(companyModel, on_delete=models.CASCADE, related_name="vacancies")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    requisitos = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "vacancy"

    def __str__(self):
        return f"{self.titulo} @ {self.company.nombre_empresa}"