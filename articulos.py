import mysql.connector

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="bd1")
        return conexion



    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(id, nombre, formula, precio, cantidad, presentacion, caducidad, laboratorio_id, ubicacion_id) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id, nombre, formula, precio, cantidad, presentacion, caducidad, laboratorio_id, ubicacion_id nombre from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, id, nombre, formula, precio, cantidad, presentacion, caducidad, laboratorio_id, ubicacion_id nombre from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount 

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update articulos set id=%s, precio=%s, nombre= %s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount 
