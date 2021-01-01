import sqlite3


class ConexionDatabase:
    instance = None
    
    @staticmethod
    def get_instance():
        if not ConexionDatabase.instance:
            ConexionDatabase.instance = ConexionDatabase()
        return ConexionDatabase.instance

    def _init_(self):
        self.conn = None

    def query(self, sql, data):
        with self.connect() as conn:
            c = conn.cursor()
            rows = c.execute(sql,data)
            return rows


    def connect(self):
        if not self.conn:
            self.conn = sqlite3.connect("/Users/marcopichardofranco/Downloads/farmaciadb.sqlite")
        return self.conn