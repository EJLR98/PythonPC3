# main.py

import os

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        return resultado
    finally:
        print(f"Directorio de trabajo: {os.getcwd()}")
        print("Proceso terminado.")

if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = dividir(num1, num2)
        print(f"Resultado de la división: {resultado}")
    except ValueError:
        print("Por favor, ingrese números válidos.")