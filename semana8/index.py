import tkinter as tk
from controller.videojuego_controller import VideojuegoController
from view.header import create_header  # ajusta si la ruta es distinta

root = tk.Tk()
root.title("Gestión de Videojuegos")
root.geometry("800x500")

# ✅ Crear controlador principal
app = VideojuegoController(root)

# ✅ Pasar el controlador al header
create_header(root, app)

# ✅ Mostrar listado inicial
app.listar_videojuegos()

root.mainloop()