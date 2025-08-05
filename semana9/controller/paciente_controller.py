from model.paciente_model import PacienteModel
from view.paciente_view import PacienteView

class PacienteController:
    def __init__(self, root):
        self.modelo = PacienteModel()
        self.view = PacienteView()
        self.root = root

         # Cuando la vista llame al callback, ejecutará este método
        self.view.on_guardar_callback = self.guardar_Paciente

    def listar_Pacientes(self):
        Pacientes = self.modelo.readAll()
        self.view.mostrar_Pacientes(Pacientes, self.root)

    def agregar_Paciente(self):
        self.view.agregar_Paciente()
        

    def guardar_Paciente(self, nombre, edad, genero, historial_medico, contacto):
        self.modelo.insert(nombre, edad, genero, historial_medico, contacto)
        self.listar_Pacientes()
    
    def editar_Paciente(self):
        Paciente_id = self.view.get_selected_item()

        if not Paciente_id:
            print("⚠️ No hay ningún Paciente seleccionado.")
            return

        # Obtener los datos del Paciente desde la BD
        Paciente = self.modelo.find_by_id(Paciente_id)

        if Paciente:
            # Pasar los datos al formulario en modo edición
            self.view.on_editar_callback = self.actualizar_Paciente
            self.view.agregar_Paciente(Paciente)
        else:
            print("❌ No se encontró el Paciente con ID:", Paciente_id)

    def actualizar_Paciente(self, id_Paciente, nombre, edad, genero, historial_medico, contacto):
        print("Actualizando Paciente ID", id_Paciente)
        self.modelo.update(id_Paciente, nombre, edad, genero, historial_medico, contacto)
        self.listar_Pacientes()

    def eliminar_Paciente(self):
        Paciente_id = self.view.get_selected_item()
        self.modelo.delete(Paciente_id)
        self.listar_Pacientes()