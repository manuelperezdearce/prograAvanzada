import tkinter as tk

# Importar componentes
from components.header import create_header
from components.formulario import create_formulario


def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()

    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi ventana Principal")
# Llamamos la función con las dimensiones deseadas
centrar_ventana(ventana, ancho=800, alto=800)

header=create_header(ventana)
formulario = create_formulario(ventana)

ventana.mainloop()