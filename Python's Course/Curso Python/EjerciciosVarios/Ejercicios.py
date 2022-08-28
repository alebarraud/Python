#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
def max1(a,b):
    if a > b:
        return a
    return b

assert(max1(1,2) == 2)
assert(max1(34,2) == 34)
assert(max1(34,22) == 34)

# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

assert(max_de_tres(111,2,3) == 111)
assert(max_de_tres(1,2,3) == 3)
assert(max_de_tres(34132,2,785) == 34132)
assert(max_de_tres(34,22423,123145) == 123145)


# Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

# "alexis" --> 6
# [1,2,3,4]--> 4 

def longitud_Cadena(a):
    contador = 0
    for x in (a):
        contador += 1
    return contador


assert(longitud_Cadena("alexis") == 6)
assert(longitud_Cadena([1,2,3,4]) == 4)


# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def esVocal(a):
    vocales = ['a','e','i', 'o', 'u']
    return(a in vocales)

assert(esVocal('a') == True)
assert(esVocal('b') == False)
assert(esVocal('u') == True)
assert(esVocal('z') == False)
assert(esVocal('i') == True)


# Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
#  Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(a):
    suma = 0
    for x in a:
        suma = suma + x 
    return suma 


assert(sum([1,2,3,4]) == 10)
assert(sum([1,2,3,4,5]) == 15)


# Definir una función inversa() que calcule la inversión de una cadena. 
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    nuevaCadena = ""
    for x in cadena:
        nuevaCadena = x + nuevaCadena
    return nuevaCadena


assert(inversa("ale") == "ela")
assert(inversa("estoy probando") == "odnaborp yotse")

# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen 
# el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.


def es_palindromo(cadena):
    return(cadena == inversa(cadena))

assert(es_palindromo("alexis") == False)
assert(es_palindromo("ele") == True)
assert(es_palindromo("ala") == True)
assert(es_palindromo("neuquen") == True)


# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 
# miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(lista1, lista2):
    for x in lista1:
        for y in lista2:
            if x == y: 
                return True
    return False 

assert(superposicion([1,2,3,4],[4,5,6,7]) == True)
assert(superposicion([1,2,3,4],[]) == False)
assert(superposicion([1,2,3,4],[5,6,7]) == False)


# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter 
# multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
       
def generar_n_caracteres(caracter, n):
    return n * caracter       
        
assert(generar_n_caracteres("a",10) == "aaaaaaaaaa")
assert(generar_n_caracteres("b",2) == "bb")
assert(generar_n_caracteres("a",1) == "a")


#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 

def procedimiento(lista):
    for x in lista:
        print("*" * int(x))


def procedimiento2(lista):
    nuevaCadena = ""
    for x in lista:
        nuevaCadena = nuevaCadena + ("*" * int(x)) + "\n"
    return nuevaCadena

print(procedimiento([4, 9, 7]))






