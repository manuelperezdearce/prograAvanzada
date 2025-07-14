from globals import DATA_PERSONAL as DATA
from datetime import datetime, date

class Remuneraciones:

    def __init__(self):
        print("Hola! nueva instancia")
        # Crear una lista para guardar la data de beneficios y luego renderizar.
        self.beneficios = []
        # Traer DATA_PERSONAL y guardar en una variable
        DATA_PERSONAL = DATA
        # Recorrer DATA_PERSONAL y agregar parámetros "antiguedad" y "beneficio"
        for persona in DATA_PERSONAL:
            persona["antiguedad"]=""
            persona["beneficio"]=""
            self._calcularAntiguedad(persona)
            self._calcularBeneficios(persona)
        self.beneficios = DATA_PERSONAL

    def tablaDeBeneficios(self):
        print("\n" + "-"*80)
        print(f"{'Tabla de Beneficios':^80}")
        print("-"*80)
        print(f"{'Nombre':^20}{'Fecha de Ingreso':^20}{'Antiguedad':^15}{'Beneficio':^25}")
        print("-"*80)

        for persona in self.beneficios:
            print(f"{persona['nombre']:^20}{persona['fecha_ingreso']:^20}{str(persona['antiguedad']):^15}{persona['beneficio']:^25}")

        print("-"*80)

    def _calcularAntiguedad(self, persona):
        print("Calcular Antiguedad")
        hoy = date.today()
        # Convertir string a date
        fecha_ingreso = datetime.strptime(persona["fecha_ingreso"], "%Y-%m-%d").date()
        dias = (hoy - fecha_ingreso).days
        antiguedad = dias // 365
        persona['antiguedad'] = antiguedad

    def _calcularBeneficios(self, persona):
        print("Calcular Beneficio")
        if persona['antiguedad'] >= 5:
            persona['beneficio'] = "Bono Anual"
            return
        if persona['antiguedad'] >= 3:
            persona['beneficio'] = "+5 días de Vacaciones"
            return



