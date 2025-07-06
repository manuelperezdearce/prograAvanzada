

class Trabajador:
    
    # __name__ = "Personal"


    def registrarTrabajador(self):
        print("\n- Ingresar visita -\n")
        
    
    def leerNominaDeTrabajadores(self):
        print("\n- Lista de Registros -\n")
        print(f"{'Nombre':<15} {'Sala':<5}")
        print("-" * 22)    
        for visita in self.registros:
            print(f"{visita['nombre']:<15} {str(visita['sala']):<5}")