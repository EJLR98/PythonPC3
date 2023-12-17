# main.py

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def mostrar_menu():
    print("Menu:")
    print("1. Dividir dos números")
    print("0. Salir")

while True:
    mostrar_menu()
    try:
        opcion_seleccionada = int(input("Seleccione una opción: "))
        if opcion_seleccionada == 1:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = dividir(num1, num2)
            print(f"Resultado de la división: {resultado}")
        elif opcion_seleccionada == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingrese un número entero o decimal.")