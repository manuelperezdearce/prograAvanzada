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
            input(messageContinuar)
            return False

        if userOption == len(self.menu) + 2:
            print(messageAppClose)
            input("Presione Enter para cerrar.")
            sys.exit()

        if userOption == len(self.menu) + 1:
            return True

        item = next((ele for ele in self.menu if ele["id"] == userOption), None)

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

        input(messageContinuar)
        return False

    def _getMenu(self):
        self.menu.clear()
        listdir = os.listdir(self.current_path)
        count = 1

        for fname in listdir:
            ruta_completa = os.path.join(self.current_path, fname)

            # Saltar la carpeta app aunque tenga __init__.py
            if fname == "app":
                continue

            # Detectar paquetes (carpeta con __init__.py)
            if os.path.isdir(ruta_completa) and "__init__.py" in os.listdir(ruta_completa):
                self.menu.append({
                    "id": count,
                    "name": fname.capitalize(),
                    "dirName": fname,
                    "extension": "",
                    "type": "package"
                })
                count += 1

            # Detectar módulos .module.py
            elif fname.endswith(".module.py"):
                nombre_base = fname[:-10]
                self.menu.append({
                    "id": count,
                    "name": nombre_base.capitalize(),
                    "dirName": nombre_base,
                    "extension": "module.py",
                    "type": "module"
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

        # Filtrar solo las clases definidas en este módulo
        clases = [
            cls for _, cls in inspect.getmembers(modulo, inspect.isclass)
            if cls.__module__ == modulo.__name__
        ]

        if not clases:
            print("No se encontraron clases propias en este módulo.")
            input(messageContinuar)
            return

        clase_seleccionada = clases[0]  # asumimos solo un Manager por archivo *.module.py

        metodos = [
            (nombre, funcion)
            for nombre, funcion in inspect.getmembers(clase_seleccionada, inspect.isfunction)
            if not nombre.startswith("_")
        ]

        if not metodos:
            print("No se encontraron métodos públicos en esta clase.")
            input(messageContinuar)
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
            input(messageContinuar)

    def _limpiarConsola(self):
        os.system("cls" if os.name == "nt" else "clear")
