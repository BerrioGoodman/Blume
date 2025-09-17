from Domain.estudiante import Estudiante

class RegistrarEstudiante:
    def __init__(self, estudiante_repo):
        self.estudiante_repo = estudiante_repo  

    def execute(self, nombre, correo, carrera):
        if not correo.endswith("@pascualbravo.edu.co"):
            raise ValueError("El correo debe ser institucional (@pascualbravo.edu.co)")

        estudiante = Estudiante(nombre=nombre, correo=correo, carrera=carrera)
        return self.estudiante_repo.save(estudiante)
