from django.db import models
from django.contrib.auth.models import User

class EstudianteModel(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="students_estudiantemodel")
    carrera = models.CharField(max_length=200)
    semestre = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username
