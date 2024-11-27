lista  = [1,5,2,7,9,32]

n = len(lista)
listaordenada = []
for posicion in range (n):

    for j in range (0, n - posicion - 1):
        if lista[j] < lista[j + 1]:
            listaordenada.append (lista[j+1])       

print(listaordenada)