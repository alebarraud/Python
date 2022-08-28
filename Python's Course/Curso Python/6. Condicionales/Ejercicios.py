"""Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". 
Sino, decirle al usuario que no es vocal
"""

vocal = input("Ingrese una vocal ")

if vocal.lower() in ("a","e","i", "o","u"):
    print("Es vocal! ")
else:
    print("No es vocal! ")

"""
Ejercicio 2

Escribir un programa que, dado un número entero, muestre su valor absoluto. 
Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52),
mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
"""
#Podriamos utiliza el metodo abs pero gueno vamos a programarlo

valor = int(input("ingrese un numero "))

if(valor >= 0):
    print(valor)
else:
    print(-1 * valor)

