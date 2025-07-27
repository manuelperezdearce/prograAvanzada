from model.videojuego_model import VideojuegoModel
from view.videojuego_view import VideojuegoView

class VideojuegoController:
    def __init__(self, root):
        self.modelo = VideojuegoModel()
        self.view = VideojuegoView()
        self.root = root

         # Cuando la vista llame al callback, ejecutará este método
        self.view.on_guardar_callback = self.guardar_videojuego

    def listar_videojuegos(self):
        videojuegos = self.modelo.readAll()
        self.view.mostrar_videojuegos(videojuegos, self.root)

    def agregar_videojuego(self):
        self.view.agregar_videojuego()
        

    def guardar_videojuego(self, titulo, genero, clasificacion, plataforma):
        # Aquí guardamos en la BD usando el modelo
        print("Guardando videojuego en BD:", titulo, genero, clasificacion, plataforma)
        self.modelo.insert(titulo, genero, clasificacion, plataforma)
        self.listar_videojuegos()
    
