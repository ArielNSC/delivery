from datetime import datetime

class Repartidor:
    def __init__(self,id = None, rut = "", nombre = "", apellidos = "", telefono = "", estado = "", fecha_ingreso = None):
        self.id = id
        self.rut = rut
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.estado = estado
        self.fecha_ingreso = fecha_ingreso if fecha_ingreso else datetime.now()
    def __str__(self):
        return f"Repartidor(id={self.id},rut='{self.rut}',nombre ='{self.nombre}',apellidos = '{self.apellidos}',telefono = {self.telefono},estado ='{self.estado}',fecha_ingreso = {self.fecha_ingreso})"