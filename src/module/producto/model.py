import sqlite3
"""
Abstracción del modelo de la base de datos

"""
class Producto:

    def _init_(self):
        self.id = 0
        self.nombre = ""
        self.formula = ""
        self.precio = 0
        self.cantidad = 0
        self.presentacion = ""
        self.caducidad = ""
        self.laboratorio_id = 0
        self.ubicacion_id = 0