import mysql.connector
from mysql.connector import Error

class ConexionDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            try:
                cls._instancia = super().__new__(cls)
                cls._instancia.conn = mysql.connector.connect(
                    host="host",
            user="usuario",
            password="password",
            database="basey_de_datos"
                )
                if cls._instancia.conn.is_connected():
                    print("Conexión establecida a la base de datos.")
            except Error as e:
                print(f"Error al conectar a MySQL: {e}")
                cls._instancia = None
        return cls._instancia

    def obtener_conexion(self):
        return self.conn if self._instancia else None
