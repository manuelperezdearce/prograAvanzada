# Python - index.py

import os

def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")

def calcularPrecioLicencia(cantidad):
    precioBase = 50
    if cantidad > 0 and cantidad < 3:
        return precioBase
    elif cantidad >= 3 and cantidad < 5:
        return precioBase * (1 - 0.2)  # 20% de descuento
    elif cantidad >= 5:
        return precioBase * (1 - 0.3)  # 30% de descuento
    else:
        return None  # Valor inválido


def opcion1():
    while True:
        limpiarConsola()
        print("-- Calcular descuento en compras de software --\n")
        print("1. Ingresar un valor")
        print("2. Volver al menú principal\n")
        option = input("Ingrese una opción para continuar: ")

        if option == "1":
            try:
                qLicencias = int(input("Ingrese cantidad de licencias a comprar: "))
                precioLicencia = calcularPrecioLicencia(qLicencias)

                if precioLicencia is None:
                    print("Error: Ingrese una cantidad mayor a 0")
                else:
                    precioTotal = qLicencias * precioLicencia
                    print(f"\nPrecio unitario: ${precioLicencia}")
                    print(f"El valor total de la compra es de: ${precioTotal}")

            except ValueError:
                print("Error: Ingrese un número entero válido.")
            
            input("\nPresione Enter para continuar...")  # Pausa antes de volver al menú

        elif option == "2":
            return  # salir de la función y volver al menú principal
        else:
            print("Opción inválida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")
        
def opcion2():
    while True:
        limpiarConsola()
        print("-- Calcular volumen de una esfera --\n")
        print("1. Ingresar un valor")
        print("2. Volver al menú principal\n")
        option = input("Ingrese una opción para continuar: ")

        if option == "1":
            try:
                radio = float(input("Ingrese el radio de la esfera: "))
                if radio <= 0:
                    print("Error: el radio debe ser mayor que cero.")
                else:
                    pi = 3.1416
                    volumen = round((4/3) * pi * radio**3, 3)
                    print(f"\nEl volumen de la esfera es: {volumen}")
            except ValueError:
                print("Error: debe ingresar un número válido.")
            input("\nPresione Enter para continuar...")  # Pausa antes de volver al menú
        elif option == "2":
            return  # vuelve al menú principal
        else:
            print("Opción inválida. Intente nuevamente.")
            input("Presione Enter para continuar...")


def run():
    while True:
        
        limpiarConsola()

        print("\n --- Bienvenido a MyPro ---\n")
        print("1. Calcular descuento en compras de software")
        print("2. Calcular el volumen de una esfera")
        print("3. Salir")
        
        option=input("\nPara continuar, selecciona una opción: \n")

        if option == "1":
            opcion1()
        elif option == "2":
            opcion2()
        elif option == "3":
            print("\nCerrando programa...\n")
            break
        else:
            print("Ingrese un valor correcto")
run()