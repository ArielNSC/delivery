from datetime import datetime

class TipoProducto:
    def __init__(self, id_tipo_producto=None, nombre="", descripcion="", fecha_ingreso=None):
        self.id_tipo_producto=id_tipo_producto
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha_ingreso=fecha_ingreso if fecha_ingreso else datetime.now ()
    def __str__(self):
        return f"TipoProducto(id={self.id_tipo_producto} nombre='{self.nombre}', descripcion ='{self.descripcion}', fecha_ingreso= {self.fecha_ingreso})"