# La tienda de llantas “Rueda Fácil” necesita un programa de facturación por compras de llantas. Se
# requiere calcular el monto a pagar por cada cliente en función de la cantidad de llantas compradas.
# El programa solicita al usuario la cantidad de clientes y, para cada cliente, registra la cantidad de
# llantas adquiridas para calcular el monto total de la compra.
# En este orden de ideas, se debe determinar el precio unitario de las llantas en base a la cantidad
# adquirida según la siguiente lógica:
# • Si se compran menos de 5 llantas, el precio unitario es de 35 000 pesos.
# • Si se compran entre 5 y 10 llantas (ambos inclusive), el precio unitario es de 40 000 pesos.
# • Para más de 10 llantas, el precio unitario es de 45 000 pesos.
# El problema está enfocado en la automatización del proceso de facturación para la tienda, brindando
# una solución sencilla y rápida para calcular el monto a pagar por cada cliente según la cantidad de
# llantas compradas, aplicando diferentes tarifas de acuerdo a la cantidad adquirida.

# 1. Explica el uso de la conversión de datos, operadores y los tipos de datos en la programación en
# Python. Ejemplifica usando el problema de la tienda de llantas.
# 2.Describe a nivel teórico la aplicación práctica del control de flujo en Python, específicamente los
# bucles. Indica además cuáles fueron las estructuras que utilizaste en la solución de la tienda.
# 3. Construye un programa en Python que solucione el problema planteado por la tienda de llantas
# “Rueda Fácil”.

cantidad = int(input("Ingrese cantidad de llantas: "))

# semana1.py

# Lista de compras realizadas por clientes
compras = [
    {"name": "cliente1", "cantidadLlantas": 5},
    {"name": "cliente2", "cantidadLlantas": 3},
    {"name": "cliente3", "cantidadLlantas": 8},
    {"name": "cliente4", "cantidadLlantas": 11},
    {"name": "cliente5", "cantidadLlantas": 6}
]

# Función para calcular el precio unitario según cantidad de llantas compradas
def calcularPrecioUnitario(cantidad):
    if cantidad < 5:
        return 35000
    elif cantidad <= 10:
        return 40000
    else:
        return 45000

# Función para calcular y mostrar el total de todas las compras
def calcularTotalCompras():
    totalCompras = 0
    print("----- FACTURACIÓN Rueda Fácil -----\n")
    for compra in compras:
        nombre = compra["name"]
        cantidad = compra["cantidadLlantas"]
        precioUnitario = calcularPrecioUnitario(cantidad)
        subtotal = cantidad * precioUnitario
        totalCompras += subtotal
        print(f"Cliente: {nombre}\n  Cantidad de llantas: {cantidad}\n  Precio unitario: ${precioUnitario}\n  Subtotal: ${subtotal}\n")

    print(f"TOTAL GENERAL DE COMPRAS: ${totalCompras}")

# Ejecutar la función principal
calcularTotalCompras()