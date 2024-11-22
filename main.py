from modelo.tipo_producto import TipoProducto
from modelo.producto import Producto
from modelo.repartidor import Repartidor

from operacion.tipo_producto_operaciones import TipoProductoOperaciones
from operacion.producto_operaciones import ProductoOperaciones
from operacion.repartidor_operaciones import RepartidorOperaciones


def seleccionar_opcion ():
    while True:
        print("** Seleccionar una opción **")
        print("1. Acceder a Tipo Producto")
        print("2. Acceder a Producto")
        print("3. Acceder a Repartidor")
        print("4. Salir") 

        seleccionar_opcion= input("Seleccione una opción: ")
        if seleccionar_opcion == "1":
            main_tipo_producto ()
        
        if seleccionar_opcion =="2":
            main_producto ()

        if seleccionar_opcion =="3":
            main_repartidor ()

        if seleccionar_opcion =="4":
            print("saliendo del programa")
            break

def main_tipo_producto():
   
    operacion = TipoProductoOperaciones()

   
    while True:
        print("*** Menú principal ***")
        print("1. Agregar tipo de producto")
        print("2. Listar tipo de producto")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
   
        opcion= input("Seleccione una opción: ")

       
        if opcion =="1":
            
            nombre= input("Nombre del tipo de producto: ")
            descripcion= input("Descripcion: ")

         
            nuevoTipoProducto = TipoProducto(nombre= nombre, descripcion=descripcion)
            
            
            resultado = operacion.agregar(nuevoTipoProducto)
            
           
            if resultado:
                print(f"Tipo de Produto ingresado correctamente con ID: {resultado.id_tipo_producto}")

        if opcion == "2":
            tipos_productos = operacion.obtener_datos() 
            if tipos_productos:
                print("*** Tipos de producto registrados ***")
                
                for tipo in tipos_productos:
                    print(f"ID: {tipo.id_tipo_producto}") 
                    print(f"NOMBRE TIPO: {tipo.nombre}") 
                    print(f"DESCRIPCION: {tipo.descripcion}")
            else:
                print("No hay registro de tipo de producto")
       
       
   
        if opcion == "3":
            id = input("Ingrese id de tipo producto a actualizar: ")
            nombre =input("Ingrese nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            
            tipo_producto = TipoProducto (id_tipo_producto=int(id), nombre=nombre, descripcion=descripcion) 
            
            if operacion.actualizar(tipo_producto):
                print("Registro actualizado correctamente")
            else: 
                print("No se actualizó ningún registro")
      
        if opcion == "4":
            id_tipo_producto=input("Ingrese id de tipo de producto a eliminar: ")
            if operacion.eliminar(int(id_tipo_producto)): 
                print("Registro eliminado correctamente")
            else:
                print("No fue posible eliminar")

        if opcion == "5":
            print("Hasta Luego! ")
            break


def main_producto():
   
    operacion = ProductoOperaciones()

    
    while True:
        print("*** Productos ***")
        print("1. Agregar un producto")
        print("2. Listar producto")
        print("3. Actualizar un producto")
        print("4. Eliminar un producto")
        print("5. Salir")
        
        opcion= input("Seleccione una opción: ")

        
        if opcion =="1":
           
            nombre= input("Nombre del producto: ")
            descripcion = input("Descripción: ")
            precio = input("Precio: ")
            id_tipo_producto=input("Tipo Producto: ")
        

           
            nuevoProducto = Producto(nombre= nombre, descripcion = descripcion, precio=precio, id_tipo_producto=id_tipo_producto)
            
            
            resultado = operacion.agregar(nuevoProducto)
            
            
            if resultado:
                print(f"Produto ingresado correctamente con ID: {resultado.id}")

        if opcion == "2":
            productos = operacion.listar_datos() 
            if productos:
                print("*** Producto registrado ***")
                
                for producto in productos:
                    print(f"ID: {producto.id}") 
                    print(f"NOMBRE PRODUCTO: {producto.nombre}") 
                    print(f"DESCRIPCION: {producto.descripcion}")
                    print(f"PRECIO:{producto.precio} ")
                    print(f"ID TIPO PRODUCTO: {producto.id_tipo_producto}")
            else:
                print("No hay registro del producto")
       
       
     
        if opcion == "3":
            id = input("Ingrese id de tipo producto a actualizar: ")
            nombre =input("Ingrese nuevo nombre: ")
            descripcion= input("Nueva descripción: ")
            precio = input ("Ingrese precio actualizado: ")
            id_tipo_producto= input("Ingrese nuevo id tipo producto: ")
            
            producto = Producto (id=int(id), nombre= nombre, descripcion = descripcion, precio=precio, id_tipo_producto=id_tipo_producto) 
            
            if operacion.actualizar(producto):
                print("Registros actualizados ")
            else: 
                print("No se pudo registrar la actualización")
      
        if opcion == "4":
            id=input("Ingrese id del producto a eliminar: ")
            if operacion.eliminar(int(id)): 
                print("Registro eliminado correctamente")
            else:
                print("No fue posible eliminar")


        if opcion == "5":
            print(" El programa ha sido cerrado.")
            break


def main_repartidor():
    operacion = RepartidorOperaciones()

    while True:
        print(" *** Menú principal *** ")
        print("1. Agregar nuevo Repartidor")
        print("2. Listar repartidores")
        print("3. Actualizar Repartidor")
        print("4. Eliminar Repartidor")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            rut = input("Rut del repartidor: ")
            nombre = input("Nombre del repartidor: ")
            apellidos = input("apellidos del repartidor: ")
            telefono = input("Telefono del repartidor: ")
            estado = input("Estado: ")

            nuevoRepartidor = Repartidor(rut = rut, nombre = nombre, apellidos = apellidos, telefono = telefono, estado = estado)

            resultado = operacion.agregar(nuevoRepartidor)

            if resultado:
                print(f" Repartidor ingresado correctamente con ID : {resultado.id} ")


        if opcion == "2":
            
            repartidores = operacion.listar_datos()
            if repartidores:
                print("Repartidores")
                for repartidor in repartidores:
                    print(f"ID: {repartidor.id}")
                    print(f"Rut: {repartidor.rut}")
                    print(f"Nombre: {repartidor.nombre}")
                    print(f"Apellidos: {repartidor.apellidos}")
                    print(f"estado: {repartidor.estado}'")
                                    
            else:
                print("No hay Repartidores registrados.")

        if opcion == "3":
            id = input("ingrese id del repartidor a actualizar: ")
            nuevo_rut = input("Nuevo rut: ")
            nuevo_nombre = input("Nuevo nombre : ")
            nuevo_apellidos  = input("Nuevo apellido: ")
            nuevo_telefono = input("Nuevo telefono: ")
            nuevo_estado = input("Nuevo estado: ")
            repartidor = Repartidor(id = int(id),rut = nuevo_rut, nombre = nuevo_nombre, apellidos = nuevo_apellidos, telefono = nuevo_telefono, estado = nuevo_estado)
            
            
            if operacion.actualizar(repartidor):
                print("Registros actualizados ")
            else: 
                print("No se pudo registrar la actualización")

        if opcion == "4":
            id = input("Ingrese el id del repartidor a eliminar: ")
            if operacion.eliminar(int(id)):

                print("Repartidor eliminado correctamente.")
            else:
                print("El repartidor no se ha podido eliminar.")

        if opcion == "5":
            print("programa finalizado")
            break


if __name__== "__main__":
    seleccionar_opcion()
