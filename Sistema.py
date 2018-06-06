from Persona import *

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

