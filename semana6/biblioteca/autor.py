class Autor:
    def __init__(self, id, nombre, nacionalidad):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Nacionalidad: {self.nacionalidad}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad
        }