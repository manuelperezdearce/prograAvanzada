import os
import pickle
from biblioteca.autor import Autor

class AutoresManager:
    def __init__(self, filepath=None):
        if filepath is None:
            base_dir = os.path.dirname(__file__)
            self.filepath = os.path.join(base_dir, "bd", "autores.pkl")
        else:
            self.filepath = filepath

        self.autores = self._cargar_autores()

    def _cargar_autores(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "rb") as file:
            return pickle.load(file)

    def _guardar_autores(self):
        with open(self.filepath, "wb") as file:
            pickle.dump(self.autores, file)

    def _askInfoToUser(self):
        nombre = input("Ingrese nombre: ")
        nacionalidad = input("Ingrese nacionalidad: ")
        return {"nombre": nombre, "nacionalidad": nacionalidad}

    def agregar_autor(self):
        userResponse = self._askInfoToUser()
        nuevo_id = 1 if not self.autores else self.autores[-1].id + 1
        autor = Autor(nuevo_id, userResponse["nombre"], userResponse["nacionalidad"])
        self.autores.append(autor)
        self._guardar_autores()
        print("\nAutor agregado correctamente.\n")

    def listar_autores(self):
        if not self.autores:
            print("No hay autores registrados.")
            return
        print("\n--- Lista de Autores ---\n")
        for autor in self.autores:
            print(autor)