# main.py

class Catalogo:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, nombre, codigo):
        self.lista_productos.append({"nombre": nombre, "codigo": codigo})

    def mostrar_productos(self):
        for producto in self.lista_productos:
            print(f"Nombre: {producto['nombre']}, Código: {producto['codigo']}")

if __name__ == "__main__":
    catalogo_tienda = Catalogo()
    catalogo_tienda.agregar_producto("Ejemplo1", "PERU-0001-2023")
    catalogo_tienda.agregar_producto("Ejemplo2", "MEXICO-0002-2023")
    catalogo_tienda.mostrar_productos()