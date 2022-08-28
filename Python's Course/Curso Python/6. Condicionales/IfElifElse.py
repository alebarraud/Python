#En python no existe el SWITCH como tal, si no que se utiliza el elif 


numero = int(input("Ingrese un valor "))

if(numero < 0):
    print("El numero que usted ingreso ({}) es menor a 0.".format(numero))
elif (numero > 0):
    print("El numero que usted ingreso ({}) es mayor a 0.".format(numero))
else:
    print("El numero que usted ingreso ({}) es igual a 0.".format(numero))



if numero in (1,2,3):
    print("Yes!")
else:
    print("Not!")
    