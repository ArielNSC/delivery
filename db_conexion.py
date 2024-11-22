import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    _instance=None  


    def __new__(cls):
      
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection=None
        return cls._instance

   
    def connect(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    host ='192.168.56.102',
                    database='delivery',
                    user='pythonapp',
                    password='inacap.2024'
                )
                
                print("Conexión efectuada correctamente.")
            except Error as e:
                print(f"Se ha producido un error: {e}")
                self.connection = None
        return self.connection
    
    def close(self): 
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            print("Conexión cerrada.")
    
    def get_connection (self):
        return self.connect ()
             

