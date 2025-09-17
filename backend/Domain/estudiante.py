import uuid

class Estudiante:
    def __init__(self, id=None, nombre=None, correo= None, carrera=None):
        self.id = id or uuid.uuid4()
        self.nombre = nombre
        self.correo = correo
        self.carrera = carrera

    def __str__(self):
        return f"{self.nombre}, {self.correo}, {self.carrera}"