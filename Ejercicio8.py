# Persona.py

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

# Instanciar datos ingresados desde teclado
nombre_persona = input("Ingrese el nombre de la persona: ")
edad_persona = int(input("Ingrese la edad de la persona: "))
ciudad_persona = input("Ingrese la ciudad de la persona: ")

mi_persona = Persona(nombre_persona, edad_persona, ciudad_persona)




