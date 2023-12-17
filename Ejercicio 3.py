class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}"


class Catalogo:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def mostrar_productos(self):
        if not self.lista_productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos:")
            for producto in self.lista_productos:
                print(producto)


# Ejemplo de uso
catalogo_tienda = Catalogo()

# Agregar productos al catálogo
producto1 = Producto("P001", "Batería de coche", 99.99)
producto2 = Producto("P002", "Filtro de aceite", 12.50)

catalogo_tienda.agregar_producto(producto1)
catalogo_tienda.agregar_producto(producto2)

# Mostrar la lista de productos en el catálogo
catalogo_tienda.mostrar_productos()