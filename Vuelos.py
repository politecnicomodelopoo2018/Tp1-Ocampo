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
        self.listaPasajeros.append(pasajero)

    def AddTripulacion (self, Tripulacion):
        self.listTripu.append(Tripulacion)

