class Avion(object):
    modelo = None
    cantpasajeros =None
    canttrip = None

    def SetModelo (self, modelo):
        self.modelo = modelo


    def SetCantPasajeros (self, cantpasajeros):
        self.cantpasajeros = cantpasajeros


    def SetCanttrip (self, canttrip):
        self.canttrip = canttrip

#recuperando info del json(descerializar)

    def descerializacion (self, diccionario):
        self.modelo = (diccionario["codigoUnico"])
        self.cantpasajeros = (diccionario["cantidadDePasajerosMaxima"])
        self.canttrip = (diccionario["cantidadDeTripulacionNecesaria"])

