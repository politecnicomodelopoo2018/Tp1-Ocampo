import datetime

class Persona(object):
    nombre = None
    apellido = None
    dni = None
    fechanaci = None

    # setts
    def SetNombre(self, nombre):
        self.nombre = nombre

    def SetApellido(self, apellido):
        self.apellido = apellido

    def SetDni(self, dni):
        self.dni = dni

    def SetFechanaci(self, fechanaci):
        self.fechanaci = fechanaci

    def descerializacion(self, diccionario, listAviones):
        self.nombre = (diccionario["nombre"])
        self.apellido = (diccionario["apellido"])
        self.dni = (diccionario["dni"])
        self.fechanaci = (diccionario["fechaNacimiento"])


class Pasajero(Persona):
    vip = None
    atencionesp = None

    # sets
    def SetVip(self, vip):
        self.vip = vip

    def SetAtencionesp(self, atencionesp):
        self.atencionesp = atencionesp

    def descerializacion(self, diccionario, listAviones):
        super().descerializacion(diccionario, listAviones)
        self.vip = diccionario["vip"]
        if "solicitudesEspeciales" in diccionario:
            self.Atencionesp = (diccionario["solicitudesEspeciales"])


class Tripulacion(Persona):

    def __init__(self):
        self.listAviones = []

    def setListAviones(self, listAviones):
        self.listAviones = listAviones

    def addAviones(self, avion):
        self.listAviones.append(avion)

    def descerializacion(self, diccionario, listAviones):
        super().descerializacion(diccionario, listAviones)
        for item in diccionario["avionesHabilitados"]:
            for item2 in listAviones:
                if item == item2.modelo:
                    self.addAviones(item2)


class Azafatas(Tripulacion):
    def __init__(self):
        super().__init__()
        self.listIdiomas = []

    def addListIdioma(self, listIdiomas):
        self.listIdiomas = listIdomas

    def addIdioma(self, idioma):
        self.listIdiomas.append(idioma)

    def descerializacion(self, diccionario, listAviones):
        super().descerializacion(diccionario, listAviones)
        for item in diccionario["idiomas"]:
            self.addIdioma(item)


class Piloto(Tripulacion):
    pass

