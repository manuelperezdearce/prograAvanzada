import os
import pickle

from biblioteca.libro import Libro

class LibrosManager:
    def __init__(self, libros_path=None, autores_path=None):
        base_dir = os.path.dirname(__file__)
        self.libros_path = libros_path or os.path.join(base_dir, "bd", "libros.pkl")
        self.autores_path = autores_path or os.path.join(base_dir, "bd", "autores.pkl")
        self.libros = self._cargar_libros()
        self.autores = self._cargar_autores()

    def _cargar_libros(self):
        if not os.path.exists(self.libros_path):
            return []
        with open(self.libros_path, "rb") as file:
            return pickle.load(file)

    def _cargar_autores(self):
        if not os.path.exists(self.autores_path):
            return []
        with open(self.autores_path, "rb") as file:
            return pickle.load(file)

    def _guardar_libros(self):
        with open(self.libros_path, "wb") as file:
            pickle.dump(self.libros, file)

    def _askInfoToUser(self):
        titulo = input("Título del libro: ")
        genero = input("Género: ")
        año = input("Año de publicación: ")

        print("\n--- Autores Disponibles ---")
        for autor in self.autores:
            print(f"{autor.id}: {autor.nombre} ({autor.nacionalidad})")

        try:
            autor_id = int(input("Seleccione el ID del autor: "))
        except ValueError:
            print("ID inválido.")
            return None

        if not any(a.id == autor_id for a in self.autores):
            print("ID de autor no válido.")
            return None

        return {
            "titulo": titulo,
            "genero": genero,
            "año": año,
            "autor_id": autor_id
        }

    def agregar_libro(self):
        data = self._askInfoToUser()
        if not data:
            return

        nuevo_id = 1 if not self.libros else self.libros[-1].id + 1
        libro = Libro(nuevo_id, data["titulo"], data["genero"], data["año"], data["autor_id"])
        self.libros.append(libro)
        self._guardar_libros()
        print("\nLibro agregado correctamente.\n")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros registrados.")
            return

        print("\n--- Lista de Libros ---\n")
        for libro in self.libros:
            autor = next((a for a in self.autores if a.id == libro.autor_id), None)
            nombre_autor = autor.nombre if autor else "Desconocido"
            print(f"{libro.id}. {libro.titulo} - {libro.genero} - {libro.anio} | Autor: {nombre_autor}")
