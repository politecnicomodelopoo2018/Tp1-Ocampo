from datetime import *

class Persona (object):
    nombre = None
    apellido = None
    dni = None
    fechanaci = None

    def SetNombre (self, nombre):
        self.nombre = nombre

    def SetApellido (self,apellido):
        self.apellido = apellido

    def SetDni (self, dni):
        self.dni = dni

    def SetFechanac (self, fechanaci):
        self.fechanaci = fechanaci


class Pasajero (Persona):
    vip = None
    atencionesp= None

    def SetVip (self, vip):
        self.vip = vip

    def SetAtencionesp (self,atencionesp):
        self.atencionesp = atencionesp


class Tripulacion(Persona):
    def __init__(self):
        self.listAviones = []


class Piloto (Tripulacion):
    pass


class Azafatas(Tripulacion):
    def __init__(self):
        super().__init__()
        self.listIdomas = []