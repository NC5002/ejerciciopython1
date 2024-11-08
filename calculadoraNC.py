"""Ejercicio Calculadora NC"""
import math

# Definición de funciones para operaciones


def sumar(x, y):
    return x + y


def restar(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero"


def potencia(x, y):
    return x ** y


def modulo(x, y):
    return x % y


def seno(x):
    return math.sin(math.radians(x))


def coseno(x):
    return math.cos(math.radians(x))


def tangente(x):
    return math.tan(math.radians(x))

# Función principal de la calculadora


def calculadora_avanzada():
    print("Bienvenido a la calculadora de NC")
    print("Opciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Salir")

    while True:
        opcion = input("Selecciona una operación (1-10): ")

        if opcion == "10":
            print("Gracias por usar la calculadora de NC. ¡Hata pronto!")
            break

        if opcion in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")
                continue

            if opcion == "1":
                print("Resultado:", sumar(num1, num2))
            elif opcion == "2":
                print("Resultado:", restar(num1, num2))
            elif opcion == "3":
                print("Resultado:", multiplicar(num1, num2))
            elif opcion == "4":
                print("Resultado:", dividir(num1, num2))
            elif opcion == "5":
                print("Resultado:", potencia(num1, num2))
            elif opcion == "6":
                print("Resultado:", modulo(num1, num2))
        elif opcion in ["7", "8", "9"]:
            try:
                num = float(input("Ingresa el ángulo en grados: "))
            except ValueError:
                print("Error: Ingresa un valor numérico válido.")
                continue

            if opcion == "7":
                print("Resultado (seno):", seno(num))
            elif opcion == "8":
                print("Resultado (coseno):", coseno(num))
            elif opcion == "9":
                print("Resultado (tangente):", tangente(num))
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 10.")


# Ejecutar la calculadora
calculadora_avanzada()
