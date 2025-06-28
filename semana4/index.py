import os

# Mensajes de la app
messageContinuar="\nPresiona Enter para continuar..."
messageInvalidOption="\nIngresa una opción válida"
messageAppClose = "\nCerrando aplicación...\nGracias por utilizar el programa"
messageSelectOption = "\nSelecciona una opción: "

# Datos de prueba
datos = [
    {"nombre": "Manuel", "sala": 1},
    {"nombre": "Camila", "sala": 2},
    {"nombre": "Pedro", "sala": 3},
    {"nombre": "Sofía", "sala": 2},
    {"nombre": "Antonio", "sala": 1},
    {"nombre": "Manuel", "sala": 3},
    {"nombre": "Pedro", "sala": 1},
    {"nombre": "Camila", "sala": 3},
    {"nombre": "Sofía", "sala": 1},
    {"nombre": "Antonio", "sala": 2},
    {"nombre": "Manuel", "sala": 2},
    {"nombre": "Sofía", "sala": 3},
    {"nombre": "Camila", "sala": 1},
    {"nombre": "Pedro", "sala": 2},
    {"nombre": "Antonio", "sala": 3}
]

# Clase Visitas
class Visitas:
    def __init__(self):
        self.registros = [] # Variable para guardar registros
        self.visitantes = set() # Conjunto de visitantes

    def agregarRegistro(self):
        print("\n- Ingresar visita -\n")
        # Solicitar al usuario que ingrese nombre válido
        try:
            inputNombre = input("Ingrese nombre de visitante: ")
            # Verificar que el ingreso no esté vacío
            if not inputNombre:
                print("El nombre no puede estar vacío")
                return
            # Eliminar espacios en inicio y fin del string
            inputNombre = inputNombre.strip()
            # Verificar que el nombre sólo contenga caracteres válidos
            if all(c.isalpha() or c.isspace() for c in inputNombre):
                nombre = inputNombre
            else:
                print("El nombre debe contener sólo letras y espacios") 
                return 
        except:
            print(messageInvalidOption)

        # Solicitar al usuario que ingrese número de sala válido
        try:
            inputSala = input("Ingrese número de sala: ")
            # Eliminar espacios en inicio y fin del string
            inputSala = inputSala.strip()
            # Verificar que el str sea un caracter numérico
            if inputSala.isdigit():
                # Verificar que el número esté entre 1 y 3
                if int(inputSala) >= 1 and int(inputSala) <= 3:
                    sala = int(inputSala)
                else:
                    print("El número de sala debe ser entre 1 y 3")
                    return 
            else:
                print("El número de sala debe ser un número")
                return 
            # Verificar que el número sea de acuerdo al número de salas
        except:
            print(messageInvalidOption)
        # Agregar registro a lista de registros      
        self.registros.append({"nombre":nombre, "sala": sala})
        # Agregar visitante al conjunto de visitantes automáticamente
        self._agregarVisitante(nombre)
    
    def leerRegistros(self):
        print("\n- Lista de Registros -\n")
        print(f"{'Nombre':<15} {'Sala':<5}")
        print("-" * 22)    
        for visita in self.registros:
            print(f"{visita['nombre']:<15} {str(visita['sala']):<5}")
    
    def listaUnicaVisitantes(self):
        print("\n- Lista Única de Visitantes -\n")
        print(f"{'Nombre':<15}")
        print("-" * 22)
        for visitante in sorted(self.visitantes):
            print(visitante)

    def _agregarVisitante(self, nombre):
        self.visitantes.add(nombre)

    def _cargaMasiva(self, datos):
        for dato in datos:
            self.registros.append(dato)
            # Agregar visitante al conjunto de visitantes automáticamente
            self._agregarVisitante(dato["nombre"])

class App():
    def __init__(self):
        self.visitas = Visitas()
        # Carga Inicial de Datos
        self.visitas._cargaMasiva(datos)

    # Crear run del programa
    def run(self):
        while True:
            self._limpiarConsola()

            print("--- Bienvenido al Programa ---")
            print("\n- Menu Principal -\n")
            print("1. Ingresar Visita")
            print("2. Lista de Registros")
            print("3. Lista Única de Visitantes")
            print("4. Salir")
            
            try:
                option = input(messageSelectOption)
                self._limpiarConsola()
                if(option == "1"):
                    self.visitas.agregarRegistro()
                elif(option == "2"):
                    self.visitas.leerRegistros()
                elif(option == "3"):
                    self.visitas.listaUnicaVisitantes()
                elif(option == "4"):
                    print(messageAppClose)
                    break
                else:
                    print(messageInvalidOption)
            except:
                print(messageInvalidOption)
            finally:
                input(messageContinuar)
    
    # Limpiar consola
    def _limpiarConsola(self):
        os.system("cls" if os.name == "nt" else "clear")

# Crea instancia de la clase App y arranca el programa con el método run()
app = App()
app.run()