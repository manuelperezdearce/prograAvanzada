import tkinter as tk
from tkinter import ttk

class PacienteView:
    def __init__(self):
        self.on_guardar_callback = None
        self.tree = None  # Guardamos el Treeview aquí

    def mostrar_Pacientes(self, Pacientes, root):
      
        if not Pacientes:
            return
        columnas = list(Pacientes[0].keys())

        # Si el Treeview no existe, crearlo solo la primera vez
        if self.tree is None:
            self.tree = ttk.Treeview(
                root,
                columns=columnas,
                show="headings"
            )
        # Crear dinamicamente los encabezados de cada columna
            for columna in columnas:
                self.tree.heading(f"{columna}", text=f"{columna.replace("_", " ").capitalize()}")
            self.tree.pack(fill="both", expand=True)

        # # Limpiar las filas anteriores
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        # # Insertar nuevas filas
        for Paciente in Pacientes:
            self.tree.insert(
                "",
                "end",
                values=tuple(Paciente[col] for col in columnas)
            )

    def agregar_Paciente(self, Paciente=None):
        ventana_formulario_insert = tk.Toplevel()
        ventana_formulario_insert.title("Editar Paciente" if Paciente else "Agregar Paciente")
        ventana_formulario_insert.geometry("300x350")

        form_frame = tk.LabelFrame(ventana_formulario_insert, text="Datos del Paciente")
        form_frame.pack(expand=True, padx=10, fill="both", pady=10)

        tk.Label(form_frame, text="Nombre:").pack()
        entry_nombre = tk.Entry(form_frame)
        entry_nombre.pack()
        if Paciente:
            entry_nombre.insert(0, Paciente["nombre"])

        tk.Label(form_frame, text="Género:").pack()
        genero_var = tk.StringVar()
        combobox_genero = ttk.Combobox(form_frame, textvariable=genero_var, state="readonly")
        combobox_genero['values'] = ("Masculino", "Femenino", "Otro")
        combobox_genero.pack()
        if Paciente:
            combobox_genero.set(Paciente["genero"])

        tk.Label(form_frame, text="Edad:").pack()
        edad_var = tk.StringVar()
        spinbox_edad = tk.Spinbox(form_frame, from_=0, to=120, textvariable=edad_var, width=5)
        spinbox_edad.pack()

        if Paciente:
            edad_var.set(Paciente["edad"])

        tk.Label(form_frame, text="Contacto:").pack()
        entry_contacto = tk.Entry(form_frame)
        entry_contacto.pack()
        if Paciente:
            entry_contacto.insert(0, Paciente["contacto"])

        tk.Label(form_frame, text="Historial Médico:").pack()
        text_historial_medico = tk.Text(form_frame, height=5, width=30)
        text_historial_medico.pack()

        if Paciente:
            text_historial_medico.insert("1.0", Paciente["historial_medico"])

        def guardar():
            nombre = entry_nombre.get()
            
            genero = genero_var.get()
            contacto = entry_contacto.get()
            edad = int(edad_var.get())
            historial_medico = text_historial_medico.get("1.0", "end").strip()

            if Paciente:
                if self.on_editar_callback:
                    self.on_editar_callback(Paciente["id"], nombre, edad, genero, historial_medico, contacto)
            else:
                if self.on_guardar_callback:
                    self.on_guardar_callback(nombre, edad, genero, historial_medico, contacto)

            ventana_formulario_insert.destroy()

        tk.Button(form_frame, text="Guardar", command=guardar).pack(pady=10)


    def get_selected_item(self):
        if self.tree:
            seleccion = self.tree.selection()
            if seleccion:
                valores = self.tree.item(seleccion[0], "values")
                return valores[0]