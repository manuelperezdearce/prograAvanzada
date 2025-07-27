import tkinter as tk
from tkinter import ttk

class VideojuegoView:
    def __init__(self):
        self.on_guardar_callback = None
        self.tree = None  # Guardamos el Treeview aquí

    def mostrar_videojuegos(self, videojuegos, root):
        # Si el Treeview no existe, crearlo solo la primera vez
        if self.tree is None:
            self.tree = ttk.Treeview(
                root,
                columns=("id", "titulo", "genero", "clasificacion", "plataforma"),
                show="headings"
            )
            self.tree.heading("id", text="ID")
            self.tree.heading("titulo", text="Título")
            self.tree.heading("genero", text="Género")
            self.tree.heading("clasificacion", text="Clasificación")
            self.tree.heading("plataforma", text="Plataforma")
            self.tree.pack(fill="both", expand=True)

        # Limpiar las filas anteriores
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        # Insertar nuevas filas
        for videojuego in videojuegos:
            self.tree.insert(
                "",
                "end",
                values=(
                    videojuego["id"],
                    videojuego["titulo"],
                    videojuego["genero"],
                    videojuego["clasificacion"],
                    videojuego["plataforma"]
                )
            )

    def agregar_videojuego(self):
        # Crear una ventana secundaria (modal)
        ventana_formulario_insert = tk.Toplevel()
        ventana_formulario_insert.title("Agregar Videojuego")
        ventana_formulario_insert.geometry("300x350")

        form_frame = tk.LabelFrame(ventana_formulario_insert, text="Datos del Videojuego")
        form_frame.pack(expand=True, padx=10, fill="both", pady=10)

        tk.Label(form_frame, text="Título:").pack()
        entry_titulo = tk.Entry(form_frame)
        entry_titulo.pack()

        tk.Label(form_frame, text="Género:").pack()
        entry_genero = tk.Entry(form_frame)
        entry_genero.pack()

        tk.Label(form_frame, text="Clasificación:").pack()
        entry_clasificacion = tk.Entry(form_frame)
        entry_clasificacion.pack()

        tk.Label(form_frame, text="Plataforma:").pack()
        entry_plataforma = tk.Entry(form_frame)
        entry_plataforma.pack()

        def guardar():
            titulo = entry_titulo.get()
            genero = entry_genero.get()
            clasificacion = entry_clasificacion.get()
            plataforma = entry_plataforma.get()

            # Si hay un callback definido, avisamos al controlador
            if self.on_guardar_callback:
                self.on_guardar_callback(titulo, genero, clasificacion, plataforma)

            ventana_formulario_insert.destroy()

        tk.Button(form_frame, text="Guardar", command=guardar).pack(pady=10)
