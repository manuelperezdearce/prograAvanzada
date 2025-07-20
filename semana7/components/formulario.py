import tkinter as tk
from tkinter import messagebox


class FormularioLibros:
    def __init__(self, parent):
        self.parent = parent

        # ===== Frame Detalles del libro =====
        self.frame_detalles = tk.LabelFrame(self.parent, text="Detalles del libro", padx=10, pady=10)
        self.frame_detalles.pack(fill="x", padx=10, pady=10)

        tk.Label(self.frame_detalles, text="Título:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_titulo = tk.Entry(self.frame_detalles)
        self.entry_titulo.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(self.frame_detalles, text="Autor:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_autor = tk.Entry(self.frame_detalles)
        self.entry_autor.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(self.frame_detalles, text="Año de publicación:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_anio = tk.Entry(self.frame_detalles)
        self.entry_anio.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.frame_detalles.columnconfigure(1, weight=1)

        # ===== Frame Género y Categoría =====
        self.frame_genero_cat = tk.LabelFrame(self.parent, text="Género y Categoría", padx=10, pady=10)
        self.frame_genero_cat.pack(fill="x", padx=10, pady=10)

        self.genero_var = tk.StringVar(value="Ficción")
        tk.Label(self.frame_genero_cat, text="Género:").grid(row=0, column=0, sticky="w", padx=5)
        tk.Radiobutton(self.frame_genero_cat, text="Ficción", variable=self.genero_var, value="Ficción").grid(row=0, column=1, sticky="w")
        tk.Radiobutton(self.frame_genero_cat, text="No Ficción", variable=self.genero_var, value="No Ficción").grid(row=0, column=2, sticky="w")

        tk.Label(self.frame_genero_cat, text="Categorías:").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        categorias = ["Novela", "Ciencia", "Historia", "Tecnología", "Arte"]
        self.categorias_vars = {}
        for i, cat in enumerate(categorias):
            var = tk.IntVar()
            self.categorias_vars[cat] = var
            tk.Checkbutton(self.frame_genero_cat, text=cat, variable=var).grid(row=1, column=i+1, sticky="w")

        # ===== Frame Estado de disponibilidad =====
        self.frame_estado = tk.LabelFrame(self.parent, text="Estado de disponibilidad", padx=10, pady=10)
        self.frame_estado.pack(fill="x", padx=10, pady=10)

        self.estado_var = tk.StringVar(value="Disponible")
        tk.Radiobutton(self.frame_estado, text="Disponible", variable=self.estado_var, value="Disponible").pack(side="left", padx=10)
        tk.Radiobutton(self.frame_estado, text="Prestado", variable=self.estado_var, value="Prestado").pack(side="left", padx=10)

        # ===== Frame Número de copias =====
        self.frame_copias = tk.LabelFrame(self.parent, text="Número de copias", padx=10, pady=10)
        self.frame_copias.pack(fill="x", padx=10, pady=10)

        tk.Label(self.frame_copias, text="Copias disponibles:").grid(row=0, column=0, sticky="w", padx=5)
        self.entry_copias = tk.Entry(self.frame_copias)
        self.entry_copias.grid(row=0, column=1, sticky="ew", padx=5)
        self.frame_copias.columnconfigure(1, weight=1)

        # ===== Frame Idioma =====
        self.frame_idioma = tk.LabelFrame(self.parent, text="Idioma del libro", padx=10, pady=10)
        self.frame_idioma.pack(fill="x", padx=10, pady=10)

        self.idioma_var = tk.StringVar(value="Español")
        idiomas_disponibles = ["Español", "Inglés", "Francés", "Alemán"]
        tk.Label(self.frame_idioma, text="Seleccione idioma:").pack(side="left", padx=10)
        tk.OptionMenu(self.frame_idioma, self.idioma_var, *idiomas_disponibles).pack(side="left")

        # ===== Frame Resumen del libro =====
        self.frame_resumen = tk.LabelFrame(self.parent, text="Resumen del libro", padx=10, pady=10)
        self.frame_resumen.pack(fill="both", expand=False, padx=10, pady=10)

        tk.Label(self.frame_resumen, text="Resumen:").pack(anchor="w")
        self.text_resumen = tk.Text(self.frame_resumen, height=4, wrap="word")
        self.text_resumen.pack(fill="both", expand=False, pady=5)

        # ===== Frame Botones de acción =====
        self.frame_botones = tk.Frame(self.parent, pady=10)
        self.frame_botones.pack()

        btn_registrar = tk.Button(self.frame_botones, text="✅ Registrar Libro", command=self.registrar_libro)
        btn_registrar.grid(row=0, column=0, padx=10)

        btn_limpiar = tk.Button(self.frame_botones, text="🗑 Limpiar", command=self.limpiar_formulario)
        btn_limpiar.grid(row=0, column=1, padx=10)

    def registrar_libro(self):
        """Función para recolectar todos los datos y mostrarlos en consola"""
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        anio = self.entry_anio.get()
        genero = self.genero_var.get()
        estado = self.estado_var.get()
        copias = self.entry_copias.get()
        idioma = self.idioma_var.get()
        resumen = self.text_resumen.get("1.0", tk.END).strip()

        categorias_seleccionadas = [cat for cat, var in self.categorias_vars.items() if var.get() == 1]

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

    def limpiar_formulario(self):
        """Resetea todos los campos del formulario"""
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_anio.delete(0, tk.END)
        self.genero_var.set("Ficción")
        self.estado_var.set("Disponible")
        self.entry_copias.delete(0, tk.END)
        self.idioma_var.set("Español")
        self.text_resumen.delete("1.0", tk.END)
        for var in self.categorias_vars.values():
            var.set(0)