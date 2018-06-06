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


class Piloto (Persona):
    pass

class Pasajero (Persona):
    vip = None
    atencionesp= None

    def SetVip (self, vip):
        self.vip = vip

    def SetAtencionesp (self,atencionesp):
        self.atencionesp = atencionesp
