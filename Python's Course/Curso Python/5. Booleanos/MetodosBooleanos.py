#Metodos booleanos de comparacion de Strings 


from sre_compile import isstring

cadena0 = "todo esta en minusculas"
cadena = "Estos mostrando los metodos booleanos para Strings"
cadena2 = "MAYUSCULAS"

#Verifica si un valor pasado como parametro es un string 
print(isstring(cadena))

#Verifica si una palabra empieza con un caracter pasado como parametros 
print(cadena.startswith("e"))

#Verifica si una palabra finaliza con un caractor pasado como parametros 
print(cadena.endswith("e"))

#Verifica si toda la palabra esta en minuscula 
print(cadena0.islower())

#Verifica si toda la palabra esta escrita en mayuscula
print(cadena2.isupper())