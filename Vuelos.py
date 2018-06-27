from Persona import *

class Vuelos (object):
    avion = None
    origen = None
    destino = None
    fecha = None
    hora = None

    def __init__(self):
        listTripu = []
        listPasajeros = []
#Sets
    def SetAvion (self, avion):
        self.avion = avion

    def SetOrigen (self, origen):
        self.origen = origen

    def SetDestino (self, destino):
        self.destino = destino

    def SetFecha (self, fecha):
        self.fecha = fecha

    def SetHora (self, hora):
        self.hora = hora

    def SetListTripu (self, listTripu):
        self.listTripu = listTripu

    def SetListPasajeros (self, listPasajeros):
        self.listPasajeros = listPasajeros

#Adds
    def AddPasajero (self, pasajero):
        self.listPasajeros.append(pasajero)

    def AddTripulacion (self, Tripulacion):
        self.listTripu.append(Tripulacion)

    def descerializacion (self, diccionario):
       for item in listAviones:
            if diccionario["avion"] == item.modelo:
                self.avion = item
                self.setFecha(datetime.strptime(diccionario["fecha"], "%Y-%m-%d"))
                self.setHora(diccionario["hora"])
                self.setDestino(diccionario["destino"])
                self.setOrigen(diccionario["origen"])
                for item in diccionario["pasajeros"]:
                    for item2 in listPersonas:
                        if type(item2) is Pasajero and item == item2.dni:
                             self.addPasajero(item2)
                             for item in dict["tripulacion"]:
                                 for item2 in listPersonas:
                                     if ((type(item2) is Piloto) or (type(item2) is Servicio)) and item == item2.dni:
                                          self.addTripulante(item2)


    def verificarTripulacion (self, Tripulacion):
        for item in Tripulacion.listAviones:
            if item.modelo == self.avion.modelo:
                return True
        return False

    def validandoTripulacion (self):
        for item in self.listTripu:
            if not self.verificarTripulacion(item):
                return False
        return True

#2
    def Joven (self):
        masjoven = self.listPasajeros = [0]
        for item in self.listPasajeros:
            if item.fechanaci > masjoven.fechanaci:
                masjoven = item
            return masjoven

#3
    def MinimaTripulacion(self):
        if len(self.listTripu) < avion.canttrip:
            return false
        return true

#4


#7
    def idomas (self):
        lenguaje = []
        for item in listTripu:
            if type(item) is Azafatas:
                for item2 in item.listIdiomas:
                    lenguaje.append (item2)
                return lenguaje


