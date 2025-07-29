import tkinter as tk

def create_header(parent, controller):
    header = tk.Frame(parent, bg="navy", pady=20)
    header.pack(fill="x")

    # Logo o título
    tk.Label(header, text="GameShark Storage", fg="white", bg="navy", font=("Arial", 14, "bold")).pack(side="left", padx=10)

    # Botones de acción
    tk.Button(header, text="Eliminar", command=controller.eliminar_videojuego).pack(side="right", padx=5)
    tk.Button(header, text="Editar", command=controller.editar_videojuego).pack(side="right", padx=5)
    tk.Button(header, text="Agregar", command=controller.agregar_videojuego).pack(side="right", padx=5)

    return header