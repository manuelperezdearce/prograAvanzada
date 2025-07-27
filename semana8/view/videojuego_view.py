class VideojuegoView:
    def __init__(self):
        pass

    def mostrar_videojuegos(self, videojuegos):
        for videojuego in videojuegos:
            print(f"{videojuego['titulo']}")