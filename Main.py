from Persona import *
from Sistema import *
from Vuelos import *
from Avion import *
import json
from datetime import *

def ConseguirData(archivito):
   with open(archivito, "r") as f:
       diccionario = json.loads(f.read())
   return diccionario

def ObteniendoAviones(diccionario):
   listAviones = []
   listDiccionarios = diccionario["Aviones"]

   for item in listDiccionarios:
       avion = Avion()
       avion.descerializacion(item)
       listAviones.append(avion)
   return listAviones

def ObteniendoPersona(diccionario, listAviones):
   listPersonas = []
   listDiccionarios = diccionario["Personas"]
   for item in listDiccionarios:
       if item["tipo"] == "Servicio":
           personita = Azafatas()
           personita.descerializacion(item, listAviones)
           listPersonas.append(personita)
       elif item["tipo"] == "Piloto":
           personita = Piloto()
           personita.descerializacion(item, listAviones)
           listPersonas.append(personita)
       elif item["tipo"] == "Pasajero":
           personita = Pasajero()
           personita.descerializacion(item, listAviones)
           listPersonas.append(personita)

   return listPersonas

def ObteniendoVuelos(diccionario, listPersonas, listAviones):
   listVuelos = []
   listDiccionarios = diccionario["Vuelos"]

   for item in listDiccionarios:
       vuelo = Vuelos()
       vuelo.descerializacion(item, listPersonas, listAviones)
       listVuelos.append(vuelo)
   return listVuelos

def DoyDatosDelAvion(Avion):
   print(Avion.modelo, "-", Avion.cantpasajeros, "-", Avion.canttrip)

def DoyDatosPersona(Persona, Azafata = False, Pasajero = False, Piloto = False):
   if type(Persona) is Pasajero and Pasajero:
       print(Persona.nombre, Persona.apellido, Persona.dni,  Persona.vip,
              Persona.atencionesp)
   elif type(Persona) is Azafatas and Azafata:
       print(Persona.nombre,  Persona.apellido, Persona.dni)
       for item in Persona.listAviones:
           print("Avion: ", item.modelo)
       for item in Persona.listIdiomas:
           print("Idiomas:", item)
   elif type(Persona) is Piloto and Piloto:
       print(Persona.nombre, Persona.apellido, Persona.dni)
       for item in Persona.listaAviones:
           print("Avion: ", item.modelo)

def ObtengoLasPersonasSepPorClases(listaPersonas, Azafata = False, Pasajero = False, Piloto = False):
   list = []
   for persona in listaPersonas:
       if type(persona) is Pasajero and Pasajero:
           list.append(persona)
       elif type(persona) is Piloto and Piloto:
           list.append(persona)
       elif type(persona) is Azafatas and Azafata:
           list.append(persona)
   return list


def DoyDatosVuelo(vuelo):
   print(vuelo.avion.modelo, vuelo.origen, vuelo.destino, vuelo.fecha, vuelo.hora)
   for item in vuelo.listPasajeros:
       print("Pasajeros: ", item.dni)
   for item in vuelo.listTripu:
       print("Tripulacion: ", item.dni)



s = Sistema()
j = {}

j = ConseguirData("datos.json")

listAviones = ObteniendoAviones(j)
listPersonas = ObteniendoPersona(j, listAviones)
listVuelos = ObteniendoVuelos(j, listPersonas, listAviones)
s.CargarList(listVuelos, listAviones, listPersonas)

print("Los pasajeros sonm :")
for item in listPersonas:
   DoyDatosPersona(item, True)

print("\n-------------------------------------------------")

print("\n", "Los Jovenes y Lista por Vuelo")
for item in listVuelos:
   print("Vuelo", item.avion.modelo)
   Joven = item.Joven()
   for item2 in item.listPasajeros:
       if item2 == Joven:
           print(item2.nombre,  item2.apellido)
       else:
           print(item2.nombre,  item2.apellido)

print("\n-------------------------------------------------")
print("Vuelos validos por Cantidad de tripulacao")
for item in listVuelos:
   if item.MinimaTripulacion():
       print(item.avion.modelo,  item.origen, item.destino, item.hora)

print("\n-------------------------------------------------")
print("Vuelos no validos por la Cantidad de tripulacao")
for item in listVuelos:
   if not item.MinimaTripulacion():
       print(item.avion.modelo,  item.origen,  item.destino, item.hora)

print("\n-------------------------------------------------")
print("\n", "Vuelos validos por Aviones Permitidos")
for item in listVuelos:
   if item.ChequeandoLosTripulantes():
       print(item.avion.modelo, item.origen, item.destino, item.hora)

print("\n-------------------------------------------------")
print("Vuelos no validos por Aviones Permitidos")
for item in listVuelos:
   if not item.ChequeandoLosTripulantes():
       print(item.avion.modelo,  item.origen, item.destino, item.hora)

print("\n-------------------------------------------------")
print("\n", "Personas validas por no laburar mas de 1 vez al dia")
for item in listPersonas:
   if type(item) is Azafatas or type(item) is Piloto:
       if s.DiasTripulacion(item):
           print(item.nombre,  item.apellido,  item.dni)

print("\n-------------------------------------------------")
print("Personas no validas por ya haber volado")
for item in listPersonas:
   if type(item) is Azafatas or type(item) is Piloto:
       if not s.DiasTripulacion(item):
           print(item.nombre,  item.apellido, item.dni)

print("\n-------------------------------------------------")
print("\n", "Los idiomas son: ")
for item in s.listVuelos:
   print("Vuelo", item.avion.modelo)
   for item2 in item.idiomas():
       print(item2)

