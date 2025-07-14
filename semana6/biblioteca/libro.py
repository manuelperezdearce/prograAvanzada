class Libro:
    def __init__(self, id, titulo, genero, anio, autor_id):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.autor_id = autor_id

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Título: {self.titulo} | "
            f"Género: {self.genero} | "
            f"Año: {self.anio} | "
            f"ID Autor: {self.autor_id}"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "anio" : self.anio,
            "autor_id": self.autor_id
        }