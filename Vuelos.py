from datetime import *
from Persona import *

class Vuelos (object):
   avion = None
   origen = None
   destino = None
   fecha = None
   hora = None

   def __init__(self):
       self.listTripu = []
       self.listPasajeros = []
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

   def descerializacion (self, diccionario, listPersonas, listAviones):
       for item in listAviones:
           if diccionario["avion"] == item.modelo:
               self.avion = item
       self.fecha  = (datetime.datetime.strptime(diccionario["fecha"], "%Y-%m-%d"))
       self.hora = (diccionario["hora"])
       self.destino = (diccionario["destino"])
       self.origen  = (diccionario["origen"])
       for item in diccionario["pasajeros"]:
           for item2 in listPersonas:
               if type(item2) is Pasajero and item == item2.dni:
                   self.listPasajeros.append(item2)
       for item in diccionario["tripulacion"]:
           for item2 in listPersonas:
               if ((type(item2) is Piloto) or (type(item2) is Azafatas)) and item == item2.dni:
                   self.listTripu.append(item2)



   def ModelosTripulacion (self, Tripulacion):
       for item in Tripulacion.listAviones:
           if item.modelo == self.avion.modelo:
               return True
       return False

   def ChequeandoLosTripulantes (self):
       for item in self.listTripu:
           if not self.ModelosTripulacion(item):
               return False
       return True

#2
   def Joven (self):
       masjoven = self.listPasajeros[0]
       for item in self.listPasajeros:
           if item.fechanaci > masjoven.fechanaci:
               masjoven = item
           return masjoven

#3
   def MinimaTripulacion(self):
       print(self.avion.canttrip)
       if self.avion.canttrip > len(self.listTripu):
           return False
       return True

#7
   def idiomas (self):
       lenguaje = []
       for item in self.listTripu:
           if type(item) is Azafatas:
               for item2 in item.listIdiomas:
                   lenguaje.append (item2)
               return lenguaje






