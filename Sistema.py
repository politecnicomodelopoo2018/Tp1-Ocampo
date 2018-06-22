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

    def addPersona(self, persona):
        self.listPersona.append(persona)

    def addVuelo (self, vuelo):
        self.listVuelos.append(vuelo)

    def Cargartodo (self, listVuelos, listAviones, listPersona):
        self.listVuelos = listVuelos
        self.listAviones = listAviones
        self.listPersona = listPersona

    def FechasPorPiloto (self, piloto):
        listFechaVuelos = []

        for item in self.listVuelos:
            for item2 in item.listTripu:
                if item2 == piloto:
                    listFechaVuelos.append(item.fecha)
                return listFechaVuelos


    def verificarDiasPiloto(self, piloto):
        for item in self.FechasPorPiloto(piloto):
            fecha = 0
            for item2 in self.FechasPorPiloto(piloto):
                if item == item2:
                    fecha += 1
                    if fecha == 2:
                        return False
        return True
