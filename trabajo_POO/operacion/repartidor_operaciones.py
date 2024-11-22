from mysql.connector import Error
from modelo.repartidor import Repartidor
from db_conexion import DatabaseConnection

class RepartidorOperaciones:
    def __init__(self):
        self.db_conexion = DatabaseConnection()

    def agregar(self, repartidor):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor()
            query = "insert into Repartidor(rut,nombre,apellidos,telefono,estado) values(%s,%s,%s,%s,%s);" 
            valores = (repartidor.rut, repartidor.nombre, repartidor.apellidos, repartidor.telefono, repartidor.estado) 
            cursor.execute(query,valores)
            conexion.commit()
            repartidor.id = cursor.lastrowid
            
            print("Repartidor se ha ingresado correctamente")
            return repartidor
        except Error as e:
            print(f"Error al insertar nuevo repartidor : {e} ")
        finally:
            if cursor:
                cursor.close()
          

    
    def listar_datos(self):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor(dictionary = True)
            query = "select * from Repartidor;"
            cursor.execute(query)
            resultados = cursor.fetchall()
            return [Repartidor(**resultado) for resultado in resultados]
        
        except Error as e:
            print(f"Error al consultar datos : {e}")
        finally:
            if cursor:
                cursor.close()
          
    
    def actualizar(self,repartidor):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor()
            query = "update Repartidor set rut= %s, nombre = %s, apellido = %s, telefono = %s, estado = %s where id = %s;"
            valores = (repartidor.rut, repartidor.nombre,repartidor.apellido,repartidor.telefono,repartidor.estado,repartidor.id)
            cursor.execute(query,valores)
            conexion.commit()
            return cursor.rowcount > 0
        
        
        except Error as e:
            print(f"Error al actualizar datos de Repartidor : {e}")
        finally:
            if cursor:
                cursor.close()
            

    def eliminar(self,id):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor()
            query = "delete from Repartidor where id = %s;"
            cursor.execute(query, (id,))
            conexion.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al eliminar el Repartidor : {e}")
        finally:
            if cursor:
                cursor.close()
                
