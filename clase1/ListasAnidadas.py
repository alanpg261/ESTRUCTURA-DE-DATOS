'''
lista = [[5,6,7,8,9], [50,60,70,80,90]]  #DECLARAR LA LISTA ANIDADA POR ASIGNACIÓN
suma = 0
for i in lista:                          #RECORRER LA LISTA ANIDADA CON UN BUCLE FOR ANIDADO
    for j in i:                             
        suma += j                        #SUMAR LOS ELEMENTOS DE LA LISTA ANIDADA   
    print(suma)

suma1 = lista[0].sum()                                #SUMAR LOS ELEMENTOS DE LA PRIMERA SUBLISTA
suma2 = lista[1].sum()                                #SUMAR LOS ELEMENTOS DE LA SEGUNDA SUBLISTA
suma_total = suma1 + suma2                            #SUMAR LOS RESULTADOS DE AMBAS SUBLISTAS
print(suma_total)

lista = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]  #DECLARAR LA LISTA ANIDADA POR ASIGNACIÓN
suma = 0
for i in lista:                          #RECORRER LA LISTA ANIDADA CON UN BUCLE FOR ANIDADO
    for j in i:                             
        suma += j                        #SUMAR LOS ELEMENTOS DE LA LISTA ANIDADA
print(suma)

lista = [[100, 7, 85, 8],[4, 8, 56, 25], [67, 89, 23, 1],[78, 56]]
print(lista)

for i in range(len(lista[0])):
    if lista[0][i] > 50:
        lista[0][i] = 0
print(lista)
'''
lista = [[100, 7, 85, 8],[4, 8, 56, 25], [67, 89, 23, 1],[78, 56]]
print(lista)

for i in lista:
    for j in i:
        if j > 10:
            j = 0

print(lista)
