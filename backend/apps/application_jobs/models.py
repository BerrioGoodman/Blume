from django.db import models
from apps.students.models import EstudianteModel
from apps.vacancies.models import Vacancy

class ApplicationJobModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    estudiante = models.ForeignKey(EstudianteModel, on_delete=models.CASCADE, related_name="application_jobs")
    vacante = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="application_jobs")
    estado = models.CharField(max_length=50, default="pendiente")
    fecha_postulacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "application_jobs"
        unique_together = ('estudiante', 'vacante')  # Un estudiante no puede postularse a la misma vacante más de una vez

    def __str__(self):
        return f"{self.estudiante.user.username} - {self.vacante.titulo} - {self.estado}"