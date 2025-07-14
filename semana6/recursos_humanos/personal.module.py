from datetime import date
from globals import DATA_PERSONAL

class Personal:

    def registrarPersonal(self):
        print("\n- Ingresar visita -\n")

        nombre = input("Ingrese un nombre: ")
        salario = input("Ingrese un salario: ")
        fechaIngreso = date.today().strftime("%Y-%m-%d")
        
        # Preparar el objeto Trabajador
        nuevoTrabajador = {
            'nombre': nombre,
            'salario': salario,
            'fecha_ingreso': fechaIngreso
        }
        print(nuevoTrabajador)
        
        # Agregar Nuevo Trabajador a la nomina actual

        DATA_PERSONAL.append(nuevoTrabajador)

    
    def leerNominaDePersonal(self):
        print("\n- Nómina de Trabajadores -\n")
        print(f"{'':>20}{'Nombre':<20}{'Salario':>10}{'Fecha de Ingreso':>20}")
        print(f"{'':>20}{'-'*50}")
        for trabajador in DATA_PERSONAL:
            print(f"{'':>20}{trabajador['nombre']:<20}{trabajador['salario']:>10}{trabajador['fecha_ingreso']:>20}")
        