

lista = [1,2,3,4,5,6,7]

lista.reverse()

print(lista)
2

print(len(lista))

lista.append(10) #metodo para agregar elementos a una lista --> se agrega al final 

print(lista)


lista.insert(2,8764) #se le pasa la posicion en donde queres agregar el elemento nuevo 

print(lista)

lista.remove(10) #metodo para remover elementos de una lista 

print(lista)

print(lista.count(1)) #cuantas veces aparece un elemento en una lista


#si quisiera definir el metodo count seria de la siguiente manera
def metodo_count(lista, valor):
    contador = 0
    for x in lista:
        if x == valor:
            contador+=1
    return contador

print(metodo_count(lista,0))

#si quisiera definir el metodo append seria de la siguiente manera
def metodo_append(lista,valor):
    lista = lista + [valor]
    return lista


print(lista.index(1)) #retorna el indice de la posicion donde se encuentra el valor pasado como parametro 
#en caso de que no este dicho elemento tira una excepcion 


lista.sort() #ordena la lista de forma ascendete 
lista.reverse() #ordena la lista de tras para atras, entonces si queremos ordenar de mayor a menor, debemos hacer un sort y luego un 
#reverse 

