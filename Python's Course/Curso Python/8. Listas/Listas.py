#las listas pueden ser homogeneas o heterogeneas, es decir, son del mismo dato o no necesariamente 
#la lista de python es lo mismo que el array o vectores de otros lenguajes de programacion 
#las listas son mutables 

lista = ['Python', 120, 'Nombre', 4.14, 6.28]
lista1 = [1,2,True,3,4]


print(type(lista))

print(lista[3])

print(len(lista))


lista[0] = 'python' #de esta forma modifico una parte de la lista 

print(lista)