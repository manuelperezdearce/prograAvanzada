# Python

import os

def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")

class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        limpiarConsola()
        print("\n-- Inventario Actual --\n")
        for producto in self.productos:
            print(f"{producto.nombre} ----- Cantidad: {producto.stock}")
        input("\nPresione Enter para continuar...")

    def agregar_stock(self):
        while True:
            limpiarConsola()
            print("\n-- Agregar Stock --\n")
            for idx, prod in enumerate(self.productos, start=1):
                print(f"{idx}. {prod.nombre}")
            print(f"\n{len(self.productos)+1}. Volver atrás")

            try:
                opcion = int(input("\nSeleccione un producto: "))
                if opcion == len(self.productos) + 1:
                    break
                if 1 <= opcion <= len(self.productos):
                    cantidad = int(input("Cantidad a añadir: "))
                    if cantidad >= 0:
                        self.productos[opcion - 1].agregar_stock(cantidad)
                        print("\nStock actualizado correctamente.")
                    else:
                        print("Cantidad inválida.")
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Entrada inválida.")
            input("\nPresione Enter para continuar...")

    def registrar_venta(self):
        while True:
            limpiarConsola()
            print("\n-- Registrar Venta --\n")
            for idx, prod in enumerate(self.productos, start=1):
                print(f"{idx}. {prod.nombre} - Stock: {prod.stock}")
            print(f"\n{len(self.productos)+1}. Volver atrás")

            try:
                opcion = int(input("\nSeleccione un producto: "))
                if opcion == len(self.productos) + 1:
                    break
                if 1 <= opcion <= len(self.productos):
                    cantidad = int(input("Cantidad vendida: "))
                    producto = self.productos[opcion - 1]
                    if cantidad < 0:
                        print("Cantidad no puede ser negativa.")
                    elif producto.vender(cantidad):
                        print(f"\nVenta registrada. Nuevo stock: {producto.stock}")
                    else:
                        print("Stock insuficiente.")
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Entrada inválida.")
            input("\nPresione Enter para continuar...")

def run():
    inventario = Inventario()
    inventario.agregar_producto(Producto("Patata", 51))
    inventario.agregar_producto(Producto("Lechuga", 15))
    inventario.agregar_producto(Producto("Manzana", 35))
    inventario.agregar_producto(Producto("Naranja", 45))

    while True:
        limpiarConsola()
        print("\n--- 🍅🥔 Bienvenido a Ventas Frescura Natural 🍎🍊 ---\n")
        print("1. Ver inventario")
        print("2. Agregar stock")
        print("3. Registrar venta")
        print("4. Salir")

        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                inventario.mostrar_productos()
            elif opcion == 2:
                inventario.agregar_stock()
            elif opcion == 3:
                inventario.registrar_venta()
            elif opcion == 4:
                print("\nGracias por usar el sistema. ¡Hasta pronto!\n")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida.")
        input("\nPresione Enter para continuar...")

run()