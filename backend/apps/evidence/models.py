from django.db import models
from apps.application_jobs.models import ApplicationJobModel

# Create your models here.

class EvidenceModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    trabajo_aplicado = models.ForeignKey(ApplicationJobModel, on_delete=models.CASCADE, related_name="evidences")
    archivo = models.FileField(upload_to='evidences/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "evidences"

    def __str__(self):
        return f"Evidencia de: {self.nombre_archivo} - {self.fecha_subida.date()}"