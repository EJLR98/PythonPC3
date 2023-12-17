import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        # Fórmula del área del círculo: A = π * r^2
        area = math.pi * self.radio**2
        return area

# Ejemplo de uso de la clase Circulo
radio_ingresado = float(input("Ingrese el radio del círculo: "))

# Crear una instancia de la clase Circulo
mi_circulo = Circulo(radio_ingresado)

# Calcular y mostrar el área del círculo
area_circulo = mi_circulo.calcular_area()
print(f"El área del círculo con radio {radio_ingresado} es: {area_circulo:.2f}")