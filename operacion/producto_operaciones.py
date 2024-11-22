from mysql.connector import Error
from modelo.producto import Producto
from db_conexion import DatabaseConnection

class ProductoOperaciones:
    #Función para inicializar una conexión  base de datos
    def __init__(self):
        self.db_conexion = DatabaseConnection()
    #Función para agregar un producto
    def agregar(self, producto):
        conexion = self.db_conexion.get_connection()
        try: 
            cursor = conexion.cursor() #cursor tiene los objetos de conexión que permite recorrer las tablas
            #Consulta SQL

            query ="insert into Producto (nombre, descripcion, precio, id_tipo_producto,) values (%s,%s,%s,%s);"

            #Extraemos valores de un objeto producto
            valores = (producto.nombre, producto.descripcion, producto.precio, producto.id_tipo_producto) 
            #Ejecutamos la operación contra la base de datos (insertar)
            cursor.execute(query, valores)
            #Ejecutamos commit o una confirmación (es para confirmar el cambio y que quede actualizado en la base de datos.)
            conexion.commit()
            #Obtenemos el id del registro insertado
            producto.id=cursor.lastrowid
            #Envíamos una confirmación
            print("Producto ingresado correctamente.")
            return producto
        except Error as e:
            print(f"Error al insertar registro: {e}")
        finally:
            if cursor:
                cursor.close()

    #Función para listar datos
    def listar_datos(self):
        conexion=self.db_conexion.get_connection()
        try:
            cursor=conexion.cursor(dictionary=True)
            query="select *from Producto;"
            cursor.execute(query)
            resultados=cursor.fetchall() 
            return[Producto(**resultado) for resultado in resultados]
        
        except Error as e:
            print(f"Error al consultar datos: {e}")
        finally:
            if cursor:
                cursor.close()
    #Función para actuazliar datos
    def actualizar (self, producto):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor()
            query = "update Producto set nombre = %s, descripcion=%s, precio=%s, id_tipo_producto=%s where id= %s;"
            valores = (producto.nombre, producto.descripcion, producto.precio, producto.id_tipo_producto, producto.id)
            cursor.execute(query, valores)
            conexion.commit()
            return cursor.rowcount > 0 
        except Error as e:
            print(f"Error al actualizar el registro: {e}")
        finally:
            if cursor:
                cursor.close()
    #Función para eliminar datos
    def eliminar (self,id):
        conexion= self.db_conexion.get_connection ()
        try:
            cursor = conexion.cursor()
            query = "delete from Producto where id = %s;"
            cursor.execute(query,(id,))
            conexion.commit ()
            return cursor.rowcount
        except Error as e:
            print(f"Error al eliminar el tipo de producto: {e}")
        finally:
            if cursor:
                cursor.close()