from django.db import models
import uuid

class EstudianteModel(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)
    carrera = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
