from .models import EstudianteModel

class EstudianteRepository:
    def save(self, estudiante):
        obj = EstudianteModel.objects.create(
            id=estudiante.id,
            nombre=estudiante.nombre,
            correo=estudiante.correo,
            carrera=estudiante.carrera
        )
        return obj
    