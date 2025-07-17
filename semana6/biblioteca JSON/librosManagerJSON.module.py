import os
import json

class LibrosManager:
    def __init__(self, libros_path=None, autores_path=None):
        base_dir = os.path.dirname(__file__)
        self.libros_path = libros_path or os.path.join(base_dir, "bd", "libros.json")
        self.autores_path = autores_path or os.path.join(base_dir, "bd", "autores.json")
        self.libros = self._cargar_json(self.libros_path)
        self.autores = self._cargar_json(self.autores_path)

    def _cargar_json(self, path):
        """Carga datos desde un JSON, si no existe crea uno vacío."""
        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump([], f, indent=4)
            return []
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _guardar_json(self, path, data):
        """Guarda datos en un JSON con indentación legible."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def _askInfoToUser(self):
        titulo = input("Título del libro: ")
        genero = input("Género: ")
        anio = input("Año de publicación: ")

        print("\n--- Autores Disponibles ---")
        for autor in self.autores:
            print(f"{autor['id']}: {autor['nombre']} ({autor['nacionalidad']})")

        try:
            autor_id = int(input("Seleccione el ID del autor: "))
        except ValueError:
            print("ID inválido.")
            return None

        if not any(a["id"] == autor_id for a in self.autores):
            print("ID de autor no válido.")
            return None

        return {
            "titulo": titulo,
            "genero": genero,
            "anio": anio,
            "autor_id": autor_id
        }

    def agregar_libro(self):
        data = self._askInfoToUser()
        if not data:
            return

        nuevo_id = 1 if not self.libros else self.libros[-1]["id"] + 1

        # Convertimos el libro en un diccionario antes de guardar
        libro = {
            "id": nuevo_id,
            "titulo": data["titulo"],
            "genero": data["genero"],
            "anio": data["anio"],
            "autor_id": data["autor_id"]
        }

        self.libros.append(libro)
        self._guardar_json(self.libros_path, self.libros)
        print("\n✅ Libro agregado correctamente.\n")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros registrados.")
            return

        print("\n--- Lista de Libros ---\n")
        for libro in self.libros:
            autor = next((a for a in self.autores if a["id"] == libro["autor_id"]), None)
            nombre_autor = autor["nombre"] if autor else "Desconocido"
            print(f"{libro['id']}. {libro['titulo']} - {libro['genero']} - {libro['anio']} | Autor: {nombre_autor}")

