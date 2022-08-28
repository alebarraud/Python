#Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. 
#El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, 
#deben ser concatenadas ambas


a = input("Ingrese una vocal en minuscula ")
b = input("Ingrese una letra en mayusculas ")

#uso de la funcion format 
print("Las letras ingresadas son {} y {} --> y su conversion es {} y {} \n".format(a,b,a.upper(),b.lower()))