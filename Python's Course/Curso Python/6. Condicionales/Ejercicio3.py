"""Ejercicio 2

Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, 
candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir 
el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
"""

voto = input("Ingrese su voto:\ncandidato A por el partido rojo \ncandidato B por el partido verde \ncandidato C por el partido azul\n")

if voto.lower() == "a":
    print("Usted ha votado por el partido rojo")
elif voto.lower() == "b":
    print("Usted ha votado por el partido verde")
elif voto.lower() == "c":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")