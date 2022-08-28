from operator import concat
from ssl import create_default_context


cadena = "Hola Alexis"
cadena2 = "Barraud"


print(cadena + " " + cadena2)

#La diferencia del contact con + es que concat recibe unicamente 2 argumentos
print(concat(cadena, concat(" ",cadena2)))


print("ale" * 5)