# components/header.py
import tkinter as tk

def create_header(parent, on_nav_callback=None):
    """
    Crea un Header (barra de navegación) y lo devuelve.
    parent: contenedor donde se agrega (puede ser la ventana principal o un frame)
    on_nav_callback: función opcional para manejar la navegación
    """
    header = tk.Frame(parent, bg="navy", pady=20)
    header.pack(fill="x")  # Ocupa todo el ancho

    # Logo o título
    tk.Label(header, text="Mi Aplicación", fg="white", bg="navy", font=("Arial", 14, "bold")).pack(side="left", padx=10)

    # Botones de navegación
    
    btn_home = tk.Button(header, text="Inicio", command=lambda: on_nav_callback("home") if on_nav_callback else None)
    btn_home.pack(side="right", padx=5)

    btn_about = tk.Button(header, text="Acerca", command=lambda: on_nav_callback("about") if on_nav_callback else None)
    btn_about.pack(side="right", padx=5)

    return header