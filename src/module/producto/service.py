from database.conexion import ConexionDatabase

 #"""
 #Logica del negocio
    #-Consulta a BD
 #-Lógica compleja

class ProductoService:

    def _init_(self) :
        self.db = ConexionDatabase.get_instance()


    def insertar(self, producto):
        return self.db.query(
            """INSERT INTO producto 
            (id, nombre, formula, precio, cantidad, presentacion, caducidad, laboratorio_id, ubicacion_id) 
            VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?); """,
            (producto.id, producto.nombre, producto.formula, producto.precio, producto.cantidad, 
            producto.presentacion, producto.caducidad, producto.laboratorio_id, producto.ubicacion_id)   
        )


    def consultar_todos(self):
        pass

    def consultar_id(self):
        pass

    def consultar_nombre(self):
        pass

    def actualizar(self):
        pass

    def eliminar(self):        
        pass

    #tupla y lista -INVESTIGAR