from Persona import *
from Vuelos import *
from datetime import *

class Sistema(object):

    def __init__(self):
        self.listPersona = []
        self.listVuelos = []
        self.listAviones = []


    def SetListPerson (self, listPersona):
        self.listPersona = listPersona

    def SetListVuelos (self, listVuelos):
        self.listVuelos = listVuelos

    def SetListAviones (self, listAviones):
        self.listAviones = listAviones

    def addPersona (self, persona):
        self.listPersona.append(persona)

    def addVuelo (self, vuelo):
        self.listVuelos.append(vuelo)

    def CargarList (self, listVuelos, listAviones, listPersona):
        self.listVuelos = listVuelos
        self.listAviones = listAviones
        self.listPersona = listPersona

#5
    def FechasPorTripulacion (self, Tripulacion):
        listFechas = []
        for item in self.listVuelos:
            for item2 in item.listTripu:
                if Tripulacion.dni == item2.dni:
                    listFechas.append(item.fecha)
        return listFechas


    def DiasTripulacion(self, Tripulacion):
        for item in self.FechasPorTripulacion(Tripulacion):
            fecha = 0
            for item2 in self.FechasPorTripulacion(Tripulacion):
                if item == item2:
                    fecha += 1
                    if fecha == 2:
                        return False
        return True
