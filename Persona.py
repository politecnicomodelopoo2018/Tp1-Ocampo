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

    def descerializacion (self, diccionario, listAviones):
        self.setNombre(diccionario["nombre"])
        self.setApellido(diccionario["apellido"])
        self.setDni(diccionario["dni"])
        self.setFechanaci(diccionario["fechaNacimiento"])
        
        

class Pasajero (Persona):
    vip = None
    atencionesp= None

    def SetVip (self, vip):
        self.vip = vip

    def SetAtencionesp (self,atencionesp):
        self.atencionesp = atencionesp

    def descerializacion (self, diccionario, listaAviones):
        
        
class Tripulacion(Persona):
    def __init__(self):
        self.listAviones = []


    def setListAviones (self, listAviones):
        self.listAviones = listAviones

    def addAviones (self, avion):
        self.listAviones.append(avion)
        
    def descerializacion (self, diccionario, listAviones):
        

        
        
class Piloto (Tripulacion):
    pass


class Azafatas(Tripulacion):
    def __init__(self):
        super().__init__()
        self.listIdomas = []
        
    def addListIdioma (self,listaIdomas):
        self.listaIdomas = listaIdomas
        
    def addIdioma (self, idioma):
        self.listaIdiomas.append(idioma)
        
    def descerializacion (self, diccionario, listaAviones):
        
        
        
         
