import os
import json

class AutoresManager:
    def __init__(self, filepath=None):
        # Definir ruta del archivo JSON
        if filepath is None:
            base_dir = os.path.dirname(__file__)
            self.filepath = os.path.join(base_dir, "bd", "autores.json")
        else:
            self.filepath = filepath

        # Cargar autores existentes o crear archivo vacío
        self.autores = self._cargar_autores()

    def _cargar_autores(self):
        """Carga los autores desde el archivo JSON. Si no existe, lo crea vacío."""
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)
            return []
        with open(self.filepath, "r", encoding="utf-8") as file:
            return json.load(file)

    def _guardar_autores(self):
        """Guarda la lista de autores en el archivo JSON."""
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(self.autores, file, indent=4, ensure_ascii=False)

    def _askInfoToUser(self):
        """Solicita los datos del autor al usuario."""
        nombre = input("Ingrese nombre: ")
        nacionalidad = input("Ingrese nacionalidad: ")
        return {"nombre": nombre, "nacionalidad": nacionalidad}

    def agregar_autor(self):
        """Agrega un nuevo autor con un ID autoincremental."""
        userResponse = self._askInfoToUser()
        # Calcular nuevo ID autoincremental
        nuevo_id = 1 if not self.autores else self.autores[-1]["id"] + 1

        nuevo_autor = {
            "id": nuevo_id,
            "nombre": userResponse["nombre"],
            "nacionalidad": userResponse["nacionalidad"]
        }

        # Agregar a la lista y guardar
        self.autores.append(nuevo_autor)
        self._guardar_autores()
        print("\n✅ Autor agregado correctamente.\n")

    def listar_autores(self):
        """Muestra todos los autores en formato legible."""
        if not self.autores:
            print("No hay autores registrados.")
            return

        print("\n--- Lista de Autores ---\n")
        for autor in self.autores:
            print(f"{autor['id']}. {autor['nombre']} - {autor['nacionalidad']}")
