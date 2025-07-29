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
        self.modelo.insert(titulo, genero, clasificacion, plataforma)
        self.listar_videojuegos()
    
    def editar_videojuego(self):
        videojuego_id = self.view.get_selected_item()

        if not videojuego_id:
            print("⚠️ No hay ningún videojuego seleccionado.")
            return

        # Obtener los datos del videojuego desde la BD
        videojuego = self.modelo.find_by_id(videojuego_id)

        if videojuego:
            # Pasar los datos al formulario en modo edición
            self.view.on_editar_callback = self.actualizar_videojuego
            self.view.agregar_videojuego(videojuego)
        else:
            print("❌ No se encontró el videojuego con ID:", videojuego_id)

    def actualizar_videojuego(self, id_videojuego, titulo, genero, clasificacion, plataforma):
        print("Actualizando videojuego ID", id_videojuego)
        self.modelo.update(id_videojuego, titulo, genero, clasificacion, plataforma)
        self.listar_videojuegos()

    def eliminar_videojuego(self):
        videojuego_id = self.view.get_selected_item()
        self.modelo.delete(videojuego_id)
        self.listar_videojuegos()
