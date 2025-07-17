import tkinter as tk
from tkinter import messagebox

def registrar_libro():
    """Función para recolectar todos los datos y mostrarlos en consola"""
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()
    genero = genero_var.get()
    estado = estado_var.get()
    copias = entry_copias.get()
    idioma = idioma_var.get()
    resumen = text_resumen.get("1.0", tk.END).strip()

    categorias_seleccionadas = [cat for cat, var in categorias_vars.items() if var.get() == 1]

    print("\n=== Detalles del libro registrado ===")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Año de publicación: {anio}")
    print(f"Género: {genero}")
    print(f"Categorías: {', '.join(categorias_seleccionadas)}")
    print(f"Estado: {estado}")
    print(f"Número de copias: {copias}")
    print(f"Idioma: {idioma}")
    print(f"Resumen:\n{resumen}")
    print("====================================\n")

    messagebox.showinfo("Registro", "📚 Libro registrado correctamente")

def limpiar_formulario():
    """Resetea todos los campos del formulario"""
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    genero_var.set("Ficción")
    estado_var.set("Disponible")
    entry_copias.delete(0, tk.END)
    idioma_var.set("Español")
    text_resumen.delete("1.0", tk.END)
    for var in categorias_vars.values():
        var.set(0)

def create_formulario(parent):
    # Ventana principal
    # parent = tk.Tk()
    # parent.title("Registro de Libros")
    # parent.geometry("600x700")

    # ===== Frame Detalles del libro =====
    frame_detalles = tk.LabelFrame(parent, text="Detalles del libro", padx=10, pady=10)
    frame_detalles.pack(fill="x", padx=10, pady=10)

    tk.Label(frame_detalles, text="Título:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_titulo = tk.Entry(frame_detalles)
    entry_titulo.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

    tk.Label(frame_detalles, text="Autor:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_autor = tk.Entry(frame_detalles)
    entry_autor.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

    tk.Label(frame_detalles, text="Año de publicación:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entry_anio = tk.Entry(frame_detalles)
    entry_anio.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

    frame_detalles.columnconfigure(1, weight=1)

    # ===== Frame Género y Categoría =====
    frame_genero_cat = tk.LabelFrame(parent, text="Género y Categoría", padx=10, pady=10)
    frame_genero_cat.pack(fill="x", padx=10, pady=10)

    genero_var = tk.StringVar(value="Ficción")
    tk.Label(frame_genero_cat, text="Género:").grid(row=0, column=0, sticky="w", padx=5)
    tk.Radiobutton(frame_genero_cat, text="Ficción", variable=genero_var, value="Ficción").grid(row=0, column=1, sticky="w")
    tk.Radiobutton(frame_genero_cat, text="No Ficción", variable=genero_var, value="No Ficción").grid(row=0, column=2, sticky="w")

    tk.Label(frame_genero_cat, text="Categorías:").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
    categorias = ["Novela", "Ciencia", "Historia", "Tecnología", "Arte", ]
    categorias_vars = {}
    for i, cat in enumerate(categorias):
        var = tk.IntVar()
        categorias_vars[cat] = var
        tk.Checkbutton(frame_genero_cat, text=cat, variable=var).grid(row=1, column=i+1, sticky="w")

    # ===== Frame Estado de disponibilidad =====
    frame_estado = tk.LabelFrame(parent, text="Estado de disponibilidad", padx=10, pady=10)
    frame_estado.pack(fill="x", padx=10, pady=10)

    estado_var = tk.StringVar(value="Disponible")
    tk.Radiobutton(frame_estado, text="Disponible", variable=estado_var, value="Disponible").pack(side="left", padx=10)
    tk.Radiobutton(frame_estado, text="Prestado", variable=estado_var, value="Prestado").pack(side="left", padx=10)

    # ===== Frame Número de copias =====
    frame_copias = tk.LabelFrame(parent, text="Número de copias", padx=10, pady=10)
    frame_copias.pack(fill="x", padx=10, pady=10)

    tk.Label(frame_copias, text="Copias disponibles:").grid(row=0, column=0, sticky="w", padx=5)
    entry_copias = tk.Entry(frame_copias)
    entry_copias.grid(row=0, column=1, sticky="ew", padx=5)
    frame_copias.columnconfigure(1, weight=1)

    # ===== Frame Idioma =====
    frame_idioma = tk.LabelFrame(parent, text="Idioma del libro", padx=10, pady=10)
    frame_idioma.pack(fill="x", padx=10, pady=10)

    idioma_var = tk.StringVar(value="Español")
    idiomas_disponibles = ["Español", "Inglés", "Francés", "Alemán"]
    tk.Label(frame_idioma, text="Seleccione idioma:").pack(side="left", padx=10)
    tk.OptionMenu(frame_idioma, idioma_var, *idiomas_disponibles).pack(side="left")

    # ===== Frame Resumen del libro =====
    frame_resumen = tk.LabelFrame(parent, text="Resumen del libro", padx=10, pady=10)
    frame_resumen.pack(fill="both", expand=False, padx=10, pady=10)

    tk.Label(frame_resumen, text="Resumen:").pack(anchor="w")
    text_resumen = tk.Text(frame_resumen, height=4, wrap="word")
    text_resumen.pack(fill="both", expand=False, pady=5)

    # ===== Frame Botones de acción =====
    frame_botones = tk.Frame(parent, pady=10)
    frame_botones.pack()

    btn_registrar = tk.Button(frame_botones, text="✅ Registrar Libro", command=registrar_libro)
    btn_registrar.grid(row=0, column=0, padx=10)

    btn_limpiar = tk.Button(frame_botones, text="🗑 Limpiar", command=limpiar_formulario)
    btn_limpiar.grid(row=0, column=1, padx=10)

    # parent.mainloop()
