from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AministratorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=150)
    nivel_acceso = models.TextField(blank=True)

    class Meta:
        db_table = "administrators"

    def __str__(self):
        return f"{self.user.username} - {self.rol}"
