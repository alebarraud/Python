import math #import library of math because in there, there is a sqrt fuction  

a = float(input("Ingrese el valor de a "))
b = float(input("Ingrese el valor de b "))
c = float(input("Ingrese el valor de c "))


sol1 = - b + (math.sqrt( (b**2) - 4 * a * c ))
sol2 = - b - (math.sqrt( (b**2) - 4 * a * c ))


print("Las dos soluciones son %f y %f " % (sol1, sol2))