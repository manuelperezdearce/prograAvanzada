import os
import importlib.util
import inspect
import sys

from .messages import (
    messageAppClose,
    messageContinuar,
    messageInvalidOption,
    messageSelectOption,
)

class App():
    def __init__(self):
        self.menu = []
        self.current_path = os.getcwd()

    def run(self):
        while True:
            self._getMenu()
            while True:
                self._limpiarConsola()
                self._renderMenu()
                if self._readUserOption():
                    return

    def _readUserOption(self):
        userOption = input(messageSelectOption)

        try:
            userOption = int(userOption)
        except ValueError:
            print("Opción no válida: debe ser un número.")
            input("Presione Enter para continuar.")
            return False

        # Opción salir
        if userOption == len(self.menu) + 2:
            print(messageAppClose)
            input("Presione Enter para cerrar.")
            sys.exit()

        # Opción volver atrás
        if userOption == len(self.menu) + 1:
            return True  # <-- Solo retorna, no modifica el path

        # Buscar opción
        item = None
        for ele in self.menu:
            if ele["id"] == userOption:
                item = ele
                break

        if item:
            if item["type"] == "package":
                nuevo_path = os.path.join(self.current_path, item["dirName"])
                nueva_app = App()
                nueva_app.current_path = nuevo_path
                nueva_app.run()
                return False
            elif item["type"] == "module":
                self._handleModule(item)
                return False
        else:
            print("No se encontró la opción.")

        input("Presione Enter para continuar.")
        return False

    def _getMenu(self):
        self.menu.clear()
        listdir = os.listdir(self.current_path)
        count = 1

        for fname in listdir:
            parts = fname.split(".")

            if len(parts) < 2:
                continue

            nombre_base = parts[0]
            extension = parts[-1]

            if len(parts) >= 3:
                anterior = parts[-2]
            else:
                anterior = ""

            if nombre_base in ("index", "main", "test"):
                continue

            es_paquete = extension == "package"
            es_modulo_valido = extension == "py" and anterior == "module"

            if es_paquete or es_modulo_valido:
                menu_name = nombre_base.capitalize()

                if extension == "py":
                    dirTYPE = "module"
                    dirName = nombre_base + ".module"
                if extension == "package":
                    dirName = nombre_base + ".package"
                    dirTYPE = "package"

                self.menu.append({
                    "id": count,
                    "name": menu_name,
                    "dirName": dirName,
                    "extension": extension,
                    "type": dirTYPE
                })

                count += 1

    def _renderMenu(self):
        print(f"Ruta actual: {self.current_path}\n")
        for option in self.menu:
            print(f"{option['id']:>3}. {option['name']:<20} {option['type']:<10}")
        print(f"\n{len(self.menu)+1:>3}. Volver atrás")
        print(f"{len(self.menu)+2:>3}. Salir\n")

    def _handleModule(self, item):
        ruta_completa = os.path.join(self.current_path, f"{item['dirName']}.{item['extension']}")

        spec = importlib.util.spec_from_file_location(item["dirName"], ruta_completa)
        modulo = importlib.util.module_from_spec(spec)
        sys.modules[item["dirName"]] = modulo
        spec.loader.exec_module(modulo)

        # Obtener clases
        clases = [m for _, m in inspect.getmembers(modulo, inspect.isclass)]
        if not clases:
            print("No se encontraron clases en este módulo.")
            input("Presione Enter para continuar.")
            return

        while True:
            self._limpiarConsola()
            print(f"-- Clases en {item['name']} --\n")
            for idx, clase in enumerate(clases, start=1):
                print(f"{idx}. {clase.__name__}")
            print(f"{len(clases)+1}. Volver al menú anterior")

            opcion = input("\nSeleccione una clase: ")
            try:
                opcion = int(opcion)
            except ValueError:
                continue

            if opcion == len(clases)+1:
                return

            clase_seleccionada = clases[opcion-1]
            metodos = [
                (nombre, funcion)
                for nombre, funcion in inspect.getmembers(clase_seleccionada, inspect.isfunction)
                if not nombre.startswith("_")
            ]

            if not metodos:
                print("No se encontraron métodos públicos en esta clase.")
                input("Enter para continuar...")
                return

            while True:
                self._limpiarConsola()
                print(f"-- Métodos de {clase_seleccionada.__name__} --\n")
                for idx, (nombre, _) in enumerate(metodos, start=1):
                    print(f"{idx}. {nombre}")
                print(f"{len(metodos)+1}. Volver al menú anterior")

                opcion_m = input("\nSeleccione un método: ")
                try:
                    opcion_m = int(opcion_m)
                except ValueError:
                    continue

                if opcion_m == len(metodos)+1:
                    break

                metodo = metodos[opcion_m-1][1]
                instancia = clase_seleccionada()
                metodo(instancia)
                input("Presione Enter para continuar.")

    def _limpiarConsola(self):
        os.system("cls" if os.name == "nt" else "clear")