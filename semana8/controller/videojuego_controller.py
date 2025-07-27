from model.videojuego_model import VideojuegoModel
from view.videojuego_view import VideojuegoView

class VideojuegoController:
    def __init__(self):
        self.modelo = VideojuegoModel()
        self.view = VideojuegoView()

    def listar_videojuegos(self):
        videojuegos = self.modelo.readAll()
        self.view.mostrar_videojuegos(videojuegos)
    


