import tkinter as tk
from controller.paciente_controller import PacienteController
from view.header import create_header

root = tk.Tk()
root.title("Gestión de Pacientes")
# root.geometry("800x500")

# Crear controlador principal
app = PacienteController(root)

# Pasar el controlador al header
create_header(root, app)

# Mostrar listado inicial
app.listar_Pacientes()

root.mainloop()