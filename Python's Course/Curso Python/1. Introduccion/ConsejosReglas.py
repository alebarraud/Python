""" No se pueden utilizar palabras reservadas como nombre de variables"""

"""No pueden empezar con numeros las variables """

"""No pueden tener caracteres especiales las variables"""

"""Camel case edadJovenes"""

"""Serpiente EdadJovenes"""

"""Script para ver todas las palabras reservadas que tiene python: """
import keyword

print(keyword.kwlist)


def estaPalabra(busqueda):
    for x in (keyword.kwlist):
        if (x == busqueda):
            return 1
    return 0 

print(estaPalabra("Print"))    

print(estaPalabra("raise"))  