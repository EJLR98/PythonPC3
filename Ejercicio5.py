# Producto.py

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def obtener_pais_y_lote(self):
        pais, lote, _ = self.codigo.split('-')
        return pais, lote

    def __str__(self):
        pais, lote = self.obtener_pais_y_lote()
        return f"Producto(nombre={self.nombre}, código={self.codigo})\nPaís de origen: {pais}, Número de lote: {lote}"