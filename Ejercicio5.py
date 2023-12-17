class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def obtener_pais_y_lote(self):
        pais, lote, _ = self.codigo.split('-')
        return pais, lote

    def __str__(self):
        return f"Producto(nombre={self.nombre}, código={self.codigo})"

# Ejemplo de uso
nombre_producto = input("Ingrese el nombre del producto: ")
codigo_producto = input("Ingrese el código del producto (en formato 'PAIS-LOTE-AÑO'): ")

mi_producto = Producto(nombre_producto, codigo_producto)

# Imprimir el objeto de forma literal
print(mi_producto)

# Identificar el país de origen y el número de lote
pais_origen, numero_lote = mi_producto.obtener_pais_y_lote()
print(f"País de origen: {pais_origen}")
print(f"Número de lote: {numero_lote}")