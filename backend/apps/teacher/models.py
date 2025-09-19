from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    materia = models.CharField(max_length=150)
    departamento = models.CharField(max_length=100)

    class Meta:
        db_table = "teachers"

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.departamento}"
